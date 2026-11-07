# OMF2107 release plan: free fan project, original assets, real 3D, two looks

Status: proposed 2026-11-05, merged with the former `ROADMAP.md` on 2026-11-06. **This is the single plan.** Where it
disagrees with another doc, this one wins. All dates are estimates for planning, assuming one main developer working with
Claude, and are least reliable beyond Phase 3. Phase starts count from Monday 2026-11-09. Update this file at the end of
each phase.

## Target

Make **OMF2107** a faithful 3D rendition of One Must Fall 2097. Fighters and arenas gain 3D models, animation, lighting
and camera work while the match stays readable as a side-view fighter. Keep the pilot-plus-HAR selection, directional
punch and kick controls, specials, blocking, stun, combos, hazards, WAR's contest for Ganymede, pilot rivalries and
endings, and Tournament mode.

The story pass expands OMF's own neural-link, WAR, Kreissack and Nova themes. The [story treatment](OMF2107_LORE_v2.md)
develops the government conspiracy, relationships and the physical cost of an experimental link, keeping the setting,
cast and central tournament. The [game specification](OMF2097_3D_GAME_SPEC.md) defines modes, combat rules,
presentation, architecture and acceptance gates. The task register below breaks the phases into tasks; it replaces the
former `OMF2097_DEVPLAN.md`, retired 2026-11-07 and kept in git history.

Fixed decisions: [rights and release rules](RIGHTS.md); no original data in a release; real 3D; two visual modes,
the simplified one a stylised look in its own right, both driven by one rig and one gameplay proxy
([engine paths](ENGINE_PATHS.md)); one source per HAR ([HAR pipeline](HAR_PIPELINE.md)). The engine base is option A:
a standalone `fightcore` with a project data pack, linked in-process.

## Where development stands today

The `project/prototype` viewer renders the match in 3D (Jaguar, Shadow and Katana) and plays Ari's story route. Until
M2 it runs on OpenOMF as the mechanical reference, as decided on 2026-10-15:

- OMF2107 does not get a new combat engine during development. Every fight runs on OpenOMF's reverse-engineered rules
  with the original AF and BK data, and the 3D view only renders the per-tick state it publishes. The prototype's own
  combat loop is a `--sandbox`-only placeholder.
- Gameplay must not be changed to make an effect visible. Shadow's shadow attacks (Shadow Punch, AF move 23) only have
  a script at enhancement level 3, exactly as in the original Tournament, so the live launchers expose that as an
  explicit `-ShadowEnhancement 3` option.
- This is a development baseline only. The release path replaces it with `fightcore` and an authored data pack
  (Phases 1 and 2), keeping the OpenOMF link as a dev-only comparison mode.
- [OMF 2097 Remastered](https://github.com/Jared-woodruff/OMF-2097-Remastered) (local sibling
  `../OMF-2097-Remastered`) was reviewed as an alternative. It is a function-by-function TypeScript port of OpenOMF
  with determinism tests, but has no parity tests against OpenOMF, no per-tick state export and no 3D renderer. It is a
  reference only (optional Spike B).

Done before M0 (the old Stages 0 to 2 and the start of 4):

- **Baseline:** range, timing and guard checks cover all 35 Jaguar and Shadow attacks
  ([OMF2107_MOVE_MEASUREMENTS.md](OMF2107_MOVE_MEASUREMENTS.md)); signature traces, Stadium wall response and a
  replayable source-driven match are recorded.
- **Match review:** the playable Stadium match was compared with the
  [recorded model match review](OMF2107_MODEL_MATCH_REVIEW.md) on 2026-10-27 (facing, hit timing, recovery) and judged
  good with both the blockout and Meshy models. Body overlap during kicks, falls, crossings and throws is accepted
  because OpenOMF has no body collision. Gate closed 2026-10-27. Carried over as polish: the eased facing turn in
  Shadow's close throw needs a live look, the Jaguar concussion shot was reviewed by screenshot only, Shadow's purple
  figures have no trails (no renderer transparency), and skinned deformation rigs wait for the asset pass.
- **Staging:** the Stadium has an enclosed bowl, stepped crowd stands and a central board. The blockout launcher
  (`run-blockout.ps1`; `run-meshy.ps1 -Fight` for Meshy stand-ins) opens a selection screen connecting ten playable
  pilots to Jaguar, Shadow or Katana, using their OpenOMF stats.
- **Story (2026-11-06):** `project/data/story/ari.story` holds Chapters 1 to 6 of the Story Pack (266 scenes, including the skippable optional scenes) with
  the Group A, bracket and championship branches and a two-fight Nova boss. It passes `story_check`, and
  `story_check walk` reaches the ending every time. Every character shown with `present` has a project-made render (Nova has none
  by design), including Kreissack, Sorell, Plug, Cossette and Ibrahim, and the viewer no longer reads the original-game portraits. The
  14 fanservice frames are wired in, with a solo epilogue `ch6_e4`. The seven NPC results are decided: Mara wins the Group A-out
  quarterfinal against Selene, the Crystal and Lyra defaults stand, and the three-way tie keeps the announced seed. Ari's sister is
  Norah (trait and memory decided 2026-11-07: a loader mechanic, hundreds died with her). Still open: a live playtest of the route (`run-story-ari.ps1`), the last trim of the short main route
  (about 41 minutes with every fight won against 25 to 35; the rest is optional episodes, see `data/story/ari.tiers`), and the older Crystal-story and news frames, which still use original
  portraits. Scope and open decisions are in
  [OMF2107_STAGE4_PLAN.md](OMF2107_STAGE4_PLAN.md).
- **Pose and mesh authoring:** mesh landmarks (`project/data/mesh_landmarks.json`) and projection-pose matching
  (`match_projection_poses.py`) feed the pose catalog; see [POSE_AUTHORING.md](POSE_AUTHORING.md).

## Milestones

| Milestone | Target | Gate |
| --- | --- | --- |
| M0 Decisions and spikes | 2026-11-20 | Extraction spike go or no-go; tool audit; permission email sent; simplified style brief; rig spec locked |
| M1 Pipeline and core skeleton | 2027-01-15 | Jaguar built from `rig.json` in both looks; data pack format and validator; `fightcore` runs a recorded match |
| M2 Data-free duel | 2027-03-12 | Jaguar and Shadow on authored data and keyframes, no original file read; parity within tolerance of the measurements; both looks playable |
| M3 Clean vertical slice | 2027-04-30 | One story route, menus, sound and music all original; build gate passes; outside playtest |
| M4 Public demo | 2027-07-30 | Four HARs, local versus, one story route, options; permission answer received or takedown plan ready |
| M5 Full roster | 2027-11-30 | All ten standard HARs plus Nova as story boss (unlock policy open), Tournament mode, remaining arenas and routes |
| M6 Release candidate | 2028-01-31 | QA, controller and options polish, packaging, rights review complete |

The old roadmap's stages map onto these: Stage 0 (source baseline) and Stage 1 (3D fidelity spike) are done; Stage 2
(combat slice) becomes M2; Stage 3 (visual and audio direction) is split between M1 (style) and M3 (audio); Stage 4
(one-player story) is M3; Stage 5 (Tournament) is M5; Stage 6 (roster and release) is M5 and M6.

## Scope boundaries

- **First playable:** one faithful match with pilot and HAR choice, source-like controls and one recognizable arena.
- **First story slice:** one existing pilot route in WAR's Ganymede contest, with original-style banter and an ending.
- **First Tournament slice:** custom pilot, prize money, an upgrade and a short bracket.
- **Later decisions:** full roster, advanced cinematics, network play and modes beyond the original. These follow a
  successful match and the rights review.

## Progress

- 2026-11-05: Spike A done (read-only), result **go with conditions**: [SPIKE_A_FINDINGS.md](SPIKE_A_FINDINGS.md). The
  tool audit (P0) first pass is in [HAR_PIPELINE.md](HAR_PIPELINE.md). Still open in Phase 0: permission email
  and simplified style brief. 2026-11-06: `rig.json` written ([robots/rig.json](../robots/rig.json), checked by
  `robots/check_rig.py`); it found that `jaguar-rigged.gltf` is stale against its generator (it has two helmet parts the
  generator no longer makes).
- 2026-11-06: Ari's route scripted end to end (see above). Docs consolidated: this plan replaces `ROADMAP.md`.

## Phase 0: decisions and spikes (2026-11-09 to 2026-11-20)

| Task | Output |
| --- | --- |
| Send the permission request to Diversions Entertainment (find contact route via the OpenOMF community) | Email sent; log in `RIGHTS.md` |
| Spike A: read `src/game/` rule code, list what it reads from AF, BK and game state | Data-model note, go or no-go (details in `ENGINE_PATHS.md`) |
| Pipeline audit (P0 in `HAR_PIPELINE.md`) | What to keep, merge and delete |
| Simplified-look style brief: pick a direction (flat, faceted, cel or other), two reference renders | One-page brief, mood images |
| Lock `rig.json` fields and axes (P1) | Spec committed |
| Optional Spike B (Remastered harness as reference only) | Notes, only if time allows |

If the spike says no-go, fall back to a rules re-implementation (option D) and push M1 to 2027-02-26.

## Phase 1: pipeline and core skeleton (2026-11-23 to 2027-01-15, 8 weeks incl. holidays)

Track E (engine): define the data pack format and its validator; lift the rules into `fightcore`; headless run of a
recorded match; a dev-only converter and tick-for-tick parity test against the existing REC fixtures (output never
committed).
Track H (HAR pipeline): P2 to P4 for Jaguar: procedural blockout, mesh importer, skinning, glTF loaded at run time.
Track A (art direction): approve the simplified style; first style pass on the Jaguar blockout.
Track R (rights): ledger cleanup, malformed rows fixed, replacement checklist converted to tracked tasks.

## Phase 2: data-free duel (2027-01-18 to 2027-03-12, 8 weeks)

- Author Jaguar and Shadow data packs from the 35 move measurements; re-run the measurement checks and accept within
  agreed tolerances (set at the start of the phase).
- P5 to P7: keyframe authoring with IK, mask generation, `har_check`; port Shadow.
- Link `fightcore` in-process in `project/prototype`; remove the shared-memory link and the OpenOMF process for
  release builds (keep a dev-only comparison mode).
- Replace the Stadium and one second arena with original art; simplified look reviewed per HAR and arena.
- Build gate: fails if any shipped file matches the original data.

## Phase 3: clean vertical slice (2027-03-15 to 2027-04-30, 7 weeks)

- Original portraits, backdrops, illustrated frames, menu and battle sounds, music (commission or generate and clear
  terms for each; record in the ledger).
- Rewrite the Crystal versus Christian route (deferred so far), original text.
- Menus, options, key remapping. Outside playtest by someone who has not seen the build.

## Phase 4: demo roster (2027-05-03 to 2027-07-30, 13 weeks)

Add two HARs per batch with the pipeline, targeting two to three weeks per HAR (to be measured on the first one;
revise this plan from the real figure). Local versus, controller support, two more arenas, more pilots. Public demo
at M4 if the permission answer or takedown readiness allows.

## Phase 5: full roster and Tournament (2027-08-02 to 2027-11-30, 17 weeks)

Remaining HARs (five more at the target rate), remaining arenas and hazards, pilot stories and endings, Tournament
mode (custom pilot, winnings, upgrades, bracket), final audio, voice if wanted.

## Phase 6: release candidate (2027-12-01 to 2028-01-31, 9 weeks)

QA across hardware, performance for both modes, accessibility, localisation if wanted, crash reporting, installers,
final rights review against the ledger, disclaimer in the README, title screen and store page.

## Task register (from the former development plan)

The old plan used Phases A to F with task IDs. The IDs stay so earlier notes still resolve; the phases map onto the
milestones above. Priorities: **P0** is needed for the next playable gate or a safe production decision, **P1** is
needed for the complete game, **P2** is an enhancement that can wait. No phase is done because the code compiles: each
gate needs a demonstrated flow, comparison with the OMF baseline where relevant, and a list of remaining defects. Create
one work item per task ID with owner, dependencies, files touched, acceptance evidence and actual effort.

| Old phase | Now | Old exit gate, in short |
| --- | --- | --- |
| A Baseline (P0) | Done before M0 | Clean build, reference captures, two-HAR move sheet, rights ledger, architecture map |
| B 3D fidelity spike (P0) | Done before M0; gate closed 2026-10-27 | Legible 3D local Stadium match on the fight plane; toolchain decision recorded (option A, see top) |
| C Vertical slice (P0) | M3, with Ari's route as the story segment | Pilot and HAR pick, exchange, fight, recovery, choice, consequence; stable enough to cost a HAR, arena and route |
| D Shared systems (P1) | Phases 3 to 5 | Every mode has a working loop; saves survive a build update; content is added without touching fight code |
| E Content production (P1) | Phases 4 and 5 (M4, M5) | Ten pilots, ten HARs, five arenas, endings, Tournament, all in the coverage matrix |
| F Release candidate (P1) | Phase 6 (M6) | Installable, playable, savable and finishable, with all shipped content cleared |

### Phases A and B (done)

Task-level status was not re-audited. The recorded outcomes are in "Done before M0". Open carry-overs:

| ID | Task | Status |
| --- | --- | --- |
| A02 | Run the source unit tests, record failures apart from 3D work | Open |
| A03 | Reference captures (Jaguar vs Shadow, Stadium plus one hazard arena); a visible human-played reference match | Replayable source-driven match recorded; human-played match open |
| A06 | Asset inventory and provenance ledger | Open, tracked under Rights in Phase 1 |
| A07 | Human playtest protocol with OMF-familiar players | Open; the Phase 3 outside playtest reuses it |
| B07 | Fidelity report and prioritized defect list | Match review done 2026-10-27; the live playtest of readability is open |
| B08 | Production toolchain decision | **Decided 2026-10-15**: option A. The Remastered port stays a reference (optional Spike B) |

### Phase C (M3)

| ID | Task | Where it lands |
| --- | --- | --- |
| C01 | Complete Jaguar and Shadow combat: move lists, stun, combos, knockdowns, rounds, timeouts, scrap finish | Phase 2, on `fightcore` and authored data |
| C02 | Original hazard arena with a visible cue and a replayable timing test | Phase 2 (second arena) |
| C03 | Slice-quality models, rigs, animations, effects, HUD, one arena treatment; OMF veterans name the machines unlabelled | Phases 1 and 2 |
| C04 | Pilot selection independent of HAR selection | Done in the selection screen; the story recommends a pairing without locking it |
| C05 | Data-driven scene runner (portraits, dialogue, choices, skip and log); invalid references reported | Done (`story_check`) |
| C06 | Story sequence: pre-fight exchange, match, recovery, evidence choice, consequence; choices persist through save and load | Ari's route built; save persistence and the live playtest open |
| C07 | One polished anime-style sequence and one short in-engine HAR sequence, skippable and replayable | Phase 3 |
| C08 | Combat sound cues, music, dialogue timing, audio controls; block, hit, stun, hazard and victory distinguishable without the HUD | Phase 3 |
| C09 | End-to-end playtests; frame pacing and input latency on a real target PC | Phase 3 outside playtest |

After the slice, measure real time for one HAR, one arena, one character sequence and one route segment, then forecast the
rest and reconcile it with capacity before authoring the full roster.

### Phase D: shared systems (P1)

| ID | Task | Acceptance |
| --- | --- | --- |
| D01 | Versioned schemas for HAR moves and hooks, pilot stats, hazards, dialogue, scene timing, ending flags | Malformed entries fail with useful errors |
| D02 | Versioned saves for story, Tournament, controls and settings, with migration tests | An older save loads after a schema change or fails safely with a message |
| D03 | Training mode: move list, input history, dummy settings, hitbox and stun display, recording playback | A player can practice one special and see why it missed |
| D04 | Arcade ladder and local Versus menu with round, time and arena options | Matches run without entering Story or Tournament |
| D05 | Tournament: pilot creation, budget, owned HARs, ranked events, payouts, repairs, training, upgrades, ranking | One short bracket can be won, spent, saved and continued; every price and stat change shown before purchase |
| D06 | Named rivals; three event templates (ranked bracket, challenge, contract); short rivalry beats | Rival state changes on repeat fights; rank does not need easy-event farming |
| D07 | Settings and accessibility: remap, text scale, subtitles and log, reduced flashes and shake, audio mix, graphics scale, scene skip | Settings persist and work on keyboard and gamepad; all story text stays available |
| D08 | Content checks and a smoke suite for every mode entry and exit, save and load, one representative fight | Invalid content is caught before a build is shared |

Arcade mode is scoped in [OMF2107_ARCADE_MODE.md](OMF2107_ARCADE_MODE.md). D05 sits in Phase 5, after the roster.

### Phase E: content rules (P1)

- **Per HAR:** build in small batches in this order: silhouette sheet, move data, placeholder implementation, balance
  test, rig and animation, effects and sound, AI tuning, review. Done means every source-defining move is represented,
  has documented inputs and timings, shows in training and AI, two local players can use it, and no major camera or
  hitbox ambiguity remains. Nova follows as a boss once the normal roster works, with explicit, learnable rules.
- **Per arena:** gameplay bounds and hazard, readable blockout, art and lighting, cue and audio, playtest.
- **Per route:** lock the shared 2097 timeline first, marking proposed additions against original canon. Done means the
  pilot can finish the campaign, every required scene and match has a fallback for any legal HAR, choices are saved and
  reflected later, and a pilot-specific ending plays. Build reusable portrait poses before commissioning unique shots;
  keep full animation for the opening, key revelations, Nova and a few endings. Romance and fanservice stay limited to
  established adult characters and voluntary scenes.
- **Tournament and audio:** several spending strategies must reach the top rank without repeating low-level fights.
  Add voice only after text and timing are stable. Tournament upgrades stay inside its ruleset unless both Versus
  players opt in.

### Phase F: release evidence (P1)

| ID | Task | Evidence |
| --- | --- | --- |
| F01 | Full combat regression: input traces, replays, all moves, all hazards, all pilot stat combinations | No reproducible winner or health desync; no unreadable move |
| F02 | Story and Tournament walkthroughs on clean profiles and upgraded saves | Every route ends; purchases, repairs, rank and choices persist |
| F03 | Performance and hardware sweep on minimum and recommended PCs | Frame pacing, input latency and load times measured |
| F04 | Accessibility, controller and UX pass with OMF newcomers and veterans | Subtitles, remaps, skip, log and reduced effects work throughout |
| F05 | Content and legal audit; packaging | Ledger complete; only approved data and licensed material ship |
| F06 | Crash and telemetry policy, bug triage, release notes, support plan | A shippable build and a known-issues list |

## Parallel tracks, always on

| Track | Standing rule |
| --- | --- |
| Rights | Every new asset gets a ledger row with origin and terms on the day it enters; nothing from the originals is committed |
| Parity | After any rules or data change, re-run the measurement and replay checks |
| Two looks | A HAR or arena is not done until both looks pass review and `har_check` |
| Docs | Update this plan at each milestone |

## Evidence to keep

| Evidence | Created | Purpose |
| --- | --- | --- |
| Clean build record ([OMF2107_BASELINE.md](OMF2107_BASELINE.md)) | Phase 0 and each release build | Setup quirks cannot mask project failures |
| Original-match reference captures | Baseline; updated only if source settings change | Anchor movement, moves, camera and hazards |
| Input and replay fixtures | Phase 1 on | Reproduce combat changes and regressions |
| Human playtest notes | Each playable gate | Catch feel and readability problems headless tests miss |
| Coverage matrix | M3 on | Track each pilot, HAR, arena, mode, route, move and scene |
| Asset ledger | Always | Separate local reference data from shippable content |
| Decision records | Spikes and scope reviews | Keep the reasons for engine, art, input and balance choices |

Automated tests target rules that can regress silently: move legality, collision and damage order, hazard timing, save
migration, content references and replay reproduction. A passing self-test does not prove a good fighting game, so also
review captured frames and live play.

## Rights checkpoint

Decision (2026-11-05): free, non-commercial fan project that keeps the name, HARs, pilots and references to the
original, and ships only original assets. Research, release rules, accepted name risk, the permission-request draft
and the replacement checklist are in [RIGHTS.md](RIGHTS.md). OpenOMF's code is MIT licensed, but the original game's
artwork, audio, text, character designs and name need their own assessment. The local `OMF2097` folder is a
development reference; its presence is not a release license. The [asset ledger](ASSET_LEDGER.md) holds the asset
provenance list.

## Biggest risks

| Risk | Effect | Mitigation |
| --- | --- | --- |
| Spike A finds the rules tied to AF structures | M1 slips about six weeks | Option D fallback; decide at M0 |
| No answer from the rights holders | Public release stays risky | Takedown plan, keep project free, send follow-up, rename fallback |
| Authored data does not feel like the original | Parity rework in Phase 2 | Agree tolerances first; keep the dev-only comparison mode |
| Two looks double the art work | Roster dates slip | `har_check` automation; style layer on the blockout before separate geometry |
| Single developer capacity | All dates slip | Re-plan at each milestone; the demo (M4) is the first safe stopping point |
| Auto-skinning quality | Extra manual weight work | Manual fixes only where `har_check` flags; thin parts handled by rigid binding |
| Audio and art sourcing and terms | Delays M3 | Start sourcing in Phase 1; record terms before use |
| Free camera or 3D rotation makes inputs feel wrong | Crossovers and corner fights confuse playtesters | Locked fight plane and facing rule; cinematic camera only in noninteractive moments |
| Art looks generic despite higher fidelity | Veterans fail to name HARs or arenas in an unlabelled clip | Review silhouette, colour blocking and framing before detail passes |
| Ten HARs and ten routes exceed capacity | Measured slice throughput exceeds available time | Re-plan batches from real costs; make any scope cut explicit |
| Tournament turns grindy or upgrades beat skill | Testers repeat easy matches; one purchase dominates | Simulate payouts, cap upgrade effects, test several career paths |
| Story scenes interrupt match rhythm | Frequent skipping between fights | Short routine scenes, all skippable, a log, animation only for major turns |
| Local build works on one machine only | A clean build cannot be reproduced | Stabilise the toolchain and build script first; test a second machine at each gate |

## Next three actions

1. Send the permission email (needs a contact; I can look for one).
2. Decide the simplified style direction from two or three quick renders of the Jaguar blockout.
3. Live playtest of Ari's route (`run-story-ari.ps1`).

(Spike A and the first pass of the tool audit are done; see the 2026-11-05 entry above.)

## References

- [Original game reference](OMF2097/OMF2097_REFERENCE.md)
- [Story treatment](OMF2107_LORE_v2.md)
- [Game specification](OMF2097_3D_GAME_SPEC.md)
- [OpenOMF repository](https://github.com/omf2097/openomf)
- [Original manual story](https://www.omf2097.com/wiki/doku.php?id=omf2097:story)
- [Decoded in-game help and text](https://www.omf2097.com/wiki/doku.php?id=omf2097:english.dat)
