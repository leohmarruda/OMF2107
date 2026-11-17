# CURRENT RELEASE — v5.8 background locations ratified (authoritative entrypoint)

The authoritative active-script manifest is the twelve-pilot table below. Read the **latest** author decisions and addenda before older sections. Historical headings such as “current release v4.8,” and historical claims that the circular-group tiebreaker is unresolved, are superseded and retained only as provenance; they are **not current rules**.

## Current policy snapshot

- **Tournament:** wins, then recorded cumulative scores for circular 1–1–1 groups; two-way equal score by head-to-head; all-three-equal score by persisted uniform random permutation. No drawn individual fights.
- **NPC knockouts:** all 66 exact-pair winners are assigned for development: 7 cinematic canon, 8 explicit author-approved, and 51 provisional. NPC-vs-NPC fights occur **offscreen**. Do not require cutscenes or choreography.
- **Relationships:** Dante–Lyra established before opening gala; Cossette–Ibrahim steady, Cossette–Milano casual, precise CNM agreements unspecified. Crystal does not recognize Raven's manipulation as it occurs. A person may unilaterally end a relationship; forming new ones requires independent affirmative decisions.
- **Nova finale:** the core destruction causal mechanism is established. Raven's noncombat exception is ratified as canon (v5.3). As of **v5.4**, the facility's zone adjacency, clearance authority, and support-cast assignments are also ratified — see `32_Day13_Finale_Reconciliation/DAY13_RECONCILIATION_v3.4.md` D13-05/D13-06 and `DAY13_ACCESS_AND_BRANCHING_v3.5.md`. As of **v5.5**, Raven's cleared/combat branch also states explicit retry-from-checkpoint on a failed G strike, matching Dante's and Selene's already-active text; his noncombat branch's failed/withheld map remains final for that attempt by design, not retried. This closes every pack-wide Day-13 open item; nothing scoped to the finale staging remains open.
- **Production:** screenplay state guards and validation functions are not evidence of runtime wiring. All conditional dialogue, group scores and saved draws must be consumed by the engine. As of **v5.6**, `29_Character_Art/` and `26_Background_Registry/` have also been audited (previously untouched by this review): the character-render set was missing Tessa Kade and all 12 HAR renders, and 113 of 449 scene-to-background bindings are unconfirmed editorial guesses pending script-editor review. See `00_README/manifest.json`'s `unapproved_decisions` for the full list.

**Release quality:** v5.8 closes the background-location open item: the author reviewed the corrected 122-scene list and ratified it as-is -- no script-editor review is required for these before image production. v5.7 found that the background-bindings file behind v5.6's provisional-scene list was itself bound to 18 stale script versions, and rebased it against the actually-active scripts -- see the v5.7 addendum below. v5.6 extended the review to character art and background prompts, closing one real gap (Tessa Kade's missing render prompt) and surfacing open items (HAR renders, provisional background locations, the Fanservice legacy-card bank's missing background references) without silently fixing any of them. v5.5 closed the last pack-wide Day-13 open decision (Raven retry/stakes parity) with one appended sentence to his active screenplay, no line-number shift; v5.4 closed the facility-map and support-cast decisions by author choice among drafted options; v5.3 fixed the test-runner's silent-skip bug and two stale audit documents. v5.2 verified source and regression integrity, not a complete playthrough or editorial signoff. See `13_Cross_Campaign_Audit/FINAL_STABILIZATION_AUDIT_v5.2.md` (with its v5.3 addendum).

---

# Current addendum: v5.8 background locations ratified. The author reviewed the corrected 122-scene list (112 `staging-provisional` + 10 `source-prose-montage`) delivered in v5.7 and approved all of it as-is. `scene_background_bindings.csv` now carries an `author_ratified` column (`v5.8` on those 122 rows). This records approval of the chosen background per scene, not a claim that the underlying prose now contains an explicit slugline -- the `binding` column and the matching inline `[BG: ... | STAGING PROVISIONAL — no source slugline]` tags in the screenplay files are unchanged, since they state a true fact about the source text that ratifying the location choice doesn't alter. No script-editor review is required for these 122 scenes before image production. Full suite: 424 tests, 24 directories, all PASS.

# Current addendum: v5.7 background bindings rebase. `26_Background_Registry/scene_background_bindings.csv` -- the file v5.6's provisional-scene list was pulled from -- turned out to be bound to stale script versions across the board: all 18 referenced screenplay files were superseded revisions (e.g. Lyra v0.5 instead of active v0.8, Crystal v0.7 instead of active v0.10, Raven v0.6 instead of active v0.9), confirmed by direct line-count and line-content diff rather than assumed. Regenerated the file from scratch by parsing the 18 actually-active scripts' scene headings, slugline detection and inline `[BG: ...]` tags; verified against `test_background_registry.py` live (4/4 pass) and spot-checked by hand. Per-directory staging-provisional counts matched the old file exactly, confirming the underlying scene structure is stable across revisions even though the old line numbers and text were wrong. New totals: 112 `staging-provisional` + 10 `source-prose-montage` = 122 scenes without an explicit slugline (the old file had missed 9 of the 10 montage chains, counting only 1). Corrected list delivered to the author. `background_registry.json`'s `source_scenes`/`scene_count`/`inferred_uses` fields are a separate, still-open instance of the same staleness -- left untouched pending author input, since `inferred_uses`' derivation logic was never documented. Full suite: 424 tests, 24 directories, all PASS; no other files touched.

# Current addendum: v5.6 art and background audit. Extended the review (for the first time) into `29_Character_Art/` and `26_Background_Registry/`. **Character art:** `Character_Render_Prompts_v1.0` claimed full-cast coverage at "12 pilots + 11 supporting = 23," but Tessa Kade -- a recurring named character with her own romance-flag branch in Ren's campaign (`connection=tessa`) -- had no prompt. Added `CHR-TES` in the same format/style as the other 23 entries; scope line corrected to 24. The 12 player HAR mecha (Jaguar, Katana, Shadow, Pyros, Chronos, Gargoyle, Thorn, Electra, Shredder, Mirage, Helix, Flail) remain entirely unprompted and out of scope for this pass, pending an author-supplied reference image. **Backgrounds:** `background_states.csv` was cross-checked directly against `BACKGROUND_CATALOG.md` and `scene_background_bindings.csv` rather than trusted as-is: all 160 catalog code+state combinations have a matching, non-empty prompt, and all 449 scene bindings resolve to real catalog entries (`test_background_registry.py` re-run live, 4/4 pass -- no regressions). Of those 449 bindings, 112 are `staging-provisional` plus 1 `source-prose-montage` (113 total) -- scenes whose background assignment is an editorial guess, never confirmed against an explicit script slugline; delivered to the author as a standalone list for review. Separately, `optional_scene_locations.csv` was found to cover only 3 scenes (all from `Ari_Alternate_Scenes_v0.1.md`); it has no entries at all for the 12 legacy Fanservice proposal cards or `Optional_Relationship_Scene_Cards_v0.1.md`. **Fanservice legacy bank:** the 12 proposal-only scene cards (S1-S12) were checked against the 65 active-script tags and found to match the same content ceiling (implied intimacy/fade-to-black, no anatomical description) with no new issue -- overlapping pairings/titles with active scenes are already self-flagged in the cards' own tag notes. Full suite: 424 tests, 24 directories, all PASS.

# Current addendum: v5.5 Day-13 retry parity. The one remaining item on `DAY13_ACCESS_AND_BRANCHING_v3.5.md`'s decisions list — explicit failure/retry presentation, stakes and timings for Dante, Selene and Raven — is closed. Dante's and Selene's active screenplay text already stated retry-from-checkpoint on a failed G strike; Raven's cleared/combat branch (R6.3) did not. One sentence was appended to his existing paragraph (no line-number shift) giving his combat branch the same retry-from-checkpoint behavior, and stating explicitly that his noncombat branch's failed/withheld map is final for that attempt — losing the chance to shape the extraction, not the chance to retry the map — a deliberate difference in kind between his two branches, not an oversight. No other campaign needed this: only Dante, Selene and Raven were ever flagged ambiguous here. This closes every pack-wide Day-13 open item; what remains in `manifest.json`'s `unapproved_decisions` is scoped to individual, non-finale items (NPC-outcome signoff, tournament-reference signoff, runtime persistence, and the already-tracked Fanservice registry staleness). Full suite: 424 tests, 24 directories, all PASS.

# Current addendum: v5.4 Day-13 canon ratification. The two remaining pack-wide open decisions from D13-05/D13-06 were drafted as three concrete options each and decided by the author. **Facility (D13-05):** clearance authority stays deliberately impersonal — no named safety office, committee, or individual ever issues a "cleared"/"denied" decision, in any save; zone adjacency is a **hub with no pilot/technician overlap** — Z1 reaches Z0 and Z4 by corridor, and Z2/Z3 (where the live Nova chassis is) only by data/command line, never a walkable door, so a technician is never physically in the chassis room. **Support cast (D13-06):** ratified the pattern already implicit in the active text — Angel/Ren/Plug are the default technical trio when not playing; Crystal (investigation/comms), Mara (worker-safety/labor-liaison) and Ari (HAR-deployment support) take their own specialty when not playing — plus three constraints: hands-on hardware action is always Plug's/an unnamed technician's unless that pilot is playing; no two campaigns may claim the same non-selected pilot performed two different, mutually exclusive physical actions in the same scene; G-credit is never reassigned off the selected pilot. The last constraint is now a real regression test, `32_Day13_Finale_Reconciliation/test_support_cast_canon_v54.py`, confirmed against a deliberately injected violation before being accepted — not merely written and trusted. Neither ratification required any screenplay edit; both were already the de facto pattern in the active scripts. Full suite: 424 tests, 24 directories, all PASS.

# Current addendum: v5.3 Day-13 audit regeneration and test-runner fix. `00_README/run_all_tests.py` now invokes `pytest` instead of `python -m unittest discover`, which was silently collecting zero tests from `19_Kreissack_Arc/test_pov_integration_v19.py` (pytest-idiom file; 27 tests recovered). Full suite: 423 tests, 24 directories, all PASS, no execution-limit issue. `32_Day13_Finale_Reconciliation/DAY13_POV_ACCESS_MATRIX_v3.4.csv` and `DAY13_RECONCILIATION_v3.4.md` were regenerated against the screenplay text actually active today: D13-04's Selene and Dante clauses were already fixed in-script and are now closed in the audit docs (no screenplay rewrites needed). Steffan's ST6.3 had the same ambiguity still genuinely open in-script; fixed with one appended sentence (new finding D13-09, closed same pass). Raven's noncombat exception (D13-03) is ratified as final canon — `finale_flow.py` and the active R6.3 text already implemented it identically, so this closes an approval gap, not a code or prose gap. Two tautological tests (`13_Cross_Campaign_Audit/test_v52_release_gate.py`, `28_Fanservice_Review/test_fanservice_registry.py`) were hardened to check real code/data instead of bare string presence; doing so surfaced two Fanservice registry entries (`FS-CRYSTAL-C3-2`, `FS-RAVEN-R3-2`) whose cached scene text predates the v4.7 relationship-canon rewrite below — both are genuine, approved content changes, now tracked as an explicit documented exception in the test rather than silently passing or failing. See `00_README/manifest.json` for the full change list.

# Current addendum: v5.1 screenplay continuity repairs. See `13_Cross_Campaign_Audit/RELATIONSHIP_SCREENPLAY_RECONCILIATION_v5.1.md`. The active Lyra, Dante, and Raven scripts now reflect the approved circular-score tiebreaker and event-time knowledge/relationship guards; no new romance or outcome was authorized.

# Current addendum: v5.0 relationship baseline and scene-time projections. See `13_Cross_Campaign_Audit/RELATIONSHIP_TIMELINE_INTEGRATION_v5.0.md`. The v4.9 audit remains historical; the 567 references are candidates, not certified scene corrections.

# OMF 2107 — Current release v4.8 (Cossette / Ibrahim / Milano)

**Latest author authority:** `02_Story_Bibles/Relationship_Canon_Clarifications_v4.8.md`. Cossette and Ibrahim remain steady partners; Cossette and Milano have a casual fling, not a second commitment, with a significant status imbalance. Relationship ledger now distinguishes casual ties from committed bonds. Precise CNM agreements remain unspecified.

# OMF 2107 — Current release v4.7 (relationship canon reconciliation)

**New direct-author authority:** `02_Story_Bibles/Relationship_Canon_Clarifications_v4.7.md`. Dante and Lyra knew each other previously and began their relationship before the gala. Crystal does not recognize Raven's manipulation as it occurs because her submissive response conceals it; a later revelation requires independent evidence. Active Dante, Lyra, Crystal and Raven scripts were narrowly corrected. Existing historical material is superseded on conflicts; no new optional romance approved.

# OMF 2107 — Current release v4.6 (provisional NPC decisions + relationship integration start)

**Latest addendum:** `07_Tournament_Model/NPC_PROVISIONAL_POLICY_v4.6.md` and `08_Relationship_Model/RELATIONSHIP_INTEGRATION_STATUS_v4.6.md`. All 66 NPC knockout pairings have a development winner (7 canonical, 8 explicit author approvals, 51 provisional). Provisional is **not** final canon; keep both gates separate. The remaining 51 no longer block development simulations.

# OMF 2107 — CURRENT RELEASE / authoring authority v4.3

**This is the current entrypoint for the project.** Earlier `README.md`, the `COMBINED_WORKING_EDITION.md` and old overview versions are historical and may list obsolete active files. This archive keeps all historical versions deliberately.

## Current active screenplay and route specifications

| Pilot | Active screenplay | Route spec |
|---|---|---|
| Ari | `04_Screenplay_Reconstructions/Chapter_01_Anniversary_v0.6.md + Chapter_02_Champions_Shadow_v0.7.md + Chapter_03_Trouble_With_Attraction_v0.7.md + Chapter_04_No_Holding_Back_v0.7.md + Chapter_05_Fractures_v0.7.md + Chapter_06_One_Must_Fall_v0.8.md` | `14_Ari_Campaign/Ari_Route_Spec_v0.1.md` |
| Lyra | `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.8.md` | `09_Lyra_Campaign/Lyra_Route_Spec_v0.1.md` |
| Mara | `10_Mara_Campaign/Mara_Playable_Screenplay_v0.6.md` | `10_Mara_Campaign/Mara_Route_Spec_v0.1.md` |
| Ren | `11_Ren_Campaign/Ren_Playable_Screenplay_v0.6.md` | `11_Ren_Campaign/Ren_Route_Spec_v0.1.md` |
| Angel | `12_Angel_Campaign/Angel_Playable_Screenplay_v0.6.md` | `12_Angel_Campaign/Angel_Route_Spec_v0.1.md` |
| Crystal | `15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.10.md` | `15_Crystal_Campaign/OMF_2107_Crystal_Route_Spec_v0.3.md` |
| Raven | `16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.9.md` | `16_Raven_Campaign/OMF_2107_Raven_Route_Spec_v0.2.md` |
| Jean-Paul | `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.5.md` | `20_Jean_Paul_Campaign/Jean_Paul_Route_Spec_v0.1.md` |
| Steffan | `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.7.md` | `21_Steffan_Campaign/Steffan_Route_Spec_v0.2.md` |
| Dante | `22_Dante_Campaign/Dante_Playable_Screenplay_v0.7.md` | `22_Dante_Campaign/Dante_Route_Spec_v0.2.md` |
| Selene | `23_Selene_Campaign/Selene_Playable_Screenplay_v0.5.md` | `23_Selene_Campaign/Selene_Route_Spec_v0.1.md` |
| Milano | `24_Milano_Campaign/Milano_Playable_Screenplay_v0.5.md` | `24_Milano_Campaign/Milano_Route_Spec_v0.1.md` |

**Ari exception:** Ari is a six-file script in `04_Screenplay_Reconstructions`. Chapter 1 stays at its v0.6 revision (the v2.8 active one); Chapters 2 to 5 are v0.7 and Chapter 6 is v0.8, and the other five chapters have new fanservice-tagged revisions. The original background and performance annotated versions remain intact.

## Canon and proposed scene precedence

1. **Direct author decisions** in addenda and current decision log are highest. Crystal's involuntary pull toward Raven, Raven's enjoyment of exploiting her, Kreissack's 2092 murder order, Steffan's technical brilliance/denied Dante attraction, and **Dante's nonromantic default** are established character facts.
2. The shared canonical *default* event timeline: no drawn fights; Day 9 Kreissack biological survival; Day 11 A/B semifinal and protected Varga disclosure to Lyra; Day 12 genuine Nova rescue **before** C/D semifinal; Day 13 official final then Nova/Kreissack core destruction; Day 30 Devroe E5 order authentication.
3. Player-divergent relationships and new supporting-character scenes in campaign drafts are **proposals** requiring reciprocal authored choice. Inclusion never implies user approval. Particular cases: Dante–Steffan elective future, Milano–Selene, Lyra–Alex, Raven–Mara, Jean-Paul–Selene, Christian–Leena, Ren–Tessa, etc.
4. Historical `Master_Story_Bible_v2.7.md` contains older descriptive sections and later addenda; when older language conflicts with author-established addenda, **the later author-established addendum controls**.
5. **Approved score policy:** circular 1–1–1 groups rank by recorded cumulative group-stage fight score (two fights per pilot); two-way equal totals are resolved by the decisive head-to-head match. Missing scores or three-way equal totals remain unresolved, not arbitrarily seeded. NPC-only knockout **method** approved: deterministic exact-pair outcomes; proposed winners in `npc_pair_proposals.py` are NOT individually approved. Historic default exact-pair results remain established. There are never drawn individual fights.
6. The `08_Relationship_Model` and per-campaign validators are **route scaffolds**, not a global persistent world save or proof of emotional plausibility.

## New review material

- `25_Narrative_Quality_Review/Narrative_Quality_Audit_v2.6.md` — twelve-campaign audit, production blockers and editorial actions.
- `25_Narrative_Quality_Review/Cross_POV_Collision_Matrix_v2.6.md` — shared couples, event ownership, evidence timing.
- `25_Narrative_Quality_Review/Arcade_and_Cinematic_Production_Plan_v2.6.md` — two-mode production budgeting and vertical-slice gates.
- `25_Narrative_Quality_Review/test_active_screenplay_structure.py` — test of unique scene identifiers in new active standalone scripts and staged Day-11/12/13/30 source contract.

**Corrected source:** `22_Dante_Campaign/Dante_Playable_Screenplay_v0.3.md` fixes duplicated scene `DV2.3` and relocates the Days 2–4 training encounter into Chapter 2. No existing prose dialogue or romance-choice semantics were changed.

**Validation:** Baseline v2.5: 268 discovered unittest methods / 18 folders. v2.6: count must be rerun after adding new checks. Tests do **not** constitute a playtest or grant editorial approval.

## Background registry update — v2.7 (retained)

The active screenplay versions listed above contain `[BG: BG-ZONE-LOCATION@STATE]` scene references. The authoritative scene/asset catalog is `26_Background_Registry/BACKGROUND_CATALOG.md`; see the CSV and JSON manifests for individual image-generation prompts, source scenes, and staging uncertainties. Older screenplay revisions remain untouched. This is a background annotation release: it does not alter canon, relationships, or tournament outcomes.

## Recent secondary-romance proposal

`08_Relationship_Model/Secondary_Romance_Expansion_v0.2.md` carries the author-approved Cossette–Ibrahim consensual-non-monogamy direction and provisional Varga/Alex/Cossette romantic expansions. These are design proposals, not added screenplay scenes or new location slots.

**Supporting subplot — Christian:** `18_Christian_Subplot/OMF_2107_Christian_Independent_Storyline_v0.6.md` (performance-annotated).

## Performance and soundtrack cues — v2.8

The **active screenplay versions listed above** now include `[PERF: ...]` on conservatively classified non-neutral spoken dialogue and `[MUSIC: ...]` beneath `[BG: ...]`. See `27_Performance_Audio_Registry/PERFORMANCE_AND_AUDIO_CATALOG.md` for enums, machine-readable dialogue and music mappings, confidence limits, review queue and character-render rules. Original BG-coded v2.7 scripts are still in this archive. **These are editorial performance proposals, not canon changes.**

## Fanservice scene review — v2.9

All active screenplay fanservice scenes and optional intimate beats have explicit `[FANSERVICE: FS-...]` tags; original dialogue, BG/MUSIC/PERF tags and route gates are unchanged. The authoritative index is `28_Fanservice_Review/Fanservice_Review_Index_v1.0.csv`; full copied scenes appear in `28_Fanservice_Review/Fanservice_Scene_Review_v1.0.md`. Historical scene cards have a separately tagged `Spicy_and_Fanservice_Scene_Cards_v0.2.md` version and are **proposal-only**. These tags reflect review scope, not creative approval or automatic eligibility.

### Previous v2.8 active performance versions (retained; not current playback sources)

These files were the baseline for the v2.9 reversible tag edits and remain referenced by the v2.8 performance-audio tests. They are **not** the currently selected gameplay scripts.

- `Angel_Playable_Screenplay_v0.4.md`
- `Chapter_01_Anniversary_v0.5.md`
- `Chapter_02_Champions_Shadow_v0.5.md`
- `Chapter_03_Trouble_With_Attraction_v0.5.md`
- `Chapter_04_No_Holding_Back_v0.5.md`
- `Chapter_05_Fractures_v0.5.md`
- `Chapter_06_One_Must_Fall_v0.6.md`
- `Dante_Playable_Screenplay_v0.5.md`
- `Jean_Paul_Playable_Screenplay_v0.3.md`
- `Lyra_Playable_Screenplay_v0.6.md`
- `Mara_Playable_Screenplay_v0.4.md`
- `Milano_Playable_Screenplay_v0.3.md`
- `OMF_2107_Christian_Independent_Storyline_v0.4.md`
- `OMF_2107_Crystal_Playable_Screenplay_v0.8.md`
- `OMF_2107_Raven_Playable_Screenplay_v0.7.md`
- `Ren_Playable_Screenplay_v0.4.md`
- `Selene_Playable_Screenplay_v0.3.md`
- `Steffan_Playable_Screenplay_v0.5.md`


## Gesture performance cues — v3.1

Current scripts above now contain editorial `[GESTURE: GST-*]` cues tied to non-neutral dialogue turns. These are separate from `EXP-*` facial expression codes; existing prose and performance annotations remain unchanged. See `33_Gesture_Registry/` for the character gesture prompts, cue list and QA summary. Historical scripts remain unchanged.


### Retained v2.9 fanservice-index source filenames (historical, not active)

The original fanservice review index references these preserved source files; the v3.1 gameplay scripts are the gesture-annotated revisions listed in the active table.

- `04_Screenplay_Reconstructions/Chapter_02_Champions_Shadow_v0.6.md`
- `04_Screenplay_Reconstructions/Chapter_03_Trouble_With_Attraction_v0.6.md`
- `04_Screenplay_Reconstructions/Chapter_04_No_Holding_Back_v0.6.md`
- `04_Screenplay_Reconstructions/Chapter_05_Fractures_v0.6.md`
- `04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.7.md`
- `04_Screenplay_Reconstructions/Spicy_and_Fanservice_Scene_Cards_v0.2.md`
- `09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.7.md`
- `10_Mara_Campaign/Mara_Playable_Screenplay_v0.5.md`
- `11_Ren_Campaign/Ren_Playable_Screenplay_v0.5.md`
- `12_Angel_Campaign/Angel_Playable_Screenplay_v0.5.md`
- `15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.9.md`
- `16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.8.md`
- `18_Christian_Subplot/OMF_2107_Christian_Independent_Storyline_v0.5.md`
- `20_Jean_Paul_Campaign/Jean_Paul_Playable_Screenplay_v0.4.md`
- `21_Steffan_Campaign/Steffan_Playable_Screenplay_v0.6.md`
- `22_Dante_Campaign/Dante_Playable_Screenplay_v0.6.md`
- `23_Selene_Campaign/Selene_Playable_Screenplay_v0.4.md`
- `24_Milano_Campaign/Milano_Playable_Screenplay_v0.4.md`

## v3.2 incremental integration repair (appended, no script changes)

See `30_Integration_Repair/REPAIR_STATUS_v3.2.md` and `13_Cross_Campaign_Audit/world_state.py`. Twelve-pilot single-save event-ledger prototype and unit tests added. Tournament tiebreaks and NPC winner defaults remain explicitly provisional; no romantic branch or event was promoted to canon. The historic heading/version above remains from v2.9; this section identifies the newest integration patch.

## v3.3 scene inventory integration (non-canonical)

See `31_Cross_POV_Integration/CROSS_POV_WORKING_MATRIX_v3.3.md`, `ACTIVE_SCENE_INVENTORY_v3.3.csv` and `EVENT_ANCHORS_v3.3.json`. Event matches are **unverified candidates**, not proof of participation or consistency. No scripts or tournament outcomes were changed.

## v3.4 Day-13 finale reconciliation (limited corrections)

See `32_Day13_Finale_Reconciliation/DAY13_RECONCILIATION_v3.4.md` and the 12-route access matrix. Two narrow active-script wording repairs (Milano B→L actuation; Dante campaign count) do not alter the story outcomes. Access clearance, Raven's special-boss exception, and Dante/Selene fight ownership remain open design decisions. This is a source-reviewed reconciliation, **not** an implemented production staging model.

## Day-13 integration v3.5 (provisional choreography)

`32_Day13_Finale_Reconciliation/DAY13_ACCESS_AND_BRANCHING_v3.5.md` and `finale_flow.py` define a functional access/escape contract and one explicit Raven noncombat exception proposal. Active Raven R6.3, Dante DV6.2 and Selene SV6.2 include compatible playable staging. This is **not** author approval of an architectural map, emergency authority, or the Raven exception as permanent canon. The v3.4 source matrix remains a historical snapshot and is not silently marked fully resolved.


## v3.6 tournament-audit extension

See `07_Tournament_Model/TOURNAMENT_DECISION_MEMO_v3.6.md`, `tournament_audit.py` and `audit_outputs/`. This extension inventories resolution provenance for every simulated bracket, identifies fallback dependence and implements a strict validation option. Public 1–1–1 rankings and nondefault NPC outcomes remain unapproved. The Day-13 branch work in v3.5 is unchanged.

## v3.7 score tiebreak and tournament-route screenplay binding

The author approved actual tracked game scores for circular standings and a deterministic authored NPC-only pairing table. `07_Tournament_Model/TOURNAMENT_INTEGRATION_v3.7.md` records the score interface, strict-mode rules, proposed NPC pair outcomes, and binding requirements. Proposed NPC winners remain pending review. `tournament_scene_state.py` produces branch-dependent character/event information for screenplay use; scripts have not all been migrated to runtime calls.

## v3.8 tournament reconciliation

See `07_Tournament_Model/TOURNAMENT_SCREENPLAY_RECONCILIATION_v3.8.md` and its source-linked CSV triage. Fixed one conditional trophy-presentation contradiction and clarified one unapproved alternative NPC result in active Ari scenes; added secondary two-way score tiebreak and branch-state contract tests. No new NPC match winner approved.

## v3.9 NPC matchup provenance audit

See `07_Tournament_Model/NPC_OUTCOME_EDITORIAL_AUDIT_v3.9.md`, `NPC_PAIR_EDITORIAL_REVIEW_v3.9.csv` and `NPC_PAIR_REVIEW_SUMMARY_v3.9.json`. The 66 proposed pairings contain seven established cinematic exact-pair defaults, 51 proposed winners inherited from the old global priority, and eight exceptions. **No new NPC winner approved.** Sampling 384 input tuples observed 21 pairs as NPC-only knockouts; that sample is not an exhaustive reachability model for arbitrary group results and score ranking. Four new regression tests protect this distinction. No active screenplay or bracket outcomes changed.

## v4.0 — focused NPC matchups (proposal only)

`07_Tournament_Model/NPC_PRIORITY_MATCHUP_DOSSIERS_v4.0.md` and `.csv` offer tactical hypotheses and counterplay for 14 observed nondefault NPC-only pairings. **No new winner is approved; `npc_pair_proposals.py` remains opt-in.** Corresponding tests are `test_npc_priority_dossiers_v40.py`. All historical review artifacts remain valid.

## v4.1 — offscreen NPC results (author decision)

NPC-versus-NPC fights are **never shown**. `07_Tournament_Model/NPC_OFFSCREEN_POLICY_v4.1.md` supersedes v4.0 dossier requests for authored fight scenes or cinematic evidence. `offscreen_npc_results.py` supplies a scoreboard/bracket/dialogue projection with no invented scores and with production-mode rejection of unapproved results. The v4.0 winner proposals remain unapproved. No active screenplay or runtime was changed in this pass.

## v4.2 — exhaustive NPC pair reachability (no new canon)

`07_Tournament_Model/NPC_REACHABILITY_AND_DECISIONS_v4.2.md` supersedes the *interpretation* of the 21-pair NPC sample: exhaustive structural bracket enumeration shows all 66 unordered fighter pairs can arise, with 18 QF, 30 SF and 36 Final stage-specific pairs. The accompanying CSV and reproducible Python enumerator identify 59 unapproved pair winners. No offscreen fights are shown; no winners are promoted to canon, no numeric scores are fabricated, and the three-way tie policy still requires approval. The v4.1 offscreen scoreboard and screenplay remain unchanged.

## v4.3 NPC decision consolidation

See `07_Tournament_Model/NPC_APPROVAL_GUIDE_v4.3.md` and `NPC_OUTCOME_APPROVAL_LEDGER_v4.3.csv`. These are REVIEW artifacts only; 59 new winners and the residual three-way score tie remain unapproved. The NPC fights are offscreen. The earlier v4.0 dossier directions for depicting fights have been superseded.

## v4.4 — approved random three-way score draw

The random six-permutation fallback for exactly equal three-way group-score totals is approved and implemented in `07_Tournament_Model/tournament_validator.py`, with the saved-draw contract in `THREE_WAY_RANDOM_TIE_CANON_v4.4.md`. Tournament runtime MUST persist the draw before using it. NPC winners (59) and score comparability remain unresolved.

## v4.5 — eight author-approved NPC outcomes

Eight previously pending NPC-only knockout results were explicitly approved by the author on 2026-11-03. **Mara vs Steffan: Steffan**, overriding the historical Mara proposal. Seven prior cinematic results remain unchanged. See `07_Tournament_Model/NPC_AUTHOR_DECISIONS_v4.5.md` and the new `NPC_OUTCOME_APPROVAL_LEDGER_v4.5.csv`. The v4.3 ledger remains historical. **15/66 pairings resolved; 51 pending.** NPC fights remain offscreen.

## v4.9 — relationship-continuity contract repair and review inventory

Separated partners may leave unilaterally following their independently recorded negative choice; a partner cannot veto separation. Five tests cover the change. See `08_Relationship_Model/RELATIONSHIP_CONTINUITY_AUDIT_v4.9.md` for outstanding integration gaps, plus its source-linked scene candidate CSV. The candidate rows are not editorial signoffs. No new romance, consent, or NPC outcome was established by this patch.
