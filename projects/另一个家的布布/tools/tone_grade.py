"""Deterministic tone grade for the night reference still (no AI): deeper darks, brighter highlights, olive-yellow-green walls.
v3: the wall hue shift is SMOOTH across brightness (light pools shift together with the wall, slightly warmer), no hard value cut,
    highlights get a soft shoulder (no clipping) and are desaturated a little (no orange/pink pools).
usage: python tone_grade.py IN OUT_PNG [gamma=1.5] [hl_gain=0.3] [wall_hue=72] [wall_strength=0.5]
Wall polygons are in 2000-px-wide coordinates (scaled automatically)."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
inp, outp = sys.argv[1], sys.argv[2]
gamma = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5
hl = float(sys.argv[4]) if len(sys.argv) > 4 else 0.3
wall_h = float(sys.argv[5]) if len(sys.argv) > 5 else 72.0
wall_k = float(sys.argv[6]) if len(sys.argv) > 6 else 0.5
im = Image.open(inp).convert("RGB"); W, H = im.size; s = W / 2000.0
a = np.asarray(im, float) / 255.0
sm = lambda x, e0, e1: np.clip((x - e0) / (e1 - e0), 0, 1) ** 2 * (3 - 2 * np.clip((x - e0) / (e1 - e0), 0, 1))   # smoothstep-like
def rgb2hsv(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]; mx = a.max(-1); mn = a.min(-1); d = mx - mn
    h = np.zeros_like(mx); m = d > 1e-6
    rc = (mx == r) & m; gc = (mx == g) & m & ~rc; bc = (mx == b) & m & ~rc & ~gc
    h[rc] = ((g - b)[rc] / d[rc]) % 6; h[gc] = (b - r)[gc] / d[gc] + 2; h[bc] = (r - g)[bc] / d[bc] + 4
    return h * 60.0, np.where(mx > 0, d / np.maximum(mx, 1e-6), 0), mx
def hsv2rgb(h, s_, v):
    h = (h % 360) / 60.0; c = v * s_; x = c * (1 - np.abs(h % 2 - 1)); m = v - c
    z = np.zeros_like(h); conds = [h<1,h<2,h<3,h<4,h<5,h<6]
    r = np.select(conds,[c,x,z,z,x,c]); g = np.select(conds,[x,c,c,x,z,z]); b = np.select(conds,[z,z,x,c,c,x])
    return np.stack([r + m, g + m, b + m], -1)
polys = [ [(0,70),(490,125),(490,495),(250,520),(60,560),(0,580)],
          [(1400,0),(2000,0),(2000,610),(1880,600),(1880,170),(1545,170),(1545,570),(1445,600),(1400,380)],
          [(490,125),(610,125),(610,540),(490,495)], [(1250,125),(1400,0),(1400,380),(1250,380)] ]
mask = Image.new("L", (W, H), 0); d = ImageDraw.Draw(mask)
for p in polys: d.polygon([(x*s, y*s) for x, y in p], fill=255)
m = np.asarray(mask.filter(ImageFilter.GaussianBlur(8*s)), float) / 255.0
clk = Image.new("L", (W, H), 0); ImageDraw.Draw(clk).ellipse([(315-85)*s,(225-85)*s,(315+85)*s,(225+85)*s], fill=255)
clk = np.asarray(clk.filter(ImageFilter.GaussianBlur(4*s)), float) / 255.0
h, sat, v = rgb2hsv(a)
gate = sm(sat, 0.04, 0.12) * (1 - sm(sat, 0.55, 0.70)) * sm(v, 0.05, 0.12) * (1 - sm(v, 0.94, 1.0))    # smooth, NOT a hard cut on brightness
gate = np.asarray(Image.fromarray((gate*255).astype("uint8")).filter(ImageFilter.GaussianBlur(3*s)), float) / 255.0
w = m * gate * (1 - clk) * wall_k
target = wall_h - 14.0 * sm(v, 0.45, 0.80)                       # bright (lit) wall pixels end up a little warmer / yellower than the shadowed wall
dh = ((target - h + 180) % 360) - 180
nh = h + dh * w
ns = sat * (1 - w) + np.clip(np.maximum(sat, 0.18), 0, 0.30) * w
a2 = hsv2rgb(nh, ns, v)
y = np.power(np.clip(a2, 0, 1), gamma)                           # deeper mids / darks
yl = y @ np.array([0.2126, 0.7152, 0.0722]); sat_gain = 0.88 * (1 - 0.30 * sm(yl, 0.35, 0.85))   # gamma raises saturation; also desaturate highlights
y = yl[..., None] + (y - yl[..., None]) * sat_gain[..., None]
y = y + hl * np.maximum(0, y - 0.25)                             # lift highlights
y = np.where(y > 0.70, 0.70 + (y - 0.70) * 0.45, y)              # soft shoulder: light pools no longer clip
y = np.clip(y, 0, 1)
Image.fromarray((y * 255).astype("uint8")).save(outp)
L = lambda x: x @ np.array([0.2126, 0.7152, 0.0722])
for name, arr in (("before", a), ("after ", y)):
    l = L(arr); print("%s mean %.3f P5 %.3f P50 %.3f P95 %.3f P99.5 %.3f dark(<0.04) %.1f%%" % (name, l.mean(), np.percentile(l,5), np.percentile(l,50), np.percentile(l,95), np.percentile(l,99.5), (l<0.04).mean()*100))
