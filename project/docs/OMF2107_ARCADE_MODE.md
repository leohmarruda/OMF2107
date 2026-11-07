# OMF2107 Arcade Mode

Mechanics of the arcade ladder as implemented on 2026-11-07. Script: `project/data/story/arcade_ari.story`. Art prompts live in `ARCADE_MODE_PROMPTS.md`; this file covers the mechanics. Pointers are file:line.

## Summary

A scripted ladder of five rungs plus a two-fight Nova boss. Each fight launches a real OpenOMF match as a child process. The match result file drives the newscast, hangar and tune-up scenes. Dialogue in the script is placeholder (`arcade_ari.story:4-5`).

## Run it

- `omf3d_prototype --arcade` swaps in `arcade_ari.story` (`main.c:3529-3539`).
- `project/scripts/run-arcade.ps1` wraps `run-story.ps1`: `-New`, `-DebugFights`, `-Scene rung1..rung5|nova1|nova2|news|hangar|victory`.
- Save: `project/build/story/arcade_ari.save`.

## Flow

1. **Setup.** HAR picker offers Jaguar, Shadow, Katana (default Jaguar, `main.c:109`, `2740-2749`). The prompts doc says Ari should be Thorn, but Thorn is not in the picker.
2. **Rungs.** Selene, Crystal, Mara, Ren, Lyra, then Nova round 1 and round 2 (`story:29-160`). Difficulty 1 to 5 across the rungs, Nova 1 at 5, Nova 2 at 6. The `lives` field is unused (`story:7`, `:25`).
3. **Match.** `story_match_start` (`main.c:2546-2611`) runs `run-blockout-jaguar.ps1` with `-RivalDifficulty` and the tune arg (Windows only). `story_match_poll` (`:2613-2640`) reads `project/build/story/match-result.txt` with `winner=` and `hit=side,height,damage` lines.
4. **Win.** `wonN` sets `beaten`, `beaten_har`, `next_opponent`, then goes to the newscast.
5. **Loss.** `retry` offers Rematch (same rung) or Give up, which goes to `gameover` (`story:209-224`).
6. **Newscast.** Shows `art news_{player_har}_{beaten_har}`, Leena in the pit lane, then the hangar (`story:163-181`). A 24-frame, 320x180 replay is captured to `project/build/news_replay` (`main.c:3404-3476`) and drawn on the studio screen (`:1860-1870`).
7. **Hangar.** Scratches are drawn from the fight's `hit=` lines (`main.c:1760-1765`, `1879-1900`) and reset every fight (`:2571`). They need the mask `project/build/art/masks/maintenance_<har>.bmp`. Sparks and warning lamps at `:2231-2360`. Name tags draw in the bottom corners (`:2431`).
8. **Tune-up.** The player picks `armor`, `power` or `speed` (`story:192-194`, read at `main.c:2576-2579`). It applies to the player's HAR until the next pick.
9. **Ending.** After Nova 2 the script goes directly to `victory` (`story:160`), skipping news and hangar.

## Tune-up values

| Pick | Effect | Code |
|---|---|---|
| armor | player HP 125% | `main.c:2577`, `har.c:2708-2710` |
| power | player damage dealt 120% | `main.c:2578`, `har.c:856-858` |
| speed | forward and back walk speed 115% (jump unaffected) | `main.c:2579`, `har.c:2739-2742` |

Environment clamp 50 to 200 (`har.c:2651-2655`).

## Implemented vs missing

- **Implemented:** ladder, match launch and result parsing, win/loss/retry, newscast replay capture, scratches, name tags, tune-up, victory.
- **Art missing from the tree:** `news_studio.png`, `news_<har>_<har>` and `maintenance_<har>` renders, the masks, and the `nova_boss_*` frames. Present: `renders/maintenance_bay.png`, `renders/news_alex_studio.png`. Run `tools/build_story_art.py` to regenerate what it can.
- **Not implemented:** `lives`, gamepad input in the arcade match, non-Windows match launch.

## Decisions made

- **Input (decided):** the arcade match must use the shared OpenOMF input layer, so remapping and gamepads work. See `OMF2107_CONTROLS.md`.
- **Tune-ups (decided):** gains diminish with each pick of the same stat. This means picks must stack, which changes the current "one pick at a time" behavior.

### Proposed stacking scheme (not implemented, needs play-testing)

Each repeat pick of a stat adds half the previous increment. Increments add up; they do not compound.

| Stat | Pick 1 | Pick 2 | Pick 3 | Pick 4 | Total after 4 |
|---|---|---|---|---|---|
| Armor (HP) | +25% | +12.5% | +6.25% | +3.1% | +46.9% |
| Power (damage) | +20% | +10% | +5% | +2.5% | +37.5% |
| Speed (walk) | +15% | +7.5% | +3.75% | +1.9% | +28.1% |

The ladder allows at most six picks (after rungs 1 to 5 and Nova round 1; the ending skips the hangar). A player who spreads picks gets more than one who stacks a single stat, which is the point. Implementation needs the tune values to persist per stat in the story save and be passed to the match as three multipliers instead of one `tune=` arg (`main.c:2576-2579`).

- **Ladder (decided):** randomized. The current script is a fixed order (Selene, Crystal, Mara, Ren, Lyra, then Nova), so this needs a design for what is random (see Still open).
- **Thorn (decided):** added later. Until then Ari plays as Jaguar, Shadow or Katana.

## Still open

- What exactly is randomized? Suggested: shuffle the five rung opponents, keep Nova 1 and Nova 2 fixed as the finale, and raise difficulty by rung number, not by opponent.
- Story beats tied to a fixed order (`beaten`, `beaten_har`, `next_opponent` newscast lines) must work in any order.
- None of the earlier open questions remain; the next step is play-testing the values.

## Lives by difficulty (decided in principle, values proposed)

**Decided:** lives depend on the difficulty mode. Easy has unlimited lives. The hardest mode has zero lives, meaning no continues: the first lost match ends the run (`gameover`). This replaces the unused `lives` field in `arcade_ari.story` (`:7`, `:25`) and the always-on Rematch in `retry` (`story:209-224`).

"Difficulty mode" is the player's run setting. It is separate from the per-fight rival difficulty (0 to 6) that the ladder already assigns by rung. A mode could also shift those per-fight values, but that is not decided.

Decided table (Normal confirmed, with 3 lives):

| Mode | Lives (continues) | On a loss |
|---|---|---|
| Easy | Unlimited | Rematch, always offered |
| Normal | 3 | Rematch, costs one life; at zero left the next loss ends the run |
| Hard | 0 | Run ends, go to `gameover` |

Decided:
- Lives are one pool for the whole run; they do not refill per rung.
- A failed run restarts with a new shuffle.
- The HUD shows lives remaining, except on Easy.
- Tune-up picks carry over a rematch and are lost only when the run ends.

Decided: the modes also change rival difficulty per fight. Implemented offsets (my values, change if play-testing says so): Easy one level lower, Normal unchanged, Hard one level higher, kept between 1 and 6.

| Fight | Easy | Normal | Hard |
|---|---|---|---|
| Position 1 | 1 | 1 | 2 |
| Position 2 | 1 | 2 | 3 |
| Position 3 | 2 | 3 | 4 |
| Position 4 | 3 | 4 | 5 |
| Position 5 | 4 | 5 | 6 |
| Nova round 1 | 4 | 5 | 6 |
| Nova round 2 | 5 | 6 | 6 |

Implementation: the mode is chosen at setup and saved in the story save; `retry` must branch on lives left. The original OpenOMF behavior is below for comparison; it has no lives at all.

## Implementation status (2026-11-07)

Built and passing `story_check` (check, and 300 of 300 random walks reach the ending). **Not yet played in the real game**, so the match launch, HUD placement and input are untested end to end.

- **Script engine** (`story.c`, `story.h`): new `add <flag> <n>` command (numeric, never below 0, leaves text flags like `unlimited` alone), new `arcade` header line, and `story_set_flag()` for the host.
- **Randomized ladder:** `story_begin` shuffles Selene, Crystal, Mara, Ren and Lyra into flags `at_<opponent>=1..5`; `arcade_ari.story` dispatches through `pick1..pick5`. Nova stays last. Opponent dialogue no longer assumes an order. Rival AI level now follows the rung (1 to 5, then Nova 5 and 6), not the opponent.
- **Lives:** Tab on the selection screen cycles Easy / Normal / Hard (Shift+Tab goes back). Lives are `unlimited`, `3` and `0`. A loss with lives left spends one and offers a rematch; at 0 the run ends. The HUD shows `LIVES n` on Normal and Hard.
- **Stacking tune-ups:** hangar picks add to counters `tn_armor`, `tn_power`, `tn_speed`; the match gets all three multipliers (`-PlayerHpPct`, `-PlayerDamagePct`, `-PlayerSpeedPct`), rounded to whole percent. After n picks: base x (2 - 2^(1-n)), so armor 125, 138, 144, 147; power 120, 130, 135, 138; speed 115, 123, 126, 128.
- **Input:** see `OMF2107_CONTROLS.md`.

Caveats:
- Old arcade saves are refused (the script fingerprint changed). Delete `project/build/story/arcade_ari.save`, or start with Shift+R.
- A new run after Game Over (Shift+R) gets a new shuffle. Quickload keeps the saved shuffle.
- Mode also shifts the rival's AI level (table above). Hard's last three fights all sit at level 6, so Hard flattens at the top.

## Reference: what OpenOMF does on a loss

From OpenOMF-derived C source (not the original binary, and the `OMF2097/` manual folder was not readable, so check the manual before treating this as the original's rule):

- **1P / arcade:** a loss shows a newsroom Continue prompt. Yes retries the same opponent (the opponent's win count is reset); No goes to the scoreboard. No lives counter or game-over screen was found (`newsroom.c:323-325`, `209-224`).
- **Rounds:** best of 1, 3, 5 or 7 from settings, default best 2 of 3 (`arena.c:1806-1822`, `settings.c:101`).
- **Tournament:** a loss drops rank by one, charges a repair fee (`trade_value / 100`, regardless of damage taken) and reduces money. The run ends only if money stays negative across two consecutive matches (`arena.c:307-322`, `348-353`, `383-392`).
- **Not found:** any limit on continues, and a tournament-specific round count.
- Does the decay rate (0.5) hold up against difficulty 5 and 6? Play-test the Nova fights.
