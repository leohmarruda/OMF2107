# NPC knockout outcomes — structural audit v4.2

## Confirmed structural result

All **66** unordered pairs among the twelve pilots can occur in an official knockout, given some permitted group-stage ranking and knockout result. Exhaustive enumeration of all `6^4 = 1,296` possible within-group final rankings gives:

| Stage | Distinct possible unordered pairs |
|---|---:|
| Quarterfinal | 18 |
| Semifinal | 30 |
| Final | 36 |
| Union | 66 |

These stage sets overlap in the sense that a given pair may be possible in more than one stage; the union is 66. The calculation treats alternative groups' ranked qualifiers and earlier knockout winners as freely variable, and establishes **structural** (not empirical, score-distribution-weighted or presently scripted) reachability. It does not assert that all group-score combinations occur in shipped gameplay or that all hypothetical NPC group upsets are implemented. It does not replace full runtime testing.

## Impact on earlier claims

The earlier 384-input sample saw only 21 NPC-only knockout pairings. That sample fixes NPC group results and mostly uses provisional group ordering; it is *not* adequate to prune the remaining 45 pairs. All 66 should have deterministic winner definitions for a production model with unconstrained bracket histories, unless a future authoritative game rule rules some histories out.

The established cinematic result table defines **seven** exact-pair results, leaving **59** winner decisions still unapproved. The v3.9 51 ranking-inherited choices and eight exceptions are **proposals**, not evidence or approvals. The v4.0 tactical dossiers cover fourteen sample-priority proposals, not all reachability scenarios.

## Production-safe behavior

- NPC versus NPC fights occur **offscreen**; only bracket results, actual recorded scores if available, and optional character reactions are shown.
- Do not create a fight cutscene or assume spectators saw any tactics.
- Canonical exact-pair winner takes precedence. Every other result requires a reviewed deterministic mapping, never a silently substituted strength ranking.
- Numeric score fields remain absent when data is absent. Match victory and arcade score are different fields; do not infer one from the other without confirming scoring semantics.
- A three-way circular group with identical cumulative scores still needs a *preannounced tertiary policy*. A documented final fallback using a seeded draw, a published seed, or a scheduled playoff could work, but no one of these has been approved. Any randomized procedure must persist a reproducible draw result in the event ledger. No unapproved procedure should run silently in production.

## Recommended decision and implementation workflow

1. Review the 59 outstanding pair winners by tactical plausibility and default continuity, using the existing 66-pair CSV and fourteen internal dossiers. A result may be a design choice even without a canonically narrated fight.
2. Mark each approved result in a separate approval ledger, preserving author, date and rationale. The existing `npc_pair_proposals.py` should not be loaded by production code by default.
3. Verify score representation for offscreen CPU fights, including whether points are comparable across all battles and whether a victorious fighter can have a lower tracked score.
4. Approve a final three-way equal-score policy and implement it with logged, deterministic provenance.
5. Consume one shared tournament result ledger for bracket UI, champion identity, opponent dialogue, Day-13 access logic and epilogues. No screenplay rewrites are performed by this structural audit.

## Files

- `npc_pair_reachability.py`: deterministic exhaustive set-based enumerator.
- `NPC_STRUCTURAL_REACHABILITY_v4.2.csv`: per-pair possible stages and approval status.
- `test_npc_pair_reachability_v42.py`: invariants for all 66 pairings and stage coverage.

### Release gate

`npc_outcome_registry.py` checks individual approved exact-pair overrides against the reachable 66-pair universe. `require_complete_npc_table(...)` rejects incomplete mappings and rejects changing the seven established results. The example synthetic winners used in the associated test exist **only in test code**, not in production data or canon. The new gate is not yet connected to an external game runtime.
