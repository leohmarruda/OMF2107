# Day-13 Nova finale: source reconciliation v3.4

**Status:** editorial source review and limited, non-canonical clerical corrections. Not an approved security plan, event choreography, or full screenplay rewrite. Base v3.3. Separate protagonist saves are **alternative histories**, not twelve simultaneous player bosses.

## Verified common chain

1. Official `FINAL` concludes before a separate `SPECIAL_NOVA` emergency encounter. Eliminated pilots can participate only under independent authorization.
2. The operational threat is Nova's unique functioning composite biological/AI core, its planned expansion and impending escape. No second core or full offsite backup is introduced.
3. A successful, fairly playable fight (where the route explicitly requires a fight) damages executive suppression gateway **G**; technicians isolate the specialized cognitive expansion relay **R** without cutting Kreissack's biological life support.
4. Destruction **D** passes an irreversible point. Nova starts ejecting the unique core **E**.
5. Disabling **G** permits Kreissack's surviving **biological initiation B → hardwired retention latch L**; his own neural command engages the *physical* latch. **He does not need to walk to it, manually grasp it, or gain admin access.**
6. L holds E in the doomed chassis. Nova cannot reverse it in software. The platform and core are destroyed once. Kreissack says **“Apparently, I can still surprise you.”** Nothing about this retroactively acquits him or authenticates E5 before Day 30.

## Cross-POV comparison

All 12 active finale scenes were read, with Ari's two-scene finale considered one continuous episode. See `DAY13_POV_ACCESS_MATRIX_v3.4.csv` for source-local evidence and *open*, unverified access fields. A stated room in an editorial script is not by itself a documented route into that room. Locations such as 'core platform', 'machine chamber', and 'research arena' **may** be distinct zones of the same containment facility, but the current scripts do not establish that equivalence. No new layout is asserted here.

**Statuses:** `ACCESS_PARTIAL` = entry/exit/authorization incomplete even where combat role is clear; `ROLE_UNCLEAR` = contribution or fighter assignment unclear; `BRANCH_CONFLICT` = explicit branch incompatible with blanket rule; none of these implies that the canonical physical sequence is contradictory.

## Confirmed findings and disposition

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| D13-01 | Medium | Milano's finale says Kreissack 'physically operates' the latch, while the detailed Ari sequence and specialist routes specify neural initiation of a hardwired physical interlock. | **Corrected active Milano wording** to biological initiation; no scene result changed. |
| D13-02 | Low | Dante's finale calls this the same event as in 'other nine campaigns', despite twelve selectable pilots. | **Corrected active Dante wording** to 'other eleven campaigns'. |
| D13-03 | High | Raven's vetted-access branch allows a map contribution without fighting. Several route/scaffold rules presume all selected pilots win `SPECIAL_NOVA`. | **Resolved (v5.3): Option B ratified as canon.** Active Raven R6.3 and `finale_flow.py`'s `route()`/`validate_event_sequence()` already implemented this identically (cleared → player boss; denied → `RAVEN_CONTAINMENT`, explicitly barred from G-credit) before this was formally ratified — this closes a documentation gap, not a code or prose gap. Raven's noncombat path is canon; do not silently force him into combat or erase his accountability gate. |
| D13-04 | High | Selene says another pilot damages G but also that the selected player contributes through combat. Dante's role similarly lacks an explicit mandatory-boss description. | **Resolved for Selene and Dante (confirmed fixed in active text, not newly edited here):** Selene's active v0.5 text ("Selene must execute the player-controlled strike that damages G... cannot be credited to an unnamed other playable protagonist") and Dante's active v0.7 text ("the player strikes the exposed G housing, which damages the gateway") are both already fully explicit. This table's own citation of these filenames had gone stale relative to their current content; `DAY13_POV_ACCESS_MATRIX_v3.4.csv` has been regenerated to match. **Steffan's previously-compressed staging (ST6.3) is fixed separately in v5.3** — see D13-09. |
| D13-05 | High | No source establishes a shared named clearance authority, map of zones, and qualified deployment route for each playable pilot. | **Resolved (v5.4).** Clearance authority: ratified as deliberately **impersonal** — "an independent emergency safety review," never a named office or person; this was already the implicit pattern in every campaign's text, now made explicit canon rather than an open gap. Zone adjacency: ratified as a **hub with no pilot/technician overlap** — Z1 connects to Z0 and Z4 by corridor, and to Z2/Z3 only by data/command lines, never a walkable door; technicians are never physically in the chassis room. Neither ratification required any screenplay edit. See `DAY13_ACCESS_AND_BRANCHING_v3.5.md`'s updated authorization-chain section for the full statement. |
| D13-06 | Medium | Technical cast support (Ari/Angel/Ren/Plug/Crystal/Mara etc.) is described differently between POVs. | **Resolved (v5.4).** Ratified: Angel/Ren/Plug are the default technical trio when not playing; Crystal (investigation/comms), Mara (worker-safety/labor-liaison) and Ari (HAR-deployment support) take their own specialty when not playing — matching what the active text already does in practice. Alongside the roster, three testable constraints are adopted: (i) hands-on hardware action is always Plug's/an unnamed technician's unless that pilot is the one playing; (ii) no two campaigns may claim the same named non-selected pilot performed two different, mutually exclusive physical actions in the same scene; (iii) G-credit is never silently reassigned off the selected pilot. (iii) is now a real regression test — see `test_support_cast_canon_v54.py`. |
| D13-07 | Medium | Background IDs and provisional sluglines differ for potentially adjacent spaces and shutdown phases. | **Open** until facility zone map and production registry harmonization. |
| D13-08 | Medium | Evacuation and blast seals are detailed in Ari but abbreviated or absent in other POVs. | **Open**; use Ari's detailed sequence as a *reference*, not automatic canonization of every room or support actor. |
| D13-09 | Medium | Steffan's ST6.3 described him contributing "timing and fire-control skill to protect the technicians" without ever stating that *his* action is what damages G — the one campaign where this stayed genuinely ambiguous after D13-04's Selene/Dante fixes. | **Resolved (v5.3).** Active Steffan v0.7 text now states explicitly: Pyros's player-directed fire-control lock damages G; the technicians his corridor protects are the ones who isolate R, not credited with damaging G themselves. Appended to the existing ST6.3 paragraph with no line-number shift (guardrail below). |

**v5.3 regeneration note:** This table and `DAY13_POV_ACCESS_MATRIX_v3.4.csv` were checked against the screenplay files actually active per `00_README/CURRENT_RELEASE.md` as of this pass, rather than trusted from the table's own prior text. D13-01's and D13-02's dispositions below were independently re-verified and still hold.

## Proposed spatial model — editorial, not canon

- **Z0: staging/security checkpoint** — identity, safety vetting, emergency authorization, pilot equipment certification.
- **Z1: remote diagnostic/relay control** — remote evidence validation and independent R isolation; must have isolated command/data paths.
- **Z2: research combat enclosure** — Nova chassis and selected playable pilot, separate from championship arena.
- **Z3: core/retention subsystem** — unique E, latch L, destruction D; may be physically within Z2, but needs a maintained controlled boundary.
- **Z4: safe evacuation and protected observation** — shutter, blast door, evacuation route and accountability witnesses.

This model is a **proposal** for harmonizing already-written room descriptions. It must not be treated as a discovered existing facility plan.

## Minimal event timeline to script and test

| Order | Event | Necessary preconditions | What must NOT happen |
|---|---|---|---|
| 1 | `FINAL_COMPLETE` | Official bracket completed | Boss changes trophy standings |
| 2 | `EMERGENCY_AUTHORIZED` | Independent safety authority and chosen route | Corporate/pilot fame grants automatic clearance |
| 3 | `SPECIAL_NOVA_ENGAGEMENT` | Fair and reachable mechanics for selected pilot OR explicit approved noncombat exception | Two simultaneous protagonist-exclusive boss victories |
| 4 | `G_DAMAGED` | Successful combat/engineering action | NPC-only blow negates a mandatory player fight without explanation |
| 5 | `R_ISOLATED` | Qualified technicians maintain life support | Isolation kills Kreissack before his last choice |
| 6 | `D_IRREVERSIBLE` | Containment threatened | Last-minute software override cancels the crisis |
| 7 | `E_EJECTION_STARTED` | Core unique and attached to platform | Offsite duplicate retcon |
| 8 | `B_L_ENGAGED` | G suppression damaged; Kreissack independently acts | Player commands Kreissack to consent |
| 9 | `CORE_DESTROYED` | L engaged, D irreversible | Additional physical sacrifice or surviving full backup |
| 10 | `ESCAPE_AND_ACCOUNTABILITY` | Safe perimeter/shutters; separately retained evidence | E5 Day-30 revelation moved into Day 13 |

**Important:** the ordering of `G_DAMAGED` versus `R_ISOLATED` is not uniformly exact in prose; both must occur before Kreissack's unsuppressed latch decision, but scripts should not claim a universal strict order unless approved. The numbered order above is a **suggested implementation sequence**, not a newly settled canonical ordering.

## Suggested decisions (status as of v5.3)

1. ~~**Boss mode for Raven**~~ **Decided (v5.3): Option B**, matching the recommendation below. Raven has a genuine noncombat investigative variant (`RAVEN_CONTAINMENT`) with a mechanically substantive containment sequence, never credited with damaging G. (A) every pilot plays the boss, with Raven's vetted clearance always earned via an alternate lawful path; (C) if barred, player controls a temporary authorized fighter — both considered and not adopted.
2. ~~**Dante and Selene action ownership**~~ **Already resolved in active text**, confirmed in this pass: both require a playable boss with protagonist-controlled combat, with specialist allies retaining nonexclusive engineering actions; exactly which protagonist action damages G is explicit in each save. **Steffan** (not originally listed here) needed the identical fix; also done, v5.3.
3. ~~**Facility map and access**~~ **Decided (v5.4).** Z0–Z4 approved as coarse zones, hub topology (Z1 ↔ Z0/Z4 by corridor, Z1 ↔ Z2/Z3 by data/command lines only), clearance authority deliberately impersonal. See D13-05 above. With D13-06 also resolved this same pass, there is no remaining pack-wide load-bearing open decision from this table; `test_scene_inventory_source_lines` / D13-07 / D13-08 remain open but are scoped to individual background-registry/evacuation-detail items, not the whole pack.

## Guardrails for subsequent screenplay edits

Only modify active screenplay versions listed by `00_README/CURRENT_RELEASE.md`. Source path + scene ID are essential: Ari's `SCENE10` repeats in different chapters. Preserve all current release metadata and source inventories; any text edits after a source heading preserve its inventory line reference, but re-run all tests and regenerate counts/manifest when changes shift line numbers.
