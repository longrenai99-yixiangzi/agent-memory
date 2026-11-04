"""Nudge the colour balance with per-channel gains, then set the mean luminance with a gamma: python wb_match.py IN OUT rgain bgain target_lum"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image
a = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float) / 255.0; rg, bg, tgt = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
a = np.clip(a * np.array([rg, 1.0, bg]), 0, 1); LW = np.array([0.2126, 0.7152, 0.0722]); lo, hi = 0.5, 1.6
for _ in range(14):
    g = (lo + hi) / 2; m = (np.power(a, g) @ LW).mean(); lo, hi = (g, hi) if m > tgt else (lo, g)
y = np.power(a, g); Image.fromarray((np.clip(y, 0, 1)*255).astype("uint8")).save(sys.argv[2])
mean = y.reshape(-1, 3).mean(0); print("gamma %.3f lum %.3f R/B %.2f" % (g, (y @ LW).mean(), mean[0]/mean[2]))
