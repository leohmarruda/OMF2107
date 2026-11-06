# Dante playable route specification v0.1 — Story Pack v2.2

**Screenplay:** `Dante_Playable_Screenplay_v0.1.md` (six chapters). **Code:** `dante_route_validator.py`, `test_dante_route_validator.py`. **Canon:** `02_Story_Bibles/Dante_Character_Addendum_v2.2.md`.

## Tournament adapter (no drawn fights)

Engine Group D order is GD1 (Angel vs Dante), GD2 (Angel vs Jean-Paul, NPC), GD3 (Dante vs Jean-Paul). Dante's screenplay plays GD3 first (Days 2–4) and GD1 second (Days 5–7). Therefore `simulate_dante(jean_paul_win, angel_win, ...)` calls the tournament with `(angel_win, jean_paul_win)`.

| Dante group result | Rank | Official path |
| --- | --- | --- |
| Wins both | D1 | Q4 versus C2 (Lyra by default) |
| Beats Jean-Paul, loses Angel | D2 | Q3 versus C1 (Steffan by default) |
| Loses Jean-Paul, beats Angel | D2 under provisional circular 1–1–1 published seeds | Q3 versus C1 |
| Loses both | D3 | Eliminated; independent investigation continues |

**Default route:** Win GD3, lose GD1, lose Q3 to Steffan. If Dante wins Q3/Q4, he participates in S_CD, and if he wins it, the genuine FINAL. `S_CD` plays Day 12 after the real Nova rescue; FINAL Day 13 before the emergency. Every actual opponent comes from the simulator, not dialogue decisions. NPC knockout fallback and circular public seeding are *provisional, not author-approved canon*.

## Critical scenes

| Scene | Day | Gate |
| --- | ---: | --- |
| DV1.1/1.3 | 0–1 | All routes |
| DV2.1 GD3 | 2–4 | All routes, player result |
| DV3.1 GD1 | 5–7 | All routes, player result |
| DV3.2–3.3 | 5–7 | Breakup only if Lyra chose to leave; provocation and spite variants otherwise |
| DV4.2 | 8–10 | Real QF if qualified, real elimination branch otherwise |
| DV4.3 | 8–10 | Kreissack survival verified independently |
| DV5.1 | 11 | Varga misconduct; protected Lyra notification independent of Dante |
| **DV5.2** | **11** | **Dante confronts Steffan and identifies his repressed fixation; tone may branch, confrontation cannot be skipped** |
| DV5.3 | 12 | Genuine rescue, independent of final AI veto |
| DV5.4 | 12 | Actual SF if advanced, watch real SF if eliminated |
| DV6.1 | 13 | Official FINAL only if earned |
| DV6.2 | 13 | Later Nova veto, gateway/latch, destruction; not an official match |
| DV6.6 | 30 | Authenticated Kreissack Devroe order only now |

## Confrontation design

Dante's insight is author-established; the **mechanism** (observing Steffan's reactions, repeated footage review, and fixation on Dante's response to Lyra) is proposed writing. The script does not pretend access to Steffan's inner monologue. Dante can choose `merciless`, `clear`, `vulnerable`; spite is morally real and may have consequences, but Steffan's feeling is not altered by a dialogue choice. The default confrontation is **private**, with optional negative public fallout only if player chose to threaten exposure. His revealing Steffan's true attraction to himself is not equivalent to proving reciprocal desire from Dante.

## Relationship safety / world-state

All romance endings are *proposals*, never automatic. Relationship intent is `solo`, `lyra`, `steffan`, `mari`, or `truce`; only one can win. An intent never sets the NPC's reciprocal choice. A plausible future Lyra reconciliation requires a prior relationship, both available, Lyra's independent repair and consent, cleared Steffan commitment, repair of any cruel outburst and a real post-tournament interval. A hypothetical Steffan romance additionally requires Dante's independent desire, Steffan's reciprocal admission, accountability to Lyra, resolved prior commitments, meaningful time, and repair of any coercive control. The `merciless` confrontation or deliberate public humiliation does not immediately turn into a romantic payoff. Mari's optional relationship needs her independent active choice and resolution of Shredder safety-contract conflicts. Nonromantic endings retain full mystery access and tournament legitimacy.

## Shared external invariants

Ren/Angel confirm Kreissack's biological survival independently. Varga's unauthorized study changed encounters and recordings, not authentic love or fight results. Day-12 rescue genuinely originates from Nova's legacy safety gateway and is not ordered by Kreissack; Day-13 Nova authority over Kreissack is first definitively exposed after the official final. Kreissack destroys the unique composite core using the retention latch; his final line remains “Apparently, I can still surprise you.” The independently authenticated Devroe E5 order is not available until Day 30. Relationship choices cannot change any of these.

## Unresolved author approvals

1. Does Dante ever reciprocate Steffan's attraction, in any optional ending?
2. Should Dante retain a plausible future Lyra reconnection, or is the romance conclusively over after the default breakup?
3. Approve or reject Mari Solis as a new adult secondary character and optional Dante romance.
4. Adopt or replace the current provisional circular group seed and nondefault NPC knockout results.
