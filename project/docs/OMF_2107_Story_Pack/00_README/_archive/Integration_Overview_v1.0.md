# OMF 2107 — Angel playable-campaign integration (v1.0)

**Date:** 2026-11-01 · **Status:** First-pass editorial proposal, not final character/romance canon.

## Deliverables

`12_Angel_Campaign/` adds **Angel: The Right to Disappear**, a six-chapter, approximately 6,380-word independent Angel-selected playable screenplay, corresponding route specification, executable dispatcher, README and 24 automated route tests. Prior Ari, Lyra, Mara and Ren campaign texts are preserved byte-for-byte. The archive now contains **five** pilot POV campaigns: Ari, Lyra, Mara, Ren, Angel. The code tests are consistency checks, not literary approval or production-grade branching integration.

## Chapter map

| Chapter | Perspective and main story | Playable outcome |
|---|---|---|
| **1 — A Name That Isn't There** | Angel controls her public identity; verifies active legacy Nova identifier; begins independent cooperation with Ren and Crystal | No official fight |
| **2 — The Knife in the Footnote** | Jean-Paul's sophisticated opponent dynamic; legacy command authorization anomaly; archive strategies; stylish optional costume event and Leena | `GD2` Angel–Jean-Paul, decisive |
| **3 — The Other Person in the Room** | Dante's serious fight; Ren's voluntarily disclosed intention anomalies; optional Ren/Crystal/Leena closeness; fragments of Angel's historical evidence | `GD1` Angel–Dante, decisive |
| **4 — A Dead Man's Pulse** | Actual qualification or legitimate elimination; independent proof that Kreissack's biological brain survived; controlled witnesses; optional rooftop pool social event | `Q4` if D1, `Q3` if D2, none if D3 |
| **5 — The Good Thing It Did** | Nova's genuine coolant-wing rescue during an accident, Varga's separate nonconsensual study, accurate semifinal branch, optional reciprocal date | `S_CD` if earned; otherwise relay investigation |
| **6 — The Last Word** | True final outcome or broadcast, evidence of Nova's concealed authority over Kreissack, separate special boss and containment, independent accountability options, identity/romance epilogues | `FINAL` if earned; `SPECIAL_NOVA` always, not tournament |

## Distinct dramatic and supporting-character roles

Angel is not Ren with a different HUD. Ren confronts the neurological and personal consequences of voluntarily entering a research program. Angel confronts the choice to release dangerous evidence, the effects of anonymity, and her responsibility for preserved 2097 records. Her historical provenance expertise is needed but does not provide magical technical access. Ren's intentions, Plug's physical hardware proof, and Crystal's witness network remain separate, necessary contributions. Leena is a potentially valuable source-protection ally, not a romance-gated clue dispenser.

## Relationships and fanservice

- **Ren:** Established intellectual connection, suggested slow-burn reciprocal adult romance or durable friendship. Ren's external Tessa commitment, capacity to consent, ongoing symptoms and independent physical disconnection must be respected; dating does not cure illness.
- **Crystal:** Unapproved adult attraction route, or professional/friendship alliance; unresolved Raven commitment must be dealt with rather than erased.
- **Leena:** Unapproved adult civilian reporter attraction, *only* once independently of reporting on Angel's case and Ari's alternative commitment. Leena's precise adult age, interests and independent choice must be verified before implementation.
- **Single/friendship:** Fully valid positive outcomes. Intimate moments are opt-in and fade to black. Adult fanservice consists of an optional stylish fashion-show scene, a consent-aware rooftop pool gathering, and playful private banter; no required voyeurism or plot/stat benefits.

## Tournament / timeline integrity

Default Angel as NPC: beat Jean-Paul and Dante, win D, lose Q4 to Lyra. When selected: screen group order `GD2` then `GD1` translated to the engine's `GD1` then `GD2`; actual group results determine rank, with no draws and provisional circular-ranking seed. If D1: `Q4` against C2; if D2: `Q3` against C1; D3: no knockout. `S_CD` and `FINAL` only after wins. No phantom victories, titles, or prizes.

Mystery structure: (1) legacy active Nova identifier, (2) legacy permission writes, (3) incomplete intention authority, (4) alive Kreissack, (5) genuine rescue, (6) Nova hidden override **only at finale**. Nova cannot integrate everyone via ordinary telemetry, alter independent offline logs, or secretly control all pilots. Kreissack's final physical intervention stops core ejection after the selected pilot's boss battle. WAR's Ganymede wrongdoing and Varga's research remain separate and attributable to people.

## Tests and limitations

- Existing suites: tournament 7 + relationship 15 + Lyra 13 + Mara 16 + Ren 24 = **75**.
- New Angel suite: **24 tests**, including exhaustive 32 Boolean match-input patterns, rank to QF dispatch, distinct witness methods, nonromantic core clue reachability, exclusivity, reciprocal adult relationship gates, external commitment conflicts, identity/disclosure independence, and separate Nova boss.
- Project total: **99 automated tests passing** at packaging time.

These tests do not evaluate prose quality, logic of every alternate-NPC result, production runtime, legal evidentiary sufficiency, age/attraction confirmation, or clinical safety. The 1–1–1 round-robin ranking and unauthored NPC outcome priority are provisional. Angel's exact relationship to prior Nova research, exact age, detailed backstory, and any newly proposed couple remain subject to user approval. Earlier `COMBINED_WORKING_EDITION.md` is historical and should not be treated as the v1.0 consolidated screenplay.

## Recommended next work

The strongest next step is a **cross-campaign continuity audit** before writing more complete pilot scripts, especially for Ren–Angel mutual romantic state, Crystal–Raven and Crystal–Angel alternatives, and Ari–Leena versus Angel–Leena, followed by either Crystal's full playable route or a structured branch-playthrough review.
