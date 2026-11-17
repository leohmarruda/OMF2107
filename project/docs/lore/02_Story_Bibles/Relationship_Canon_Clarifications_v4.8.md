# Relationship canon clarification — v4.8

## Cossette, Ibrahim and Milano (author decision, 2026-11-03)

- **Cossette and Ibrahim are steady partners.** Their affection, continuity and separate professional judgment are preserved.
- **Cossette and Milano have a casual fling.** The connection does not imply a second committed partnership, exclusivity, a breakup with Ibrahim, or a romance progression arc for Milano.
- **Milano has substantially higher social/institutional status than Cossette.** This creates a power asymmetry, not an entitlement. Cossette retains agency; the encounter must not purchase access, professional compliance or silence.
- **Consensual non-monogamy** is the already selected direction for the established Cossette–Ibrahim relationship. The precise agreements, boundaries and offscreen negotiations have not been described by the author. Do not invent their terms or imply that Cossette is having a secret affair.
- A player choosing Milano may affect minor tone or follow-up, but cannot unilaterally upgrade a casual connection to commitment, terminate Cossette–Ibrahim, or dictate Cossette's private decisions.
- When other POVs mention this connection, keep the same status distinction. It may remain mostly offscreen; no explicit encounter is required.

**Implementation:** `WorldState.casual_connections` is separate from `bonds`; event validation requires two independent decisions and appropriate consent coverage where an existing commitment is present. These event records are a runtime contract, *not* an invented scene of negotiation. Historical route-spec statements excluding Cossette/Milano intimacy are superseded.
