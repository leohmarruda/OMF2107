"""Export original-game art and sounds for the story viewer into the git-ignored project/build folder.

Writes:
  project/build/portraits/<Pilot>.bmp     the ten pilot faces (see export_pilot_portraits.py)
  project/build/backdrops/<arena>.bmp     the five original arena backgrounds (ARENA0-4.BK)
  project/build/sounds/<name>.wav         two original menu sounds from SOUNDS.DAT: move and select
  project/build/art/<name>.bmp            illustrated-sequence frames composed from the above (build_story_art.py)

This is original-game material, kept local as a development reference and never committed or distributed.
It is recorded in project/docs/ASSET_LEDGER.md. The story viewer works without any of it: it draws generated
backdrops and plays no sound.

Usage (repository root, after building bktool and soundtool with project/scripts/build.ps1):
    python project/tools/export_story_assets.py
"""
from __future__ import annotations

import re
import struct
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

from PIL import Image

import build_story_art
import export_pilot_portraits

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "build" / "omf_debug_z7"
BKTOOL = BUILD / "bktool.exe"
SOUNDTOOL = BUILD / "soundtool.exe"
GAME = ROOT / "OMF2097"
BACKDROPS = ROOT / "project" / "build" / "backdrops"
SOUNDS = ROOT / "project" / "build" / "sounds"

# ARENA0-4.BK in order; the names follow the original game's arena list.
ARENAS = ["stadium", "danger_room", "power_plant", "fire_pit", "desert"]

# SOUNDS.DAT sample indices as the engine numbers them (0-based): 19 and 20 are the menu move and press sounds
# OpenOMF plays. Battle sounds come from OpenOMF itself when a story match runs with sound.
SOUND_INDEX = {"move": 19, "select": 20}


def run(args: list[str]) -> str:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed: {result.stdout}{result.stderr}")
    return result.stdout


def export_arenas() -> None:
    BACKDROPS.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for index, name in enumerate(ARENAS):
            png = Path(tmp) / f"{name}.png"
            run([str(BKTOOL), "-f", str(GAME / f"ARENA{index}.BK"), "-k", "background", f"--export={png}"])
            with Image.open(png) as image:
                image.convert("RGB").save(BACKDROPS / f"{name}.bmp")
    print(f"Wrote {len(ARENAS)} arena backdrops to {BACKDROPS}")


def au_to_wav(au: bytes, rate: int, wav_path: Path) -> None:
    """soundtool exports signed 8-bit (silence 0x00); WAV wants unsigned (silence 0x80), so shift by 128.

    soundtool's AU header always says 8000 Hz, so the real rate (from the sample's frequency key) is passed in.
    """
    offset, _size, encoding, _header_rate, channels = struct.unpack("<5I", au[4:24])
    if au[:4] != b"dns." or channels != 1:
        raise ValueError(f"unexpected sample format (encoding {encoding}, {channels} channels)")
    with wave.open(str(wav_path), "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(1)
        out.setframerate(rate)
        out.writeframes(bytes((x + 128) & 0xFF for x in au[offset:]))


def sample_rate(index: int) -> int:
    """The sample's rate in Hz. soundtool prints it for 1-based ids but exports by 0-based index."""
    text = run([str(SOUNDTOOL), "-f", str(GAME / "SOUNDS.DAT"), "-s", str(index + 1), "--print=1"])
    match = re.search(r"= (\d+) Hz", text)
    if not match:
        raise RuntimeError(f"no sample rate for sound {index}: {text}")
    return int(match.group(1))


def export_sounds() -> None:
    SOUNDS.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for name, index in SOUND_INDEX.items():
            au = Path(tmp) / f"{name}.au"
            run([str(SOUNDTOOL), "-f", str(GAME / "SOUNDS.DAT"), "-s", str(index), "-e", str(au)])
            au_to_wav(au.read_bytes(), sample_rate(index), SOUNDS / f"{name}.wav")
    print(f"Wrote {len(SOUND_INDEX)} sounds to {SOUNDS}")


def main() -> int:
    for needed in (BKTOOL, SOUNDTOOL, GAME / "SOUNDS.DAT"):
        if not needed.exists():
            print(f"Missing {needed}", file=sys.stderr)
            return 1
    if export_pilot_portraits.main() != 0:
        return 1
    export_arenas()
    export_sounds()
    return build_story_art.main()


if __name__ == "__main__":
    raise SystemExit(main())
