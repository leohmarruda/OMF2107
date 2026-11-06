# Release plan: free fan project, original assets, real 3D, two looks

Status: proposed 2026-11-05. All dates are estimates for planning, assuming one main developer working with
Claude, and are least reliable beyond Phase 3. Phase starts count from Monday 2026-11-09. Update this file at the
end of each phase.

Fixed decisions: [rights and release rules](RIGHTS.md); no original data in a release; real 3D; two visual modes,
the simplified one a stylised look in its own right, both driven by one rig and one gameplay proxy
([engine paths](ENGINE_PATHS.md)); one source per HAR ([HAR pipeline](HAR_PIPELINE.md)). The engine base is option A:
a standalone `fightcore` with a project data pack, linked in-process.

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

## Progress

- 2026-11-05: Spike A done (read-only), result **go with conditions**: [SPIKE_A_FINDINGS.md](SPIKE_A_FINDINGS.md). The
  tool audit (P0) first pass is in [HAR_PIPELINE.md](HAR_PIPELINE.md). Still open in Phase 0: permission email,
  simplified style brief, `rig.json` fields.

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
revise the roadmap from the real figure). Local versus, controller support, two more arenas, more pilots. Public demo
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
| Docs | Update `ROADMAP.md` and this plan at each milestone |

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
2. Start Spike A and the tool audit (both are read-only on the codebase).
3. Decide the simplified style direction from two or three quick renders of the Jaguar blockout.
