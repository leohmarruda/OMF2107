# Three-way group score tie — approved canon (v4.4)

**Authority:** User approved a random resolution for the exceptional case of a 1–1–1 circular group with identical cumulative match scores for all three fighters. Earlier v4.3 documents proposing a random draw are superseded on this point.

## Ranking policy
1. Rank by group-stage wins.
2. If all three finish 1–1, rank by cumulative game-tracked scores (only if real comparable scores for all matches are available).
3. An exactly two-fighter cumulative-score tie is resolved by their group head-to-head result.
4. If all three cumulative scores match exactly, conduct one **uniform random permutation** of all three positions (6 equally likely orders). Show this as an official tournament tiebreak draw.

## Implementation and persistence
- Call `generate_group_tie_draw(group)` **once per affected tournament group** after the complete three-way score tie has been established.
- Atomically store `{event_type: "group_three_way_tie_draw", group, order, tournament_id}` in the authoritative event ledger **before** advancing the bracket or showing standings.
- Pass the recorded `order` to `simulate(..., tie_draws={group: order})`; reuse it on reload, replays, and alternative character perspectives. Never reroll during reconstruction or UI rendering.
- `simulate(..., require_authored=True)` rejects an unrecorded three-way draw, rather than randomly altering the standing on repeat invocations. Non-strict mode retains the explicitly noncanonical provisional seed only when source scores/draws are missing.
- Recorded orders must be permutations of the three members of that group; invalid/mismatched records are rejected.
- The generator uses `secrets.SystemRandom().shuffle`, which samples each permutation without fighter preference. This is a random policy, not an unexplained tie-breaking order.
- Numeric score comparability between actual player and CPU matches remains an **independent** unresolved runtime integration requirement.

## Unchanged
- NPC-versus-NPC fights are not shown; only results and bracket standings may be shown.
- The seven established knockout outcomes remain canon; 59 proposed alternative pair winners remain pending approval.
