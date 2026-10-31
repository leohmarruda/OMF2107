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
- **Step 2, save data: built.** `story_save` and `story_load_save` write and read a versioned
  text save (position, flags, log, script fingerprint); an older or newer format version, a changed
  script, or a damaged file is refused with a message and leaves the run untouched. The viewer
  autosaves at every choice and match result, resumes on start, and clears the save on restart.
  `story_check selftest` covers round trips at a say line, a choice, a match, and the end, and each
  refusal case.
- **Debug fights: built.** `--debug-fights` lets a tester skip a match by choosing win or loss, and
  logs it; `run-story.ps1` launches story mode and warns about a stale executable.
- **Step 3, the match handoff: built** as designed below. Tested end to end headlessly with no one at the
  keyboard: the story viewer starts the match, the AI wins, the result file is read, the story moves to the
  lose scene, and the log and autosave record it. Also tested: closing the story window mid-match ends
  OpenOMF and the match viewer, and closing only the match window leaves the story at the match with no
  result. Not yet tested: winning a match by playing it.
- **Fixes after the first playtest (2026-10-27).** (1) A second round appeared whatever the result. OpenOMF
  plays one round (a headless run showed a single round and match winner on the same tick), but in the
  match viewer Enter and Y on the result overlay still meant "try again", which restarted the arena. In
  story mode those keys now return to the story, and rematch requests are ignored. (2) The match did not
  seem to change the story, because the win and lose scenes only differed by a line before merging. The draft
  now lets the result decide who receives WAR's Tier-2 offer, which recovery scene plays, and the closing.
  The first fix is from reading the code and was not reproduced by playing, so it needs a playtest.
- **Step 5, selection screen: built** (decided 2026-10-27: the player is Crystal and picks her HAR, the
  rival takes the other, and the portraits are the original game's art). The script format gained `player`,
  `rival`, and `card` header lines, `@flag` HARs in `fight`, and `{flag}` text, all covered by
  `story_check selftest`. The selection screen shows each pilot's original portrait, OpenOMF stats, and card
  text. Tested: both HAR routes through the draft with `story_check play --har`, screenshots of the screen, and
  a full Shadow-route match through the pipeline (`-Player Shadow -Pilot Crystal -RivalPilot Christian`). The
  portraits are exported locally, git-ignored, and logged in `ASSET_LEDGER.md` as not distributable.
  Not tested: choosing a HAR with the keyboard on the screen, and playing Crystal in Shadow by hand.
- **Dialogue decision (2026-10-27):** the draft dialogue in `crystal_christian.story` is kept as it is for
  now after a playtest ("it ran fine"). A rewrite is deferred, not cancelled; the file stays placeholder
  wording built from `OMF20115_SIMPLE_LORE.md`.
- **Backdrops and sounds: built** (decided 2026-10-27: generated backdrops for story scenes, the original
  arenas behind fights, original sounds). The viewer draws the original arena image when a scene's `bg` names
  an arena and an exported file exists, and generated scenes otherwise (green room, medical bay, a stand-in
  Stadium, and a plain gradient for any other name). It plays two original menu sounds (move and press) for
  menu movement, choices, and starting a match; advancing dialogue is silent (playtest feedback, 2026-10-27:
  sounds matter more in the battle). The battle itself now has OpenOMF's own original sound effects and music:
  the match launcher takes a `-Sound` switch, which the story viewer passes unless muted, instead of
  starting OpenOMF with its audio disabled. `M` or `--mute` turns the viewer's sounds off and starts matches
  silent. The art and sounds are exported locally by `export_story_assets.py` and logged in the
  asset ledger as not distributable. Tested: screenshots of all backdrops, the sound export checked
  byte-for-byte against the sound tool, and the audio device opening with the sounds loaded, and a full match with `-Sound` (OpenOMF started without
  the audio-disable flag and opened its SDL_mixer audio device; the result reached the story). Not tested:
  hearing the menu sounds. The battle sound was played by the project owner and judged good (2026-10-27).
  Original music (the game's `.PSM` tracker files) was not attempted.
- **Illustrated sequence: built** (chosen 2026-10-27). The script format gained `art <name> [effect]`
  (fade, zoom, pan, or none; `art off` clears it; names may use `{flag}`), saved and restored with the story and
  covered by `story_check selftest`. The draft opens with four frames and captions: a title over the Stadium,
  Crystal's card, Christian's card, and a face-off showing the chosen HARs. The frames are composed locally from
  original portraits, arena art, and HAR idle sprites by `build_story_art.py`, with bars, a vignette, name plates,
  and text drawn by the tool; they are logged in the ledger as not distributable. Tested: screenshots of every
  frame in the viewer and the return to the backdrop afterwards. Not tested: how the zoom, pan, and fade look in
  motion (screenshots only show them a few seconds in). Changing the script invalidates older saves, so the first
  run after this change starts over.
- **Presentation pass (2026-10-27, inspired by the visual-novel style of the Ace Attorney games; presentation
  only, no typewriter blips, no screen shakes):** speaker portraits over the backdrop with the speaker lit and
  the other dimmed (a bob on the speaking portrait was removed after the first look), typewriter text (Enter shows the whole line, then moves on), a name tab and a blinking next arrow, and
  `flash` and `banner <text>` script commands. The draft gained three beats (a flash at the face-off, a TIER-2
  banner when the invitation arrives, and a flash when the telemetry message arrives); its dialogue is unchanged.
  Nothing from the series is used: no art, sounds, or catchphrases. Tested: the new commands in
  `story_check selftest`, and screenshots of the portraits, a half-typed line, narration, and the banner. Not
  tested: how the typing speed, flash, and banner feel in motion. A flash is a strobe of opaque white
  because the viewer cannot blend colours.
- **Endings (2026-10-29), read as one ending for each sibling:** after the existing closing lines the draft plays an
  illustrated epilogue on the Desert sunset: Crystal's ending (shaped by what she did with the telemetry: released,
  verified, or given to Christian), Christian's ending (shaped by whether he got the files, so whether the
  violent strike was ever on the table), a closing frame with the siblings together or apart (shaped by whether
  she told him about the tremors), and an "END OF SLICE" title. Five new frames, nine new scenes (25 in all), lore
  only: Crystal's weight of unverified evidence and Christian moving from control to trust and away from violence
  against civilians. Tested: all 12 combinations of evidence, tremors, and match result reach the end with
  distinct endings (`story_check play`), no scene is unreachable, and screenshots of each frame in the viewer.
  Not tested: the endings played in sequence with their timing.
- **Soundtrack (2026-10-29):** the script format gained `music <track>` (menu, arena0 to arena4, end, or off), saved
  and restored with the story and covered by `story_check selftest`. The viewer decodes the original `.PSM` files
  from `OMF2097/` with libxmp (now linked into the prototype) on a second audio device, loops the track, plays
  `menu` on the selection screen, goes quiet while a match runs, and follows `M` and `--mute`. The draft uses the
  menu track for the opening and the scenes around the match, `arena0` before the match, and `end` for the
  endings. Tested: all seven original tracks decode to real audio with libxmp (non-zero peak and RMS over the
  first six seconds), and the viewer loads `MENU.PSM` and reports its music device ready with no errors. Not
  tested: hearing it, the volume balance against the effects and the battle, and the track changes in sequence.
  Recorded in the ledger as local-only and not distributable.
- **Playtest package (2026-10-29):** `project/scripts/package-playtest.ps1` zips a Release build (`build.ps1 -Config Release`), the C runtime, the story, the exported art and sounds, and the original game data into `dist/OMF2115-playtest.zip` (about 15 MB) with `Play.bat`, `Play-NewGame.bat`, and a tester README. The launchers use `bin/` when it exists. Tested: the unzipped package ran a full match through the pipeline from its own folder (result file written, no errors, sounds and music loaded). Not tested: a PC without the build tools, or SmartScreen's first-run prompt. It contains non-distributable material; see the ledger.
- **Not yet done:** a clean end-to-end playtest by someone who has not seen the build (step 6).

## Step 3 design: the match handoff (built)

**What exists today.** A live match is two processes joined by shared memory: OpenOMF with
`--omf3k-live`, and the viewer in `--source-live` mode, both started by `run-blockout-jaguar.ps1`.
OpenOMF builds the match from environment variables. Player 0 is the keyboard player and takes its
pilot from `OMF3K_LIVE_PILOT_ID`; player 1 is an AI fixed to the other HAR with a hard-coded pilot
(Shirro against Shadow, otherwise Crystal). The match is one round in Stadium with hazards off, and
when it ends OpenOMF stays on the final pose while the viewer shows the winner and a retry prompt.

**Proposal: the story viewer runs a match as a child pipeline and waits for a result file.** At a
`fight` command the story viewer starts a launcher script (a variant of the existing one) and waits;
the viewer's window stays open on a "match in progress" screen. When the match is decided, the live
viewer writes a small result file and exits, and the story viewer reads it and continues with
`story_fight_result`. This reuses the working live pipeline and keeps story logic out of OpenOMF.

Changes it needs:
1. **OpenOMF:** read `OMF3K_LIVE_RIVAL_PILOT_ID` so the rival can be Christian (a few lines in
   `game_state.c`; the HARs stay Jaguar and Shadow). Optionally `OMF3K_LIVE_AI_LEVEL` later.
2. **Live viewer:** a `--result-file path` option. When the match is decided it writes the winner
   and the winner's remaining health, waits a few seconds on the final pose, and exits instead of
   showing the retry prompt.
3. **A launcher script** for story matches: pilot and HAR for each side, plus the result file path.
4. **Story viewer:** run the launcher at a `fight`, wait while still handling window events, then
   read the result. If the match exits without a result (window closed, a crash), keep the fight
   event and offer to retry. Debug fights stay available as the way to skip.
5. **Tests:** the result file format and the retry path can be tested headlessly; a full match needs
   a playtest.

**Conventions to confirm.** The first fighter in a `fight` line is the human player and the second
is the AI, and `win` means the first fighter won, which is what the script and runner already
assume. The match uses the live pipeline's current settings (one round, Stadium, no hazards).

**Risks.** Two windows and about four seconds of viewer warmup before OpenOMF starts; the pipeline is
Windows-only (shared memory); a rival AI at default strength may not suit the story; and this is an
interim bridge, since the later integration should hold story and match in one program.

**Alternatives considered.** Running OpenOMF and the story in one process would remove the
two-window handoff but is a much larger change. Moving the story into OpenOMF's own scene system
is the intended later integration. Both are better done once the story format has settled.

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
