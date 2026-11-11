# OMF2107 Feature List

Single list of committed features with milestone mapping. Sources: `DEVPLAN.md` (formerly `RELEASE_PLAN.md`, "RP"; wins on conflict, including the direction change of 2026-11-07), the task register inside it (IDs such as A02 and C06 come from the retired `OMF2097_DEVPLAN.md`, "DP"; R IDs are for the career layer), the spec (`OMF2107_GAME_SPEC.md`), the archived Reimagined pitch (`_archive/omf-reimagined-design-pitch-v0.3.md`, proposal numbers shown as #n for traceability only), and the code state found on 2026-11-07. "Milestone" is from DEVPLAN (RP/DP); "none" means no doc assigns one.

Milestones (RP, re-planned 2026-11-07): M0 2026-11-20, M1 2027-01-22, M2 2027-03-19, M3 2027-04-30 (career core), M4 2027-06-18, M5 2027-09-17, M6 2028-01-14, M7 2028-03-17.

## Modes

| Feature | Ruleset | Milestone | State |
|---|---|---|---|
| Story (ten routes, Nova conclusion, per-pilot endings) | `classic`; no economy, upgrades or damage | spec §6; RP M4 (Ari), M6 (rest) | Ari route built (`ari.story`, 266 scenes, passes story_check) |
| Arcade / One Player | `classic` plus disclosed tune-ups | RP Phase 4 playtest; DP D04 (P1) | Playable ladder for Ari, placeholder dialogue. See `OMF2107_ARCADE_MODE.md` |
| Tournament career | `career`; Model A; insolvency is game over | RP M3 (short bracket), M6 (full career); DP D05 | Not started |
| Training | Both | D03 (P1, task register) | Not audited |
| Options + key remapping | n/a | RP Phase 4 / M4; DP D07 (P1) | Not audited |
| Onboarding tutorial | `classic` | none | Unassigned |
| Local Versus | `classic` | RP "Later decisions" (moved 2026-11-07) | Not audited |
| Online play, console ports | n/a | deferred | Out of scope |

## Combat

- Fixed side-on plane, authored hit shapes, stun, knockdown, air hits, combos, original-style finish, learnable hazards.
- Destruction finishers only in the last round and only when the finisher is in good condition, in every mode (R15). In `classic`: every round won, none lost, each ended with at least 50% health. The AI follows the same rule and its destructions play in full.
- **Stun is the only combat resource** (no heat; #7 rejected).
- Shared rules for player and AI; difficulty 0 to 6 in code.
- Replays store inputs, game version and ruleset ID (DEVPLAN, Evidence table).
- Fidelity gate on `classic`: capture walk speed, jump arc, startup/recovery, hit/push distance, block response, stun and special behavior for Jaguar and one rival before tuning. 35 Jaguar and Shadow attacks measured so far (RP).

## Career layer (Tournament only)

| Feature | # | Milestone | Task |
|---|---|---|---|
| Region damage: 4 regions x 3 states, stun-centred numeric effects, no move removal, carried between rounds | #1 | M3 | R02 |
| Height-based region targeting; pre-match scouting | #13 | M3 | R03 |
| Destruction finishers: last round only, finisher in good condition | n/a | M3 (gate), M5 to M6 (sequences) | R15 |
| Damage visuals in both looks, no hurtbox change | #22 | M1 spike, M3 | R04, R05 |
| Repair ladder: full, patch, fight damaged; insurance | #2 | M3 | R06 |
| Persistent purse, HARs, upgrades and damage (Model A) | n/a | M3 | R06, D05 |
| Insolvency game over (negative after two consecutive matches), with warning; sponsor support near insolvency | #10 (minimal) | M3 | R06, R11a |
| Lower bracket after a routine loss | #3 | M3 | R08 |
| Economy simulation | n/a | M3 | R07 |
| Rivals with memory | #4 | M6 | D06 |
| One personality profile per opponent; AI pressures damaged regions | #5 (part) | M4 | R10a |
| Bounded adaptation to player habits | #5 | M6 | R10 |
| Full sponsors and contracts with a refusal path | #10, #16 | M6 | R11 |
| Rankings and circuit | #17 | M6 | D05 |
| Decide after M3 playtest | #24, #24a | n/a | n/a |

## Content

- Pilots: original ten, each with an ending; Kreissack as boss.
- HARs: original ten standard plus Nova as story boss. Unlock policy open (spec §13). Each HAR needs region masks and swap parts in both looks.
- Arenas: Stadium, Danger Room, Power Plant, Fire Pit, Desert.
- Story tools: skip and log required; critical evidence has alternate carriers.
- Presentation: portraits, short 2D scenes, in-engine scenes, dialogue panels; reduced flashes, shake and particles option.

## Platform

Windows first, Linux where practical. 60 fps presentation in both looks, damage effects included; budgets in `DEVPLAN.md`, "3D engine requirements". Minimum PC profile fixed at M3. Controller latency to be tested on hardware.

## Known doc conflicts (items 1, 5 and 6 are resolved; keep until the R14 re-check at M1)

1. **First slice.** Resolved 2026-11-07: Ari's route is the first complete story slice; Crystal vs Christian moves to Phase 4.
2. **HAR count.** Resolved by wording 2026-11-07: "ten standard HARs plus Nova as story boss". Assumes "All 11" meant ten plus Nova. Revert if an eleventh playable HAR was intended.
3. **Arcade and Training milestones.** Partly resolved 2026-11-07: Arcade's ruleset is decided and its live playtest sits in Phase 4. Training still has no milestone of its own.
4. **Content rating.** Spec/RP include consensual adult romance and fanservice frames with consent and skip required; no rating review is stated.
5. **Faithful remake vs Reimagined.** Resolved 2026-11-07: Reimagined direction on a parity foundation. The spec's design pillars and §7 were updated to match.
6. **Reimagined pitch.** Resolved 2026-11-09: archived; its rules still in force are in the spec (§4.4, §5, §7, §8).
