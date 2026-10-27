# Asset ledger

Records where each non-original asset comes from, how it is used, and whether it may be distributed. The
[roadmap's rights checkpoint](ROADMAP.md#rights-checkpoint) and the [development plan](OMF2097_DEVPLAN.md)
(tasks A06 and F05) require this: original-game artwork, audio, and text have not been cleared for release, and
only entries marked distributable may go into a release package.

This ledger was started on 2026-10-27 with the first entry below. Other local reference material (original
sprites and poses in `project/docs/OMF2097/`, the Remastered captures, and so on) has not been inventoried here yet.

| Asset | Origin | Intended use | Where it lives | Replacement status | Distribution status |
| --- | --- | --- | --- | --- | --- |
| Pilot portraits (the ten playable pilots) | Original One Must Fall 2097 data: `OMF2097/MELEE.BK`, animation 4, sprite per pilot id. Exported by `project/tools/export_pilot_portraits.py`. | Shown on the story mode selection screen of the 3D prototype, by the project owner's decision (2026-10-27). | `project/build/portraits/<Pilot>.bmp`, a git-ignored folder; never committed. | To be replaced by new artwork before any release. The viewer shows plain placeholder cards when the files are absent. | **Local development only. Not distributable.** No rights assessment has been made. |
