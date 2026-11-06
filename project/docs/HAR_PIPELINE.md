# HAR pipeline: one source, every output

Status: proposed 2026-11-05. Goal: adding or refining a HAR touches each fact once. Today the same fact is entered
several times. This note lists the redundancy found, the proposed single flow, and what it replaces.

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
                       rig.json  (one per HAR family: joints, hierarchy, rest pose, units, axes, front)
                           |
   har.json  (proportions, part parameters, effect anchors, visual variants)
        |                  |
        |        +---------+----------------------------+
        v        v                                      v
  blockout (procedural)               detailed mesh (imported once)      keyframes (authored once, rig space)
  from rig + parameters               auto-aligned, auto-weighted         per-move poses + timing, IK for limbs
        \                                    |                                   /
         +------------------ one skinned glTF per variant ---------------------+
                                             |
                    har_build  ->  runtime pack  +  collision masks (from the blockout)
                                             |
                                          har_check  (one report)
```

### Rules

1. **One rig spec per HAR family** (`rig.json`): joint names, hierarchy, units (rig units, floor at 0, root on the
   floor at the origin), axes (-z toward the opponent, +y up, as the blockout generators and the prototype have it),
   rest pose. Everything else reads it. Jaguar and Shadow share the same 16 joints and hierarchy; they differ only in 13
   pivot offsets of 0.01 to 0.03 rig units, which are proportions and move to `har.json`. Written 2026-11-06 as
   [robots/rig.json](../robots/rig.json), guarded by `python robots/check_rig.py`.
2. **The blockout is generated, not modelled.** Built procedurally from `rig.json` plus per-HAR part parameters
   (lengths, widths, armor volumes). A proportion change is a parameter edit. It has no landmarks to match, because
   it is made from the rig.
3. **The detailed mesh is imported once through an importer** that does the coordinate matching: detects up and
   front (symmetry and foot direction, replacing the `FRONT_SIGN` guess), scales and centres it to the rig, proposes
   the landmark points automatically (from the mesh's symmetry and extremities), and asks a human only to confirm or
   nudge the points. The result is stored as a small `landmarks` file next to the mesh, in rig units, never raw
   FBX coordinates.
4. **Skinning replaces splitting.** Automatic weights from the landmarks produce a real skin (joint influences), so
   limbs bend without the blend-band hack and the same animation drives any mesh bound to the rig. Tune weights per
   HAR only where the check flags a problem.
5. **Animation is authored once, in rig space, as keyframes.** Per move: a few key poses (startup, contact, recovery)
   with timing from the data pack, in-betweens interpolated, limbs placed by IK to targets (hand or foot reaching the
   measured contact point). Both visual variants play it with no retargeting. Edit poses on the 3D model, not over a
   sprite. Poses shared by several animations are one clip, referenced by name.
6. **Collision masks and hit volumes are generated from the blockout** at build time, per animation frame, and
   cached by a hash of the pose. They do not depend on the detailed mesh or on any original sprite.
7. **Effect anchors live on the rig** (hands, feet, chest, a muzzle point), so effects work in both variants.
8. **Output is one skinned glTF per variant plus one runtime pack.** The viewer loads them at run time, so the
   per-mesh C header generators go away.
9. **One command checks everything.** `har_check <har>` (in the spirit of `story_check`) reports: rig matches,
   landmarks present, skin binds, every pose and animation exists for both variants, silhouette of the detailed mesh
   inside the tolerance of the blockout per pose, masks regenerated, effect anchors present, data pack valid. A HAR is
   "done" when it passes.
10. **Reuse across HARs.** Keyframes use IK and proportion-relative targets, so a new HAR on the same rig inherits
    the shared move library and only authors what is different. Fighters that do not fit the shared rig (extra limbs,
    a chain weapon) get an extension to the rig spec, not a separate pipeline.

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
pose evaluation in `main.c` (lines ~820-950) to decide what moves into data.

## What this replaces or retires

- The per-sprite pose fitting (`pose_catalog.csv` rows, `pose_editor`, `fit_poses.py`, `merge_pose_rows.py`) becomes a
  development reference tool for comparing against the original; shipped poses are the new keyframes. The
  sprite-group dedupe stays useful as an analysis aid until the keyframe library covers every move.
- `generate_model_meshes.py` and `generate_meshy_meshes.py` and their C headers (`model_meshes.h`,
  `meshy_meshes.h`) are replaced by `har_build` plus run-time glTF loading.
- The landmark editor stays, shrunk to confirming auto-proposed points.
- `match_projection_poses.py` (stand-in poses for Shadow's projectiles) is replaced by authored clips.

## Work, in order

| ID | Task | Output |
| --- | --- | --- |
| P0 | Audit the tools above: what each reads, writes and duplicates; confirm the table | One-page audit, list of what to delete |
| P1 | Write `rig.json` from the existing Jaguar and Shadow rig; verify all generators use it | Spec file plus a check. **Done 2026-11-06** for the glTF rig; the pose code in `main.c` and the CSV catalog are not checked against it yet |
| P2 | Procedural blockout from rig plus parameters; match the accepted Jaguar and Shadow blockouts | `har_build` blockout stage; before and after silhouette diff |
| P3 | Importer: auto up, front, scale; landmark proposal; confirm UI | Detailed mesh in rig space, small landmarks file |
| P4 | Auto-skinning and glTF export; viewer loads glTF at run time | One skinned glTF per variant; C headers removed |
| P5 | Keyframe authoring on the 3D model with IK; port Jaguar's moves | Clip library, first moves played in both variants |
| P6 | Mask generation from the blockout, cached | Masks for Jaguar frames, matching the data-pack hit tests |
| P7 | `har_check` report | One command, one pass or fail |
| P8 | Port Shadow, then use the pipeline for the next HAR as the test of reuse | Time per new HAR recorded |

Measure success by time to add a HAR (target in the release plan) and by the number of places a joint name or rest
height is written (target: one).

## Risks

- Auto-weights can fail on thin or spiky parts (blades, claws); expect manual weight fixes for those.
- Interpolated keyframes may not reproduce the snap of 1994 sprite animation; allow hold and step curves.
- Procedural blockouts may lose details that the accepted hand-built blockouts have; compare silhouettes in P2.
- The stylised simplified look may not be the raw collision blockout; if they diverge, derive the look from the
  blockout by a style layer (shading and edge treatment) before allowing separate geometry.
