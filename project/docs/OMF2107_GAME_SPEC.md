# OMF2107 — game specification

**Version:** 0.3, 2026-11-09. Renamed from `OMF2097_3D_GAME_SPEC.md`; now holds the design rules taken from the archived Reimagined pitch. `DEVPLAN.md` wins on conflict.  
**Project name:** OMF2107  
**Basis:** the original game, the local OpenOMF source, the [original-game reference](OMF2097/OMF2097_REFERENCE.md), and the proposed [story treatment](OMF2107_LORE_v2.md). The [Reimagined design pitch v0.3](_archive/omf-reimagined-design-pitch-v0.3.md) is archived; the rules still in force are restated here and in `DEVPLAN.md`.

## 1. Product definition

OMF2107 is a single-player robot fighting game with a career layer, built on
*One Must Fall 2097* in 3D. Players choose a **pilot and a HAR independently**,
fight on a **side-on gameplay plane**, and use recognizable OMF attacks, specials, stun,
combos, arena hazards, and scrap finishes. The new production adds expressive
3D robots and arenas, anime-influenced character sequences, a deeper 2097
Ganymede story, and a Tournament career where damage costs money, rivals
remember and sponsors push. The original combat, measured against OpenOMF,
is the foundation; new mechanics are added on top of it in the Tournament
(`career` ruleset). The only changes to `classic` are the Arcade tune-ups and
the last-round destruction finisher (`DEVPLAN.md`, "Rulesets" and "Finishers").

The original's fast match rhythm and readable robot identities are the
reference. The 3D camera and animation should make those fights more dramatic
without changing their fundamental geometry or controls.

### Design pillars

1. **OMF at first glance and first input.** Jaguar, Electra, Katana, and the
   other HARs must be recognizable by silhouette, movement, and signature
   moves. The game must feel like a fighting game within one round.
2. **Two identities per fighter.** The pilot affects stats, voice, rivalry,
   portrait, and story; the HAR determines body, range, movement, and moves.
   The selection system must never merge them into fixed character pairs.
3. **Spectacle with legible rules.** 3D models, lighting, cameras, and impact
   effects serve spacing, facing, guard, and hit confirmation.
4. **People behind machines.** Between matches, character scenes show
   ambition, intimacy, fear, recovery, and moral conflict. Choices affect
   relationships and endings without replacing the fights.
5. **A career where damage has a price.** Tournament mode keeps the
   original's money, training, repair, and upgrades, adds localized damage
   with readable repair decisions, and keeps the career persistent. Story and
   Arcade stay on the classic rules.

## 2. Product scope

| Area | Full game target | First playable proof |
| --- | --- | --- |
| Pilots | Original ten selectable pilots, each with an ending; Kreissack remains a boss | Ari (story route); a custom pilot (Tournament) |
| HARs | Original ten standard HARs; Nova as story boss and unlock policy to be decided after rights review | Jaguar plus one contrasting HAR |
| Arenas | Original five arenas with their recognizable hazards | Stadium, then one hazard arena |
| Modes | Story, Tournament, Arcade/One Player; Training as a support tool; local Versus is a later decision | One story segment and a short Tournament bracket |
| Story presentation | Illustrated/anime sequences, voiced or text dialogue, in-engine transitions, pilot endings | Intro, pre-fight exchange, recovery scene, short ending |
| Tournament | Persistent custom pilot, ranking, money, robot ownership, training, parts, localized damage, repairs, sponsors, rival events | One short bracket with region damage, repair choices and a persistent purse |

**Platform target:** desktop Windows first, with Linux support retained where
practical through the existing cross-platform source. Keyboard and gamepad are
both primary inputs. The minimum PC profile is fixed at M3
(`DEVPLAN.md`, 3D engine requirements and R12). Online play and console ports are later scope decisions; neither blocks
the first complete game.

## 3. Core player flow

1. Choose a mode.
2. Select a pilot, then a HAR. Story may recommend a pairing but does not
   force it. Tournament uses the player's custom pilot and owned HARs.
3. See a short opponent introduction with a skip option.
4. Fight on a fixed side-on plane. Camera, effects, and stage geometry add
   depth without changing left/right combat inputs.
5. See the result, reward, and a character beat appropriate to the mode.
6. In Story, choose a response or alliance at selected moments and advance
   through the Ganymede bracket. In Tournament, repair, train, buy, and enter
   the next event.

Every mode uses the same move definitions. Match rules come from a named
ruleset, always shown before the fight:

- `classic` (Story, Arcade): the original rules, measured against OpenOMF.
  Arcade adds its tune-up multipliers as disclosed pre-match conditions.
- `career` (Tournament): `classic` plus localized damage (section 7).

Story has no economy, upgrades or damage.

## 4. Combat specification

### 4.1 Spatial rules and camera

- Fighters move left/right on one gameplay plane; jumping and crouching retain
  their original purpose. Visual geometry may extend behind the plane.
- The default camera frames both HARs and the relevant arena boundary.
  Dynamic movement may adjust height, zoom, and lateral framing. It must not
  cross the fighting axis or reverse attack directions during play.
- Facing changes follow explicit combat rules, not the 3D model's rotation.
  A crossover test must show predictable left/right input behavior.
- Match intro, victory, scrap, and story cinematics may use free cameras only
  after player control is paused or the match is over.

### 4.2 Inputs and mechanics

- Preserve directional movement, punch, kick, standing and low guard,
  jumping, crouching, throws, and each HAR's distinctive special inputs.
  Remapping is available for keyboard and gamepad.
- **Stun is the only combat resource.** There is no heat, overclock, rage or
  desperation meter.
- Maintain separate life/energy and stun behavior, round wins, time limits,
  knockdowns, air hits, combos, and the original-style dramatic finish.
- Destruction finishers are available only in the last round of a match and
  only when the finishing HAR is in good condition (in `career`, no Critical
  region and the limb used Operational; in `classic`, every round won without
  losing one, each ended with at least 50% health). Otherwise the match ends with the normal finish.
  The HUD shows availability, and the AI obeys the same rule; when the AI
  destroys the player's HAR, the full sequence plays. This is a
  documented change from the original, added after the parity gate.
- Hits use authored gameplay shapes and timing on the fight plane. Visual
  limbs may stretch or trail for impact, but rendered mesh overlap alone does
  not decide damage.
- Arena hazards are readable and consistent. Their activation area and timing
  must be learnable; camera cuts cannot hide the cue.
- AI uses the same move legality and recovery rules as the player. Difficulty
  adjusts decision quality and reaction allowance, not hidden damage bonuses.
- A 60 Hz fixed simulation is the initial implementation target. If the source
  baseline shows that another tick model is necessary for move parity, record
  the decision before content production.

### 4.3 Fidelity and balance gates

Capture reference matches from OpenOMF and the original data. For Jaguar and
one rival, document walking speed, jump arc, facing, attack startup and
recovery, hit and push distance, block response, stun, and special behavior.
The 3D match should be compared side by side with the reference before the
remaining roster is built. Changes for feel or accessibility are deliberate,
documented tuning decisions, not accidental consequences of new animation.

Training mode exposes move lists, input display, hitboxes, stun state, and
record/playback for the practice opponent. Match replays should store inputs
and game version so fights can be reviewed and combat regressions reproduced.

### 4.4 Opponent AI

AI is central to a single-player fighting game; its complexity must show up as
results the player can see.

- **Two layers.** A stable **personality** per opponent (aggression, preferred
  range, risk tolerance, tactical preferences, adaptation speed, willingness
  to exploit damage), defined independently of difficulty; and **bounded
  adaptation** that tracks a small set of observed habits (jump rate, approach
  pattern, throw and strike mix, repeated punishes, retreats under damage) and
  reacts only after plausible observation and within reaction limits.
- **No input reading or impossible foreknowledge.** Difficulty comes from
  decision quality and from punishing predictable habits, never from perfect
  reactions or hidden bonuses.
- **Legible counterplay.** The player can tell what an opponent learned
  (through behaviour, banter or a post-match report, not an analytics screen)
  and vary tactics to beat it.
- **Story-reactive variants** (fight to win, hesitant, desperate) may reflect
  relationships without making the AI deliberately incompetent.
- **Career memory** (who won, decisive tactics, grudges) affects preparation
  and commentary; it is separate from real-time adaptation.
- **Bosses** may be asymmetric if their patterns and tells are learnable.
- **No machine learning is required.** A learned "Shadow" AI is rejected.
- **Verification:** profiles recognizable without dialogue; adaptation beats
  repetitive habits without cheating; players can counter-adapt; every
  difficulty stays fair. Collect decision traces in test builds, not only win
  rates.

## 5. Visual, animation, and audio direction

### HARs and arenas

- New 3D HAR models preserve the original machines' silhouette, main colors,
  weapons, and scale relationships. Materials add mechanical depth without
  turning the roster into interchangeable realistic robots.
- For Jaguar, use the approved [front, back, and right-side modeling references](../robots/jaguar/canonical/README.md) as the visual source of truth for the OMF2107 mesh. Original sprites continue to guide movement and recognizability.
- For Shadow, use the approved [front, back, and right-side modeling references](../robots/shadow/canonical/README.md) as the visual source of truth for the OMF2107 mesh. Original sprites continue to guide movement and recognizability.
- Where the original sprites are too small to resolve a robot feature or a pilot's appearance, consult OMF 2097 Remastered's higher-resolution robot and character sprites as an additional reference. Keep the approved OMF2107 modeling views and measured OpenOMF move timing as the production guides; record the remastered asset used and review its terms before reuse.
- Animation has a readable anticipation, active strike, and recovery.
  Gameplay timing drives animation; animation does not secretly change hit
  timing or move distance.
- Rebuild Stadium, Danger Room, Power Plant, Fire Pit, and Desert as layered
  3D spaces. Their lighting and hazards remain recognizable at fight-camera
  distance. Avoid clutter directly behind the fighters.
- **Readability in 3D:** strong silhouettes, clear startup tells, and
  visible damage that never hides collision behaviour or a startup tell.
- Effects emphasize impact, stun, electricity, fire, and arena danger. Offer
  settings to reduce flashes, camera shake, and visual noise.
- The HUD shows pilot and HAR names, health/energy, stun, timer, rounds, and
  relevant mode status. Critical fight information remains visible during
  cinematic effects.

### Human characters and anime sequences

The human cast receives a distinct illustrated style consistent with the
retro-future OMF setting. Sequences should feel like sharp character drama,
not imports of another series' designs or iconography.

| Sequence type | Use | Production rule |
| --- | --- | --- |
| Character portraits and expression changes | Selection, banter, recovery, Tournament encounters | Reusable pose and expression library for all ten pilots |
| Short 2D animated scenes | Opening, act turns, major revelations, endings | Reserve full animation for moments that change the story |
| In-engine scenes | HAR launch, arena entrances, victories, Nova reveal | Reuse match rigs and arenas; keep them brief and skippable |
| Dialogue panels with motion graphics | Most between-match conversations | Text, subtitles, voice where available, and readable pacing |

The story treatment permits optional romantic tension among adult characters.
All characters are presumed bisexual, regardless of their default
relationships; romance routes are available only to consenting adults.
Intimate moments are skippable and depend on
consent. OMF2107 establishes Angel as 28 because the original manual leaves her
age unspecified. Steffan remains 17 and has no romance or sexual route in the
2097 story.

Audio retains the energetic arena identity of OMF. New music may reinterpret
the pace and instrumentation without assuming rights to the original tracks.
Sound must separate a blocked hit, clean hit, stun, hazard, and scrap finish.
Story dialogue can launch with text and focused voice lines; full voice acting
is a content-budget decision made after the first route is playable.

## 6. Story mode

### Premise and structure

Story mode follows WAR's 2097 tournament for the Ganymede position. The
[story treatment](OMF2107_LORE_v2.md) supplies the proposed conspiracy:
an experimental neural link drains pilots, a cover-up protects the Ganymede
charter, and Kreissack uses the trial to advance Nova. The tone combines public
spectacle with private physical and emotional cost. There is no supernatural
or cosmic explanation.

The player chooses one of the original ten pilots. Each route has an intro,
pre-fight rival exchanges, at least one distinctive mid-route scene, a Nova
conclusion, and a pilot-specific ending. Every pilot has a default path while
unselected; when selected, the player controls their decisions and alliances.
No playable pilot is irreplaceable: critical evidence and finale functions
have alternate carriers. Ari is the reference route for the first
complete production pass, not the required lead of every route.

### Choices and consequences

- Between fights, let the player choose whom to approach and whether to
  challenge, sabotage, spy, share secrets, or pursue a consensual romance with
  an eligible adult. These choices affect relationships and evidence routes.
- Choices alter relationship scenes, information available, and epilogue
  details. They do not skip required HAR fights or replace pilot-specific
  endings with one generic conclusion.
- A romance is never the sole route to critical evidence. Alex, Darius
  Kade, and Leena Sato are optional media allies and adult romance options;
  their reporting functions have alternatives if they are absent or opposed.
- The hidden link's toll is primarily shown in narrative scenes. If a player
  accepts a performance boost that has a gameplay cost, show both effects and
  let them decline it. Never degrade basic input response without notice.
- Shared scenes, replayed cutscenes, and dialogue can be skipped; a log records
  key evidence and decisions. Route select shows which pilots are complete.

**First complete story slice:** Ari's route (`project/data/story/ari.story`,
Chapters 1 to 6, built and passing `story_check`; see `DEVPLAN.md`
Progress). It covers a pre-fight exchange, match, recovery scene, evidence
choice, and consequence, and tests the new story's tone while preserving OMF's
core structure. The Crystal versus Christian route is deferred to Phase 4 of the
development plan. `DEVPLAN.md` wins where the two documents disagree.

## 7. Tournament mode

Tournament is a separate, replayable career on the `career` ruleset. It
expands the original mode's custom pilot, earnings, training, robot purchases,
repairs, upgrades, and rankings while keeping fights as the main activity. Story-mode conspiracy
choices do not gate Tournament progression.

### Career loop

1. Create a pilot identity and choose starting strengths within a fixed budget.
2. Enter a ranked event or a specific contract with known prize, arena,
   opponent class, and repair risk.
3. Fight and receive transparent payouts for result and optional objectives.
4. Spend money on repairs (full repair, standard patch, or fight damaged),
   insurance, training, or legal HAR parts; compare the projected effect
   before buying.
5. Build rivalries and sponsorship reputation, advance to tougher brackets,
   and work toward the top title.

### Localized damage

- Four regions (arms, legs, torso, head), three states each: Operational,
  Damaged, Critical. Match health and stun work as in `classic`; region
  condition is a separate layer.
- Effects are numeric and deterministic: weaker punches (arms), slower walk
  with jumps unchanged (legs), more damage taken (torso), longer own stun
  (head). No move is ever removed. Values are in `DEVPLAN.md`.
- Hits are assigned to regions by hit height (low to legs, mid to torso, high
  to head and arms), so players can aim for a region without a new input.
  Region state lives in the simulation and is part of replays.
- Damage carries between rounds of a match and between matches until
  repaired. The pre-match screen shows the opponent's region states.

### Persistence and insolvency

- The career is persistent: money, owned HARs, upgrades and unrepaired damage
  carry between events.
- Insolvency ends the career (game over). Before that point, sponsors and
  other resources (an advance, a contract with conditions, a salvage sale,
  insurance) offer ways out, and the game warns before any match that could
  end the career. The trigger is the original rule: money still negative after
  two consecutive matches.
- A routine loss never ends the career on its own; it can drop the pilot to a
  lower bracket or a qualifier.

### Economy rules

- Every spend is an opportunity cost, not a flat tax: **repair** (full repair,
  standard patch, fight damaged), **preparation** (legal upgrades and
  opponent-specific choices) and **risk management** (insurance, salvage).
  Example: a damaged arm before an aerial opponent; restoring the arm, buying
  an anti-air option and saving the money should each sometimes be rational.
- **Solvency target:** expected winnings per fight minus expected repair and
  preparation cost is positive for a representative player at default
  difficulty. That alone is not enough: the economy simulation also measures
  the loss tail, the chance of reaching insolvency after one or two bad
  fights, and recovery without grinding.
- **No turtling incentive and no recklessness incentive:** bonuses reward
  varied skill, including precise defence; contract objectives are explicit,
  feasible and optional.
- **Anti-spiral tools:** cheap patches, insurance, salvage sales, sponsor
  rescues, lower brackets. A failing player never also loses the ability to
  fight competently.

### Sponsors and contracts

- Sponsors are actors with agendas, not multipliers. Offers can include cash,
  equipment, repair access, intelligence, invitations or protection; demands
  can include a fighting style, testing a part, keeping a secret, throwing a
  match or taking a side.
- **Every questionable offer has a legible refusal path**, even if refusal
  costs an advantage.
- Consequences cross systems: money, reputation, rival behaviour, access and,
  where relevant, story evidence.
- No obvious "good" or "evil" bonus: principled choices can be costly in the
  short term.
- Major offers are authored; small contracts are reusable templates.

### Rivals and reputation

- Named rivals remember important matches, adjust HAR and preparation, change
  sponsors and reference what happened, using a small set of state tags and
  reusable events rather than bespoke writing for every history.
- Reputation tracks how the pilot fights and behaves (sportsmanship,
  spectacle, ruthlessness, reliability, corporate alignment) through a few
  broad, readable profiles, not many hidden gauges.

### Improvements over the original

- **Clear economy:** show repair estimates, part effects, training limits,
  event rewards, and how a purchase changes the pilot or HAR.
- **Build identity:** upgrades create distinct approaches but remain bounded;
  a well-played base HAR can beat an upgraded one.
- **Rival continuity:** named pilots remember prior fights, issue challenges,
  and appear in short illustrated scenes. These scenes add character without
  forcing lengthy dialogue between every match.
- **Less grind:** offer several event types and optional contracts, while
  ensuring core ranking progress is possible without repeating easy fights.
- **Recovery decisions:** repair damaged equipment, rest/train the pilot, or
  enter the next event at a disclosed disadvantage. No invisible injury roll.
- **Save clarity:** autosave after matches and purchases; show the next event
  and current build at resume.

The first Tournament slice needs one custom pilot, two HARs, region damage, a
short bracket, prize money, a repair decision with real trade-offs, one part
upgrade (the M3 gate in `DEVPLAN.md`). Rankings arrive at M6.
Balance can expand only after this loop is fun over repeated sessions.

## 8. Other modes and usability

- **Arcade/One Player:** a quick original-style ladder without the longer
  story scenes, on `classic` with stacking tune-ups between fights (see
  `OMF2107_ARCADE_MODE.md`).
- **Local Versus (later decision):** two players on keyboard/gamepads with
  pilot and HAR choice, arena choice, round/time options, and rematch, on
  `classic`.
- **Training:** move list, input display, dummy guard/action settings,
  hitbox/stun view, and saveable practice setup.
- **Options:** remappable input, text size, subtitles, dialogue log, color
  differentiation beyond hue, reduced flashes/shake, scalable graphics,
  audio sliders, and skippable scenes.
- **Accessibility (proposed 2026-11-09, decide by M4):**
  - Optional assist inputs per profile, such as one-button specials. They
    change how a move is entered, never its timing, damage or rules.
  - A **Story difficulty** that softens execution (AI decision quality and
    reaction allowance) without changing the ruleset.
  - Readable damage and stun indicators that do not rely on flashing or
    colour alone.
  - No reflex quick-time events; normal defeats never need one.
  - Assists never alter `classic` or `career` numbers. Whether assists are
    allowed in Tournament is open (see `DEVPLAN.md`).
- **Onboarding:** a short optional tutorial teaches movement, guard, stun,
  one special, and arena hazards. It should use an actual HAR, not a detached
  mini-game.

## 9. Production architecture

### What the checkout already provides

OpenOMF is a C11/CMake project using SDL2 and an OpenGL 3 renderer. Its local
source contains pilot and HAR identifiers, arena scenes, fight rules, resource
loaders, Tournament systems, replay/network code, and tests. The current
`project/prototype` is a standalone SDL2/OpenGL side-on build that renders 3D
Jaguar, Shadow and Katana and plays Ari's route and Arcade (see `DEVPLAN.md`,
current state). Its own combat loop is a `--sandbox`-only placeholder; real
fights run on OpenOMF's rules until `fightcore` replaces them.

### Recommended implementation path

1. Keep a runnable OpenOMF baseline and capture match data before changing
   combat. Preserve its original mode and data behavior as a comparison tool.
2. (Done, gate closed 2026-10-27.) Build a **side-on 3D match spike** using the current C/SDL/OpenGL stack and
   two HARs. Separate combat state from 3D pose and camera state. Feed both
   from the same fixed-tick match events.
3. Audit how much of OpenOMF's 2D robot and scene logic can be adapted without
   changing timing. Reuse tested rules, data parsing, and mode logic where
   practical; place new models, animation, effects, and scenes behind explicit
   interfaces. Do not assume the existing sprite renderer can simply display
   rigged models.
4. After the spike, decide whether to continue in the C renderer or move the
   presentation/content layer to a dedicated 3D toolchain. Judge the options
   on animation authoring, fight fidelity, build reliability, and team skills.
   Keep combat data and story scripts portable so this decision does not erase
   the baseline work.
5. Author new story dialogue, branching flags, portraits, and cutscene cues as
   data. Add versioned saves and content validation before writing ten routes.

**Subsystem boundary:** simulation owns inputs, state, collisions, damage,
stun, hazards, AI, and results; presentation reads events and poses; narrative
owns route state and between-match choices; Tournament owns career economy.
Presentation must not be the authority for whether a hit landed. The boundary
allows a match replay to reproduce the same outcome with lower graphics.

## 10. Validation and acceptance criteria

| Gate | Pass condition |
| --- | --- |
| Fight identity | A player familiar with OMF recognizes the HARs, plane, guard, specials, stun, and hazards in an unlabelled match clip and short hands-on test. |
| Combat parity | Side-by-side Jaguar reference documents all timing and spacing differences; intentional changes are recorded and playtested. |
| Camera and input | Camera motion never makes a directional attack or guard ambiguous; fighters retain a readable silhouette at normal speed. |
| Story slice | Ari's route plays start to finish, offers a clear evidence choice, records it, and shows a consequence after the match. |
| Tournament slice | A custom pilot finishes a bracket, earns money, makes repair choices under region damage, upgrades a HAR, and sees changed performance after loading a save. Playtesters choose different repairs for the same situation and do not play passively. |
| Performance | The worst-case match (both HARs Critical in several regions, maximum effects) holds 60 fps in both looks on the minimum PC (budgets in `DEVPLAN.md`). |
| Content pipeline | A new dialogue scene, model, animation, and arena hazard can be added without changing combat code. |
| Accessibility | Every story scene has readable text and skip/log support; flashes and camera shake can be reduced. |
| Release readiness | All intended pilots, HARs, arenas, routes, and modes pass content review; assets and music have documented distribution rights. |

Target smooth 60 fps match presentation on the eventual minimum PC profile.
Set a concrete GPU/CPU profile after the first representative HAR, arena,
effects, and HUD are running together. Test controller latency and frame pacing
on hardware, not only in a headless check.

## 11. Delivery phases and decisions

| Phase | Deliverable | Decision unlocked |
| --- | --- | --- |
| A. Baseline | Source match captures, move data, rights inventory | Which mechanics can be reused unchanged? |
| B. 3D fidelity spike | Two recognizable HARs, Stadium, fixed plane, camera, one complete move set | Keep the C rendering path or choose a 3D content toolchain? |
| C. Vertical slice | Two pilots, two HARs, second arena hazard, polished match, Ari's route story segment | Is the combat/story presentation worth scaling? |
| D. Systems alpha | Core combat roster in progress, Tournament economy, saves, UI, art pipeline | Are authoring and balance costs sustainable? |
| E. Content production | Ten pilots, ten standard HARs, five arenas, routes, anime sequences, Tournament events | Is the full target complete and licensed? |
| F. Release candidate | Performance, accessibility, balance, packaging, regression and rights checks | Ship or narrow scope explicitly. |

Phases A and B are done. `DEVPLAN.md` uses Phases 0 to 7 and milestones M0 to
M7; the letters above are the old phases. Mapping: A and B are done; C is M4
(clean vertical slice); D and E span M5 and M6; F is M7. DEVPLAN adds a
career-core milestone (M3) after the classic duel (M2). The next executable
tasks and dates live there.

The two visual looks are **blockout** (flat, readable, shipped as a finished
look) and **mesh** (full models); both must pass `har_check`. See `DEVPLAN.md`.

## 12. Rights and source boundary

The OpenOMF source in this checkout is MIT licensed; the original OMF game
data, designs, characters, dialogue, music, and title are separate rights
questions. Local access to `OMF2097` data is a development reference, not a
distribution grant. Record provenance for every final asset and text passage;
commission or create replacement art and audio when reuse rights are unclear.
Patent concerns about fighting-game mechanics are unverified; get legal advice
before shipping a system closely resembling a known patented one.
The story's anime influence should be expressed through pacing, acting, and
framing, with original designs and scenes.

## 13. Open decisions for the team

These do not block the baseline or first 3D spike:

- Final game title and permission to distribute original OMF identity/assets.
- Whether Nova becomes unlockable after its boss role.
- Whether all story routes receive voice acting or only key scenes.
- Final minimum hardware profile (fixed at M3) and whether Linux ships on the same day.
- Whether local Versus ships, and whether online play follows it.
- Sponsor safety net and upgrade model (decided at M3, see `DEVPLAN.md`).
  Damage carry-over between rounds and matches is decided (2026-11-09).

## Source notes

- [Local OpenOMF build instructions](../../BUILD.md), [CMake configuration](../../CMakeLists.txt), and [pilot/HAR identifiers](../../src/game/common_defines.c).
- [Existing 3D prototype notes](../prototype/README.md) and [development plan](DEVPLAN.md).
- [Original OMF manual](https://www.omf2097.com/wiki/doku.php?id=omf2097:manual.doc) and [decoded story text](https://www.omf2097.com/wiki/doku.php?id=omf2097:english.dat) for canon checks.
