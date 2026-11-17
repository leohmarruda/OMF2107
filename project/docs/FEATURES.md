# Mecha Link 2100 feature list

Single list of committed features with milestone mapping. Sources: `DEVPLAN.md` (formerly `RELEASE_PLAN.md`, "RP"; wins on conflict, including the direction change of 2026-11-07), the task register inside it (IDs such as A02 and C06 come from the retired `OMF2097_DEVPLAN.md`, "DP"; R IDs are for the career layer), the spec (`GAME_SPEC.md`), the archived Reimagined pitch (`_archive/omf-reimagined-design-pitch-v0.3.md`, proposal numbers shown as #n for traceability only), and the code state found on 2026-11-07. "Milestone" is from DEVPLAN (RP/DP); "none" means no doc assigns one.

Milestones (RP, re-planned 2026-11-07): M0 2026-11-20, M1 2027-01-22, M2 2027-03-19, M3 2027-04-30 (career core), M4 2027-06-18, M5 2027-09-17, M6 2028-01-14, M7 2028-03-17.

## Modes

| Feature | Ruleset | Milestone | State |
|---|---|---|---|
| Story (about ten routes, boss conclusion, per-pilot endings) | `classic`; no economy, upgrades or damage | spec §6; RP M4 (Ari), M6 (rest) | Ari route built in the original game's world (`ari.story`, 266 scenes, passes story_check); text to be rewritten for the new setting (R23, M4) |
| Arcade / One Player | `classic` plus disclosed tune-ups | RP Phase 4 playtest; DP D04 (P1) | Playable ladder for Ari, placeholder dialogue. See `ARCADE_MODE.md` |
| Tournament career | `career`; Model A; insolvency is game over | RP M3 (short bracket), M6 (full career); DP D05 | Not started |
| Training | Both | D03 (P1, task register) | Not audited |
| Options + key remapping | n/a | RP Phase 4 / M4; DP D07 (P1) | Not audited |
| Onboarding tutorial | `classic` | none | Unassigned |
| Local Versus | `classic` | RP "Later decisions" (moved 2026-11-07) | Not audited |
| Online play, console ports | n/a | deferred | Out of scope |

## Combat

- Fixed side-on plane, authored hit shapes, stun, knockdown, air hits, combos, dramatic finish, learnable hazards.
- Destruction finishers only in the last round and only when the finisher is in good condition, in every mode (R15). In `classic`: every round won, none lost, each ended with at least 50% health. The AI follows the same rule and its destructions play in full.
- **Stun is the only combat resource** (no heat; #7 rejected).
- Four attack buttons (S1, S2, C1, C2) and a universal S1 + C1 grab with an escape window; three standard special-command families (decided 2026-11-17; R24, M1 spike, M2). State: not built; the prototype still has one punch and one kick.
- Mecha attributes Power, Agility, Resistance (1 to 10, 18 points), authored per mecha (R25, M2).
- Five special traits (camouflage, counter, flight, modular weapons as a fixed move set, energy shield) and twelve power subtypes acting through stun and component damage only (R26, M2 first traits, M5 to M6 the rest).
- Geometry model (pushboxes, component hurtboxes, timed hitboxes, universal grab at any size, appendage rules): proposed 2026-11-17 by the design team, R28, M1 to M2. Gravity arenas with a descent rule, flight limits and projectile rules: proposed, open (R29, R30; see DEVPLAN open decisions).
- Details in `COMBAT_UPGRADE.md`; the shared design document for the external team is `GAME_MECHANICS.md`.
- Shared rules for player and AI; difficulty 0 to 6 in code.
- Replays store inputs, game version and ruleset ID (DEVPLAN, Evidence table).
- Baseline for `classic`: walk speed, jump arc, startup/recovery, hit/push distance, block response, stun and special behavior are measured on the OpenOMF scaffold for two contrasting roles (35 Jaguar and Shadow attacks so far), then re-authored and tuned for the new mechas. Every difference from the baseline is a recorded decision (DEVPLAN, "Independence").

## Career layer (Tournament only)

| Feature | # | Milestone | Task |
|---|---|---|---|
| Component damage (the four regions, named after each mecha's anatomy): 4 components x 3 states, stun-centred numeric effects, no move removal, carried between rounds | #1 | M3 | R02, R27 |
| Height-based region targeting; pre-match scouting | #13 | M3 | R03 |
| Destruction finishers: last round only, finisher in good condition | n/a | M3 (gate), M5 to M6 (sequences) | R15 |
| Damage visuals in both looks, no hurtbox change | #22 | M1 spike, M3 | R04, R05 |
| Repair ladder: full, patch, fight damaged; insurance | #2 | M3 | R06 |
| Persistent purse, mechas, upgrades and damage (Model A) | n/a | M3 | R06, D05 |
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

- Pilots: an original cast of about ten, each with an ending, plus an antagonist. All new; the original game's pilots are placeholders only.
- Mechas: an original roster of about ten standard mechas plus a story boss, each from a written brief. Unlock policy open (spec §13). Each mecha needs component masks and swap parts in both looks, attributes, a trait list and a move set on four buttons. Roster archetypes proposed in `COMBAT_UPGRADE.md` (section 7); the design team's guide now lists 17 candidates (the mecha design guide), from which about ten plus a boss are chosen.
- Arenas: about five original arenas, each with one hazard.
- Story tools: skip and log required; critical evidence has alternate carriers.
- Presentation: portraits, short 2D scenes, in-engine scenes, dialogue panels; reduced flashes, shake and particles option.

## Platform

Windows first, Linux where practical. 60 fps presentation in both looks, damage effects included; budgets in `DEVPLAN.md`, "3D engine requirements". Minimum PC profile fixed at M3. Controller latency to be tested on hardware.

## Known doc conflicts (items 1, 5 and 6 are resolved; keep until the R14 re-check at M1)

1. **First slice.** Resolved 2026-11-07: Ari's route is the first complete story slice; Crystal vs Christian moves to Phase 4.
2. **Mecha count.** Reset 2026-11-11: about ten standard mechas plus a story boss, an original roster whose size is set by the roster plan (checklist D2), not by the original game's eleven.
3. **Arcade and Training milestones.** Partly resolved 2026-11-07: Arcade's ruleset is decided and its live playtest sits in Phase 4. Training still has no milestone of its own.
4. **Content rating.** Spec/RP include consensual adult romance and fanservice frames with consent and skip required; no rating review is stated.
5. **Faithful remake vs Reimagined.** Resolved 2026-11-07 (Reimagined), superseded 2026-11-11: the game is independent, with OpenOMF as a scaffold and measured baseline. The spec was rewritten (v0.4).
6. **Reimagined pitch.** Resolved 2026-11-09: archived; its rules still in force are in the spec (§4.4, §5, §7, §8).
7. **Setting and story.** Open (R23): the Story row describes the legacy route in the original game's world. It is rewritten in the new setting for M4.
