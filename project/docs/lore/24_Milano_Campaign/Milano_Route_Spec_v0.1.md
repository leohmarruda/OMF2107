# Milano Angston — cinematic route contract v0.1 (Story Pack v2.5)

## 1. Scope and authority

This route has one selected pilot, **Milano**, and uses `07_Tournament_Model/tournament_validator.py` as the sole official fight authority. Cinematic prose is subordinate to the simulator's actual result. Other campaigns are *alternative saved timelines*, not concurrent champions. Local booleans are **test assertions or integration inputs**, not proof that an off-player NPC has chosen romance. The default story remains unchanged.

## 2. Official matches and screen-input adapter

Group C engine combinations: `GC1` Steffan–Lyra (default Steffan), `GC2` Steffan–Milano, `GC3` Lyra–Milano. The **screenplay displays GC3 first, GC2 second**. Invoke `simulate_milano(lyra_win, steffan_win, knockout_wins)`; it calls shared `simulate('Milano', (steffan_win, lyra_win), knockout_wins)`.

| Screen wins (Lyra, Steffan) | Group C rank | Qualification | First knockout |
|---|---:|---|---|
| `00` | 3 | No | — |
| `10` | 2 | Yes | Q4 vs D1 |
| `01` | 3 | No; circular 1–1–1 | — |
| `11` | 1 | Yes | Q3 vs D2 |

*No draws*: `01` produces equal 1–1 **standings**, provisionally resolved by published rank Steffan–Lyra–Milano. This rule needs author sign-off. If QF played and won, `S_CD` is Day 12 (after the genuine Nova rescue), and `FINAL` Day 13 only if semifinal was won. Actual names and outcomes from match objects. NPC alternative knockout fallback is marked `provisional_npc_priority_NOT_CANON`.

## 3. Mandatory story anchors

1. MA1.3 — original authorization restricted neural trials under safeguards; Milano supported it, but did not knowingly sign the later unauthorized use.
2. MA2.2, MA3.3, MA4.2 — missing independent supervision, procedural waiver, documented escalation; he contributes **governance evidence**, not supplier identification (Selene) or neural causality (Angel/Ren).
3. MA4.3 Day 9 — independent discovery of Kreissack **biologically alive**, not proof of AI dominance or the Devroe assassination authorization.
4. MA5.1 Day 11 — Varga unauthorized emotion study publicly implicated, separate from Milano's waiver inquiry. If present, `S_CD` Day 12 after the rescue.
5. MA5.2 Day 12 — genuine Nova lifesaving action + false Kreissack command attribution; MA5.3 S_CD follows the rescue if qualified. Distinguish from a staged attack or confirmed control takeover.
6. MA6.1 Day 13 — only championship participant who actually won S_CD may fight in final; actual winner takes trophy.
7. MA6.2 Day 13 — gateway incapacitated through independent action; Nova's conditional control of Kreissack revealed; he takes irreversible physical retention-latch action. Shared last line exact and composite core destroyed. Official tournament already over; boss not rematch.
8. MA6.5 Day 30 — Christian independently authenticates Kreissack's signed 2092 Devroe assassination order, after the finale. Milano may only *hear of* it if disclosed; he does not authenticate it himself.

## 4. Player agency and institutional aftermath

`public_stance`, `authorization_position`, `investigation`, `review`, `board_strategy`, `institutional_ending` affect trust, legitimacy, documentation access within normal jurisdiction, accountability, board dynamics and epilogues. They **cannot** change past authorization, opponent outcome, rescue/corpse status, correct evidence, Nova's core destruction or other protagonists' autonomous decisions. Paths:

- `independent_reform`: independent review, record preservation, recusal; possible loss of office.
- `managed_reform`: partial oversight, retained influence, remaining transparency problems.
- `consolidate`: attempt to exploit emergency to obtain executive authority, credible dissent and future exposure; neither owns nor saves Nova.

An investigation remains playable for a group-stage loser. Shielding paperwork may damage Milano's credibility but does not erase copies held by external investigators.

## 5. Relationships

Default has **no new committed relationship for Milano**. Cossette and Milano have a casual fling, while Cossette and Ibrahim remain a steady couple; this is not a second Milano commitment or a Cossette breakup. The social/status imbalance (Milano substantially higher status) must not turn into transactional pressure or control over Cossette’s work. Their consensual-non-monogamy arrangement permits the connection, but its specific negotiated terms are not authored here. Milano–Selene is an established flirtatious corporate rivalry, not a confirmed couple. A romance ending requires *all*: Milano and Selene adults; both available and actively consenting; Selene independently and explicitly chooses Milano (including in her POV when selected); mutual attraction/reciprocity; enough time after the crisis; no other exclusive bonds; no blackmail, trade of data, threats or conflicts of power/financial dependence; business negotiations and material contractual leverage separated. A Milano player's unilateral `relationship_intent='selene'` produces only `selene_unresolved` absent proof of these facts. No relationship gives exclusive evidence. If Jean-Paul–Selene is active, this route is blocked unless the relationship ends through separately authored independent events. `normalized_pairs` from the existing cross-campaign model is an additional guard and not automatically integrated.

Other adult characters (Crystal, Ari, Mira) have meaningful professional, adversarial or supportive scenes without implied romance. Cossette and Ibrahim retain independent technical and personal agency regardless of Milano’s casual connection with Cossette. Glamour, machine spectacle and potential sensuality are optional and do not dominate the fighting-game campaign.

## 6. Open editorial decisions

- Approval of new secondary aide **Mira**, the detailed waiver sequence, and specific board-room dialogue. Sorell and Haldane remain in their established roles, not silently rewritten.
- Approval of Milano's three governance endings and the precise financial/legal consequences.
- Approval of a reciprocal Milano–Selene endpoint; both POVs must converge and preserve Selene's actual identity-disclosure and contractual choices.
- Finalize group circular seed and nondefault NPC knockout outcomes. 
- General project debt: shared persistent relationship state remains partial, and many alternate NPC matches need authored fight choreography. Tests check constraints, not pacing or chemistry.

## 7. Reproducibility

`python 00_README/run_all_tests.py` from pack root enumerates all `unittest` files. `test_milano_route_validator.py` includes all **32** combinations of two on-screen group inputs and three knockout inputs; unused knockouts are ignored after elimination. The suite checks round order, scene gates, nonromantic defaults, reciprocal romance, evidence timing and independent conclusions.
