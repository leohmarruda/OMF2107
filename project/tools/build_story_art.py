"""Compose the story's illustrated-sequence frames from original-game art, into the git-ignored project/build/art.

Frames are 320x124 pixels, the shape of the story viewer's art area. They are built from material already exported by
export_story_assets.py (pilot portraits, arena backgrounds) plus the HAR idle sprites exported here with aftool, with
diagonal colour bars, a vignette, and name plates drawn on top.

  stadium_title        the arena under the tournament title
  crystal_card         Crystal's portrait on cyan bars
  christian_card       Christian's portrait on orange bars
  faceoff_jaguar       Crystal in Jaguar (left) against Christian in Shadow (right)
  faceoff_shadow       Crystal in Shadow (left) against Christian in Jaguar (right)

The result is original-game material rearranged for local development, never committed or distributed (see
project/docs/ASSET_LEDGER.md). Normally run through export_story_assets.py.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "build" / "omf_debug_z7"
AFTOOL = BUILD / "aftool.exe"
GAME = ROOT / "OMF2097"
PORTRAITS = ROOT / "project" / "build" / "portraits"
BACKDROPS = ROOT / "project" / "build" / "backdrops"
ART = ROOT / "project" / "build" / "art"

W, H = 320, 124
CYAN = (60, 200, 255)
ORANGE = (255, 140, 70)
WHITE = (240, 245, 255)

# Idle stance (animation 11, sprite 0) of each HAR's FIGHTR<id>.AF file; the HAR id is the file number.
HAR_FILE = {"jaguar": 0, "shadow": 1}


def font(size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.load_default(size=size)
    except TypeError:        # older Pillow: the fixed-size bitmap font
        return ImageFont.load_default()


def arena(name: str, brightness: float) -> Image.Image:
    image = Image.open(BACKDROPS / f"{name}.bmp").convert("RGB")
    top = (image.height - H) // 2
    image = image.crop((0, top, W, top + H))
    return ImageEnhance.Brightness(image).enhance(brightness)


def bars(base: Image.Image, color: tuple[int, int, int], flip: bool = False) -> Image.Image:
    """Diagonal speed bars across the frame, in the character's colour."""
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for i, (x, width, alpha) in enumerate([(-30, 34, 90), (30, 12, 150), (58, 50, 70), (140, 16, 120), (176, 60, 60),
                                           (262, 22, 140)]):
        shift = 70
        points = [(x, H), (x + width, H), (x + width + shift, 0), (x + shift, 0)]
        draw.polygon(points, fill=color + (alpha,))
    if flip:
        layer = layer.transpose(Image.FLIP_LEFT_RIGHT)
    return Image.alpha_composite(base.convert("RGBA"), layer).convert("RGB")


def vignette(base: Image.Image, strength: float = .75) -> Image.Image:
    mask = Image.new("L", base.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((-W * .25, -H * .35, W * 1.25, H * 1.35), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(26))
    dark = Image.new("RGB", base.size, (0, 0, 0))
    inverse = ImageChops.invert(mask).point(lambda v: int(v * strength))
    return Image.composite(dark, base, inverse)


def portrait(pilot: str, scale: float, color: tuple[int, int, int]) -> Image.Image:
    image = Image.open(PORTRAITS / f"{pilot}.bmp").convert("RGB")
    image = image.resize((round(image.width * scale), round(image.height * scale)), Image.NEAREST)
    framed = Image.new("RGB", (image.width + 6, image.height + 6), color)
    framed.paste(image, (3, 3))
    return framed


def paste_shadowed(base: Image.Image, layer: Image.Image, xy: tuple[int, int]) -> None:
    shade = Image.new("RGB", layer.size, (0, 0, 0))
    base.paste(shade, (xy[0] + 3, xy[1] + 3))
    base.paste(layer, xy)


def text(base: Image.Image, label: str, xy: tuple[int, int], size: int, fill=WHITE) -> None:
    draw = ImageDraw.Draw(base)
    f = font(size)
    draw.text((xy[0] + 1, xy[1] + 1), label, font=f, fill=(0, 0, 0))
    draw.text(xy, label, font=f, fill=fill)


def plate(base: Image.Image, label: str, x: int, y: int, width: int, color: tuple[int, int, int]) -> None:
    draw = ImageDraw.Draw(base)
    draw.polygon([(x, y), (x + width, y), (x + width - 8, y + 15), (x - 8, y + 15)], fill=color)
    text(base, label, (x + 4, y + 1), 11, fill=(10, 14, 24))


def har_sprite(har: str, tmp: Path) -> Image.Image:
    png = tmp / f"{har}.png"
    result = subprocess.run(
        [str(AFTOOL), "-f", str(GAME / f"FIGHTR{HAR_FILE[har]}.AF"), "-p", str(GAME / "ARENA0.BK"), "-m", "11", "-s", "0",
         f"--export-png={png}"], capture_output=True, text=True)
    if result.returncode != 0 or not png.exists():
        raise RuntimeError(f"could not export the {har} sprite: {result.stdout}{result.stderr}")
    # Palette index 0 is the transparent colour of the game's sprites.
    indexed = Image.open(png)
    sprite = indexed.convert("RGBA")
    sprite.putalpha(indexed.point(lambda i: 0 if i == 0 else 255).convert("L"))
    return sprite


def paste_sprite(base: Image.Image, sprite: Image.Image, scale: float, x: int, bottom: int, mirror: bool) -> None:
    if mirror:
        sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
    sprite = sprite.resize((round(sprite.width * scale), round(sprite.height * scale)), Image.NEAREST)
    shadow = Image.new("RGBA", sprite.size, (0, 0, 0, 0))
    shadow.paste((0, 0, 0, 150), mask=sprite.split()[3])
    base.paste(shadow, (x + 4, bottom - sprite.height + 3), shadow)
    base.paste(sprite, (x, bottom - sprite.height), sprite)


def pixel_text(base: Image.Image, label: str, xy: tuple[int, int], size: int, scale: int, fill=WHITE) -> None:
    """Large blocky text: drawn small into a mask, then scaled up without smoothing."""
    f = font(size)
    probe = ImageDraw.Draw(Image.new("L", (1, 1)))
    left, top, right, bottom = probe.textbbox((0, 0), label, font=f)
    mask = Image.new("L", (right + 4, bottom + 4), 0)
    ImageDraw.Draw(mask).text((2, 2), label, font=f, fill=255)
    mask = mask.resize((mask.width * scale, mask.height * scale), Image.NEAREST)
    shade = Image.new("RGB", mask.size, (0, 0, 0))
    base.paste(shade, (xy[0] + scale, xy[1] + scale), mask)
    base.paste(Image.new("RGB", mask.size, fill), xy, mask)


def title_frame() -> Image.Image:
    frame = vignette(bars(arena("stadium", .55), (70, 110, 200)), .8)
    pixel_text(frame, "WAR PRESENTS", (88, 18), 10, 2, (255, 190, 90))
    pixel_text(frame, "OMF 2115", (50, 46), 16, 3)
    return frame


def card_frame(pilot: str, title: str, color: tuple[int, int, int], right: bool) -> Image.Image:
    frame = vignette(bars(arena("stadium", .5), color, flip=right), .7)
    face = portrait(pilot, 1.9, color)
    x = W - face.width - 34 if right else 34
    paste_shadowed(frame, face, (x, 6))
    plate(frame, title, 190 if not right else 40, 82, 112, color)
    return frame


def faceoff_frame(player_har: str, rival_har: str, tmp: Path) -> Image.Image:
    frame = Image.new("RGB", (W, H))
    left = bars(arena("stadium", .5), CYAN)
    right = bars(arena("stadium", .5), ORANGE, flip=True)
    split = Image.new("L", (W, H), 0)
    ImageDraw.Draw(split).polygon([(W // 2 + 14, 0), (W, 0), (W, H), (W // 2 - 14, H)], fill=255)
    frame = vignette(Image.composite(right, left, split), .7)
    draw = ImageDraw.Draw(frame)
    draw.polygon([(W // 2 + 14, 0), (W // 2 + 20, 0), (W // 2 - 8, H), (W // 2 - 14, H)], fill=WHITE)   # the dividing slash
    crystal, christian = portrait("Crystal", .75, CYAN), portrait("Christian", .75, ORANGE)
    paste_shadowed(frame, crystal, (8, 6))
    paste_shadowed(frame, christian, (W - 8 - christian.width, 6))
    player, rival = har_sprite(player_har, tmp), har_sprite(rival_har, tmp)
    paste_sprite(frame, player, 1.0, 144 - player.width, H - 4, mirror=False)    # right edge just left of the slash
    paste_sprite(frame, rival, 1.0, 176, H - 4, mirror=True)                       # left edge just right of it
    pixel_text(frame, "VS", (139, 8), 14, 2, (255, 220, 120))
    return frame


def main() -> int:
    for needed in (AFTOOL, PORTRAITS / "Crystal.bmp", BACKDROPS / "stadium.bmp"):
        if not needed.exists():
            print(f"Missing {needed} (run export_story_assets.py first)", file=sys.stderr)
            return 1
    ART.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        frames = {
            "stadium_title": title_frame(),
            "crystal_card": card_frame("Crystal", "CRYSTAL DEVROE", CYAN, right=False),
            "christian_card": card_frame("Christian", "CHRISTIAN DEVROE", ORANGE, right=True),
            "faceoff_jaguar": faceoff_frame("jaguar", "shadow", Path(tmp)),
            "faceoff_shadow": faceoff_frame("shadow", "jaguar", Path(tmp)),
        }
    for name, frame in frames.items():
        frame.save(ART / f"{name}.bmp")
    print(f"Wrote {len(frames)} illustration frames to {ART}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
