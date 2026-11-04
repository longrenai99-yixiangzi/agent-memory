"""Pull the colour (Lab a/b mean and spread) of a still toward a reference still; luminance is then set with a gamma.
usage: python lab_match.py SRC REF OUT [mean_strength=1.0] [target_lum] [spread_strength=0.5]"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image
def to_lab(rgb):
    c = np.where(rgb > 0.04045, ((rgb + 0.055) / 1.055) ** 2.4, rgb / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]]); xyz = (c @ M.T) / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116); return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)
def to_rgb(lab):
    fy = (lab[..., 0] + 16) / 116; fx = fy + lab[..., 1] / 500; fz = fy - lab[..., 2] / 200; f = np.stack([fx, fy, fz], -1)
    xyz = np.where(f ** 3 > 0.008856, f ** 3, (f - 16 / 116) / 7.787) * np.array([0.95047, 1.0, 1.08883])
    Mi = np.linalg.inv(np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])); c = np.clip(xyz @ Mi.T, 0, 1)
    return np.where(c > 0.0031308, 1.055 * c ** (1 / 2.4) - 0.055, 12.92 * c)
src = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float) / 255.0; ref = np.asarray(Image.open(sys.argv[2]).convert("RGB").resize((960, 540)), float) / 255.0
k = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0; ks = float(sys.argv[6]) if len(sys.argv) > 6 else 0.5; tgt = float(sys.argv[5]) if len(sys.argv) > 5 else None
ls = to_lab(src); lr = to_lab(ref); out = ls.copy()
for ch in (1, 2):
    ms, ss = ls[..., ch].mean(), ls[..., ch].std(); mr, sr = lr[..., ch].mean(), lr[..., ch].std()
    scale = 1 + ks * (sr / max(ss, 1e-6) - 1)                      # spread moves only part of the way, so each scene keeps its own contrast
    out[..., ch] = ms + (ls[..., ch] - ms) * scale + k * (mr - ms)     # the mean colour goes fully to the reference
y = to_rgb(out); LW = np.array([0.2126, 0.7152, 0.0722])
if tgt:
    lo, hi = 0.5, 2.0
    for _ in range(14):
        g = (lo + hi) / 2; m = (np.power(y, g) @ LW).mean(); lo, hi = (g, hi) if m > tgt else (lo, g)
    y = np.power(y, g)
Image.fromarray((np.clip(y, 0, 1)*255).astype("uint8")).save(sys.argv[3]); mean = y.reshape(-1, 3).mean(0)
print("lum %.3f R/B %.2f" % ((y @ LW).mean(), mean[0]/mean[2]))
