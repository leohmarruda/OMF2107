# OMF2107 Balance and Tuning

Where tuning values live and which rules govern changing them. Spec §4.3 names the metrics to capture but gives no numbers; the numbers below come from code on 2026-11-07 (file:line). Per-move frame and hit data live in the original AF/move files, which are not text in this repo and were not inspected. See `OMF2107_MOVE_MEASUREMENTS.md` and `OMF2107_MOVE_CATALOG.md` for measured data.

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

## Difficulty

- Rival difficulty 0 to 6 (`game_state.c:1433-1441`). Without an override the game setting applies (default 1, `settings.c:100`).
- Arcade ladder level follows the fight's position: 1 to 5, then Nova 5 and 6. The run's mode shifts it (Easy -1, Hard +1, clamped to 1 to 6), set in `story_match_start` in `main.c`. See the table in `OMF2107_ARCADE_MODE.md`.

## Arcade tune-ups

Current code: armor 125% HP, power 120% damage, speed 115% walk speed, one pick at a time. Decided: gains diminish with repeat picks. Proposed scheme (halving increments, about +47% HP, +38% damage, +28% speed after four picks of one stat) is in `OMF2107_ARCADE_MODE.md`. Neither version has been checked against the "bounded upgrade" rule.

## Other numbers

- Simulation 60 Hz, presentation 60 fps (spec).
- Story trim target about 41 minutes with every fight won, against 25 to 35 (RP).
- 35 Jaguar and Shadow attacks measured (RP).
- The prototype viewer's own sim (`main.c:474-477`: forward 4.4, back 3.52, attack 1.2) is not the arcade match.

## To do

1. Record the Jaguar and rival baseline in the metrics above (start from `OMF2107_JAGUAR_BASELINE.md`).
2. Play-test whether a 25% HP or 20% damage edge breaks the "base HAR can win" rule against difficulty 5 and 6.
3. Decide per-difficulty reaction allowance values and write them here.
4. Add a change log below for every deliberate tuning decision.

## Tuning decisions log

| Date | Change | Reason |
|---|---|---|
| (none yet) | | |
