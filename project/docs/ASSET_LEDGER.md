# Asset ledger

Records where each non-original asset comes from, how it is used, and whether it may be distributed. The
[release plan's rights checkpoint](RELEASE_PLAN.md#rights-checkpoint) and the [development plan](OMF2097_DEVPLAN.md)
(tasks A06 and F05) require this: original-game artwork, audio, and text have not been cleared for release, and
only entries marked distributable may go into a release package.

Release position (2026-11-05): free fan project with original assets only, keeping the original names; see
[RIGHTS.md](RIGHTS.md). Every "Not distributable" entry below must be replaced before a public release.

This ledger was started on 2026-10-27 with the entries below. Other local reference material (original
sprites and poses in `project/docs/OMF2097/`, the Remastered captures, and so on) has not been inventoried here yet.

| Asset | Origin | Intended use | Where it lives | Replacement status | Distribution status |
| --- | --- | --- | --- | --- | --- |
| Pilot portraits (the ten playable pilots) | Original One Must Fall 2097 data: `OMF2097/MELEE.BK`, animation 4, sprite per pilot id. Exported by `project/tools/export_pilot_portraits.py`. | Shown on the story mode selection screen of the 3D prototype, by the project owner's decision (2026-10-27). | `project/build/portraits/<Pilot>.bmp`, a git-ignored folder; never committed. | To be replaced by new artwork before any release. The viewer shows plain placeholder cards when the files are absent. | **Local development only. Not distributable.** No rights assessment has been made. |
| Arena backdrops (five arenas: Stadium, Danger Room, Power Plant, Fire Pit, Desert) | Original game data: the background image of `OMF2097/ARENA0.BK` to `ARENA4.BK`. Exported by `project/tools/export_story_assets.py`. | Behind story scenes whose `bg` names an arena (`stadium`, `danger room`, `power plant`, `fire pit`, `desert`), by the project owner's decision (2026-10-27). | `project/build/backdrops/<arena>.bmp`, git-ignored; never committed. | Replace with new artwork before release. Without the files the viewer draws a generated stand-in. Each also has a smooth 4x upscale, `<arena>_hd.bmp` (`project/tools/story_upscale.py`), which the viewer prefers; it is derived from the original and is equally local-only. | **Local development only. Not distributable.** No rights assessment has been made. |
| Menu sound effects (move and press) | Original game data: two samples of `OMF2097/SOUNDS.DAT` (engine sample indices 19 and 20). Exported by `project/tools/export_story_assets.py`. | Played by the story viewer for menu movement, choices, and starting a match, by the project owner's decision (2026-10-27). |
| Story music: the original soundtrack (`MENU`, `ARENA0` to `ARENA4`, `END`) | Original game data: the tracker modules `OMF2097/MENU.PSM`, `ARENA0.PSM` to `ARENA4.PSM`, and `END.PSM`, decoded at run time with libxmp. Nothing is exported or copied. | Background music in the story viewer, chosen by the script's `music` command, by the project owner's decision (2026-10-29). | Read at run time from the local `OMF2097/` folder. | Replace with new music before release. Without the files the story is silent. | **Local development only. Not distributable.** No rights assessment has been made. |
| Battle sound effects and music | Original game data, played directly by OpenOMF from `OMF2097/` (`SOUNDS.DAT` and the `.PSM` music) during a story match started with `-Sound`. Nothing is exported or copied. | Sound in story matches, by the project owner's decision (2026-10-27). | Read at run time from the local `OMF2097/` folder. | Replace with new sound before release. A match started without `-Sound` is silent. | **Local development only. Not distributable.** No rights assessment has been made. |
| Sound effects, continued | | | | | | `project/build/sounds/<name>.wav`, git-ignored; never committed. | Replace with new sounds before release. Without the files the viewer is silent. | **Local development only. Not distributable.** No rights assessment has been made. |
| Illustrated-sequence frames (opening: title, Crystal and Christian cards, two face-offs; before each match: four hangar frames `bay_<pilot>_<har>`; after it: two newsroom frames `news_<pilot>` and four repair-bay frames `wreck_<har>_<result>` of damaged HARs; ending: two cards, together, apart, title) | Composed by `project/tools/build_story_art.py` from original game material (the pilot portraits and the Stadium and Desert backgrounds above, the hangar picture of `OMF2097/VS.BK` exported to `project/build/scenes/`, plus the idle sprites of `OMF2097/FIGHTR0.AF` and `FIGHTR1.AF`) with diagonal bars, a vignette, name plates, and text drawn by the tool. | The scripted opening and endings of the draft story, by the project owner's decision (2026-10-27). | `project/build/art/<name>.bmp`, git-ignored; never committed. | Replace with new artwork before release. Without the files the viewer shows the scene's backdrop instead. Each frame also has a smooth 4x upscale, `<name>_hd.bmp`, which the viewer prefers. | **Local development only. Not distributable** (the composition is project-made, but it is built from original material). |
| Scene backdrops: green room, medical bay, and a stand-in Stadium | Drawn by the viewer's own code in `project/prototype/main.c` as flat coloured shapes; no original material. | Story scenes without an exported original arena image. | In the source code. | Placeholder art; improve or replace as the visual direction develops. | Project-made, so distributable with the code. |

## Private playtest packages

On 2026-10-29 the project owner decided to send a playtest package to a tester that includes the original game data
(`OMF2097/`), the exported portraits, backdrops, sounds and illustrated frames above, and the music, so the build runs
out of the box. `project/scripts/package-playtest.ps1` builds it into the git-ignored `dist/` folder. This does not make
any asset distributable: the package is for the named tester only, its README says not to share it, and it must not
be published, uploaded, or attached to a release. Record the recipient and date here when it is sent.
