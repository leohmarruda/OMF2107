# OMF 2107 — Shared World Event and Relationship State Contract v1.1

**Status:** Implementable design guideline and test scaffold, NOT a full production engine or new story canon.

## One save, one protagonist

All campaigns inhabit *one* simulated tournament and one sequence of shared events **per save file**. Choose Ari, Lyra, Mara, Ren or Angel once at campaign start. Other pilots are NPCs with their own choice/relationship states. A win by an alternative protagonist replaces the corresponding default winner, never adds a second official final. Scene POV is a camera/agency choice; neither side gets to retroactively decide the other's preferences.

## Authoritative match and scene order

| Absolute period | Shared event | Scene owners / stage |
|---|---|---|
| Day 0–1 | Anniversary/gala and legacy clues | Every pilot Ch1 |
| Days 3–5 | 12 decisive qualifying matches | Each pilot has two; IDs are not screen chronological order |
| Days 8–10 | Four QFs, Kreissack biological survival supported | `Q1`–`Q4`; distinct clue paths |
| Day 11 | First semifinal | `S_AB`, involving Groups A/B |
| Day 12 midday | Accident and Nova rescue | One event, different POVs; no rigged catastrophe |
| Day 12 evening | Second semifinal | `S_CD`, involving Groups C/D |
| Day 13 | Official final / champion | `FINAL`; actual winner receives trophy |
| Day 13, after final | Covert override revealed, special boss, Kreissack containment intervention | `SPECIAL_NOVA`, outside official competition |
| Weeks later | Fallout and endings | Independent evidence and romance outcomes |

**UI matchup order** (two booleans mean WIN/LOSS, never a draw):

| Protagonist | On-screen first | On-screen second | Engine data order | Adapter |
|---|---|---|---|---|
| Ari | Selene | Crystal | Crystal, Selene | `simulate_screen` (cross-audit; Ari production dispatcher pending) |
| Lyra | Milano | Steffan | Steffan, Milano | `simulate_lyra_screen` |
| Mara | Raven | Ren | Ren, Raven | `simulate_mara` |
| Ren | Raven | Mara | Mara, Raven | `simulate_ren` |
| Angel | Jean-Paul | Dante | Dante, Jean-Paul | `simulate_angel` |

For permanent records, store outcomes keyed by **match ID and actual participants**, not positional booleans. Keep one `world_state.tournament.matches` and use it to render every scene. `S_AB` is always before the rescue and `S_CD` always after.

## Suggested single-state schema

```text
WorldState
  selected_pilot: PilotId
  event_phase: EventId
  official_matches: Map<MatchId, {left, right, winner, loser}>
  group_ranking_policy: RuleVersion   # currently provisional
  npc_match_rule_version: RuleVersion # currently provisional
  relationship_graph: Set<Pair(PilotOrNPC, PilotOrNPC)>
  relationship_intentions: Map<PersonId, PersonId | none>
  reciprocal_decisions: Map<Pair, {initiated_by, accepted_by, time, conditions}>
  verified_separations: Set<{pair, time, parties_confirmed}>
  professional_recusals: Set<{person, case, effective_time}>
  neuro_program: Map<PilotId, {participation, disclosure, risk, disconnect_status}>
  evidence_ledger: Map<ClueId, {first_known_time, source, custody, independently_verified}>
  identity_and_privacy: Map<PersonId, {publicity_scope, disclosures, consent}>
  finance_and_family: Map<PersonId, {agreements, contingent_prize, privacy_consent}>
  nova_boss_access: {safety_authorization, equipment_available, task, escorts}
  selected_character_ending: EndingId
```

The implemented v1.1 `cross_campaign_validator.py` provides a narrower schema-independent assertion layer (fight-order dispatch, shared scene ordering, relationship conflict rejection) rather than fully representing this structure.

## Commitment rules

1. Commitments are **symmetric** and exclusive in this draft; one pair occupies both people.
2. Each person's independent decision is required. A `romance_intent` flag from the selected character is not a reciprocal decision.
3. A past exclusive bond may be lifted by an **authored, mutually clear separation**, not by assigning `partner_free=True` alone.
4. Separate procedural gates: Leena/Alex coverage and conflict recusal; Plug maintenance recusal; Ren's decision-making capacity and physical interface isolation; relevant age verification for supporting roles; privacy and permission for family information.
5. Nonromantic closeness and solo outcomes are first-class routes. Neither grants nor removes essential evidence.
6. A romance can be available but *not selected*. The epilogue displays exactly the chosen eligible outcome, not a montage of alternative partners.
7. No new pairing in this document is approved by inclusion; assess counterpart interest and narrative plausibility before promotion to canon.

## Clue and ending guards

| Clue/event | Earliest stable phase | Cannot be replaced by |
|---|---|---|
| Intent/permission anomaly | Ch1–3, as suspicion | Proof Nova already incorporated every fighter |
| Kreissack biological survival | Ch4 / Act III | Full proof of Nova secret executive veto |
| Genuine Nova rescue and unexplained command attribution | Ch5 / Act IV | Evidence Nova sabotaged the accident or that it is always benevolent |
| Varga's emotional study | Ch4–5 | Claim fights were rigged or love magically manufactured |
| NOVA conditional executive veto and expansion motive | Ch6 / Act V | Recontextualizing Ganymede policy responsibility as Nova's fault |
| Nova special boss | After **actual** tournament final | Official championship or unearned trophy |

## Production gates still missing

- Explicit Ari alternative loser/finalist/champion scenes and production dispatcher.
- NPC relationship and availability schedules with counterpart-authored consent, not manually user-set external Booleans.
- Hour-by-hour event ledger, including journalists' schedules and technician access to safety corridors.
- Final grouped-round-ranking rule and nondefault NPC fight outcome matrix.
- Protagonist-specific physical Nova access and evacuee staging following the *same* global emergency.
