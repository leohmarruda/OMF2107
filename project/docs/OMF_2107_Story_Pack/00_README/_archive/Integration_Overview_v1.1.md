# OMF 2107 — Five-campaign continuity audit integration (v1.1)

**Date:** 2026-11-01 · **Status:** Cross-campaign technical/editorial repair, NOT approval of new NPC romances or official tournament tie-breaking.

## What changed

- Added `13_Cross_Campaign_Audit/` with a detailed audit, shared event/state contract, cross-pilot adapters and relationship graph checks.
- Corrected Angel's impossible Day 2–6 chapter chronology to the shared **Day 13 final** (Ch2 group matches Days 3–4; Ch3 Day 5; Ch4 QF Days 8–10; Ch5 rescue and CD semifinal Days 11–12; Ch6 finale Day 13).
- Corrected the first semifinal timing: Mara and Ren now put their **S_AB on Day 11 before the Day-12 Nova rescue**, in both prose and dispatcher event lists. Scene IDs are stable but no longer numerically displayed in exact order within Chapter 5.
- Added `simulate_lyra_screen(milano_win, steffan_win, ...)` to prevent the Lyra on-screen fight order from silently reversing the engine's winner inputs. Also added a cross-campaign Ari adapter for Selene before Crystal.
- Preserved original fight results, the established default storyline, and all existing 99 tests. Added 8 tests including a 160-input cross-pilot traversal and contradictory-romance cases.

## Remaining major work (not fixed)

1. **Ari's actual cinematic branches** after a loss to Selene / finishing third, alternate championship opponent, losing the final or being eliminated earlier. The legacy Chapter 6 Scenes 3–4 presently dramatize only Ari beating Lyra; notes promise alternatives but authored branches are missing.
2. **Single production relationship state**: v1.1's validator protects against simultaneous *recorded* exclusive commitments; it cannot verify offscreen NPC consent or separations that the game did not record. Connect one authoritative save-file graph, counterpart choices, and professional recusal data before using romance endings.
3. **Tournament rule choices**: 1–1–1 group seeding and unauthored NPC knockout winners are intentionally provisional, not canon. Every fight still has a winner and a loser.
4. **Production-level timing and final-base access** across alternate eliminations; tests do not replace an animatic or a five-route script playthrough.
5. **Author approval** for all newly proposed romantic pairings, NPC precise ages and Tessa Kade; their inclusion in a draft is not a decision.

## Validated

Project test suites: 7 tournament, 15 relationship, 13 Lyra, 16 Mara, 24 Ren, 24 Angel, and 8 cross-campaign = **107 passing**. The new test traverses five pilots × four group input combinations × eight possible knockout decision tuples = **160 scenarios**, which include ignored excess knockout input when the player is already eliminated. The baseline 384-entry full-12-pilot tournament sweep was previously checked by the tournament validator tests. Cross-level checks do not mean every scene permutation was text-playtested.

**Read first:** `13_Cross_Campaign_Audit/Cross_Campaign_Continuity_Audit_v1.1.md`.
