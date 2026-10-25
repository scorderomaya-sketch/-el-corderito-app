#!/usr/bin/env python3
"""Generate adaptive, legacy and Android splash icons from high-resolution vector.

The source asset was traced from the user's original 1254x1254 mascot.
Unlike the previous inline WebP thumbnail, it can be rasterized at any scale.
This script deliberately fails if the vector asset is missing or malformed.
"""
from __future__ import annotations

import base64
import io
import zlib
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "android/app/src/main/res"
SOURCE = ROOT / "assets/corderito_head_vector.zlib.b64"
CREAM = (254, 248, 234, 255)

encoded = SOURCE.read_text(encoding="ascii").strip()
svg = zlib.decompress(base64.b64decode(encoded, validate=True))
if b'viewBox="0 0 640 640"' not in svg or b'<path' not in svg:
    raise SystemExit("The high-resolution mascot vector is invalid")

# Render at 2048 to preserve crisp contours in high-density Android launchers
# and on the system-managed Android 12+ splash screen.
png = cairosvg.svg2png(bytestring=svg, output_width=2048, output_height=2048)
image = Image.open(io.BytesIO(png)).convert("RGBA")
assert image.size == (2048, 2048)
print(f"High-resolution mascot source: vector → {image.width}×{image.height}")

def resample(size: int) -> Image.Image:
    picture = image.resize((size, size), Image.Resampling.LANCZOS)
    return picture

# Adaptive icon 108×108dp at Android xxhdpi/xxxhdpi.
# The 432×432 resource keeps the lamb entirely inside the launcher-safe zone.
foreground = Image.new("RGBA", (432, 432), (0, 0, 0, 0))
foreground.alpha_composite(resample(306), (63, 63))
out = RES / "drawable-nodpi/ic_launcher_fg.png"
out.parent.mkdir(parents=True, exist_ok=True)
foreground.save(out, optimize=True)

# Legacy icon sizes for launchers that don't use Android adaptive icons.
for qualifier, size in [
    ("mipmap-mdpi", 48), ("mipmap-hdpi", 72),
    ("mipmap-xhdpi", 96), ("mipmap-xxhdpi", 144),
    ("mipmap-xxxhdpi", 192),
]:
    canvas = Image.new("RGBA", (512, 512), CREAM)
    art = resample(474)
    canvas.alpha_composite(art, (19, 19))
    mask = Image.new("L", (512, 512))
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 511, 511), radius=112, fill=255)
    canvas.putalpha(mask)
    output = RES / qualifier / "ic_launcher.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.resize((size, size), Image.Resampling.LANCZOS).save(output, optimize=True)
    print(f"Created {output.relative_to(ROOT)}")

print("High-resolution Android mascot icons generated")
