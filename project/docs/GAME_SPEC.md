# Game specification

**Version:** 0.4, 2026-11-11. Rewritten for the independent game; v0.3 was the OMF2107 spec. `DEVPLAN.md` wins on conflict.  
**Title:** *Mecha Link 2100* (chosen 2026-11-11; trademark and store clearance pending, [REBRAND_CHECKLIST.md](REBRAND_CHECKLIST.md) D1). This document mostly says "the game".  
**Basis:** the project's own design decisions, recorded in `DEVPLAN.md`. *One Must Fall 2097* is an acknowledged inspiration and OpenOMF (MIT) is the development scaffold (section 9). Neither is a source of names, characters, robot designs, setting, story, text, art or audio.

**Terms.** The fighting machines are **mechas** (working term, 2026-11-11, replacing "HAR"); this spec also says
"robot" where that reads better. Code, data and older docs keep the old working names (OMF2107, HAR, the original robot and pilot names) as private placeholders until the rename sweep (R22) reaches them.

## 1. Product definition

The game is an original single-player robot fighting game in 3D, with a career layer. Players choose a **pilot and a
robot independently**, fight on a **side-on gameplay plane**, and use directional attacks, specials, stun, combos,
arena hazards and destruction finishers. Between fights, illustrated character scenes carry an original story. A
Tournament career makes damage cost money; rivals remember and sponsors push.

Its roots are the 1990s side-view robot fighter, *One Must Fall 2097* above all: short, fast rounds; heavy machines
with very different bodies; pilots separate from the robots they drive; a career of prize money, repairs and upgrades.
Those are genre conventions and mechanics, and the game keeps them. Its title, world, cast, robots, art, music and text
are its own.

Two rulesets share one set of move definitions:

- `classic` is the game's base rules. Its starting values were measured from OpenOMF (section 4.3) and it changes only
  through documented tuning decisions. Story and Arcade use it; Arcade adds disclosed tune-ups.
- `career` (Tournament) is `classic` plus localized damage (section 7).

### Design pillars

1. **Readable machines.** Each robot is recognizable by silhouette, movement and signature moves within one round. No
   robot reads as a machine from another game (derivation rule in `REBRAND_CHECKLIST.md`). The game must feel like a
   fighting game within one round.
2. **Two identities per fighter.** The pilot affects stats, voice, rivalry, portrait and story; the robot determines
   body, range, movement and moves. The selection system never merges them into fixed pairs.
3. **Spectacle with legible rules.** 3D models, lighting, cameras and impact effects serve spacing, facing, guard and
   hit confirmation.
4. **People behind machines.** Between matches, character scenes show ambition, intimacy, fear, recovery and moral
   conflict. Choices affect relationships and endings without replacing the fights.
5. **A career where damage has a price.** Tournament has money, training, repairs and upgrades, adds localized damage
   with readable repair decisions, and keeps the career persistent. Story and Arcade stay on `classic`.

## 2. Product scope

| Area | Full game target | First playable proof |
| --- | --- | --- |
| Pilots | An original cast of about ten selectable pilots, each with an ending, plus an antagonist. The final count is set after the slice is costed | One story pilot (Ari's route, rewritten); a custom pilot (Tournament) |
| Robots | An original roster of about ten standard robots plus a story boss, each designed from a written brief (`project/robots/_briefs/`). Whether the boss becomes unlockable is open | Two contrasting new robots (the M2 pair) |
| Arenas | About five original arenas, each with one readable hazard | One arena, then one hazard arena |
| Modes | Story, Tournament, Arcade; Training as a support tool; local Versus is a later decision | One story segment and a short Tournament bracket |
| Story presentation | Illustrated or anime-style sequences, voiced or text dialogue, in-engine transitions, pilot endings | Intro, pre-fight exchange, recovery scene, short ending |
| Tournament | Persistent custom pilot, ranking, money, robot ownership, training, parts, localized damage, repairs, sponsors, rival events | One short bracket with region damage, repair choices and a persistent purse |

**Platform target:** desktop Windows first. Linux support is kept where practical through the existing cross-platform
source. Keyboard and gamepad are both primary inputs. The minimum PC profile is fixed at M3 (`DEVPLAN.md`, 3D engine
requirements and R12). Online play and console ports are later scope decisions; neither blocks the first complete game.

## 3. Core player flow

1. Choose a mode.
2. Select a pilot, then a robot. Story may recommend a pairing but does not force it. Tournament uses the player's
   custom pilot and owned robots.
3. See a short opponent introduction, with a skip option.
4. Fight on a fixed side-on plane. Camera, effects and stage geometry add depth without changing left/right inputs.
5. See the result, reward, and a character beat suited to the mode.
6. In Story, choose a response or alliance at selected moments and advance through the story's tournament. In
   Tournament, repair, train, buy and enter the next event.

Every mode uses the same move definitions. The match's ruleset is always shown before the fight. Story has no economy,
upgrades or damage.

## 4. Combat specification

### 4.1 Spatial rules and camera

- Fighters move left/right on one gameplay plane; jumping and crouching keep their usual roles. Visual geometry may
  extend behind the plane.
- The default camera frames both robots and the relevant arena boundary. Dynamic movement may adjust height, zoom and
  lateral framing. It must not cross the fighting axis or reverse attack directions during play.
- Facing changes follow explicit combat rules, not the 3D model's rotation. A crossover test must show predictable
  left/right input behaviour.
- Match intro, victory, finisher and story cinematics may use free cameras only after player control is paused or the
  match is over.

### 4.2 Inputs and mechanics

- Directional movement, **four attack buttons (S1 light punch, S2 strong punch, C1 light kick, C2 strong kick)**,
  standing and low guard, jumping, crouching, a **universal grab on S1 + C1** (escapable in a short window) and each
  mecha's distinctive special inputs. Special commands come in three standard families: Down + S1 + S2 (signature
  technique), down, down-forward, forward + S1 or S2 (offensive special), and down, down-back, back + C1 or C2
  (mobility or control). Effects differ per mecha, commands do not. Buttons are combat functions, not literal limbs: a
  serpent kicks with its tail. Remapping is available for keyboard and gamepad (decided 2026-11-17, see
  `COMBAT_UPGRADE.md` and `GAME_MECHANICS.md`).
- **Mecha attributes:** every mecha has Power, Agility and Resistance on a 1 to 10 scale, 18 points in total at the
  start. They are authored per mecha (not read from the original game's files) and guide design; per-move data wins in
  any conflict. How they feed the health, stun and speed formulas is set in `BALANCE.md`.
- **Special traits:** camouflage, counter, flight, modular weapons and energy shield. None has its own button. **Power
  subtypes** (impact, penetration, cutting, explosive, thermal, electric, electromagnetic, energy, corrosive, kinetic,
  concussive, structural) tag attacks and act through stun and component damage only; thermal is not a heat meter.
- **Stun is the only combat resource.** There is no heat, overclock, rage or desperation meter.
- Separate health and stun, round wins, time limits, knockdowns, air hits, combos and a dramatic finish.
- Destruction finishers are available only in the last round of a match and only when the finishing robot is in good
  condition. In `career` that means no Critical region and the limb used Operational. In `classic` it means every round
  won without losing one, each ended with at least 50% health. Otherwise the match ends with the normal finish. The HUD
  shows availability and the AI obeys the same rule; when the AI destroys the player's robot, the full sequence plays.
- Hits use authored gameplay shapes and timing on the fight plane. Visual limbs may stretch or trail for impact, but
  rendered mesh overlap alone never decides damage.
- Arena hazards are readable and consistent. Their area and timing must be learnable; camera cuts cannot hide the cue.
- AI uses the same move legality and recovery rules as the player. Difficulty adjusts decision quality and reaction
  allowance, not hidden damage bonuses.
- `fightcore` starts on OpenOMF's match tick (28 ms at the default speed, not 60 Hz), so the scaffold comparison stays
  valid, and presentation interpolates to 60 fps. The game's final tick model is recorded at M1, before content
  production (`DEVPLAN.md`, 3D engine requirements).

### 4.3 Combat baseline and tuning

The combat baseline comes from OpenOMF, used as a measuring instrument. Reference matches captured there document
walking speed, jump arc, facing, attack startup and recovery, hit and push distance, block response, stun and special
behaviour for two contrasting robot roles. The first new robots' data starts from those measurements and is then tuned
for this game.

Comparison with OpenOMF is a development tool, not the goal. Every difference from the reference is a recorded decision,
checked in playtest, never an accidental result of new animation. When the scaffold stops being useful, the comparison
mode may be retired by a recorded decision (`DEVPLAN.md`, open decision "Scaffold"), and the measurement suite then
becomes the game's own regression test.

Training mode exposes move lists, input display, hitboxes, stun state, and record/playback for the practice opponent.
Match replays store inputs, game version and ruleset ID, so fights can be reviewed and regressions reproduced.

### 4.4 Opponent AI

AI is central to a single-player fighting game; its complexity must show up as results the player can see.

- **Two layers.** A stable **personality** per opponent (aggression, preferred range, risk tolerance, tactical
  preferences, adaptation speed, willingness to exploit damage), defined independently of difficulty; and **bounded
  adaptation** that tracks a small set of observed habits (jump rate, approach pattern, throw and strike mix, repeated
  punishes, retreats under damage) and reacts only after plausible observation and within reaction limits.
- **No input reading or impossible foreknowledge.** Difficulty comes from decision quality and from punishing
  predictable habits, never from perfect reactions or hidden bonuses.
- **Legible counterplay.** The player can tell what an opponent learned (through behaviour, banter or a post-match
  report, not an analytics screen) and vary tactics to beat it.
- **Story-reactive variants** (fight to win, hesitant, desperate) may reflect relationships without making the AI
  deliberately incompetent.
- **Career memory** (who won, decisive tactics, grudges) affects preparation and commentary; it is separate from
  real-time adaptation.
- **Bosses** may be asymmetric if their patterns and tells are learnable.
- **No machine learning is required.** A learned AI that copies the player is rejected.
- **Verification:** profiles recognizable without dialogue; adaptation beats repetitive habits without cheating;
  players can counter-adapt; every difficulty stays fair. Collect decision traces in test builds, not only win rates.

## 5. Visual, animation and audio direction

### Robots and arenas

- Every robot is a new 3D design made from a written brief (`project/robots/_briefs/`): role, weight class, range and
  movement feel, then its own silhouette, proportions, head and limb shapes, colours, markings and materials. Materials
  add mechanical depth without turning the roster into interchangeable realistic robots.
- A robot may take a **role** from the genre (fast striker, heavy grappler, zoner), never a **look**. Some robots are
  wholly new, so the roster as a whole is not a reskin. Each robot keeps a derivation log
  (`project/robots/<name>/DERIVATION.md`) per the checklist's derivation rule.
- No original sprite, frame or render is traced, painted over or used as a pose reference in final art. The existing
  Jaguar and Shadow modelling references, blockouts and Meshy stand-ins are private placeholders for scaffold work and
  are not a source for production art.
- Animation has a readable anticipation, active strike and recovery. Gameplay timing drives animation; animation never
  secretly changes hit timing or move distance.
- Arenas are original layered 3D spaces, each with one hazard that stays readable at fight-camera distance. Avoid
  clutter directly behind the fighters.
- **Readability in 3D:** strong silhouettes, clear startup tells, and visible damage that never hides collision
  behaviour or a startup tell.
- Effects emphasize impact, stun, electricity, fire and arena danger. Settings reduce flashes, camera shake and visual
  noise.
- The HUD shows pilot and robot names, health, stun, timer, rounds and relevant mode status. Critical fight information
  stays visible during cinematic effects.

### Human characters and anime-style sequences

The human cast has a distinct illustrated style suited to the game's own retro-future setting. Sequences should feel
like sharp character drama, not imports of another series' designs or iconography.

| Sequence type | Use | Production rule |
| --- | --- | --- |
| Character portraits and expression changes | Selection, banter, recovery, Tournament encounters | Reusable pose and expression library for every pilot |
| Short 2D animated scenes | Opening, act turns, major revelations, endings | Reserve full animation for moments that change the story |
| In-engine scenes | Robot launch, arena entrances, victories, boss reveal | Reuse match rigs and arenas; keep them brief and skippable |
| Dialogue panels with motion graphics | Most between-match conversations | Text, subtitles, voice where available, and readable pacing |

The story permits optional romantic tension among adult characters. All characters are presumed bisexual, regardless
of their default relationships. Romance and intimate scenes involve adults only: each romanceable character's age (18
or over) is stated in their character bible, and any minor in the cast has no romance or sexual content. Intimate
moments are skippable and depend on consent.

Audio is fast and energetic, with original compositions or clearly licensed tracks; no reuse or close imitation of the
original game's score. Sound must separate a blocked hit, clean hit, stun, hazard and finisher. Story dialogue can launch
with text and focused voice lines; full voice acting is a budget decision made after the first route is playable.

## 6. Story mode

### Setting and premise

The setting is original and is still to be written (checklist D4, task R23). It needs its own world, organisations,
places, cast and year (the title fixes the year at 2100). A televised robot tournament whose prize matters to
powerful interests is a genre convention and may stay as the frame.

Themes the project developed in its current treatment carry over if the new setting supports them: a pilot link with a
physical cost, a cover-up that protects the tournament's backers, and public spectacle set against private cost. There is
no supernatural or cosmic explanation. Anything that depends on the original game's plot, organisations, places or
characters is dropped, not renamed.

**Existing material.** `project/data/story/ari.story` (Chapters 1 to 6, 266 scenes) and the Story Pack in `lore/` are set
in the original game's world. Ari's route keeps its structure (scene runner, branches, fights, endings) as the template
for the first slice, and its text is rewritten in the new setting. Project-invented characters may stay if they do not
depend on original ones (checklist D3). Each Story Pack file is rewritten, archived or dropped.

### Route structure

The player chooses one of the playable pilots. Each route has an intro, pre-fight rival exchanges, at least one
distinctive mid-route scene, a boss conclusion and a pilot-specific ending. Every pilot has a default path while
unselected; when selected, the player controls their decisions and alliances. No playable pilot is irreplaceable:
critical evidence and finale functions have alternate carriers. Ari is the reference route for the first complete
production pass, not the required lead of every route.

### Choices and consequences

- Between fights, the player chooses whom to approach and whether to challenge, sabotage, spy, share secrets, or pursue
  a consensual romance with an eligible adult. These choices affect relationships and evidence routes.
- Choices alter relationship scenes, information available and epilogue details. They do not skip required fights or
  replace pilot-specific endings with one generic conclusion.
- A romance is never the only route to critical evidence. Optional media allies who are also romance options have
  alternatives if they are absent or opposed.
- The link's toll is shown mainly in narrative scenes. If a player accepts a performance boost with a gameplay cost,
  show both effects and let them decline it. Never degrade basic input response without notice.
- Shared scenes, replayed cutscenes and dialogue can be skipped; a log records key evidence and decisions. Route select
  shows which pilots are complete.

**First complete story slice:** Ari's route rewritten in the new setting, on `classic` (M4). It covers a pre-fight
exchange, match, recovery scene, evidence choice and consequence. A second route follows in Phase 6.

## 7. Tournament mode

Tournament is a separate, replayable career on the `career` ruleset: a custom pilot, earnings, training, robot
purchases, repairs, upgrades and rankings, with fights as the main activity. Story choices do not gate Tournament
progression.

### Career loop

1. Create a pilot and choose starting strengths within a fixed budget.
2. Enter a ranked event or a contract with known prize, arena, opponent class and repair risk.
3. Fight and receive transparent payouts for the result and optional objectives.
4. Spend money on repairs (full repair, standard patch, or fight damaged), insurance, training or legal robot parts;
   compare the projected effect before buying.
5. Build rivalries and sponsorship reputation, advance to tougher brackets, and work toward the top title.

### Localized damage

- Four **components** (arms, legs, torso, head slots; named after each mecha's own anatomy, for example wings,
  thrusters, power core, sensor array), three states each: Operational, Damaged, Critical. "Region" in older text means
  the same thing. Match health and stun work as in `classic`; component condition is a separate layer.
- Effects are numeric and deterministic: weaker punches (arms), slower walk with jumps unchanged (legs), more damage
  taken (torso), longer own stun (head). No move is ever removed. Values are in `DEVPLAN.md`.
- Hits are assigned to regions by hit height (low to legs, mid to torso, high to head and arms), so players can aim for
  a region without a new input. Region state lives in the simulation and is part of replays.
- Damage carries between rounds of a match and between matches until repaired. The pre-match screen shows the
  opponent's region states.

### Persistence and insolvency

- The career is persistent: money, owned robots, upgrades and unrepaired damage carry between events.
- Insolvency ends the career (game over): money still negative after two consecutive matches. Whether an upgrade is
  force-sold first is decided at M3 (`DEVPLAN.md`). Before that point, sponsors and other resources (an advance, a
  contract with conditions, a salvage sale, insurance) offer ways out, and the game warns before any match that could
  end the career.
- A routine loss never ends the career on its own; it can drop the pilot to a lower bracket or a qualifier.

### Economy rules

- Every spend is an opportunity cost, not a flat tax: **repair** (full repair, standard patch, fight damaged),
  **preparation** (legal upgrades and opponent-specific choices) and **risk management** (insurance, salvage). Example:
  with a damaged arm before an aerial opponent, restoring the arm, buying an anti-air option and saving the money should
  each sometimes be rational.
- **Solvency target:** expected winnings per fight minus expected repair and preparation cost is positive for a
  representative player at default difficulty. The economy simulation also measures the loss tail, the chance of
  insolvency after one or two bad fights, and recovery without grinding.
- **No turtling and no recklessness incentive:** bonuses reward varied skill, including precise defence; contract
  objectives are explicit, feasible and optional.
- **Anti-spiral tools:** cheap patches, insurance, salvage sales, sponsor rescues, lower brackets. A failing player never
  also loses the ability to fight competently.

### Sponsors and contracts

- Sponsors are actors with agendas, not multipliers. Offers can include cash, equipment, repair access, intelligence,
  invitations or protection; demands can include a fighting style, testing a part, keeping a secret, throwing a match or
  taking a side.
- **Every questionable offer has a legible refusal path**, even if refusal costs an advantage.
- Consequences cross systems: money, reputation, rival behaviour, access and, where relevant, story evidence.
- No obvious "good" or "evil" bonus: principled choices can be costly in the short term.
- Major offers are authored; small contracts are reusable templates.

### Rivals and reputation

- Named rivals remember important matches, adjust robot and preparation, change sponsors and reference what happened,
  using a small set of state tags and reusable events rather than bespoke writing for every history.
- Reputation tracks how the pilot fights and behaves (sportsmanship, spectacle, ruthlessness, reliability, corporate
  alignment) through a few broad, readable profiles, not many hidden gauges.

### Career principles

- **Clear economy:** show repair estimates, part effects, training limits, event rewards, and how a purchase changes
  the pilot or robot.
- **Build identity:** upgrades create distinct approaches but stay bounded; a well-played base robot can beat an
  upgraded one.
- **Rival continuity:** named pilots remember prior fights, issue challenges and appear in short illustrated scenes,
  without lengthy dialogue between every match.
- **Less grind:** several event types and optional contracts; core ranking progress never needs repeated easy fights.
- **Recovery decisions:** repair, rest or train, or enter the next event at a disclosed disadvantage. No invisible
  injury roll.
- **Save clarity:** autosave after matches and purchases; show the next event and current build on resume.

The first Tournament slice needs one custom pilot, two robots, region damage, a short bracket, prize money, a repair
decision with real trade-offs and one part upgrade (the M3 gate in `DEVPLAN.md`). Rankings arrive at M6. Balance expands
only after this loop is fun over repeated sessions.

## 8. Other modes and usability

- **Arcade:** a quick ladder without the longer story scenes, on `classic` with stacking tune-ups between fights (see
  `ARCADE_MODE.md`).
- **Local Versus (later decision):** two players on keyboard or gamepads with pilot and robot choice, arena choice,
  round and time options, and rematch, on `classic`.
- **Training:** move list, input display, dummy guard and action settings, hitbox and stun view, saveable practice setup.
- **Options:** remappable input, text size, subtitles, dialogue log, colour differentiation beyond hue, reduced flashes
  and shake, scalable graphics, audio sliders, skippable scenes.
- **Accessibility (proposed 2026-11-09, decide by M4):**
  - Optional assist inputs per profile, such as one-button specials. They change how a move is entered, never its
    timing, damage or rules.
  - A **Story difficulty** that softens execution (AI decision quality and reaction allowance) without changing the
    ruleset.
  - Readable damage and stun indicators that do not rely on flashing or colour alone.
  - No reflex quick-time events; normal defeats never need one.
  - Assists never alter `classic` or `career` numbers. Whether assists are allowed in Tournament is open.
- **Onboarding:** a short optional tutorial teaches movement, guard, stun, one special and arena hazards, using an actual
  robot rather than a detached mini-game.

## 9. Production architecture

### The scaffold

The project is built on a fork of OpenOMF (C11, CMake, SDL2, OpenGL 3; MIT licence). OpenOMF is the **development
scaffold**: its rules run the prototype's fights today and give a measurable combat baseline, and its code may be reused
with its notice kept. The game does not depend on it permanently and may discard it.

The current `project/prototype` is a standalone SDL2/OpenGL side-on build that renders 3D placeholder robots and plays
the Ari story route and Arcade (`DEVPLAN.md`, current state). Its own combat loop is a `--sandbox`-only placeholder;
real fights run on OpenOMF's rules until `fightcore` replaces them. While it runs on the scaffold it reads the original
game's data, so it is dev-only.

### Implementation path

1. Keep the scaffold runnable as a dev-only reference while it is useful, and capture baseline data from it (done for
   two robot roles).
2. (Done, gate closed 2026-10-27.) A side-on 3D match spike on the current C/SDL/OpenGL stack, with combat state
   separated from pose and camera state and both fed from the same fixed-tick events.
3. Lift the rules into `fightcore`, a standalone library that reads a project-made data pack. Release builds read no
   original data and launch no OpenOMF process.
4. Renderer decision at M1 (Spike C): keep the C renderer, or move only the presentation layer to a dedicated 3D
   toolchain. Combat data and story scripts stay portable so this decision does not erase earlier work.
5. Author story dialogue, branching flags, portraits and cutscene cues as data. Add versioned saves and content
   validation before writing more routes.
6. Retire the scaffold, if and when chosen: once `fightcore` and the data pack cover everything the game uses, the
   comparison mode and unused upstream code may be dropped by a recorded decision. Any code that stays keeps the MIT
   notice in NOTICES.

**Subsystem boundary:** simulation owns inputs, state, collisions, damage, stun, hazards, AI and results; presentation
reads events and poses; narrative owns route state and between-match choices; Tournament owns the career economy.
Presentation is never the authority for whether a hit landed, so a replay reproduces the same outcome with lower
graphics.

## 10. Validation and acceptance criteria

| Gate | Pass condition |
| --- | --- |
| Robot identity | Players who have not seen the robots tell them apart and name each one's role in an unlabelled match clip and a short hands-on test. In a side-by-side silhouette check, no robot reads as a machine from another game. |
| Combat baseline | The M2 duel's timing and spacing are measured against the OpenOMF reference; every difference is recorded as a decision and playtested. After the scaffold is retired, the measurements are the regression baseline. |
| Camera and input | Camera motion never makes a directional attack or guard ambiguous; fighters keep a readable silhouette at normal speed. |
| Story slice | Ari's route in the new setting plays start to finish, offers a clear evidence choice, records it, and shows a consequence after the match. |
| Tournament slice | A custom pilot finishes a bracket, earns money, makes repair choices under region damage, upgrades a robot, and sees changed performance after loading a save. Playtesters choose different repairs for the same situation and do not play passively. |
| Performance | The worst-case match (both robots Critical in several regions, maximum effects) holds 60 fps in both looks on the minimum PC (budgets in `DEVPLAN.md`). |
| Content pipeline | A new dialogue scene, model, animation and arena hazard can be added without changing combat code. |
| Accessibility | Every story scene has readable text and skip and log support; flashes and camera shake can be reduced. |
| Release readiness | All intended pilots, robots, arenas, routes and modes pass content review; every asset has documented distribution rights; the final scan finds no name, character, design, text or file from *One Must Fall 2097* or *Battlegrounds* (checklist, "Done when"). |

Target smooth 60 fps match presentation on the eventual minimum PC profile. Set a concrete GPU and CPU profile after the
first representative robot, arena, effects and HUD run together. Test controller latency and frame pacing on hardware,
not only in a headless check.

## 11. Delivery phases

`DEVPLAN.md` uses Phases 0 to 7 and milestones M0 to M7 and holds the dates. The letters below are the older phases,
kept so earlier notes still resolve.

| Phase | Deliverable | Status or milestone |
| --- | --- | --- |
| A. Baseline | Scaffold match captures, move data, rights inventory | Done |
| B. 3D fidelity spike | Two placeholder robots, one arena, fixed plane, camera, one complete move set | Done (2026-10-27) |
| C. Vertical slice | Two new robots, second arena with a hazard, polished match, Ari's route in the new setting | M4 (after the M2 duel and M3 career core) |
| D. Systems alpha | Roster in progress, Tournament economy, saves, UI, art pipeline | M5 to M6 |
| E. Content production | Full pilot cast, robot roster, arenas, routes, anime sequences, Tournament events | M5 to M6 |
| F. Release candidate | Performance, accessibility, balance, packaging, regression and rights checks | M7 |

The two visual looks are **blockout** (flat, readable, shipped as a finished look) and **mesh** (full models); both must
pass `har_check`. See `DEVPLAN.md`.

## 12. Rights and source boundary

- **Independent game.** No distributed build contains a title, name, character, robot design, setting, story, text,
  art, music or sound from *One Must Fall 2097*, *One Must Fall: Battlegrounds* or their owners.
- **Mechanics are kept.** Move structure, timing and stats are rules, not expression. The baseline measured through
  OpenOMF is re-authored as the project's own data pack (`RIGHTS.md` rule 4, checklist D6); no original number tables or
  text ship.
- **Code.** OpenOMF is MIT licensed; reused code keeps its notice in a NOTICES file shipped with every build, alongside
  the vendored and linked libraries' notices.
- **Placeholders.** The local `OMF2097/` data and the original robots, pilots, sounds and music are private development
  placeholders. They never appear in a distributed build, public screenshot or trailer, and they are gone from every
  build by M5.
- **Credit.** "Built on OpenOMF" (required for reused code) and "inspired by *One Must Fall 2097* by Diversions
  Entertainment; not affiliated with or endorsed by its owners" (wording in checklist D7). Credit is courtesy, not
  permission.
- **Provenance.** Every final asset and text passage has a row in [ASSET_LEDGER.md](ASSET_LEDGER.md). Replace anything
  whose rights are unclear.
- **Patents.** Concerns about fighting-game mechanics are unverified; get legal advice before shipping a system closely
  resembling a known patented one.
- **Anime influence** is expressed through pacing, acting and framing, with original designs and scenes.

## 13. Open decisions

These do not block the current work:

- Title clearance (checklist D1; the code name is `ML2100`); whether "mecha" stays the final term once the setting is written (D2).
- Setting, in-fiction organisations and cast; the year is 2100 (checklist D4, R23).
- Whether and when to retire the OpenOMF scaffold (`DEVPLAN.md`, open decision "Scaffold").
- Whether the story boss becomes unlockable.
- Whether all story routes receive voice acting or only key scenes.
- Final minimum hardware profile (fixed at M3) and whether Linux ships on the same day.
- Whether local Versus ships, and whether online play follows it.
- Sponsor safety net and upgrade model (decided at M3, see `DEVPLAN.md`). Damage carry-over between rounds and matches
  was decided on 2026-11-09.

## Source notes

- [Local OpenOMF build instructions](../../BUILD.md), [CMake configuration](../../CMakeLists.txt).
- [Existing 3D prototype notes](../prototype/README.md) and [development plan](DEVPLAN.md).
- [Rebrand checklist](REBRAND_CHECKLIST.md) (derivation rule, placeholders, decisions D1 to D7) and [rights research](RIGHTS.md).
