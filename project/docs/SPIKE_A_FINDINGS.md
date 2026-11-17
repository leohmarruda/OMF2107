# Spike A findings: can the rules run on a project data pack?

Date: 2026-11-05. Read-only review of the OpenOMF source in `src/`. Nothing was built or run. Line counts and
include lists come from the files; behaviour is read from the code, not executed.

## Verdict: GO, with conditions

OpenOMF turns the original files into a small runtime data model, and the rule code works on that model. A new loader
that fills the same model from a project data pack is a contained job. The real work is not the loader. It is
authoring new data, and replacing the sprite-pixel hit test with generated masks.

## The seam

`load_af_file()` (`src/resources/af_loader.c`) reads an original AF file into `sd_af_file`, then `af_create()`
converts it to the runtime struct. Everything in `game/` uses the runtime structs only:

```
af (resources/af.h)            id, health, endurance, forward/reverse/jump/fall speed, sound table, moves[]
 af_move (resources/af_move.h) id, animation, pos_constraints, next_move, successor_id, category, points,
                               block_damage, block_stun, throw_duration, extra_string_selector, damage, stun,
                               move_string (input), footer_string
  animation (resources/animation.h)  id, start_pos, collision_coords[{pos, frame_index}],
                               animation_string, extra_strings[], sprites[]
   sprite (resources/sprite.h) id, pos (offset), data = surface (palette-index pixels; width and height)
```

A project loader (`af_create_from_pack`) producing these structs is the whole interface for HAR data. Arena
(`bk_info`), pilot and tournament data have similar loaders (`bk_loader.c`, `pilots.c`, `trnmanager.c`) and are
separate work. OpenOMF also has a mod manager (`resources/modmanager.c`) that overrides sprites, hit coordinates and
AF moves at run time; its interface (`modmanager_get_af_move`, `modmanager_get_hitcoords`, `modmanager_get_sprite`)
shows the same data shape, and it may be a faster first target than a new loader. Not read in detail.

## How hits are decided (matters for 3D)

`game/protos/intersect.c`, function `intersect()`:

- The attacker's frame carries hit points (`collision_coords`, 2D positions in sprite space).
- Each hit point is converted to the target's sprite space. The hit counts only if the target's sprite has a
  non-transparent pixel there, and, for a HAR target, a palette index below 96 (the "main HAR colors").
- Sprite position offsets and sprite size also feed movement (`object_get_size()` = the current sprite's size), so
  the bounding box of the defender's silhouette affects body size in the arena.
- Side flipping is handled in this function.

Consequences for the project:

1. The defender needs, per animation frame, a **bitmap mask and an offset**, in the same 2D resolution as the
   original (the sprite pixel size matters, because physics uses it).
2. The attacker needs, per active frame, **hit points**. These can be generated: the 3D position of the striking
   hand or foot (the rig's effect anchor), projected side-on, instead of being copied from the original data.
3. Both come out of one build step on the blockout proxy (see `HAR_PIPELINE.md`, step P6). The palette-index rule
   (index below 96) becomes a mask flag: body pixels count, effect pixels do not.
4. The mask resolution must match what the measured moves were tuned against. Keep the original sprite scale (a
   HAR of about 100 pixels tall) for the proxy, whatever the 3D view shows.

## Coupling to rendering, audio and UI

Counts of references inside each file (`video_` or `vga_state`, `audio_` or `music_`, `surface`, `gui` or `menu`):

| File | Lines | video | audio | surface | gui |
| --- | --- | --- | --- | --- | --- |
| `game/objects/har.c` | 2,933 | 3 | 0 | 15 | 0 |
| `game/protos/player.c` | 929 | 0 | 4 | 0 | 0 |
| `game/protos/object.c` | 829 | 15 | 0 | 8 | 0 |
| `game/objects/projectile.c` | 274 | 2 | 0 | 22 | 0 |
| `game/objects/hazard.c`, `scrap.c` | 106 | 0 | 0 | 0 | 0 |
| `game/scenes/arena.c` | 2,190 | 3 | 11 | 0 | 55 |
| `game/game_state.c` | 1,717 | 5 | 0 | 0 | 19 |

Reading: the HAR, player-script, object and projectile code is mostly rules, with few rendering and audio calls that
can sit behind interfaces. `arena.c` and `game_state.c` mix rules (round flow, damage, win condition) with menus,
HUD and settings, and need splitting. The extractable core is roughly 6,500 lines (har, player, object, projectile,
hazard, scrap, intersect, controller input) plus the rule parts of arena and game_state. Because the project already
drives OpenOMF through a per-tick state export and shared memory, a simpler first step exists: keep OpenOMF as is,
swap its data loader, and only later fold it in-process.

## What the data pack has to contain (HAR)

| Field group | Source in the pack | Authored or generated |
| --- | --- | --- |
| Stats: health, endurance, four speeds | `har.json` | Authored, tuned to measured behaviour |
| Move table: input string, category, damage, stun, block values, successor, constraints | `moves.json` | Authored from `verification/MOVE_MEASUREMENTS.md` targets |
| Animation string and extra strings (the timing script with tags) | `anim/<id>.txt` | Authored |
| Frame list: per-frame sprite offset and size | Generated | From the proxy pose per frame |
| Defender mask per frame | Generated | From the blockout proxy, cached by pose hash |
| Attacker hit points per active frame | Generated | From the rig's striking anchor, projected |
| Sound table | `har.json` | Authored (new sounds) |

Not in `af`: palette and remap data used for colouring, and shared effect animations (sparks, scrap, blasts). These
need replacements too, listed in "Open items".

## Conditions and risks

1. **Animation strings are a script language** with tags that drive speed, gravity, effects and sounds (`player.c`,
   `formats/script.c`). Authoring them is skilled work. Start by studying how a measured move maps to its string, then
   write a small authoring layer (generate the string from keyframes and measured timing) rather than hand-writing all.
2. **Shared and predefined animations** (jump, stunned, block, walk, idle, victory, defeat, effects) are required by the
   engine (`animation.h` enum). Every HAR must supply them.
3. **Pixel-scale dependence.** Physics reads sprite size, so mask generation must reproduce comparable bounding boxes,
   or movement tuning shifts. Check with the measured wall and crossing behaviour.
4. **Quirk inheritance.** Parity with the measured baseline carries OpenOMF's quirks (for example the accepted
   body overlap in kicks and throws) into the release.
5. **The rule code is MIT** (headers cite Andrew Thompson and Tuomas Virtanen, 2013-2026); keep the notices.

## Open items before M1

- Read `modmanager.c`, `scene.c` (where `load_af_file` is called) and `ai_controller.c` to decide between a mod-manager
  route and a new loader.
- Decide the mask scale and where the mask generator runs (Python in the pipeline, or in the pack builder).
- Arena, pilot, tournament and font replacements: list the formats and loaders (`bk_loader.c`, `pilots.c`,
  `trnmanager.c`, `fonts.c`, `languages.c`, `sounds_loader.c`) and rank by effort.
- Replacement of shared effects and the palette/remap data the sprites assume.
- Confirm by a small experiment: build one fake `af` with one move and a generated mask and run it in a match.

## Estimate

About two weeks for a first loader and one authored move running (the experiment above), then the data-pack format and
validator in Phase 1 as planned. This fits the development plan's M1 date; the main uncertainty is the animation-string
authoring layer.
