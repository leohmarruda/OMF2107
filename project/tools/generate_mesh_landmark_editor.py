"""Build a local HTML editor for the joint landmarks the Meshy meshes are fitted with.

generate_meshy_meshes.py splits each Meshy mesh into the rig's groups by the nearest bone and retargets the
arms and legs about their joints. Both steps rest on landmarks (head base, neck, spine, shoulders, elbows,
wrists, hips, knees, ankles). This page shows the mesh from the front and from the side with the landmarks
as draggable points joined by bones, so you can place them on the mesh the way you place joints on a sprite
in the pose editor. The front view fixes a point's sideways position and the side view its depth; height is
shared. It also shows the segment lengths of both sides (a left and right limb of different length is fitted
to different lengths). "l" and "r" are the character's own left and right, so "l" is on the image's right in the
front view. Save the download as project/data/mesh_landmarks.json; generate_meshy_meshes.py picks
it up, and with depths in it assigns the mesh to bones in 3D.

    python project/tools/generate_mesh_landmark_editor.py     # writes project/build/mesh-landmarks/index.html
    (drag the points in the browser, then "Download mesh_landmarks.json" into project/data/)
    python project/tools/generate_meshy_meshes.py             # or project/scripts/run-meshy.ps1

Both pictures are rendered here from the FBX in the model's own pixel frame (origin and pixels per unit in
generate_meshy_meshes.py), so a point sits on the mesh exactly where the generator will read it. In the side
picture the character faces the image's right and FBX Y = 0 is at the origin's x pixel.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import generate_meshy_meshes as gm  # noqa: E402
import paths  # noqa: E402
from fbx_reader import mesh  # noqa: E402

OUT = paths.ARTIFACTS / "mesh-landmarks"
LABELS = {"meshy": "Jaguar - Robot Mascot", "jester": "Shadow - Rocket Jester"}


def anatomical(points):
    """The generator keeps "l" for the limb on the image's left; the editor and its file use the character's own
    left, which is on the image's right when it faces us, so the names are swapped on the way in."""
    return {(k[:-1] + ("r" if k.endswith("_l") else "l") if k[-2:] in ("_l", "_r") else k): v
            for k, v in points.items()}


def canvas_size(m):
    """Picture size: the model's own pixel frame (origin and scale) with the whole mesh inside it."""
    return int(max(600, 2 * max(m.origin)))


def render(m, v, tris, view, size):
    """Orthographic view of the mesh in the model's own pixel frame, painter's algorithm, flat shading.

    front: the camera looks at the model's front (x across, z up, same mapping the generator reads landmarks
    with). side: the model's front faces the image's right and FBX Y = 0 is at the origin's x pixel.
    """
    ppu = m.pixels_per_unit
    ox, oy = m.origin
    py = oy - v[:, 2] * ppu
    if view == "front":
        px = ox + v[:, 0] * ppu
        far = -m.front_sign * v[:, 1]                  # larger is further from a camera at the model's front
        light = np.array([-0.35, 0.55 * m.front_sign, 0.75])
    else:
        px = ox + v[:, 1] * ppu / m.front_sign
        far = v[:, 0]                                    # camera on the -X side
        light = np.array([-0.55, 0.0, 0.75])
    light /= np.linalg.norm(light)
    a, b, c = (v[tris[:, i]] for i in range(3))
    n = np.cross(b - a, c - a)
    n /= np.maximum(np.linalg.norm(n, axis=1, keepdims=True), 1e-12)
    shade = np.clip(0.38 + 0.62 * np.abs(n @ light), 0, 1)
    order = np.argsort(far[tris].mean(axis=1))[::-1]   # far first
    img = Image.new("RGB", (size, size), (24, 31, 40))
    draw = ImageDraw.Draw(img)
    for i in order:
        t = tris[i]
        s = shade[i]
        draw.polygon([(px[t[0]], py[t[0]]), (px[t[1]], py[t[1]]), (px[t[2]], py[t[2]])],
                     fill=(int(120 * s + 30), int(155 * s + 30), int(190 * s + 30)))
    return img


def estimate_depth(m, v, landmarks):
    """Depth pixel for landmarks that have none: the median depth of the mesh around each one."""
    ox, oy = m.origin
    out = {}
    for name, (x, y) in landmarks.items():
        wx, wz = (x - ox) / m.pixels_per_unit, (oy - y) / m.pixels_per_unit
        near = (np.abs(v[:, 0] - wx) < .06) & (np.abs(v[:, 2] - wz) < .06)
        depth = float(np.median(v[near, 1])) if near.sum() > 20 else 0.0
        out[name] = float(ox + depth * m.pixels_per_unit / m.front_sign)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    models = []
    for m in gm.MODELS:
        v, tris = mesh(gm.MESH_DIR / m.fbx)
        size = canvas_size(m)
        for view in ("front", "side"):
            render(m, v, tris, view, size).save(OUT / f"{m.prefix}-{view}.png")
        guess = estimate_depth(m, v, m.landmarks)
        points = anatomical({k: [round(x, 1), round(z, 1), round(m.depth.get(k, guess[k]), 1)]
                             for k, (x, z) in m.landmarks.items()})
        code = gm.CODE_LANDMARKS[m.prefix]
        cguess = estimate_depth(m, v, code)
        defaults = anatomical({k: [round(x, 1), round(z, 1), round(cguess[k], 1)] for k, (x, z) in code.items()})
        models.append({"prefix": m.prefix, "label": LABELS[m.prefix], "size": size, "front": f"{m.prefix}-front.png",
                       "side": f"{m.prefix}-side.png", "landmarks": points, "defaults": defaults})
    page = (paths.WEB / "mesh_landmarks_page.html").read_text(encoding="utf-8")
    data = json.dumps({"models": models}).replace("</", "<\/")
    (OUT / "index.html").write_text(page.replace("__DATA__", data), encoding="utf-8")
    saved = paths.DATA / "mesh_landmarks.json"
    print(f"{len(models)} models -> {OUT / 'index.html'}"
          + (f" (starting from {saved.name})" if saved.is_file() else " (starting from the generator's landmarks)"))


if __name__ == "__main__":
    main()
