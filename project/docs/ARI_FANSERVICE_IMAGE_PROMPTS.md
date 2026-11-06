# Ari route: fanservice scene illustration prompts

Prompts for the 12 fanservice-tagged scenes in Ari's route (registry: `OMF_2107_Story_Pack/28_Fanservice_Review`). These are optional story frames. Each scene is gated in the script, so a frame only shows when its branch is played.

## How to use

1. Generate the frame with the shared direction plus the scene prompt.
2. Save as PNG in `project/renders/`, wide format (2.58:1, e.g. 2048x792; the story viewer crops to 1280x496).
3. Add the file to `build_ari_art.py` as a frame with the name given below.

## What to attach

Attach the character renders from `project/renders/` as reference images, and say which image is which ("Image 1 is Lyra, image 2 is Alex. Keep their faces, hair and outfit colors exactly"). Do not paste the character prompts: they describe a standing portrait and will fight the scene pose. Attach only the characters in the scene (two or three works best), and a background only where noted, as "setting and lighting reference only". Plug, Cossette and Ibrahim have no render yet.

## Shared direction

Put this at the start of every prompt.

**Content rules (apply to every prompt):** all characters are adults. Tone is flirtatious, glamorou, romantic, or sexy, but never explicit: clothed or in ordinary resort wear, no nudity. Characters keep their own agency and expressions.

> Create a **wide cinematic story-mode scene illustration** for a **futuristic fighting-game visual novel** set in **2107**, in a **polished semi-realistic anime / high-end game illustration style** with **clean linework, cinematic lighting, rich atmospheric color, and strong composition**. The characters must match their approved character renders exactly (face, hair, build, signature outfit colors). All characters are **adults**. The mood is **warm, flirtatious or romantic but tasteful and non-explicit**: characters are fully clothed, expressions are natural and mutual. Landscape 2.58:1 composition with the key characters in the central band so the top and bottom can be cropped. **No text, no lettering, no UI, no logos, no watermarks.**

---

## 1. FS-ARI2-1B — Off Air (Lyra / Alex) — `ari_fs_off_air`

**Attach:** `lyra.png`, `alex.png`. No background.

Backstage broadcast studio just after the interview lights go dark, evening, cool blue-white fill light fading to warm practical lamps. **Lyra** in her shimmering sponsor jacket over training gear sets her Electra gloves down on a desk; **Alex**, the androgynous news anchor, unclips a lapel mic and leans on the desk nearby. They are close but guarded, trading a wry half-smile. Cables, a dark camera and a monitor in soft focus behind them. Mood: relieved, quietly flirtatious.

## 2. FS-ARI2-4B — Neon Respite (public fan event) — `ari_fs_neon_respite`

**Attach:** `lyra.png`, `steffan_thomas.png`, `dante.png`, `mara_voss.png`. Crystal and Shirro: describe only (`crystal_devroe.png` and `shirro.png` if the model keeps faces apart). Too many faces for one pass, so generate the four named fighters first and add the others by edit. No background.

Sponsor rooftop pool at night, neon signage reflecting across the water. A small group of fighters relaxes in **tailored resort attire and tasteful swimwear**: **Lyra**, **Steffan** mid-splash with a grin, **Dante** holding up a soaked jacket in mock dismay, **Mara** with arms crossed and an amused smirk, **Crystal** and **Shirro** laughing at a table. In the foreground a display of miniature HARs catches the reflected pool light. Playful ensemble comedy, glamorous lighting, nobody posed provocatively.

## 3. FS-ARI3-3B — The Velvet Problem (Jean-Paul) — `ari_fs_velvet_problem`

**Attach:** `jean_paul.png`, `varga.png`, plus `BG-SOC-GALA_NIGHT.png` as setting and lighting only.

Research-benefit reception, late evening, a half-empty ballroom with warm chandelier light. **Jean-Paul** with his tuxedo jacket slung over one shoulder and **Dr. Ilse Varga** in an elegant evening suit trade a few graceful dance steps, faces close, eyes locked in a charged, suspicious near-kiss. Hands held at a correct formal distance. Mood: seductive, tense, each clearly testing the other.

## 4. FS-ARI3-5B — Five More Seconds (Ari / Mara) — `ari_fs_five_seconds`

**Attach:** `ari_solano.png`, `mara_voss.png`. Background: `BG-ARE-MAIN_DAY.png` only if it reads as a training hall rather than the match arena; otherwise none.

Training hall in the late afternoon, golden light through high windows. **Mara** in ordinary practice clothing hands **Ari** a towel; their fingers linger a beat too long. Behind them a practice HAR's display flashes a fresh countdown. Both are slightly out of breath, grinning, teasing. No kiss. Mood: athletic banter, a spark neither will name.

## 5. FS-ARI3-7 — An Unfortunate Coincidence (Lyra / Steffan) — `ari_fs_coincidence`

**Attach:** `lyra.png`, `steffan_thomas.png`. No background (the Jupiter window is in the prompt). `BG-EXT-STATION_BASE.png` only if you want its view of Jupiter.

A quiet station service corridor at night, a large window showing Jupiter's banded glow beyond the glass. **Lyra** and **Steffan** stand close in their everyday fight-circuit clothes, sharing an impulsive, mutual, tender kiss, her hand resting on his jacket. Their faces and posture carry regret and conflict as much as affection. Cool blue light from Jupiter on one side, a warm service lamp on the other. Mood: stolen, conflicted, human.

## 6. FS-ARI3-10B — Two Inventors, One Dance (supporting cast) — `ari_fs_two_inventors`

**Attach:** No character renders exist for Cossette or Ibrahim: generate them from the text alone, then save the result as `cossette.png` and `ibrahim.png` in `project/renders/` for reuse. Optional background: `BG-TEC-EXPERIMENT_NIGHT.png` for the workshop.

A cluttered workshop turned into an unexpected ballroom by a test lighting fixture throwing colored light across the room. **Cossette** and **Ibrahim**, an established adult couple, dance joyfully among workbenches and half-built equipment, mid-spin and laughing, an "absurd victory" glow behind them. Warm, cozy, comic. Mood: playful and domestic.

## 7. FS-ARI3-11 — Something Worth Winning For (Ari / Mara) — `ari_fs_worth_winning`

**Attach:** `ari_solano.png`, `mara_voss.png`. No background.

An observation garden on the station, evening. Carefully regulated artificial light on plants, a small ornamental pool, and Jupiter filling the viewport. **Ari** and **Mara** stand side by side at the rail, then closer: his hand finding hers, a quiet sad-then-warm exchange of looks. Soft rim light on both faces, reflections in the pool. Mood: grief easing into tenderness. The kiss branch can be a separate variant (`_kiss`) showing a gentle clothed kiss with the garden softly out of focus.

## 8. FS-ARI4-3B — Cooling System (Mara / Plug) — `ari_fs_cooling_system`

**Attach:** `mara_voss.png`. Plug has no render: describe only, then save the result as `plug.png`. Background: `BG-TEC-EXPERIMENT_NIGHT.png` for the workshop, if it suits.

A hangar workshop, night work lights, a repaired Flail actuator on the bench. **Mara** has pushed her safety goggles up and leans over the actuator, grease on her forearm, exchanging dry banter with **Plug**, who watches her with an unguarded smile. Close, easy, working-partner intimacy; sparks of a welder in the background. Mood: warm, wry, competent.

## 9. FS-ARI4-4B — The Blue Hour (Ari / Mara) — `ari_fs_blue_hour`

**Attach:** `ari_solano.png`, `mara_voss.png`. No background.

A hallway doorway late in the evening, the city bathing everything in deep blue neon through a tall window. **Ari** has put his jacket across **Mara**'s shoulders; they stand close after an argument, guarded and quiet, neither looking away. Soft shadows, blue and magenta edge lights. Mood: intimate, hesitant, after the storm.

## 10. FS-ARI5-7B — Own the Spotlight (Lyra) — `ari_fs_spotlight`

**Attach:** `lyra.png`. Steffan appears only as a silhouette on a screen, so he needs no reference. No background.

A press-prep room with a rack of dramatic tailored outfits. **Lyra** in a metallic-jacketed Electra-inspired outfit holds a confident, defiant pose beside her HAR as flashes go off. On a screen behind her, two silhouettes posed like a romantic duel (no readable caption). Photographers' silhouettes in the foreground, glossy highlights. Mood: glamorous and in control; she owns the story.

## 11. FS-ARI6-15B — No Interview Tonight (Lyra / Alex) — `ari_fs_no_interview`

**Attach:** `lyra.png`, `alex.png`. No background.

A city-view terrace in the evening after a repair event. A huge holographic advertisement of **Lyra**'s old smiling self glows behind her while the real, tired Lyra leans on the rail. **Alex** joins her without a microphone, standing close and offering a quiet smile. Honest, wistful, warm city lights. Mood: tired, tender, no cameras.

## 12. FS-ARI6-16B — Alternative Relationship Epilogues (E1–E4)

**Attach:** E1 `ari_solano.png` + `leena_sato.png`; E2 `mara_voss.png` (Plug: describe only, or `plug.png` once saved); E3 `crystal_devroe.png` + `raven.png`; E4 `ari_solano.png`. Generate one frame per call. No backgrounds.

Produce four small frames, one per branch:

- **`ari_fs_epi_ari_leena` (E1)**: a rain-streaked transit-station noodle bar, **Ari** and **Leena** sharing a booth, Ari's press badge turned face down on the table, both relaxed and smiling.
- **`ari_fs_epi_mara_plug` (E2)**: a public train-station café, **Mara** and **Plug** with a folded "Flail's last invoice" between them, laughing over cups.
- **`ari_fs_epi_crystal_raven` (E3)**: a training room with the sparring lamps on, **Crystal** and **Raven** standing close, comfortable, a faint smile each.
- **`ari_fs_epi_solo` (E4)**: **Ari** alone on a station view platform at dawn, content, a friend's jacket over his arm.

Mood for all four: quiet, resolved, weeks later. Soft warm light, no kissing required.

---

## Open points before production

- The Leena, Alex, Plug and Angel renders need confirmed adult ages in the cast notes (the registry asks for this before production). Scenes 1, 8, 11 and E1/E2 use them.
- Scene 7 shows Lyra kissing Steffan while the default route has her dating Dante. Keep this frame behind its branch gate.
- BG tags and headers disagree for scenes 8, 9 and 10 (time or location). The prompts above follow the scene text; check against the BG cue when the frames are wired in.
