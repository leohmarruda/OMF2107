"""Smooth upscaling of the story viewer's backdrops and illustration frames.

The original game's backgrounds are 320x200 with a 256-colour palette, so they look blocky at the viewer's window
size. This turns each one into a larger picture the viewer draws as a smooth texture: bicubic upscale, a small median to
round the staircase edges, a light blur, then an unsharp mask to bring the edge contrast back. It cannot add detail
that is not in the original; it only removes the visible pixel steps.

The results are written next to the originals as <name>_hd.bmp. The viewer prefers them and falls back to the original
pixels when they are missing. Like the originals they are original-game material, local only (see ASSET_LEDGER.md).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

SCALE = 4


def smooth_upscale(image: Image.Image, scale: int = SCALE) -> Image.Image:
    big = image.convert("RGB").resize((image.width * scale, image.height * scale), Image.BICUBIC)
    pixels = np.asarray(big).astype(np.float32)
    rounded = np.stack([ndimage.median_filter(pixels[..., c], size=scale + 1) for c in range(3)], axis=-1)
    soft = Image.fromarray(np.clip(rounded, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    return soft.filter(ImageFilter.UnsharpMask(radius=2.0, percent=70, threshold=2))


def write_hd(source: Path) -> Path:
    """Writes <source stem>_hd.bmp next to source and returns its path."""
    target = source.with_name(f"{source.stem}_hd.bmp")
    if target.exists() and target.stat().st_mtime >= source.stat().st_mtime:
        return target   # written after the original, from a render: not an upscale to replace
    with Image.open(source) as image:
        smooth_upscale(image).save(target)
    return target


def write_all_hd(folder: Path) -> int:
    """Upscales every original bmp in folder (those not already _hd); returns how many were written."""
    count = 0
    for source in sorted(folder.glob("*.bmp")):
        if source.stem.endswith("_hd"):
            continue
        write_hd(source)
        count += 1
    return count
