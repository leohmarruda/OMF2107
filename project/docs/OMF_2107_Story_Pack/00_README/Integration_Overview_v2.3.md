# OMF 2107 — Integration Overview v2.3

**Date:** 2026-11-02. **Scope:** Author-established Dante/Steffan default nonromantic, optional player-created romance. No new character campaign or revised match outcomes.

## Canon decision

Dante is more emotionally mature than Steffan and recognizes Steffan's denied attraction, but his **default feelings are nonromantic**. The player may alter his trajectory over time, developing attraction if he chooses to learn more about Steffan, listen after the Day-11 confrontation, and later deliberately explore a reciprocal relationship. Steffan's attraction is already established; Dante's possible attraction must emerge through player choices, not an assumed hidden desire. Steffan may still be cruel, envious, and controlling toward Lyra, and romance is not an automatic redemption.

## Active updates

- `02_Story_Bibles/Dante_Character_Addendum_v2.3.md` — authoritative user decision; v2.2 retained.
- `02_Story_Bibles/Steffan_Character_Addendum_v2.3.md` and `Master_Story_Bible_v2.7.md` — compatible default/alternate relationship language.
- `22_Dante_Campaign/Dante_Playable_Screenplay_v0.2.md` — new DV2.3 professional curiosity seed, DV5.2 private contact choice and DV6.4 future exploration; default explicitly nonromantic.
- `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.3.md` — Steffan-side consistency; revised optional epilogue.
- `22_Dante_Campaign/Dante_Route_Spec_v0.2.md` — branch gates.
- `dante_route_validator.py` + tests — default values and three-stage player progression required for a romantic future.

## Default versus elective path

| Beat | Default | Optional player course |
| --- | --- | --- |
| Days 2–4 | Professional respect, no romance | Curious about Steffan as a person |
| Day 11 | Private confrontation and firm nonromantic boundary | Listens and leaves personal contact open |
| Day 13+ | Rivalry, distance or truce | Chooses to explore newly developing desire |
| Months later | Single, independent, or other nonromantic ending | Possible reciprocal romance **only** if both independently choose it after accountability |

All key investigations, official fights and Nova final events are independent of romantic choices. The optional ending is not achieved merely through an intent flag, sympathy for Steffan, or winning a fight. Lyra has agency and is not required to forgive either man.

## Unresolved / limits

Narrative timing and dialogue are editorial drafts. A unified runtime relationship store has not yet been implemented across all campaigns; Steffan's existing route model exposes external Dante-consent inputs, which must be driven by the actual shared world state in a game implementation. Three-way circular group seeding and nondefault NPC results remain provisional.

Run `python 00_README/run_all_tests.py` for reproducible test counts.
