"""Compare an edited 朝阳台 night image against the original and report where pixels changed.
usage: python verify_edit.py ORIGINAL EDITED OUT_PNG [allowed: curtain,clothes,object,clock,frame,vase]
Regions are in the 3837x2160 original's pixel coordinates (scaled if sizes differ)."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
REG = {  # name: (x0,y0,x1,y1) in 3837x2160 coordinates
 "curtain": (900,230,1330,1100), "clothes": (1400,330,2400,830), "object": (1600,1100,1760,1260),
 "clock": (250,150,750,550), "frame": (3400,1100,3650,1380), "vase": (1650,1250,2000,1450)}
ref_w, ref_h = 3837, 2160
a_path, b_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
allowed = (sys.argv[4].split(",") if len(sys.argv) > 4 else list(REG))
A = Image.open(a_path).convert("RGB"); B = Image.open(b_path).convert("RGB")
note = ""
if B.size != A.size:
    note = f"edited size {B.size} != original {A.size}, resized to original for comparison"
    B = B.resize(A.size, Image.LANCZOS)
W, H = A.size; sx, sy = W / ref_w, H / ref_h
a = np.asarray(A.filter(ImageFilter.GaussianBlur(3)), float); b = np.asarray(B.filter(ImageFilter.GaussianBlur(3)), float)
d = np.abs(a - b).mean(axis=2); changed = d > 25
mask = np.zeros(changed.shape, bool); rows = []
for name, (x0, y0, x1, y1) in REG.items():
    X0, Y0, X1, Y1 = int(x0*sx), int(y0*sy), int(x1*sx), int(y1*sy)
    pct = changed[Y0:Y1, X0:X1].mean() * 100
    rows.append((name, pct, name in allowed))
    if name in allowed: mask[Y0:Y1, X0:X1] = True
outside = changed[~mask].mean() * 100
print(note) if note else None
print("changed pixels per region (%):")
for n, p, al in rows: print(f"  {n:8s} {p:6.1f}%  {'(allowed to change)' if al else '(should NOT change)'}")
print(f"changed outside the allowed regions: {outside:.2f}% of the rest of the image")
# 8x6 grid of change share outside allowed regions, to point at where the drift is
gh, gw = 6, 8; print("drift grid (% changed outside allowed regions; rows top->bottom):")
for r in range(gh):
    line = []
    for c in range(gw):
        ys, ye, xs, xe = r*H//gh, (r+1)*H//gh, c*W//gw, (c+1)*W//gw
        m = ~mask[ys:ye, xs:xe]; cell = changed[ys:ye, xs:xe]
        line.append(f"{(cell[m].mean()*100 if m.any() else 0):5.1f}")
    print("  " + " ".join(line))
ov = np.asarray(A.convert("RGB"), float) * 0.45
ov[changed & ~mask] = [255, 0, 0]; ov[changed & mask] = [255, 210, 0]
im = Image.fromarray(ov.astype("uint8")); dr = ImageDraw.Draw(im)
for name, (x0, y0, x1, y1) in REG.items():
    dr.rectangle([x0*sx, y0*sy, x1*sx, y1*sy], outline=(0, 255, 255) if name in allowed else (255, 255, 255), width=4)
im.thumbnail((1600, 900)); im.save(out); print("overlay saved:", out, "(red = changed outside allowed, yellow = changed inside allowed, cyan box = allowed region)")
