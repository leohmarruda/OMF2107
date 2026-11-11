# HAR pipeline: one source, every output

Status: proposed 2026-11-05; **aligned 2026-11-09** with the per-HAR stage gates H1 to H5 in `DEVPLAN.md` ("HAR
production pipeline"), which wins on conflict. Goal: adding or refining a HAR touches each fact once, in both visual
modes (**blockout** and **mesh**), with correct body coordinates and collisions, including HARs with non-humanoid limbs.

This file owns the **tools** (tasks P0 to P12, built once). `DEVPLAN.md` owns the **per-HAR stages** (H1 to H5, run
for every HAR) and the dates.

Basis: read from `POSE_AUTHORING.md`, `docs/mesh/README.md`, `robots/README.md`, the file list of `project/tools/`,
and the heads of `generate_meshy_meshes.py`-related docs and `match_projection_poses.py`. The tool internals have not
been read line by line; step P0 below audits them before anything is deleted.

## Redundancy found

| What is entered or produced more than once | Where today |
| --- | --- |
| The skeleton: joint names, rest heights, axes | The blockout build (`robots/*/blockout/build.py`, `build_rigged.py`), the pose catalog columns, `model_meshes.h`, `meshy_meshes.h`, the landmark JSON |
| Mesh coordinates hand-matched to the rig | `data/mesh_landmarks.json` holds 16 hand-placed raw FBX points per mesh; `generate_meshy_meshes.py` then rescales to blockout joint heights and guesses the front (`FRONT_SIGN`) |
| Mesh-to-rig binding | Nearest-bone splitting plus a blend band (`ModelBlend`), baked into C headers; a different path from the blockout's rigid parts |
| Output format | At least three: blockout glTF, rigged glTF, and generated C headers for the viewer |
| Poses | Fitted once per original sprite (about 3,490 sprite keys across 11 HARs) by dragging joints over the sprite in the pose editor, in 2D (y, z) numbers, tied to the original artwork |
| Per-mesh retargeting | Each new mesh needs its own split, scale and blend tuning before it can use the poses |
| The collision shape | Not generated; hit tests come from OpenOMF's sprite pixels |

Consequences: a blockout change is not seen by the detailed mesh; a new mesh costs a hand pass; poses cannot ship
(they come from original sprites); there is no single check that says a HAR is complete.

## Proposed flow

```
                rig.json  (one per HAR family: joints, hierarchy, rest pose, units, axes, front,
                           sockets, region IDs, optional appendage chains)
                    |
   har.json  (proportions, part parameters, appendage parameters, visual variants)
        |           |
        |   +-------+---------------------------------------------+
        v   v                                                     v
  blockout (procedural)              detailed mesh (imported once)          keyframes (authored once, rig space,
  from rig + parameters              auto-aligned, auto-weighted,            timed by the data pack; IK for limbs)
        |                            conformed to the blockout envelope                    |
        |                                    |                                             |
        +------- collision masks (from the posed blockout, per frame) <--------------------+
        |                                    |
        +----------------- one skinned glTF per variant -------------------+
                                             |
                    har_build  ->  runtime pack (data pack + masks + glTFs)
                                             |
                                har_check  (one report, per stage H1 to H5)
```

### Rules

1. **One rig spec per HAR family** (`rig.json`): joint names, hierarchy, units (rig units, floor at 0, root on the
   floor at the origin), axes (-z toward the opponent, +y up, as the blockout generators and the prototype have it),
   rest pose, joint limits, sockets (contact, ground, effect, swap) and region IDs. Everything else reads it. Jaguar
   and Shadow share the same 16 joints and hierarchy; they differ only in 13 pivot offsets of 0.01 to 0.03 rig units,
   which are proportions and move to `har.json`. Written 2026-11-06 as [robots/rig.json](../robots/rig.json), guarded
   by `python robots/check_rig.py`. Locked as schema v1 only after the all-HAR stress test (P9).
2. **The blockout is generated, not modelled, and it ships.** Built procedurally from `rig.json` plus `har.json` part
   parameters (lengths, widths, armor volumes). A proportion change is a parameter edit. It has no landmarks to match,
   because it is made from the rig. The blockout style (primitives, bevels, palette, materials, procedural damage
   shader) lives in the generator, so every HAR inherits it.
3. **The detailed mesh is imported once through an importer** that does the coordinate matching: detects up and
   front (symmetry and foot direction, replacing the `FRONT_SIGN` guess), scales and centres it to the rig, proposes
   the landmark points automatically (from the mesh's symmetry and extremities), and asks a human only to confirm or
   nudge the points. The result is stored as a small `landmarks` file next to the mesh, in rig units, never raw
   FBX coordinates. The mesh is then **conformed to the blockout envelope** per bone.
4. **Skinning replaces splitting.** Automatic weights from the landmarks produce a real skin (joint influences), so
   limbs bend without the blend-band hack and the same animation drives any mesh bound to the rig. Tune weights per
   HAR only where the check flags a problem.
5. **Animation is authored once, in rig space, as keyframes.** Per move: a few key poses (startup, contact, recovery)
   with timing from the data pack, in-betweens interpolated, limbs placed by IK to targets (hand or foot reaching the
   measured contact point). Both visual variants play it with no retargeting. Edit poses on the 3D model, not over a
   sprite. Poses shared by several animations are one clip, referenced by name. Hold and step curves are allowed for
   the snap of the original animation.
6. **Collision masks are generated from the posed blockout** at build time, per animation frame, projected on the
   fight plane, and cached by a hash of the pose. They are stored in the data pack and are the only gameplay
   collision in every look. They never depend on the detailed mesh or on any original sprite. Parity is checked by
   comparing them with the measured reach, timing and hits. Cosmetic appendages are excluded (rule 11).
7. **Effect anchors live on the rig** (hands, feet, chest, a muzzle point, a tail tip), so effects work in both
   variants.
8. **Output is one skinned glTF per variant plus one runtime pack.** The viewer loads them at run time, so the
   per-mesh C header generators go away. Generated files are build outputs: CI regenerates them and fails if a
   committed copy differs (P11).
9. **One command checks everything.** `har_check <har> [--stage H1..H5]` (in the spirit of `story_check`) runs the
   checks listed under "har_check" below. A HAR is "done" when it passes H5.
10. **Reuse across HARs.** Keyframes use IK and proportion-relative targets, so a new HAR on the same rig family
    inherits the shared move library and only authors what is different.
11. **Non-humanoid limbs extend the rig spec, not the pipeline.** Optional appendage chains are declared by type:
    tail, wing, flail or chain, thruster, extra arm, weapon mount. Each declares segment count, joint limits, attach
    bone, region and behaviour:
    - **Gameplay appendage** (can hit or be hit): keyframed like any limb, with a contact socket, and included in mask
      generation.
    - **Cosmetic appendage:** secondary motion computed deterministically from the tick (no variable-step physics),
      excluded from masks, so replays look identical and collisions do not change.
    - Region: the attach bone's region unless the rig says otherwise.
12. **No limb passes through a solid, fixed in the viewer.** OpenOMF has no body collision, and a gameplay pushbox
    would change the fight, so the simulation is untouched. A solid-contact layer (DEVPLAN R18) uses capsule and box
    proxies generated from the blockout parts and resolves, in order: HAR against HAR (depth separation, then a small
    ease-back), limb against body (IK stop at the surface; on a hit frame the contact socket lands on the opponent's
    surface), arena (foot planting, wall and floor stops) and self (push-out after blends). Offsets are capped so a
    landed hit never looks like a miss.

## har_check

| Check | Stage | Looks |
| --- | --- | --- |
| `rig.json` and `har.json` valid against schema v1; joint names and rest heights written in one place only | H1 | n/a |
| Appendages declared with type, region and behaviour | H1 | n/a |
| Coordinates: root on the floor at the origin, axes, front, scale in rig units | H2 | Both |
| Ground contact: feet or ground sockets on the floor in idle, walk and landing frames | H2, H3 | Both |
| Facing flip mirrors correctly around the fight plane | H2, H3 | Both |
| Blockout silhouette compared with the accepted hand-built blockout (where one exists) | H2 | Blockout |
| Generated masks match the measured reach, timing and hits within tolerance (parity) | H3 | Blockout |
| Contact socket inside the hit mask on every active frame | H3, H4 | Both |
| No self-intersection beyond tolerance, extreme poses and throws included | H3, H4 | Both |
| Collision proxies generated for every part and appendage | H2 | n/a |
| Penetration replay suite: every move against every HAR already in the pack and in every arena, with the solid-contact layer on, below the tolerance | H3, H4 | Both |
| Every move and clip exists and plays in both variants | H3, H4 | Both |
| Mesh quality: manifold, normals, no degenerate faces, scale, origin, polygon and material budget, LODs | H4 | Mesh |
| Mesh inside the blockout silhouette per pose, within tolerance | H4 | Mesh |
| Skin binds; deformation over every frame of every move without collapse or tearing | H4 | Mesh |
| All 12 region states (4 regions x 3) and the patched variant present; plates on their swap sockets | H5 | Both |
| Every removable plate has an inner frame part beneath it: no hole into the model from any fight-camera angle | H5 | Both |
| Masks and contact proxies identical across all damage states | H5 | Both |
| Silhouette change per state under the P1 limit; no startup tell hidden | H5 | Both |
| Destruction sequence plays; engine budgets from `DEVPLAN.md` met | H5 | Both |
| Masks and glTFs regenerated identically from source | All | Both |

Tolerances are set in P1 and recorded in `rig.json`.

## Audit result (P0, 2026-11-05)

Checked by file sizes, symbol searches and the heads of the files; not every function was read.

| Finding | Evidence |
| --- | --- |
| The pelvis height `1.38` is written in at least two places | `project/prototype/main.c` (lines 659, 669, 765-770, 844, 883) and `robots/build_rigged.py` (line 109) |
| The pose logic lives in the C viewer, as code, not data | `main.c` computes hip, shoulder and wrist positions from `body_drop`, `lean`, `guard` and `arm_forward` (lines ~840-900); `pose_catalog.c` only overrides it |
| Two generators bake the same blockouts to C headers | `tools/generate_model_meshes.py` (77 lines) imports both `blockout/build.py` files and writes `model_meshes.h`; `tools/generate_meshy_meshes.py` (655 lines) writes `meshy_meshes.h` |
| The mesh generator holds its own rig data and group rules | `generate_meshy_meshes.py`: `GROUP_NAMES`, `JOINTS`, `CODE_LANDMARKS`, `MODELS` and per-model landmark sets, plus the name-prefix grouping in `generate_model_meshes.py` (`helmet`, `eye_`, `upper_arm`...) |
| Landmark data is hand-entered in raw FBX coordinates | `data/mesh_landmarks.json`: 16 points per mesh, such as `[333.4, 136.5, 327.5]`, with different units per mesh |
| The pose tools are many and sprite-bound | `fit_poses.py` (322), `generate_pose_editor.py` (328), `merge_pose_rows.py` (106), `generate_pose_catalog.py` (191), `sprite_duplicates.py` (151), all reading the original sprites |

What to keep: `sprite_duplicates.py` and `fit_poses.py` as development comparison tools; the landmark editor (reduced to
confirming points); `blockout/build.py` as the starting point of the procedural blockout.

What to merge or delete after P4: the two mesh generators and their C headers; `merge_pose_rows.py` and the CSV pose
catalog once keyframes cover a move; `match_projection_poses.py`.

Next step for the audit: read `build.py` (296 lines) and `build_rigged.py` (209) fully to define `rig.json`, and read the
pose evaluation in `main.c` (lines ~820-950) to decide what moves into data. The pelvis height and the pose logic in
`main.c` must move into `rig.json` and the keyframes before P9 locks the schema.

## What this replaces or retires

- The per-sprite pose fitting (`pose_catalog.csv` rows, `pose_editor`, `fit_poses.py`, `merge_pose_rows.py`) becomes a
  development reference tool for comparing against the original; shipped poses are the new keyframes. The
  sprite-group dedupe stays useful as an analysis aid until the keyframe library covers every move.
- `generate_model_meshes.py` and `generate_meshy_meshes.py` and their C headers (`model_meshes.h`,
  `meshy_meshes.h`) are replaced by `har_build` plus run-time glTF loading.
- The landmark editor stays, shrunk to confirming auto-proposed points.
- `match_projection_poses.py` (stand-in poses for Shadow's projectiles) is replaced by authored clips.
- Meshy stand-in meshes stay review references. One becomes a production mesh only if it passes P3, H4 and the rights
  ledger.

## Work, in order

| ID | Task | Output | DEVPLAN phase | Enables |
| --- | --- | --- | --- | --- |
| P0 | Audit the tools above: what each reads, writes and duplicates; confirm the table | One-page audit, list of what to delete. **First pass done 2026-11-05**; finish with the reads listed above | 0 | All |
| P1 | Write `rig.json` from the existing Jaguar and Shadow rig; verify all generators use it; set `har_check` tolerances | Spec file plus a check. **Done 2026-11-06** for the glTF rig; the pose code in `main.c` and the CSV catalog are not checked against it yet; tolerances open | 0 | H1 |
| P9 | **Schema stress test** (DEVPLAN R16): `rig.json` or extensions plus `har.json` and generated blockouts for all ten HARs and Nova, appendages included, confirmed from the original reference; no animation, no mesh. Lock schema v1 | Eleven blockouts; schema v1 locked; family list | 1 | H1 for every HAR |
| P2 | Procedural blockout from rig plus parameters, with the blockout style; match the accepted Jaguar and Shadow blockouts | `har_build` blockout stage; before and after silhouette diff | 1 | H2 |
| P7 | `har_check` with the checks above, stage by stage (DEVPLAN R17); grows as later tools land | One command, one pass or fail per stage | 1 onward | All gates |
| P11 | Generated-artifact check in CI (DEVPLAN R19) | Build fails on drift | 1 | All |
| P3 | Importer: auto up, front, scale; landmark proposal; confirm UI; envelope conform | Detailed mesh in rig space, small landmarks file | 1 (path test on a throwaway mesh) | H4 |
| P4 | Auto-skinning and glTF export; viewer loads glTF at run time | One skinned glTF per variant; C headers removed | 1 | H4 |
| P5 | Keyframe authoring on the 3D model with IK, hold and step curves; port Jaguar's moves | Clip library, first moves played in both variants | 2 | H3 |
| P6 | Mask generation from the posed blockout, cached, written to the data pack; cosmetic appendages excluded | Masks for Jaguar frames, matching the measured hit tests | 2 | H3 |
| P12 | Solid-contact layer and penetration replay suite (DEVPLAN R18) | Proxies generated per HAR; suite passes for every move, HAR pair and arena; at most 0.5 ms per frame | 2 | H3 and H4 gates |
| P10 | Damage layer (DEVPLAN "Damage parts", R04): frame and plate declaration in `har.json`; generator split into frame plus plate shell with dented, removed and patched variants; procedural blockout damage shader; mesh plate, inner frame and patch naming checked by the importer; packed mask channels; deterministic debris; limb detachment for destruction | All 12 region states plus patched on Jaguar in both looks | 1 (spike, with Spike C), 3 | H5 |
| P8 | Port Shadow, then use the pipeline for the next HAR as the test of reuse | Time per stage per HAR recorded | 2, then 5 | Roster |

Order constraints: P9 before any H4 work on any HAR; P5 and P6 before Jaguar's H3; P3 and P4 before Jaguar's H4; P10
before H5.

Measure success by time to add a HAR, per stage (target in the development plan), and by the number of places a joint
name or rest height is written (target: one).

## Risks

- Auto-weights can fail on thin or spiky parts (blades, claws, tails); expect manual weight fixes for those.
- Interpolated keyframes may not reproduce the snap of 1994 sprite animation; allow hold and step curves.
- Procedural blockouts may lose details that the accepted hand-built blockouts have; compare silhouettes in P2.
- Collision follows the keyframes, so a keyframe edit changes gameplay. Keyframes freeze at H3; any later edit re-runs
  parity.
- Masks projected from a 3D blockout may not reproduce the original's pixel hit tests closely enough; set and check
  the tolerance on Jaguar in Phase 2 before porting other HARs.
- A HAR found in P9 to need a new appendage type after schema v1 is locked forces a schema change; P9 covers all
  eleven HARs for this reason.
- The blockout now ships as a finished look, so its style must be good enough on its own; review it in Phase 1 before
  the generator is used for all HARs.
