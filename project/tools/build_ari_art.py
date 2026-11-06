"""Build the Ari Chapter 1 story frames from the generated renders in project/renders into project/build/art.

Each frame is the story viewer's art shape: 320x124 (<name>.bmp) plus a 1280x496 copy (<name>_hd.bmp).
  ari_ch1_nova_lab    the ruined Nova laboratory, 2097 (the archive montage)
  ari_ch1_ganymede    the Ganymede colony under Jupiter (the construction montage)
  ari_ch1_arena       the arena as broadcast (the opening of the match)
  ari_ch1_station, _gala, _tech, _arena_main, _arena_day, _med   the generated backgrounds (BG-* renders)
  <name>_cut          a cut-out portrait (head and torso, 32-bit with alpha) for the story's present command, for ari, selene,
                       mara, crystal, steffan, ren, angel, shirro, alex, leena, lyra, dante, varga,
                       haldane, christian, jeanpaul, raven and milano
  ari_card, selene_card, mara_card, ari_ch1_card_<name>   a name card for each character: the render's head and torso
                       on dark colour bars (crystal, steffan, ren, angel, shirro, alex, leena)

The renders are generated images kept in project/renders. Run: python project/tools/build_ari_art.py
"""
from __future__ import annotations

from pathlib import Path

import struct

import numpy as np
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
RENDERS = ROOT / "project" / "renders"
ART = ROOT / "project" / "build" / "art"
W, H = 1280, 496

SCENES = {
    "ari_ch1_nova_lab": "art_nova_lab_2097.png",
    "ari_ch1_ganymede": "art_ganymede_colony.png",
    "ari_ch1_arena": "art_arena_broadcast.png",
    "ari_ch1_station": "BG-EXT-STATION_BASE.png",
    "ari_ch1_gala": "BG-SOC-GALA_NIGHT.png",
    "ari_ch1_tech": "BG-TEC-EXPERIMENT_NIGHT.png",
    "ari_ch1_arena_main": "BG-ARE-MAIN_BASE.png",
    "ari_ch1_arena_day": "BG-ARE-MAIN_DAY.png",
    "ari_ch1_med": "BG-ARE-MED_BASE.png",
    "ari_fs_five_seconds": "fs_ari_five_seconds.png",   # optional scene 5B (ch3_towel)
}
CARDS = {  # name: (render, title, bar colour, figure on the right)
    "ari_card": ("ari_solano.png", "ARI SOLANO", (200, 90, 40), False),
    "selene_card": ("selene_vale.png", "SELENE VALE", (120, 70, 190), True),
    "mara_card": ("mara_voss.png", "MARA VOSS", (60, 150, 140), False),
    "ari_ch1_card_crystal": ("crystal_devroe.png", "CRYSTAL DEVROE", (190, 40, 60), True),
    "ari_ch1_card_steffan": ("steffan_thomas.png", "STEFFAN THOMAS", (230, 120, 30), False),
    "ari_ch1_card_ren": ("ren_akiyama.png", "REN AKIYAMA", (70, 130, 220), True),
    "ari_ch1_card_angel": ("angel.png", "ANGEL", (60, 160, 200), False),
    "ari_ch1_card_shirro": ("shirro.png", "SHIRRO", (220, 170, 40), True),
    "ari_ch1_card_alex": ("alex.png", "ALEX", (150, 150, 200), False),
    "ari_ch1_card_leena": ("leena_sato.png", "LEENA SATO", (60, 170, 110), True),
}


def save(img: Image.Image, name: str) -> None:
    ART.mkdir(parents=True, exist_ok=True)
    img = img.convert("RGB").resize((W, H), Image.LANCZOS)
    img.save(ART / f"{name}_hd.bmp")
    img.resize((320, 124), Image.LANCZOS).save(ART / f"{name}.bmp")


def scene(src: str) -> Image.Image:
    im = Image.open(RENDERS / src).convert("RGB")
    h = int(im.width * H / W)
    top = (im.height - h) // 2
    return im.crop((0, top, im.width, top + h))


LEFT_TRIM = {"ari_ch1_card_ren": 0.3}   # Ren's sheet has a larger sliver of the neighbouring figure


def card(src: str, title: str, color, right: bool, left_trim: float = 0.09) -> Image.Image:
    fig, fig_alpha = load_fig(src)
    # head and torso: the 1024x1536 renders show about a third of the height; the tall 768x2880 sheets need a taller slice
    crop_h = int(fig.width * 1.45) if fig.height > 2 * fig.width else int(fig.width * H / W * 1.6)
    tall = fig.height > 2 * fig.width            # the sheets carry slivers of the next figure
    trim_l, trim_r = (int(fig.width * left_trim), int(fig.width * 0.09)) if tall else (0, 0)
    box = (trim_l, 0, fig.width - trim_r, crop_h)
    fig = fig.crop(box)
    if fig_alpha is not None:
        fig_alpha = fig_alpha.crop(box)
    size = (int(fig.width * H / crop_h), H)
    fig = fig.resize(size)   # width here is already the trimmed width
    bg = np.zeros((H, W, 3), np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    bars = (((xx + (W if right else 0) * 0 + yy * 0.9) // 90) % 2).astype(np.float32)
    for c in range(3):
        bg[..., c] = 12 + bars * 0.30 * color[c] + 0.05 * color[c]
    arr = np.asarray(fig, np.float32)
    if fig_alpha is not None:
        mask = fig_alpha.resize(size).filter(ImageFilter.GaussianBlur(1.0))
    else:
        white = np.clip((arr.min(axis=2) - 185) / 35.0, 0, 1)           # near-white studio backdrop
        mask = Image.fromarray(((1 - white) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
    out = Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8))
    x = W - fig.width - 80 if right else 80
    out.paste(fig, (x, 0), mask)
    d = ImageDraw.Draw(out)
    try:
        font = ImageFont.truetype("arialbd.ttf", 64)
    except OSError:
        font = ImageFont.load_default()
    tx = 70 if right else W - 70
    d.text((tx, H - 90), title, font=font, fill=(255, 255, 255), anchor="ls" if right else "rs",
           stroke_width=4, stroke_fill=(0, 0, 0))
    return out


CUTS = {  # name: render
    "ari": "ari_solano.png",
    "selene": "selene_vale.png",
    "mara": "mara_voss.png",
    "crystal": "crystal_devroe.png",
    "steffan": "steffan_thomas.png",
    "ren": "ren_akiyama.png",
    "angel": "angel.png",
    "shirro": "shirro.png",
    "alex": "alex.png",
    "leena": "leena_sato.png",
    "lyra": "lyra.png",
    "dante": "dante.png",
    "varga": "varga.png",
    "haldane": "haldane.png",
    "christian": "christian_devroe.png",
    "jeanpaul": "jean_paul.png",
    "raven": "raven.png",
    "milano": "milano.png",
}


def load_fig(src: str) -> tuple[Image.Image, Image.Image | None]:
    """The render as RGB, plus its alpha channel when the PNG carries a real transparent backdrop (else None)."""
    im = Image.open(RENDERS / src)
    if im.mode in ("RGBA", "LA") and im.getchannel("A").getextrema()[0] < 250:
        im = im.convert("RGBA")
        return im.convert("RGB"), im.getchannel("A")
    return im.convert("RGB"), None


def cutout(src: str, left_trim: float = 0.09) -> Image.Image:
    """Head and torso with the studio backdrop removed: only white connected to the picture's border goes transparent,
    so white clothing survives."""
    fig, fig_alpha = load_fig(src)
    tall = fig.height > 2 * fig.width
    crop_h = int(fig.width * (1.45 if tall else 0.82))   # tall sheets are 3:11, the others 2:3: head to chest or hip
    trim_l, trim_r = (int(fig.width * left_trim), int(fig.width * 0.09)) if tall else (0, 0)
    box = (trim_l, 0, fig.width - trim_r, min(crop_h, fig.height))
    fig = fig.crop(box)
    arr = np.asarray(fig, np.float32)
    if fig_alpha is not None:                                               # a transparent PNG: use its own alpha
        out = np.dstack([arr, np.asarray(fig_alpha.crop(box), np.float32)]).astype(np.uint8)
        img = Image.fromarray(out, "RGBA")
        scale = 1024 / img.height if img.height > 1024 else 1.0
        return img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS) if scale < 1 else img
    edge_px = arr[:3].reshape(-1, 3)                                        # the top rows: the figure never reaches them
    backdrop = np.median(edge_px, axis=0)                                  # the studio colour, whatever its tint
    near_white = (np.abs(arr - backdrop).max(axis=2) <= 24) & (arr.min(axis=2) >= 170)
    labels, _ = ndimage.label(near_white)
    border = np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]]))
    background = np.isin(labels, border[border > 0])
    alpha = ndimage.gaussian_filter((~background).astype(np.float32), 1.2)
    alpha = np.clip((alpha - 0.25) / 0.5, 0, 1)
    a3 = np.maximum(alpha, 1e-3)[..., None]
    rgb = np.clip((arr - (1 - alpha[..., None]) * 255.0) / a3, 0, 255)   # remove the white fringe from soft edges
    out = np.dstack([rgb, alpha * 255]).astype(np.uint8)
    img = Image.fromarray(out, "RGBA")
    scale = 1024 / img.height if img.height > 1024 else 1.0
    return img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS) if scale < 1 else img


def save_bmp32(img: Image.Image, path: Path) -> None:
    """A 32-bit BMP with an alpha channel (BITMAPV4HEADER with channel masks), which SDL reads as RGBA."""
    w, h = img.size
    bgra = np.asarray(img.convert("RGBA"))[:, :, [2, 1, 0, 3]][::-1].tobytes()   # bottom-up rows
    header = struct.pack("<2sIHHI", b"BM", 14 + 108 + len(bgra), 0, 0, 14 + 108)
    v4 = struct.pack("<IiiHHIIiiII", 108, w, h, 1, 32, 3, len(bgra), 2835, 2835, 0, 0)
    v4 += struct.pack("<IIII", 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000) + struct.pack("<I", 0x73524742) + bytes(48)
    path.write_bytes(header + v4 + bgra)


def check_renders() -> None:
    """Stop before building anything if a render the tables name is missing (a rename would otherwise fail midway)."""
    names = set(SCENES.values()) | {v[0] for v in CARDS.values()} | set(CUTS.values())
    missing = sorted(n for n in names if not (RENDERS / n).is_file())
    if missing:
        raise SystemExit("missing renders in " + str(RENDERS) + ": " + ", ".join(missing))


def main() -> None:
    check_renders()
    for name, src in SCENES.items():
        save(scene(src), name)
    for name, (src, title, color, right) in CARDS.items():
        save(card(src, title, color, right, LEFT_TRIM.get(name, 0.09)), name)
    for name, src in CUTS.items():
        save_bmp32(cutout(src, LEFT_TRIM.get(f"ari_ch1_card_{name}", 0.09)), ART / f"{name}_cut.bmp")
    print("wrote", len(SCENES) + len(CARDS), "frames and", len(CUTS), "cut-outs to", ART)


if __name__ == "__main__":
    main()
