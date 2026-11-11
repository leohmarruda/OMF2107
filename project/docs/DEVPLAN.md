# OMF2107 development plan: OMF combat in real 3D, with a career layer, two looks

Status: proposed 2026-11-05, merged with the former `ROADMAP.md` on 2026-11-06, **redirected 2026-11-07** to the
Reimagined design (see "Direction change" below). **This is the single plan.** Where it disagrees with another doc,
this one wins. All dates are estimates for planning, assuming one main developer working with Claude, and are least
reliable beyond Phase 3. Phase starts count from Monday 2026-11-09. Update this file at the end of each phase.

**Rebrand (2026-11-10):** the project is being fully rebranded, provisionally as **Steel Skin 2100** (see "Rebrand"
below and [REBRAND_CHECKLIST.md](REBRAND_CHECKLIST.md)). This plan keeps the old names (OMF2107, the HAR and pilot
names) until the sweep (R22) reaches it.

## Direction change (2026-11-07)

OMF2107 is no longer a strictly faithful rendition. It becomes a **single-player fighting game with a career layer**,
built on the Reimagined design pitch v0.3 (now archived; its rules still in force are in the spec and here) and keeping One Must Fall 2097's
combat as its foundation. Decisions taken:

| Decision | Detail |
| --- | --- |
| Foundation first | The M2 parity gate stays. Jaguar and Shadow must match the OpenOMF measurements on `fightcore` before any new mechanic changes match rules. New mechanics are deltas on that baseline. |
| Three modes | Story, Tournament and Arcade. Training stays as a support tool. Local Versus moves to "Later decisions". |
| Combat resource | **Stun only**, as in the original. No heat, overclock, rage or desperation meter (#7 and #27 rejected). |
| Story rules | Story fights use the `classic` ruleset: no economy, no upgrades, no localized damage. Story keeps its own fail-forward (a loss either changes the route or ends in a game-over ending, depending on chapter and state). |
| Tournament rules | `career` ruleset: localized damage, repair economy, upgrades. **Persistent career (Model A):** money, owned HARs, upgrades and unrepaired damage carry between events. **Insolvency is game over** (decided 2026-11-07), using the original rule: the career ends when money is still negative after two consecutive matches. Sponsors and other resources are the way out before that point. |
| Arcade rules | `classic` plus the existing stacking tune-ups (decided 2026-11-07). No region damage and no economy in Arcade. |
| Engine | The 3D engine must carry the new features at 60 fps on the minimum PC. See "3D engine requirements". |

## Rebrand (2026-11-10)

Research into the rights ([RIGHTS.md](RIGHTS.md), sources in `rights_sources/`) found no primary licence beyond Rob
Elam's 1999 freeware post, which covers distributing copies of the game only. Statements on modification are second-hand
and the OpenOMF Discord gave no legal clarity (replies logged 2026-11-10). Decision: **full rebrand and credit**, the
safest course, with a free-only, no-monetization release and a takedown plan.

| Decision | Detail |
| --- | --- |
| Title | Provisionally **Steel Skin 2100**; clearance pending (checklist D1). Needs a code name for targets and the repo. |
| Scope | **All robots (names and designs), characters, sounds and music will be replaced, eventually** (decided 2026-11-10; checklist D2, D3, D3a). Lore terms are open (D4). Original robots, characters, sounds and music stay as private development placeholders only and must be gone from every distributed build by M5. Original-derived assets and the original data path leave every distributed build. |
| Kept | OpenOMF's MIT code with its notice, credited; combat parity data (mechanics) per RIGHTS.md rule 4, to confirm (D6). |
| Credit | Credit OpenOMF; acknowledge the original game as inspiration with an unofficial, not-affiliated disclaimer. Credit is courtesy, not permission. |
| Where it lands | Decisions D1 to D7 in M0; code, build and robot renames in Phase 1 (cheapest before content exists); asset replacement with Phases 2 to 4; final old-name scan and notices at M5. Task R22. |
| Engine base | The existing fork stays as it is: no merge of the 71 newer upstream OpenOMF commits for now (decided 2026-11-10). It builds clean in Release (2026-11-10). |

Consequence for the spec: "every mode uses the same match rules" no longer holds. All modes share **move definitions**;
match rules come from a named ruleset, always shown before the fight. Update the spec, `OMF2107_FEATURES.md`,
`OMF2107_CORE_LOOP.md` and `OMF2107_ARCADE_MODE.md` to match (task R14).

## Target

Make **OMF2107** a 3D One Must Fall 2097 whose fights read and feel like the original, wrapped in a career where damage
costs money, rivals remember, and sponsors push. Fighters and arenas gain 3D models, animation, lighting and camera
work while the match stays readable as a side-view fighter. Keep the pilot-plus-HAR selection, directional punch and
kick controls, specials, blocking, stun, combos, hazards, WAR's contest for Ganymede, pilot rivalries and endings.

The story pass expands OMF's own neural-link, WAR, Kreissack and Nova themes. The [story treatment](OMF2107_LORE_v2.md)
develops the government conspiracy, relationships and the physical cost of an experimental link. The
[game specification](OMF2107_GAME_SPEC.md) defines modes, combat rules, presentation, architecture and acceptance
gates (to be updated per R14). The task register below breaks the phases into tasks.

Fixed decisions: [rights and release rules](RIGHTS.md); no original data in a release; real 3D; two visual modes,
**blockout** and **mesh** (decided 2026-11-09; the blockout replaces the earlier "simplified stylised look" and ships as
a finished look), both driven by one rig, one set of keyframes and one gameplay proxy (see "HAR production pipeline")
([engine paths](ENGINE_PATHS.md)); one source per HAR ([HAR pipeline](HAR_PIPELINE.md)). The engine base is option A:
a standalone `fightcore` with a project data pack, linked in-process.

## Feature selection from the Reimagined pitch

Numbers are the proposal IDs of the [archived pitch](_archive/omf-reimagined-design-pitch-v0.3.md), kept for traceability.
Design rules still in force from it live in the spec: AI (§4.4), readability (§5), economy, sponsors, rivals and
reputation (§7), accessibility (§8).

| Tier | Features | Lands in |
| --- | --- | --- |
| Foundation | #11 fixed HAR signatures and physics-fidelity baseline | M2 (parity) |
| Core 1 | #1 three-state localized damage; #2 repair, preparation and insurance economy (Model A); #3 fail-forward in Tournament; #22 damage visuals (part of #1's presentation); a minimal form of #10, sponsor support offers, because sponsors are the main resource against insolvency | M3 career core |
| Core 2 | #5 personality AI with bounded rule-based adaptation; #4 rivals that remember (= D06); #10 full sponsors with agendas and demands; #16 contract conditions; #17 circuit rankings | M6, Tournament |
| Adopted 2026-11-09 | #13 limb targeting, through height-based region mapping (no new input); pre-match scouting of the opponent's region damage; destruction finishers gated by condition (see "Finishers"); one personality profile per opponent before M4 (R10a) | M3 to M4 |
| Selective | #24 broadcast and public reputation; #24a spectator hype | Decide after the M3 playtest |
| Deferred | #6 hybrid tournament simulation; #8 three-axis relationships; #15 new arena engineering; #19 illicit technology as items; #20 modular parts beyond the upgrade list; #24b native affinity | Post-release or never |
| Rejected | #7 heat and overclock (stun only); #24c jury-rigged repair (retired 2026-11-07); #14 emergency power rerouting (2026-11-09: needs new input and UI without heat, small gain); #25 learned Shadow AI; #27 desperation window; #29 transformation; #30 neural stress penalties; #31 persistent injury roster | Not planned |

No comeback mechanic is planned: it would reintroduce the rage or desperation meter rejected above.

## Rulesets

`fightcore` reads a ruleset from the data pack. Move definitions are shared; rulesets only switch systems on or off and
set their numbers.

| Ruleset | Used by | Contents |
| --- | --- | --- |
| `classic` | Story; Arcade; dev comparison against OpenOMF | OpenOMF-parity rules. Health, stun, rounds, hazards. Arcade adds its tune-up multipliers (HP, damage dealt, walk speed) as disclosed pre-match conditions; Story adds nothing. |
| `career` | Tournament | `classic` plus per-region condition, region effects, carried damage, pre-match upgrades and repairs |

Rules for the `career` layer:

- Match health and stun behave as in `classic`. Region condition is a second, separate layer.
- **Four regions** (arms, legs, torso, head), three states each (Operational, Damaged, Critical). The original
  "specials" region is folded into the torso: it had no hit location and its proposed effect depended on heat.
- Effects are numeric, deterministic, centred on stun, shown in the HUD and pre-match screen. **No move is ever
  removed**, so every HAR keeps its full signature set (design pillar 1). Starting values, to be tuned in playtest:

  | Region | Damaged | Critical | Existing hook |
  | --- | --- | --- | --- |
  | Arms | Punches deal -10% damage | -20% | Damage-dealt multiplier (as Arcade `power`, `har.c`) |
  | Legs | Walk speed -10%; jump unchanged, so combos and juggles keep working | -20% | Walk-speed multiplier (as Arcade `speed`) |
  | Torso | Takes +10% damage | +20% | HP or damage-taken multiplier (as Arcade `armor`) |
  | Head | Own stun lasts slightly longer | Clearly longer | New code |

- Hits are assigned to regions by hit height from data the match already produces (`hit=side,height,damage`): low
  hits go to legs, high hits to head and arms, mid hits to torso. This gives limb targeting (#13) without a new input.
  The mapping is authored data, not mesh contact.
- **Region damage carries between rounds of the same match** (so the last round differs from the first) and between
  matches until repaired (decided 2026-11-09).
- **Scouting:** the pre-match screen shows the opponent's region states, so the economy feeds HAR and tactic choice.
- Region state lives in the simulation, is part of replays (inputs, version and ruleset ID), and is the authority.
  Presentation only reads it.
- Not changed in any ruleset: input buffer, frame data, hitboxes and jump arcs. These are what parity measures.

## Finishers (decided 2026-11-09)

Destruction finishers exist only in the **last round** of a match, and only when the **finishing HAR is in good
condition**. Otherwise the match ends with the normal finish.

| Ruleset | "Good condition" (proposed, to tune) |
| --- | --- |
| `career` | No region in Critical, and the limb the destruction move uses (arms or legs) Operational |
| `classic` | **Decided 2026-11-09:** the finisher has won every round of the match without losing one, and ended each of them with health at or above 50% (in the last round, at the moment of the finish). In the default best of three this means a 2-0 with at least 50% in both rounds |

- The gate is a deliberate, documented change from the original rules (spec §4.3). In `classic` it is applied only
  after the M2 parity gate passes, behind a ruleset flag that the dev comparison mode switches off. The original's
  own finisher conditions must be confirmed in the OpenOMF code first (R15).
- The HUD shows when a destruction finisher is available. The AI obeys the same gate, and when the AI destroys the
  player's HAR, the player sees the full sequence (decided 2026-11-09).
- Tournament: a destruction earns a disclosed payout and reputation bonus and a rival-memory tag. Being destroyed adds
  **no extra carried damage**: a loss is already the penalty, and more would feed the Model A spiral.
- Presentation: one in-engine destruction sequence per HAR in both looks, using swap parts and the free camera after
  player control ends. This is real content cost per HAR; Phase 5 measures it with the rest of the HAR work.

## Where development stands today

The `project/prototype` viewer renders the match in 3D (Jaguar, Shadow and Katana) and plays Ari's story route and an
Arcade ladder. Until M2 it runs on OpenOMF as the mechanical reference, as decided on 2026-10-15:

- OMF2107 does not get a new combat engine during the parity work. Every fight runs on OpenOMF's reverse-engineered
  rules with the original AF and BK data, and the 3D view only renders the per-tick state it publishes. The prototype's
  own combat loop is a `--sandbox`-only placeholder.
- Until M2, gameplay must not be changed to make an effect visible. Shadow's shadow attacks (Shadow Punch, AF move 23)
  only have a script at enhancement level 3, exactly as in the original Tournament, so the live launchers expose that
  as an explicit `-ShadowEnhancement 3` option. From M3 on, rule changes are allowed only inside the `career` ruleset, with one exception: the `classic` finisher flag (R15).
- This is a development baseline only. The release path replaces it with `fightcore` and an authored data pack
  (Phases 1 and 2), keeping the OpenOMF link as a dev-only comparison mode for the `classic` ruleset.
- [OMF 2097 Remastered](https://github.com/Jared-woodruff/OMF-2097-Remastered) (local sibling
  `../OMF-2097-Remastered`) was reviewed as an alternative. It is a function-by-function TypeScript port of OpenOMF
  with determinism tests, but has no parity tests against OpenOMF, no per-tick state export and no 3D renderer. It is a
  reference only (optional Spike B).

Done before M0 (the old Stages 0 to 2 and the start of 4):

- **Baseline:** range, timing and guard checks cover all 35 Jaguar and Shadow attacks
  ([OMF2107_MOVE_MEASUREMENTS.md](OMF2107_MOVE_MEASUREMENTS.md)); signature traces, Stadium wall response and a
  replayable source-driven match are recorded.
- **Match review:** the playable Stadium match was compared with the
  [recorded model match review](OMF2107_MODEL_MATCH_REVIEW.md) on 2026-10-27 (facing, hit timing, recovery) and judged
  good with both the blockout and Meshy models. Body overlap during kicks, falls, crossings and throws is accepted
  because OpenOMF has no body collision. Gate closed 2026-10-27. Carried over as polish: the eased facing turn in
  Shadow's close throw needs a live look, the Jaguar concussion shot was reviewed by screenshot only, Shadow's purple
  figures have no trails (no renderer transparency; now tracked as R05), and skinned deformation rigs wait for the
  asset pass.
- **Staging:** the Stadium has an enclosed bowl, stepped crowd stands and a central board. The blockout launcher
  (`run-blockout.ps1`; `run-meshy.ps1 -Fight` for Meshy stand-ins) opens a selection screen connecting ten playable
  pilots to Jaguar, Shadow or Katana, using their OpenOMF stats.
- **Story (2026-11-06):** `project/data/story/ari.story` holds Chapters 1 to 6 of the Story Pack (266 scenes, including
  the skippable optional scenes) with the Group A, bracket and championship branches and a two-fight Nova boss. It
  passes `story_check`, and `story_check walk` reaches the ending every time. Every character shown with `present` has
  a project-made render (Nova has none by design), and the viewer no longer reads the original-game portraits. The 14
  fanservice frames are wired in, with a solo epilogue `ch6_e4`. The seven NPC results are decided. Ari's sister is
  Norah (decided 2026-11-07). Still open: a live playtest of the route (`run-story-ari.ps1`), the last trim of the short
  main route (about 41 minutes with every fight won against 25 to 35; see `data/story/ari.tiers`), and the older
  Crystal-story and news frames, which still use original portraits. Story stays on the `classic` ruleset, so the
  route needs no rework for the direction change. Scope and open decisions are in
  [OMF2107_STAGE4_PLAN.md](OMF2107_STAGE4_PLAN.md).
- **Arcade (2026-11-07):** randomized five-rung ladder plus Nova, lives by difficulty mode, stacking tune-ups, newscast
  replay and hangar scratches drawn from the fight's `hit=` lines. Passes `story_check`; not yet played end to end. See
  [OMF2107_ARCADE_MODE.md](OMF2107_ARCADE_MODE.md). The hangar scratch masks are the first piece of the damage
  presentation pipeline (R04).
- **Pose and mesh authoring:** mesh landmarks (`project/data/mesh_landmarks.json`) and projection-pose matching
  (`match_projection_poses.py`) feed the pose catalog; see [POSE_AUTHORING.md](POSE_AUTHORING.md).

## 3D engine requirements

The engine must carry the career features at the same frame rate as the plain match. Budgets below are **proposed
starting values**; Spike C confirms or replaces them, and the minimum PC profile is fixed at M3.

| Area | Requirement |
| --- | --- |
| Frame rate | 60 fps presentation at the minimum PC in both looks. Gate on frame times over a scripted worst-case match: p99 at most 16.7 ms, median at most 12 ms (headroom for the HUD and effects). |
| Simulation | Fixed 60 Hz tick. `fightcore` including region damage at most 1 ms per tick on the minimum PC. Rendering never stalls the tick. |
| Damage state display | 4 regions x 3 states per HAR, driven by simulation events. Done with packed region masks and material parameters (extending the hangar's `maintenance_<har>` masks), plus pre-authored swap parts for Critical (dented or missing plates). No runtime mesh cutting or deformation. |
| No mid-match hitches | Every damage variant, swap part, decal and effect is loaded and warmed at match start. Zero allocations and zero file reads on a state change. |
| Gameplay separation | Damage visuals never change hurtboxes or hitboxes. Swap parts do not alter the silhouette enough to hide a startup tell (spec §5 readability rules). |
| Transparency | A sorted alpha-blended pass for sparks, smoke, electrical arcs and Shadow's trails. The renderer has none today (R05). |
| Particles | Pooled and instanced, with a hard cap (start at 2,000 live particles), and a reduced-effects setting that lowers it. |
| Two looks | Blockout and mesh share one skeleton and one set of keyframes; only geometry and materials differ. Both show all three states per region. A HAR is not done until both pass `har_check` at stage H5. |
| Rig | `rig.json` holds region IDs, contact, ground, swap and emitter sockets and optional appendage chains, so damage and collisions are authored once per HAR. |
| Solid contact | The solid-contact layer (R18) runs after animation and before skinning, on capsule and box proxies; at most 0.5 ms per frame for both HARs. |
| Appendages | Cosmetic secondary motion is deterministic per tick and budgeted with the particles; it never runs a variable-step physics solver. |
| Determinism | Replays reproduce region states exactly; presentation can be skipped (headless) with identical results. |
| Measurement | A frame-time capture tool and a scripted worst-case match (both HARs Critical in several regions, maximum particles, both looks), run at each milestone. |

Engine choice: option A (C11, SDL2, OpenGL 3) stays. Spike C tests whether this renderer meets the table. If it
does not, the fallback allowed by the spec (§9, step 4) applies: keep `fightcore` and the data pack, and move only the
presentation layer to a dedicated 3D toolchain. That decision is taken at M1, before content production.

## HAR production pipeline (anti-rework, decided 2026-11-09)

Goal: both looks free of defects, with correct body coordinates and collisions, for every HAR including those with
non-humanoid limbs (tail, wings, flails, thrusters, extra arms), without redoing models or animation. Three rules:

1. **One source of truth per HAR, data flows one way.** Nothing downstream is edited by hand.
2. **Cheap layers freeze before expensive ones start.** No mesh before the animation is frozen on the blockout; no
   damage parts before the mesh is accepted.
3. **Every stage has an automated check** (`har_check`); a HAR does not move on until it passes.

### Source chain

| Layer | Source | Derived from it |
| --- | --- | --- |
| Rig | `rig.json` per HAR family, one shared schema: units, origin, axes (-z toward the opponent, +y up, root on the floor at the origin), joint hierarchy, rest pose, joint limits, contact, ground, swap and emitter sockets, region IDs, optional appendage chains. `har.json` per HAR: proportions, part parameters, appendage parameters, visual variants | Blockout, skinning targets, checks |
| Move timing | `fightcore` data pack: frame timing, damage, stun and move rules, from the measurements | Keyframe timing |
| Animation | Keyframes in rig space, timed by the data pack | Both looks; no per-look animation |
| Blockout | **Generated** from `rig.json` plus `har.json`, never hand-modelled | Envelope that the mesh must fit; collision masks |
| Collision | Hit and hurt masks **generated from the posed blockout** per frame at build time, cached, stored in the data pack | The only gameplay collision, in every look. Validated against the measurements (parity) |
| Mesh | Modelled (or a cleared Meshy source), conformed to the blockout envelope and skinned to the same skeleton | Region masks, swap parts |
| Damage | Region IDs from the rig. Blockout: procedural per-region tint and crack shader, nothing authored. Mesh: packed masks and swap parts | Destruction sequence |

Generated files (`*.gltf`, masks, blockouts) are build outputs. CI regenerates them and fails if a committed copy
differs, which stops the `jaguar-rigged.gltf` drift found on 2026-11-06 from recurring (R19).

### Body coordinates and collisions

- Gameplay collisions come from masks generated from the posed blockout (HAR_PIPELINE rule 6), so in the blockout look
  the visual and the collision agree by construction. The mesh never feeds collision: it must stay inside the blockout
  silhouette per pose within a tolerance set in P1, and the striking contact socket (fist, foot, tail tip, weapon) must
  lie inside the active hit mask on every active frame. `har_check` tests this per frame, per move, in both looks.
- Because collision follows the keyframes, a keyframe edit changes gameplay. That is why keyframes freeze at H3 and any
  later edit re-runs parity.
- Ground contact: feet (or the declared ground sockets) touch the floor plane in idle, walk and landing frames, with
  no sinking or floating beyond tolerance.
- Facing: the side flip mirrors the rig around the fight plane without changing contact socket positions relative to
  the hitboxes.
- **No limb passes through a solid in 3D (decided 2026-11-09).** OpenOMF has no body collision, and a gameplay
  pushbox would change spacing, corners, cross-ups and throws, so the simulation is left as it is. A **solid-contact
  layer** in the viewer corrects what is drawn, in every mode (R18). Order of resolution each frame:
  1. Each HAR carries simple collision proxies, capsules and boxes generated from its blockout parts (one per bone,
     appendages included). The same proxies serve both looks, because the mesh stays inside the blockout.
  2. **HAR against HAR:** when proxies of the two HARs overlap, the viewer moves them apart in depth (off the fight
     plane) and, if that is not enough, eases one back along the plane, by the smallest amount that clears the
     overlap, blended over a few frames so nothing pops.
  3. **Limb against body:** a limb that would still enter the other HAR is bent by IK to stop at the surface. On a hit
     frame the striking contact socket is placed on the opponent's surface, so a punch lands on the armour instead of
     sinking in.
  4. **Arena:** feet are planted on the floor by IK; limbs and appendages stop at walls and the floor during wall
     slams, falls and knockdowns.
  5. **Self:** prevented at authoring time (H3 and H4 checks); the runtime layer also pushes a limb out of its own
     body if a blend between clips causes a pass-through.
- The layer never changes the simulation, collision masks, hits or timing, so replays and parity are unaffected. Visual
  offsets are capped (limit set in P1) so a landed hit never looks like a miss.
- Acceptance: a replay suite plays every move of every HAR against every HAR and in every arena, and measures
  penetration depth per frame; it fails above the tolerance. Budget: at most 0.5 ms per frame for both HARs on the
  minimum PC.
- Self-intersection: no limb passes through the body beyond tolerance in any frame, including extreme poses and
  throws.

### Non-humanoid limbs

- The schema has core chains with fixed names (spine, head, two arms, two legs) so IK, landmarks and pose tools work
  on every HAR, plus **optional appendage chains declared by type**: tail, wing, flail or chain, thruster, extra arm,
  weapon mount. Each declares segment count, joint limits, attach bone, region and behaviour.
- Behaviour is one of two kinds. **Gameplay appendage:** if it can hit or be hit, its strikes are authored moves with a
  contact socket, and it is included in mask generation. **Cosmetic appendage:** secondary motion only, computed deterministically
  from the tick (no variable-step physics), so replays look identical; it is excluded from masks and never affects collision.
- Damage: each appendage belongs to the region of its attach bone unless the rig says otherwise (a tail usually maps
  to legs, wings to the torso).
- Which HARs need which appendages is confirmed from the original reference during the schema stress test (R16), not
  guessed.

### Damage parts (decided 2026-11-09)

Each HAR's armour is split into a **structural frame** (always present) and **armour plates** on top of it, declared
per region in `har.json`. Damage is shown by changing the plates, never the frame, so a missing plate always reveals
machinery, never a hole.

| State | What changes | Blockout look (generated) | Mesh look (authored) |
| --- | --- | --- | --- |
| Operational | Nothing | Clean | Clean |
| Damaged | Surface only: scratches, scorch, small dents; occasional sparks at the region socket | Procedural shader: per-region tint and crack lines | Packed mask channels (scratches, scorch, dent normals) |
| Critical | Geometry: one or two plates per region dented or gone, frame exposed; smoke and sparks | Generator splits each part into frame plus a plate shell and bakes a dented and a removed variant | Plates modelled as separate meshes on swap sockets, each with a dented variant (or a dent normal map) and an inner frame part beneath |
| Patched (Tournament) | A Critical plate replaced by a welded, unpainted plate: the region is back to Damaged and the player can see it was patched | Plate in a contrasting primer material | Patch-plate variant per region |

Rules:

- **Collision never changes with damage.** Masks and the solid-contact proxies always come from the undamaged
  blockout, so losing a plate never changes reach, hurt area or hits.
- **Readability:** at most two plates per region change state, and the silhouette change stays under a limit set in
  P1, so no damage hides a startup tell.
- **Plates falling off:** when a region enters Critical, its plate detaches as debris. Debris is presentation only:
  trajectory computed from the tick (deterministic, same in replays), lands on the floor through the solid-contact
  layer, never touches gameplay, stays until the round ends, pooled with a cap of 12 pieces per HAR.
- **Destruction finisher:** reuses the same plates and adds limb detachment at the joints; no extra damage assets.
- **Performance:** all variants preloaded and warmed at match start; a state change only toggles visibility and
  material parameters (engine table).
- **Naming:** plates, inner frame parts and patch variants follow a naming convention that the mesh importer (P3)
  checks, so an incomplete HAR fails H5 instead of shipping with a gap.

### Stage gates per HAR

| Stage | Work | Gate (`har_check` plus review) | Freezes |
| --- | --- | --- | --- |
| H1 Rig | Family `rig.json` (or an extension for appendages) and `har.json`, proportions from the reference silhouette and from measured reach | Schema valid; appendages declared with behaviour | Skeleton, proportions |
| H2 Blockout and timing | Generated blockout; move timing in the data pack | Coordinate, ground and facing checks on idle and key poses; silhouette compared with the accepted hand-built blockout where one exists | Blockout parameters, timing |
| H3 Animation and collision | All moves keyframed on the blockout; masks generated | Generated masks reproduce the measured reach, timing and hits within tolerance (parity on `classic`); contact sockets in hit masks; no self-intersection; readability review | Keyframes, masks |
| H4 Mesh | Model, conform to the blockout envelope per bone, skin | Mesh quality (manifold, normals, no degenerate faces, scale, origin, polygon and material budget, LODs); deformation over every frame of every move; all H2 and H3 checks again on the mesh | Mesh |
| H5 Damage and finish | Region masks, swap parts, destruction sequence | All 12 region states in both looks; engine table budgets; no hurtbox or silhouette-tell change | Done |

A change to a frozen layer needs a written change request, and the checks for every later layer are re-run. Batches
overlap: H1 to H3 of the next HAR run while H4 and H5 of the current one are being built.

## Milestones

| Milestone | Target | Gate |
| --- | --- | --- |
| M0 Decisions and spikes | 2026-11-20 | Extraction spike go or no-go; tool audit; Reimagined scope and ruleset note; rights evidence logged and the rebrand decisions D1 to D7 settled, with the title cleared (the permission email is sent only if a contact is found); blockout style brief; rig schema v0 drafted |
| M1 Pipeline, core skeleton, damage-render spike | 2027-01-22 | Code, build and robot renames done under the new code name (R22, checklist sections 1 and 2); rig schema v1 locked after the all-HAR stress test (R16); Jaguar at H2; `har_check` v2 (R17); data pack format and validator with ruleset field; `fightcore` runs a recorded match; Spike C result (renderer go or no-go against the engine table) |
| M2 Data-free classic duel | 2027-03-19 | Jaguar and Shadow at H4: authored data and keyframes, no original file read, parity within tolerance on `classic`, meshes accepted; both looks playable and passing `har_check` |
| M3 Career core | 2027-04-30 | `career` ruleset with region damage, repair ladder and persistent purse; a short Tournament bracket with Jaguar and Shadow; one part upgrade; economy simulation passes; playtest shows varied repair choices and no passive play; frame-time gate passes; minimum PC profile fixed |
| M4 Clean vertical slice | 2027-06-18 | Ari's route on `classic`; Arcade on its chosen ruleset; menus, sound and music all original; build gate passes; outside playtest |
| M5 Public demo | 2027-09-17 | Four HARs with damage states in both looks; Story route, Arcade, short Tournament; options; rebrand sweep complete (final scan finds no old title, robot, pilot or lore name and no original-derived file in the build; NOTICES, credits and disclaimer shipped); takedown plan ready |
| M6 Full roster and career | 2028-01-14 | All ten standard HARs plus Nova as story boss (unlock policy open); full Tournament career with rivals, sponsors and rankings; remaining arenas and routes |
| M7 Release candidate | 2028-03-17 | QA, controller and options polish, performance sweep, packaging, rights review complete |

Compared with the plan of 2026-11-06, the career core adds one phase and moves the release candidate from 2028-01-31 to
2028-03-17 (about six and a half weeks).

## Open decisions

| Decision | Options | Decide by |
| --- | --- | --- |
| Sponsor safety net | Which resources can rescue a pilot near insolvency (sponsor advance, contract with conditions, salvage sale), how often, and at what cost to reputation or freedom | M3 |
| Upgrade model | Original vertical upgrades with a cap (a well-played base HAR can still win); or horizontal options (#18) | M3 |
| Finisher condition in `career` | Keep the region rule alone, or also require the `classic` rule (no round lost, 50% or more) | M3 playtest |
| Selective features | #24, #24a | After the M3 playtest |
| Local Versus | Post-release, or in M5 on `classic` | M5 planning |
| Accessibility assists | Which assists ship (proposed: one-button specials, Story difficulty, non-flashing indicators, no QTEs) and whether assists are allowed in Tournament | M4 |
| Project name | **Decided 2026-11-10: full rebrand and credit** (Discord replies gave no clarity; safest course); task R22 and [REBRAND_CHECKLIST.md](REBRAND_CHECKLIST.md). **Provisional title: Steel Skin 2100** (2026-11-10; checklist D1, clearance pending). Still open: the code name and the scope of robot, pilot and design changes (checklist D2 to D7). Files, build and docs keep the old names until the sweep (R22). Was: keep OMF2107, or rename to OMF2110. Affects the permission email (R13), `RIGHTS.md`, the docs, the build and the art. Renaming does not by itself remove the risk from HAR names and likenesses (see `RIGHTS.md`, "Findings 2026-11-10"): check how much HAR terminology the project keeps. Added 2026-11-09 | Proposed: M0, before the permission email is sent |
| OMF Battlegrounds review | Check OMF Battlegrounds for ideas worth adapting (mechanics, tools, lore elements). Battlegrounds is Rob Elam's and off limits for code, assets, design documents and lore without his agreement (`RIGHTS.md`), so this is a review for inspiration only. Each candidate goes through the rights check and the ledger before use; lore items are checked against `OMF2107_LORE_v2.md`. Added 2026-11-09 | Proposed: M1 (output: a short note listing what to adopt, adapt or skip) |

## Scope boundaries

- **First playable:** one faithful match with pilot and HAR choice, source-like controls and one recognizable arena
  (done on OpenOMF; repeated on `fightcore` at M2).
- **First career slice:** two HARs, region damage, a repair decision with real trade-offs, a persistent purse and a
  short bracket (M3).
- **First story slice:** Ari's route in WAR's Ganymede contest, on `classic`, with original-style banter and an ending.
- **Later decisions:** Local Versus, network play, advanced cinematics, deferred Reimagined features. These follow a
  successful career slice and the rights review.

## Progress

- 2026-11-05: Spike A done (read-only), result **go with conditions**: [SPIKE_A_FINDINGS.md](SPIKE_A_FINDINGS.md). The
  tool audit (P0) first pass is in [HAR_PIPELINE.md](HAR_PIPELINE.md). Still open in Phase 0: permission email and
  simplified style brief. 2026-11-06: `rig.json` written ([robots/rig.json](../robots/rig.json), checked by
  `robots/check_rig.py`); it found that `jaguar-rigged.gltf` is stale against its generator (it has two helmet parts
  the generator no longer makes).
- 2026-11-06: Ari's route scripted end to end (see above). Docs consolidated: this plan replaces `ROADMAP.md`.
- 2026-11-07: Arcade ladder randomized with lives and stacking tune-ups. Direction changed to the Reimagined design
  (see top); milestones re-planned. Same day: Arcade stays on `classic` with tune-ups; Tournament insolvency is game
  over after two consecutive matches with negative money (the original rule), with sponsors as the safety net; jury-rigged repair retired; R14 doc updates done.
- 2026-11-09: HAR pipeline restructured to avoid rework: looks are blockout and mesh; one source chain per HAR;
  stage gates H1 to H5 with freezes; all-HAR rig schema stress test before lock (R16); `har_check` v2 (R17);
  solid-contact layer so no limb passes through a solid (R18); generated-artifact check (R19).
- 2026-11-09: Fight dynamics decided: four regions with stun-centred numeric effects, no move removal, height-based
  region mapping (#13), damage carried between rounds, scouting, rerouting rejected, one AI profile per opponent in
  Phase 4 (R10a), destruction finishers only in the last round and only in good condition (R15).
- 2026-11-09: Reimagined pitch archived; AI, readability, economy, sponsor, rival and accessibility rules moved into
  the spec, which is renamed `OMF2107_GAME_SPEC.md` (R21). Doc sweep against this plan done; R14 and R21 reopened
  for the rest. Open decisions added: project name, Battlegrounds review.
- 2026-11-10: Rights research: Rob Elam's 1999 freeware post found (primary; distribution of copies only), Battlegrounds
  agreement (unsigned copy) and the Epic thread saved in `rights_sources/`. Posted to the OpenOMF Discord; replies gave
  no legal clarity. Decided a full rebrand, provisionally Steel Skin 2100 ([REBRAND_CHECKLIST.md](REBRAND_CHECKLIST.md),
  R22). OpenOMF licence audit: MIT code, permissive dependencies, no copyleft, CC-BY icons. Fork kept as it is (no
  upstream merge); Release build passes, `story_check selftest` passes.

## Phase 0: decisions and spikes (2026-11-09 to 2026-11-20)

| Task | Output |
| --- | --- |
| Rights: the Discord rights export and sources are logged in `RIGHTS.md` and `rights_sources/`; the Discord post of 2026-11-10 got no clarity. Check for a contact for Rob Elam ("Justin") and send at most one short permission message if one turns up (R13); otherwise proceed on the rebrand. No monetization of any kind | Findings logged (done); email only if a contact is found |
| Rebrand decisions D1 to D7 in [REBRAND_CHECKLIST.md](REBRAND_CHECKLIST.md) (R22): clear the title (USPTO, WIPO, Steam, itch.io, domain, repo), pick the code name, decide robot and pilot scope and the setting year | Decisions recorded; title cleared |
| Spike A: read `src/game/` rule code, list what it reads from AF, BK and game state | Done 2026-11-05 |
| Pipeline audit (P0 in `HAR_PIPELINE.md`) | First pass done; finish |
| Reimagined scope and ruleset note (R01): rulesets, which mode uses which, feature tiers | Short note committed; spec update scheduled (R14) |
| Blockout style brief: primitives, bevels, palette per HAR, materials and damage shader, so the blockout ships as a finished look; two reference renders | One-page brief |
| Draft rig schema v0 (P1): units, origin, axes, core chain names, appendage types, sockets, region IDs, tolerances for `har_check` | Draft committed; locked at M1 after R16 |
| Optional Spike B (Remastered harness as reference only) | Notes, only if time allows |

If Spike A had said no-go, the fallback was a rules re-implementation (option D); it said go with conditions.

## Phase 1: pipeline, core skeleton, damage-render spike (2026-11-23 to 2027-01-22, 9 weeks incl. holidays)

Track E (engine): define the data pack format (with a ruleset field) and its validator; lift the rules into
`fightcore`; headless run of a recorded match; a dev-only converter and tick-for-tick parity test against the existing
REC fixtures (output never committed).
Track H (HAR pipeline):
- R16, schema stress test (about two weeks): `rig.json` and generated blockouts for all ten HARs plus Nova, no
  animation and no mesh, including every non-humanoid appendage confirmed from the reference. Lock rig schema v1 only
  when all eleven fit without special cases. This is the main protection against redoing rigs after meshes exist.
- R17, `har_check` v2: coordinate, ground, facing, contact-socket, self-intersection and mesh-quality checks.
- R19: generated-artifact check in CI.
- Jaguar to H2: rig v1, generated blockout, mesh importer and skinning path tested on a throwaway mesh, glTF loaded
  at run time.
Track S (Spike C, about one week): on the Jaguar blockout and on a throwaway Jaguar mesh of production budget, render all 15 region states, swap parts, and a
particle and transparency stress scene in the Stadium; capture frame times; write the go or no-go against the engine
table. Includes the minimal sorted transparency pass (R05).
Track A (art direction): approve the blockout style; apply it in the blockout generator so every HAR inherits it.
Track R (rights): ledger cleanup, malformed rows fixed, replacement checklist converted to tracked tasks.

## Phase 2: data-free classic duel (2027-01-25 to 2027-03-19, 8 weeks)

- Author Jaguar and Shadow move timing from the 35 move measurements; generate their collision masks from the posed
  blockouts (P6); re-run the measurement checks and accept within agreed tolerances (set at the start of the phase).
  This is the `classic` ruleset.
- Jaguar and Shadow through H3 on the blockout first: keyframe authoring with IK, all checks green, parity accepted.
  Only then H4: meshes conformed to the frozen envelopes and skinned, with every check re-run. Region masks wait for
  H5 in Phase 3.
- R18: solid-contact layer (HAR against HAR, limb against body, arena, self) for Jaguar and Shadow, with its replay suite.
- Link `fightcore` in-process in `project/prototype`; remove the shared-memory link and the OpenOMF process for release
  builds (keep a dev-only comparison mode).
- Replace the Stadium and one second arena with original art; blockout look reviewed per HAR and arena.
- Build gate: fails if any shipped file matches the original data.

## Phase 3: career core (2027-03-22 to 2027-04-30, 6 weeks)

- R02 and R03: region damage model and hit-to-region mapping in `fightcore`, behind the `career` ruleset; `classic`
  parity checks must still pass unchanged.
- R04: Jaguar and Shadow to H5 (region masks, swap parts, procedural blockout damage).
- R06 to R08: repair ladder (full repair, standard patch, fight damaged), insurance, persistent purse,
  insolvency game over (negative after two consecutive matches), minimal sponsor support offers (R11a), lower-bracket fallback; a short bracket
  in a minimal Tournament shell.
- R07: economy simulation before the playtest.
- R15 (gate only): destruction-finisher gate in both rulesets.
- R12: frame-time gate on the worst-case match; fix the minimum PC profile.
- Playtest with three to five players, OMF veterans and newcomers. Pass: players choose different repairs for the same
  situation, matches stay enjoyable under damage, no one reports a loss of control, and a player near insolvency sees a
  way out before the career ends. If repair costs make play passive, redesign before any more content.

## Phase 4: clean vertical slice (2027-05-03 to 2027-06-18, 7 weeks)

- Original portraits, backdrops, illustrated frames, menu and battle sounds, music (commission or generate and clear
  terms for each; record in the ledger).
- R10a: one personality profile per opponent for the slice HARs (spec §4.4).
- R20: accessibility assists, after the decision on which ship.
- Arcade live playtest on `classic` with tune-ups; check that stacked tune-ups do not trivialise the Nova fights.
- Rewrite the Crystal versus Christian route (deferred so far), original text, on `classic`.
- Menus, options, key remapping, damage readability in the HUD. Outside playtest by someone who has not seen the build.

## Phase 5: demo roster (2027-06-21 to 2027-09-17, 13 weeks)

Add two HARs per batch through H1 to H5, overlapping batches (H1 to H3 of the next while H4 and H5 of the current are
built). Rigs already exist from R16, so batches start at H2. The old estimate of two to three weeks per HAR is likely
low with damage states and destruction sequences; measure the first HAR of this phase per stage and revise this plan
from the real figures. Controller support, two more arenas, more pilots. Public demo at M5 if the permission answer or
takedown readiness allows.

## Phase 6: full roster and career (2027-09-20 to 2028-01-14, 17 weeks)

Remaining HARs, remaining arenas and hazards, pilot stories and endings, full Tournament career: custom pilot, upgrades,
rankings, named rivals with memory (D06, #4; spec §7 rivals), personality AI with bounded adaptation (R10), sponsors and contracts
(R11), final audio, voice if wanted.

## Phase 7: release candidate (2028-01-17 to 2028-03-17, 9 weeks)

QA across hardware, performance sweep for both looks with the worst-case match, accessibility, localisation if wanted,
crash reporting, installers, final rights review against the ledger, disclaimer in the README, title screen and store
page.

## Task register

The old plan used Phases A to F with task IDs. The IDs stay so earlier notes still resolve; the phases map onto the
milestones above. New tasks for the career layer use R IDs. Priorities: **P0** is needed for the next playable gate or a
safe production decision, **P1** is needed for the complete game, **P2** is an enhancement that can wait. No phase is
done because the code compiles: each gate needs a demonstrated flow, comparison with the baseline where relevant, and a
list of remaining defects. Create one work item per task ID with owner, dependencies, files touched, acceptance
evidence and actual effort.

| Old phase | Now | Old exit gate, in short |
| --- | --- | --- |
| A Baseline (P0) | Done before M0 | Clean build, reference captures, two-HAR move sheet, rights ledger, architecture map |
| B 3D fidelity spike (P0) | Done before M0; gate closed 2026-10-27 | Legible 3D local Stadium match on the fight plane; toolchain decision recorded (option A, see top) |
| C Vertical slice (P0) | M4, with Ari's route as the story segment | Pilot and HAR pick, exchange, fight, recovery, choice, consequence; stable enough to cost a HAR, arena and route |
| D Shared systems (P1) | Phases 3 to 6 | Every mode has a working loop; saves survive a build update; content is added without touching fight code |
| E Content production (P1) | Phases 5 and 6 (M5, M6) | Ten pilots, ten HARs, five arenas, endings, Tournament, all in the coverage matrix |
| F Release candidate (P1) | Phase 7 (M7) | Installable, playable, savable and finishable, with all shipped content cleared |

### Career layer (R tasks)

| ID | Task | Pri | Phase | Acceptance |
| --- | --- | --- | --- | --- |
| R01 | Reimagined scope and ruleset note: `classic` and `career`, mode mapping, feature tiers | P0 | 0 | Committed; no contradiction with this plan |
| R02 | Region damage model: 4 regions, 3 states, carried between rounds and matches, thresholds and effects as data (table in "Rulesets") | P0 | 3 | Every effect has a HUD signal and a counterplay; validator rejects missing entries |
| R03 | Hit-to-region mapping by hit height; pre-match scouting of opponent regions | P0 | 3 | Same inputs give the same regions in replay; testers can predict where damage goes and aim for a region on purpose |
| R04 | (HAR_PIPELINE P10) Damage parts per "Damage parts": frame and plates, generated blockout variants, authored mesh plates with inner frame and patch variants, debris, sparks and smoke, both looks | P0 | 1 (spike), 3 | All 12 region states plus patched; no hole when a plate is removed; masks unchanged across states; meets the engine table; readable at fight-camera distance |
| R05 | Sorted transparency pass in the renderer | P0 | 1 | Sparks, smoke and Shadow's trails draw correctly; frame-time gate holds |
| R06 | Repair ladder, insurance, persistent purse (Model A), insolvency game over | P0 | 3 | Each option shown with cost and effect before buying; all repair choices are sometimes rational in playtest; the HUD warns before a match that could end the career |
| R07 | Career economy simulation (scripted careers across skill levels) | P0 | 3 | Expected net winnings positive at default difficulty; measured chance of game over by insolvency after one or two bad fights, with and without sponsor help; recovery without grinding |
| R08 | Fail-forward in Tournament: lower-bracket and qualifier fallback | P1 | 3 | A routine loss never ends the career on its own; only insolvency does |
| R09 | Arcade ruleset: decided 2026-11-07, `classic` with tune-ups | Done | 0 | Recorded here and in `OMF2107_ARCADE_MODE.md`; live run still open |
| R10a | One personality profile per opponent (aggression, range, risk) on `fightcore`, all modes; in `career` the AI pressures the player's damaged regions and protects its own | P1 | 4 | Profiles recognizable without dialogue; difficulty still changes decision quality only |
| R10 | Bounded adaptation to player habits, on top of R10a | P1 | 6 | Profiles recognizable without dialogue; adaptation beats repetitive habits without input reading; players can counter-adapt |
| R11a | Minimal sponsor support: advance, conditioned contract or salvage buyer offered near insolvency | P0 | 3 | Every pilot near insolvency gets at least one disclosed offer; each offer has a visible cost |
| R11 | Full sponsors and contracts with agendas and a refusal path | P1 | 6 | Each offer changes at least two systems; refusal always available |
| R12 | Frame-time capture tool and scripted worst-case match | P0 | 1, then each milestone | p99 and median recorded per look on the minimum PC |
| R13 | Rewrite the permission request for the new direction | P0 | 0 | Sent; logged in `RIGHTS.md` |
| R16 | (HAR_PIPELINE P9) Rig schema stress test: `rig.json` and generated blockouts for all ten HARs plus Nova, appendages included; lock schema v1 | P0 | 1 | All eleven fit with no special cases; `check_rig` passes |
| R17 | (HAR_PIPELINE P7) `har_check` v2: coordinates, ground contact, facing, contact sockets in hit masks per active frame, generated masks against measurements, self-intersection, mesh quality, deformation | P0 | 1 | Runs headless on both looks; fails on any defect beyond tolerance |
| R18 | (HAR_PIPELINE P12) Solid-contact layer in the viewer: proxies from the blockout, depth separation, IK limb stops, hit-contact placement, foot planting, wall and floor stops | P0 | 2 | Penetration replay suite passes for every move, HAR pair and arena in both looks; at most 0.5 ms per frame; simulation, masks and replays unchanged |
| R19 | (HAR_PIPELINE P11) Generated-artifact check in CI | P0 | 1 | Build fails if a committed generated file differs from regenerated output |
| R15 | Destruction finishers: confirm the original's finisher rules in OpenOMF, implement the last-round and condition gate in both rulesets, HUD indicator, Tournament reward | P1 | 3 (gate), 5 to 6 (sequences per HAR) | Gate never fires outside the last round or below the threshold; AI follows it; `classic` parity checks pass with the flag off |
| R20 | Accessibility assists per spec §8: assist inputs, Story difficulty, readable indicators | P1 | 4 | Assists change input or AI allowance only; ruleset numbers unchanged; tested with newcomers |
| R21 | Archive the Reimagined pitch; move its rules still in force into the spec; rename the spec to `OMF2107_GAME_SPEC.md` | Reopened 2026-11-09 (links and stale spec sections still to fix) | 0 | No doc cites the pitch as a source of rules; no link to the old spec name |
| R22 | Full rebrand: new title, robot, pilot and lore names, replaced assets and data path, notices and credits (checklist in [REBRAND_CHECKLIST.md](REBRAND_CHECKLIST.md)) | P0 for decisions D1 to D7, P1 for the sweep | 0 for decisions; sweep before M5 public demo | Checklist "Done when" met; no old name or original-derived file in a distributed build |
| R14 | Update the spec, `OMF2107_FEATURES.md`, `OMF2107_CORE_LOOP.md`, `OMF2107_ARCADE_MODE.md` | Reopened 2026-11-09 (docs lag the plan) | 0 | No doc contradicts this plan; re-check at M1 |

### Phases A and B (done)

Task-level status was not re-audited. The recorded outcomes are in "Done before M0". Open carry-overs:

| ID | Task | Status |
| --- | --- | --- |
| A02 | Run the source unit tests, record failures apart from 3D work | Open |
| A03 | Reference captures (Jaguar vs Shadow, Stadium plus one hazard arena); a visible human-played reference match | Replayable source-driven match recorded; human-played match open |
| A06 | Asset inventory and provenance ledger | Open, tracked under Rights in Phase 1 |
| A07 | Human playtest protocol with OMF-familiar players | Open; the Phase 3 and Phase 4 playtests reuse it |
| B07 | Fidelity report and prioritized defect list | Match review done 2026-10-27; the live playtest of readability is open |
| B08 | Production toolchain decision | **Decided 2026-10-15**: option A. Presentation layer re-checked by Spike C at M1 |

### Phase C (M4)

| ID | Task | Where it lands |
| --- | --- | --- |
| C01 | Complete Jaguar and Shadow combat: move lists, stun, combos, knockdowns, rounds, timeouts, scrap finish | Phase 2, on `fightcore` and authored data |
| C02 | Original hazard arena with a visible cue and a replayable timing test | Phase 2 (second arena) |
| C03 | Slice-quality models, rigs, animations, effects, HUD, one arena treatment; OMF veterans name the machines unlabelled | Phases 1 to 3 |
| C04 | Pilot selection independent of HAR selection | Done in the selection screen; the story recommends a pairing without locking it |
| C05 | Data-driven scene runner (portraits, dialogue, choices, skip and log); invalid references reported | Done (`story_check`) |
| C06 | Story sequence: pre-fight exchange, match, recovery, evidence choice, consequence; choices persist through save and load | Ari's route built; save persistence and the live playtest open |
| C07 | One polished anime-style sequence and one short in-engine HAR sequence, skippable and replayable | Phase 4 |
| C08 | Combat sound cues, music, dialogue timing, audio controls; block, hit, stun, hazard, region damage and victory distinguishable without the HUD | Phase 4 |
| C09 | End-to-end playtests; frame pacing and input latency on a real target PC | Phase 4 outside playtest |

After the slice, measure real time for one HAR (with damage states), one arena, one character sequence and one route
segment, then forecast the rest and reconcile it with capacity before authoring the full roster.

### Phase D: shared systems (P1)

| ID | Task | Acceptance |
| --- | --- | --- |
| D01 | Versioned schemas for HAR moves and hooks, pilot stats, hazards, rulesets, region damage, dialogue, scene timing, ending flags | Malformed entries fail with useful errors |
| D02 | Versioned saves for story, Tournament (purse, owned HARs, upgrades, carried damage), controls and settings, with migration tests | An older save loads after a schema change or fails safely with a message |
| D03 | Training mode: move list, input history, dummy settings, hitbox, stun and region display, recording playback | A player can practice one special and see why it missed |
| D04 | Arcade ladder (done for Ari); local Versus moved to "Later decisions" | Matches run without entering Story or Tournament |
| D05 | Tournament: pilot creation, budget, owned HARs, ranked events, payouts, repairs, training, upgrades, ranking, all under Model A | One short bracket (M3), then a full career (M6), can be won, spent, saved and continued; every price and stat change shown before purchase |
| D06 | Named rivals with memory; three event templates (ranked bracket, challenge, contract); short rivalry beats | Rival state changes on repeat fights; rank does not need easy-event farming |
| D07 | Settings and accessibility: remap, text scale, subtitles and log, reduced flashes, shake and particles, audio mix, graphics scale, scene skip | Settings persist and work on keyboard and gamepad; all story text stays available |
| D08 | Content checks and a smoke suite for every mode entry and exit, save and load, one representative fight per ruleset | Invalid content is caught before a build is shared |

### Phase E: content rules (P1)

- **Per HAR:** follow stages H1 to H5 ("HAR production pipeline"), then effects and sound, AI tuning, review. Done means every
  source-defining move is represented, has documented inputs and timings, shows in training and AI, works on both
  rulesets, shows all damage states in both looks, passes `har_check` at H5, and no major camera or hitbox ambiguity remains. Nova follows as a
  boss once the normal roster works, with explicit, learnable rules.
- **Per arena:** gameplay bounds and hazard, readable blockout, art and lighting, cue and audio, playtest.
- **Per route:** lock the shared 2097 timeline first, marking proposed additions against original canon. Done means the
  pilot can finish the campaign, every required scene and match has a fallback for any legal HAR, choices are saved and
  reflected later, and a pilot-specific ending plays. Story stays on `classic`. Build reusable portrait poses before
  commissioning unique shots; keep full animation for the opening, key revelations, Nova and a few endings. Romance and
  fanservice stay limited to established adult characters and voluntary scenes.
- **Tournament and audio:** several spending strategies must reach the top rank without repeating low-level fights, and
  the economy simulation (R07) is re-run after every price or reward change. Add voice only after text and timing are
  stable.

### Phase F: release evidence (P1)

| ID | Task | Evidence |
| --- | --- | --- |
| F01 | Full combat regression on both rulesets: input traces, replays, all moves, all hazards, all region states, all pilot stat combinations | No reproducible winner, health or region desync; no unreadable move |
| F02 | Story and Tournament walkthroughs on clean profiles and upgraded saves | Every route ends; purchases, repairs, carried damage, rank and choices persist |
| F03 | Performance and hardware sweep on minimum and recommended PCs with the worst-case match | Frame pacing, input latency and load times measured per look |
| F04 | Accessibility, controller and UX pass with OMF newcomers and veterans | Subtitles, remaps, skip, log and reduced effects work throughout |
| F05 | Content and legal audit; packaging | Ledger complete; only approved data and licensed material ship |
| F06 | Crash and telemetry policy, bug triage, release notes, support plan | A shippable build and a known-issues list |

## Parallel tracks, always on

| Track | Standing rule |
| --- | --- |
| Rights | Every new asset gets a ledger row with origin and terms on the day it enters; nothing from the originals is committed |
| Parity | After any rules or data change, re-run the measurement and replay checks on `classic` |
| Performance | After any renderer, effect or HAR asset change, re-run the worst-case match and record frame times |
| Two looks | A HAR or arena is not done until both looks pass review and `har_check`, damage states included |
| Freeze discipline | No work on a layer whose source is not frozen; changes to frozen layers go through a change request and re-run later checks |
| Docs | Update this plan at each milestone |

## Evidence to keep

| Evidence | Created | Purpose |
| --- | --- | --- |
| Clean build record ([OMF2107_BASELINE.md](OMF2107_BASELINE.md)) | Phase 0 and each release build | Setup quirks cannot mask project failures |
| Original-match reference captures | Baseline; updated only if source settings change | Anchor movement, moves, camera and hazards |
| Input and replay fixtures (with ruleset ID) | Phase 1 on | Reproduce combat changes and regressions |
| Frame-time captures | Phase 1 on, each milestone | Hold the 60 fps target as features land |
| Economy simulation reports | Phase 3 on, after each balance change | Catch spirals and runaway wealth before players do |
| Human playtest notes | Each playable gate | Catch feel, readability and passivity problems headless tests miss |
| Coverage matrix | M4 on | Track each pilot, HAR, damage state, arena, mode, route, move and scene |
| Asset ledger | Always | Separate local reference data from shippable content |
| Decision records | Spikes and scope reviews | Keep the reasons for engine, art, input, ruleset and balance choices |

Automated tests target rules that can regress silently: move legality, collision and damage order, region assignment,
hazard timing, save migration, content references and replay reproduction. A passing self-test does not prove a good
fighting game, so also review captured frames and live play.

## Rights checkpoint

Decision (2026-11-05): free, non-commercial fan project that keeps the name, HARs, pilots and references to the
original, and ships only original assets. **Superseded 2026-11-10:** the name, HARs and pilots are no longer kept; see
"Rebrand". Free-only, original-assets-only and the takedown plan stand. The 2026-11-07 direction change makes OMF2107 a derivative game with new
mechanics rather than a remake, so the permission request must say so (R13). Research, release rules, accepted name
risk, the permission-request draft and the replacement checklist are in [RIGHTS.md](RIGHTS.md). OpenOMF's code is MIT
licensed, but the original game's artwork, audio, text, character designs and name need their own assessment. The
local `OMF2097` folder is a development reference; its presence is not a release license. The
[asset ledger](ASSET_LEDGER.md) holds the asset provenance list. Patent concerns about mechanics are unverified
(spec §12); get advice before shipping a system close to a known patent.

## Biggest risks

| Risk | Effect | Mitigation |
| --- | --- | --- |
| Region damage makes play passive or feels unfair | Career layer fails its purpose | M3 playtest gate before more content; fairness rules in R02; redesign before scaling |
| Model A spiral (poor results lead to worse equipment and more losses), ending in an insolvency game over | Players lose long careers to a bad streak and quit | Economy simulation (R07), repair ladder with cheap options, insurance, sponsor support from M3 (R11a), lower-bracket fallback, a warning before any match that could end the career |
| Two rulesets double balance work | Slower tuning, drift between modes | Shared move data; `career` only adds systems on top; parity checks run on `classic` after every change |
| C renderer cannot meet the frame budget with damage effects | Late engine change | Spike C at M1, before content; fallback is moving presentation only |
| Damage states raise per-HAR cost | Roster dates slip | Measure the first HAR of Phase 5; packed masks and few swap parts; `har_check` automation |
| Spike A finds the rules tied to AF structures | M1 slips about six weeks | Option D fallback (Spike A said go with conditions) |
| No answer from the rights holders (no contact found; Discord gave no clarity) | Public release stays risky | Full rebrand (R22), keep the project free with no monetization, takedown plan, credits and disclaimer |
| The provisional title is not cleared, or collides with an existing mark | A second rename, wasted sweep | Clear the title (checklist D1) before Phase 1 renames; keep the code name separate from the title |
| Replacement robots and characters are built after the originals | Meshes, keyframes and data authored twice | Author the M2 data pack and H4 art for the replacement robots, not Jaguar and Shadow; use the originals only for private parity measurement; original concept art, not original sprites, as the source for redesigns |
| The rebrand sweep is large (hundreds of files, the Story Pack, art tools) | Phase 1 and the demo slip | Rename code and build first, in small commits; archive or drop Story Pack files instead of rewriting all of them; final scan at M5 |
| Authored data does not feel like the original | Parity rework in Phase 2 | Agree tolerances first; keep the dev-only comparison mode |
| Two looks double the art work | Roster dates slip | Blockout generated from the rig, not modelled; one skeleton and one set of keyframes for both looks |
| Rig schema changes after meshes exist | Meshes, skinning and keyframes redone | All-HAR schema stress test (R16) before lock; freeze gates H1 to H5 |
| Non-humanoid limbs break collisions or replays | Unfair hits, desyncs | Gameplay appendages are included in the generated masks; cosmetic ones are deterministic per tick and never touch hitboxes |
| Visual and gameplay collisions disagree | Hits look like misses or ghosts | Contact-socket checks per active frame in both looks (R17) |
| Single developer capacity | All dates slip | Re-plan at each milestone; M3 (career core) and M5 (demo) are safe stopping points |
| Free camera or 3D rotation makes inputs feel wrong | Crossovers and corner fights confuse playtesters | Locked fight plane and facing rule; cinematic camera only in noninteractive moments |
| Damage visuals hide startup tells or silhouettes | Fights become hard to read | Readability review per HAR with damage states on; reduced-effects setting |
| Ten HARs and ten routes exceed capacity | Measured throughput exceeds available time | Re-plan batches from real costs; make any scope cut explicit |
| Story scenes interrupt match rhythm | Frequent skipping between fights | Short routine scenes, all skippable, a log, animation only for major turns |
| Local build works on one machine only | A clean build cannot be reproduced | Stabilise the toolchain and build script first; test a second machine at each gate |

## Next three actions

1. Settle the rebrand decisions (R22, checklist D1 to D7): clear Steel Skin 2100, pick the code name, decide robot and
   pilot scope and the setting year.
2. Write the Reimagined scope and ruleset note (R01). Finish the reopened R14 and R21 doc sweep.
3. Draft rig schema v0 and the blockout style brief; list each HAR's appendages from the reference for R16.

Still open from before: the live playtest of Ari's route (`run-story-ari.ps1`) and of the Arcade ladder.

## References

- [Reimagined design pitch v0.3](_archive/omf-reimagined-design-pitch-v0.3.md) (archived, history only)
- [Original game reference](OMF2097/OMF2097_REFERENCE.md)
- [Story treatment](OMF2107_LORE_v2.md)
- [Game specification](OMF2107_GAME_SPEC.md)
- [OpenOMF repository](https://github.com/omf2097/openomf)
- [Original manual story](https://www.omf2097.com/wiki/doku.php?id=omf2097:story)
- [Decoded in-game help and text](https://www.omf2097.com/wiki/doku.php?id=omf2097:english.dat)
