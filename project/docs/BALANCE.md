# OMF2107 Balance and Tuning

Where tuning values live and which rules govern changing them. Spec §4.3 names the metrics to capture but gives no numbers; the numbers below come from code on 2026-11-07 (file:line). Per-move frame and hit data live in the original AF/move files, which are not text in this repo and were not inspected. See `verification/MOVE_MEASUREMENTS.md` and `verification/MOVE_CATALOG.md` for measured data.

## Governing rules (spec §4.3, §4.2, §7)

- Feel or accessibility changes must be deliberate, documented tuning decisions.
- AI difficulty adjusts decision quality and reaction allowance, not hidden damage.
- Upgrades stay bounded: a well-played base HAR can beat an upgraded one.
- Expand balance only after the loop is fun over repeated sessions.
- Metrics to capture for Jaguar and one rival: walking speed, jump arc, facing, attack startup and recovery, hit and push distance, block response, stun, special behavior.

## Current formulas (OpenOMF, non-tournament branch)

`is_tournament` is `chr != NULL` (`game_state.c:1707-1709`) and nothing found sets `chr`, so live matches appear to use these. Confirm in play.

| Quantity | Formula | Code |
|---|---|---|
| Damage | base x (20 + power) / 30 + 1, then tune multiplier | `har.c:850-858` |
| Stun | base | `har.c:850-858` |
| Health | AF health x (endurance + 25) / 35 x 1.1 x power mult x vitality | `har.c:2706-2707` |
| Power mult | 2.25 - 0.25 x power | `har.c:2691` |
| Stun cap | AF endurance x 3.6 x (endurance + 16) / 23 | `har.c:2695-2696` |
| Stun factor | 1.2 x 256 x (endurance + 30) / 40 | `har.c:2695-2696` |
| Walk speed | (agility + 20) / 30 x AF speed | `har.c:2729-2743` |
| Jump speed | (agility + 35) / 45 x AF jump speed | `har.c:2729-2743` |

Vitality default 100 (`settings.c:114`). Pilot stat table (power, agility, endurance) is at `main.c:112-115` and feeds HUD rows only.

## Mecha attributes and the new combat layer (decided 2026-11-17)

Each new mecha has Power, Agility and Resistance, 1 to 10, 18 points in total (`COMBAT_UPGRADE.md`, `GAME_MECHANICS.md`). They replace the original AF data as the source of per-robot numbers.

- **Proposed mapping (untested):** the formulas above take the 1 to 10 attribute times 2.5 as their power, agility and endurance input (Power to the power terms, Agility to walk and jump speed, Resistance to the endurance terms). The per-move base damage and stun stay authored per move. The scale of the formula inputs must be confirmed against the original stat range before use; record the final mapping in the log below.
- Pilot stats (about 30 points, `main.c:112-115`) feed the HUD only and stay a separate layer. How they combine with mecha attributes is open (DEVPLAN, "Attribute mapping").
- Attributes guide design; move properties (reach, startup, recovery, damage, guard) win in any conflict.
- **Targets to measure after the first duel (equal-skill players):** matchups near 45 to 55%, tolerated 35 to 65%; no unanswerable strategy; every mecha has a guard, low attacks and an anti-air tool; flight never evades indefinitely. Common combos 2 to 4 hits, exceptional 5 to 7, damage falling in long combos, capped structural damage per combo. Starting damage values (common combo about 8 to 18% of health, exceptional at most about 25 to 30%) are hypotheses against the formulas above.
- **Component damage targets (`career`, fresh mecha):** some component damage in 20 to 40% of fights, at least one Critical component in under 10%, none in over 60% of fights; several Criticals in one fight are exceptional.
- Known risks to test: air mechas dominating slow ones, very tough mechas causing long fights, grabs too strong against guards, camouflage cutting reaction time, snowballing component damage, small bodies winning on collision, combos aimed at one component.

## Difficulty

- Rival difficulty 0 to 6 (`game_state.c:1433-1441`). Without an override the game setting applies (default 1, `settings.c:100`).
- Arcade ladder level follows the fight's position: 1 to 5, then Nova 5 and 6. The run's mode shifts it (Easy -1, Hard +1, clamped to 1 to 6), set in `story_match_start` in `main.c`. See the table in `ARCADE_MODE.md`.

## Arcade tune-ups

Current code: armor 125% HP, power 120% damage, speed 115% walk speed, first-pick values. Decided and implemented: picks stack with halving increments (about +47% HP, +38% damage, +28% speed after four picks of one stat; see `ARCADE_MODE.md`). The stacking has not been play-tested or checked against the "bounded upgrade" rule.

## Other numbers

- Simulation 60 Hz, presentation 60 fps (spec).
- Story trim target about 41 minutes with every fight won, against 25 to 35 (RP).
- 35 Jaguar and Shadow attacks measured (RP).
- The prototype viewer's own sim (`main.c:474-477`: forward 4.4, back 3.52, attack 1.2) is not the arcade match.

## To do

1. Record the Jaguar and rival baseline in the metrics above (start from `verification/JAGUAR_BASELINE.md`).
2. Play-test whether a 25% HP or 20% damage edge breaks the "base HAR can win" rule against difficulty 5 and 6.
3. Decide per-difficulty reaction allowance values and write them here.
4. Add a change log below for every deliberate tuning decision.

## Tuning decisions log

| Date | Change | Reason |
|---|---|---|
| 2026-11-17 | Decided (not yet built): four attack buttons, S1 + C1 grab, mecha attributes 1 to 10 with an 18-point budget, targets above | Adopted from the external robot design document; see `COMBAT_UPGRADE.md` |
