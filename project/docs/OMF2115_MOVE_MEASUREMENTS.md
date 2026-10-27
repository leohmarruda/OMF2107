# Jaguar and Shadow move measurements — 2026-10-27

Isolated range, timing, damage, and guard checks for every selectable Jaguar and
Shadow ground and air attack, measured on OpenOMF with the original AF data. They
complete the "isolated range and guard/stun checks" item of the
[roadmap](ROADMAP.md#immediate-next-work). Nothing here changes gameplay; the 3D
view only renders what OpenOMF reports.

## Method

`project/tools/measure_moves.py` edits a *copy* of `rectests/6P.REC` (Crystal/Jaguar
vs Shirro/Shadow, Stadium) with `rectool`: it sets the fighters' starting X positions,
adds the attacker's inputs taken from the AF move string, and optionally makes the
defender hold standing or low guard. The trace build of OpenOMF replays each fixture
headlessly at speed 10; every number below is read from the per-tick trace. Run
`python project/tools/measure_moves.py [--har jaguar|shadow] [--move ID]` from the
repository root; outputs go to the ignored `build/omf_trace_z7/moves/`.

## Results

| HAR | Move | Input | Name | Anim ticks | Startup | Damage | Max hit gap | Hit reaction | Adv. on hit | High guard (adv.) | Low guard (adv.) |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | --- | --- |
| jaguar | 42 | `P` | standing punch | 8 | 2 | 7 | 88.0 | recoil>standing | 1 | block (–) | block (3) |
| jaguar | 41 | `K` | standing kick | 15 | 3 | 19 | 102.0 | recoil>standing | -2 | block (–) | block (0) |
| jaguar | 23 | `P3` | down-forward punch | 6 | 1 | 7 | 100.0 | recoil>standing | 2 | block (–) | block (4) |
| jaguar | 30 | `P2` | down punch | 14 | 3 | 19 | 106.0 | recoil>standing | -1 | block (–) | block (1) |
| jaguar | 32 | `P1` | down-back punch | 26 | 4 | 30 | 83.0 | recoil>standing-up>standing | 30 | block (–) | block (-9) |
| jaguar | 27 | `P4` | back punch | 14 | 3 | 19 | 94.6 | recoil>standing | -1 | block (–) | miss (–) |
| jaguar | 18 | `K3` | down-forward kick | 7 | 1 | 9 | 100.0 | recoil>standing | 1 | hit (–) | block (3) |
| jaguar | 19 | `K2` | down kick | 14 | 2 | 19 | 85.0 | recoil>standing | -2 | hit (–) | block (0) |
| jaguar | 33 | `K1` | down-back kick | 24 | 5 | 27 | 107.0 | recoil>standing-up>standing | 33 | hit (–) | block (-6) |
| jaguar | 24 | `K4` | back kick | 18 | 1 | 30 | 89.6 | recoil>standing | -5 | block (–) | block (-3) |
| jaguar | 20 | `P6` | close throw | 23 | 19 | 38 | 38.0 | recoil>standing-up>standing | 49 | hit (–) | hit (49) |
| jaguar | 17 | `P63` | leap (grounded P63) | 21 | 1 | 19 | 151.0 | recoil>standing-up>standing | 13 | block (–) | block (-7) |
| jaguar | 16 | `P6321` | overhead throw special (P6321) | 26 | 1 | 19 | 176.0 | recoil>standing-up>standing | 39 | block (–) | block (-7) |
| jaguar | 21 | `P41` | concussion cannon | 19 | 6 | 22 | 199.6 | recoil>standing | -1 | block (–) | block (1) |
| jaguar | 44 | `P` | jump punch | 15 | 10 | 21 | 71.0 | recoil>standing | 5 | miss (–) | hit (7) |
| jaguar | 43 | `K` | jump kick | 15 | 10 | 21 | 85.0 | recoil>standing | 5 | block (–) | hit (7) |
| shadow | 43 | `P` | standing punch | 13 | 2 | 30 | 95.0 | recoil>standing | -1 | block (–) | block (1) |
| shadow | 42 | `K` | standing kick | 15 | 3 | 30 | 101.0 | recoil>standing | -2 | block (–) | block (0) |
| shadow | 41 | `P6` | forward punch | 7 | 1 | 11 | 95.4 | recoil>standing | 1 | block (–) | block (3) |
| shadow | 15 | `P3` | down-forward punch | 5 | 1 | 17 | 77.0 | recoil>standing | 4 | block (–) | block (6) |
| shadow | 36 | `P2` | down punch | 10 | 1 | 30 | 77.0 | recoil>standing | 1 | block (–) | block (3) |
| shadow | 31 | `P1` | down-back punch | 18 | 5 | 38 | 89.0 | recoil>standing | -2 | block (–) | block (0) |
| shadow | 30 | `P4` | back punch | 13 | 3 | 38 | 104.5 | recoil>standing | 1 | block (–) | block (3) |
| shadow | 17 | `K3` | down-forward kick | 9 | 2 | 17 | 91.0 | recoil>standing | 1 | hit (–) | block (3) |
| shadow | 18 | `K2` | down kick | 14 | 3 | 27 | 91.0 | recoil>standing | -2 | hit (–) | block (0) |
| shadow | 19 | `K1` | down-back kick | 15 | 3 | 41 | 111.0 | recoil>standing-up>standing | 28 | hit (–) | block (-5) |
| shadow | 32 | `K6` | forward kick | 11 | 3 | 17 | 101.4 | recoil>standing | 0 | block (–) | block (2) |
| shadow | 33 | `K4` | back kick | 19 | 4 | 43 | 93.5 | recoil>standing-up>standing | 27 | block (–) | block (-5) |
| shadow | 20 | `P6` | close throw | 46 | 21 | 61 | 37.4 | recoil>wall-damage>recoil>standing-up>standing | 28 | miss (–) | hit (28) |
| shadow | 23 | `P4123` | Shadow Punch (enhancement 3) | 15 | 10 | 14 | 205.5 | recoil>standing | 66 | hit (–) | block (5) |
| shadow | 16 | `P252` | Shadow Grab (P252; holds, no damage) | 14 | 50 | – | 200.0 | recoil>standing | 121 | grab (–) | grab (121) |
| shadow | 24 | `P41` | P41 special (unenhanced) | 15 | 8 | 41 | 205.5 | recoil>standing-up>standing | 35 | block (–) | block (1) |
| shadow | 21 | `K41` | K41 special | 13 | 7 | 41 | 205.5 | recoil>standing-up>standing | 36 | hit (–) | block (-1) |
| shadow | 46 | `P` | jump punch | 18 | 12 | 27 | 62.0 | recoil>standing | -1 | miss (–) | miss (–) |
| shadow | 68 | `K` | jump kick | 16 | 12 | 34 | 69.0 | recoil>standing | 6 | miss (–) | miss (–) |

Columns: **Anim ticks** is the move's full animation length in source ticks (startup,
active, and recovery). **Startup** is ticks from the final input to damage.
**Max hit gap** is the largest tested centre-to-centre distance, in source units, at
which the move still hit (the sweep tests 30–200 units; a result of 199.6 or 205.5
means the projectile reached the end of the sweep). **Adv. on hit** is how many ticks
earlier the attacker is free than the defender (positive favours the attacker); the
guard columns give the result against standing and low guard.

## Reading the table

- Damage includes the match's pilot modifiers; the AF damage field differs (for
  example Jaguar's close throw has an AF value of 45 but measures 38).
- Low attacks (`K3`, `K2`, `K1`) hit a standing guard and are blocked by low guard.
  Jaguar's close throw hit through both guards; Shadow's shows a miss against standing
  guard and a hit against low guard, which has not been explained (it may be a range
  effect at the tested gaps, since the throw's hit gap is only 53 units).
- Jaguar's down punch, the move whose recovery tail was previously unmeasured, runs
  14 ticks: 3 to damage, −1 on hit, +1 against low guard.

## Gaps and special rows

- **Shadow Grab (animation 16, `P252`)** grabs rather than damages. In every tested
  distance up to the 200-unit end of the sweep, Shadow's projection reaches the
  opponent, holds them in throw state 7 for about 85 ticks (tick 176 to 261 in the
  fixture), and releases them with no health loss. It takes 50 ticks from the input
  to the grab, and the grab is not stopped by standing or low guard. The table's
  startup counts ticks to the grab, "damage" is empty by design, and "Adv. on hit"
  (121) is the harness's free-tick comparison, not a normal frame advantage.
- **Shadow jump kick (animation 68)** only connects late in the jump. The harness
  normally presses the button 6 ticks after the jump input, and the kick misses at every
  distance with that lead; with a 12-tick lead (`jump_lead` in `measure_moves.py`) it hits
  for 34 with startup 12. The table row uses a neutral jump, so its 69-unit reach
  understates a forward jump: a scratch run with a forward jump and the same lead hit
  at 40, 70 and 100 units (sample points, not a refined sweep) and missed at 20 and 140.
  The kick missed both standing and low guard in the guard check.
- **Shadow Punch (animation 23, `P4123`)** only exists at enhancement level 3 (its
  base script is a no-op, as in the original Tournament), so the harness sets Shadow's
  upgrade level to 3 for it. Its ice blade travels along the floor: it hits standing
  guard and is blocked by low guard, and its reach (205.5 units) is the end of the
  sweep. Unenhanced, the same input performs animation 24 (`P41`).
- **Shadow forward punch (animation 41)** now reports a normal punch (7 ticks, 11
  damage). At gaps near 30 units the same `P6` input becomes the close throw (animation
  20), so the harness only counts a hit when the attacker is playing the tested
  animation. That correction also lowered Shadow's close-throw reach from 53.4 to 37.4
  units, against Jaguar's 48.0.
- Shadow's `P41` (animation 24) and `K41` (animation 21) were measured unenhanced, as in
  the original Tournament.
- These are single-pilot, single-stage measurements, not universal values.
