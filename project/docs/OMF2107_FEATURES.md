# OMF2107 Feature List

Single list of committed features with milestone mapping. Sources: spec (`OMF2097_3D_GAME_SPEC.md`), `DEVPLAN.md` (RP, formerly the release plan; wins on conflict), the task register inside it (DP IDs, from the former `OMF2097_DEVPLAN.md`), and the code state found on 2026-11-07. "Milestone" is from RP/DP; "none" means no doc assigns one.

Milestones (RP): M0 2026-11-20, M1 2027-01-15, M2 2027-03-12, M3 2027-04-30, M4 2027-07-30, M5 2027-11-30, M6 2028-01-31.

## Modes

| Feature | Milestone | State |
|---|---|---|
| Story (ten routes, Nova conclusion, per-pilot endings) | spec §6; RP Phase 3 | Ari route built (`ari.story`, 266 scenes, passes story_check) |
| Arcade / One Player | DP D04 (P1); RP none | Playable ladder for Ari, placeholder dialogue. See `OMF2107_ARCADE_MODE.md` |
| Tournament career | spec §7; first slice defined | Not started in this audit |
| Local Versus | RP M4 ("four HARs, local versus"); DP D04 | Not audited |
| Training | DP D03 (P1); RP none | Not audited |
| Options + key remapping | RP Phase 3 / M3; DP D07 (P1) | Not audited |
| Onboarding tutorial | none | Unassigned |
| Online play, console ports | deferred (RP "Later decisions", spec §13) | Out of scope |

## Combat

- Fixed side-on plane, authored hit shapes, stun, knockdown, air hits, combos, original-style finish, learnable hazards.
- Shared rules for player and AI; difficulty 0 to 6 in code.
- Replays store inputs and game version (DP D03).
- Fidelity gate: capture walk speed, jump arc, startup/recovery, hit/push distance, block response, stun and special behavior for Jaguar and one rival before tuning. 35 Jaguar and Shadow attacks measured so far (RP).

## Content

- Pilots: original ten, each with an ending; Kreissack as boss.
- HARs: original ten standard plus Nova as story boss. Unlock policy open (spec §13).
- Arenas: Stadium, Danger Room, Power Plant, Fire Pit, Desert.
- Story tools: skip and log required; critical evidence has alternate carriers.
- Presentation: portraits, short 2D scenes, in-engine scenes, dialogue panels; reduced flashes and shake option.

## Platform

Windows first, Linux where practical. 60 fps presentation target. Controller latency to be tested on hardware.

## Known doc conflicts (decide before presenting)

1. **First slice.** Resolved 2026-11-07: spec §6 now names Ari's route as the first complete slice and defers Crystal vs Christian to Phase 3, matching RP.
2. **HAR count.** Resolved by wording 2026-11-07: RP M5 now reads "ten standard HARs plus Nova as story boss", matching the spec's 11 total. Assumes "All 11" meant ten plus Nova. Revert if an eleventh playable HAR was intended.
3. **Arcade and Training have no milestone** in RP, though DP lists them as P1.
4. **Content rating.** Spec/RP include consensual adult romance and fanservice frames with consent and skip required; no rating review is stated.
