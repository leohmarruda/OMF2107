# OMF 2107 — Integration Overview v2.4

**Date:** 2026-11-02. **Change:** Selene Vale becomes the **eleventh fully drafted playable POV**, with her six-chapter campaign *The Art of Deception*, separate route contract, executable dispatcher, and tests. Previous material remains preserved; this work does not claim approval of new romances or scenes.

## New material

- `23_Selene_Campaign/Selene_Playable_Screenplay_v0.1.md` — roughly 5,350 words. A corporate-infiltration story with legitimate Mirage fights, family influence, media identity exposure, audit dilemmas, optional glamorous scenes, and divergent endings.
- `23_Selene_Campaign/Selene_Route_Spec_v0.1.md` — combat adapter, scene/relationship gates, clue provenance and unresolved author choices.
- `23_Selene_Campaign/selene_route_validator.py` — uses the single tournament authority; does not invent fight results.
- `23_Selene_Campaign/test_selene_route_validator.py` — 13 new unittest methods; all 32 fight-input patterns checked.

## Established versus proposed

**Established:** Selene (32), undercover corporate heiress, technically capable Mirage pilot, ambitious and sophisticated, morally flexible, identity/loyalty conflict; Milano flirtatious rivalry and Jean-Paul competitive rapport; default defeats to Ari and Crystal; all shared Nova and Devroe chronology.

**New proposals, not auto-canon:** Registered beneficial-ownership reveal scene, sub-vendor procurement anomaly, familial corporate mandate details, Milano and Jean-Paul as *possible* mutually consensual romance endpoints, corporate reform/acquisition choices, personal epilogues.

## Tournament decisions

- On-screen Selene–Ari `GA3` is first, then Selene–Crystal `GA2`. Engine expects `GA2` then `GA3`: explicit input adapter included.
- `00`: eliminated (A3); `10`: second (A2), Q2; `01`: eliminated (A3) under provisional circular published seed; `11`: first (A1), Q1. Bits are `(beat Ari, beat Crystal)`.
- If qualified, play actual QF on Days 8–10; S_AB **Day 11 before** the Day-12 rescue; final Day 13 if earned. Never turn a qualifying loss into a win for cinematic convenience.
- Exact opponents and winners derive from the simulator. Placeholder NPC results and seed order remain unapproved.

## Cross-campaign continuity

Selene's supplier records are an original but **limited** investigation contribution; Angel/Ren demonstrate Kreissack's biological survival on Day 9, the beneficial rescue occurs Day 12, the veto and unique Nova core destruction on Day 13, E5 Devroe evidence is independently authenticated on Day 30. She neither alters Varga's research results nor trades romance for evidence. Jean-Paul–Varga commitments and Milano's independent choices can veto romantic endings. Dante remains nonromantic toward Steffan by default, with a separate elective route. Older campaign files are unchanged and retain precedence for their protagonists.

## Validation and limits

**252/252 unittest methods passed across 17 directories**, with 13 added to the 239 in v2.3. Test methods are not a count of complete playthroughs; within the Selene tests 32 binary match input combinations are enumerated explicitly. Archive and SHA-256 verification are independent steps. The game still lacks a single integrated runtime relationship store, full authored NPC alternate matches, and editorial approval of the new relationship paths.

**Character-bible addendum:** `02_Story_Bibles/Selene_Character_Addendum_v2.4.md` consolidates established personality traits and proposed interpretations; it does not overwrite character canon.
