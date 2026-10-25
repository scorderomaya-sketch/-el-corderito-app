#!/usr/bin/env python3
"""Build El Corderito launcher icons from the approved head-on-cream mascot.

The source of truth is the inline WebP used by the web app header. No external
image, repository token, or network request is required during icon generation.
"""
from __future__ import annotations

import base64
import io
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
RES = ROOT / "android/app/src/main/res"

html = HTML.read_text(encoding="utf-8")
found = re.search(r"data:image/webp;base64,([A-Za-z0-9+/=]+)", html)
if not found:
    raise SystemExit("Mascot WebP not found in index.html")

image = Image.open(io.BytesIO(base64.b64decode(found.group(1)))).convert("RGBA")
if min(image.size) < 64:
    raise SystemExit("Mascot source unexpectedly small")
print(f"Approved mascot source: {image.width}x{image.height}")

CREAM = (251, 247, 237, 255)
def resample(size: int) -> Image.Image:
    pic = image.resize((size, size), Image.Resampling.LANCZOS)
    return ImageEnhance.Sharpness(pic).enhance(1.15)

# The Android adaptive icon mask owns the background color.
front = Image.new("RGBA", (432, 432), (0, 0, 0, 0))
art = resample(292)
front.alpha_composite(art, (70, 70))
out = RES / "drawable-nodpi/ic_launcher_fg.png"
out.parent.mkdir(parents=True, exist_ok=True)
front.save(out, optimize=True)

# Legacy icons for Android 8+ and launchers that do not support adaptive icons.
for qualifier, size in [
    ("mipmap-mdpi", 48), ("mipmap-hdpi", 72),
    ("mipmap-xhdpi", 96), ("mipmap-xxhdpi", 144),
    ("mipmap-xxxhdpi", 192),
]:
    canvas = Image.new("RGBA", (512, 512), CREAM)
    art = resample(472)
    canvas.alpha_composite(art, (20, 20))
    mask = Image.new("L", (512, 512))
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, 511, 511), radius=112, fill=255)
    canvas.putalpha(mask)
    output = RES / qualifier / "ic_launcher.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.resize((size, size), Image.Resampling.LANCZOS).save(output, optimize=True)
    print(f"Created {output.relative_to(ROOT)}")

print("Approved lamb-head icons ready")
