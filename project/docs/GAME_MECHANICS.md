# Mecha Link 2100: game mechanics for the robot design team

Version 0.9, 2026-11-17 (v0.8 plus section 13: geometry, arenas, 17 candidates). Replaces the external "Robot Fighting Game: Game Design Document" v0.7, which is kept only as a source. This document is shared with the external robot design team and is developed jointly. Sections marked **Fixed** come from the project's combat rules and need project agreement to change. Sections marked **Open** are for the design team to propose.

Terms: robots are called **mechas** (working term). Names of mechas, including the 15 working names in v0.7, are placeholders until they pass a name clearance (section 9).

## 1. What changed from v0.7

| Topic | v0.7 | v0.8 |
|---|---|---|
| Health and match format | 1000 HP, one continuous fight, no rounds, no timer | **Not adopted.** Health, a separate stun value, rounds and a time limit, as in the project's `classic` rules. |
| Attack buttons | S1, S2, C1, C2 | Kept. |
| Grab | S1 + C1 | Kept. |
| Component damage | 3 to 5 components per robot | **Four components per mecha**, three states each (see section 4). |
| Attributes | Power, Agility, Resistance, 1 to 10, 18 points | Kept. |
| Special traits, power subtypes, special commands | As listed | Kept, with the limits in sections 5 to 7. |
| Roster | 15 robots | 15 archetypes as a candidate pool. The release roster is about ten mechas plus a story boss. |
| Super meter, special energy | None | Same. Stun is the only combat resource. |

## 2. Overview (Fixed)

- Side-on 2D fighting plane, one against one. The game is 3D-rendered but plays on a fixed plane.
- A match is a series of rounds. Each mecha has **health** and a separate **stun** value. A mecha loses a round when its health reaches zero. There are time limits, knockdowns, air hits, combos and a dramatic finish.
- **Stun is the only combat resource.** There is no super meter, heat meter, rage or desperation mechanic, and none is planned. Any mechanic that behaves like one of these is out of scope.
- Two rulesets use the same moves: `classic` (Story, Arcade) and `career` (Tournament, which adds component damage that carries between rounds and matches until repaired).

Design goals (kept from v0.7):
1. Simple, universal, consistent controls.
2. Visually distinct mechas with their own styles.
3. Medium-pace combat: positioning, moderate combos and powerful attacks.
4. Functional anatomies that make mechanical sense.
5. Component damage with real consequences, but rare incapacitation.
6. Competitive balance without erasing the differences between models.
7. Robots tough enough for many fights, repaired between them.

## 3. Attributes (Fixed scale, Open values)

Every mecha has three numbers on a 1 to 10 scale, **18 points in total** at the start:

- **Power:** damage and impact of attacks.
- **Agility:** speed, mobility, repositioning.
- **Resistance:** damage absorbed and stability under hits.

Attributes guide design. They do not replace per-move data (reach, startup, recovery, damage, guard); move data wins in any conflict. The conversion of attributes into the game's health, stun, damage and speed numbers is a project task and is not final.

## 4. Components (Fixed structure, Open names and values)

Each mecha has **four components** that map onto four fixed slots. Each component has three states: **Operational**, **Damaged**, **Critical**.

| Slot | Effect when Damaged, stronger when Critical | The design team names the part |
|---|---|---|
| Arms | Weaker punches | Manipulator, wings, ram, blade arm, ... |
| Legs | Slower walking, jumping unchanged | Hind legs, thrusters, tail, ... |
| Torso | More damage taken | Armour core, power plant, shield generator, ... |
| Head | Own stun lasts longer | Sensor array, optical emitters, cannon, ... |

Rules:
- **No move is ever removed.** A Critical component weakens a mecha, it never disables a button.
- Hits are assigned to slots by hit height: low to legs, mid to torso, high to head and arms. The design team can propose which slot a given attack or body part feeds, within this rule.
- Damage persists until repaired in `career`. Temporary effects (stuns, electronic faults) end during the fight without repairing damage.
- Armour and exposure are per-mecha tuning: an armoured component takes more hits before it changes state; an exposed one less. They are not new rules.
- Targets, measured later: component damage in 20 to 40% of `career` fights, at least one Critical component in under 10%, none in over 60%; several Criticals in one fight are exceptional.
- Losing a fight does not mean destruction. Mechas are built to survive many fights.

## 5. Special traits (Fixed list, Open per-mecha use)

Five traits. None has its own button.

| Trait | Function | Rule |
|---|---|---|
| Camouflage | Harder to read or anticipate | Must not cut the opponent's reaction below a fair level. |
| Counter | Rewards a well-timed defence or reply | Must cost a commitment, not be a free comeback. |
| Flight | Limited extra aerial mobility | No indefinite evasion. Every mecha keeps an anti-air tool. |
| Modular weapons | Alternate weapons and styles | For now a fixed per-mecha move set, not live-swappable parts. |
| Energy shield | Extra active protection | Must be breakable or bypassable. |

Each trait needs a mechanical and a visual justification, and a visible signal that tells the opponent it is active.

## 6. Power subtypes (Fixed list, Open per-attack use)

Twelve subtypes that can combine in one attack: Impact, Penetration, Cutting, Explosive, Thermal, Electric, Electromagnetic, Energy, Corrosive, Kinetic, Concussive, Structural.

They act only through the existing systems:
- Concussive and Electric act through **stun**. Structural, Penetration and Cutting act through **component damage**. Impact adds pressure on guards.
- Indirect effects (explosions, heat, interference, corrosion) never skip armour or guard automatically.
- **Thermal is a flavour of damage and stun, not a heat meter.** Overheating that builds into a resource or a penalty bar is out of scope.
- Effects beyond damage and stun (shield interference, sensor disruption, progressive corrosion) are optional proposals; each needs its own approval before it ships.

## 7. Controls (Fixed)

Directions are relative to the opponent.

| Input | Function |
|---|---|
| Forward / back | Advance / retreat. Back guards. |
| Up / down | Jump or rise / crouch. Down + back guards low. |
| S1 | Light punch: fast attack |
| S2 | Strong punch: powerful attack |
| C1 | Light kick: fast attack, alternate trajectory |
| C2 | Strong kick: wide or long-reach attack |
| S1 + C1 | Grab: close range, animation per anatomy, escapable with an escape input in a short window |

Each attack button has standing, crouching and airborne versions. Directional variants may be added later.

Special commands (same commands for every mecha, effects differ):

| Command | Family |
|---|---|
| Down + S1 + S2 | Signature ability or exclusive technique |
| Down, down-forward, forward + S1 or S2 | Offensive special |
| Down, down-back, back + C1 or C2 | Mobility or control |

Buttons are **combat functions, not limbs**. A serpentine mecha kicks with its tail; a drone punches with a ram. Every mecha has all four buttons and all three special families, regardless of anatomy.

Combos are short: 2 to 4 hits common, 5 to 7 exceptional, with falling damage in long combos and a cap on structural damage per combo. Damage figures are hypotheses to test, not rules: common combos about 8 to 18% of health, exceptional ones at most about 25 to 30%.

## 8. Design rules for mechas (Fixed)

1. **Fragility needs compensation.** An exposed weak part needs agility, a shield, camouflage, retractable plates or a controlled exposure window.
2. **The look states the function.** Heavy, fast, tough, stealthy or specialised should read at a glance.
3. **Every major structure has a mechanical reason.** Wings, claws, tails, pincers, thrusters and extra arms must do what they look like.
4. **Silhouettes differ**, and read without colour or texture.
5. **Clear strengths and weaknesses.** Not every mecha is good in every situation.
6. **No unanswerable strategies.** Low mechas are not immune to whole attack classes; flyers cannot stay out of reach forever; heavy mechas can pressure fast ones; light mechas are not removed by one common mistake.
7. **Controls do not depend on anatomy** (section 7).
8. **Weak points are readable.** Damaged components show visible signs.
9. **Every mecha has a guard, low attacks and an anti-air tool.**

Known risks to test: air mechas dominating slow ones, very tough mechas causing long fights, grabs too strong against guards, camouflage cutting reaction time, snowballing component damage, small or low bodies winning on collision, combos aimed at one component. Balance goal, measured only after implementation with players of equal skill: matchups near 45 to 55%, tolerated 35 to 65%.

## 9. Originality and rights (Fixed, applies to every deliverable)

The game is independent. Nothing may resemble or derive from the robots, characters, names or art of *One Must Fall 2097*.
- Work from written briefs and your own references. Do not trace or use original sprites, renders or frames, and do not use that game's robot names.
- Change the silhouette, not only the surface; a recolour or "Mk2" version does not count.
- The 15 working names in v0.7 are generic and not cleared. Treat them as labels. Any proposed final name needs a similarity search (games, trademarks, app stores) before adoption.
- Keep a short note per mecha: which archetype or reference it echoes, what is new, who drew it.

## 10. Archetypes (Open: the candidate pool)

The release roster is about ten mechas plus a story boss, and the design team is asked to propose which archetypes to build and which to merge or drop. All rows total 18 points.

**v0.9 update:** the team's design guide (v1.5) lists **17 candidates**. It replaces the disc drone with a hovering manta and the air bomber with a flying reptilian striker (their inherited attributes need reassessment) and adds three non-humanoid candidates: a non-biomimetic tripod, a mantis-inspired machine and a single-wheel combat robot (attributes and traits to be defined). The table below is the original 15-row pool; use the guide for the 17 and its working names, which are uncleared (section 9).

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

v0.7 proposed the heavy tank, stealth assassin and aerial bird as the first three prototypes. In the project, two original briefs already exist for a heavy and a stealth role; the first two mechas to be built will be chosen from this pool together with the team.

Four-armed and multi-limb mechas share the four-button layout. Extra limbs change animation and grabs, not the number of buttons.

## 11. Mecha template (Open: please fill one per archetype)

For each mecha the design team supplies:
1. Working name and role in one sentence; anatomy; weight class.
2. Attributes P / A / R (18 points) and why.
3. Traits and power subtypes, each with its visual signal and its counterplay.
4. The four components: the part named for each slot, its armour and exposure, and what Damaged and Critical look like.
5. Moves: S1, S2, C1, C2 in standing, crouching and airborne versions (12 normal moves), the grab, and one move for each of the three special families. For every move: reach class, speed class (fast, medium, slow), height (low, mid, high), purpose, subtypes.
6. Strategy, vulnerability, and the answer to each of the risks in section 8.
7. Silhouette sketch or reference sheet, front and side, with the originality note (section 9).

## 12. Questions for the design team (Open)

1. Which archetypes to build for a roster of about ten plus a boss, and what is the boss: a fixed unusual mecha with its own explicit, learnable rules?
2. Per archetype, a proposed answer to the unanswerable-strategy rule: what stops the flyers, what gets past the shields, what catches the fast ones.
3. Which traits belong in the first two mechas and which should wait. Flight and camouflage are the hardest to make fair.
4. Whether the three special families give enough room for the archetype with the most distinct identity (for example the modular and four-arm ones).
5. How strong the grab should be against guards, and the escape window, so grabs are not oppressive against defenders.
6. How a mecha's Damaged and Critical states should look for each of the four slots, readable at fight-camera distance.
7. Whether 18 points is enough room to separate fast, tough and heavy builds.

## 13. Geometry, arenas and environment (v0.9, from the team's documents)

**Geometry (accepted in principle, to be prototyped).**
- Play is on the X-Y plane. Each mecha has solid bodies (pushboxes) that may leave out wings, tails and arms so appendages never block movement permanently; hurtboxes that follow the anatomy and map to the four components; hitboxes active only during a move's active frames, each with shape, timing, class and component.
- Attack classes (low, mid, high) are functional, not literal contact height. Every anatomy has low and high attacks, a guard and an anti-air answer.
- No mecha is permanently unreachable because of size, shape or rest position (the 20 cm levitation does not make a mecha immune to low attacks).
- Mixed sizes are allowed. Long reach is balanced with speed, recovery, mobility, exposure and counterplay. The 2 to 8 m range is exploratory, not an approval limit.
- The universal grab works at any size difference. A small mecha need not lift a large one; the animation changes, the rules do not.
- Appendages that add reach need matching limits or vulnerabilities.
- First test bodies: small agile, wide low, tall long-reach; then serpent, bird and disc or manta. Eight geometry tests (approach and collision, low attacks, high attacks and guards, grabs, anti-air, throws and descents, arena edges, no permanent overlap or block) are repeated in each gravity.

**Arenas and gravity (proposed, not decided).** Earth (1 g), Mars (about 0.378 g) and Moon (about 0.165 g), one command set. A descent module gives a minimum fall acceleration of 0.7 g so low-gravity jumps stay readable. Flight is capped at the height of a standard jump (2 m is a proposal, the arena length 30 m too). Low levitation is up to 0.20 m.

**Rules the project cannot accept as written (needs your input).** The regulation's **2 s flight budget** and **shared pool of 6 projectile charges** act as limited resources, while the project's rule is that stun is the only resource. Proposed fix: express both as per-move recovery and cooldowns, with no pool and no HUD counter. If the team needs a pool, bring the case and the project will decide. Banned in the regulation and kept: energy beams, grenades, warheads and impact, proximity or command detonation; secondary explosions from damage are allowed. Rule enforcement should be deterministic (an illegal design fails validation) rather than penalties in play.

**Other open points the team is asked to settle:** how the descent rule affects hitstun, throws, air combos and knockdowns; the physical reference point for measuring flight height; oblique and combined propulsion; simultaneous shots; the "Shield" and "Energy Shield" naming; whether Explosive attacks are consistent with the banned-explosives list (Forge Ape and the pterosaur carry that subtype); and the regulation's count (still 15 candidates, still lists the replaced drone and bomber).

## 14. Project status, for context

Concept stage for the new mechas. The design guide (English) is kept as `MECHA_DESIGN_GUIDE_V1.5.txt`; the other two team documents (Portuguese) are not kept. All three are summarised here. The combat prototype still uses one punch and one kick; the four-button input, grab and per-mecha attributes are decided and are scheduled with the first new mechas. Nothing here is balanced yet: every number is a starting hypothesis.

Project documents (`COMBAT_UPGRADE.md`, `GAME_SPEC.md`, `DEVPLAN.md`, `BALANCE.md`, `CONTROLS.md`) hold the project-side detail. When this document and a project document disagree, the project document wins until the project agrees a change.
