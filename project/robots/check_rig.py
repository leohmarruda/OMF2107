#!/usr/bin/env python3
"""Check robots/rig.json against the code and the exported rigs.

Usage: python robots/check_rig.py [--write]

Checks:
  1. rig.json is the rig that build_rigged.rig(0) (Jaguar) produces: the same joints, parents and pivots.
  2. Shadow has the same joints and hierarchy as Jaguar; its pivot differences are reported (they are proportions, and
     belong in har.json when that exists).
  3. Each exported *-rigged.gltf has the joint nodes, hierarchy and local offsets that rig(har) gives.
With --write, rig.json is rewritten from the code (use it once, then edit by hand and let the check guard the code).
Exit status 1 on any mismatch in 1 or 3, or a hierarchy mismatch in 2.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import build_rigged  # noqa: E402

TOL = 1e-6
GROUPS = ["torso", "head", "pelvis", "shoulder", "elbow", "wrist", "hip", "knee", "ankle"]   # generate_model_meshes.group()


def from_code(har: int) -> dict:
    pivots, parents = build_rigged.rig(har)
    return {"joints": [{"name": n, "parent": parents[n], "pivot": [round(float(v), 4) for v in p]} for n, p in pivots.items()]}


def document() -> dict:
    return {
        "version": 1,
        "families": {"jaguar_shadow": ["jaguar", "shadow"]},
        "units": "rig units; the floor is y = 0 and the root sits on it at the origin (a Jaguar is about 3.3 units tall)",
        "axes": {"up": "+y", "front": "-z (the fighter faces the opponent along -z)", "lateral": "x; the paired joints are suffixed -1 and +1"},
        "pose": "rest pose is a standing, arms down; clips rotate a joint about its local X axis, in radians (side-view plane y/z)",
        "pairs": "a joint in the list below with the suffix _-1 or _+1 exists once per side with the x of its pivot mirrored",
        "mesh_groups": GROUPS,
        "pivots_are": "absolute rest positions of the Jaguar; Shadow's differences are proportions (see check_rig.py)",
        **from_code(0),
    }


def check_rig_json(errors: list[str]) -> None:
    path = ROOT / "rig.json"
    if not path.is_file():
        errors.append("rig.json is missing (run with --write once)")
        return
    doc = json.loads(path.read_text(encoding="utf-8"))
    want = {j["name"]: j for j in from_code(0)["joints"]}
    have = {j["name"]: j for j in doc.get("joints", [])}
    for name in sorted(set(want) | set(have)):
        if name not in have:
            errors.append(f"rig.json lacks joint {name}")
        elif name not in want:
            errors.append(f"rig.json has joint {name} that build_rigged.rig(0) does not")
        else:
            if have[name]["parent"] != want[name]["parent"]:
                errors.append(f"{name}: parent {have[name]['parent']} in rig.json, {want[name]['parent']} in code")
            if any(abs(a - b) > TOL for a, b in zip(have[name]["pivot"], want[name]["pivot"])):
                errors.append(f"{name}: pivot {have[name]['pivot']} in rig.json, {want[name]['pivot']} in code")


def check_variants(errors: list[str]) -> list[str]:
    jag, sha = {j["name"]: j for j in from_code(0)["joints"]}, {j["name"]: j for j in from_code(1)["joints"]}
    notes = []
    if set(jag) != set(sha):
        errors.append("Shadow and Jaguar do not have the same joints: " + ", ".join(sorted(set(jag) ^ set(sha))))
    for name in sorted(set(jag) & set(sha)):
        if jag[name]["parent"] != sha[name]["parent"]:
            errors.append(f"{name}: Shadow's parent differs from Jaguar's")
        delta = [round(b - a, 4) for a, b in zip(jag[name]["pivot"], sha[name]["pivot"])]
        if any(abs(d) > TOL for d in delta):
            notes.append(f"  Shadow differs at {name}: {delta}")
    return notes


def check_gltf(har: int, path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"{path.name} is missing")
        return
    gltf = json.loads(path.read_text(encoding="utf-8"))
    nodes = gltf["nodes"]
    by_name = {n["name"]: i for i, n in enumerate(nodes) if "mesh" not in n}
    pivots, parents = build_rigged.rig(har)
    parent_of = {c: i for i, n in enumerate(nodes) for c in n.get("children", [])}
    for name, pivot in pivots.items():
        if name not in by_name:
            errors.append(f"{path.name}: no node for joint {name}")
            continue
        node = nodes[by_name[name]]
        base = pivots[parents[name]] if parents[name] else (0, 0, 0)
        rel = [pivot[i] - base[i] for i in range(3)]
        if any(abs(a - b) > 1e-5 for a, b in zip(node["translation"], rel)):
            errors.append(f"{path.name}: {name} is at {node['translation']}, the rig says {rel}")
        want_parent = parents[name]
        got_parent = nodes[parent_of[by_name[name]]]["name"] if by_name[name] in parent_of else None
        if want_parent != got_parent:
            errors.append(f"{path.name}: {name} hangs from {got_parent}, the rig says {want_parent}")
    extra = set(by_name) - set(pivots)
    if extra:
        errors.append(f"{path.name}: joint nodes not in the rig: {', '.join(sorted(extra))}")


def main() -> int:
    if "--write" in sys.argv:
        (ROOT / "rig.json").write_text(json.dumps(document(), indent=2) + "\n", encoding="utf-8")
        print("wrote", ROOT / "rig.json")
    errors: list[str] = []
    check_rig_json(errors)
    notes = check_variants(errors)
    check_gltf(0, ROOT / "jaguar" / "blockout" / "jaguar-rigged.gltf", errors)
    check_gltf(1, ROOT / "shadow" / "blockout" / "shadow-rigged.gltf", errors)
    print(f"{len(from_code(0)['joints'])} joints; Shadow's pivot differences from Jaguar ({len(notes)}):")
    print("\n".join(notes))
    if errors:
        print("\nMISMATCH:")
        print("\n".join("  " + e for e in errors))
        return 1
    print("rig.json, the code and both rigged glTF files agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
