# OMF 2107 — Mara playable-campaign integration (v0.8)

**Date:** 2026-11-01 · **Status:** First-pass editorial proposal, no new romantic pairing automatically canonized.

## Deliverables

`10_Mara_Campaign/` adds a **six-chapter, approximately 5,600-word** Mara-POV script, route/continuity spec, executable dispatcher, and 16 automated tests. Existing 6 Ari and 6 Lyra chapters, original lore and older canonical story material remain untouched. The v0.7 pack is preserved and v0.8 builds on it.

| Chapter | New Mara-centric purpose | Match or key variant |
|---|---|---|
| **1. The Cost of a Win** | Introduce Mara's mother as an independent person, Mara's financial predicament, class mismatch with gala, Ari, Plug and Raven | Arrival, optional repair contract, no battle |
| **2. Hard Metal, Soft Spots** | Compete with Raven and Ren; negotiate real medical-plan choices, paid work and privacy; enjoy ensemble poolside comedy | Actual `GB2` Mara–Raven then `GB1` Mara–Ren; dynamic results |
| **3. Five More Seconds** | Mutual attraction or friendship with Ari; possible future professional Plug or accountable Raven; refuse any thrown match | Real group standings and dynamic knockout opponent |
| **4. An Honest Defeat** | Competitive QF **only if qualified**; mother's autonomous care preferences; distinctive physical evidence of WAR relay | `Q2` if B1, `Q1` if B2, independent investigation if B3; Kreissack biologically alive |
| **5. The Person Behind the Debt** | Rescued workers, signed safety data, nonmagical finance paths, choice-dependent relationship trust and Varga scandal | `S_AB` if earned; Nova's beneficial intervention precedes final executive-control reveal |
| **6. No One's Prize** | Actual champion or actual winner broadcast; physical safety contribution in Nova finale; truthful, consent-based family and romantic aftermath | `FINAL` only if earned; Nova confrontation for all, separate from bracket |

### Romance, fun and secondary cast

- **Ari:** Default slow-burn available, with an independent friendship route, optional mutual kiss/date, real competitive integrity and conditional repair if he conceals neural research.
- **Plug:** Proposal for post-tournament mutual romance, never purchased by accepting maintenance work; adult verification and absence of professional conflict mandatory. Provides significant nonromantic technical friendship.
- **Raven:** Proposal for slow chemistry only after accountability for hidden records, genuinely independent choice and no existing Crystal commitment. Friendship/rivalry is available without romance.
- **Solo:** Family relations, paid career, investigation, professional pride and close friendships form a complete story, not a consolation prize.
- **Fanservice:** adult-only and opt-in sparring, rooftop pool with group comedy, charged dialogue, kisses and discreet fade-to-black intimacy where consent and route eligibility permit.
- **Other supporting characters:** Ren, Angel, Crystal, Cossette, Ibrahim, Leena and Mara's mother are essential independent agents, not collectible partners or exposition dispensers.

### Continuity and safety of branches

**Critical input-order subtlety:** existing Group B match IDs are `GB1` vs Ren and `GB2` vs Raven, but the outline presents **Raven before Ren**. The human-facing helper swaps the two group-result arguments before using the tournament model. The result is never inferred from prose, and every official match has a winner and loser.

- Trophy, prize eligibility and match opponent are derived only from actual tournament results. **32 possible 5-bit input patterns** are covered by tests, although early elimination means some extra inputs are ignored. There are no drawn fights.
- All routes retain access to the core Nova conspiracy via independent worker-safety credentials. Group elimination is not a dead story end; Mara contributes mechanical proof, signed human testimony or emergency safety coordination instead of imitating Angel's specialized neural science.
- Preserve the established Nova causality separation: **Act III** Kreissack's biological survival, **Act IV** genuine beneficial safety-gateway rescue during an accidental fault, **Act V** covert executive override/conditional autonomy and brain incorporation. Human officials—not Nova—remain responsible for delayed Ganymede relief.
- Her mother must consent independently to treatment-related publicity. Proposed sponsor income is blocked, with a private financial fallback, until relevant consent exists. No strategy automatically clears debt or pays the prize before settlement.
- The author has approved *developing* optional adult romance and fanservice, not an exhaustive list of new couples, final medical numbers or specific alternate outcomes.

### Automated tests

- 7 tournament validator checks (retained)
- 15 relationship route checks (retained)
- 13 Lyra route checks (retained)
- **16 Mara route checks (new)**, including 32 tournament input sets, prize eligibility, early loss, adult/mutual/ethical romance guards, mother publicity consent, and romance-independent fight results.

**51 tests passing** (these are model consistency checks, not cinematic/acting playtests). The archive's SHA-256 checksums and compressed-file CRC are regenerated and verified in packaging.

### Remaining author decisions and next creative work

1. **Money/care specifics:** name and life outside illness for Mara's mother; actual cost/prize/currency/medical system; which finance outcomes have convincing sacrifices.
2. **Romance canon:** whether Plug's and/or Raven's independent attraction are real routes; whether Crystal's relationship with Raven can coexist with this alternative continuity; whether Ari has a neural trust-repair path in Mara's campaign.
3. **Brackets/implementation:** settle circular standings and provisional NPC outcomes; select practical cinematics/voice lengths and test pacing; define credible final containment and Kreissack's fate. The next lead campaign could be Ren (informed consent/technology) or Angel (neural science and forensic investigation), avoiding duplication with Mara and Lyra.

**Reading order:** `10_Mara_Campaign/Mara_Playable_Screenplay_v0.1.md` → `Mara_Route_Spec_v0.1.md` → dispatcher/tests. `COMBINED_WORKING_EDITION.md` is a historical snapshot and does not contain v0.8 chapters.
