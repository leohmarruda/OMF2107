# OMF 2107 — Crystal route specification v0.1

**Baseline:** v1.2. **Status:** First-pass campaign dispatcher and production gating contract. New Crystal–Raven submissive orientation is author-specified in the 2026-11-01 request; its consensual enactment is a branch. Other new scene details remain proposals.

## 1. Core distinction: felt submission versus consent

- `involuntary_pull_to_raven = true` is **characterization**, not a random outcome, secret brain link, loss of capacity, or an “obedience meter.” It may be visible in C1.2 even in a solo or alternate romantic ending.
- `chooses_private_ds` is a player decision. `raven_reciprocates`, `raven_free`, `crystal_free`, `raven_disclosure_verified`, `limits_agreed`, `crystal_active_consent`, `raven_active_consent` are separate requirements for an enacted consensual D/s romantic ending. Any failed gate means **no active D/s scene**, while the felt attraction remains canon.
- Agreement is granular, revocable and confined to specific private interaction. It cannot compel speech, legal decisions, evidence withholding, familial estrangement, tournament outcomes, neural participation or restricted-access approvals.
- Raven's sworn testimony and evidence chain never imply he is absolved of concealed wrongdoing. Crystal's attraction gives him no license to shape or suppress the investigation. Independent verification proceeds on every path.
- Proposed alternative Crystal–Angel: only with adulthood, mutual romance choice, Crystal/Raven prior commitment settled, Angel free and no concurrent Angel–Ren/Angel–Leena commitment. If declined, friendship remains.
- **One save, one POV and one exclusive commitment graph**; cross-run choices never rewrite NPC partner decisions. The boolean prototype gates are test scaffolds, not evidence that NPC consent was scripted.

## 2. Tournament and stage mapping

Group A participant order (`Crystal`, `Ari`, `Selene`):

| Screenplay scene | Match ID | Opponent | Screen input position | Engine group position | Default selected result |
|---|---|---|---|---|---|
| C2.1 | `GA2` | Selene | 1 | 2 | win |
| C2.3 | `GA1` | Ari | 2 | 1 | win |

Nonplayer Ari–Selene (`GA3`) is an authored default Ari win for a Crystal POV. `simulate_crystal_screen(selene_win, ari_win, ...)` passes `(ari_win, selene_win)` to the common model. For a circular 1–1–1 Group A, provisional public seed sorts Crystal > Ari > Selene; this is not a drawn fight. Every fight is decisive. If Crystal rank A1 she enters `Q1` versus B2; if A2, `Q2` versus B1; if A3, no QF. QF win → S_AB Day 11; SF win → FINAL Day 13. Final opponent and official champion come from actual tournament results, never default dialogue or intimacy. Alternate NPC knockout results lacking author decisions are explicitly `provisional_npc_priority_NOT_CANON`.

**Default:** Crystal GA2 win, GA1 win, Q1 vs Ren win, S_AB vs Ari loss; no official final, Ari champion. **Nondefault possibilities:** early elimination, other QFs, SF win, final loss/win. `SPECIAL_NOVA` after official final is always separate, unranked.

## 3. Narrative state and relationship guards

`CrystalChoices` fields:

| Dimension | Choices / requirements | Scope |
|---|---|---|
| `shuttle_method` | `independent_archive`, `protected_deposition`, `victim_family_inquiry` | Independent evidence presentation, not facts based on Raven affection |
| `reform_policy` | `conditional_council`, `outside_watchdog`, `public_witness` | Endings affect practical coalition, not match results |
| `relationship_intent` | `raven`, `angel`, `friendship`, `single` | Exactly one requested primary relationship |
| `chooses_private_ds` | bool | Optional chosen *enactment*, not the felt involuntary pull |
| `raven_reciprocates`, `raven_free`, `crystal_free` | bool | Independent mutual desire and eligibility |
| `raven_disclosure_verified` | bool | Independent material deposition; **not innocence** |
| `limits_agreed`, `crystal_active_consent`, `raven_active_consent` | bool | Specific D/s adult relationship gates |
| `angel_adult_verified`, `angel_reciprocates`, `angel_free`, `raven_relationship_cleared` | bool | Alternative romance and cross-save exclusivity |

`interpret()` never returns an active Raven romance unless all seven necessary conditions hold and the relationship intent is Raven, even if Crystal instinctively yields to him in dialogue. A failed Raven eligibility yields `raven_unresolved`, indicating **no committed relationship or intimate scene**. A failed Angel eligibility yields `angel_friendship_only`; neither denotes romantic commitment. If `relationship_intent='friendship'` or `single`, that ending is honored.

## 4. Mandatory plot clue sequence, independent of romance and fighting

| Earliest phase | Evidence / fact | Forbidden premature inference |
|---|---|---|
| Ch1 | Nova legacy diagnostic / altered custody metadata suspicion | Kreissack alive established |
| Ch2 | independent Devroe shuttle custody gap | Raven's precise culpability / exoneration |
| Ch3 | legacy permission discrepancy | Nova covertly controls Kreissack |
| Ch4 | independently established biological survival | Full Nova autonomous motive |
| Ch5 (Day 12) | accidental fault; **genuine** Nova rescue; attribution anomaly | Nova caused accident or is wholly benevolent |
| Ch6 (after final) | Nova secretly vetoes Kreissack's conflicting decisions; brain integration motive | Ganymede human responsibility erased |
| Ch6 | physical `SPECIAL_NOVA` separate from bracket; vetted emergency access | Official champion determined by boss |
| Independent across phases | Ganymede human culpability; Varga's separate study | Neural romance, deliberate match fixing |

The independent shuttle evidence always reaches investigators. Raven may cooperate, evade or face consequences; his disclosure affects a **relationship gate**, never whether Crystal can learn that records were withheld. Raven's legal culpability is not conclusively decided in this campaign.

## 5. Scene dispatch

| ID | Guard | Variant |
|---|---|---|
| C1.2 | unconditional | She feels involuntary submissive response, acts on nothing automatically |
| C2.1/C2.3 | unconditional | Real GA2/GA1 outcome |
| C2.2 | optional | Explicit permission for a benign training correction or independent coach |
| C3.2 | optional | Discuss limits, say no or leave without romance penalty |
| C4.1 | rank <=2 | Real Q1/Q2; if A3 investigation instead |
| C4.2/C4.3 | all | independent biological survival and shuttle accountability |
| C4.4 | optional | Angel affinity without guaranteed reciprocity |
| C5.1 | QF win only | Real S_AB, always before rescue |
| C5.1B | all, Day 11 | Independently authenticated ignored distress request; no fight or romance gate |
| C5.2 | all, Day 12 | genuine rescue, command mismatch |
| C5.3 | Day 12 confrontation optional (noncoercive Raven; Crystal autonomously attends) | No intimacy. If she declines, separate family/investigation scene |
| C6.1 | SF win only | Actual FINAL opponent, trophy to winner |
| C6.2/C6.3 | all, postfinal | Nova veto reveal and separate boss |
| C6.5 | exactly one resolved ending | Raven D/s, attraction without reunion, Angel, friendship/solo |

## 6. Outstanding design work

1. **Resolved in working sequel canon v1.5:** see Devroe case bible. The senior kill-order signatory, legal disposition and whether a restored distress channel could have saved the ship remain open, not Raven's historic acts.
2. Approve or reject the proposed Angel alternative, including Angel's verified adulthood and true independent agency.
3. Implement a single real-time shared character relationship graph and consent timeline instead of boolean gate inputs.
4. Finalize circular group ranking policy and full authored nondefault NPC knockout outcomes.
5. Confirm exact hour-by-hour investigator and safety corridor access schedule, including how a previously eliminated Crystal receives emergency authorization.
6. Perform line-by-line editorial voice review and cinematic pacing pass. Python checks verify branch outputs only, not creative quality or sex-positive representation.

## v1.5 Devroe override

The independent investigation proves Raven signed a civilian distress-relay blackout, failed to restore it during the emergency and falsified later evidence; human flight-control sabotage directly killed the parents. Neither Crystal's relationship intent nor Raven's current testimony chooses these historical facts. Her Day 12 private scene is **confrontation only**; `C5.3_CONSENSUAL_DS` is superseded by `C5.3_INFORMED_NO_INTIMACY`. `C5.1B` is a mandatory independent emergency-message deposition. An eligible romantic encounter can occur **only in the post-hearing epilogue**, with Crystal independently informed, Raven's sworn complete account, and no coercion. The Raven–Crystal attraction continues in all branches.
