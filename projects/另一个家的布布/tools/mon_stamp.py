"""Burn a surveillance timestamp into the monitor still (post, not AI): python mon_stamp.py IN OUT "客厅 06-12 23:24:07" """
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
im = Image.open(sys.argv[1]).convert("RGB"); W, H = im.size
font = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", int(H * 0.034))
txt = Image.new("L", (W, H), 0); d = ImageDraw.Draw(txt); x, y = int(W * 0.035), int(H * 0.045)
d.text((x, y), sys.argv[3], font=font, fill=255)
sh = txt.filter(ImageFilter.GaussianBlur(2)); a = np.asarray(im, float)
a = a * (1 - 0.55 * np.asarray(sh, float)[..., None] / 255)                    # soft dark edge so it reads on bright areas
t = np.asarray(txt.filter(ImageFilter.GaussianBlur(0.6)), float)[..., None] / 255
a = a * (1 - 0.92 * t) + 235 * 0.92 * t                                        # slightly off-white, like a camera OSD
Image.fromarray(np.clip(a, 0, 255).astype("uint8")).save(sys.argv[2])
