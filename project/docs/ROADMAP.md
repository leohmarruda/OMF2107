# OMF2107 — roadmap

Status: revised after comparing the prototype with the [original game
reference](OMF2097/OMF2097_REFERENCE.md). This is a milestone plan, not a date
commitment.

## Target

Make **OMF2107** a faithful 3D rendition of One Must Fall 2097. Fighters and arenas
gain 3D models, animation, lighting, and camera work while the match remains
readable as a side-view fighter. Preserve the game's pilot-plus-HAR selection,
directional punch/kick controls, specials, blocking, stun, combos, hazards,
WAR's contest for Ganymede, pilot rivalries and endings, and Tournament mode.
The `project/prototype` spike now uses a side-on plane and the accepted Jaguar
and Shadow silhouette blockouts. Its standalone combat values and arena remain
technical placeholders rather than the combat or story template.

The story pass should expand OMF's own neural-link, WAR, Kreissack, and Nova
themes. The [story treatment](OMF2107_LORE_v2.md) develops the
government conspiracy, relationships, and physical cost of an experimental
link while keeping the setting, cast, and central tournament.
The [game specification](OMF2097_3D_GAME_SPEC.md) defines the target modes,
combat rules, presentation, production architecture, and acceptance gates.
The [development plan](OMF2097_DEVPLAN.md) breaks these into tasks,
dependencies, and phase exit checks.

## Technical approach

Keep OpenOMF as the mechanical reference and working baseline. It already
parses the original data and implements fights, story scenes, Tournament,
recordings, and tests. Before choosing how much to port or replace, make one
side-by-side match study: movement speed, facing, jump arc, hit timing, stun,
guard, and one HAR's specials. A production 3D engine may handle models and
animation, but gameplay parity is the measure of success. Do not commit to a
full engine migration until that study and a 3D match spike are complete.

**Fight engine decision (2026-10-15):** OMF2107 does not get a new combat engine.
Every fight runs on OpenOMF's reverse-engineered rules with the original AF/BK
data; the 3D view only renders the per-tick state it publishes. The prototype's
built-in combat loop is now a `--sandbox`-only placeholder and is no longer the
default. Gameplay must not be changed to make an effect visible: for example,
Shadow's shadow attacks (Shadow Punch, AF move 23) only have a script at
enhancement level 3, exactly as in the original Tournament, so the live
launchers expose that as an explicit `-ShadowEnhancement 3` option instead of
forcing it.

[OMF 2097 Remastered](https://github.com/Jared-woodruff/OMF-2097-Remastered)
(local sibling `../OMF-2097-Remastered`) was reviewed as an alternative. Its
MIT-licensed TypeScript fight code is a function-by-function port of OpenOMF,
runs headless in Node, parses the same original files, and has tick-for-tick
determinism tests. It is not adopted now because it has no parity tests
against OpenOMF, no per-tick state export, and no 3D renderer, and because the
OpenOMF trace, shared-memory live link, REC fixtures, and baselines already
exist. Revisit it at B08 if the production client moves to a web/TypeScript
stack; it would then need the same state exporter and REC parity checks.

## Milestones

| Stage | Deliverable | Completion check |
| --- | --- | --- |
| 0. Source baseline | Catalog pilot/HAR/arena/story data and rights; capture reference matches | Reference sheet includes controls, move timing, HUD, hazards, selection flow, and images from OMF. |
| 1. 3D fidelity spike | Jaguar and one rival, Stadium, side-on camera, 3D models, original-style movement | Players recognize the match as OMF: spacing, jumps, facing, punch/kick, and block behave like the source baseline. |
| 2. Combat vertical slice | Pilot-plus-HAR selection, one complete HAR move set, stun, combos, round flow, second arena hazard | A recorded source match and 3D match can be compared move by move; victory and defeat work. |
| 3. Visual and audio direction | Approved HAR silhouettes, arena material and lighting language, HUD, impacts, music approach | Fight remains readable at normal speed; original machines and arenas are recognizable in 3D. |
| 4. One-player story | WAR/Ganymede setup, pre-fight exchanges, Kreissack/Nova arc, pilot-specific outcome | One pilot's entire story route can be played from selection to ending. |
| 5. Tournament foundation | Custom pilot, winnings, upgrades, training, repair/economy, tournament progression | A pilot can enter, earn money, improve a HAR, and advance through a short bracket. |
| 6. Roster and release | Remaining pilots/HARs/arenas, local versus, controller support, options, packaging | Content and playtests meet agreed parity targets; every distributed asset has recorded provenance and permission. |

## Immediate next work

1. Finish the **original-game baseline**. Isolated range, timing, and guard
   checks now cover all 35 Jaguar and Shadow attacks in
   [OMF2107_MOVE_MEASUREMENTS.md](OMF2107_MOVE_MEASUREMENTS.md) (Shadow Grab holds
   rather than damages, and Shadow Punch is measured at enhancement 3).
   Signature traces, Stadium
   wall response, and a replayable source-driven match are recorded. Full-match
   readability has had a human playtest with both the blockout and Meshy
   models (2026-10-27): both judged good.
2. Human-review of close-contact punch/kick spacing and signature poses at
   normal speed was part of that playtest; source-replay captures verify the
   sampled contact positions without changing OpenOMF timing or results.
3. Stadium staging has an enclosed bowl, stepped crowd stands, and a central
   board. The blockout launcher (`run-blockout.ps1`; `run-meshy.ps1 -Fight` for
   the Meshy stand-ins) opens an in-game selection screen that connects ten
   playable pilots to Jaguar or Shadow, using their OpenOMF stats. The full
   Stadium match was human-tested while OpenOMF owns combat timing/results.
4. Compare that playable match against the [recorded model match review](OMF2107_MODEL_MATCH_REVIEW.md)
   before expanding the roster or adding story scenes. **Compared 2026-10-27:**
   facing, hit timing, and recovery match the OpenOMF recordings, including
   Jaguar's close throw and Shadow Grab; the playtest found no mismatch with the
   source apart from the items below. Body overlap during kicks, falls,
   crossings, and throws is accepted because OpenOMF has no body collision. A
   Shadow Grab projection facing error was a stale executable, not a code fault
   (rebuild with `build.ps1 -Config Debug` after editing `main.c`; the
   `run-blockout*.ps1` launchers do not build). **Gate closed 2026-10-27**; carried over
   into Stage 4 as polish, none a source-fidelity problem:
   - Shadow's close throw (animation 20) is now recorded
     (`rectests/SHADOW-CLOSE-THROW.REC`) and compared. Its anomalies were a
     fixture teleport at tick 123 (watch from tick 124) and source frames and
     facing changes, not renderer faults; the facing turn is now eased in the
     viewer, which still needs a live look.
   - The ice-blade sequence (`rectests/SHADOW-ICE-BLADE.REC`) was watched live and
     judged better after the air flash was removed and the blade ramped in; the
     Jaguar concussion shot has been reviewed by screenshot only.
   - Shadow's purple figures have no trails (the renderer has no transparency).
   - Skinned deformation rigs remain deferred to the finished asset pass.
5. Stage 4 planning has started: see [OMF2107_STAGE4_PLAN.md](OMF2107_STAGE4_PLAN.md)
   for the proposed scope, work order, and open decisions. **Ari's route is scripted end to end
   (2026-11-06):** `project/data/story/ari.story` holds Chapters 1 to 6 of the Story Pack (216 scenes), with
   the Group A, bracket and championship branches from the route spec and a two-fight Nova boss. It passes
   `story_check`, and `story_check walk` (random choices and fight results; 300 to 1000 runs per HAR, checked
   2026-11-06) reaches the ending every time. Every character shown with `present` now has a portrait. Still
   open: a live playtest of the route (`run-story-ari.ps1`), portraits for Kreissack, Nova and the one-line
   extras, NPC results that are only provisional defaults, and the optional scenes that were not converted.
6. In parallel, pose and mesh authoring: mesh landmarks
   (`project/data/mesh_landmarks.json`, landmark editor) and projection-pose
   matching (`match_projection_poses.py`) feed the pose catalog; see
   [POSE_AUTHORING.md](POSE_AUTHORING.md).

7. Release path (2026-11-05): see [RELEASE_PLAN.md](RELEASE_PLAN.md) for the dated phases,
   [ENGINE_PATHS.md](ENGINE_PATHS.md) for the data-free engine choice and
   [HAR_PIPELINE.md](HAR_PIPELINE.md) for the streamlined modeling flow.

## Scope boundaries

- **First playable:** one faithful match with pilot and HAR choice, source-like
  controls, and one recognizable arena.
- **First story slice:** one existing pilot route in WAR's Ganymede contest,
  including original-style banter and an ending.
- **First Tournament slice:** custom pilot, prize money, an upgrade, and a
  short bracket.
- **Later decisions:** full roster, advanced cinematics, network play, and
  modes beyond the original. These follow a successful match and rights review.

## Rights checkpoint

**Decision (2026-11-05):** free, non-commercial fan project that keeps the name, HARs,
pilots and references to the original, and ships only original assets. The research,
release rules, accepted name risk, permission-request draft and replacement checklist
are in [RIGHTS.md](RIGHTS.md).

OpenOMF's code is MIT licensed, but the original game's artwork, audio, text,
character designs, and name need their own distribution assessment. The local
`OMF2097` folder is useful as a development reference; its presence is not a
release license. Maintain an asset provenance list throughout production; the [asset ledger](ASSET_LEDGER.md)
holds it (started 2026-10-27 with the original pilot portraits used locally in the story prototype).

## References

- [Original game reference](OMF2097/OMF2097_REFERENCE.md)
- [Story treatment](OMF2107_LORE_v2.md)
- [Game specification](OMF2097_3D_GAME_SPEC.md)
- [Development plan](OMF2097_DEVPLAN.md)
- [OpenOMF repository](https://github.com/omf2097/openomf)
- [Original manual story](https://www.omf2097.com/wiki/doku.php?id=omf2097:story)
- [Decoded in-game help and text](https://www.omf2097.com/wiki/doku.php?id=omf2097:english.dat)
