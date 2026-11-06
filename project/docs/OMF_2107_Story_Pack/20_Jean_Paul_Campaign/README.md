# Jean-Paul: The Observer Effect — playable pilot campaign v0.1

> **Current versions (see `../00_README/CURRENT_FILES.md`):** `Jean_Paul_Playable_Screenplay_v0.5.md` with `Jean_Paul_Route_Spec_v0.1.md` (the v0.1 screenplay named below is superseded and kept in place because a validator test reads it).

- **Active narrative:** `Jean_Paul_Playable_Screenplay_v0.1.md` — six chapters / approximately 5,500 words, plus Day-30 epilogue.
- **Branch design:** `Jean_Paul_Route_Spec_v0.1.md` — relationship gates, knowledge chronology, consent, evidence, tournament progression.
- **Executable selected-pilot route:** `jean_paul_route_validator.py` — standard-library Python dispatcher using the shared group and knockout bracket.
- **Tests:** `test_jean_paul_route_validator.py` — local unit and static chronology checks.

This adds Jean-Paul as the **eighth** fully scripted selected-pilot POV alongside Ari, Lyra, Mara, Ren, Angel, Crystal, and Raven. The existing original game roster has 12 fighters and is **not** altered. The default result remains Jean-Paul's elimination in Group D; player victory alternatives follow actual match results. The default Varga relationship has a more sustained narrative treatment; Selene romance is a **proposal**. Fanservice is optional, adult and linked to characterization.

**How to test:** From the pack root run `python -m unittest discover -s 20_Jean_Paul_Campaign -v`. To verify all modules use `python -m unittest discover -s <each numbered test directory>` because prior versions contain separate modules and duplicate top-level names.

**Authority:** Current screenplay for Jean-Paul alone; it does not overrule the v1.9 shared Kreissack finale, the v1.7 Devroe E5 clock, or actual game results. `00_README/COMBINED_WORKING_EDITION.md` remains an older historical snapshot, not the current selected-pilot compilation.
