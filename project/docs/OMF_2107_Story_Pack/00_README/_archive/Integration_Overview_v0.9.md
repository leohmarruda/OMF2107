# OMF 2107 — Ren playable-campaign integration (v0.9)

**Date:** 2026-11-01 · **Status:** First-pass editorial proposal; no new romance or civilian character approved as canon.

## Deliverables

`11_Ren_Campaign/` adds a **six-chapter, ~7,500-word** Ren-selected screenplay, a route and continuity specification, an executable dispatcher, and **24 automated tests**. It builds on v0.8 while preserving the six Ari chapters and existing Lyra/Mara campaigns.

| Chapter | Playable Ren focus | Fight or condition |
|---|---|---|
| **1 — The Person in the Loop** | Gala awkwardness, Lyra friendship, Haldane's promising research and missing executive-authority field; Angel's historic Nova identifier; meet proposed civilian Tessa | No official battle |
| **2 — What the Body Knows** | Legitimate Raven fight, symptoms, independent recording; optional rooftop flirtation, Cossette–Ibrahim warmth | `GB3` Ren–Raven, actual result |
| **3 — The Price of Precision** | Legitimate Mara fight, disclosure choices, withdraw/audit/continue research, Angel/Tessa bonds | `GB1` Ren–Mara; actual ranking |
| **4 — A Face Behind the Signal** | Qualified QF or honest early-elimination alternative; certified traces; **Kreissack biological survival** | `Q1` if B2, `Q2` if B1, otherwise investigation |
| **5 — The Kindness of a Dangerous Machine** | Nova's genuine accidental-fault rescue, Varga's separately unethical emotional study, research consequences and optional romance | `S_AB` if earned, else real broadcast and evidence work |
| **6 — Who Gets the Final Say** | Actual final or real result broadcast; independent executive-veto reveal; Nova special boss, Kreissack intervention, credible scientific and relationship outcomes | `FINAL` only if earned; `SPECIAL_NOVA` for all |

## Relationships, fanservice, secondary cast

- **Angel–Ren:** Proposed mutual slow-burn romance or fully realized investigative friendship. Her privacy, independent choices and potential other commitments remain intact.
- **Tessa Kade:** Newly proposed 30-year-old independent civilian accessibility choreographer, an intentional nonresearch setting for friendship, flirtation and mutually chosen romantic scenes. Not a gatekeeper for evidence.
- **Lyra:** Warm friendship; no new Lyra/Ren romance canonized. **Plug, Crystal, Cossette, Ibrahim, Haldane, Varga, Shirro, Alex and Raven** have meaningful nonromantic interactions.
- **Adult fanservice:** Playful pool party, low-gravity dance, charged banter, consensual kisses and fade-to-black romantic possibilities. No sex during an acute cognitive episode or while an unverified high-bandwidth path remains connected.

## Continuity, controls and tested properties

- **Ren's group play order is Raven then Mara (`GB3` then `GB1`)**, but tournament engine input order is **Mara then Raven**. `simulate_ren(raven_win, mara_win, knockout_wins, choices)` maps inputs correctly.
- Every group, QF, SF and championship fight has exactly one winner; no draw. Actual advancing pilots face actual seeded opponents. `NOVA` is a separate boss, not a tournament result.
- The default nonselected Ren record remains: win Raven, lose Mara, qualify B2, lose QF to Crystal. A selected Ren can lose in group or become the official champion, and either way retain an independent Nova investigation role.
- A research, romance or disclosure choice never grants a fighting advantage, determines match results or yields essential evidence exclusively. Ren's symptoms and consent remain open clinical and ethical concerns, not instant player buffs or cures.
- Clue timing preserves **Kreissack alive in Act III**, **Nova's beneficial, unprompted coolant rescue in Act IV**, **Nova's hidden conditional executive veto in Act V**. Kreissack is the only confirmed deeply incorporated person; ordinary pilot anomalies are not sufficient to prove Ren is incorporated. WAR human managers remain responsible for Ganymede, and Varga's private emotional experiments are distinct.
- New romantic pairings and civilian character are **draft proposals**, not settled user canon. Provisional group circular-order rule and nondefault NPC outcomes remain unapproved.

## Verification

- Previously passing project tests: **51** (7 tournament + 15 relationship + 13 Lyra + 16 Mara).
- Ren-specific tests: **24**, including all 32 five-bit fight-input patterns, group order, advancement, trophy, clue access, research-state, romance consent and exclusivity, and elimination fallback.
- Total intended: **75 tests**; package build independently verifies file hashes and ZIP CRC.

**Reading order:** `11_Ren_Campaign/Ren_Playable_Screenplay_v0.1.md` → `Ren_Route_Spec_v0.1.md` → route validator/tests. `00_README/COMBINED_WORKING_EDITION.md` remains historical and does **not** include Ren's current campaign.
