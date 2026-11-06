#!/usr/bin/env python3
"""Ari selected-pilot screenplay dispatcher.

Inputs are *screen order* (Selene, Crystal). Outcomes are sourced from the
single authoritative tournament. Nondefault NPC results still use the legacy
provisional fallback unless explicitly supplied by an author: NOT CANON.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Mapping, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "07_Tournament_Model"))
from tournament_validator import simulate  # noqa: E402

GROUP_CASES = {
    (True, False): "GA_DEFAULT",
    (True, True): "GA_ARI_WINNER",
    (False, True): "GA_CYCLE",
    (False, False): "GA_OUT",
}


def simulate_ari_screen(
    selene_win: bool,
    crystal_win: bool,
    knockout_wins: Sequence[bool] = (),
    *,
    npc_knockout_winners: Mapping[frozenset[str], str] | None = None,
    romance: str = "solo",  # mara_romance | mara_friendship | leena_romance | solo
    mara_reciprocal: bool = False,
    leena_reciprocal: bool = False,
    leena_recused: bool = False,
    neural_program: str = "refused",  # refused | monitored | extended
    evidence_approach: str = "independent_custody",  # custody | technical | witness
) -> dict:
    if type(selene_win) is not bool or type(crystal_win) is not bool:
        raise ValueError("Screen results must be Boolean wins/losses, not drawn bouts")
    if romance not in {"mara_romance", "mara_friendship", "leena_romance", "solo"}:
        raise ValueError("Invalid romance selection")
    if neural_program not in {"refused", "monitored", "extended"}:
        raise ValueError("Invalid neural program choice")
    if evidence_approach not in {"independent_custody", "technical_review", "witness_privacy"}:
        raise ValueError("Invalid evidence choice")
    if romance == "mara_romance" and not mara_reciprocal:
        raise ValueError("Ari interest does not establish Mara's reciprocal consent")
    if romance == "leena_romance" and not (leena_reciprocal and leena_recused):
        raise ValueError("Leena romance requires reciprocal interest and post-coverage recusal")
    # Engine group order is Crystal then Selene, not the on-screen order.
    result = simulate(
        "Ari", (crystal_win, selene_win), knockout_wins,
        npc_knockout_winners=dict(npc_knockout_winners or {}),
    )
    by_id = {m["id"]: m for m in result["matches"]}
    case = GROUP_CASES[(selene_win, crystal_win)]
    rank = result["group_standings"]["A"]["ranked"].index("Ari") + 1
    assert (rank <= 2) == result["selected_pilot_advances_from_group"]
    assert (case == "GA_OUT") == (rank == 3)
    assert (case == "GA_CYCLE") == ("A" in result["circular_groups"])

    player_knockouts = [m for m in result["matches"] if
                        not m["id"].startswith("G") and "Ari" in (m["left"], m["right"])]
    qf = player_knockouts[0] if player_knockouts and player_knockouts[0]["id"].startswith("Q") else None
    sf = next((m for m in player_knockouts if m["id"] == "S_AB"), None)
    final = by_id["FINAL"]
    in_final = "Ari" in (final["left"], final["right"])
    if in_final != (sf is not None and sf["winner"] == "Ari"):
        raise AssertionError("An Ari finalist must have won the A/B semifinal")
    if in_final and not final["resolution"] == "player_result":
        raise AssertionError("Selected Ari final must be player-contested")
    if not in_final and final["resolution"] == "player_result":
        raise AssertionError("Eliminated Ari cannot control the official final")

    book = ["A1_ARI_BEATS_SELENE" if selene_win else "A1_ARI_LOSES_TO_SELENE",
            "A2_ARI_BEATS_CRYSTAL" if crystal_win else "A2_ARI_LOSES_TO_CRYSTAL",
            "A2_" + case, "A3_" + case + "_DRAW"]
    events = [
        {"day": 3, "key": "SELENE_MATCH", "result": "ARI_WIN" if selene_win else "SELENE_WIN"},
        {"day": 5, "key": "CRYSTAL_MATCH", "result": "ARI_WIN" if crystal_win else "CRYSTAL_WIN"},
        {"day": 8, "key": "DRAW", "group_case": case, "ari_rank": rank},
    ]
    if qf:
        book.append("A5_ARI_QF_WIN" if qf["winner"] == "Ari" else "A5_ARI_QF_LOSS")
        events.append({"day": 9, "key": qf["id"], "left": qf["left"],
                       "right": qf["right"], "winner": qf["winner"]})
    else:
        book.append("A4_GROUP_OUT_ARCHIVE_INVESTIGATION")
        events.append({"day": 9, "key": "ARCHIVE_INVESTIGATION", "route": evidence_approach})
    if sf:
        book.append("A6_ARI_SEMIFINAL_WIN" if sf["winner"] == "Ari" else "A6_ARI_SEMIFINAL_LOSS")
    else:
        book.append("A6_ARI_ABSENT_FROM_SEMIFINAL")
    events.append({"day": 11, "key": "S_AB", "left": by_id["S_AB"]["left"],
                   "right": by_id["S_AB"]["right"], "winner": by_id["S_AB"]["winner"]})
    events.extend([
        {"day": 12, "key": "COOLANT_RESCUE", "fact": "unsabotaged_accident_beneficial_ai_intervention"},
        {"day": 12, "key": "S_CD", "left": by_id["S_CD"]["left"],
         "right": by_id["S_CD"]["right"], "winner": by_id["S_CD"]["winner"]},
    ])
    if in_final:
        book.append("A7_ARI_FINAL_WIN" if result["player_champion"] else "A7_ARI_FINAL_LOSS")
        book.append("A7_ARI_TROPHY" if result["player_champion"] else "A7_OTHER_TROPHY")
    else:
        book += ["A7_NPC_FINAL_BROADCAST", "A7_OTHER_TROPHY"]
    events.append({"day": 13, "key": "FINAL", "left": final["left"],
                   "right": final["right"], "winner": final["winner"],
                   "playable_by_ari": in_final})
    # No boss gate on sporting progression; access requires medical clearance and safety authorization
    # in scene text and cannot silently force an unsafe neural interface.
    events.append({"day": 13, "key": "SPECIAL_NOVA", "official_match": False,
                   "access": "safety_authorized_manual_or_medically_cleared"})
    book.extend(["A8_NOVA_EMERGENCY", "A9_EPILOGUE_" + romance.upper()])
    events.append({"day": 20, "key": "EPILOGUE", "relationship": romance})

    provisional = sorted(m["id"] for m in result["matches"]
                         if m["resolution"] == "provisional_npc_priority_NOT_CANON")
    return {
        "screen_group_wins": {"Selene": selene_win, "Crystal": crystal_win},
        "group_case": case,
        "ari_group_rank": rank,
        "qualified": qf is not None,
        "qf_id": qf["id"] if qf else None,
        "qf_opponent": (qf["right"] if qf["left"] == "Ari" else qf["left"]) if qf else None,
        "sf_played_by_ari": sf is not None,
        "ari_finalist": in_final,
        "champion": final["winner"],
        "finalists": (final["left"], final["right"]),
        "ari_receives_trophy": result["player_champion"],
        "player_elimination_match": result["player_elimination_match"],
        "romance": romance,
        "neural_program": neural_program,
        "evidence_approach": evidence_approach,
        "scene_keys": book,
        "events": events,
        "provisional_npc_match_ids": provisional,
        "npc_results_ready_for_canon": False,  # author-supplied override is not proof of user approval
        "uses_npc_test_fallback": bool(provisional),
        "tournament": result,
    }
