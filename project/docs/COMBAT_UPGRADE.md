# Combat upgrade: four buttons, components, attributes and traits

Status: proposal, 2026-11-17. Input: an external robot-fighting design document (v0.7, written outside the project). This file records which parts were adopted into the current combat design and which were not. It changes nothing in `GAME_SPEC.md`, `CONTROLS.md` or `DEVPLAN.md` until those are updated (see "Follow-up edits").

Robot names, anatomies and the "mecha" term are working titles. The external names (Juggernaut, Phantom and the rest) were not collision-checked and are not adopted. See `REBRAND_CHECKLIST.md` D2 and `RIGHTS.md`.

## Decisions

| Topic | Decision |
|---|---|
| Health and match format | **Unchanged.** Keep the current model: health from the OpenOMF formulas in `BALANCE.md`, separate stun, rounds, time limits. The external 1000 HP, continuous fight and no-timer format is not adopted. |
| Buttons | **Four attack buttons:** two punches (S1 light, S2 strong) and two kicks (C1 light, C2 strong). Replaces the single punch and kick. |
| Grab | **Universal S1 + C1**, close range, with an escape input in the right window. Replaces the punch-based throw. |
| Damage regions | **Keep the four regions** (arms, legs, torso, head) and their three states (Operational, Damaged, Critical). Rename them **components** in design and UI text. |
| Robot attributes | **Power, Agility, Resistance**, 1 to 10, 18 points per robot. Per-robot data, no longer inherited from the original AF files. |
| Specials | **Adopt** the five special traits, the twelve power subtypes and the three special-command families. |

## 1. Buttons and inputs

- Attack buttons: S1 light punch (fast), S2 strong punch (powerful), C1 light kick (fast, alternate trajectory), C2 strong kick (wide or long reach).
- Each button has standing, crouching and airborne versions. Directional variants can be added later.
- Directions are relative to the opponent. Back guards, down and back guards low. Jump, crouch and diagonal variants stay as in `CONTROLS.md`.
- Controls describe combat functions, not literal limbs. A serpentine robot kicks with its tail and a drone punches with a ram. Every robot has all four buttons.
- Grab: S1 + C1 within close range. Each anatomy gets its own animation. Defended by an escape input in a short window. Special robots may add extra grabs.
- Special-command families (standardised, effects differ per robot):

| Command | Family |
|---|---|
| Down + S1 + S2 | Signature ability or exclusive technique |
| Down, down-forward, forward + S1 or S2 | Offensive special |
| Down, down-back, back + C1 or C2 | Mobility or control special |

Effect on the repo:
- `CONTROLS.md` defaults (J punch, K kick, gamepad A and B) need two more buttons, one extra pair per player in the OpenOMF settings, and the shared-memory input path in `game_state.c`.
- Existing move-input data (`project/data/move_names.csv`, Shadow Punch QCB+P, Grab D+D+P) belongs to placeholder robots and is replaced by the new command families when each robot is authored.
- Combos stay short: 2 to 4 hits common, 5 to 7 exceptional, with falling damage in long combos and a cap on structural damage accumulated in one combo. The external 8 to 18% and 25 to 30% damage figures are starting values to test against the current health formulas, not rules.

## 2. Components (the existing four regions)

The structure in `GAME_SPEC.md` (Localized damage) is kept: four regions, three states, hit-height assignment, numeric effects, no move removed, damage persists until repaired in `career`.

What changes is the naming and the anatomy mapping:
- Each robot names its four slots after its own anatomy, so the damage layer reads as machine parts. The slot still maps to the same effect.

| Slot | Effect when Damaged or Critical | Example names by anatomy |
|---|---|---|
| Arms | Weaker punches | Manipulator, wings, ram, blade arm |
| Legs | Slower walk, jumps unchanged | Hind legs, thrusters, tail, articulations |
| Torso | More damage taken | Armour core, power plant, shield generator |
| Head | Longer own stun | Sensor array, optical emitters, cannon |

- The external 3 to 5 component count is not adopted. Four slots keep one effect table for all robots (the values live in `DEVPLAN.md`).
- Exposure windows and local armour from the external design are folded into the slot: an armoured slot takes less damage before it changes state. They are per-robot tuning, not new rules.
- Incapacitation stays rare. The external targets are checked in simulation: dangerous component damage in 20 to 40% of fights, at least one Critical slot in under 10%, none in over 60%. These apply to `classic` and the first `career` fights. The `career` layer deliberately raises them over a season, so measure on a fresh robot.

## 3. Attributes

- Three attributes per robot, 1 to 10: Power (damage and impact), Agility (speed, mobility, repositioning), Resistance (damage absorbed and stability).
- Budget: 18 points per robot, as a starting constraint.
- Attributes guide design. They do not replace per-move data (reach, startup, recovery, damage, guard). Move properties win in any conflict.
- Pilot stats (`main.c`, `story.c`, about 30 points each) are a separate layer and stay as they are. Open: how a robot attribute (1 to 10) maps onto the health, stun and speed formulas of `BALANCE.md`, and how pilot stats combine with it. Decide before the first new robot is balanced.

## 4. Special traits

Five traits, none with its own button:

| Trait | Function | Design guard |
|---|---|---|
| Camouflage | Harder to read or anticipate | Must not reduce the opponent's ability to react below a fair level (risk 4 below). |
| Counter | Rewards a well-timed defence or reply | Must cost the robot a commit, not be free. |
| Flight | Limited extra aerial mobility | No indefinite evasion. Every robot keeps an anti-air tool. |
| Modular weapons | Swap weapons and offensive styles | `DEVPLAN.md` #20 (modular parts) is deferred. This trait stays a fixed per-robot move set until that is decided. |
| Energy shield | Extra active protection | Must be able to break or be bypassed. |

Each trait needs a mechanical and a visual justification.

## 5. Power subtypes

Twelve subtypes, combinable in one attack: Impact, Penetration, Cutting, Explosive, Thermal, Electric, Electromagnetic, Energy, Corrosive, Kinetic, Concussive, Structural.

They feed hit effects on the existing systems only:
- Concussive and Electric act through **stun**. Structural and Penetration act through **component damage**. Impact adds pressure on guards.
- Indirect effects (explosions, heat, interference, corrosion) never skip armour or guard by themselves.
- **Conflict with `DEVPLAN.md:88`:** heat and overclock are on the rejected list. Thermal therefore stays a damage and stun flavour. It does not become a heat meter, and the doc's "overheating" is not adopted as a resource.
- There is no super meter and no special-energy bar, which matches `GAME_SPEC.md` (stun is the only resource).

Subtype effects beyond damage and stun (shield interference, sensor disruption, progressive corrosion) are optional and each needs its own task before it ships.

## 6. Design rules for new robots

Adopted as written in the external document:
1. Fragility needs compensation: exposed weak parts require agility, a shield, camouflage, retractable plates or a controlled exposure window.
2. The look states the function: heavy, fast, tough, stealthy or specialised at a glance.
3. Every major structure has a mechanical reason: wings, claws, tails, pincers, thrusters and extra arms must do what they look like.
4. Silhouettes differ and read without colour or texture.
5. Each robot has clear strengths and weaknesses.
6. No unanswerable strategies: low robots are not immune to whole attack classes, flyers cannot stay out of reach forever, heavy robots can pressure fast ones, light robots are not removed by one common mistake.
7. Losing does not mean destruction. Robots are built to survive many fights and are maintained between them. This fits the `career` repair loop.

Known risks to test: air robots dominating slow ones, very tough robots making long fights, grabs too strong against guards, camouflage cutting reaction time, snowballing component damage, small or low bodies winning on collision, combos aimed at one component.

Balance goals from the document: matchups near 45 to 55%, tolerance 35 to 65%, every robot with a defence, low attacks and anti-air. Measure only after implementation, with players of equal skill.

## 7. Roster candidates

The external roster is a pool of archetypes for the open roster decision (`DEVPLAN.md:370`, about ten mechas plus a boss). Names below are descriptive labels, not names to use.

| Archetype | Anatomy | P / A / R | Traits | Subtypes |
|---|---|---|---|---|
| Heavy tank | Armoured quadruped | 7 / 2 / 9 | Shield | Impact, Concussive |
| Stealth assassin | Stealth humanoid | 8 / 8 / 2 | Camouflage | Cutting, Penetration |
| Aerial bird | Mechanical bird | 5 / 9 / 4 | Flight | Energy, Kinetic |
| Defensive fortress | Hexapod | 4 / 4 / 10 | Shield, Counter | Impact, Electric |
| Industrial brawler | Industrial humanoid | 9 / 5 / 4 | None | Thermal, Explosive |
| Disc drone | Discoid drone | 5 / 10 / 3 | Camouflage, Flight | Electromagnetic, Electric |
| Colossus | Colossal humanoid | 10 / 2 / 6 | None | Impact, Structural, Concussive |
| Adaptive quadruped | Modular quadruped | 6 / 6 / 6 | Modular weapons | Cutting, Kinetic, Energy |
| Serpent | Serpentine | 7 / 7 / 4 | Camouflage | Corrosive, Penetration |
| Technical defender | Defensive humanoid | 3 / 6 / 9 | Shield, Counter | Concussive, Electric |
| Predator | Animal biped | 7 / 9 / 2 | Counter | Cutting, Kinetic |
| Air bomber | Aerial platform | 8 / 7 / 3 | Flight | Explosive, Energy, Thermal |
| Spider | Arachnid | 5 / 7 / 6 | Modular weapons | Electromagnetic, Electric, Concussive |
| Four-arm gladiator | Four-armed humanoid | 9 / 3 / 6 | Counter | Impact, Structural |
| Versatile elite | Advanced humanoid | 6 / 7 / 5 | Modular weapons, Shield | Penetration, Energy, Corrosive |

Notes:
- All rows sum to 18. Three of these (tank, assassin, bird) are the external document's first prototype set. Panthera and Shade (`project/robots/_briefs/`) are the in-repo briefs replacing Jaguar and Shadow, and should be compared with the closest archetypes here (heavy, stealth) before more art is made.
- The 15 count is not committed. The decided scope is about ten plus a boss, with new robots in batches from M2 (`DEVPLAN.md:347-353`).
- Four-armed and multi-limb robots share one punch and kick layout with the rest. Their extra limbs change animation and grabs, not the button count.

## Follow-up edits (done 2026-11-17)

1. `GAME_SPEC.md`: §4.2 inputs, attributes, traits and subtypes; Localized damage uses "components".
2. `CONTROLS.md`: new decided scheme and the required work (code still has one punch and one kick).
3. `FEATURES.md` and `DEVPLAN.md`: decision row, tasks R24 to R27, open decisions (attribute mapping, four-button engine cost, trait order), the #7 and #20 checks and a changelog entry.
4. `BALANCE.md`: proposed attribute mapping, targets, risks and a log entry.
5. `REBRAND_CHECKLIST.md` D2: archetypes as the starting pool, names not adopted.
6. `docs/README.md`: index entries.
7. `GAME_MECHANICS.md`: the shared document for the external design team; it supersedes the external v0.7 file.

## Open questions

- Engine cost of four buttons: OpenOMF reads one punch and one kick per player and its AF move data assumes that. How much of the move system must be re-authored for new robots, and does the prototype keep the old scheme until M2?
- Attribute mapping (1 to 10, 18 points) onto health, stun, speed and damage, and how pilot stats combine with it.
- Whether S1/C1 light and S2/C2 strong map to existing weak and strong tiers or need new move data.
- Whether Flight and Camouflage ship in the first slice or wait for a later batch.
