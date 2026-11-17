# OMF 2107 — Expression Sprite Production List v1.0

**Purpose:** Standalone checklist for character-expression artwork. **Source of truth:** Story Pack v2.8, `27_Performance_Audio_Registry/registry.json`, `sprite_asset_plan.csv`, and `sprite_selection_cues.csv`. This file does **not** introduce or rename any expression codes.

**Inventory:** **8 reusable sprite families**, **32 registered expression types**, and a mandatory baseline neutral portrait for every rendered speaker. Counts are observations from the **351 explicitly tagged dialogue cues**, not an exhaustive inventory of every emotion in the screenplay; 843 additional lines are in the editorial review queue.

## Asset production rule

Generate the *base facial pose* for each needed `SPR-…` family **per character**. Realize `EXP-…` variants as eyebrow/eye/mouth layers, blendshapes or separate full sprites as required by the game engine. Do not produce 32 unrelated character portraits when eight base families plus overlays suffice. `SPR-NEUTRAL` must exist even when the dialogue has no explicitly annotated neutral line.

- **Framing:** consistent three-quarter-body or waist-up character portrait, same camera, scale, anatomy, hairstyle, outfit and lighting across all expression variants of that character; transparent background; no environmental background, text or speech bubble.
- **Identity:** preserve distinctive facial structure and silhouette. Emotion changes expression, not facial identity.
- **Naming:** `CHARACTER__SPR-FAMILY.png` for bases; `CHARACTER__EXP-CODE.png` for full expression renders, or an equivalent keyed overlay asset. Use stable code exactly as registered.
- **Priority:** `P1` = ≥10 current tagged uses; `P2` = 1–9; `P3` = 0 uses (retain in registry, render when needed). This is production evidence, **not** a measure of story importance. Surprise is a sensible optional generic transition even though currently untagged.
- **Intensity:** keep the same expression key and modulate strength at levels 1/2/3; do not create a new code per intensity.

## 1. Base sprite family checklist

| Produce | Base code | Family | Art direction | Registered expression types | Tagged cue uses |
|---|---|---|---|---:|---:|
| ☐ | `SPR-NEUTRAL` | **Neutral / restrained** | Resting face and relaxed posture, fully recognizable; all characters need a neutral default. | 2 | 16 |
| ☐ | `SPR-SMILE` | **Positive / playful** | Raised mouth corners, responsive cheeks and brightened eyes; suitable for amusement, teasing and triumph. | 4 | 103 |
| ☐ | `SPR-WARM` | **Tender / receptive** | Gentle eyes, relaxed cheeks, soft mouth; differentiate affection, hope and vulnerability with gaze and brows. | 5 | 39 |
| ☐ | `SPR-INTENSE` | **Assertive / confrontational** | Focused eyes, controlled brows and jaw tension; cover resolve, pride, defiance, anger and menace. | 6 | 92 |
| ☐ | `SPR-SKEPTICAL` | **Guarded / calculating** | Asymmetric brows, narrowed eyes and controlled mouth; cover doubt, sarcasm, disdain and manipulation. | 5 | 64 |
| ☐ | `SPR-SAD` | **Pain / remorse** | Lower gaze, drawn brows and reduced muscle energy; grief and hurt need different intensity, not identical crying. | 5 | 19 |
| ☐ | `SPR-CONCERN` | **Concern / fear / conflict** | Tension in eyes and brows, uncertain mouth; concern can be outward-focused, fear can be wider-eyed. | 4 | 18 |
| ☐ | `SPR-SURPRISE` | **Surprise / shock** | Eyebrows lifted, eyes widened, mouth briefly parted; usually a short transitional pose. | 1 | 0 |

## 2. Complete expression-type checklist (all 32)

For each entry, generate a keyed face variant only for characters who need it. A line of dialogue can use a variant without requiring an entirely new body pose.

### `SPR-NEUTRAL` — Neutral / restrained

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-RESERVED` | Minimal mouth movement, guarded eyes, tightened corners; no overt hostility. | 15 | P1 |
| ☐ | `EXP-COMPOSED` | Level gaze, relaxed jaw, slight confidence without a smile; restrained posture. | 1 | P2 |

### `SPR-SMILE` — Positive / playful

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-BRIGHT` | Wide enthusiastic smile, lively eyes; energetic rather than permanently shouting. | 62 | P1 |
| ☐ | `EXP-SMILE` | Authentic modest smile; cheek lift and slight eye crinkle. | 23 | P1 |
| ☐ | `EXP-SMIRK` | One corner of mouth raised, eyebrow subtly cocked; playful or provocative. | 18 | P1 |
| ☐ | `EXP-TRIUMPH` | Exultant smile, raised chin and visibly released tension after victory. | 0 | P3 |

### `SPR-WARM` — Tender / receptive

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-FLIRT` | Soft, sustained eye contact; half-smile, slightly lowered lids; confident not necessarily submissive. | 12 | P1 |
| ☐ | `EXP-VULNERABLE` | Unprotected gaze and loosened facial mask; uncertain mouth and subtle hesitation. | 11 | P1 |
| ☐ | `EXP-HOPE` | Tentative brightening in eyes, mouth just beginning to lift; expectation with uncertainty. | 10 | P1 |
| ☐ | `EXP-TENDER` | Gentle, open gaze and restrained warm smile; tenderness without forced happiness. | 5 | P2 |
| ☐ | `EXP-RELIEF` | Exhale visible through softened jaw/brows and eased shoulders; release of held tension. | 1 | P2 |

### `SPR-INTENSE` — Assertive / confrontational

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-DEFIANT` | Firm eye contact, set jaw, brows drawn; refusing to yield. | 35 | P1 |
| ☐ | `EXP-PROUD` | Chin slightly raised, composed intense eyes, contained satisfied smile or none. | 21 | P1 |
| ☐ | `EXP-GLARE` | Hard direct stare, compressed mouth and tense jaw; clearly hostile or accusatory. | 15 | P1 |
| ☐ | `EXP-FOCUSED` | Narrowed attentive gaze, steady mouth and concentrated brow; not anger. | 10 | P1 |
| ☐ | `EXP-MENACE` | Cold narrowed eyes, slight downward brow angle, threatening stillness; avoid villain caricature. | 6 | P2 |
| ☐ | `EXP-INTENSE` | Unbroken piercing gaze and controlled jaw; powerful directive presence, not inherently sexual. | 5 | P2 |

### `SPR-SKEPTICAL` — Guarded / calculating

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-SKEPTICAL` | One brow raised, doubtful eyes and closed lips; question rather than condemn. | 21 | P1 |
| ☐ | `EXP-BITTER` | Uneven tight mouth, slight sneer, resentful eyes; lingering grudge rather than explosive anger. | 17 | P1 |
| ☐ | `EXP-DISDAIN` | Mild upper-lip raise and dismissive gaze or brow; superior and contemptuous. | 12 | P1 |
| ☐ | `EXP-DRY` | Deadpan eyes, tiny unilateral mouth shift; sarcasm without an exaggerated grin. | 12 | P1 |
| ☐ | `EXP-CALCULATING` | Measuring side-glance or still gaze, barely perceptible knowing smile; keep true intent ambiguous. | 2 | P2 |

### `SPR-SAD` — Pain / remorse

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-REMORSE` | Brows angled upward centrally, downcast eyes, apologetic tense mouth; responsibility rather than mere sadness. | 10 | P1 |
| ☐ | `EXP-HURT` | Brows pinched, gaze unsteady, lips pressed to contain emotion; wounded but not necessarily crying. | 5 | P2 |
| ☐ | `EXP-SAD` | Downward eye focus, gentle lowered brows and mouth; subdued grief/sadness. | 2 | P2 |
| ☐ | `EXP-DOWNCAST` | Avoided gaze, lowered head and tense self-conscious mouth; embarrassment or shame. | 1 | P2 |
| ☐ | `EXP-GRIEF` | Trembling lower eyelids, strained mouth and possible tears; use sparingly for acute loss. | 1 | P2 |

### `SPR-CONCERN` — Concern / fear / conflict

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-CONFLICTED` | Uneven tension across eyebrows, hesitant mouth; competing feelings and indecision. | 8 | P2 |
| ☐ | `EXP-CONCERN` | Brows furrowed or lifted toward center, attentive anxious gaze; care directed at someone else. | 6 | P2 |
| ☐ | `EXP-FEAR` | Widened eyes, raised brows, parted tense lips; credible alarm rather than comedy. | 3 | P2 |
| ☐ | `EXP-WORRIED` | Restless eye line, knitted brows and subtle lip bite/press; anticipatory anxiety. | 1 | P2 |

### `SPR-SURPRISE` — Surprise / shock

| Generate | Expression key | Visible facial direction | Uses | Priority |
|---|---|---|---:|---|
| ☐ | `EXP-SURPRISED` | Quick widened eyes, high brows, slightly open mouth; transitional shock. | 0 | P3 |

## 3. Minimum expressions by character (currently evidenced)

This is an **initial order sheet**, not a final per-character list. Every character additionally gets `SPR-NEUTRAL`, and families/expressions missing from the cue pass may be required after editorial review. Family abbreviations use the unchanged `SPR-…` codes.

| Character | Tagged expressions | Families evidenced beyond neutral (number of dialogue cues) |
|---|---:|---|
| Ari | 23 | `SPR-INTENSE` (10), `SPR-SMILE` (4), `SPR-SKEPTICAL` (4), `SPR-WARM` (3), `SPR-CONCERN` (1), `SPR-SAD` (1) |
| Mara | 36 | `SPR-INTENSE` (11), `SPR-SKEPTICAL` (10), `SPR-WARM` (6), `SPR-SMILE` (4), `SPR-SAD` (2), `SPR-CONCERN` (2) |
| Lyra | 51 | `SPR-INTENSE` (20), `SPR-SMILE` (15), `SPR-SKEPTICAL` (6), `SPR-SAD` (4), `SPR-WARM` (4), `SPR-CONCERN` (1) |
| Ren | 12 | `SPR-CONCERN` (4), `SPR-SKEPTICAL` (3), `SPR-INTENSE` (2), `SPR-WARM` (2), `SPR-SMILE` (1) |
| Angel | 16 | `SPR-SMILE` (4), `SPR-WARM` (4), `SPR-SKEPTICAL` (3), `SPR-INTENSE` (2), `SPR-CONCERN` (1), `SPR-SAD` (1) |
| Crystal | 28 | `SPR-INTENSE` (12), `SPR-SKEPTICAL` (5), `SPR-CONCERN` (3), `SPR-SMILE` (3), `SPR-SAD` (2) |
| Raven | 14 | `SPR-INTENSE` (6), `SPR-SKEPTICAL` (3), `SPR-WARM` (1), `SPR-SMILE` (1) |
| Jean-Paul | 10 | `SPR-INTENSE` (5), `SPR-WARM` (3), `SPR-SMILE` (1), `SPR-SKEPTICAL` (1) |
| Steffan | 27 | `SPR-WARM` (7), `SPR-SMILE` (6), `SPR-INTENSE` (5), `SPR-SKEPTICAL` (4), `SPR-SAD` (2) |
| Dante | 23 | `SPR-SKEPTICAL` (8), `SPR-INTENSE` (6), `SPR-WARM` (3), `SPR-CONCERN` (3), `SPR-SMILE` (1) |
| Selene | 15 | `SPR-INTENSE` (4), `SPR-SKEPTICAL` (4), `SPR-SMILE` (4), `SPR-CONCERN` (1), `SPR-WARM` (1) |
| Milano | 5 | `SPR-WARM` (2), `SPR-SKEPTICAL` (1), `SPR-SAD` (1), `SPR-INTENSE` (1) |
| Christian | 5 | `SPR-WARM` (2), `SPR-INTENSE` (1), `SPR-SAD` (1), `SPR-CONCERN` (1) |
| Varga | 4 | `SPR-SAD` (2), `SPR-INTENSE` (1) |
| Alex | 9 | `SPR-SMILE` (8), `SPR-SKEPTICAL` (1) |
| Leena | 4 | `SPR-SMILE` (2), `SPR-WARM` (1), `SPR-INTENSE` (1) |
| Plug | 6 | `SPR-SMILE` (4), `SPR-SKEPTICAL` (1), `SPR-INTENSE` (1) |
| Shirro | 33 | `SPR-SMILE` (33) |
| Kreissack | 8 | `SPR-SMILE` (6), `SPR-SAD` (2) |
| Ibrahim | 1 | `SPR-SAD` (1) |
| Cosette | 0 | None yet — editorial review required |

**Caution:** The zero-use result for Cossette is an annotation-coverage gap, **not** a recommendation to omit her. Her established romance with Ibrahim and potential consensual non-monogamous routes require deliberate warm, playful, and composed sprite review. Similarly, untagged neutral dialogue should not be interpreted as proof that the character has no emotion.

## 4. Recommended generation sequence

1. Draw neutral portraits for the 12 playable pilots and supporting characters who appear visually. Lock each character’s model sheet, palette, proportions, clothing and eye line.
2. Draw the most frequently used expressive families per character (`SPR-INTENSE`, `SPR-SMILE`, `SPR-SKEPTICAL`, `SPR-WARM` are common across the current pass).
3. Add remaining required families from the table, then author `EXP-…` micro-variants using expression layers wherever possible.
4. Review the 843 flagged dialogue lines and any unparsed dialogue before locking the asset manifest; add expression demand without changing existing codes unless a new distinct visual state truly warrants it.
5. Spot-check adjacent dialogue for jarring pose toggles, especially romantic deception, restrained anger, ironic speech, coercive behavior, and hidden motives. Do **not** visually portray involuntary emotional reactions as consent.

## 5. Implementation acceptance checklist

- [ ] Every sprite-capable character has an approved neutral portrait and consistent camera/scale.
- [ ] Each `EXP-…` referenced by the scripts resolves to its registered `SPR-…` family or a specific valid rendered asset.
- [ ] Expressions are legible at dialogue-box scale without exaggerated facial distortion.
- [ ] Sprite overlays align with the original neutral facial landmarks.
- [ ] Alternative costumes and outfits reuse expression layers when facial geometry allows.
- [ ] Missing or ambiguous expression cues are visibly marked as editorial TBD, not silently converted to neutral canon.
- [ ] Voice-only characters (notably Nova) receive appropriate vocal delivery/effects rather than fabricated humanoid expression portraits.

---

*Provenance: derived from the embedded v2.8 registry and observed v2.8 selection cues. Does not change existing scripts, route logic or canon.*
