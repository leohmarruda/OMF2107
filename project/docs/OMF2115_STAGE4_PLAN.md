# Stage 4 plan — one-player story slice

Status: proposed 2026-10-27, after the Stage 1–2 match comparison gate was closed.
This plan narrows the [development plan](OMF2097_DEVPLAN.md) phase C and the
[game specification](OMF2097_3D_GAME_SPEC.md) section 6 to what can be built next.
It does not change either document; open decisions are listed at the end.

## Goal and exit check

A player picks a pilot and a HAR, sees a character exchange, fights a match on
OpenOMF's rules, sees a recovery scene, makes an evidence choice, and sees its
consequence later. Choices persist through save and load, and the fight stays
required. This is exit gate C of the development plan.

## What exists

- A faithful match: OpenOMF owns combat, the 3D viewer renders its per-tick state,
  and all 35 Jaguar and Shadow attacks are measured.
- A fighter selection screen: ten pilots and two HARs (Jaguar, Shadow) with their
  OpenOMF stats. The story may recommend a pairing but must not lock it.
- A match result and a retry or quit choice at the end of a live match.
- OpenOMF's own scenes (`cutscene.c`, `newsroom.c`, `vs.c`, `mechlab`) as a reference for
  scene progression. I have not read them for reuse.

## What does not exist

I searched the 3D prototype (`project/prototype/main.c`) and found no dialogue,
cutscene, portrait, choice, or save code. Stage 4 builds all of these, plus the
writing and art that feed them.

## Proposed work, in order

IDs refer to the development plan.

1. **Scene data format and runner (C05).** A data file describes lines, speakers,
   choices, and flags; a runner plays it with skip and a log. First version is text only
   with placeholder portraits. Acceptance: a writer edits a scene without touching combat
   code, and invalid references are reported.
2. **Save data (D02).** Versioned story progress and choice flags, with a test that
   an older save loads or fails with a clear message.
3. **Match handoff.** Start a match from a scene with chosen pilot and HAR, and return
   the result (winner, health left) to the scene runner. This is the one integration point
   between the story and OpenOMF; the 3D client already detects the result.
4. **Route content (C06).** Author the slice: pre-fight exchange, match, recovery
   scene, evidence choice, and a consequence beat.
5. **Pilot selection with route context (C04).** Add portraits, stats, and route
   hints to the existing selection screen.
6. **Polish for the gate (C07–C09).** One illustrated sequence, audio cues, and an
   end-to-end playtest by someone who has not seen the build.

Steps 1–3 can proceed without final art or finished writing, and they carry most of
the technical risk, so they come first.

## Progress

Decisions made 2026-10-27: the slice is Crystal versus Christian, the scene runner lives in
the 3D prototype for easier testing (integration with OpenOMF comes later), and the first pass is
text with placeholder portraits.

- **Step 1, scene format and runner: built.** `story.c` parses and validates the script format,
  runs it, and keeps a log and flags; `story_check` self-tests and plays scripts without a window;
  `omf3d_prototype --story` plays a script with a dialogue box, choices, skip, and a log. A draft
  of the slice (`project/data/story/crystal_christian.story`, 12 scenes) was written from
  `OMF20115_SIMPLE_LORE.md` and checks and plays through.
- **Not yet done:** save data (step 2), the real match handoff (step 3), review and rewrite of the
  draft dialogue, portraits, and audio.

## Decisions that were needed before step 1 (answered above)

1. **Which slice.** The specification and development plan say Crystal versus Christian
   (exchange, match, recovery, evidence choice, consequence). The story treatment's
   section 15 says a two-match ensemble slice (Round 1 match, the Tier-2 offer scene
   with three pilots, a concealment moment, and the green room scene). They test
   different things. I recommend Crystal versus Christian, because it matches the
   exit check.
2. **Where the scene runner lives.** In the 3D prototype client, which is the only
   place that currently draws the match, or inside OpenOMF's scene system. The
   prototype is the likelier fit, but then story logic and save data live outside
   OpenOMF and need a clean handoff.
3. **First pass format.** Text and placeholder portraits only, or illustrated frames
   from the start. Text-first lets the writing and flow be judged cheaply.
4. **Rights.** The story uses the original cast and setting; the
   [roadmap's rights checkpoint](ROADMAP.md#rights-checkpoint) applies to any portrait or
   dialogue asset that is reused from the original game.

## Risks

- The scene runner and match handoff touch both the 3D client and OpenOMF; a poor
  boundary here is expensive to fix later.
- The two slice definitions may produce rework if the choice is made late.
- Writing and art are not started, and they gate steps 4–6.
