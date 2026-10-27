"""Export the ten pilot portraits from the original game's MELEE.BK for the story viewer.

The portraits are the big faces of the pilot selection screen (MELEE.BK animation 4, one sprite per pilot id, the
same order as OpenOMF's PILOT_* enum). They are written as 24-bit BMP files to project/build/portraits/<Pilot>.bmp,
which the viewer loads in story mode.

This is original-game artwork. The output stays in the git-ignored build folder: it is a local development
reference, not something to commit or distribute. See the rights checkpoint in project/docs/ROADMAP.md.
Without these files the story viewer shows plain placeholder cards instead.

Usage (repository root, after building bktool with project/scripts/build.ps1):
    python project/tools/export_pilot_portraits.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
BKTOOL = ROOT / "build" / "omf_debug_z7" / "bktool.exe"
MELEE = ROOT / "OMF2097" / "MELEE.BK"
OUT = ROOT / "project" / "build" / "portraits"
BIG_PORTRAITS = 4   # MELEE.BK animation holding the big faces

# OpenOMF's pilot ids 0-9, as in src/game/common_defines.h.
PILOTS = ["Crystal", "Steffan", "Milano", "Christian", "Shirro", "JeanPaul", "Ibrahim", "Angel", "Cossette", "Raven"]


def main() -> int:
    for needed in (BKTOOL, MELEE):
        if not needed.exists():
            print(f"Missing {needed}", file=sys.stderr)
            return 1
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for sprite, pilot in enumerate(PILOTS):
            png = Path(tmp) / f"{pilot}.png"
            result = subprocess.run(
                [str(BKTOOL), "-f", str(MELEE), "-a", str(BIG_PORTRAITS), "-s", str(sprite), "-k", "image",
                 f"--export={png}"],
                capture_output=True, text=True)
            if result.returncode != 0 or not png.exists():
                print(f"Could not export {pilot}: {result.stdout}{result.stderr}", file=sys.stderr)
                return 1
            with Image.open(png) as image:
                image.convert("RGB").save(OUT / f"{pilot}.bmp")
    print(f"Wrote {len(PILOTS)} portraits to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
