# Cross-POV integration working matrix — v3.3

**Status:** generated source-linked inventory and review protocol. **Not a confirmed continuity audit or a canon change.** Baseline: v3.2. Narrative dialogue, canon, fight results, relationship outcomes and authored branch rules are unchanged.

## Coverage

- 12 selectable pilots, 17 active campaign screenplay files and 405 structurally identified scenes.
- Scene counts: Ari 106, Lyra 30, Mara 27, Ren 30, Angel 26, Crystal 27, Raven 27, Jean-Paul 28, Steffan 27, Dante 25, Selene 27, Milano 25.
- Candidate shared-event references: K_BIO 47, VARGA_EVIDENCE 27, DANTE_STEFFAN_PRIVATE 8, SF_AB 17, RESCUE 32, SF_CD 9, FINAL 43, NOVA_CORE 29, DEVROE_ORDER_E5 10.
- Ari uses different scene-heading conventions and chapter-local scene numbering; **source path + ID**, not ID alone, is its identity.
- Event candidates are keyword matches within a scene, **not** validated event instances. A scene discussing a historical event may match without witnessing it. Empty event candidates do **not** prove absence.

## Required verification fields (in CSV)

`event_verified`: approved shared event ID(s) **only** after comparing actual described action. `phase_candidate`: provisional reference only; review actual in-scene timing. `physical_access_verified`: independently justified route, escort, equipment, constraints, exit. `knowledge_verified`: evidence acquired from known source before acted upon. `branch_predicates_verified`: explicit on/off conditions, NPC agency, tournament dependency. `review_status`: UNREVIEWED / CONFIRMED / REWRITE_NEEDED / NOT_APPLICABLE. Empty fields mean **not evaluated**, not passing.

## One physical event, many POV observations

| Global event | Canon timing | Required consistency checks |
|---|---|---|
| K_BIO | Day 9 | Protagonist's evidence provenance vs audience disclosure; do not grant omniscience |
| VARGA_EVIDENCE | Days 8–11; Lyra obtains protected evidence Day 11 | Sender, custody, recipient, disclosure, privacy |
| DANTE_STEFFAN_PRIVATE | Day 11 | Same underlying exchange; Dante nonromantic by default; optional attraction only via explicit later branch |
| SF_AB | Day 11 | Bracket-qualified fighters and results exclusively from match state |
| RESCUE | Day 12, before SF_CD | One autonomous Nova rescue; separate witnesses, no falsified command ownership |
| SF_CD | Day 12, after RESCUE | Actual bracket-qualified fighters and result |
| FINAL | Day 13 | Tournament concludes before Nova boss; no dialogue-created victories |
| NOVA_CORE | Day 13 after FINAL | Exactly one destruction event; participant entry, location, access and equipment must reconcile |
| DEVROE_ORDER_E5 | Day 30 | Christian's independent authentication; prior knowledge must not be retroactively inferred |

## Collision-review procedure

1. Filter `ACTIVE_SCENE_INVENTORY_v3.3.csv` by a candidate event. Read **all source scenes** in that event cluster; include scenes with no keyword hits identified by plot review.
2. Assign single physical event ID; record separate witness statements, access route and source of information for every pilot. Do not automatically merge alternative selected-pilot histories.
3. Record event facts that must be invariant and route-dependent facts that can differ. Determine whether NPC decisions belong to counterpart-authored scenes.
4. Check cause and effect: each character's knowledge must predate their relevant actions; the Nova rescue precedes CD semifinal, and official final precedes Nova encounter.
5. Validate conditional branches against a specific world-state event sequence. If the material is ambiguous, mark REWRITE_NEEDED or an author decision—never assume new canon.

## Integration status and explicit blockers

- **Delivered:** deterministic inventory + source line anchors + 9 event-cluster candidate searches + checks for coverage and source shifts.
- **Not delivered:** human verification of all scenes, scene-by-scene access routes, canonical witness assignments, full evidence custody graph, conditional branch execution, narrative rewrites, NPC tournament defaults.
- **Priority review sequence:** Day-13 `NOVA_CORE` access/witness paths; Day-11 Dante–Steffan scene; protected Varga disclosure; Day-12 rescue; Day-30 order; bracket-dependent fights.
- **Author decisions preserved as open:** circular standings, NPC knockout outcomes, proposed optional romances and any new physical event access resolution.
