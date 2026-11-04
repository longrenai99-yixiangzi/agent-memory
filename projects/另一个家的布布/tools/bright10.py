"""Raise the mean luminance by a given factor (default 1.10) with a gamma, no clipping: usage: python bright10.py IN OUT [factor=1.10]"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image
a = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float) / 255.0; f = float(sys.argv[3]) if len(sys.argv) > 3 else 1.10
LW = np.array([0.2126, 0.7152, 0.0722]); m0 = (a @ LW).mean(); lo, hi = 0.5, 1.0
for _ in range(14):
    g = (lo + hi) / 2; m = (np.power(a, g) @ LW).mean(); lo, hi = (g, hi) if m > m0 * f else (lo, g)
y = np.power(a, g); Image.fromarray((np.clip(y, 0, 1)*255).astype("uint8")).save(sys.argv[2])
l = y @ LW; print("gamma %.3f mean %.3f -> %.3f P99.5 %.3f clipped %.2f%%" % (g, m0, l.mean(), np.percentile(l, 99.5), (y.max(-1) >= 0.999).mean()*100))
