"""Compose the story's illustrated-sequence frames from original-game art, into the git-ignored project/build/art.

Frames are 320x124 pixels, the shape of the story viewer's art area. They are built from material already exported by
export_story_assets.py (pilot portraits, arena backgrounds) plus the HAR idle sprites exported here with aftool, with
diagonal colour bars, a vignette, and name plates drawn on top.

  stadium_title        the arena under the tournament title
  crystal_card         Crystal's portrait on cyan bars
  christian_card       Christian's portrait on orange bars
  faceoff_jaguar       Crystal in Jaguar (left) against Christian in Shadow (right)
  faceoff_shadow       Crystal in Shadow (left) against Christian in Jaguar (right)
  faceoff_katana       Crystal in Katana (left) against Christian in Jaguar (right)
  ending_crystal       Crystal's ending card, on the Desert sunset
  ending_christian     Christian's ending card
  ending_together      the siblings side by side (they faced it together)
  ending_apart         the siblings far apart under a dividing slash (they did not)
  ending_title         "END OF SLICE"
  bay_<pilot>_<har>    the VS-screen hangar before the match: the player's pilot in that HAR (left) against the other
                       sibling in the other HAR (right); four frames (crystal or christian, jaguar or shadow)
  news_<pilot>         the newsroom after the match (drawn here, with the anchor Alex), with that pilot on the news screen as the winner
  wreck_<har>_<result> the repair bay after the match: the damaged HARs, the player's (left) in that HAR, and the result
                       (won or lost) from the player's side; four frames (jaguar or shadow, won or lost)

The result is original-game material rearranged for local development, never committed or distributed (see
project/docs/ASSET_LEDGER.md). Normally run through export_story_assets.py.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "build" / "omf_debug_z7"
AFTOOL = BUILD / "aftool.exe"
GAME = ROOT / "OMF2097"
PORTRAITS = ROOT / "project" / "build" / "portraits"
BACKDROPS = ROOT / "project" / "build" / "backdrops"
SCENES = ROOT / "project" / "build" / "scenes"   # vs.bmp and newsroom.bmp, exported by export_story_assets.py
ART = ROOT / "project" / "build" / "art"

W, H = 320, 124
CYAN = (60, 200, 255)
ORANGE = (255, 140, 70)
WHITE = (240, 245, 255)

# Idle stance (animation 11, sprite 0) of each HAR's FIGHTR<id>.AF file; the HAR id is the file number.
HAR_FILE = {"jaguar": 0, "shadow": 1, "katana": 5}
# The HAR each takes against it in the story (never the player's own), as in the viewer's selection screen.
RIVAL_OF = {"jaguar": "shadow", "shadow": "jaguar", "katana": "jaguar"}


def font(size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.load_default(size=size)
    except TypeError:        # older Pillow: the fixed-size bitmap font
        return ImageFont.load_default()


def arena(name: str, brightness: float, shift: int = 0) -> Image.Image:
    """The arena picture cropped to the frame; a negative shift moves the crop up the picture."""
    image = Image.open(BACKDROPS / f"{name}.bmp").convert("RGB")
    top = max(0, min(image.height - H, (image.height - H) // 2 + shift))
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


def har_sprite(har: str, tmp: Path, animation: int = 11, sprite: int = 0) -> Image.Image:
    png = tmp / f"{har}-{animation}-{sprite}.png"
    result = subprocess.run(
        [str(AFTOOL), "-f", str(GAME / f"FIGHTR{HAR_FILE[har]}.AF"), "-p", str(GAME / "ARENA0.BK"), "-m", str(animation),
         "-s", str(sprite), f"--export-png={png}"], capture_output=True, text=True)
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


def card_frame(pilot: str, title: str, color: tuple[int, int, int], right: bool, backdrop: str = "stadium",
               brightness: float = .5) -> Image.Image:
    frame = vignette(bars(arena(backdrop, brightness, shift=-16 if backdrop == "desert" else 0), color, flip=right), .7)
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


def sunset(brightness: float = .8) -> Image.Image:
    """The Desert arena's sky and dunes: the warm backdrop for the endings."""
    return arena("desert", brightness, shift=-16)


def ending_together_frame() -> Image.Image:
    frame = vignette(bars(sunset(), (255, 170, 90)), .6)
    crystal, christian = portrait("Crystal", 1.5, CYAN), portrait("Christian", 1.5, ORANGE)
    paste_shadowed(frame, crystal, (W // 2 - crystal.width - 4, 14))
    paste_shadowed(frame, christian, (W // 2 + 4, 14))
    return frame


def ending_apart_frame() -> Image.Image:
    frame = vignette(sunset(.6), .75)
    draw = ImageDraw.Draw(frame)
    draw.polygon([(W // 2 + 6, 0), (W // 2 + 12, 0), (W // 2 - 6, H), (W // 2 - 12, H)], fill=WHITE)   # the dividing slash
    paste_shadowed(frame, portrait("Crystal", 1.5, CYAN), (18, 14))
    christian = portrait("Christian", 1.5, ORANGE)
    paste_shadowed(frame, christian, (W - 18 - christian.width, 14))
    return frame


def ending_title_frame() -> Image.Image:
    frame = vignette(sunset(.6), .8)
    pixel_text(frame, "END OF SLICE", (30, 34), 20, 2)
    pixel_text(frame, "OMF 2115", (110, 88), 10, 2, (255, 190, 90))
    return frame


PILOT_COLOR = {"crystal": CYAN, "christian": ORANGE}


def hangar_frame(player: str, player_har: str, tmp: Path) -> Image.Image:
    """The VS-screen hangar bay, mirrored to fill the frame, with the two HARs facing each other."""
    rival = "christian" if player == "crystal" else "crystal"
    rival_har = RIVAL_OF[player_har]
    bay = Image.open(SCENES / "vs.bmp").convert("RGB").crop((0, 12, 150, 12 + H)).resize((W // 2, H), Image.NEAREST)
    frame = Image.new("RGB", (W, H))
    frame.paste(bay, (0, 0))
    frame.paste(bay.transpose(Image.FLIP_LEFT_RIGHT), (W // 2, 0))
    frame = vignette(ImageEnhance.Brightness(frame).enhance(.8), .6)
    left, right = PILOT_COLOR[player], PILOT_COLOR[rival]
    paste_sprite(frame, har_sprite(player_har, tmp), 1.1, 72, H - 4, mirror=False)
    sprite = har_sprite(rival_har, tmp)
    paste_sprite(frame, sprite, 1.1, W - 72 - round(sprite.width * 1.1), H - 4, mirror=True)
    for who, color, x in ((player, left, 8), (rival, right, None)):
        face = portrait(who.capitalize(), .75, color)
        x = x if x is not None else W - 8 - face.width
        paste_shadowed(frame, face, (x, 6))
    plate(frame, player.upper(), 10, 56, 68, left)
    plate(frame, rival.upper(), W - 78, 56, 68, right)
    pixel_text(frame, "VS", (139, 8), 14, 2, (255, 220, 120))
    return frame


# The newsroom set, drawn for this project (no original art): a cream studio wall of tilted "WRDE NEWS" lettering, the
# news screen where the winner appears, and the anchor Alex, a nonbinary, androgynous presenter. It is 320x200 like the
# original picture it replaced, with the screen at the same place, so news_frame can crop it the same way.
NEWS_SCREEN = (163, 13, 307, 116)    # left, top, right, bottom of the black news screen, in set pixels
SKIN = (233, 190, 152)
SKIN_SHADE = (205, 154, 120)
HAIR = (88, 60, 58)
HAIR_LIGHT = (140, 98, 88)
JACKET = (40, 196, 204)
JACKET_SHADE = (20, 140, 156)
OUTLINE = (50, 30, 30)


def newsroom_wall() -> Image.Image:
    wall = np.zeros((200, 320, 3), np.float32)
    yy, xx = np.mgrid[0:200, 0:320]
    glow = np.clip(1.0 - np.hypot((xx - 160) / 260.0, (yy - 90) / 190.0), 0, 1)   # lighter toward the middle
    wall[:] = (226, 220, 164)
    wall += glow[..., None] * np.array([18, 18, 22], np.float32)
    layer = Image.new("RGBA", (520, 520), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    f = font(22)
    colours = [(196, 36, 48), (40, 48, 170), (120, 40, 140)]
    for row in range(-1, 12):
        for column in range(-1, 6):
            word = "WRDE" if (row + column) % 2 == 0 else "NEWS"
            offset = 46 if row % 2 else 0
            draw.text((column * 108 + offset, row * 44), word, font=f, fill=colours[(row + 2 * column) % 3] + (215,))
    layer = layer.rotate(-24, resample=Image.BICUBIC).crop((100, 100, 420, 300))
    base = Image.fromarray(np.clip(wall, 0, 255).astype(np.uint8)).convert("RGBA")
    return Image.alpha_composite(base, layer).convert("RGB")


def anchor_alex(image: Image.Image) -> None:
    """Alex: a short layered cut swept to one side, a soft jaw, a tailored teal jacket with a high collar, a small stud."""
    d = ImageDraw.Draw(image)
    cx = 84
    # Shoulders and jacket, with a pale shirt and a high collar.
    d.polygon([(10, 200), (22, 150), (52, 134), (116, 134), (146, 150), (158, 200)], fill=JACKET, outline=OUTLINE)
    d.polygon([(10, 200), (22, 150), (40, 144), (44, 200)], fill=JACKET_SHADE)
    d.polygon([(66, 134), (102, 134), (96, 200), (72, 200)], fill=(236, 240, 244))                  # shirt
    d.polygon([(52, 134), (68, 134), (80, 176), (62, 200), (44, 200), (40, 150)], fill=JACKET_SHADE, outline=OUTLINE)   # lapels
    d.polygon([(116, 134), (100, 134), (88, 176), (106, 200), (124, 200), (128, 150)], fill=JACKET, outline=OUTLINE)
    d.polygon([(62, 126), (106, 126), (102, 140), (66, 140)], fill=(246, 248, 250), outline=OUTLINE)   # collar
    d.ellipse((112, 160, 122, 170), fill=(255, 196, 60), outline=OUTLINE)                               # a small pin
    # Neck.
    d.polygon([(70, 108), (98, 108), (100, 132), (68, 132)], fill=SKIN)
    d.polygon([(70, 108), (98, 108), (98, 120), (70, 124)], fill=SKIN_SHADE)
    # Hair behind the head, then the face.
    d.ellipse((44, 22, 126, 108), fill=HAIR, outline=OUTLINE)
    d.polygon([(48, 80), (120, 80), (118, 106), (50, 106)], fill=HAIR)
    d.ellipse((52, 40, 116, 122), fill=SKIN, outline=OUTLINE)
    d.polygon([(56, 98), (112, 98), (100, 118), (68, 118)], fill=SKIN)                               # a soft, narrow jaw
    d.polygon([(106, 52), (114, 76), (112, 100), (100, 116), (104, 90)], fill=SKIN_SHADE)             # shade on one side of the face
    # Ears, and a stud.
    d.ellipse((46, 76, 56, 96), fill=SKIN, outline=OUTLINE)
    d.ellipse((112, 76, 122, 96), fill=SKIN_SHADE, outline=OUTLINE)
    d.ellipse((48, 94, 53, 99), fill=(255, 196, 60))
    # The fringe: layered and swept across the forehead from one side.
    d.pieslice((46, 24, 124, 100), 180, 330, fill=HAIR, outline=OUTLINE)
    d.polygon([(48, 72), (54, 44), (80, 30), (112, 40), (118, 62), (100, 52), (84, 58), (66, 68), (56, 86)], fill=HAIR)
    d.polygon([(70, 34), (96, 30), (108, 40), (90, 42), (72, 46)], fill=HAIR_LIGHT)
    d.polygon([(52, 74), (46, 96), (54, 104), (58, 84)], fill=HAIR)
    # Face: level brows, almond eyes, a straight nose and a calm, slight smile.
    for ex in (68, 98):
        d.polygon([(ex - 9, 70), (ex + 9, 68), (ex + 9, 72), (ex - 9, 74)], fill=HAIR)                  # brow
        d.polygon([(ex - 9, 80), (ex, 75), (ex + 9, 80), (ex, 85)], fill=(250, 250, 250), outline=OUTLINE)   # eye
        d.ellipse((ex - 4, 76, ex + 4, 84), fill=(54, 118, 96))                                            # iris
        d.ellipse((ex - 2, 78, ex + 2, 82), fill=(18, 24, 24))
        d.point((ex + 2, 77), fill=(255, 255, 255))
    d.line([(cx + 2, 84), (cx - 1, 98), (cx + 4, 100)], fill=SKIN_SHADE, width=2)                       # nose
    d.polygon([(72, 106), (cx, 109), (96, 106), (cx, 112)], fill=(206, 118, 112))                       # lips
    d.line([(74, 106), (cx, 108), (94, 105)], fill=OUTLINE, width=1)


def newsroom_set() -> Image.Image:
    image = newsroom_wall()
    layer = Image.new("RGBA", (320, 200), (0, 0, 0, 0))
    anchor_alex(layer)                                           # drawn large, then scaled so the head and jacket both fit the frame
    figure = layer.crop((8, 20, 162, 200)).resize((126, 147), Image.LANCZOS)
    image.paste(figure, (16, 30), figure)
    d = ImageDraw.Draw(image)
    d.rectangle(NEWS_SCREEN, fill=(0, 0, 0), outline=(30, 30, 230), width=3)
    return image


def news_frame(winner: str) -> Image.Image:
    """The newsroom set, the winner's portrait on the news screen and a name plate under it."""
    frame = newsroom_set().crop((0, 10, W, 10 + H))
    color = PILOT_COLOR[winner]
    face = portrait(winner.capitalize(), 1.7, color)
    screen = (165, 5, 305, 104)   # the black screen of the original picture, in frame pixels
    frame.paste(face, ((screen[0] + screen[2] - face.width) // 2, (screen[1] + screen[3] - face.height) // 2))
    plate(frame, f"{winner.upper()} WINS", 172, 106, 130, color)
    return frame


# The original sprites for being hit (animation 9, sprite 5) and for lying defeated (animation 49; Jaguar's sprite 3,
# Shadow's sprite 0, as listed in project/docs/OMF2097/poses).
HIT_POSE = (9, 5)
DEFEAT_POSE = {"jaguar": (49, 3), "shadow": (49, 0), "katana": (49, 0)}


def damaged(sprite: Image.Image, seed: int) -> Image.Image:
    """Scorches, dents and a burnt orange edge on a HAR sprite: dark patches in its plating and glowing seams."""
    rng = np.random.default_rng(seed)
    pixels = np.asarray(sprite).astype(np.float32)
    alpha = pixels[..., 3] > 0
    noise = ndimage.gaussian_filter(rng.random(alpha.shape).astype(np.float32), 1.6)
    noise = (noise - noise.min()) / (noise.max() - noise.min() + 1e-6)
    burn = np.clip((noise - .52) * 4.0, 0, 1) * alpha            # soot patches
    crack = ndimage.gaussian_filter(rng.random(alpha.shape).astype(np.float32), .6)
    crack = (crack > np.quantile(crack[alpha], .965)) & alpha   # a scatter of fine dark cracks
    for c in range(3):
        pixels[..., c] *= 1.0 - .62 * burn
    pixels[crack, :3] *= .35
    edge = alpha & ~ndimage.binary_erosion(alpha, iterations=1)
    hot = edge & (noise > .50)                                  # orange glow along some of the edges
    pixels[hot, 0] = np.minimum(255, pixels[hot, 0] * .5 + 190)
    pixels[hot, 1] = np.minimum(255, pixels[hot, 1] * .5 + 80)
    return Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8), "RGBA")


def smoke(frame: Image.Image, x: int, y: int, seed: int) -> Image.Image:
    """A few soft grey puffs rising from (x, y), blended over the frame."""
    rng = np.random.default_rng(seed)
    layer = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for i in range(7):
        r = 5 + i * 2 + int(rng.integers(0, 4))
        cx = x + int(rng.integers(-5, 6)) + i * int(rng.integers(-2, 3))
        cy = y - i * 9
        shade = 150 - i * 8
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(shade, shade, shade + 6, max(50, 175 - i * 16)))
    return Image.alpha_composite(frame.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(4))).convert("RGB")


def sparks(frame: Image.Image, x: int, y: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    draw = ImageDraw.Draw(frame)
    for _ in range(9):
        angle = rng.uniform(-3.14, 0)
        length = rng.uniform(4, 14)
        x2, y2 = x + np.cos(angle) * length, y + np.sin(angle) * length
        draw.line((x, y, x2, y2), fill=(255, int(rng.integers(150, 230)), 70), width=1)


def wreck_frame(player_har: str, result: str, tmp: Path) -> Image.Image:
    """The repair bay after the match. The winner stands battered; the loser lies where it fell."""
    rival_har = RIVAL_OF[player_har]
    bay = Image.open(SCENES / "vs.bmp").convert("RGB").crop((0, 12, 150, 12 + H)).resize((W // 2, H), Image.NEAREST)
    frame = Image.new("RGB", (W, H))
    frame.paste(bay, (0, 0))
    frame.paste(bay.transpose(Image.FLIP_LEFT_RIGHT), (W // 2, 0))
    frame = ImageEnhance.Brightness(frame).enhance(.5)
    tint = Image.new("RGB", frame.size, (255, 150, 95))          # emergency lighting
    frame = Image.blend(frame, ImageChops.multiply(frame, tint), .75)
    frame = vignette(frame, .75)
    winner_is_player = result == "won"
    for index, (har, left) in enumerate(((player_har, True), (rival_har, False))):
        standing = (har == player_har) == winner_is_player
        animation, sprite = HIT_POSE if standing else DEFEAT_POSE[har]
        art = damaged(har_sprite(har, tmp, animation, sprite), seed=index + 7 + (3 if standing else 0))
        scale = 1.15
        width = round(art.width * scale)
        inset = 18 if not standing else 70               # the fallen one lies toward the edge, clear of the standing one
        x = inset if left else W - inset - width
        if not left:
            art = art.transpose(Image.FLIP_LEFT_RIGHT)
        paste_sprite(frame, art, scale, x, H - 6, mirror=False)
        top = H - 6 - round(art.height * scale)
        frame = smoke(frame, x + width // 2, max(34, top + 10), seed=11 + index)
        sparks(frame, x + width // 2, top + round(art.height * scale * .35), seed=21 + index)
    pixel_text(frame, "REPAIR BAY", (92, 8), 12, 2, (255, 170, 90))
    return frame


def main() -> int:
    for needed in (AFTOOL, PORTRAITS / "Crystal.bmp", BACKDROPS / "stadium.bmp", SCENES / "vs.bmp"):
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
            "faceoff_katana": faceoff_frame("katana", "jaguar", Path(tmp)),
            "ending_crystal": card_frame("Crystal", "CRYSTAL DEVROE", CYAN, right=False, backdrop="desert", brightness=.8),
            "ending_christian": card_frame("Christian", "CHRISTIAN DEVROE", ORANGE, right=True, backdrop="desert",
                                           brightness=.8),
            "ending_together": ending_together_frame(),
            "ending_apart": ending_apart_frame(),
            "ending_title": ending_title_frame(),
            "news_crystal": news_frame("crystal"),
            "news_christian": news_frame("christian"),
        }
        for har in ("jaguar", "shadow", "katana"):
            for result in ("won", "lost"):
                frames[f"wreck_{har}_{result}"] = wreck_frame(har, result, Path(tmp))
        for pilot in ("crystal", "christian"):
            for har in ("jaguar", "shadow", "katana"):
                frames[f"bay_{pilot}_{har}"] = hangar_frame(pilot, har, Path(tmp))
    for name, frame in frames.items():
        frame.save(ART / f"{name}.bmp")
    print(f"Wrote {len(frames)} illustration frames to {ART}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
