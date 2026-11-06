# OMF 2107 — Integration Overview v2.2

**Date:** 2026-11-02. **Scope:** Tenth full playable pilot campaign, Dante Vey: *What You Cannot Win*. Updates Steffan and Lyra cross-POV scenes, the active Master Bible, and cross-route checks. All former revisions are retained for provenance.

## User-established characterization

Dante is comparatively **more mature and aware** than Steffan, but passionate and prone to anger and spite when Steffan interferes with Lyra. He eventually **confronts Steffan and exposes the truth**: Steffan envies him, desires his attention, has denied attraction to him, and partly used genuine attraction to Lyra as a vehicle for imagining dominance over Dante. Dante's ability to see this doesn't mean he responds kindly; players can make his accurate insight cruel. Dante's reciprocal attraction to Steffan remains **unestablished**.

## New/updated materials

- `22_Dante_Campaign/Dante_Playable_Screenplay_v0.1.md`: six chapters (~4,600 words). Distinct athletic, social and technical-evidence arc; harsh or restrained confrontation, a valid early-elimination investigation, optional secondary relationship with proposed adult technician Mari Solis, optional fanservice, and several post-tournament endings.
- `22_Dante_Campaign/Dante_Route_Spec_v0.1.md`: scene timeline, relationship eligibility and official tournament adapter.
- `22_Dante_Campaign/dante_route_validator.py`: actual wins/losses drive standings, quarterfinal, semifinal, final and champion. Dante's screen-fight order (GD3 Jean-Paul, GD1 Angel) is reversed for the shared simulator (GD1, GD3).
- `22_Dante_Campaign/test_dante_route_validator.py` and `test_dante_cross_pov.py`: tournament, romance, knowledge timing and cross-protagonist consistency.
- `02_Story_Bibles/Dante_Character_Addendum_v2.2.md`: author-established psychological direction separated from scene proposals.
- `02_Story_Bibles/Master_Story_Bible_v2.6.md`: Dante canon supplement; older Master v2.5 preserved.
- `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.2.md`: Day-11 confrontation `ST5.1b` synchronizes with Dante's `DV5.2`, while `ST5.4` is now an optional later follow-up.
- `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.4.md`: Lyra rejects being used as proxy in Dante's confrontation; fixes placement of the Day-12 rescue after Day-11 Varga evidence and breakup, before semifinal. Keeps identifier `L5.0` for the rescue to avoid breaking any older scene references.

## Default narrative and combat

Dante beats Jean-Paul and loses to Angel in Group D; he qualifies D2 and loses Q3 to Steffan. Steffan later loses legitimately to Lyra; Ari is the default champion. Varga's research altered exposure and media but did not induce love or manipulate fights. Dante confronts Steffan on Day 11 after the Varga findings; Lyra's notification remains independently secure. Day 12: real Nova rescue before any semifinal. Day 13: actual official final before Kreissack discovers Nova's conditional veto and sacrifices himself, destroying the single unique composite core. Day 30: independently authenticated Kreissack E5 murder order is learned. All fights have decisive outcomes; any equal *standings* require a published tiebreaker, still provisional.

## Romantic and ethical branches

Dante can desire reunion with Lyra, explore a *possible future* reciprocal bond with Steffan, consider a proposed secondary romance with Mari, choose a professional truce, or remain solo. Romance never follows from victories or a humiliating disclosure. Each person must independently choose; Steffan's and Lyra's competing relationships cannot be assigned by Dante's desire. An optional public exposure variant is destructive, rather than a glamorized way to claim Steffan.

## Validation and limitations

Run `python 00_README/run_all_tests.py`. There are **232 passing unit-test methods in 16 directories** in this revision (214 previously, 18 new Dante checks). These test branching invariants, not scene quality, completeness of a runtime global relationship database or actual NPC consent. Default fixture integrity and individual match definitiveness remain checked; nondefault NPC knockout priority and 1–1–1 public seeding remain **draft placeholders**.

**Open creative decisions:** Dante–Steffan reciprocal attraction, optional Dante–Lyra reunion, new Mari Solis relationship, precise exposure fallout and official circular group-ranking rule. All other players' prior active campaigns remain unchanged.
