# NPC knockout decisions — v4.3 author review ledger

**Authority boundary:** Seven exact-pair cinematic results are established. All 59 other winners remain **PENDING_AUTHOR_APPROVAL**, irrespective of the `proposed_winner` column. Do not import this CSV as a production winner table. No new outcome has been approved here.

## Review scope

- 66 structurally possible knockout pairings, from the v4.2 reachability enumerator.
- Approval ledger: `NPC_OUTCOME_APPROVAL_LEDGER_v4.3.csv`.
- Priority counts: {'CANON': 7, 'P0': 8, 'P1': 11, 'P2': 40}. P0 = eight historical ranking exceptions; P1 = other pairs with v4.0 tactical hypothesis; P2 = remaining ranking-derived proposals. Priority is editorial review order, **not** likelihood of occurring.
- When reviewing, decide whether to accept the draft winner or replace it based on fighter capability and fairness; provide one-sentence reasoning. A losing fighter's player-controlled route is not predetermined by any NPC-only result.
- Existing established result pairs are **not** general power rankings and are immutable by default.

## No NPC fight presentation

NPC-vs-NPC matches are **offscreen**. The game presents results in bracket/standings UI, and may include selective dialogue or commentary *about the outcome*. Tactical notes are designer-only hypotheses, not spectator knowledge. Earlier dossier `required_scene_evidence` instructions such as 'depict the exchange' are **superseded**; do not create fight cinematics.

## Historical proposal — superseded by v4.4 approved canon

The existing 1–1–1 group cycle first compares cumulative scores. Equal totals for exactly two fighters use their head-to-head winner. If **all three totals are identical**, the existing head-to-head results are circular, so cannot decide a winner.

Recommended *exceptional fallback*: a **public, recorded random draw** for the three finishing positions, conducted with a verifiable tournament event identifier and stored as one immutable order in the global event ledger. A deterministic seeded generator with a logged seed/reveal may be used for reproducibility, but must not silently derive the seed from pilot identity, matchup strength, or a mutable timestamp. If the author prefers avoiding randomness, an announced pre-tournament seed order is simpler but can give a lasting advantage unrelated to fighting performance. The user approved the random draw in v4.4. See `THREE_WAY_RANDOM_TIE_CANON_v4.4.md`. Strict mode accepts a recorded draw and rejects an unrecorded one.

## Critical runtime checks

1. Establish what 'score' means in the actual game: points versus health remaining versus ranking points; whether CPU scores are available and comparable; and whether a fight winner can score fewer points.
2. Record actual scores for every group fight; never invent a score from a win/loss flag.
3. If a draw fallback is approved later, log the full ordered three-fighter draw **once** and reuse it for all perspectives and replay displays.
4. Do not allow unapproved `proposed_winner` values to pass production-mode validation.
5. Resolve NPC matches only when both fighters are NPCs; player-controlled matches take their actual result.
