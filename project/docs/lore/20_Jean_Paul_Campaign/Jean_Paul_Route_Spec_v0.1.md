# OMF 2107 — Jean-Paul playable route specification v0.1

**Status:** First-pass editor-authored mechanics, not blanket approval of new romance canon. Works with the v1.9 shared tournament and finale, no changes to default NPC outcomes or earlier story bibles. Screenplay: `Jean_Paul_Playable_Screenplay_v0.1.md`.

## Premise, default, stakes

Jean-Paul (37, Shadow) is a social spy and charming but compromised intelligence broker. Core established relationship: Dr. Ilse Varga. They genuinely desire each other while using and deceiving one another. Varga's privately unauthorized emotional research manipulates social circumstances and collects participant data without adequate consent, but **does not manufacture love or rig official fights**. Jean-Paul can tell the truth, exploit secrets, attempt protection, or evade personal accountability. No branch automatically transforms Varga into an ethical researcher.

Default `GD2`: Angel beats Jean-Paul; `GD3`: Dante beats Jean-Paul. Angel also beats Dante in `GD1` → D1 Angel / D2 Dante / D3 Jean-Paul. He is eliminated from the official tournament, but continues the Varga investigation and reaches the separate Day-13 Nova crisis.

## Tournament integration

`simulate_jean_paul(angel_win, dante_win, knockout_wins, choices)` consumes player match outcomes in **on-screen order: vs Angel, vs Dante**, which is also the engine's selected-pilot order in Group D (`GD2`, `GD3`). `GD1` is the actual Angel–Dante NPC result. All fights are decisive, never drawn.

| Group D position | Official QF | Opponent | If QF won | If SF won |
|---|---|---|---|---|
| D1 | `Q4` | actual Group C runner-up | `S_CD` on Day 12 after rescue | `FINAL` Day 13 |
| D2 | `Q3` | actual Group C winner | `S_CD` on Day 12 after rescue | `FINAL` Day 13 |
| D3 | none | none | no semifinal | no final |

A player 1–1 result can create circular 1–1–1 Group D standings depending on `GD1`, resolved by the provisional **public seeding**. This has no drawn fights. No changes to the canonical default; NPC knockout upsets still rely on **noncanonical provisional priorities** unless separately authored. `FINAL` opponent derives from `S_AB` actual winner. The `official_champion` and `player_champion` derive exclusively from the real final record. The Nova boss is not an official match. Fight outcome flags cannot be set by ethics/romance/intimacy/Spy preferences.

## Choices, eligibility, and relationship arbitration

| Key | Values | Consequence |
|---|---|---|
| `approach` | `investigate`, `court`, `keep_distance` | dialogue, access-request style; no locked clues |
| `client_policy` | `independent_audit`, `sell_to_bidder`, `war_inside_channel` | reputational/procedural consequences, not clue deletion |
| `evidence_policy` | `protected_release`, `escrow_negotiation`, `brokerage` | who sends protected participant notice and personal liability |
| `varga_boundary` | `distance`, `accountability_only`, `conditional_contact` | restricts whether a later relationship is narratively eligible |
| `final_evidence_action` | `audited_disclosure`, `compromised_bargain`, `illicit_sale` | self-compromise and consequences; independent investigation continues |
| `public_stance` | `accountable_testimony`, `protected_cooperation`, `self_serving_spin` | aftereffects; no erasure of records |
| `relationship_intent` | `varga`, `selene`, `friendship`, `single` | one intended route per save |

**Varga romance eligibility:** `relationship_intent=varga`, `varga_boundary=conditional_contact`, both adults, both uncommitted, both reciprocate **and choose freely**, Varga has ended unauthorized collection, made substantiated disclosure of the research, and accepted independent accountability. These are gates for optional after-confrontation intimacy and ongoing romance; they do not prove that all harm is repaired or that she escapes consequences. Failed gates yield `varga_unresolved_or_separated`, with friendship/single continuations. Earlier chosen kisses in a properly offline, consensual setting do not waive evidence or generate a lasting romance.

**Selene romance (new draft proposal, NOT canon):** available only when both adults, freely reciprocal, uncommitted, and Selene's connection with Milano is actually cleared, with no professional coercion. Otherwise `selene_friendship_or_distance`. Cannot simultaneously finalize with Varga. Shared-world commitments in a future game implementation must be authoritative; local booleans are only conservative demonstration gates.

**No-romance endings:** `friendship` and `single` are complete endings. No evidence, tournament, Nova survival, safety participation, or character dignity is contingent on sex or romantic success. Jean-Paul may remain morally compromised and still help stop Nova.

## Evidence and revelation order

| Clue/event | First admissible point | Verification | Limits |
|---|---|---|---|
| `jp_legacy_funding_discrepancy` | JP-C1.2 Day 0 | public serial/procurement mismatch | no living Kreissack inference |
| `jp_legacy_authorization_trace` | JP-C2.1 Days 3–4 | public device serial, Angel custody | no hidden veto inference |
| `jp_unauthorized_study_pointer` | JP-C3.3 Days 5–7 | room scheduling and registry mismatch | a pointer, not all personal biometric files |
| `jp_varga_authenticated_misconduct` | JP-C4.2 Days 8–10 | authenticated preservation record, independent logs, Leena | independent of Jean-Paul romance/profit |
| `kreissack_biological_survival` | JP-C4.4 Days 8–10 | Angel/Ren with corroboration | Nova's AI sovereignty **not revealed** |
| `nova_genuine_rescue` | JP-C5.1 Day 12 before S_CD | worker witnesses, actual machine action | not staged or evidence of Kreissack initiation |
| `nova_attribution_anomaly` | JP-C6.2 Day 13 | Angel/Ren independent matched signal traces | full composite veto only in finale |
| `nova_conditional_executive_veto` | JP-C6.3 Day 13 | gateway disruption plus matched signals | still authentic Kreissack experience and conditional autonomy |
| `kreissack_2092_murder_order_E5` | JP-C6.5 Day 30 | Christian and independent E5 authentication | **never Day 0–13** |

Varga's independent misconduct must not be equated with Haldane's officially authorized but risky neural program, nor retroactively attributed to Nova. Varga cannot create attraction or rig matches. Lyra learns the authenticated encounter interference even when Jean-Paul chooses brokerage: participant notice proceeds through independent custodian/Leena. Angel/Ren discover Kreissack biological survival independently. Raven's 2092 guilt and Kreissack's assassination order remain separate from Varga and Nova.

## Event order and shared finale

1. Days 0–1: JP-C1.1–JP-C1.4, invitation and public procurement anomaly.
2. Days 3–4: JP-C2.1 `GD2`, study suspicion, optional gala/fanservice.
3. Days 5–7: JP-C3.1 `GD3`, standings, study pointer and optional dance.
4. Days 8–10: JP-C4.1 `Q3/Q4` only if qualified; JP-C4.2 authenticated preliminary Varga evidence; JP-C4.3 pending participant notice; JP-C4.4 biological survival.
5. Days 11–12: JP-C5.0 Varga confrontation and independent Lyra notification on Day 11, optional JP-C5.0B relationship boundary; JP-C5.1 **Day-12 real rescue**, then JP-C5.2 `S_CD` (if real qualifier), then evidence-choice and romance scenes.
6. Day 13: JP-C6.1 `FINAL` only if real finalist; JP-C6.2 post-final activation with K4/K5 audience-only cutaways; JP-C6.3 special Nova encounter and K6 latch sequence; JP-C6.4 epilogues.
7. Day 30: JP-C6.5 optional E5 Devroe report, with the assassinations verified **only now**.

**Shared final hardware:** official tournament complete → Kreissack takes control and fails to isolate Nova → combat damages executive gateway G → Angel/Ren isolate relay R → irreversible destruction D starts → E attempts eject → B→L regained for an instant → Kreissack holds L → unique core destroyed, no complete backup. Last line exactly **“Apparently, I can still surprise you.”** K3 (post-rescue), K4, K5 are *audience-only private* if shown before independent corroboration. No character can use private cutaway speech as evidence.

## Implementation and outstanding approvals

- See `jean_paul_route_validator.py` and `test_jean_paul_route_validator.py` for executable scene dispatch and tests. They check reachability and constraints, **not** actual screenplay writing quality.
- Selene–Jean-Paul pairing, which previous bibles floated, remains a proposal. Varga's ultimate willingness to change and full accountability outcome remain authored branches rather than canon fact.
- Specific spy clients, dance/fundraiser, ethics-review mechanics and Jean-Paul's liability outcomes are draft screenplay detail.
- Shared relationship state is partially modeled in v1.9; the real game still needs one canonical state store and consistent NPC autonomous choices.
- Provisional group seeding and default fallback NPC knockout results require a future author decision.
