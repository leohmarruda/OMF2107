# Engine path without the original data files

Status: proposed 2026-11-05. Follows the [rights decision](RIGHTS.md): a release may contain no original
art, audio, music, text or data. Today OpenOMF cannot meet that, because it loads the original `AF`, `BK`,
`SOUNDS.DAT` and `PSM` files at run time. This document compares the ways out and recommends one.
Nothing here is built yet. Statements about how OpenOMF is structured come from its file layout (`src/formats/`,
`src/game/`) and have not been verified by reading the code.

## What must be replaced

| OpenOMF depends on | Holds | Release replacement |
| --- | --- | --- |
| `FIGHTR*.AF` (via `src/formats/af.c`, `animation.c`, `move.c`) | Move scripts, timings, damage, hit boxes, HAR stats | Project-authored HAR data |
| `ARENA*.BK`, `MELEE.BK`, `VS.BK` (`bk.c`, `bkanim.c`) | Arena art, hazards, portraits, scenes | Project-authored arena and scene data |
| `SOUNDS.DAT`, `*.PSM` | Effects and music | New audio files |
| `*.CHR`, `*.SCO`, pilot and setup data | Pilots, tournaments, scores | Project-authored pilot and tournament data |
| `languages`, fonts, palettes | Text, fonts | Project text and fonts |

The combat rules themselves (the C code) are MIT-licensed and reusable. The data is what cannot ship.

## The data problem, plainly

Move timings, damage numbers and hit-box sizes are game mechanics. Copying the original binary files
verbatim is not safe; authoring new files that behave similarly is a much stronger position. You have already measured
all 35 Jaguar and Shadow attacks, so those measurements are design targets for new data. Write the new data from
scratch and tune it to the targets; do not run a converter and ship its output. A converter is still useful
for development only (see "Parity" below).

## Options

### A. Keep the C rules, replace the data loader (recommended)
Extract the fight rules from OpenOMF into a standalone library (a `fightcore`), swap `af`/`bk` loading for a
loader of a new project data pack (a text or JSON format), and link it into the 3D prototype in-process.

- Pros: keeps the combat feel you have already validated; removes the two-process shared-memory link; deterministic
  and testable; reuses MIT code; smallest change to the working prototype.
- Cons: OpenOMF's rule code is likely tied to its AF structures, so the data model will mirror them and
  extraction takes real work; you inherit its quirks; a new data format and tools are needed.
- Risk: the structures may be more entangled with rendering and the game state than the layout suggests.
  A short extraction spike will show this.

### B. Adopt the Remastered TypeScript port
[OMF 2097 Remastered](https://github.com/Jared-woodruff/OMF-2097-Remastered) (local sibling checkout reviewed
2026-11-05, release 0.2.1) is a function-by-function TypeScript port of OpenOMF. MIT code, about 77,000 lines,
65 test files, headless tests, deterministic replays, lockstep LAN play, a training lab, gamepads, 14 languages,
a Windows app (Tauri) and a web build.

What the review found:

- **It already has the structure option A would create.** Rules run in `GameState` with no renderer; replays and
  netplay depend on tick-exact determinism; tests drive a headless game. The extraction spike for A would be
  largely done.
- **It has a path for authored content in the original formats.** Its new robots (HARs 11-14) and arenas (5-8) are
  generated *from source code* into `FIGHTR11.AF` to `FIGHTR14.AF` and `ARENAn.BK`, and ship as a mod. The robot
  workshop and OMF Studio author robots, arenas and pilots. This is a precedent for "new data, same engine".
- **It still needs the original files at run time.** Its own docs say the engine "loads the original data files".
  Even its generated robots copy shared effect moves, palette entries, remap rows and sounds from `FIGHTR0.AF` and
  `ARENA0.BK`, and menus, fonts, language text, scenes and music come from the originals. So it does not remove the
  data problem; it widens it to the menus, scenes and tournaments, which you would have to replace too.
- **It is a 2D indexed-palette sprite engine.** Its "3D" is pre-rendered sprites (the new robots are rendered in
  Blender) plus depth effects. Your prototype is a real 3D scene. Hit detection in Remastered tests sprite pixels
  (`intersect.ts`), so a new robot needs rendered frames to fight at all. The same is probably true of OpenOMF
  and option A (not verified), so this applies to both.
- **Its HD art is not usable.** `NOTICE.md` says the HD artwork was made from the original images with an image
  model and is shared on the game's no-charge terms. Only the MIT source code can be reused, never its `public/`
  artwork, audio or game data.
- **It is young and has one maintainer.** The repository is dated 2026 and has a single main author, so expect churn.
- **Parity with your baseline is untested.** The development plan (`DEVPLAN.md`, which absorbed the old roadmap) notes it has no parity tests against OpenOMF.

Assessment:

- Pros: no extraction spike; a modern deterministic core; netplay, replays, training and tooling come with it; web
  and desktop reach; authoring tools for robots, arenas and pilots.
- Cons: you switch from C to TypeScript, so `project/prototype` (viewer, story runner, source replay) is rewritten or
  kept as a separate client; real 3D is not provided; the original-data dependency is broader; you inherit a
  large codebase you did not write.
- Fits best if the release is web or desktop with a TypeScript client, and a 3D view reads `GameState` in-process.

### C. A new engine (Godot, Unity or Unreal) with a rules core as a library
Use option A's `fightcore` as a plugin, or reimplement it in the engine's language.

- Pros: professional tooling for animation, VFX, UI, audio, controller support and packaging; easier hiring.
- Cons: the biggest rewrite; a bridge for a C library, or rule parity to re-prove if reimplemented.
- This is the likely end state for a polished 3D release. It does not conflict with A: A produces the library.

### D. A clean-room rules engine
Write new combat logic from the measured behaviour, not from OpenOMF's code.

- Pros: no inherited code or quirks; complete ownership.
- Cons: the feel is not guaranteed to match, and months of validation are repeated. Not recommended unless
  option A's extraction fails.

## Constraint: real 3D (decided 2026-11-05)

The release must be a real 3D game, not pre-rendered sprites. This changes the ranking:

- Remastered (B) is built on indexed sprites, so it could only supply the rules; the 3D view would be a new client
  reading its state. That removes most of its advantage over A, and it keeps the wider original-data dependency.
- Hit detection in the OMF family tests sprite pixels. A data-free 3D game needs a replacement for it. Two ways:
  1. **Silhouette masks:** project each posed 3D model side-on into a hidden mask per animation frame, and let the
     existing rules test those masks. This keeps the rule semantics unchanged and needs a new
     build step (nothing in the repo generates masks today; `match_projection_poses.py` only picks stand-in poses for
     Shadow's projectile sprites by silhouette overlap, which is a related idea, not this). Masks are generated at
     data build time by [the HAR pipeline](HAR_PIPELINE.md).
  2. **3D hit volumes:** capsules or boxes on the skeleton, tested in the side plane. Cleaner for a 3D engine, but it
     changes the rules, so parity must be re-measured.
  Recommendation: start with 1 to keep parity, and move to 2 only if the measured feel allows it.

## Constraint: two 3D visual modes (decided 2026-11-05, renamed 2026-11-09)

The release keeps two looks, called **blockout** (geometric forms) and **mesh** (full meshes). They were called
"simplified" and "detailed" before 2026-11-09 (`DEVPLAN.md`). The blockout ships as a finished look. Design rules that
follow:

1. **Gameplay is independent of the look.** Hit masks or volumes, timing and stats come from one canonical collision
   proxy per HAR, never from whichever mesh is on screen. Replays, saves and any future netplay are then identical in
   both modes, and switching modes mid-match is safe. Suggested proxy: the blockout, since it is the
   most stable and measurable; the mesh must fit inside agreed tolerances of it.
2. **One skeleton and one pose/animation set** drive both meshes. Each mode is a skin or mesh bound to the same rig,
   with the same named landmarks (the existing mesh landmarks and pose catalog). Animation is authored once.
3. **Modes are data, not code.** A HAR's data pack lists its visual variants (`blockout`, `mesh`) with mesh,
   materials and effect anchors, plus a validator check that both bind to the rig and cover every pose.
4. **Effects anchor to rig points,** not to a mesh, so hit sparks, trails and projectiles work in both.
5. **A fidelity check per HAR:** render both modes from the same pose set and compare silhouettes against the proxy,
   as the model match review already does for the blockouts. Flag poses where the mesh sticks out or
   falls short of the proxy by more than the tolerance (to be set).
6. **Performance and options:** the blockout doubles as a low-spec setting; the player chooses a mode in Options.

Decided 2026-11-05: the blockout is a **stylised look in its own right**, not a fallback. It gets its own art
direction (shading, palette, lighting, arena treatment, effects, HUD fit), its own polish pass and its own acceptance
review for every HAR and arena, equal to the mesh look. Low-spec use is a side benefit, not its purpose. Open: the
specific style (flat-shaded, faceted, cel, or other; the M0 blockout style brief in `DEVPLAN.md` settles it) and the
mesh tolerance against the proxy.

## Recommendation

**Option A, then C if the polish needs it. Treat Remastered (B) as a reference, not the base.** With real 3D required,
B's main advantages shrink. Keep one short, optional Spike B (below) only to borrow ideas and tests.

- **Spike B (about one week):** (1) run the OpenOMF REC fixtures in `project/rectests/` through Remastered's headless
  harness and compare results with your recorded traces; (2) boot a stripped-down mod with the original files
  removed and list every file it still asks for; (3) read `GameState` and note how a 3D viewer would read per-tick
  state. Output: parity result, the dependency list, and a go or no-go.
- **Spike A (about one to two weeks):** the extraction described in step 1 below. **Done 2026-11-05, go with
  conditions** (`SPIKE_A_FINDINGS.md`).
- **Spike C (about one week, M1):** a renderer test, not a rules test. On the Jaguar blockout and a throwaway
  production-budget mesh, render all 15 region states, swap parts, and run a particle and transparency stress scene;
  capture frame times against the engine requirements table in `DEVPLAN.md`. Output: renderer go or no-go.

Spike B is optional. Run it only if you want Remastered's REC-replay harness, training lab or netplay design as a
reference. The later steps are the same either way:
a project-made data pack, authored from the measurements, and a build gate against original data. The decision
costs little to reverse until one of them is picked.

1. **Extraction spike (about one to two weeks):** identify what OpenOMF's `src/game/` rule code reads from `sd_af`,
   `sd_bk` and the game state; list the exact fields. Output: a one-page data-model note and a go or no-go.
2. **Define the data pack:** a versioned text format for HARs, moves, pilots, arenas and hazards, with a validator
   in the same spirit as `story_check`. Include a schema document.
3. **Dev-only converter and parity test:** convert the local originals to the new format *locally* and check that
   `fightcore` plus the converted pack reproduces the existing REC recordings tick for tick. This proves the core. The
   converted output is never committed or shipped.
4. **Author the real pack:** write Jaguar and Shadow data from scratch against the move measurements, then
   re-run the measurement checks. Accept it when range, timing and guard land within agreed tolerances.
5. **Link in-process:** replace the shared-memory link in `project/prototype` with direct `fightcore` calls; keep
   the `source_replay` tests.
6. **Release data gate:** a build check that fails if any shipped file derives from the original data (hash check
   against the local originals plus the ledger).

## Open decisions

- Data format: JSON, a custom text format, or binary with tools. Recommendation: text with a validator.
- Whether the release stays on the C viewer or moves to a game engine (option C). Decided 2026-10-15: option A (C viewer); Spike C at M1 re-checks the renderer against the engine table in `DEVPLAN.md`. Spike A was done 2026-11-05 (go with conditions).
- Tolerances for "feels the same" in step 4, since authored data will not match the original exactly.
- Whether to keep a developer-only mode that loads the original data for comparison. Recommendation: yes, never shipped.
