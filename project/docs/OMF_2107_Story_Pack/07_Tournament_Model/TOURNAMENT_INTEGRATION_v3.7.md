# Tournament score tiebreak / scene binding — v3.7

## Approved author decisions

- **D1:** The game tracks match scores; use scores to rank circular 1–1–1 groups. Working assumption: each fighter has a recorded numeric score in each group battle; sum of two group-stage scores is the first tiebreak. Do not confuse combat score with points for match wins. Different scoring schemes or impossible comparisons require revisiting this assumption.
- **D2:** NPC-only knockout matches use deterministic authored **exact-pair** results. Do not extrapolate a total power ordering. The 66-pair explicit proposal table is a **review worksheet**; its individual winners are not approved canon or justified by the scripts.

## Required score interface

`group_match_scores: {"GA1": (score_of_left_fighter, score_of_right_fighter), ...}`; other IDs are `GA2–3`, `GB1–3`, `GC1–3`, `GD1–3`. `left/right` come from each group's `itertools.combinations` order in `GROUPS`. Numbers are finite and nonnegative. Scores for a circular group must cover all three matches. When only two totals tie, their head-to-head result breaks the tie. If all three totals tie, strict mode throws pending a tertiary rule. No fictitious scores are filled into the default storyline. Tiebreak calculations apply only where win records equal 1–1–1.

**Open design decisions:** score definition and scale (especially CPU-vs-CPU results), three-way equal total scores, whether any anti-farming normalization is necessary, and per-match recorded scores in canonical default fights. Avoid using historical provisional seeding in production.

## NPC result approval process

`npc_pair_proposals.py` lists all 66 unordered pairs for editorial assessment; default seven exact-pair results already override it. **These suggested winners were generated as a starting worksheet and are not supported by character-specific fight evidence.** Review every reachable alternate pairing against fighting styles, arcs, previous fights, and cinematic consequences. Only move individually approved outcomes into `npc_knockout_winners` for strict validation. No randomness or implicit winner-by-strength ranking in production.

## Script binding

`build_scene_state(simulation_result)` returns `champion`, `finalists`, `semifinalists`, `selected_pilot_elimination`, `selected_pilot_is_champion`, `group_rankings`, `official_tournament_over_before_nova`, and `audit`. Every conditional trophy reference, opponent name, tournament success scene and Day-13 entrance must use this state or a verified equivalent. Gameplay scoring affects only bracket placement; it never changes the established Day-13 core destruction mechanism.

## Editorial screen audit

`ACTIVE_TOURNAMENT_REFERENCE_REVIEW_v3.7.csv` records keyword-screened references in the current active scripts. These are candidates, **not verified contradictions**. Selene's stale provisional fallback note was corrected in the active v0.5 script. Other lines require scene-level editorial inspection before changes.
