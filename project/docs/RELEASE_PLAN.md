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
presentation, architecture and acceptance gates. The [development plan](OMF2097_DEVPLAN.md) breaks them into tasks.

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
  `story_check walk` reaches the ending every time. Every character shown with `present` has a portrait. Still open: a
  live playtest of the route (`run-story-ari.ps1`), and a portrait for Nova (voice-only by design, so possibly none). Kreissack, Sorell and Plug have
  portraits. The seven NPC results are decided: Mara wins the Group A-out quarterfinal against Selene, the Crystal
  and Lyra defaults stand, and the three-way tie keeps the announced seed. Scope and open decisions are in
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
| M5 Full roster | 2027-11-30 | All 11 HARs, Tournament mode, remaining arenas and routes |
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

## Parallel tracks, always on

| Track | Standing rule |
| --- | --- |
| Rights | Every new asset gets a ledger row with origin and terms on the day it enters; nothing from the originals is committed |
| Parity | After any rules or data change, re-run the measurement and replay checks |
| Two looks | A HAR or arena is not done until both looks pass review and `har_check` |
| Docs | Update this plan at each milestone |

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

## Next three actions

1. Send the permission email (needs a contact; I can look for one).
2. Decide the simplified style direction from two or three quick renders of the Jaguar blockout.
3. Live playtest of Ari's route (`run-story-ari.ps1`).

(Spike A and the first pass of the tool audit are done; see the 2026-11-05 entry above.)

## References

- [Original game reference](OMF2097/OMF2097_REFERENCE.md)
- [Story treatment](OMF2107_LORE_v2.md)
- [Game specification](OMF2097_3D_GAME_SPEC.md)
- [Development plan](OMF2097_DEVPLAN.md)
- [OpenOMF repository](https://github.com/omf2097/openomf)
- [Original manual story](https://www.omf2097.com/wiki/doku.php?id=omf2097:story)
- [Decoded in-game help and text](https://www.omf2097.com/wiki/doku.php?id=omf2097:english.dat)
