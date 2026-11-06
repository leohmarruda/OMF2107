# Ari's route: prompts for the missing images

`project/data/story/ari.story` shows a character with `present <image> ...`, which loads `project/build/art/<image>_cut.bmp`. **Status (2026-11-06):** the renders for all eight missing characters and the five remakes (Crystal, Steffan, Angel, Shirro, Alex) are now in `project/renders/`. They are renamed to the file names `build_ari_art.py` expects, all 18 cut-outs are built, and the eight characters now show their portraits. The prompts below are the current ones, and the pack files `Character_Render_Prompts_v1.0.md` and `.csv` (and Alex in `ARI_CH1_IMAGE_PROMPTS.md`) were synced to them. Eight characters in the route had no portrait: this file collects their prompts. Edit them here and re-sync the pack, or the copies will drift.

No scene art is missing: every `art` line in the script uses a frame that `project/tools/build_ari_art.py` already builds. The `bg` lines are free text and need no image.

## How to add a portrait

1. Generate the render with the shared direction below plus the character prompt.
2. Save it in `project/renders/` as a PNG, in the same shape as the existing character renders (1024x1536, or a tall 768x2880 sheet).
3. Add a cut-out entry for it to `project/tools/build_ari_art.py` (the script already builds `ari`, `selene`, `mara`, `crystal`, `steffan`, `ren`, `angel`, `shirro`, `alex` and `leena`), then run `python project/tools/build_ari_art.py`.
4. The file name must be the lower-case `present` name plus `_cut.bmp`, for example `lyra_cut.bmp`.

The cut-out is the head and torso of the render, 32-bit with alpha, so keep the face and shoulders clear and the background plain.

## Shared art direction

Put this at the start of every character prompt below.

> Create a **full-body character render** for a **futuristic fighting-game story mode** set in **2107**, using a **polished semi-realistic anime / high-end game illustration style** with **clean linework, cinematic shading, strong silhouette readability, high facial detail, and premium sci-fi costume design**. Show the character in a **front three-quarter standing pose**, centered, with a **neutral transparent background** or plain studio backdrop, suitable for cutting into dialogue scenes. Keep the design visually consistent across the whole cast. Emphasize **personality, clothing silhouette, age, posture, expression, and color palette**. Avoid chibi proportions, caricature, or overly generic cyberpunk clutter. The result should look like a **playable character render or dialogue sprite base**.

Optional suffix for a sprite base: *Keep the pose readable and relatively neutral so the render can serve as a base for expression variants. Prioritize a clean silhouette, clear costume layers, and unobstructed facial features.*

Technical notes from the pack: full body visible, hands visible, neutral expression, no text, no watermark, no logos, transparent background if the renderer supports it.

## Missing portraits (8)

| `present` name | File to produce | Appearances in the script |
| --- | --- | --- |
| lyra | `lyra_cut.bmp` | 7 |
| dante | `dante_cut.bmp` | 5 |
| varga | `varga_cut.bmp` | 5 |
| haldane | `haldane_cut.bmp` | 5 |
| christian | `christian_cut.bmp` | 3 |
| jeanpaul | `jeanpaul_cut.bmp` | 3 |
| raven | `raven_cut.bmp` | 2 |
| milano | `milano_cut.bmp` | 2 |

### CHR-LYR — Lyra Kisaragi  (`lyra`)

**Prompt:**
Create a full-body render of **Lyra Kisaragi**, a **26-year-old idol champion and elite athlete**. She should be **stylish, colorful, expressive, and physically credible as a top competitor**, blending **futuristic idol fashion** with **real athletic practicality**. Her wardrobe should balance glamour, playfulness, and competitive confidence. She should radiate charm, social intelligence, and strong self-awareness. Her pose should feel lively and camera-ready, but she must still look like a serious fighter rather than just a pop star. Convey an autonomous woman managing fame on her own terms.

### CHR-DAN — Dante Vey  (`dante`)

**Prompt:**
Create a full-body render of **Dante Vey**, a **28-year-old passionate rival and explosive champion**. He is **athletic, striking, intense, and slightly rebellious**, dressed in fashionable futuristic combat-streetwear that is **stylish but less polished than Steffan’s**. His stance should feel dynamic and confrontational, as if he naturally takes up space and challenges authority. His face should show emotional openness, pride, and volatility. Convey genuine maturity and perceptiveness beneath the temper, but make sure the first impression is strong, passionate, and hard to ignore.

### CHR-VAR — Dr. Ilse Varga  (`varga`)

**Prompt:**
Create a full-body render of **Dr. Ilse Varga**, a **51-year-old senior neural-interface scientist and psychological antagonist**. She is **brilliant, elegant, attractive, dryly humorous, and emotionally cold**. Dress her in a fusion of **high-level research fashion and refined executive elegance**—for example, a sleek futuristic lab ensemble, precision tailoring, and subtle luxury detailing. She should project intelligence, seductive composure, and moral detachment. Her expression should feel controlled and faintly amused, as if she is always analyzing everyone in the room.

### CHR-HAL — Dr. Celia Haldane  (`haldane`)

**Prompt:**
Create a full-body render of **Dr. Celia Haldane**, a **55-year-old technocratic director supervising advanced neural research**. She should look **brilliant, disciplined, austere, and intensely rational**, with a design that blends scientific precision and political authority. Make her clearly different from Dr. Varga: a **short, stocky-to-solid build, broad shoulders, a square face with a strong jaw, deep brown skin, short cropped steel-grey hair, and rimless angular glasses**, with no glamour or softness. Dress her in a **high-collared, structured institutional uniform-coat in slate grey and deep navy with a rigid, military-administrative cut**, minimal jewelry, a small data-badge at the collar, and sensible flat boots, so the look is bureaucratic command rather than luxury fashion. Her posture should be upright and exact, hands clasped behind her back or holding a slate, conveying faith in systems, competence, and dangerous certainty. Her expression should be stern, unsmiling and unblinking.

### CHR-CHR — Christian Devroe  (`christian`)

**Prompt:**
Create a full-body render of **Christian Devroe**, a **33-year-old independent investigator and Crystal’s twin brother**. He should look **intense, protective, and more grounded than he was in youth**, with a practical, field-capable wardrobe that can plausibly belong to a former competitor turned investigator or security specialist. His visual design should echo Crystal subtly without duplicating her style. He should project vigilance, loyalty, and unresolved suspicion. Use a serious expression and ready, observant posture. Likeness to the original game: shaggy, shoulder-length blond hair with a straight fringe, grey-blue eyes, fair skin, a hard level stare. Keep that hair and face recognisable at 33 years old, and keep it close to Crystal's family colouring.

### CHR-JPA — Jean-Paul  (`jeanpaul`)

**Prompt:**
Create a full-body render of **Jean-Paul**, a **37-year-old charming spy, socialite, and competitor**. He is **elegant, expressive, and impeccably dressed**, with **dark hair**, an easy smile, refined posture, and the air of a man utterly comfortable in elite spaces. His clothing should be **luxurious but understated**, futuristic formalwear with tailored lines and subtle premium detailing rather than loud ornament. He should look flirtatious, intelligent, and socially dangerous, with a relaxed pose that suggests confidence, wit, and emotional self-possession. His render should communicate both sophistication and a hint of espionage. Likeness to the original game: spiky orange-red hair swept up and back, green eyes, a fine-boned pale face with a calm, slightly arrogant look. Replace the pack's "dark hair" with this orange-red hair, tamed into an elegant swept-back style for 37.

### CHR-RAV — Raven  (`raven`)

**Prompt:**
Create a full-body render of **Raven**, a **36-year-old dangerous antihero and former mercenary bodyguard**. He is **tall, lean, imposing, and severe**, with a controlled, predatory stillness. Include **visible scars**, sharp facial features, and a dark, economical wardrobe with **black, graphite, and restrained crimson accents**. His posture should feel disciplined and intimidating, like someone who wastes no movement. He should project danger, emotional opacity, and ruthless competence. His design should suggest a man capable of violence, manipulation, and cold self-control, while remaining charismatic enough to anchor a major storyline. Likeness to the original game: dark skin, long straight black hair with a blue sheen falling over one side of the face, narrow pale eyes, a severe closed expression. Use the long black hair, not a shaved or short cut.

### CHR-MIL — Milano Angston  (`milano`)

**Prompt:**
Create a full-body render of **Milano Angston**, a **45-year-old corporate heir and powerful political operator**. He is **tall, elegant, impeccably groomed, and visibly wealthy**, wearing **premium tailored futuristic corporate attire** with understated insignia and impeccable fit. His expression should be carefully controlled, his posture authoritative, and his overall presence polished rather than flashy. He should look like someone accustomed to boardrooms, high-level negotiations, and public scrutiny. Convey refinement, intelligence, institutional power, and a desire for control. Likeness to the original game: tan skin, black hair slicked straight back and tied in a short tail with a red band, heavy brows, a hard sideways look and a faint smirk. Keep the tied-back black hair and red accent, aged to 45 with grey at the temples.

## Remakes of existing renders (5)

Crystal, Steffan, Angel and Shirro already have renders (`crystal_devroe.png`, `steffan_thomas.png`, `angel.png`, `shirro.png` in `project/renders/`), but their faces differ from the original game. These prompts replace them. Each is the pack prompt with the original hair and eye colour added. The changed words are marked with "Changed from the pack". Keep each outfit and palette as in the current render. Put the shared art direction in front of each, and keep the same file name when you replace the PNG, so `build_ari_art.py` needs no change. Re-run it afterwards.

### CHR-CRY — Crystal Devroe  (`crystal`, remake)

**Prompt:**
Create a full-body render of **Crystal Devroe**, a **33-year-old legendary tournament heroine**. She is **elegant, athletic, confident, and composed**, with **long, straight, bright yellow-blonde hair, blue eyes and fair skin**, a poised stance, and the aura of a public icon who still feels most comfortable in training spaces. Her face should communicate maturity, self-control, and residual emotional weight beneath a polished exterior. Dress her in a **practical but sophisticated futuristic outfit** that combines **deep red, white, and metallic accents**, balancing interview-ready polish with combat-athlete functionality. She should look like a veteran champion and independent public figure, not a naive rookie. Use a calm, dignified expression and subtle heroic presence.

Changed from the pack: "distinctive dark red hair" is now long, straight, bright yellow-blonde hair with blue eyes, as in her original portrait. Her red and white outfit stays, so the hair no longer clashes with it. Her twin Christian must share this blonde colouring.

### CHR-STE — Steffan Thomas  (`steffan`, remake)

**Prompt:**
Create a full-body render of **Steffan Thomas**, a **27-year-old celebrity champion**. He is **attractive, athletic, highly stylish, and visibly media-trained**, with **short, dark black hair swept up and back, blue eyes**, a flawless smile, and a posture that says he expects attention. Dress him in **designer futuristic streetwear / athlete-luxury fashion** with a **high white collar** and fashionable accessories, and a silhouette that makes him instantly recognizable. His palette can include hot, energetic tones influenced by his Pyros identity. He should look charismatic, brilliant, competitive, and slightly smug. Beneath the glamorous finish, his expression should hint at emotional immaturity, vanity, and a deep need for admiration.

Changed from the pack: "expressive hair" is now short black hair with blue eyes, and a high white collar echoes his original portrait. Keep the flame-print jacket.

### CHR-ANG — Angel  (`angel`, remake)

**Prompt:**
Create a full-body render of **Angel**, a **provisional 38-year-old mysterious hacker and veteran pilot**. She is **minimalist, understated, technically brilliant, and quietly striking**, with **short, cropped white hair, green eyes and a pale complexion**, a cool color palette, practical futuristic clothing, and custom-designed wearable tech. Her aesthetic should be sleek but not flashy, suggesting a person who values privacy, function, and control over spectacle. She should appear intelligent, observant, and difficult to read. Incorporate subtle hacker / systems-engineer motifs in her gear. Her posture should be calm and self-possessed, with a reserved expression that still carries intensity.

Changed from the pack: the pack gives no hair. It is now short white hair with green eyes, as in her original portrait, instead of a grey bun.

### CHR-SHI — Shirro  (`shirro`, remake)

**Prompt:**
Create a full-body render of **Shirro**, an **83-year-old legendary showman and tournament founder**. He should be **flamboyant, vain, funny, and charismatic**, with a **completely bald head, a heavy square jaw, tanned weathered skin and a broad, knowing grin**, dressed in eye-catching futuristic showman attire that blends luxury, theatricality, and sports-broadcast spectacle. He is elderly but energetic, with a larger-than-life public persona and the timing of a born announcer. His pose should feel performative and playful, as if he is always halfway through introducing the next big event.

Changed from the pack: the pack gives no head or face. He is now bald with a heavy jaw, as in his original portrait, instead of white curly hair. Keep the purple and gold showman coat, and drop the tinted glasses and the microphone only if they hide his face.

### CHR-ALX — Alex  (`alex`, remake)

The current `alex.png` reads as a woman: lipstick, drop earrings, a necklace, a wrap skirt-like overlay and stiletto heels. Alex is nonbinary and androgynous (they/them), so the remake removes every one of those cues.

**Prompt:**
Create a full-body render of **Alex**, a **42-year-old nonbinary, androgynous broadcast anchor**. Their face and body must read as **genuinely gender-ambiguous**: a **slim, straight, medium-height frame with narrow hips and shoulders of the same width, a soft but angular face with a defined jaw and cheekbones, natural bare lips with no lipstick or makeup beyond subtle skin polish, and short, neat, side-parted hair** (keep the cool silver-lilac colour of the current render). No earrings, no necklace, no jewelry except a small pin or a slim wrist-comm. Dress them in **sharp, tailored futuristic broadcast wear**: a **long structured jacket with clean straight lines, high mandarin collar, matching straight-leg trousers and flat polished ankle boots**, in pearl white, graphite and a restrained violet accent, with no skirt, no sash, no heels and no plunging neckline. Pose: upright, composed, one hand holding a slim data slate, calm and neutral. Expression: poised, quietly intelligent, a faint professional half-smile. They should look capable of interviewing celebrities and announcing a scandal with equal composure. Avoid both hyper-feminine and hyper-masculine signals and avoid stereotype; the impression is elegance and neutrality.

Changed from the current render: hair stays short and silver-lilac but is neat and side-parted instead of wavy and glamorous; makeup, earrings, necklace, heels and skirt are removed. Keep the white, graphite and violet palette.

## Likeness to the original OMF 2097 portraits

The new renders must read as the same people as the original in-game pilot portraits (the 56-pixel faces in `project/build/portraits/`, exported from `MELEE.BK`). The pack's prompts leave out hair and eye colour, so the new faces drift. For the four missing portraits that were original pilots (Christian, Raven, Milano, Jean-Paul), a "Likeness to the original game" sentence is now appended to each prompt below. It is an addition to the pack text, so copy it back into the pack file too.

Four renders that already exist also differ from the original. Full replacement prompts for them are in "Remakes of existing renders" above; this table summarises what changes:

| Pilot | Original portrait | Existing render | Regeneration cue |
| --- | --- | --- | --- |
| Crystal | long straight yellow-blonde hair, blue eyes | long wavy dark red hair | long blonde hair, keep the white and crimson suit |
| Steffan | short black hair, blue eyes, white high collar | tousled blond hair | short black hair, blue eyes, keep the flame jacket |
| Angel | short white hair, green eyes | silver-grey hair in a bun | short white hair, green eyes |
| Shirro | bald, heavy, older, tan skin | curly white hair, tinted glasses, purple showman coat | bald head, heavy jaw, keep the showman coat |

Ren, Leena, Alex, Ari, Selene and Mara have no original portrait, so they stay as they are.

## Optional extras

These characters speak but are never shown with `present`, so they need nothing now. Their prompts are in the same pack file if you want portraits later: Major Hans Kreissack (`CHR-KRE`), Plug McEllis (`CHR-PLG`), Imani Sorell (`CHR-IMA`).

## Not covered

- **HARs.** Thorn (Ari's screenplay HAR) and Mirage have no prompts in the pack, and the prototype renders only Jaguar, Shadow and Katana. Nova's two boss forms have no image either.
- **One-line extras** with no prompt in the pack: the interviewer, the sponsors' representative, the technicians and inspectors, the test pilot, the panel member and the legal researcher.
- **Ari is written masculine** in the pack's character prompt, while the screenplay says pronouns adapt to the player's customization.
