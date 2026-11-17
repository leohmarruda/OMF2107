#!/usr/bin/env python3
"""OMF 2107 tournament route validator (Python 3.10+, stdlib only).

All fights are decisive. Circular 1-1-1 groups use tracked cumulative scores
when complete; a recorded uniform random draw resolves exact three-way score ties.
Legacy seeding remains a test-only fallback for missing score data.
Unapproved NPC-only knockout outcomes are never canon by implication.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import secrets
from typing import Dict, List, Sequence, Tuple

GROUPS = {
    "A": ("Crystal", "Ari", "Selene"),
    "B": ("Mara", "Ren", "Raven"),
    "C": ("Steffan", "Lyra", "Milano"),
    "D": ("Angel", "Dante", "Jean-Paul"),
}
# Historical provisional order, used ONLY for non-strict simulations lacking scores.
CYCLE_SEED = {
    "A": ("Crystal", "Ari", "Selene"),
    "B": ("Mara", "Ren", "Raven"),
    "C": ("Steffan", "Lyra", "Milano"),
    "D": ("Angel", "Dante", "Jean-Paul"),
}
DEFAULT_GROUP_WINNERS = {
    frozenset(("Crystal", "Ari")): "Crystal",
    frozenset(("Crystal", "Selene")): "Crystal",
    frozenset(("Ari", "Selene")): "Ari",
    frozenset(("Mara", "Ren")): "Mara",
    frozenset(("Mara", "Raven")): "Mara",
    frozenset(("Ren", "Raven")): "Ren",
    frozenset(("Steffan", "Lyra")): "Steffan",
    frozenset(("Steffan", "Milano")): "Steffan",
    frozenset(("Lyra", "Milano")): "Lyra",
    frozenset(("Angel", "Dante")): "Angel",
    frozenset(("Angel", "Jean-Paul")): "Angel",
    frozenset(("Dante", "Jean-Paul")): "Dante",
}
# Default cinematic bracket, recorded in the existing model's reference path.
# A result applies only when this exact pairing occurs; altered pairings remain unapproved.
DEFAULT_KNOCKOUT_WINNERS = {
    frozenset(("Crystal", "Ren")): "Crystal",
    frozenset(("Ari", "Mara")): "Ari",
    frozenset(("Steffan", "Dante")): "Steffan",
    frozenset(("Angel", "Lyra")): "Lyra",
    frozenset(("Crystal", "Ari")): "Ari",
    frozenset(("Steffan", "Lyra")): "Lyra",
    frozenset(("Ari", "Lyra")): "Ari",
}
# Draft NONCANONICAL fallback for pairs without an authored NPC result.
# The order reproduces all default bracket results; revise with the route scripts.
NPC_KNOCKOUT_PRIORITY = (
    "Ari", "Lyra", "Crystal", "Steffan", "Mara", "Angel", "Ren", "Dante",
    "Selene", "Raven", "Milano", "Jean-Paul",
)



def generate_group_tie_draw(group: str) -> tuple[str, str, str]:
    """Uniformly sample one of the 3! orders using system randomness.

    Save the order in the tournament event ledger *before* using it for
    standings. Reloads must replay the recorded order, never redraw.
    """
    if group not in GROUPS:
        raise ValueError(f"Unknown group for tie draw: {group}")
    order = list(GROUPS[group])
    secrets.SystemRandom().shuffle(order)
    return tuple(order)


def simulate(
    selected_pilot: str,
    group_wins: Sequence[bool],
    knockout_wins: Sequence[bool],
    *,
    cycle_seed: Dict[str, Tuple[str, ...]] | None = None,
    npc_knockout_winners: Dict[frozenset, str] | None = None,
    require_authored: bool = False,
    group_match_scores: dict[str, tuple[float, float]] | None = None,
    use_proposed_npc: bool = False,
    tie_draws: dict[str, Sequence[str]] | None = None,
) -> dict:
    """Run a branch with selected pilot's binary win/loss inputs.

    group_wins: exactly 2 booleans, corresponding to selected pilot's group
                match order in combinations(GROUPS[group], 2).
    knockout_wins: up to 3 booleans, consumed when selected pilot actually
                   contests QF, SF and Final; extra values are ignored when
                   pilot is eliminated. Must supply enough if they advance.
    NPC knockout results: explicit pair mapping wins over proposals and test-only priority.
    group_match_scores: G[A-D][1-3] -> (left_score, right_score),
        using GROUPS combination order; numeric scores must be finite and >= 0.
        In circular groups, totals of each fighter's two scored fights rank fighters.
    use_proposed_npc: opt into the review-pending explicit pair table.
    tie_draws: already-recorded random orders for exact three-way score ties.
        Generate once via generate_group_tie_draw and persist to game state.
        In strict mode an unrecorded draw cannot silently be regenerated.

    """
    all_pilots = {p for fighters in GROUPS.values() for p in fighters}
    if selected_pilot not in all_pilots:
        raise ValueError("Unknown selected pilot")
    if len(group_wins) != 2 or any(type(x) is not bool for x in group_wins):
        raise ValueError("group_wins must be exactly two booleans")
    if len(knockout_wins) > 3 or any(type(x) is not bool for x in knockout_wins):
        raise ValueError("knockout_wins must contain at most three booleans")

    seeds = CYCLE_SEED if cycle_seed is None else cycle_seed
    npc_results = {} if npc_knockout_winners is None else npc_knockout_winners
    if set(seeds) != set(GROUPS):
        raise ValueError("Cycle seed policy must define all four groups")
    for group, fighters in GROUPS.items():
        if len(seeds[group]) != 3 or set(seeds[group]) != set(fighters):
            raise ValueError(f"Invalid cycle seed for group {group}")
    for pair, winner in npc_results.items():
        if not isinstance(pair, frozenset) or len(pair) != 2 or not pair <= all_pilots or winner not in pair:
            raise ValueError(f"Invalid NPC knockout override: {pair!r} -> {winner!r}")
    score_inputs = {} if group_match_scores is None else group_match_scores
    valid_group_ids = {f"G{g}{i}" for g in GROUPS for i in range(1, 4)}
    if not isinstance(score_inputs, dict) or set(score_inputs) - valid_group_ids:
        raise ValueError("Unknown group match score keys")
    for mid, score in score_inputs.items():
        if not isinstance(score, (tuple, list)) or len(score) != 2 or any(
            type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in score
        ):
            raise ValueError(f"Invalid group match score for {mid}")
    recorded_draws = {} if tie_draws is None else tie_draws
    if not isinstance(recorded_draws, dict) or set(recorded_draws) - set(GROUPS):
        raise ValueError("Unknown three-way tie draw group")
    for group, order in recorded_draws.items():
        if (not isinstance(order, (tuple, list)) or len(order) != 3
                or len(set(order)) != 3 or set(order) != set(GROUPS[group])):
            raise ValueError(f"Invalid recorded three-way tie draw for group {group}")
    proposed = {}
    if use_proposed_npc:
        from npc_pair_proposals import PROPOSED_PAIR_WINNERS
        proposed = PROPOSED_PAIR_WINNERS
    priority = {p: i for i, p in enumerate(NPC_KNOCKOUT_PRIORITY)}
    matches = []
    standings = {}
    used_group = 0
    used_ko = 0
    circular_groups = []
    unresolved_score_groups = []
    applied_random_tie_draws = {}
    proposed_npc_matches = []

    def record(match_id: str, left: str, right: str, winner: str, origin: str):
        if left == right or winner not in (left, right):
            raise ValueError(f"Invalid decisive match {match_id}: {left} vs {right}, winner {winner}")
        matches.append({"id": match_id, "left": left, "right": right,
                        "winner": winner, "loser": right if winner == left else left,
                        "resolution": origin})
        return winner

    for group, fighters in GROUPS.items():
        wins = {p: 0 for p in fighters}
        matchups = list(itertools.combinations(fighters, 2))
        total_scores = {p: 0.0 for p in fighters}
        score_complete = True
        for i, (left, right) in enumerate(matchups, start=1):
            if selected_pilot in (left, right):
                selected_won = group_wins[used_group]
                used_group += 1
                winner = selected_pilot if selected_won else (right if left == selected_pilot else left)
                origin = "player_result"
            else:
                winner = DEFAULT_GROUP_WINNERS[frozenset((left, right))]
                origin = "authored_default_group"
            mid = f"G{group}{i}"
            record(mid, left, right, winner, origin)
            wins[winner] += 1
            if mid in score_inputs:
                a_score, b_score = score_inputs[mid]
                total_scores[left] += a_score
                total_scores[right] += b_score
                matches[-1]['scores'] = {left: a_score, right: b_score}
            else:
                score_complete = False

        if sorted(wins.values()) == [1, 1, 1]:
            circular_groups.append(group)
            published = seeds.get(group)
            if not published or set(published) != set(fighters) or len(published) != 3:
                raise ValueError(f"No valid published cycle seed for {group}")
            if score_complete:
                # Head-to-head is well defined for exactly two fighters tied in
                # cumulative score. A three-way score tie remains unresolved,
                # since the underlying 1-1-1 match cycle has no H2H winner.
                score_buckets = {}
                for fighter in fighters:
                    score_buckets.setdefault(total_scores[fighter], []).append(fighter)
                if max(map(len, score_buckets.values())) <= 2:
                    head_to_head = {
                        frozenset((m['left'], m['right'])): m['winner']
                        for m in matches if m['id'].startswith(f'G{group}')
                    }
                    order = []
                    for score in sorted(score_buckets, reverse=True):
                        bucket = score_buckets[score]
                        if len(bucket) == 2:
                            winner = head_to_head[frozenset(bucket)]
                            bucket = [winner, next(f for f in bucket if f != winner)]
                        order.extend(bucket)
                    ranking_method = ('group_total_score_then_head_to_head'
                                      if len(score_buckets) < 3 else 'group_total_score')
                else:
                    # The score totals are equal across all three; the
                    # head-to-head results form a cycle, so replay the once-
                    # recorded independent draw instead of a seeded ranking.
                    order = list(recorded_draws[group]) if group in recorded_draws else None
                    if order is not None:
                        ranking_method = 'recorded_uniform_random_draw'
                        applied_random_tie_draws[group] = order.copy()
            else:
                order = None
            if order is None:
                unresolved_score_groups.append(group)
                if require_authored:
                    raise ValueError(f"Unapproved circular-group score resolution (scores missing or tied; three-way tied totals require a recorded random draw) for group {group}")
                order = list(published)
                ranking_method = 'provisional_seed_NOT_CANON' 
        elif sorted(wins.values()) == [0, 1, 2]:
            order = sorted(fighters, key=lambda p: -wins[p])
            ranking_method = 'match_wins' 
        else:
            raise AssertionError(f"Unexpected three-player decisive standings: {wins}")
        standings[group] = {"ranked": order, "wins": wins,
                            "score_totals": total_scores if score_complete else None,
                            "ranking_method": ranking_method,
                            "circular_1_1_1": group in circular_groups}

    a, b, c, d = (standings[group]["ranked"] for group in "ABCD")
    def knockout(match_id, left, right):
        nonlocal used_ko
        if selected_pilot in (left, right):
            if used_ko >= len(knockout_wins):
                raise ValueError(f"Missing selected pilot outcome for {match_id}")
            selected_won = knockout_wins[used_ko]
            used_ko += 1
            winner = selected_pilot if selected_won else (right if left == selected_pilot else left)
            origin = "player_result"
        elif frozenset((left, right)) in npc_results:
            winner = npc_results[frozenset((left, right))]
            origin = "authored_npc_override"
        elif frozenset((left, right)) in DEFAULT_KNOCKOUT_WINNERS:
            winner = DEFAULT_KNOCKOUT_WINNERS[frozenset((left, right))]
            origin = "authored_default_knockout"
        elif frozenset((left, right)) in proposed:
            winner = proposed[frozenset((left, right))]
            proposed_npc_matches.append(match_id)
            origin = 'proposed_npc_pair_PENDING_APPROVAL'
            if require_authored:
                raise ValueError(f"Missing approved NPC result for {match_id}: {left} vs {right}")
        else:
            if require_authored:
                raise ValueError(f"Missing authored NPC result for {match_id}: {left} vs {right}")
            winner = min((left, right), key=lambda p: priority[p])
            origin = "provisional_npc_priority_NOT_CANON"
        return record(match_id, left, right, winner, origin)

    q1 = knockout("Q1", a[0], b[1]); q2 = knockout("Q2", a[1], b[0])
    q3 = knockout("Q3", c[0], d[1]); q4 = knockout("Q4", d[0], c[1])
    s1 = knockout("S_AB", q1, q2); s2 = knockout("S_CD", q3, q4)
    champion = knockout("FINAL", s1, s2)
    selected_matches = [m for m in matches if selected_pilot in (m["left"], m["right"])]
    selected_ko_losses = [m for m in selected_matches if not m["id"].startswith("G") and m["loser"] == selected_pilot]
    qualified = any(selected_pilot in standings[g]["ranked"][:2] for g in GROUPS)
    provisional_matches = [m["id"] for m in matches if m["resolution"] == "provisional_npc_priority_NOT_CANON"]
    result = {"selected_pilot": selected_pilot,
              "group_standings": standings, "circular_groups": circular_groups,
              "matches": matches, "champion": champion,
              "recorded_random_tie_draws": applied_random_tie_draws,
              "player_champion": champion == selected_pilot,
              "player_match_ids": [m["id"] for m in selected_matches],
              "player_elimination_match": (selected_ko_losses[-1]["id"] if selected_ko_losses else ("GROUP_STAGE" if not qualified else None)),
              "selected_pilot_advances_from_group": qualified,
              "used_group_results": used_group, "used_knockout_results": used_ko,
              "nova_encounter": "SEPARATE_FROM_OFFICIAL_BRACKET",
              "audit": {
                  "unapproved_cycle_seed_groups": unresolved_score_groups,
                  "recorded_random_tie_draws": applied_random_tie_draws,
                  "provisional_npc_match_ids": provisional_matches,
                  "proposed_npc_match_ids": proposed_npc_matches,
                  "canon_ready": not provisional_matches and not proposed_npc_matches and not unresolved_score_groups,
              }}
    validate(result)
    return result


def validate(result: dict) -> None:
    """Reject impossible schedules or indecisive match data."""
    matches = result["matches"]
    if len(matches) != 19:  # 12 group fights + 4 QF + 2 SF + 1 final
        raise AssertionError("Wrong number of official matches")
    if len({m["id"] for m in matches}) != 19:
        raise AssertionError("Duplicate match IDs")
    for m in matches:
        if m["left"] == m["right"] or m["winner"] not in (m["left"], m["right"]):
            raise AssertionError("Match without exactly one valid winner")
        if m["loser"] not in (m["left"], m["right"]) or m["loser"] == m["winner"]:
            raise AssertionError("Match without exactly one valid loser")
    for group, players in GROUPS.items():
        group_matches = [m for m in matches if m["id"].startswith(f"G{group}")]
        if len(group_matches) != 3:
            raise AssertionError("Each group must have three matches")
        if sorted(p for m in group_matches for p in (m["left"], m["right"])) != sorted(players * 2):
            raise AssertionError("Each group participant must fight twice")
    if matches[-1]["winner"] != result["champion"]:
        raise AssertionError("Champion must win official final")


def main():
    p = argparse.ArgumentParser(description="Validate decisive OMF 2107 tournament routes")
    p.add_argument("--pilot", default="Ari", choices=NPC_KNOCKOUT_PRIORITY)
    p.add_argument("--group-wins", default="01", help="Two binary outcomes; 1=pilot wins")
    p.add_argument("--knockout-wins", default="111", help="Up to three binary outcomes")
    p.add_argument("--brief", action="store_true")
    args = p.parse_args()
    if len(args.group_wins) != 2 or set(args.group_wins) - set("01"):
        p.error("--group-wins requires exactly two 0/1 digits")
    if len(args.knockout_wins) > 3 or set(args.knockout_wins) - set("01"):
        p.error("--knockout-wins accepts at most three 0/1 digits")
    result = simulate(args.pilot,
                      tuple(x == "1" for x in args.group_wins),
                      tuple(x == "1" for x in args.knockout_wins))
    if args.brief:
        result = {k: result[k] for k in ("selected_pilot", "champion", "player_match_ids",
                                         "circular_groups", "player_elimination_match")}
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
