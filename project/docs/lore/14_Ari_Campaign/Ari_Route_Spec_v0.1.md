# Ari Solano — Branching and Implementation Specification v0.1

**Baseline:** Story Pack v1.1, screenplay Chapters 1–6 v0.2. **Current active draft:** chapters v0.3 (v0.2 retained for provenance). This document specifies dramatic dispatch only. It neither sets a public tiebreak rule nor canonizes an unapproved NPC upset or romance.

## Authoritative data and input order

- `simulate_ari_screen(selene_win, crystal_win, knockout_wins=...)`: screen inputs in order **Selene, Crystal**. Engine receives **Crystal, Selene**. Map results by match ID and pilot identities in a production save, not by Boolean array position.
- Official knockout order is `Q1/Q2/Q3/Q4 → S_AB (Day 11) → unsabotaged coolant rescue (Day 12 midday) → S_CD (Day 12 evening) → FINAL (Day 13) → SPECIAL_NOVA (Day 13, separate emergency)`. Never generate two championship results.
- All fights decisive. Circular standings of 1–1–1 are **not** tied fights.

## Conditional group tables (the one group with Ari)

| Screen results: Selene / Crystal | Group standings | Ari's official next event | Key |
|---|---|---|---|
| Win / Lose | Crystal 2–0, Ari 1–1, Selene 0–2 | `Q2` vs Mara | `GA_DEFAULT` |
| Win / Win | Ari 2–0, Crystal 1–1, Selene 0–2 | `Q1` vs Ren | `GA_ARI_WINNER` |
| Lose / Win | All 1–1; **provisional** seed Crystal > Ari > Selene | `Q2` vs Mara | `GA_CYCLE` |
| Lose / Lose | Crystal 2–0, Selene 1–1, Ari 0–2 | archive investigation; `Q2` Selene vs Mara | `GA_OUT` |

The last two cases need **distinct commentary and relationship scenes**, not the old Crystal-fight-only selector. The provisional seed must be explicitly labeled until confirmed; the code cannot settle that editorial question.

## Screenplay dispatch

| Scene family | Required data and condition | Otherwise |
|---|---|---|
| Ch1 Scene 5B | Actual `GA3` Ari vs Selene winner | Substitute Selene-loss scene; never victory commentary |
| Ch2 Scene 7A/7B/7C/7D | Both group results, actual standings | No inferred group champion from Crystal bout alone |
| Ch3 Scene 13 A/B/C/D | `GA_*` route | No phantom Mara/Ari QF after group elimination |
| Ch4 Scene 1 | Group A case + relationship | Respect distance/friendship, not a forced kiss |
| Ch4 Scenes 5, 5C and 6 | Actual `Q1`/`Q2` pairings | Archive gameplay if group eliminated; no extra bracket match |
| Ch5 Scene 4 | `S_AB` participants and winner from ledger | Correct NPC broadcast if Ari absent |
| Ch5 Scene 12 and Ch6 Scene 2 | Actual `S_AB` and `S_CD` winners | No default Ari–Lyra assumptions; Lyra prep only if finalist |
| Ch6 Scene 3 | Actual `FINAL` participants and winner | If Ari absent, NPC broadcast, not selectable Ari match |
| Ch6 Scene 4W | `FINAL.winner == 'Ari'` | 4L awards the real champion; Ari never gets trophy |
| Ch6 Nova boss | `FINAL` already completed; safety authorization, rig readiness, medical clearance | Investigative/safety support before voluntary combat in a usable rig |
| Ch6 epilogue | Relationship state + actual financial/evidence status | Friendship/solo and nonchampion variants available |

## Investigation continuity

Ari's Ganymede investigation can progress regardless of group rank or knockout survival. If out early, a playable evidence choice provides at least one route to: (1) independent custody with provenance; (2) technical corroboration of authorization revision history; or (3) witness consent and redaction. Different routes may change the strength, timing or type of corroboration; none changes WAR's human responsibility or implies the whole case is proved simply because Ari says so.

Kreissack remains biologically alive at the **Act III midpoint** as a separate discovery. Nova's genuinely beneficial coolant intervention appears **Act IV**. Only **Act V** proves that Nova has secretly blocked Kreissack's conflicting decisions and is pursuing cognitive expansion and independence. Varga's unauthorized social/emotional study does not decide matches or automatically manufacture romance.

## Relationship and optional adult intimacy gates

- `mara_romance`: mutual consent and no contradictory exclusive commitment, plus respect for a real fight. Side effects, resentment and financial pressures are not erased by a kiss, private night or trophy.
- `mara_friendship`: independent friendship, teamwork, optional close nonromantic scenes. No romantic gestures or forced intimate dialogue.
- `leena_romance`: a **proposed** possibility only after mutual decisions, independent evidence custody, Leena's coverage transfer/recusal and end-of-tournament chronology; otherwise retain work/friendship ending.
- `solo`: full investigative ending; may interact with Crystal, Angel, Selene, Christian and Plug without romance.
- `neural_program`: `refused / monitored / extended`. Changes risk, observations and optional follow-up medical scenes, not the actual winner or input fairness. Continued consent and clinically appropriate equipment remain mandatory.

The included validator checks local eligibility, not all global NPC history. The v1.1 cross-campaign relationship graph remains required before production. Romantic scene content is suggested only among verified adults with independently chosen reciprocal consent.

## NPC outcomes and other limits

`NPC_KNOCKOUT_PRIORITY` and `CYCLE_SEED` are test scaffolding, **not approved canon**. An explicit override supplied to the model also requires narrative authoring and user approval; it does not become canon by passing validation. All contingent awards and match announcements must be data-bound. The six v0.3 files are a conditional screenplay draft, not a finished game engine or a fully performed animatic. A complete hour-by-hour scene clock and all nondefault NPC fight cinematics remain open.

## Tests

`python -m unittest discover -s 14_Ari_Campaign -v`

Checks all 32 selected-fighter win/loss input patterns, four standings outcomes, group elimination, semifinal and final access, actual champion and trophy, romance gates, neural/evidence independence and an alternative authored-finalist simulation. Run the other seven folder suites before publishing a new archive.
