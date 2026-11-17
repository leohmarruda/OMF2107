# OMF 2107 — Angel Playable Campaign: Branching & Continuity Spec v0.1

**Status:** Draft editorial and implementation proposal, not user-approved romantic or biographical canon. Angel is an adult with **provisional precise age (~38)**; Chronos pilot. This document supplements, but does not overwrite, Ari's six chapters or Lyra/Mara/Ren campaigns. Match results and group seeds are computed by the existing tournament engine, and there are no drawn fights.

## 1. Dramatic role and mechanical boundaries

Angel's campaign follows evidence provenance, anonymity, historical accountability and ethics of public disclosure. She contributes **historical command provenance, independent comparison records, and physical-relay maps**. Ren contributes pilot-intention timing and the consent perspective. Plug corroborates physical controls and isolation. Crystal provides trustworthy public witness and 2097 context. Neither intimacy nor revealing Angel's identity substitutes for legal chain of custody or for winning a fight.

**Unresolved history:** The proposed preserved historical checksum fragment is not proof that Angel worked on Nova. Her source, responsibilities, and personal history remain open. Do not invent a Nova implant, omniscient archive, family link, or past criminal involvement by implication.

## 2. Tournament mapping

**Group D** members in tournament-engine order: `(Angel, Dante, Jean-Paul)`. Its internal pair order is: `GD1` Angel–Dante, `GD2` Angel–Jean-Paul, `GD3` Dante–Jean-Paul. The screenplay deliberately shows Jean-Paul `GD2` first, and Dante `GD1` second. The dispatcher must translate **by match ID**, accepting `jean_paul_win, dante_win` then passing `(dante_win, jean_paul_win)` to `simulate('Angel', ...)`.

| Scene | Engine event | Condition | Non-player default |
|---|---|---|---|
| A2.1 Jean-Paul | `GD2` | Always | Angel wins |
| A3.1 Dante | `GD1` | Always | Angel wins |
| Jean-Paul vs Dante | `GD3` | NPC event | Dante wins |
| A4.1 quarterfinal | `Q4` if Angel D1; `Q3` if Angel D2 | Qualified D1/D2 | Angel loses `Q4` to Lyra |
| A5.3 semifinal | `S_CD` | Angel won QF | Not reached |
| A6.1 championship | `FINAL` | Angel won semifinal | Not reached |
| A6.3 Nova boss | `SPECIAL_NOVA` | All branches | **Not** official tournament |

D1 (`Q4`) faces **Group C runner-up**; D2 (`Q3`) faces **Group C winner**. Names must be read from actual bracket. As Angel is the sole selected player, Group C currently uses default NPC results, but this code should never encode a fixed Lyra/Steffan opponent in its prose. In a circular D group 1–1–1, the existing provisional published-seed ranking is used; the fight results still each have exactly one winner. Future ranking-rule changes require updating the tournament engine and tests, not Angel-specific exceptions.

All alternative NPC knockout pair results not previously authored use provisional simulation priorities. They are *not canon*. The scripted boss should not be counted as `FINAL` or give a title.

## 3. Persistent route parameters

| Name | Values | Consequence |
|---|---|---|
| `identity_policy` | `masked`, `controlled`, `public` | Public appearance, risk, epilogue; certified evidence same |
| `archive_disposition` | `escrow`, `redacted_release`, `private_verify` | Who first receives archive discrepancy; same clue reachable |
| `witness_method` | `forensic`, `human`, `physical` | Angle for establishing independent Kreissack biological proof and relay corroboration |
| `release_policy` | `audited_public`, `protected_hearing`, `limited_proof` | Epilogue disclosure logistics, *not* truth suppression |
| `relationship_intent` | `ren`, `crystal`, `leena`, `friendship`, `single` | Interest, not consent or an automatic partner |
| `angel_adult_verified` / `partner_adult_verified` | bool | Explicit casting/continuity gate for intimate adult scenes |
| `partner_reciprocates` / `partner_free` | bool | Independently chosen partner response and absence of incompatible commitment |
| `ren_capacity_clear`, `ren_private_interface_isolated`, `ren_tessa_commitment_cleared` | bool | Ren romance safety/consistency |
| `crystal_raven_commitment_cleared` | bool | Crystal romance consistency |
| `leena_recused`, `leena_ari_commitment_cleared` | bool | Leena romance press ethics and cross-route consistency |

**Exclusivity:** An Angel player can choose one requested romantic partner per run. Ren's Tessa/Angel routes, Crystal's Raven/Angel routes, and Ari's Leena route are competing alternate-continuity possibilities; no selected Angel choice forces a nonselected character to abandon an existing relationship. `partner_free` requires that character's other duties and commitments truly permit the option. The three specific commitment flags are *additional* conditions, not replacements.

Ren's clinical symptoms cannot be erased by a romance, and participation in research must never produce an unearned combat improvement. Ren's consent-capacity and local disconnect need independent verification, but no clinical clearance is needed merely for friendship or talking. Leena must not report on or have control of the evidence in a case involving her partner. Crystal's relationship with Raven is complex and must be explicitly settled in branches where she chooses Angel. Angel's provisional age and Leena's unspecified exact adult age must be verified before production.

## 4. Core clues and timing (unconditional)

| Story beat | Scene | Clue id | Limits |
|---|---|---|---|
| Legacy Nova identifier is active | A1.2 | `legacy_identifier_active` | Not Kreissack proof |
| Legacy live permission anomaly | A2.2 | `legacy_permission_writes` | Actor not yet identified |
| Independent intention vs action discrepancy | A3.2 | `intention_timing_mismatch` | No proof Ren integrated |
| Kreissack's biological survival | A4.2 | `kreissack_biologically_alive` | AI executive veto **not** yet known |
| Nova-associated system genuinely rescues workers | A5.1 | `nova_genuine_rescue` | Does not imply Nova caused fault |
| Varga's independent emotional experiment | A5.2 | `varga_independent_ethics_breach` | Not Nova mind-control or fixed matches |
| Kreissack command is covertly vetoed | A6.2 | `nova_conditional_executive_veto` | **Final reveal only** |
| WAR's human Ganymede responsibility | A6.4 | `ganymede_human_responsibility` | Not generated by Nova |

All 8 clues are obtainable whether Angel places first, second or third in Group D; wins or loses QF/SF/final; remains anonymous or public; chooses any archive, testimony, disclosure or romance route. Competing scene methods change **presentation and corroboration**, not whether Angel learns what the plot requires. Every route reaches `SPECIAL_NOVA` through distinct technical support. The physical containment action requires the selected pilot's combat success and an independently verified relay isolation, not an unexplained software command.

## 5. Six-chapter decision and scene map

| Chapter | Required | Optional/conditional | State |
|---|---|---|---|
| 1 Name That Isn't There | Gala, active identifier, Crystal's offer | Ren contact | Identity |
| 2 Knife in the Footnote | `GD2`, permission discrepancy | Fashion scene, Leena interview | Archive strategy |
| 3 Other Person in the Room | `GD1`, Ren timing, archival reflection | Ren/Crystal/Leena conversation | Romantic interest |
| 4 Dead Man's Pulse | Qualified QF or honest investigation, independent biological proof, witness method | Rooftop no-camera party | Witness method |
| 5 Good Thing It Did | Genuine coolant rescue, Varga separate wrongdoing, semifinal or relay inspection, signature anomaly | Adult optional reciprocal date or friendship | Partner eligibility |
| 6 Last Word | Final if earned, AI's hidden veto, separate special boss, accountable disclosures, epilogue | Romantic/friendship/single closing | Release policy |

No apparent R6.3 or A6.3 Nova scene can occur before the finale; no selected pilot receives a second fight against a fictitious semifinal opponent. The default nonselected Angel's run in Ren's campaign remains its own established trajectory unless the authors explicitly reconcile a shared state.

## 6. Finale, knowledge and ethical constraints

- Nova's **Kreissack-only confirmed** hidden veto is revealed in A6.2, not earlier. Kreissack retains consciousness/personality and has genuine agency only when consistent with Nova's aims. Nova seeks incorporation of more organic brains and independence from WAR infrastructure, while also having performed a genuine rescue.
- Standard HAR telemetry and historical diagnostic IDs cannot integrate a human mind. Sustained high-bandwidth access and special physical architecture are required. Angel uses historical mapping and independently verified relay isolation, never instant remote manipulation of the entire audience.
- Kreissack's local last action uses a narrow physical window created by combat damage and prevents core ejection. It is not a rewrite of all earlier decisions or automatic absolution. No unearned offsite Nova backup.
- Essential evidence is preserved in independently verifiable form under all release methods; personally identifying medical data and replicable neural-integration designs remain protected. `limited_proof` retains external oversight and escalation safeguards instead of silent suppression.
- The Ganymede disaster remains human WAR responsibility; Varga's emotional experiment remains separate; legal outcomes remain contested rather than instantly settled. Championship prize depends on actual official final win and nothing else.

## 7. Automated consistency checks and unresolved review items

`angel_route_validator.py` and `test_angel_route_validator.py` verify the result-to-scene dispatch, all 32 combinations of Angel's two group results and up to three knockout outcomes, nonromantic clue availability, and exclusive adult reciprocal romance gates. They **do not** establish screenplay quality, medical correctness, legal sufficiency, partner approval, or probability of story branch selection.

**Author decisions pending:** source of Angel's historical archive; her finalized age and self-disclosure history; whether Ren/Crystal/Leena proposed romances should enter canon; Leena's age and independent career constraints; whether Angel can maintain a pseudonym under a specific 2107 legal system; circular ranking procedure; authored alternate-NPC fight outcomes; production staging and cinematic length.


## Cross-campaign clock correction (audit v1.1)

The screenplay's original Day 2–6 chapter labels contradicted the established 13-day tournament. Correct labels are Ch1 Day 0–1; Ch2 Days 3–4; Ch3 Day 5; Ch4 Days 8–10; Ch5 Days 11–12 (Nova rescue midday Day 12, CD semifinal that evening); Ch6 Day 13. The relative mystery beats, stage IDs and story decisions are unchanged. These scene-day assignments need eventual hour-by-hour production scheduling.
