"""Composite an untouched photo into a picture frame using a perspective warp (no AI redraw).
usage: python composite_frame.py SCENE PHOTO OUT_PNG [overlay_only]
Quad = corners of the white mat opening, in the coordinates of a 2000-px-wide scene (scaled automatically)."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
QUAD = [(1272,578),(1316,576),(1319,635),(1271,636)]
REAL_ASPECT = 0.74
INSET = 0.06            # white mat margin around the photo, fraction of opening width
SS = 8                  # supersampling for the local warp
def homography(src, dst):
    A = []; b = []
    for (x, y), (u, v) in zip(src, dst):
        A.append([x, y, 1, 0, 0, 0, -u*x, -u*y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v*x, -v*y]); b.append(v)
    return np.linalg.solve(np.array(A, float), np.array(b, float))
scene = Image.open(sys.argv[1]).convert("RGB"); photo = Image.open(sys.argv[2]).convert("RGB"); out = sys.argv[3]
W, H = scene.size; s = W / 2000.0
quad = [(x*s, y*s) for x, y in QUAD]
x0 = int(min(p[0] for p in quad)) - 12; x1 = int(max(p[0] for p in quad)) + 12
y0 = int(min(p[1] for p in quad)) - 12; y1 = int(max(p[1] for p in quad)) + 12
roi = scene.crop((x0, y0, x1, y1)); rw, rh = roi.size
if len(sys.argv) > 4:   # overlay check only
    d = ImageDraw.Draw(roi); d.polygon([(x-x0, y-y0) for x, y in quad], outline=(0, 255, 255))
    roi = roi.resize((rw*6, rh*6), Image.LANCZOS); roi.save(out); print("overlay", out); sys.exit()
# 1) rectified mat canvas: opening rectangle of aspect REAL_ASPECT, photo fitted with a white margin
CH = 800; CW = int(CH * REAL_ASPECT)
orig_np = np.asarray(roi, float)
qmask_small = Image.new("L", (rw, rh), 0); ImageDraw.Draw(qmask_small).polygon([(x-x0, y-y0) for x, y in quad], fill=255)
qm = np.asarray(qmask_small) > 128
mat_col = np.percentile(orig_np[qm], 80, axis=0)              # the real mat colour in this lighting
canvas = Image.new("RGB", (CW, CH), tuple(int(c) for c in (255, 255, 255)))
pw = CW * (1 - 2*INSET); ph = pw * photo.height / photo.width
if ph > CH*(1-2*INSET): ph = CH*(1-2*INSET); pw = ph * photo.width / photo.height
ph_i, pw_i = int(ph), int(pw)
canvas.paste(photo.resize((pw_i, ph_i), Image.LANCZOS), ((CW-pw_i)//2, (CH-ph_i)//2))
# 2) warp onto an 8x supersampled ROI
qs = [((x-x0)*SS, (y-y0)*SS) for x, y in quad]
rect = [(0, 0), (CW, 0), (CW, CH), (0, CH)]
c = homography(qs, rect)                                        # output(px) -> canvas coords for PIL
warped = canvas.transform((rw*SS, rh*SS), Image.PERSPECTIVE, tuple(c), Image.BICUBIC)
mask = Image.new("L", (rw*SS, rh*SS), 0); ImageDraw.Draw(mask).polygon(qs, fill=255)
warped = warped.resize((rw, rh), Image.LANCZOS); mask = mask.resize((rw, rh), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.6))
# 3) light match: keep the real shading of the mat, scale brightness so the white mat equals the scene's mat colour
wn = np.asarray(warped, float) / 255.0
L_orig = orig_np @ np.array([0.2126, 0.7152, 0.0722])
shade = np.asarray(Image.fromarray(L_orig.astype("uint8")).filter(ImageFilter.GaussianBlur(6)), float)
shade = shade / max(shade[qm].mean(), 1e-6); shade = np.clip(shade, 0.80, 1.20)
res = wn * (mat_col / 255.0)[None, None, :] * shade[..., None]
res = np.asarray(Image.fromarray((np.clip(res, 0, 1)*255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.5)), float)
m = (np.asarray(mask, float) / 255.0)[..., None]
final = (res * m + orig_np * (1 - m)).clip(0, 255).astype("uint8")
scene.paste(Image.fromarray(final), (x0, y0)); scene.save(out)
print("saved", out, "| mat colour used:", [int(v) for v in mat_col], "| photo fitted", pw_i, "x", ph_i, "in canvas", CW, "x", CH)
