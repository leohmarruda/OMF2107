# OMF 2107 — Christian secondary route and evidence specification v0.1

**Status:** New supporting-character implementation proposal based on Devroe v1.7 historical truth and E5 chronology. Christian is a **non-playable** secondary protagonist in the sequel, not the eighth selectable HAR pilot. His testimony and investigation can appear in all seven selected-pilot campaigns without making the evidence depend on romance or survival in the tournament.

## Invariants

- Fixed 2092: two Devroe parents die; human contractor installed lethal flight-control attack; Raven knowingly authorized illicit distress blackout, observed restoration request, refused, then concealed evidence; Raven did not know the lethal code was installed beforehand. Nova and Varga **did not cause** the 2092 deaths.
- The truth can be authenticated through a civilian custodian, insurer/relay archives, independent flight examiner and dual-custody message log even when Raven refuses, lies, destroys his private copy, is eliminated, or dates nobody.
- E1 Days 0–5 (fully authenticated by end Day 5): suspicious custody gap / false completion; E2 Days 6–8: signed distress blackout; E3 Days 8–10: independent malicious command and Iron Fist-linked contractor trace; E4 Days 9–11: emergency restoration request acknowledged and ignored. E5 Day 30: neutral escrow releases Kreissack-signed fatal directive with independent contractor-settlement match. Investigators' access to a provisional lead is NOT the same as proving it or disclosing it to Crystal.
- The effect of restoring the emergency channel cannot be proven; no automatic convicted killer, unknown human signatory, or identified saboteur is created. The eventual hearing takes place **weeks after Day 13**. Nova's secret conditional override is not proved before the separate post-final confrontation.
- Christian's relationships and career cannot change official matches or force a specific Crystal romance outcome. He is allowed to be wrong, fearful, controlling and to repair his behavior. Crystal retains agency and testimony rights.

## Chapter and clue scene dispatch

| Scene | Earliest slot | Evidence / source | Revelation boundary |
|---|---|---|---|
| CH1.1 | Day 0 | Suspicious public index | Not proof of fraud or sabotage |
| CH1.2 | Day 0 | Leena meets Christian | No compelled flirtation / protected source |
| CH2.1 | Day 4 | Preservation / public catalogue | Not full insurer file |
| CH2.3 | Day 5 | E1 authenticated | Custody gap only |
| CH3.1 | Day 8 | E2 relay/insurer plus neutral officer | Raven's authorization, not lethal intent |
| CH3.2 | Day 8 | Leena journalism boundaries | No privileged packet |
| CH4.1 | Day 10 | E3 flight forensics | Deliberate override, unknown signer |
| CH4.3 | Day 10 | Optional music venue | Kiss requires prior recusal, adults and reciprocity |
| CH5.1 | Day 11 | E4 emergency receipt | Refusal, **not** guaranteed rescue |
| CH5.2 | Day 12 | Genuine beneficial Nova rescue | **Not** secret veto proof |
| CH6.1 | Day 13 after final | Covert Nova executive override | Separate from 2092 case |
| CH6.2 | Weeks later | Independent hearing | Separate legal process, no automatic verdict |
| CH6.3 | Weeks later | Personal ending, optional Leena | No relationship reward for testimony |

**Reuse / duplicate guard:** CH3.1 is the Christian POV coverage of D1; CH4.1 is D2; CH5.1 is D3; CH6.2 is D5. When the selected pilot is Crystal or Raven, use **one** shared event and authored alternate camera/dialogue, not four separate discoveries or hearings with inconsistent witnesses.

## Secondary narrative states

```text
ChristianSecondaryState:
  family_dynamic: collaborate | parallel | private | intrusive
  records_approach: methodical | public_pressure
  raven_meeting: formal | demand_meeting | avoid_face_to_face
  post_hearing_direction: records_service | fieldwork | music_break
  evidence_ledger: E1 (day5) E2 (day8) E3 (day10) E4 (day11) E5 (day30)
  disclosure_to_crystal: stage-aware; separate from fact authentication
  nova_override_known: only day13 after official final
  leena_route: none | optional_romance
  leena_editorial_recusal_day: null | day <= actual intimacy time
  leena_mutual_choice: boolean (independent NPC decision)
  leena_existing_partner / christian_existing_partner: global world state
  crystal_response: independent NPC/selected character choice
  raven_statement: full | selective | false denial (never rewrite history)
  criminal_verdict: unresolved
```

If Christian publicly pressures Crystal (`family_dynamic=intrusive`), add a trust cost and optional apology scene; never transfer Crystal's consent or testimony into his control. If he takes a pause from investigating (`music_break`), the independent case custody still proceeds.

## Leena romantic route (PROPOSED, not approved canon)

- Christian and Leena are both adult professionals (Christian 33; Leena's age/eligibility must be confirmed in the production cast bible). Mutual interest, not player pressure, is mandatory. She can prefer friendship, Ari/Angel if available, or single life.
- The global exclusive relationship graph must show both unattached at the actual relationship start. Player-selected Ari–Leena, Angel–Leena, or another validated existing partner blocks this route. A kiss is not sufficient to mark an exclusive relationship.
- An **independent newsroom editor must accept Leena's actual recusal** from handling Devroe coverage or receiving confidential evidence *before* private romance proceeds. A later independent journalist continues the case. A friend interview is not a romantic quid pro quo; Christian does not supply privileged records for intimacy.
- Optional Day 10 dance/kiss needs recusal by Day 10; default professional interaction stays platonic. The committed romance scene belongs weeks after the hearing, with recusal continuing and separately authored reciprocal decisions.
- Sexual/romantic content is adult, mutual, optional and suggestive/nonexplicit. Case evidence and Crystal's safety do not depend on it.

## Per-protagonist insertion plan

| POV | Insert | No-change guarantee |
|---|---|---|
| Ari | Ch4 investigator meeting, Ch6 records response | Ganymede testimony and match results separate |
| Lyra | Ch2 public image vs absent parent record, Ch5 safety corridor | Lyra relationship/tournament unaffected |
| Mara | Ch4 technician interview, Ch6 mutual aid / case-access rights | Her mother finances remain separate |
| Ren | Ch3 custody provenance, Ch5 safety operation | Ren neural-link decisions and agency independent |
| Angel | Ch3 privacy-preserving archive request, Ch6 conditional override comparison | Angel's identity privacy remains hers |
| Crystal | C1.3, C3.4/D1, C4.3/D2, C5.1B/D3, C6.4/D5 | Crystal can refuse Raven and needn't adopt brother's choices |
| Raven | R1 challenge, R3/D1, R4/D2, R5/D3, R6/D5 | His confession affects testimony, **never** proof existence |

## Validation scope

The attached `christian_secondary_state.py` checks chronology, fixed case facts, independent evidence, character knowledge, exclusivity, recusal, romance eligibility and ending preservation. It is a route contract, **not** a full global campaign engine, witness simulation, judicial decision model, or screenplay parser. Cross-campaign NPC commitment must eventually be stored in one actual save-state ledger rather than passed as booleans.

## Creative questions remaining

1. Leena's age and reciprocal romantic interest with Christian, if any, require approval before treating romance as canon.
2. Christian's ultimate career direction should remain player-reactive but not necessarily determined by the pilot; the three versions are alternative character futures.
3. **Kreissack is the proven kill-order authorizer from Day 30 E5**; the direct contractor coder, legal jurisdiction/disposition and whether Christian ever forgives Raven remain open. Investigation findings do not presuppose answers.

## V1.7 hearing gate

New `CH6.1B_E5_KREISSACK_ORDER` triggers on Day 30 **after** Day 13 Nova revelation and **before** the hearing. Neither Christian nor Crystal may cite the lethal order earlier, though readers know the hidden historical fact. All seven player campaigns and all Raven statements yield the same record.
