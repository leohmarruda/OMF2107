# Tournament-to-screenplay reconciliation v3.8

## Scope and verified fixes

This pass examines the 166 references previously harvested from the 18 active screenplay files. These are keyword candidates; the full list is preserved as `TOURNAMENT_REFERENCE_TRIAGE_v3.8.csv`. A keyword hit cannot certify a contradiction. The new triage separates default-context references from other candidates and records a confirmed branch-dependent staging defect.

1. **Confirmed, corrected:** The Ari campaign's Chapter 6, Scene 4L previously required Crystal to award the trophy to the actual winner even when the winner was Crystal. The active screenplay now gates the presenter: Crystal presents to another champion, while an authorized awards official presents when Crystal wins. The exact official identity remains unassigned, not a new story character.
2. **Confirmed, corrected:** Ari Chapter 4 labeled Mara beating Crystal as a “proposed alternate default.” This is an unapproved NPC pairing outcome, not a competing default. The active screenplay now makes that distinction explicit and requires ledger binding.
3. **Previously conditional, retained:** Campaigns generally gate their quarterfinal, semifinal, final, and championship honor by the selected protagonist's real bracket state. Do not replace those established gates with hard-coded canonical defaults.

## New automated scene bindings

`tournament_scene_state.build_scene_state()` now exposes an exact official `matches_by_id` ledger, `final_is_playable`, `played_knockout_ids`, `final_winner`, and a `ceremony_presenter_rule` alongside prior placement, champion and ranking state. Those outputs are **integration contracts**, not a script-engine runtime. The scene engine still needs to consume these bindings explicitly.

## Approved tie policy and residual ambiguity

For circular 1–1–1 group standings: rank by each fighter's sum of tracked group-battle scores. If **exactly two** fighters have the same total, use their decisive head-to-head match as a secondary tiebreaker. A **three-way total-score tie** cannot be resolved by head-to-head (the wins themselves form a cycle); strict mode rejects it pending an approved tertiary rule. Missing scores also fail strict mode. Score semantics and CPU score comparability still require confirmation.

## Remaining editorial blockers

- Approval of individually proposed winners for reachable alternate NPC-only knockout pairings; method approval is not winner approval.
- The 166 candidate references need a complete human line-by-line narrative review, including their surrounding scenes. This release does not claim 166 independently verified conditions.
- For nondefault final opponents, several branches explicitly require authored opponent-specific lines; generic placeholders are not finalized dialogue.
- The scripting runtime must connect ledger-based conditions to all 12 campaigns, including ceremony, opponent portraits, elimination speeches and prize effects.
- Three-way equal score groups need a published tertiary procedure that is both implementable and consistent with the tournament's schedule.

## Regression

`test_tournament_score_tie_v38.py` checks two-way tiebreaks, strict three-way-tie failure and missing-score provenance. `test_tournament_scene_state_v38.py` checks championship gating, winner-dependent presenter and ledger consistency. No tournament winner was newly canonized.
