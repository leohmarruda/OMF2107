# Selene — route and continuity specification v0.1

**Scope:** Six-chapter proposed playable campaign, *The Art of Deception*, for Selene Vale, age 32, with Mirage. Does not amend the locked 2092 Devroe, Day-13 Nova or default tournament outcome. Does not canonize Milano–Selene or Jean-Paul–Selene romance.

## 1. Tournament

**Screen order:** GA3 Selene–Ari first (Days 1–2), GA2 Selene–Crystal second (Days 5–7). **Engine order:** GA2 then GA3. `simulate_selene(ari_win, crystal_win, ...)` passes `(crystal_win, ari_win)` to the shared tournament simulator.

| Selene beats Ari? | Selene beats Crystal? | Group A outcome | Qualification |
| --- | --- | --- | --- |
| No | No | A3, 0–2 | None (default) |
| Yes | No | A2, 1–1 | Q2 vs B1 |
| No | Yes | A3, circular 1–1–1, published seed order Crystal–Ari–Selene | None (provisional ranking) |
| Yes | Yes | A1, 2–0 | Q1 vs B2 |

Q1/Q2 are Days 8–10. If the player wins her quarterfinal, she reaches S_AB on **Day 11**, before the genuine Day-12 rescue. If she wins S_AB, the final occurs on Day 13. A selected-pilot knockout loss or group elimination instead triggers honest witness/investigation scenes. The separate Nova encounter is reachable in every route. All matches have exactly one winner and one loser. Alternate NPC-only knockout results are still **noncanonical priority placeholders**, not authored game outcomes. The circular ranking mechanism remains provisional and needs author approval before final game implementation.

## 2. Scene gates

| Marker | Day | Gate / context |
| --- | --- | --- |
| SV1.1–1.4 | 0–1 | Arrival, corporate cover, engineering, optional adult dance |
| SV2.1 GA3 | 1–2 | Selene–Ari, actual result |
| SV2.2–2.4 | 2–4 | Public procurement, Jean-Paul optional, Crystal training |
| SV3.1 GA2 | 5–7 | Selene–Crystal, actual result |
| SV3.2 | 7 | Either real qualification or early-elimination investigation |
| SV3.3–3.5 | 7 | Legally valid registration, ownership exposure, optional Milano attraction, family mandate |
| SV4.1 | 8–10 | Corporate procurement evidence, distinct from biological proof |
| SV4.2 | 8–10 | Real QF only if A1/A2; otherwise records investigation |
| SV4.3 | 9 | Independent Angel/Ren Kreissack survival proof |
| SV4.4 | 9–10 | Optional Jean-Paul connection, professional boundaries |
| SV5.1 | 11 | Family/Milano business offers |
| **SV5.3** | **11** | **Real S_AB only if earned; always before Day-12 coolant rescue** |
| SV5.2 | 12 | Actual Nova-initiated rescue; imperfect Kreissack attribution, no proven veto yet |
| SV5.4–5.5 | 12+ | Optional mutually chosen Milano / Jean-Paul scenes; neither guaranteed |
| SV6.1 | 13 | Real final iff earned, with true winner |
| SV6.2 | 13 | Nova veto reveal, gateway damage, hardwired retention latch, unique core destruction |
| SV6.3–6.4 | 13+ | Business and personal outcomes; romance only via shared eligible state |
| SV6.5 | 30 | Authenticated Devroe E5 evidence, never before |

## 3. Relationship choices

**Default:** Selene remains single and professionally independent. Optional, mutually exclusive future routes: `milano`, `jean_paul`, `friendship`, `solo`. These are **proposals**. A selected relationship intent is *not* proof of reciprocation.

- Both persons must be adults, currently available and individually consenting; no unresolved exclusive relationship, and no material quid pro quo involving trade secrets, sponsorship, employment or evidence.
- Milano relationship requires mutual attraction, independent commitment, time, and separation of corporate authority. A gala dance or rooftop kiss is not a merger or automatic commitment.
- Jean-Paul relationship requires Varga's prior relationship to have ended by his own independent choices, ongoing availability, time and mutual interest. His Varga investigative evidence cannot be bartered for intimacy.
- Selene is entitled to nonromantic trust with Ari, Crystal, Leena, Cossette, Ibrahim and other cast members; professional disagreement does not create attraction.
- The existing shared-state relationship service remains the authority for NPC commitments. The route validator is a selected-playthrough projection, not a global state engine.

## 4. Mystery and moral economy

Selene's value is a **lawful money-and-contract trail**, not omniscient access to Nova's interior. Her procurement anomalies can corroborate that WAR still financed Nova-era infrastructure. Angel/Ren supply biological proof on Day 9 and command-attribution anomaly after the genuine rescue on Day 12; covert executive veto is confirmed only on Day 13. Varga's illicit research and Ganymede's human wrongdoing remain separate; Kreissack's 2092 assassination order is independently authenticated by Christian on Day 30.

`identity_strategy`, `family_mandate`, `investigation` and `business_strategy` affect credibility, legal risk, alliances, and epilogues. **They never change** victory, the physical Nova finale, or the independent minimum evidence set. Exploiting the crisis is permitted as a dark route, but it has identifiable legal/personal consequences and does not magically erase public records.

## 5. Editorial status / open choices

1. Approve details of Selene's corporate cover and family organization; only her undercover-heiress status and valid event entry are already established.
2. Decide if Milano and/or Jean-Paul should become major reciprocal romance branches, rather than passing flirtations. Neither is established as an active partner.
3. Approve the specific supplier-identifier trail, exposure scene and Selene's contribution to the gateway shutdown; they are draft mechanisms rather than source canon.
4. Replace/ratify the provisional published seed for three-way Group A standings; provide authored alternate NPC matchup results.
5. Decide whether to adapt other POVs to reflect Selene's identity reveal and corporate disclosures. None is silently overwritten in v2.4.

## 6. Reproducibility

Use `python 00_README/run_all_tests.py` from the pack root to run all suites, including `23_Selene_Campaign/test_selene_route_validator.py`. Tests cover all 32 five-bit fight patterns (unused knockout inputs ignored), chronology, qualification gates, independent evidence, romance eligibility, and integrity. They do not certify dialogue quality or adjudicate every multi-character mixed-playthrough combination.
