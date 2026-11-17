# Arcade mode image prompts

Image prompts for the arcade ladder story (`project/data/story/arcade_ari.story`). Same house style as `ARI_FANSERVICE_IMAGE_PROMPTS.md`.

## Shared direction

- Wide format, 2.58:1 (e.g. 2048x792).
- Style: polished semi-realistic anime / high-end game illustration style.
- Negatives are written inline in each prompt: no text, no lettering, no UI, no logos, no watermarks, no gore, no nudity.
- Attach reference renders and say which image is which.
- Save finished images in `project/renders/`, named as given in each entry.
- The newsroom and the hangar are **generic sets**: no pilots, no HARs and no characters in them. Pilots, HARs and the live replay are placed on top in the game or in compositing, so each set must leave clear, plain space for them (described in each entry).

## 1. Newsroom: the empty studio

File: `news_studio.png`

Used for the news scenes in the ladder (`art news_{player_har}_{beaten_har}`). The procedural newsroom in `project/tools/build_story_art.py` (`studio_frame()`) is the placeholder this replaces. The anchor (Alex) is added on top of this set, and the story viewer draws the live replay of the fight on the big screen.

Prompt:

> Polished semi-realistic anime / high-end game illustration style, wide cinematic frame. The WRDE tournament newsroom, empty and ready for broadcast: a clean cream studio wall with big tilted lettering and soft graphite and violet accent panels, and a curved anchor desk in the foreground on the left half of the frame with a clear empty chair behind it. On the right, a very large, flat, dark screen mounted on the wall, its glass blank with a faint cool-blue glow and a slim violet bezel, seen at a slight angle so its edges are clear and straight. A small red LIVE badge and a scrolling ticker bar sit at the lower edge, kept abstract. Warm key light on the desk, cool blue spill from the screen, and a shallow depth of field on the background. Mood: polished, authoritative and slightly wry, the voice of the tournament. No people, no robots, no characters, no text, no lettering, no UI, no logos, no watermarks, no gore, no nudity.

Placement notes:

- Keep the big screen a plain, even surface with four clear corners: the live replay is drawn over it as a four-sided shape. In the game, the four corner positions are set by numbers in `story_draw_art_texture` in `main.c` and need updating for a new image.
- Leave the area behind the desk free, so the anchor can be placed there. Alex (CHR-ALX in `29_Character_Art/Character_Render_Prompts_v1.0.md`): 42, nonbinary, silver-lilac side-parted hair, long structured mandarin-collar jacket in pearl white, graphite and violet.
- The existing `news_alex_studio.png` has Alex and two robots baked in, so it does not match this prompt. It is the version in use until this set exists.

## 2. Hangar: the empty repair bay

File: `maintenance_bay.png`

Used for `art maintenance_{player_har}` in the hangar scene after the news. One image serves all HARs: the HAR is placed on top, on the right, facing left, and the mechanic's portrait goes over the left third.

Prompt:

> Polished semi-realistic anime / high-end game illustration style, wide cinematic frame. A HAR maintenance hangar after a tournament fight, empty, lit by warm orange work lamps, with steam drifting through the beams and a few welding sparks hanging in the air. On the right side of the frame an empty repair cradle stands on a clear, flat, lit floor, with maintenance gantries, cables and tool arms around it, and clear open space above it for a giant machine. The left third stays calm and uncluttered: a workbench, tool racks and floor markings, softly out of focus. Mood: tired, warm and hopeful, the pause between fights. No HAR, no robots, no people, no text, no lettering, no UI, no logos, no watermarks, no gore, no nudity.

Placement notes:

- Keep the cradle's floor and background plain and darker than a HAR would be, so a HAR placed on top reads clearly.
- The hangar scratches are drawn live over the HAR using a mask of its outline (`project/build/art/masks/maintenance_<har>.bmp`). `build_story_art.py` builds that mask from the HAR sprite it places today, and will keep doing so when the HAR is composited on the new bay.
- The story file sets Ari's HAR to Jaguar by default. The screenplay gives Ari the Thorn HAR (`ari.story:8`).

## 3. Nova boss fight: two arena frames

Files: `nova_boss_1.png`, `nova_boss_2.png`

The ladder ends with a two-fight Nova boss (`arcade_ari.story:132-159`). Both scenes use `ari_ch1_arena_main` today, and there is no render for it. Nova has no visual specification: the docs call Nova voice-only and mention only "Nova's visor-like sensor array". Kreissack is present in both scenes, and the Character Render Prompts describe him as a 113-year-old whose surviving mind is integrated into a robotic life-support body connected to Nova.

**This section is a proposal.** The look of Nova's HAR is not canon, so approve or change it before generating.

Frame 1, the first form (Nova fights in a Jaguar-class HAR in the script):

> Polished semi-realistic anime / high-end game illustration style, wide cinematic frame. The tournament arena before the final fight, seen from low behind the player's HAR on the left, which faces the boss across the ring. On the right stands **Nova's HAR**, a tall, smooth, unnaturally clean machine with no markings, a single wide visor-like sensor array glowing pale cyan where a head would be, and a stillness that feels wrong beside the other fighters. Spotlights cut through haze, the crowd is a dark blur of lights, and a large video wall above shows only a white-blue glow. High up in a shadowed observation box, a second small light suggests someone watching. Mood: cold, clinical, ominous. No pilot visible, no text, no lettering, no UI, no logos, no watermarks, no gore, no nudity.

Frame 2, the second form (Nova fights in a Shadow-class HAR in the script):

> Same arena and camera as the previous image, a few moments later. **Nova's HAR** has changed: its smooth plating has split and shifted into a slimmer, darker, more fluid form, the visor array now fractured into several drifting pale-cyan lights, and projections of itself, translucent copies, flicker at its sides. The player's HAR on the left is scorched and scratched but standing. The arena lights flicker, the video wall glitches, and the haze is thicker. Mood: uncanny and desperate, the last fight. No pilot visible, no text, no lettering, no UI, no logos, no watermarks, no gore, no nudity.

Attach: a game capture of each HAR for the silhouettes (there are no HAR renders in `project/renders/` yet), and `kreissack.png` if the observation box should show him.

Notes:

- The news scene after fight 1 shows the beaten HAR as Jaguar, and there is no news scene after fight 2 (the script goes straight to `victory`). Check that is what you want before making a third frame.
