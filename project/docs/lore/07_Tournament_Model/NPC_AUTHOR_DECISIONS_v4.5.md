# NPC knockout outcomes — author decisions v4.5

**Newly approved:** eight explicit NPC-only pairing winners, preserving the seven established cinematic results. All NPC-only fights remain offscreen. These author approvals determine outcomes **only when neither fighter is player-controlled**; they never predetermine a player fight.

| Pair | Approved winner | Previous proposal | Decision |
|---|---|---|---|
| Angel, Milano | Milano | Milano | Confirmed |
| Angel, Ren | Ren | Ren | Confirmed |
| Crystal, Lyra | Crystal | Crystal | Confirmed |
| Dante, Ren | Dante | Dante | Confirmed |
| Jean-Paul, Selene | Jean-Paul | Jean-Paul | Confirmed |
| Mara, Selene | Selene | Selene | Confirmed |
| Mara, Steffan | Steffan | Mara | Revised |
| Raven, Steffan | Raven | Raven | Confirmed |

## Authority / integration

- The current ledger is `NPC_OUTCOME_APPROVAL_LEDGER_v4.5.csv`. `v4.3.csv` is preserved as an historical snapshot.
- `npc_author_approved_v45.py` lists the eight new decisions; `npc_outcome_registry.approved_author_outcomes()` and `current_author_approval_status()` validate them alongside the seven immutable cinematic outcomes.
- **15 approved pairings (7 established + 8 new); 51 still pending.** `require_complete_npc_table(approved_author_outcomes())` must fail until the remaining 51 decisions are approved.
- `npc_pair_proposals.py` is an **unapproved historical suggestion table**. In particular its Mara–Steffan entry still proposes Mara, which is **superseded** by the approved Steffan decision. Do not use that module as production authority.
- UI and dialogue may report the offscreen result, but no NPC fight scenes should be added. The score and downstream screenplay runtime bindings still require implementation.
