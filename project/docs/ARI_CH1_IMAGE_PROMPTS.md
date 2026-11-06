# Ari Chapter 1: image prompts

Every image the opening slice (Chapter 1 scenes 1 to 5; now part of `project/data/story/ari.story`) called for, collected from the Story Pack. The prompts come from `OMF_2107_Story_Pack/29_Character_Art/Character_Render_Prompts_v1.0.md` and `OMF_2107_Story_Pack/26_Background_Registry/background_states.csv`. Some character prompts (Alex, Haldane, Varga and others) have since been revised and synced into the pack, so check `ARI_MISSING_IMAGE_PROMPTS.md` for the current wording.

All of these images now exist in `project/renders/` and are built into `project/build/art` by `project/tools/build_ari_art.py`; `ari.story` uses them through `art` and `present` lines.

## Not covered

- **HARs.** Thorn (Ari's screenplay HAR) and Mirage (Selene's) have no prompts in the pack, and the prototype only renders Jaguar, Shadow and Katana, so the fight uses those. A HAR cockpit or faceoff image still needs an author-supplied reference.
- **One-line extras** with no prompt in the pack: the sponsors' representative, the gala guest, and the technician in scene 4.
- **Ari is written masculine** in the character prompt, while the screenplay uses "they" and says pronouns adapt to the player's customization.

## 1. Shared art direction for the characters

Put this at the start of every character prompt below.

> Create a **full-body character render** for a **futuristic fighting-game story mode** set in **2107**, using a **polished semi-realistic anime / high-end game illustration style** with **clean linework, cinematic shading, strong silhouette readability, high facial detail, and premium sci-fi costume design**. Show the character in a **front three-quarter standing pose**, centered, with a **neutral transparent background** or plain studio backdrop, suitable for cutting into dialogue scenes. Keep the design visually consistent across the whole cast. Emphasize **personality, clothing silhouette, age, posture, expression, and color palette**. Avoid chibi proportions, caricature, or overly generic cyberpunk clutter. The result should look like a **playable character render or dialogue sprite base**.

Optional suffix for a sprite base: *Keep the pose readable and relatively neutral so the render can serve as a base for expression variants. Prioritize a clean silhouette, clear costume layers, and unobstructed facial features.*

## 2. Characters (10)

### CHR-ARI — Ari Solano
*Used in: Scenes 3 to 5; the player character.*

Create a full-body render of **Ari Solano**, a **26-year-old Ganymede rebel pilot**. Use the **default masculine cinematic interpretation**, while keeping the design compatible with later alternate gender presentations. Ari should look agile, determined, intelligent, and somewhat rough-edged, with the visible marks of living in a working colony. Dress him in **practical frontier / industrial sci-fi clothing**, individualistic rather than corporate, with a silhouette emphasizing mobility rather than brute force. He should project courage, curiosity, distrust of authority, and emotional resilience after loss. Include subtle cues of a colonial outsider with strong convictions.

### CHR-SEL — Selene Vale
*Used in: Scene 5; the opponent in the opening fight.*

Create a full-body render of **Selene Vale**, a **32-year-old undercover heiress and corporate competitor**. She is **elegant, attractive, sophisticated, and self-controlled**, with a mischievous smile and effortless poise. Her wardrobe should move between **luxurious executive fashion** and **high-performance technical practicality**, suggesting a woman equally at home in gala spaces and strategy rooms. She should look intelligent, secretive, and flirtatious without losing authority. Her render should capture someone who enjoys leverage, ambiguity, and polished power.

### CHR-MAR — Mara Voss
*Used in: Scene 3; the gala conversation and the post-loss scene.*

Create a full-body render of **Mara Voss**, a **34-year-old underground champion and hard-lived fighter**. She is **athletic, rugged, practical, and visibly tougher-edged than the glamorous competitors**, with **short dark hair**, a battle-worn style, and signs of a difficult working life. Dress her in **worn leather, practical gear, patched or modified equipment**, and details suggesting a pilot who repairs and repurposes her own tools. Her posture should feel grounded, irreverent, and formidable. Convey both hardness and buried warmth.

### CHR-CRY — Crystal Devroe
*Used in: Scenes 1 and 2; the gala and the watching beat after the win.*

Create a full-body render of **Crystal Devroe**, a **33-year-old legendary tournament heroine**. She is **elegant, athletic, confident, and composed**, with **distinctive dark red hair**, a poised stance, and the aura of a public icon who still feels most comfortable in training spaces. Her face should communicate maturity, self-control, and residual emotional weight beneath a polished exterior. Dress her in a **practical but sophisticated futuristic outfit** that combines **deep red, white, and metallic accents**, balancing interview-ready polish with combat-athlete functionality. She should look like a veteran champion and independent public figure, not a naive rookie. Use a calm, dignified expression and subtle heroic presence.

### CHR-STE — Steffan Thomas
*Used in: Scene 3; seen posing for photographs.*

Create a full-body render of **Steffan Thomas**, a **27-year-old celebrity champion**. He is **attractive, athletic, highly stylish, and visibly media-trained**, with **expressive hair**, a flawless smile, and a posture that says he expects attention. Dress him in **designer futuristic streetwear / athlete-luxury fashion** with fashionable accessories and a silhouette that makes him instantly recognizable. His palette can include hot, energetic tones influenced by his Pyros identity. He should look charismatic, brilliant, competitive, and slightly smug. Beneath the glamorous finish, his expression should hint at emotional immaturity, vanity, and a deep need for admiration.

### CHR-REN — Ren Akiyama
*Used in: Scene 4.*

Create a full-body render of **Ren Akiyama**, a **25-year-old idealistic ace pilot**. Ren should appear **androgynous, elegant, restrained, and distinctly futuristic**, wearing sleek technical clothing with clean silhouettes and minimal decoration. Their design should feel advanced and refined, but still deeply human. Emphasize grace, thoughtfulness, and controlled physicality. Ren should look like someone engaged with cutting-edge human-machine integration without becoming cold or robotic. Use a calm, intelligent expression and a subtle sense of idealism.

### CHR-ANG — Angel
*Used in: Scene 4.*

Create a full-body render of **Angel**, a **provisional 38-year-old mysterious hacker and veteran pilot**. She is **minimalist, understated, technically brilliant, and quietly striking**, with a cool color palette, practical futuristic clothing, and custom-designed wearable tech. Her aesthetic should be sleek but not flashy, suggesting a person who values privacy, function, and control over spectacle. She should appear intelligent, observant, and difficult to read. Incorporate subtle hacker / systems-engineer motifs in her gear. Her posture should be calm and self-possessed, with a reserved expression that still carries intensity.

### CHR-SHI — Shirro
*Used in: Scenes 1 and 5; the announcer.*

Create a full-body render of **Shirro**, an **83-year-old legendary showman and tournament founder**. He should be **flamboyant, vain, funny, and charismatic**, dressed in eye-catching futuristic showman attire that blends luxury, theatricality, and sports-broadcast spectacle. He is elderly but energetic, with a larger-than-life public persona and the timing of a born announcer. His pose should feel performative and playful, as if he is always halfway through introducing the next big event.

### CHR-ALX — Alex
*Used in: Scene 5; broadcast anchor.*

Create a full-body render of **Alex**, a **42-year-old nonbinary, androgynous broadcast anchor**. Their face and body must read as **genuinely gender-ambiguous**: a **slim, straight, medium-height frame with narrow hips and shoulders of the same width, a soft but angular face with a defined jaw and cheekbones, natural bare lips with no lipstick or makeup beyond subtle skin polish, and short, neat, side-parted hair** (keep the cool silver-lilac colour of the current render). No earrings, no necklace, no jewelry except a small pin or a slim wrist-comm. Dress them in **sharp, tailored futuristic broadcast wear**: a **long structured jacket with clean straight lines, high mandarin collar, matching straight-leg trousers and flat polished ankle boots**, in pearl white, graphite and a restrained violet accent, with no skirt, no sash, no heels and no plunging neckline. Pose: upright, composed, one hand holding a slim data slate, calm and neutral. Expression: poised, quietly intelligent, a faint professional half-smile. They should look capable of interviewing celebrities and announcing a scandal with equal composure. Avoid both hyper-feminine and hyper-masculine signals and avoid stereotype; the impression is elegance and neutrality.

Changed from the current render: hair stays short and silver-lilac but is neat and side-parted instead of wavy and glamorous; makeup, earrings, necklace, heels and skirt are removed. Keep the white, graphite and violet palette.

### CHR-LEE — Leena Sato
*Used in: Scene 5; broadcast reporter.*

Create a full-body render of **Leena Sato**, an **investigative reporter**. She should appear **perceptive, empathetic, professionally skeptical, and persistent**, with a practical but stylish journalistic look suitable for moving between public events, backstage access, and sensitive investigations. Her design should convey intelligence and trustworthiness rather than glamour-first presentation. She should feel grounded, observant, and emotionally present.

## 3. Backgrounds (9)

Each prompt already carries the shared station art direction. All are 16:9, 3840x2160, with no people in the foreground.

### BG-HIS-ARENA97@ARCHIVAL: 2097 combat tournament arena
*Used in: intro: 2097 archive footage.*

High quality 2D painted science-fiction visual-novel environment plate, clean perspective, 16:9 3840x2160, empty foreground for character sprites and subtitles, no named people, logos, text or interface. Industrial late-21st-century mechanized tournament floor with angular steel spectator galleries, battered armor plates and coarse analog broadcast lights; clearly earlier technology than the 2107 stadium. Maintain camera framing and industrial 2107 world bible style. Archival 2097 analog-video visual treatment, muted saturation, slight signal aging.

### BG-HIS-LAB97@ARCHIVAL: 2097 destroyed Nova laboratory
*Used in: intro: destroyed laboratory in the montage.*

High quality 2D painted science-fiction visual-novel environment plate, clean perspective, 16:9 3840x2160, empty foreground for character sprites and subtitles, no named people, logos, text or interface. Ruined 2097-era robotics lab after Nova defeat, broken gantries, hanging power cable, devastated experimental pods, dust and severe industrial damage; no bodies. Maintain camera framing and industrial 2107 world bible style. Archival 2097 analog-video visual treatment, muted saturation, slight signal aging.

### BG-EXT-COLONY-CONSTRUCTION@BASE: Ganymede colony construction montage
*Used in: intro: Ganymede construction montage.*

High quality 2D painted science-fiction visual-novel environment plate, clean perspective, 16:9 3840x2160, empty foreground for character sprites and subtitles, no named people, logos, text or interface. Wide 2107-era Ganymede ice-colony construction site, unfinished domes, cargo gantries and blue-grey ice fields, Jupiter dominating black sky. Maintain camera framing and industrial 2107 world bible style. Neutral intact base scene.

### BG-EXT-STATION@BASE: Orbital anniversary complex exterior
*Used in: intro: the arena complex before the title card.*

High-quality hand-painted 2D sci-fi fighting-game and visual-novel environment background, year 2107, cinematic clear architecture, unified WAR orbital station design: ivory ceramic, brushed titanium and amber in public areas, graphite industrial steel in technical areas, cool cyan in restricted labs. Wide locked-off composition, 16:9 landscape 3840x2160, dialogue-safe clean lower foreground, readable perspective geometry, no foreground characters or identifiable people, no robots in the foreground, no lettering, no readable signage, no interface overlays, no watermarks. Jovian orbital anniversary complex built around a circular HAR stadium and observation dome, Jupiter outside. Light, signage, and architecture must align with the other assets in this location family.  Neutral intact base scene.

### BG-SOC-GALA@NIGHT: Anniversary gala interior
*Used in: scenes gala, sponsors, mara_meet and mara_after.*

High-quality hand-painted 2D sci-fi fighting-game and visual-novel environment background, year 2107, cinematic clear architecture, unified WAR orbital station design: ivory ceramic, brushed titanium and amber in public areas, graphite industrial steel in technical areas, cool cyan in restricted labs. Wide locked-off composition, 16:9 landscape 3840x2160, dialogue-safe clean lower foreground, readable perspective geometry, no foreground characters or identifiable people, no robots in the foreground, no lettering, no readable signage, no interface overlays, no watermarks. Double-height anniversary reception hall with panoramic Jovian glazing, warm ivory titanium and amber accents. Light, signage, and architecture must align with the other assets in this location family.  Night-cycle lighting.

### BG-TEC-EXPERIMENT@NIGHT: Experimental equipment / demonstration wing
*Used in: scene ghost.*

High-quality hand-painted 2D sci-fi fighting-game and visual-novel environment background, year 2107, cinematic clear architecture, unified WAR orbital station design: ivory ceramic, brushed titanium and amber in public areas, graphite industrial steel in technical areas, cool cyan in restricted labs. Wide locked-off composition, 16:9 landscape 3840x2160, dialogue-safe clean lower foreground, readable perspective geometry, no foreground characters or identifiable people, no robots in the foreground, no lettering, no readable signage, no interface overlays, no watermarks. Experimental equipment and public demonstration wing, equipment racks, sealed machinery and test platforms. Light, signage, and architecture must align with the other assets in this location family.  Night-cycle lighting.

### BG-ARE-MAIN@BASE: Main tournament combat arena
*Used in: scenes arena, hangar and prefight (the screenplay uses @DAY for the pre-fight).*

High-quality hand-painted 2D sci-fi fighting-game and visual-novel environment background, year 2107, cinematic clear architecture, unified WAR orbital station design: ivory ceramic, brushed titanium and amber in public areas, graphite industrial steel in technical areas, cool cyan in restricted labs. Wide locked-off composition, 16:9 landscape 3840x2160, dialogue-safe clean lower foreground, readable perspective geometry, no foreground characters or identifiable people, no robots in the foreground, no lettering, no readable signage, no interface overlays, no watermarks. Single official HAR tournament arena: reinforced rectangular competition floor, barrier walls, grandstands, overhead display gantries. Light, signage, and architecture must align with the other assets in this location family.  Neutral intact base scene.

### BG-ARE-MAIN@DAY: Main tournament combat arena
*Used in: pre-fight and post-fight in the main arena.*

High-quality hand-painted 2D sci-fi fighting-game and visual-novel environment background, year 2107, cinematic clear architecture, unified WAR orbital station design: ivory ceramic, brushed titanium and amber in public areas, graphite industrial steel in technical areas, cool cyan in restricted labs. Wide locked-off composition, 16:9 landscape 3840x2160, dialogue-safe clean lower foreground, readable perspective geometry, no foreground characters or identifiable people, no robots in the foreground, no lettering, no readable signage, no interface overlays, no watermarks. Single official HAR tournament arena: reinforced rectangular competition floor, barrier walls, grandstands, overhead display gantries. Light, signage, and architecture must align with the other assets in this location family.  Day-cycle station light.

### BG-ARE-MED@BASE: Tournament medical and recovery facilities
*Used in: scene lost: the competitors' medical hall.*

High-quality hand-painted 2D sci-fi fighting-game and visual-novel environment background, year 2107, cinematic clear architecture, unified WAR orbital station design: ivory ceramic, brushed titanium and amber in public areas, graphite industrial steel in technical areas, cool cyan in restricted labs. Wide locked-off composition, 16:9 landscape 3840x2160, dialogue-safe clean lower foreground, readable perspective geometry, no foreground characters or identifiable people, no robots in the foreground, no lettering, no readable signage, no interface overlays, no watermarks. Tournament clinic and recovery corridor, softly lit clinical partitions, medical doors and benches. Light, signage, and architecture must align with the other assets in this location family.  Neutral intact base scene.
