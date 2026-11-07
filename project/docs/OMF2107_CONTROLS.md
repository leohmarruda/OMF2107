# OMF2107 Controls

Default bindings as found in code on 2026-11-07. The spec (§4.2) only commits to preserving movement, punch, kick, guards, jump, crouch, throws and special inputs, with remapping for keyboard and gamepad. It names no defaults, so this file records what the code does today. Sources are file:line pointers.

## Story / arcade window (`project/prototype/main.c:2734-2764`)

| Key | Action |
|---|---|
| Space / Enter | Advance or pick (first press completes the line) |
| Up / Down | Move between choices |
| S | Skip to next choice |
| L | Log |
| Q | Quicksave |
| R | Quickload |
| Shift+R | Restart story |
| M | Mute |
| Y / N | Win / lose match (only with `-DebugFights`) |
| Setup screen | Up/Down/W/S switch route or cycle HAR; Left/Right/A/D choose HAR; Enter/Space starts |

`project/scripts/playtest/README-TESTER.txt` says R restarts the story. Current source says R is quickload and Shift+R restarts. The README describes the packaged tester build, so check which build is right before editing either.

## Arcade match input (`main.c:337-351`, `484-499`)

A/D move, W jump, S duck, J punch, K kick (K wins if both held). Holding away from the opponent guards (per the tester README). Esc closes the match. Input is fed through shared memory (`game_state.c:86-90`, `keyboard.c:33-69`). OpenOMF's own bindings below are not used in the arcade match, and no gamepad path was found for it.

## OpenOMF keyboard defaults (`src/game/utils/settings.c:119-150`)

- **P1:** Up jump, PageUp jump-forward, Right walk-forward, PageDown duck-forward, Down duck, End duck-back, Left walk-back, Home jump-back, Right Shift kick, Return punch.
- **P2:** W jump, E jump-forward, D walk-forward, C duck-forward, X duck, Z duck-back, A walk-back, Q jump-back, Left Shift kick, Left Ctrl punch.

## Menus (`src/controller/keyboard.c:145-175`)

Arrows or numpad 8/2/4/6 navigate. Enter or numpad Enter confirms (punch). Right Shift or numpad 0 is kick. Esc cancels.

## Gamepad (`src/controller/joystick.c:174-184`)

Left stick and D-pad move. A punch (preferred over kick), B kick, Start is Escape. Menus use the same mapping.

## Debug keys (`src/engine.c:205-251`, `DEBUG-KEYS.md`)

F1 screenshot, F2 debug palette, F3 save REC, F5 pause, F6 fight debug, F9 texture atlas, F10 back. `DEBUG-KEYS.md` also lists a Backspace rewind that was not found in code.

## Gaps and decisions

- **Decided:** the arcade match shares OpenOMF's input settings (needed for the remapping commitment in spec §4.2 and DP D07).
- **Implemented 2026-11-07 (not yet tried in play), in the viewer, not in OpenOMF:** the viewer that owns the match window now reads player 1's `key1_*` bindings from `openomf.conf` (looked up in `OPENOMF_CONFIG_PATH`, `XDG_CONFIG_HOME`, then `%APPDATA%\OpenOMF\`) and sends them to the match, so remapping in OpenOMF's Options applies. The first gamepad also works: left stick or D-pad moves, A punch, B kick. Diagonal bindings (jump-forward and so on) are supported. If no `openomf.conf` is found, the old fixed keys (A/D/W/S/J/K) are used.
- **Consequence for testers:** with a config present, the keys follow it (on this machine P1 is W/A/X/D, Left Shift punch, Left Ctrl kick). The tester README's A/D/W/S/J/K line is then wrong.
- **Not done:** this is the smaller of two designs. The viewer still owns the window and the result file, and OpenOMF still reads input from shared memory. Making OpenOMF itself own input would need a visible window, a result writer and a fix at `game_state.c:531`. Player 2 bindings and menu keys are not used by the match.
- Throws, guards and special inputs have no default listed in any doc.
- Story Esc behavior is unconfirmed.
