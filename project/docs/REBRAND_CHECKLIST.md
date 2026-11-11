# Full rebrand checklist

Status: drafted 2026-11-10. Decision: full rebrand (project owner, 2026-11-10), after the OpenOMF Discord replies gave no
legal clarity ([RIGHTS.md](RIGHTS.md), "Rebrand"). Counts come from a name inventory run the same day; they are
case-insensitive substring counts and approximate, and short names (Ari, Ren, Plug, Alex) also match ordinary words.
Nothing here is legal advice. Items marked **decision** must be settled before the work that depends on them.

Goal: no title, name, character, robot design or asset in a distributed build that comes from One Must Fall 2097,
Battlegrounds or their owners, while crediting OpenOMF (MIT) and acknowledging the original game as inspiration.

## 0. Decisions first

- [x] **D1. New title: provisionally "Steel Skin 2100" (2026-11-10).** Still to do: a short code name (for targets, env
  vars, repo), and the clearance below. A web search on 2026-11-10 found no game or trademark filing called "Steel
  Skin" or "Steel Skin 2100" (similar names exist: Steel Combat, Fight of Steel, Real Steel, Fighting Steel, now
  cancelled). Not a real clearance: check USPTO and WIPO trademark databases, Steam and itch.io, app stores, domain and
  repo name. Avoid "One Must Fall", "OMF", "2097" and "Battlegrounds". Note the title says 2100 while the current
  lore is set in 2107; decide whether the setting year changes (D4).
- [x] **D2. Fighter robots: all replaced, "eventually" (decided 2026-11-10).** New names and new designs for all eleven
  (Jaguar, Shadow, Katana, Thorn, Pyros, Electra, Shredder, Flail, Gargoyle, Chronos, Nova) and a new generic term for
  "HAR" (1,183 hits in 188 files). The Discord view was that remaking the designs "might be too close" and that
  tweaking names ("Mk2") is not a safe fix, so this is a redesign, not a rename. Still open: the new names and the
  term, and the **order**: the original robots stay as private development placeholders until replaced, and none may
  ship (see "Placeholders" below).
- [x] **D3. Characters: all replaced, "eventually" (decided 2026-11-10).** All ten original pilots plus Kreissack
  (Crystal Devroe, Steffan Thomas, Raven, Christian Devroe, Shirro, Jean-Paul, Angel, Cossette, Milano, Ibrahim,
  Kreissack) get new names, backstories and looks. Still open: confirm which story characters are project-invented
  (Ari, Lyra, Mara, Ren, Selene, Dante, Haldane, Alex, Leena, Norah, Varga, Plug, Solano, and so on) against the Story
  Pack bibles, since the inventory inferred it; those can stay unless they depend on original characters.
- [x] **D3a. Sound and music: all replaced, "eventually" (decided 2026-11-10).** Every sound effect and music track,
  including the `.PSM` modules and `SOUNDS.DAT` effects the build still reads at runtime. Needs an original source for
  each (own composition, commissioned, or clearly licensed), logged in [ASSET_LEDGER.md](ASSET_LEDGER.md).

**Derivation rule (decided 2026-11-10).** Some replacement robots may be based on the originals "with considerable
modification". This lowers the risk but does not remove it; the Discord view was that remaking designs "might be too
close". To keep the modification real and provable:
- Work from a written design brief, not from the original sprites or renders: role, range, weight class and movement feel
  (mechanics, which are kept) are fair to carry over; silhouette, proportions, head and limb shapes, colours, markings,
  emblems and materials must be new.
- Change the silhouette, not only the surface. A recolour, a "Mk2" tag or added armour on the original shape does not
  count. Test: placed side by side in silhouette, a player should not read it as the original robot.
- Keep a **derivation log** per robot (`project/robots/<name>/DERIVATION.md`): which original it echoes, what is kept
  (role, move set, range), what is new, who drew it, and which references were used. This is the evidence if anyone asks.
- Prefer robots that borrow a role, not a look, and make some robots wholly new so the roster as a whole is not a
  reskin.
- No original sprite, frame or render is traced, painted over or used as a pose reference in the final art.

**Placeholders.** Until a replacement exists, original robots, characters, sounds and music may stay in local
development builds only. They must not appear in any distributed build, public screenshot or trailer, or outside
private tester packages. A hard stop: M5 (public demo). To avoid doing the work twice, author **new** robots from the
start where the plan builds new art: the Phase 2 data pack, meshes and keyframes for the first two HARs (M2, H4) should
be of the replacement robots, not of Jaguar and Shadow, and only the parity measurements (private, dev-only) use the
originals.
- [ ] **D4. World terms.** Ganymede (1,048 hits), "2097" (904), "Tournament" (2,593; generic, probably keep), arena
  names (Stadium, Fire Pit, Power Plant, Desert; generic, probably keep unless copied exactly), in-fiction organisations
  from the original lore. Decide how far the setting changes; the year "2107" in the old name is tied to the setting.
- [ ] **D5. OpenOMF naming.** Keep upstream names (`openomf`, `OPENOMF_*` env vars, `openomf.conf`, `org.openomf.*`) as
  credited code, or rename them in the project's own build. They are MIT and may be renamed; keep the notice.
- [ ] **D6. Combat data.** Move data, frame timing and stats parsed from the original files (parity work) are mechanics
  and are kept per RIGHTS.md rule 4. Confirm that stays the position, and that no original numbers or text ship in
  the data pack.
- [ ] **D7. Credits wording** and disclaimer text (section 9).

## 1. Names and strings in the build

- [ ] Window and view titles: `OMF2107 / PROTOTYPE`, `/ STORY`, `/ MODEL BLOCKOUTS`, `/ LIVE SOURCE`, `OMF2107`
  (`project/prototype/main.c` around 1395, 2151, 2486, 3396, 3407, 3500, 3902); move browser title
  (`project/tools/generate_move_browser.py:210,242`).
- [ ] CMake: `project(OpenOMF C)` (`CMakeLists.txt:31`), option `OMF3K_SOURCE_TRACE`, targets `openomf`, `omf3d_prototype`,
  `story_check`, `openomf_core`, `openomf_test_main`; build dirs `build/omf_*`.
- [ ] Environment variables and output names: the `OMF3K_*` family (about 40), `omf3d_*` output files (about 84),
  `project/build/omf3d_model_*.bmp`.
- [ ] Save, config and log names: `<name>.save`, SDL pref path `"OpenOMF"` (`main.c:373`), `openomf.conf`, `openomf.log`.
- [ ] Release and packaging names: `openomf_<ver>_windows_msvc_<arch>.zip`, AppImage, `.deb`, macOS app and bundle id
  `org.openomf.OpenOMF`, flatpak id and metainfo, `.github/` workflows (about 65 hits).
- [ ] Scripts in `project/scripts/*.ps1` (`run-blockout-jaguar.ps1`, `replay-rec.ps1`, `build.ps1`,
  `package-playtest.ps1`, `run-meshy.ps1`, `run-story.ps1`, `run-blockout.ps1`).
- [ ] Repo identity: root directory `OMF2107`, GitHub repo `leohmarruda/OMF2107`, the `upstream` remote name
  (`omf3015`). Rename on the host first, then update remotes and docs links.
- [ ] Root `README.md` (17 hits; lines 62-68 are the project section; the rest is upstream OpenOMF text) and
  `project/README.md`, `project/prototype/README.md` (69 hits).

## 2. Robots (names, term and designs)

- [ ] Rename the eleven robots in code and data: Jaguar (236 code/data hits, 543 doc hits), Shadow (278/503), Katana
  (44/149), Nova (150/5,498), Electra, Pyros, Flail, Gargoyle, Chronos, Shredder, Thorn, plus `--har` options, the
  `story_setup_har` picker (`main.c:109`), `project/data/move_names.csv`, `project/data/story/*.story`.
- [ ] Replace "HAR" / "Human Assisted Robot" everywhere (code, docs, rig schema, `har.json`, `har_check`, the
  `HAR_PIPELINE.md` filename and the H1 to H5 gates).
- [ ] Rename robot folders and files: `project/robots/jaguar/`, `project/robots/shadow/`, render filenames,
  `maintenance_<har>`, `news_<pilot>_<har>`, `wreck_<har>_<result>`.
- [ ] Redesign decision (D2) applied: front and side variants documented as based on `FIGHTR0.AF` and the original
  victory frame (`robots/jaguar/front/README.md`, `faithful-v2/README.md`) must be re-derived from original concept
  art, not from original sprites.
- [ ] Repo-root `rectests/`: 25 tracked `.REC` files named by robot (`KATANA_DAMAGE.REC`, `PYROS_DESTRUCT.REC`, ...).
  These are comparison fixtures from the original game's behaviour; keep private or rename, and never ship.

## 3. Pilots, story and lore

- [ ] Apply D3 across `project/data/story/*.story` (`ari.story` alone has about 2,158 name hits), `ari.tiers`,
  `crystal_christian.story`, `christian_crystal.story`, `arcade_ari.story`.
- [ ] Pilot stats copied from OpenOMF (`main.c:112-115`) and selection names (`main.c:118-119`).
- [ ] Renders named for original pilots in `project/renders/` (11 files: `angel`, `christian_devroe`, `cossette`,
  `crystal_devroe`, `ibrahim`, `jean_paul`, `kreissack`, `milano`, `raven`, `shirro`, `steffan_thomas`).
- [ ] `OMF_2107_Story_Pack/` (472 files, about a quarter of all name hits): decide per file whether to rewrite, archive
  or drop. Largest: `COMBINED_WORKING_EDITION.md` (4,465 hits), `dialogue_cues.csv` (3,082),
  `Fanservice_Scene_Review_v1.0.md`, and the versioned `Chapter_06_One_Must_Fall_v0.x.md` and
  `Chapter_04_No_Holding_Back_v0.x.md` duplicates. Remove the `.pyc` build artifacts inside it.
- [ ] `OMF2107_LORE_v2.md`, `OMF2097_LORE.md`, `OMF2107_STAGE4_PLAN.md`, `ARCADE_MODE_PROMPTS.md`: rewrite or retire.
  "One Must Fall" also appears as a chapter title in the Story Pack.
- [ ] Setting terms per D4 (Ganymede, 2097, arena names) in story, art tools (`build_story_art.py`,
  `export_story_assets.py` arena list) and docs.
- [ ] Original instruction manual PDF in `project/docs/` (`One_Must_Fall_2097_Instruction_Manual.pdf`): reference only,
  never distributed.

## 4. Assets (nothing derived from the original ships)

- [ ] Ledger rows 16 to 22 in [ASSET_LEDGER.md](ASSET_LEDGER.md) (portraits from `MELEE.BK`, backdrops from
  `ARENA0-4.BK`, menu sounds from `SOUNDS.DAT`, `.PSM` music, battle sound, `FIGHTR*.AF` frames, `VS.BK` scene): each
  needs a replacement before release. Fix the malformed row 21 first.
- [ ] Music: the prototype loads `OMF2097/*.PSM` at runtime (`main.c:1457-1480`). Replace with original music; rights to the
  original score are unclear (composer Kenny Chou).
- [ ] `build_story_art.py` still reads `OMF2097/` (`:44`) and original sprites; retire or rewrite to use original art.
- [ ] Renders in `project/renders/` are project-made (ledger), but 33 of 54 are named for original or Ari-route
  characters; review each for likeness to original portraits.
- [ ] Generated pose folders `project/docs/OMF2097/poses/` and `project/docs/Remastered/poses/` (gitignored, derived from
  originals): keep private, exclude from any release.
- [ ] Remove from any distributed build: the `OMF2097/` data directory. `package-playtest.ps1:41` copies it into `dist/`;
  that package is private only.
- [ ] Upstream CI downloads `openomf-assets.zip` from omf2097.com into the release zip
  (`.github/actions/build_msvc/action.yaml:42-50`): remove before any public release.

## 5. Data path (engine and tooling)

- [ ] The release path must not read original data: `fightcore` plus a project-made data pack (see
  [ENGINE_PATHS.md](ENGINE_PATHS.md)) with the release data gate that fails on derived files.
- [ ] Tools that read `OMF2097/` (`paths.py:34`, `export_pilot_portraits.py`, `export_story_assets.py`,
  `build_story_art.py`, `extract_hd_leg_poses.py`, `fit_poses.py`, `measure_moves.py`, `render_remastered_poses.py`,
  `pose_inventory.py`): mark as dev-only, keep outside the release.
- [ ] `project/web/*.html` and `generate_pose_editor.py` (references the Remastered atlas): dev-only.

## 6. Documentation

- [ ] Rename the 17 `OMF2107_*.md` files in `project/docs/` and the archive files (`OMF2097_3D_GAME_SPEC.md`,
  `omf-reimagined-design-pitch-v0.3.md`, `OMF2107_BLOCKOUT_REVIEW.md`); update every link. Do this in one commit
  after D1 so history stays readable.
- [ ] `DEVPLAN.md` (title, "Reimagined" naming, R-tasks), `README.md` index, `HAR_PIPELINE.md`, `FEATURES.md`,
  `GAME_SPEC.md`, `ENGINE_PATHS.md`.
- [ ] `RIGHTS.md`: rewrite the decision and the permission-request draft for the new project; keep the sourced findings
  and `rights_sources/` unedited as evidence.
- [ ] Keep references to the original game only where they state history, credit or comparison (parity baseline,
  OpenOMF), written as "the original game", not as part of the new title.

## 7. Legal and credits

- [ ] Add a combined **NOTICES** file shipped with every build: OpenOMF MIT notice (required), and the vendored and linked
  libraries' notices. The current install step ships only the root LICENSE, gamecontrollerdb, argtable and zip
  licences; it omits the CC-BY icon text and the dependency licences (SDL, libxmp, libepoxy, enet, libconfuse,
  libpng, opusfile, miniupnpc, libnatpmp).
- [ ] Replace OpenOMF's icons and splash (`resources/icons/*`, `openomf.png`, `openomf.bk`): CC-BY with no named creator,
  scope unclear. Make your own.
- [ ] Translation files (`resources/ENGLISH2.TXT`, `GERMAN2.TXT`, `DANISH.TXT`, `DANISH2.TXT`): no licence or author;
  the English text derives from the original. Do not ship; write original strings.
- [ ] Tidy licence ambiguities: `src/vendored/zip/LICENSE.zip` has no holder; README vs `miniz.h` disagree on MIT vs
  public domain; README line 47 gives the wrong gamecontrollerdb path; `resources/openomf.gpl` is a palette, not
  the GPL.
- [ ] Credits and disclaimer (D7). Suggested content: built on OpenOMF (MIT, link); inspired by One Must Fall 2097 by
  Diversions Entertainment; unofficial, not affiliated with or endorsed by Diversions, Epic or Rob Elam; free, no
  monetization. Credit is courtesy, not permission.
- [ ] Keep the free-only rule, no donation links, and the takedown plan (RIGHTS.md rules 1, 7, 9).

## 8. Order of work

1. D1 to D7 decisions. Do not start renames before D1 and D2.
2. Freeze: tag the current state, so the old names stay reachable in history.
3. Replace all distributed assets and the data path (sections 4 and 5). These matter most legally and block a release.
4. Rename in code and build (section 1), then robots and pilots (sections 2 and 3), in small commits.
5. Docs sweep and file renames (section 6), then regenerate the link check.
6. Notices, credits and disclaimer (section 7).
7. Final scan: search the tree for each old name and for `OMF2097`, `.PSM`, `.BK`, `.AF`; check the release zip contents
   against the ledger; re-run the release data gate.

## 9. Done when

- [ ] A search of every distributed file (build, docs shipped with it, strings) finds no old title, robot, pilot or lore
  name, apart from the credit text and the OpenOMF notice.
- [ ] The release zip contains no file derived from the original game.
- [ ] NOTICES, credits and disclaimer are present and match the licences.
- [ ] RIGHTS.md, ASSET_LEDGER.md and DEVPLAN.md describe the rebranded project.
