# OMF2115 — side-on 3D fidelity spike

## Shadow visual references

The approved [Shadow front, back, and side modeling references](../robots/shadow/canonical/README.md) are the visual source of truth for OMF2115's Shadow mesh. They define the featureless dark face opening with only green eyes, triangular shoulder/chest armor, ribbed limbs, and hand, elbow, and knee spikes. The [earlier concepts](../robots/shadow/front/README.md) remain available for comparison.

## Jaguar visual references

The approved [Jaguar front, back, and side modeling references](../robots/jaguar/canonical/README.md) are the visual source of truth for OMF2115's Jaguar mesh. They define the selected helmet, eyes, chest emblem, three-digit hands, armor proportions, materials, and two-panel rear head. The pose gallery below remains a reference for the original robot's movement and identity.

Run `powershell -ExecutionPolicy Bypass -File project/scripts/export-jaguar-poses.ps1`
from the repository root to extract 16 original Jaguar poses from the local
game data. The picture list is written to `project/docs/OMF2097/poses/jaguar/index.md`. These
side-view sprites complement the approved three-view modeling reference.

For the complete robot roster, run
`powershell -ExecutionPolicy Bypass -File project/scripts/export-robot-poses.ps1`.
It writes a roster index to `project/docs/OMF2097/poses/index.md` and a 16-pose picture
list for each of the 11 robots, including Nova. Attack frames are mapped from
each robot's own animation file because their move IDs differ.

For higher-resolution move captures, run
`py -3 project/tools/render_remastered_poses.py` after the original export.
It matches every indexed frame to the local sibling OMF 2097 Remastered HD
atlas and writes `project/docs/Remastered/poses/index.md`, 16 HD poses for each of the
11 original robots and four new Remastered robots, and
`project/docs/Remastered/poses/manifest.csv` with exact image provenance. The new
robots (Glacier, Tempest, Helix, and Spectre) come from Remastered's optional
*New robots and arenas* mod and have no original-game counterparts. The original
gallery stays available for comparison. The HD images are visual references;
the approved OMF2115 three-view sheets still define the robot designs.

This is a standalone, asset-free prototype beside OpenOMF. It now tests a
side-on camera, one gameplay plane, discrete facing, a basic jump, punch,
kick, back-to-block guard, a simple opponent, health, and brief title/result screens. Both
robots now use **editable Jaguar and Shadow low-poly mesh blockouts** based on the approved
three-view references. The models show their contrasting chest, helmet,
limb, hand, and accent shapes. A generated render-data header loads the same
parts into this prototype; its rigid-part joint rig is not a final skinned rig.
Their silhouettes were accepted for the prototype milestone on 2026-10-14.
Other HARs still use the generic placeholder robot. The asset-free arena now
uses a Stadium blockout: an enclosed roof, stepped seating, abstract crowd
silhouettes, and a central arena board. It is new prototype geometry, not
original Stadium art.
The combat values are provisional and have not been matched to OpenOMF. The
prototype does not load or alter the original game's data.

## Play

**Fights use the original-game engine.** Start a match with
`run-blockout.ps1` to open the in-game fighter selection screen and choose a pilot
and either modeled HAR, or use
`run-blockout-jaguar.ps1` and `run-blockout-shadow.ps1` for the original pairings
(see *Live Jaguar–Shadow experiment* below). OpenOMF resolves all combat and the 3D window only renders
it. Running the executable without a mode now prints these options instead of
starting the provisional built-in fight.

The table below applies only to `omf3d_prototype.exe --sandbox`, the old
standalone combat loop. Its values are not OMF rules; it is kept for rendering
experiments and `--self-test`.

Build with `BUILD_3D_PROTOTYPE=ON` and run the `omf3d_prototype` target from its
build directory. The verified Windows Debug executable is
`build/omf_debug_z7/omf3d_prototype.exe` (paths in this folder's docs are from the
repository root). It needs an OpenGL 3.3 capable driver.

| Key | Action |
| --- | --- |
| Enter | Deploy or confirm the post-fight choice |
| Left / Right (or A / D) | Select Yes / No at “Try again?” |
| Y / N | Restart / quit immediately at the post-fight choice |
| A / D | Move left / right on the fighting plane |
| W | Jump (press once per jump) |
| J / K | Punch / kick (hold to repeat) |
| Hold away from opponent | Block while grounded |
| Escape | Quit |

Run `build/omf_debug_z7/omf3d_prototype.exe --self-test` for the headless
combat check. It verifies a reachable win, facing after a side crossing,
jump/landing, and back-to-block on either side. Run the same executable with
`--capture` from the project root
to save a hidden-window render at `project/build/omf3d_sideon_capture.bmp`.

## Inspect Jaguar and Shadow

For the repeatable process of inventorying source moves, exporting reference
frames, authoring pose data, and checking coverage, see the
[pose authoring workflow](../docs/POSE_AUTHORING.md).

Run `build/omf_debug_z7/omf3d_prototype.exe --model-preview` to inspect the
two blockouts at a larger scale without starting a fight. Press **1** for the
right-side view, **2** for front, **3** for back, **4** for punch, **5** for kick,
**6** for guard, **7** for crouch, **0** for idle, and **Escape** to close it.
Press **8** for walk, **9** for jump, **H** for hit, and **M** for a signature
move pose. For a repeatable visual review, run the executable with
`--model-preview-capture` from the repository root. It saves
`project/build/omf3d_model_side.bmp`, `project/build/omf3d_model_front.bmp`,
`project/build/omf3d_model_back.bmp`, and side-view `punch`, `kick`, `guard`,
`crouch`, `walk`, `jump`, `hit`, and `special` files with the same prefix. These
are renders of the editable blockout meshes,
not copies of the approved concept images. Compare them with the
[Jaguar](../robots/jaguar/canonical/README.md) and
[Shadow](../robots/shadow/canonical/README.md) references before refining the
meshes.
The runtime pose rig places shoulder, elbow, wrist, hip, knee, and ankle joints
and keeps armor segments connected through punch, kick, guard, and crouch poses.
Crouching lowers the torso and bends the hips and knees while the feet stay
planted, instead of shrinking the whole model.
The signature poses use Jaguar animation 21 and Shadow animation 23 sprite
keys. They were compared with exactly matched Remastered frames. The
[source trace](../docs/OMF2115_SIGNATURE_MOVE_TRACE.md) now records their timing,
near/far health changes, and active projectile positions. The 3D replay
displays a cyan shot and a purple Shadow duplicate as visual blockouts.

To regenerate the embedded model data after editing either blockout, run
`py -3 project/tools/generate_model_meshes.py` and rebuild the target.

## Live Jaguar–Shadow experiment

From the repository root, run `powershell -ExecutionPolicy Bypass -File project/scripts/run-blockout.ps1`
to choose Jaguar or Shadow and one of the ten playable pilots. The pilot's
original power, agility, and endurance values are used by OpenOMF. The rival
remains the canonical pilot of the other HAR: Shirro/Shadow or Crystal/Jaguar.
For a direct launch, pass `-Har Shadow -Pilot Angel` (for example). This is a
The live HUD echoes both pilot names so the chosen pilot remains visible during
the match. The selection screen uses Up/Down for the robot, Left/Right for the
pilot, Enter to start, and Escape to cancel.

From the repository root, run `powershell -ExecutionPolicy Bypass -File project/scripts/run-blockout-jaguar.ps1`.
This starts an OpenOMF Stadium match with Crystal/Jaguar against Shirro/Shadow
and opens the 3D view. OpenOMF resolves movement, attacks, guarding, damage,
and the AI; the 3D window displays each completed source tick.
Run `powershell -ExecutionPolicy Bypass -File project/scripts/run-blockout-shadow.ps1`
to start the same match with Shirro/Shadow
under your control against Crystal/Jaguar. Both launchers accept
`-CaptureTick`, `-WarmupSeconds`, and `-Pilot`; the Jaguar launcher also accepts
`-Player Shadow` for the same setup. Without `-Pilot`, the defaults remain
Crystal/Jaguar and Shirro/Shadow.

**Shadow's shadow attacks.** In the original data, Shadow Punch (AF move 23)
and Shadow's other shadow attacks only have a script when the pilot has
Shadow enhancement level 3, which is a Tournament upgrade. A plain match
(default `-ShadowEnhancement 0`) therefore never shows the purple shadow
projection, matching the original. `run-blockout-shadow.ps1` now defaults to `-ShadowEnhancement 3`; pass `-ShadowEnhancement 0` for the original plain match. Add `-ShadowEnhancement 3` to either
launcher to fight with the upgraded Shadow; under your control, Shadow Punch is
down-forward, down, down-back, back + punch (`P4123`). The setting only
changes the pilot's upgrade level; OpenOMF still decides every move and hit.

Both need
`build/omf_trace_z7/openomf.exe` (`OMF3K_SOURCE_TRACE=ON`),
`build/omf_debug_z7/omf3d_prototype.exe`, and local OpenOMF resources.
The 3D window appears first and waits about four seconds before starting the
match, allowing the graphics driver to initialize before gameplay. It requests
the high-performance GPU on Windows; `OMF3K_PROFILE_LIVE=1` prints the GPU
actually used and frame timings. Windows graphics preferences may override
the request. The launcher's `-WarmupSeconds` parameter can change the wait.

| Key | Action |
| --- | --- |
| A / D | Move left / right |
| W / S | Jump / duck (combine with direction) |
| J / K | Punch / kick |
| Hold away from opponent | Guard |
| Escape | Close the 3D window and source match |

Controls become active when the first source fight state arrives; keys held
during loading are applied once the match is ready. Opposing direction keys
cancel each other. The live window shows a loading message while OpenOMF starts,
then displays **ROUND 1** followed by **FIGHT** when the first fight state arrives.

The launcher starts one round with hazards off at speed 5, about 28 ms per
source fight tick. The 3D view blends positions between completed source
ticks while health and combat state still come directly from OpenOMF. A short
expanding amber ring marks a source hit, and a cyan ring marks a source block.
The accepted blockouts use source stance, animation ID, and animation tick to
drive walking strides, crouch height,
raised guards, punch and kick reach, and recoil poses. Jaguar's punch and kick
timing is based on measured source traces. Jaguar's standing punch now selects
four arm poses from animation 42's source sprite IDs, including the two-tick
full-extension hold and later recovery. Its standing kick uses four authored
leg poses from animation 41's sprite IDs. Shadow's standing kick and punch
use its own animation IDs (42 and 43) and authored sprite poses. The kick and
punch fits were compared with exact matching higher-resolution OMF 2097
Remastered frames; the approved three-view sheets still define their design.
In source replay and live play, standing punch and kick striking limbs fold
toward a nearby opponent. This presentation fit keeps their maximum-reach
poses and never changes OpenOMF collision, health, or move timing.
Jaguar's down punch (animation 30) now has four arm poses and a forward lunge
matched to its HD frames. Its timing and contact are still unmeasured. Other
moves still use rough poses.
The 3D window displays **YOU WIN** or **YOU LOSE** for player 1 when OpenOMF
declares the match winner. Before a match is decided, a knockout displays
**ROUND WON**, **ROUND LOST**, or **ROUND DRAW**. Version 3 traces append
OpenOMF's `match_winner`, `hit_mask`, `block_mask`, and `round_winner` fields
to each fighter row; older traces remain readable. A declared winner displays even when both
health values are above zero. At the end of a live-source match, the viewer asks **Try again?**
Use **Left/Right** to choose, then **Enter** to confirm. **Yes** resets the running OpenOMF arena
in place and keeps the viewer open; **No** closes the viewer and source process. Recorded CSV
playback remains a separate mode. On Windows, live controls and fighter state pass through
short-lived shared memory channels; if the viewer closes unexpectedly,
OpenOMF stops accepting input after one second.

For a hidden-window integration capture, run:

```text
powershell -ExecutionPolicy Bypass -File project/scripts/run-blockout-jaguar.ps1 -CaptureTick 160
```

The output is
`project/build/omf3d_source_replay_capture.bmp`. The captured tick can be newer than
160 because the viewer follows the most recent completed source tick.

## Source-driven replay view

The prototype can now display the completed fighter states from an OpenOMF
trace. This view uses source position, facing, health, state, animation ID, and
animation tick;
it never runs the prototype's combat rules while the replay is playing. The
robot blockouts are accepted for this prototype milestone; the stage remains
provisional. Record a CSV using the optional
`OMF3K_SOURCE_TRACE` build and `OMF3K_TRACE_PATH` described in the
[Jaguar baseline](../docs/OMF2115_JAGUAR_BASELINE.md), then run from the
repository root:

```text
build/omf_debug_z7/omf3d_prototype.exe --source-replay-check build/omf_trace_z7/jag-corner-trace.csv
build/omf_debug_z7/omf3d_prototype.exe --source-replay build/omf_trace_z7/jag-corner-trace.csv
build/omf_debug_z7/omf3d_prototype.exe --source-replay build/omf_trace_z7/jag-corner-trace.csv --capture-tick 210
```

The last command saves `project/build/omf3d_source_replay_capture.bmp`. Space pauses,
left/right steps one source tick while paused, and holding left or right seeks
through the recording (paused or playing), speeding up the longer it is held. R restarts, and Escape quits.
Playback currently uses 28 ms per source tick, matching the speed-5 trace
captures. Replay mode reads a recorded match and has no input control. Live
mode uses the same state adapter and forwards controls to the source
controller. The next integration step is to match more robot-specific poses
to source move frames and playtest event readability.

Normal OpenOMF builds can opt into the `omf3d_prototype` CMake target via
`BUILD_3D_PROTOTYPE=ON` (the default). A fresh CMake/Ninja build succeeds with
MSVC `/Z7`; see the [source baseline](../docs/OMF2115_BASELINE.md) for the
Windows toolchain and dependency setup.

## What the source inspection showed

- OpenOMF is C11, built with CMake, SDL2, and an OpenGL 3.3 renderer.
- Its game state, arena scene, robot behavior, record playback, and networking
  are organized around 2D sprite objects and original OMF data formats.
- The OpenOMF **code** is MIT licensed. Some bundled support files have their
  own notices. The `OMF2097` directory holds separate original game assets;
  the code license alone does not establish rights to remake or distribute
  those assets, designs, music, or story.
- `OMF2097` and `vcpkg_installed` were present but untracked when this work
  began. This prototype deliberately does not copy them into its output.

## Recommended production architecture

The current spike establishes the presentation and movement plane and uses
Jaguar's source 5:4 forward/reverse speed ratio. The
target remains a faithful 3D rendition of OMF 2097 with its pilots, HARs,
side-on fighting, WAR/Ganymede story, and Tournament progression. Compare
source match timing and moves with this spike before choosing the production
engine. See the [original-game reference](../docs/OMF2097/OMF2097_REFERENCE.md) and
[Jaguar data baseline](../docs/OMF2115_JAGUAR_BASELINE.md).

## Roadmap

See [the project roadmap](../docs/ROADMAP.md) for milestones, completion checks,
near-term work, and scope decisions.

## Current visual pass

The prototype now lights the authored robot meshes by face direction so their
armor facets remain legible at fight distance. Shadow's source-positioned
projection uses the Shadow mesh with violet and cyan materials; Jaguar's shot
has a brighter core and a directional trail. The Stadium blockout adds a
roofed enclosure, stepped audience stands, stylized spectators, a central
scoreboard, quieter floor markings, and a visible front apron. These are
presentation changes: source replay positions and combat timing remain
authoritative. A local frame is in `project/build/mesh-match-ticks/stadium-crowd-blockout.bmp`.
Captured examples are in `project/build/mesh-match-ticks/` as
`shadow-projection-visual-pass.bmp` and `jag-projectile-visual-pass.bmp`.

Current limits: Jaguar and Shadow are editable low-poly rigid-part blockouts,
and the Stadium is a presentation blockout rather than final arena art. Attacks
use simple horizontal reach and height checks rather than source move data or
per-limb hitboxes; the opponent is basic; there is one encounter, no controller
support, save data, audio, or online play. The render has been inspected via a
captured frame; live play still needs human playtesting. The crouch is an
articulated first pass, not a finished pose matched frame by frame to the
original sprites.

## Story mode

`--story` plays a scene script (dialogue, choices, flags, and a match handoff marker) in the same
window system as the viewer. The format, validator, and runner live in `story.h` and `story.c` with
no graphics code, so they can move into the full game later. The draft Crystal versus Christian
slice is `project/data/story/crystal_christian.story`, written from
`project/docs/OMF20115_SIMPLE_LORE.md`; its wording is placeholder dialogue.

```text
build/omf_debug_z7/omf3d_prototype.exe --story project/data/story/crystal_christian.story
```

Enter or Space advances and picks, Up and Down move the choice, S skips to the next choice or match,
L opens the log, R restarts, and Escape quits. At a match marker the prototype only offers Y for a win
and N for a loss; the real match handoff is a later step. Options: `--scene id` starts at a scene,
`--script a,a,c1,w` applies scripted inputs first (a advance, cN choose, u/d move, w/l match result,
s skip, g log, r restart), and `--shot out.bmp` saves one frame headlessly and exits.

`story_check` validates and tests scripts without a window:

```text
build/omf_debug_z7/story_check.exe selftest
build/omf_debug_z7/story_check.exe check project/data/story/crystal_christian.story
build/omf_debug_z7/story_check.exe play project/data/story/crystal_christian.story --choices 0,1 --results 1
```

At a `fight` line, Enter starts a real match: the first fighter is you and the second is the AI. The
story viewer runs `project/scripts/run-blockout-jaguar.ps1` as a child process (Windows only) and waits;
when the match is decided the live viewer writes `project/build/story/match-result.txt`, shows the result
for a few seconds (Enter or Space returns at once), and exits, and the story continues on its win or lose
scene and autosaves. A story match is played once: the retry prompt and rematch keys are off in this mode. Closing the
match window cancels and leaves the story at the match to retry. The child runs in a job object, so
closing the story window also ends the match and OpenOMF. The two fighters must use different HARs
(Jaguar and Shadow), and a match is one round in Stadium with hazards off against the default AI.

A script that starts with `player <pilot> <har>` and `rival <pilot>` lines (and optional `card <pilot>: <text>`
context lines) opens a selection screen first. The player picks their HAR with Left and Right, the rival takes the
other, and Enter starts the story; the story's recommended HAR is marked. Each side shows a portrait, the pilot's
OpenOMF power, agility and endurance, and its card text. A `fight` can name its HARs as `@player_har` and
`@rival_har`, and dialogue can say `{player_har}` and `{rival_har}`, so any pairing works from one script. A saved
story resumes without the screen; R restarts and brings it back. `--har Jaguar|Shadow` skips the screen.

Original art and sounds are exported locally by `python project/tools/export_story_assets.py` into the
git-ignored `project/build/` folder (a local development reference, never committed or distributed; see
`project/docs/ASSET_LEDGER.md`): the pilot portraits (`portraits/`), the five arena backgrounds
(`backdrops/`), and four sounds (`sounds/`). A scene's `bg` picks its backdrop: a name such as `stadium`,
`danger room`, `power plant`, `fire pit`, or `desert` uses the matching original arena image, and other names
(`green room`, `medical bay`, or anything else) are drawn by the viewer itself. Menu movement, choices, and
starting a match play a move or press sound; advancing dialogue is silent. Matches run with OpenOMF's own
original sound effects and music (the launcher's `-Sound` switch, which the story viewer passes), so the
battle has its usual sounds and its own win and lose voices. `M` or `--mute` turns off the viewer's sounds and
starts matches silent.

A scene can show an illustration with `art <name> [none|fade|zoom|pan]` (`art off` clears it); the name may use
`{flag}`, so the draft's face-off frame is `faceoff_{player_har}`. Frames are 320x124 pictures in
`project/build/art/`, composed from original portraits, arena art, and HAR sprites by
`project/tools/build_story_art.py` (the export command above runs it). `fade` brightens from black, `zoom` pushes
in slowly, and `pan` slides across a slightly zoomed frame. The draft story opens with a four-frame sequence this
way. A missing frame falls back to the scene's backdrop. Without the exported files the viewer still works: it shows placeholder cards,
generated backdrops, and no menu sounds.

`--debug-fights` (or `run-story.ps1 -DebugFights`) lets you skip a match by choosing the result with Y
(win) or N (loss); the log records "Match skipped". `project/scripts/run-story.ps1` starts story mode
(`-New`, `-DebugFights`, `-Scene id`) and warns when the viewer executable is older than its sources,
since the run scripts do not build. Rebuild OpenOMF's trace build as well (`build.ps1 -Config All`) after
changes under `src/`, because the live match uses `build/omf_trace_z7/openomf.exe`.

Progress is saved automatically to `project/build/story/<script name>.save` whenever a choice or a
match result is decided and whenever play stops at a choice, match, or the end. Opening the same
script again resumes from the save, and R restarts and clears it. `--new` ignores the existing save,
and `--save-file path` uses another file. The save is a small versioned text file with the position,
flags, and log, plus a fingerprint of the script: a save made against an edited script, or by a
different format version, is refused with a message and the story starts over. Scripted
(`--script`) and screenshot (`--shot`) runs do not touch the save unless `--save-file` is given.

Validation rejects unknown scenes and commands, duplicate scene ids, scenes that can run off their
end, commands after a jump, end, fight, or choice menu, more than six choices, and fight lines naming
an unknown pilot or HAR, each with the script line number. It warns about scenes that cannot be reached.

