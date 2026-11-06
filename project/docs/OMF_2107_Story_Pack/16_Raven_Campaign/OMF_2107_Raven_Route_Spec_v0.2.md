# OMF 2107 — Raven route specification v0.1

**Baseline:** v1.3 + explicitly author-set Raven dark characterization (2026-11-01). **Status:** First-pass Raven POV dispatcher, scene conditions and cross-route compatibility proposal; not a production state engine.

## 1. Canon and agency

- `enjoys_exploiting_crystal = True` is **character truth**, not a player reward, a variable that can be turned off, or proof of Crystal's consent. He may delight in making her hesitate or comply, and a player may choose manipulation, threats, evidence trading or isolation attempts. These are harmful choices, not secretly consensual romantic play.
- `crystal_involuntary_pull_to_raven = True` remains author-set. She can reject a relationship, report coercive behavior, and independently investigate. Existing Crystal v1.3 draft's morally considerate Raven represents a **possible restrained branch**, not guaranteed baseline behavior. Revised Crystal v0.2 script covers dark alternatives.
- `sexual_boundary`: if no specific freely given consent, there is no D/s intimacy; in exploitation paths there is no erotic reward. Raven's manipulative impulses can shape a noir thriller without glamorizing a violation.
- The route does not determine Crystal's affection, Mara's availability, or the Devroe shuttle cause from Raven's preferences. Real accountability and NPC decisions are separate inputs.

## 2. Tournament contract

| Screen event | Match | Opponent | Engine outcome order | Default |
|---|---|---|---|---|
| R2.1 | `GB2` | Mara | 1 | Lose |
| R2.3 | `GB3` | Ren | 2 | Lose |

Other B match is Mara beats Ren (`GB1`). B standings: `LL` → B3; `WL` → B3 (circular 1–1–1, provisional `Mara > Ren > Raven`); `LW` → B2; `WW` → B1. **These are decisive individual matches; the circular standing is not a draw.** Raven B2 faces A1 in `Q1`; Raven B1 faces A2 in `Q2`. If QF win → `S_AB` Day 11; if SF win → `FINAL` Day 13; only final winner receives trophy. `SPECIAL_NOVA` occurs afterward and is not official competition. The nondefault NPC priority system and circular ranking are provisional.

## 3. Route choices and resulting incident ledger

| Choice | Values | Effect |
|---|---|---|
| `gala_behavior` | `probe`, `withhold`, `admit` | `probe` and `withhold` register manipulation incidents (no evidence advantage) |
| `money_choice` | `refuse`, `take_advance`, `counsel_copy` | `take_advance` registers corrupt payment; independent sources survive |
| `shuttle_statement` | `full`, `selective`, `false_denial` | `false_denial` registers deceit; disclosure completeness affected |
| `crystal_pressure` | `exploit`, `bargain`, `disclose`, `leave` | `exploit` and `bargain` register predatory behavior; no romantic payoff |
| `hearing_response` | `testify`, `limited`, `obstruct` | `obstruct` registers misconduct; independently authenticated evidence survives |
| `final_offer` | `refuse`, `accept_trace`, `obstruct` | Accepted bribe or obstruction registers misconduct; cannot change Nova rescue |
| `relationship_intent` | `crystal`, `mara`, `friendship`, `single` | Player **intent** only; does not establish a reciprocal commitment |
| `nova_attitude` | `oppose`, `envy_but_oppose`, `try_bargain` | Changes dialogue and risk, not whether Nova has a genuine rescue or executive veto |

**Conservative v0.1 romance gate**: Crystal–Raven only if `crystal` intent; no recorded manipulation, corrupt-payment, false-denial or obstruction incidents; full statement + testimony + independently verified disclosure; both are free; reciprocal independent adult interest; `chooses_ds`, `limits_agreed`, `crystal_active_consent`, `raven_active_consent` all true. This is stricter than a possible later route allowing fully documented repair: the latter requires new scenes and an explicit, independent NPC decision, not a checkbox.

**Mara gate**: `mara` intent, Raven free, Mara adult and free, mutually interested, Crystal relationship clearly closed, and no attempt to buy cooperation with sponsorship. A morally suspect Raven can still flirt; a romance cannot be generated from money, tournament success, or a unilateral player option. This pairing is a **proposal**.

**Ending dispatch:** `crystal_consensual_ds`, `crystal_refuses_or_unavailable`, `mara_romance`, `mara_friendship_only`, `friendship`, `single`; `dark_exposed` supersedes a romantic intention when an incident ledger contains predatory or obstructive conduct, but it is **not** a judgment that every ethically suspect person is unable to have relationships. It represents the concrete narrative response in this draft.

## 4. Global event order

| Chapter/scene | Day | Information Raven can know |
|---|---|---|
| R1.* | 0–1 | Old Nova diagnostic echoes, shuttle file custody suspicion |
| R2.* | 3–7 | Group standings and independently preserved suspicious contract |
| R3.* | 6–8 | Shuttle custody index and legacy permission anomaly; NOT biological survival proven |
| R4.1–R4.3 | 8–10 | Real QF if qualified, biological survival confirmed, shuttle concealment corroborated |
| R5.1 | 11 | Real S_AB if earned |
| R5.2 | 12 midday | Genuine Nova rescue; attribution mismatch, not yet independent veto proof |
| R5.3–R5.4 | 12 | Conditional private intimacy or boundary violation; off-bracket S_CD that evening |
| R6.1 | 13 | Real final and actual champion |
| R6.2 | 13 postfinal | Conditional covert Nova veto and composite biological-brain expansion revealed |
| R6.3 | 13 postfinal | Separate Nova emergency; authorized Raven or support role |
| R6.4–R6.5 | weeks later | Court/relationship outcomes; Devroe murder mechanism established; courtroom disposition open |

### Mandatory clue trail

`shuttle_custody_gap`, `legacy_nova_identifier`, `protected_kreissack_life_support`, `nova_genuine_rescue`, `nova_attribution_mismatch`, `nova_conditional_executive_veto`, `biological_brain_expansion`, `ganymede_human_accountability`, `varga_separate_study` are reachable on **every** path. Revelation flags aren't dependent on romance, match result, payment or Raven's cooperation. The **independent investigation** may advance when Raven withholds evidence; it is not the same as Raven receiving a clue through impossible privileged access.

## 5. Scene conditions

| Scene | Condition | Fallback |
|---|---|---|
| R1.1, R1.2, R1.3 | always | — |
| R1.4, R3.3, R4.4 | optional | none; clues still supplied elsewhere |
| R2.1, R2.2, R2.3, R2.4 | always | engine-recorded two matches |
| R3.1, R3.2, R3.4 | always, intimacy never automatic | no private encounter if Crystal refuses meeting; public accountability dialogue |
| R4.1 | B1/B2 and QF | R4.1_NO_QF evidence audit |
| R4.2, R4.3 | always | independent corroboration if Raven refuses cooperation |
| R5.1 | QF winner | R5.1_NO_SF witness debrief |
| R5.1B | always, Day 11 before Nova rescue | Independent emergency request receipt and Raven acknowledgment |
| R5.2, R5.4 | always | — |
| R5.3 | optional, Day 12 informed confrontation only, no private intimacy | Raven alone or neutral mediated notice |
| R6.1 | SF winner | R6.1_SPECTATE |
| R6.2, R6.3, R6.4, R6.5 | always | alternate Nova role if no access; any intimate route only post-hearing |

## 6. Outstanding matters

1. Cross-POV **single global world state** is still proposed rather than implemented. Crystal cannot be both Raven's available partner and committed to Angel in the same save. Optional Raven–Mara needs mutual decision, not a naked boolean.
2. Devroe shuttle: causation and Raven's three historic acts resolved in working story canon v1.5 (`02_Story_Bibles/Devroe_Shuttle_Case_Canon_v1.5.md`). The kill-order signatory and legal disposition remain open. A romance is never a pardon.
3. The rule for circular group standings and nondefault NPC winners are not approved canon.
4. A future full model should track specific manipulation incidents, acknowledgments, accountability process and **Crystal's autonomous decisions over time** instead of reducing harm to a romance boolean. A more complex repair ending must be written, not unlocked by a soft score.
5. Exact medical/technical Nova emergency authorization and partner timeline require coordinated production pass. Running tests cannot certify literary quality or NPC agency.

## v1.5 override — locked 2092 past, contingent 2107 accountability

The full historical facts must remain reachable in every branch (see `17_Devroe_Case/Devroe_Scene_Packet_v1.5.md`). Raven's `shuttle_statement` changes his **2107 testimony**, never 2092 behavior. `R5.1B` must reveal the ignored restoration request after the independent receipt is authenticated. `R5.3` on Day 12 is an **informed conversation only**; an adult private D/s scene, if any, belongs in the post-hearing epilogue when the family knows the facts and separate boundaries are negotiated.
