# OMF 2107 — Ren Playable Campaign: Branching and Continuity Spec v0.1

**Status:** Editorial proposal, not approved final canon; pairs with `Ren_Playable_Screenplay_v0.1.md` and the existing executable tournament model. Ren is 25, uses they/them, pilots Helix. No official fight has a draw. New supporting character Tessa Kade (30) and romantic outcomes are provisional.

## 1. Distinct dramatic role

Ren's player story is about genuine technological promise, independent research, informed consent, self-worth, and the difference between *being assisted* and *being subordinated*. It must not mimic Ari's Ganymede investigation, Mara's family finance conflict, or Lyra's public-image story. Ren provides independent **pilot intention timing, documented informed-consent concerns, and relay-authorization evidence**. Angel handles historical log forensics, Plug handles physical isolation, Crystal supplies 2097 context, and others do not become redundant.

## 2. Tournament map and input-order trap

Group B consists of `(Mara, Ren, Raven)`. The engine's two Ren group input booleans are in order **versus Mara (`GB1`) first, then versus Raven (`GB3`)**, because it traverses lexicographic pair combinations of the group tuple. The screenplay presents **Raven (`GB3`) first, Mara (`GB1`) second**. Always capture actual match results by match ID, never chronological position. The supplied helper accepts `(raven_win, mara_win)` then supplies `(mara_win, raven_win)` to the engine.

| Scene | Match ID | Condition | Default result when Ren is NPC |
|---|---|---|---|
| R2.1 vs Raven | `GB3` | Always | Ren wins |
| R3.1 vs Mara | `GB1` | Always | Ren loses |
| R4.1 quarterfinal | `Q2` if B1, `Q1` if B2 | Ren qualifies top two | Ren loses to Crystal in `Q1` |
| R5.3 semifinal | `S_AB` | Ren wins QF | None |
| R6.1 final | `FINAL` | Ren wins SF | None |
| R6.3 Nova | `SPECIAL_NOVA` | Every route | Separate post-tournament boss |

The actual opponent is derived from the bracket. If Ren is B3, no knockout scenes are staged, no fictional trophy is assigned, and Ren still reaches the Nova confrontation through the independently recorded relay evidence. In a circular three-way 1–1 group, the existing published-seed fallback is provisional **and does not create drawn fights**. Nondefault NPC matchups also use openly provisional outcomes until authored or substituted.

## 3. Route variables

| Variable | Allowed values | When set / effect |
|---|---|---|
| `research_path` | `withdraw`, `audited`, `persist_safeguarded` | Ch3; affects research trust/exposure/epilogue, never combat stats |
| `symptom_disclosure` | `full`, `limited`, `concealed` | Ch2; concealment requires corrective disclosure before more participation |
| `corrected_disclosure` | bool | Ch3/5 repair; not a cure |
| `evidence_method` | `offline_record`, `witness_protocol`, `hardware_isolation` | Ch4; alters Ren's special-boss support role |
| `relationship_intent` | `angel`, `tessa`, `friendship`, `single` | Ch3/5; signals interest, not partner agreement |
| `angel_reciprocates` / `tessa_reciprocates` | bool | Separate response from other character; never assumed |
| `consent_capacity_clear` | bool | No acute impairment, ability to consent, supported by independent clinical and personal circumstances |
| `private_interface_isolated` | bool | Independent local disconnect before physical romantic intimacy, not an assurance that all risks have vanished |
| `angel_current_commitment_cleared` | bool | Crystal/Angel proposals in other stories cannot become an incompatible ongoing commitment |

A player's interest is never equivalent to consent from Angel or Tessa. Existing histories: Angel is adult (exact age **provisional**), mutual intellectual affinity with Ren is established; Tessa is a **new proposed adult civilian** with her own interests and no NII clinical authority. Friendship and single outcomes must always remain available. Romance options are exclusive unless a separate explicitly mutually negotiated relationship design is approved (none is in v0.1). Lyra/Ren romance is not implemented in this draft; Lyra remains a friend, and her other campaign's relationship decisions are not silently rewritten.

If `research_path=persist_safeguarded`, advanced sessions still require genuine clearance and independent oversight; a romance can occur only after an independently verified local isolation and unimpeded, alert consent. Concealment blocks resumption of deep research until repaired, **but does not automatically deny Ren all friendship or affection**.

## 4. Essential clue paths (ungated)

1. `executive_write_field_missing` — revised consent record at R1.2, even without NII enrollment.
2. `unexplained_permission_escalation` — R2.2 independent trace regardless of disclosure.
3. `intention_command_mismatch` — R3.2 independently recorded evidence, even after withdrawal.
4. `kreissack_biological_survival` — R4.3 Angel/Crystal/independent medical confirmation.
5. `nova_beneficial_rescue` — R5.1 accidental coolant fault, genuine rescue, no evidence Nova caused it.
6. `varga_emotional_experiment` — R5.4 distinct unauthorized human research.
7. `ganymede_human_responsibility` — separate WAR chain in R6.4, not Nova manipulation.
8. `nova_conditional_override` — R6.2 *finale only*: original Kreissack intention and suppressed motor authorization compared on independent logs; gradual human-brain incorporation requires sustained high-bandwidth access.

Relationships add voice and perspective, **never exclusive evidence access**. `withdraw` leaves historical recorded anomalies; `audited` adds independently observed checks; `persist_safeguarded` may contribute records but is not necessary. No early scene should assert proven full assimilation or Nova's final hidden veto.

## 5. Romance eligibility and scenes

- Angel route: `relationship_intent=angel`, `angel_reciprocates`, `angel_current_commitment_cleared`, `consent_capacity_clear`, and `private_interface_isolated`. Ch3/4 tension builds trust; Ch5 first optional kiss, Ch6 mutually chosen partnership or friendship. She retains independent professional and privacy boundaries.
- Tessa route: `relationship_intent=tessa`, `tessa_reciprocates`, `consent_capacity_clear`, `private_interface_isolated`. She is an independent accessibility choreographer, aged 30, not an investigator or researcher. The Ch5 optional dance/kiss is her choice too.
- Friendship: Angel technical friendship, Tessa civilian friendship, or close ensemble community are complete arcs; single is never a bad ending.
- If guards fail, show a respectful, non-intimate variant and later follow-up, not an instant invalid choice or automatic sexuality-based penalty. No acute episode scene turns medical vulnerability into romantic persuasion. Professional access and evidence cannot be purchased by intimacy.

## 6. Finale and canonical boundaries

Only group/QF/SF/final are official; `SPECIAL_NOVA` happens later with actual player control and no official trophy. The player-selected Ren remains an authentic human mind not yet demonstrably fully integrated by Nova. Nova's **Kreissack-only confirmed** covert override is revealed in Chapter 6. Kreissack's sacrifice prevents physical escape as proposed in the main story bible; limitations on Nova access and backups are respected. No instant cure for Ren; no instant Ganymede reparations, Haldane accountability or Varga absolution.

## 7. Open matters for author

1. Whether Angel and/or Tessa romances should become implemented alternatives, and whether Tessa merits inclusion as a new continuing NPC.
2. Final clinical side-effect specifics, independent oversight feasibility, and the exact interface safeguards/physical isolation staging.
3. Published group circular-ranking rule and authored NPC upset matrix for alternative brackets.
4. Chapter pacing/voice budgets and whether Ren's experimental participation should have any **noncompetitive** gameplay mechanic without unbalancing fights.

**Validation:** `ren_route_validator.py` and `test_ren_route_validator.py` check bracket mapping, romance gates, per-route essential clues and research-independent fight outcomes. These are consistency tests, not a quality judgment about the scenes.


## Shared semifinal clock (audit v1.1)

`R5.3 S_AB` plays on Day 11 **before** `R5.1` Nova's accidental rescue (Day 12). Existing scene IDs remain unchanged; the actual screenplay and route event list are now arranged chronologically. When Ren is already eliminated, the genuine AB semifinal plays on Day 11 and Ren's relay-audit contribution continues independently.
