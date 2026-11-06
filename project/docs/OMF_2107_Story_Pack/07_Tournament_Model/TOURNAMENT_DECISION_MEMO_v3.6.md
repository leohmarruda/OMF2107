# OMF 2107 — Tournament integration audit v3.6

**Status:** Implementation and source-supported mechanical validation; no new player-facing tournament rule has been canonized.

## Verified rules

- Four groups of three; each pilot fights twice; top two advance.
- Official matches are decisive, no fight draws. There are exactly 12 group matches, four quarterfinals, two semifinals and one final.
- Q1=A1×B2, Q2=A2×B1, Q3=C1×D2, Q4=D1×C2; the A/B and C/D sides remain separate until the final.
- Nova is outside the official bracket; emergency access and combat do not retroactively change the champion.
- The seven exact pairs of the established reference cinematic bracket now have recorded default winners. A different pairing is not licensed to inherit an arbitrary winner.

## Exhaustive audit summary

See generated `audit_outputs/summary.json` and `route_matrix.csv`. They enumerate 384 raw tuples (12 pilots × four group patterns × eight KO bit strings), of which 144 are distinct after unused KO inputs are ignored. **Raw-tuple frequencies are not probabilities**; many tuples repeat the same playable path. The unapproved-seed and provisional-NPC categories may overlap. The canon-ready flag only speaks to resolution provenance.

## Decision D1 — 1–1–1 group ranking

**Recommendation:** Publicly announce a fixed tournament seed order as the tie-breaking rule *before* matches. Advantages: fully auditable, no new tracked telemetry, short arcade pacing. Strongest objection: a player can win a head-to-head match yet finish below that opponent because the group forms a cycle; seeded resolution may feel arbitrary or unfair. Alternative: a measured in-game score differential (requires an actual and uniform score system for CPU and player fights). A deciding playoff is fairer in one sense but adds encounters and timing complexity.

**Do not canonize yet.** `CYCLE_SEED` remains a placeholder; all four groups need explicit ranking approval.

## Decision D2 — NPC-only results

**Recommendation:** Use an authored deterministic pair table for every *reachable* nondefault NPC pairing, with a documented rationale and script consequences. This is more transparent than a hidden global power ranking and allows character-consistent upsets. The table must not override player-controlled fights. Alternatives are a seeded stochastic simulation (needs reproducibility and scene coverage) or constrained skill ratings (risks reducing narrative outcomes to power scaling).

**Do not canonize yet.** `NPC_KNOCKOUT_PRIORITY` remains expressly unapproved.

## Decision D3 — Screenplay binding

Route scripts must read the computed champion, placement, opponent and elimination point, not a fixed Ari-default championship. Follow-up check: identify any dialogue or epilogue that implicitly declares a champion or semifinalist regardless of tournament state. Such lines are not fixed in this release.

## Engineering changes

- Strict mode distinguishes documented exact-pair outcomes from provisional NPC fallback and blocks unapproved sources.
- Inputs for overrides and seed policy are validated.
- Every simulation result reports provenance in `audit`; CSV and JSON support independent inspection.
- New tests exercise strict mode and exhaustive provenance.

## Open validation boundaries

This is a model-layer audit, **not** a complete line-by-line screenplay or cross-POV tournament continuity reconciliation. The meaning and implementation of gameplay-dependent scores must be checked against the actual game before selecting a metric tie-breaker.
