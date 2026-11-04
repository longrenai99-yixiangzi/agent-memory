import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image
from labutil import to_lab
LW = np.array([0.2126, 0.7152, 0.0722])
for p in sys.argv[1:]:
    a = np.asarray(Image.open(p).convert("RGB").resize((640, 360)), float) / 255; lab = to_lab(a); m = a.reshape(-1, 3).mean(0)
    print("%-36s lum %.3f  R/B %.2f  a %+5.1f b %+5.1f  spread a %.1f b %.1f" % (os.path.basename(p)[:36], (a @ LW).mean(), m[0]/m[2], lab[..., 1].mean(), lab[..., 2].mean(), lab[..., 1].std(), lab[..., 2].std()))
