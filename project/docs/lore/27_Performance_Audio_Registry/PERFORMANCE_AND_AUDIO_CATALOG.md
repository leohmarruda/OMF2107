# OMF 2107 — Performance and Soundtrack Annotation Catalog v1.0

**Status:** first editorial cue pass, not an approved performance direction or finalized soundtrack. **Scope:** all twelve playable campaigns (Ari's six chapters) plus Christian's subplot. **Source:** BG-coded Story Pack v2.7. No dialogue, choice, match result, emotional canon, or location code was rewritten.

## Inline notation

A voiced statement with clear non-neutral delivery has a `PERF` cue. The cue defines the outward on-screen presentation, not what the character secretly believes.

```markdown
**LYRA:** [PERF: tone=defiant | expression=EXP-DEFIANT | delivery=sharp and steady | intensity=2] Then sell the romance I approve.

**STEFFAN**
**[PERF: tone=determined | expression=EXP-FOCUSED | delivery=steady and purposeful | intensity=2]**
I intend to win.
```

`intensity=1` subtle, `2` noticeable, `3` high; an emotional cue can be changed per shot without rewriting dialogue. **Unmarked lines are unclassified**, not necessarily neutral. Do not generate a bespoke facial sprite for every variation in voice delivery. All expression codes map to a reusable asset family, with lighting, pose and eyebrows providing secondary animation.

A `MUSIC` cue appears beneath each active background entry, for example:

```markdown
**[BG: BG-SOC-GALA@NIGHT]**
**[MUSIC: MUS-GALA | behavior=palette; continue_same_theme_unless_edited]**
```

A cue selects a **scene palette**, not a hard track restart. When a background changes but the emotional beat continues, keep the existing track; when a romance/confrontation choice changes the beat, the runtime may crossfade to a different palette. Do not gate core evidence, fight results, or character decisions on soundtrack selection. All themes must be newly composed or properly licensed; no actual audio is included.

## Character-render guidelines

- Facial expression is the **visible performance**. Track hidden motives separately (`subtext` / relationship-state), especially for Steffan, Raven, Kreissack, and Nova.
- Dante is **nonromantic toward Steffan by default**. The optional romance requires active player choices; a facial cue never overrides that distinction.
- Crystal's involuntary submissive response to Raven can coexist with alarm, defiance and anger. **Do not interpret a vulnerable expression as consent.** Raven's enjoyment of exploitation is established independently of player-controlled restraint.
- Lyra's athletic confidence and glamour can coexist; a seductive or playful expression does not imply the absence of boundaries.
- Varga's charm must not overwrite her culpability for unauthorized psychological research. Kreissack's sacrifice does not absolve his 2092 murders.
- For voiced-only systems such as Nova, apply delivery/voice processing rather than forcibly rendering a human face.

## Assets and validation

- `registry.json`: emotion → expression → default delivery; music palette descriptions; active revision map.
- `dialogue_cues.csv`: one parsed actor statement per row, including currently unclassified statements; source line, speaker, emotion, facial expression, intensity and evidence.
- `scene_music_cues.csv`: every soundtrack/background binding with source filename and scene heading.
- `editorial_review_queue.csv`: conservative follow-up queue of ambiguous lines and weaker inferred cues.
- `script_revisions.csv`: previous and annotated active screenplay versions. Original versions are retained.
- `test_performance_audio_registry.py`: confirms all annotated files can be stripped back to the byte-identical screenplay and validates cue codes.

### Performance cue coverage

| Campaign | Dialogue turns parsed | Explicit expressive cues |
|---|---:|---:|
| Ari | 2018 | 175 |
| Lyra | 112 | 16 |
| Mara | 83 | 15 |
| Ren | 138 | 16 |
| Angel | 100 | 17 |
| Crystal | 76 | 10 |
| Raven | 89 | 27 |
| Jean-Paul | 70 | 8 |
| Steffan | 77 | 23 |
| Dante | 95 | 18 |
| Selene | 59 | 15 |
| Milano | 93 | 6 |
| Christian | 72 | 5 |

Total: **3,082** parsed spoken lines, **351** expressive cues, **449** music palette placements and **843** editorial-review candidates. The expressive cue count is **not a claim that every remaining line is neutral**. Statements embedded in choice-description prose without a recognized speaker label may require manual insertion.

### Music palette distribution

| Palette | Scene placements | Suggested use |
|---|---:|---|
| `MUS-ARENA` | 129 | driving electronic rock and mechanical percussion, combat intensity |
| `MUS-RESCUE` | 64 | urgent rhythmic electronics and high strings, rescue |
| `MUS-INVESTIGATION` | 57 | minimal ticking sequencers and suspense textures |
| `MUS-UNEASE` | 46 | low pulsing synth drones, withheld answers |
| `MUS-ROMANCE` | 34 | warm restrained synth pads and melodic piano, intimate |
| `MUS-GALA` | 32 | opulent electro-orchestral pulse, social spectacle |
| `MUS-CONFRONT` | 24 | driving low strings and industrial pulses, personal conflict |
| `MUS-FINALE` | 15 | hybrid orchestra and industrial electronics, final confrontation |
| `MUS-AFTERMATH` | 14 | quiet elegiac synth and distant strings |
| `MUS-BANTER` | 13 | light syncopated futuristic lounge groove, playful |
| `MUS-ATHLETIC` | 9 | rhythmic electro-percussion, confident athletic motion |
| `MUS-CLINICAL` | 7 | minimal sterile arpeggios and soft electrical hum |
| `MUS-NOVA` | 2 | unsettling polyphonic electronic textures and subbass, autonomous intelligence |
| `MUS-GRIEF` | 2 | sparse piano, low sustained strings, vulnerable |
| `MUS-CORPORATE` | 1 | clean futuristic ambient pulse, public-facing authority |

## Editorial acceptance rules

1. Review all flagged ambiguous lines; distinguish irony, deliberate masking, affection, resentment, manipulative calm, and natural excitement. Do not promote a speculative emotion to canon.
2. Sample adjacent exchanges for expression continuity and sprite feasibility. Use a crossfade or sustained shot, not an instantaneous expression flicker every sentence.
3. Listen to a **scene**, not a single line, when confirming the music palette; add authored choice-triggered transitions for material emotional reversals.
4. Keep early Nova hints subtle: no omniscient AI track declaring covert control before the final reveal. Preserve Day-9/12/13/30 revelation timing.
5. Confirm actor/sprite identity for multipart and voiceover lines; conditional spoken choices in prose are a known follow-up.
6. Preserve player-independent consent, NPC autonomy, and tournament outcomes when adjusting any emotional cues.

**Known limitation:** Cues were assigned through transparent rules plus targeted manual selections, not exhaustive human direction line-by-line. Artistic approval of the flagged queue and of unmarked dialogue remains necessary before character-render commissioning or final score lock.

## Sprite production strategy

The 32 facial-expression codes map into **8 base sprite families** per character where applicable; microexpressions, eye movement, eyebrow blend shapes and lighting provide the variations. See `sprite_asset_plan.csv` and `sprite_selection_cues.csv`. Not all performers need all eight families; minor roles may use a subset. This is an art-direction proposal, not a demand to draw 32 different portraits per character.
