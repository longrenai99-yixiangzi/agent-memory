"""Turn the downlights OFF in a day still: flatten the warm light pools on the wall back to the wall's own colour and paint the lit bulbs as plain ceiling.
usage: python day_nolights.py IN OUT   (positions in 1600-wide coords: pools at x=558, 1048; bulbs at (558,80) (1048,80) (72,38))"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
im = Image.open(sys.argv[1]).convert("RGB"); W, H = im.size; s = W / 1600.0
a = np.asarray(im, float) / 255.0; LW = np.array([0.2126, 0.7152, 0.0722]); L = a @ LW
yy, xx = np.mgrid[0:H, 0:W]; xx = xx/s; yy = yy/s
def samp(x0, y0, x1, y1): return np.median(a[int(y0*s):int(y1*s), int(x0*s):int(x1*s)].reshape(-1, 3), 0)
wall_col = (samp(330, 110, 470, 225) + samp(1150, 110, 1290, 225)) / 2                    # the wall's own colour, far from the pools
gw = np.zeros((H, W))
for cx in (558, 1048): gw = np.maximum(gw, np.exp(-(((xx-cx)/230)**2 + ((yy-185)/105)**2)))
zone = Image.new("L", (W, H), 0); ImageDraw.Draw(zone).rectangle([305*s, 92*s, 1322*s, 430*s], fill=255); ImageDraw.Draw(zone).rectangle([636*s, 232*s, 1020*s, 460*s], fill=0)   # the wall around the TV, not the TV
mx = a.max(-1); mn = a.min(-1); sat = np.where(mx > 0, (mx-mn)/np.maximum(mx, 1e-6), 0)
smo = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
wallish = (1 - smo(sat, 0.36, 0.46)) * smo(mx, 0.55, 0.65)                                  # plants (saturated) and shadows are left alone
z = np.clip(gw * 1.6, 0, 1) * np.asarray(zone.filter(ImageFilter.GaussianBlur(3*s)), float) / 255 * wallish
# keep the wall's own faint texture/gradient: add back the local deviation of the wall far from the pools (none here), so just blend to the wall colour
a = a * (1 - z[..., None]) + wall_col[None, None, :] * z[..., None]
# bulbs: fill each lit disc with the mean colour of the ring around it (crop only, fast)
out = np.asarray(Image.fromarray((np.clip(a,0,1)*255).astype("uint8")), float)
for bx, by in ((558, 80), (1048, 80), (72, 38)):
    cx, cy, r = int(bx*s), int(by*s), int(15*s); R = int(r*2.4)
    y0, y1, x0, x1 = max(cy-R, 0), cy+R, max(cx-R, 0), cx+R
    gy, gx = np.mgrid[y0:y1, x0:x1]; d = np.hypot(gx-cx, gy-cy); dy = gy-cy
    top = out[y0:y1, x0:x1][(d > r*1.2) & (d < r*2.0) & (dy < -r*0.4)].mean(0)       # ceiling side
    bot = out[y0:y1, x0:x1][(d > r*1.2) & (d < r*2.0) & (dy > r*0.4)].mean(0)       # wall side
    t = np.clip((dy / r + 1) / 2, 0, 1)[..., None]; col = top * (1 - t) + bot * t        # the bulb sits on the ceiling/wall edge: blend the two
    w = np.clip((r*1.25 - d) / (r*0.4), 0, 1)[..., None]
    out[y0:y1, x0:x1] = out[y0:y1, x0:x1]*(1-w) + col*w
Image.fromarray(np.clip(out,0,255).astype("uint8")).save(sys.argv[2])
