"""Fix a colour cast by remapping hue bands toward the standard night look (no AI, geometry untouched).
usage: python hue_fix.py IN OUT_PNG
bands: magenta/purple -> warm beige; dull green walls -> olive; orange light pools -> softer yellow-warm; violet-blue -> clean blue."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image
a = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float) / 255.0
sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s,v):
    h=(h%360)/60.0; c=v*s; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
h, s, v = rgb2hsv(a)
hc = ((h + 180) % 360) - 180                       # signed hue around red, so 300..360..30 is one contiguous band
nh, ns = h.copy(), s.copy()
def pull(mask, target_signed, k, sat_to=None, sat_k=0.0):
    global nh, ns
    cur = ((nh + 180) % 360) - 180
    target_signed = ((target_signed + 180) % 360) - 180
    nh = np.where(mask > 0, (cur + (target_signed - cur) * mask * k) % 360, nh)
    if sat_to is not None: ns = ns * (1 - mask * sat_k) + sat_to * mask * sat_k
col = sm(s, 0.06, 0.14)                              # only coloured pixels, neutral greys untouched
# 1) magenta / purple cast (sofa, radiator, pink in shadows): hue 255..360 and 0..8 -> warm beige 30 deg
mag = col * sm(h, 250, 275) * (1 - sm(h, 358, 360)) + col * (1 - sm(h, 0, 10)) * (h < 10)
pull(np.clip(mag, 0, 1) * (1 - sm(v, 0.92, 1.0)), 30, 1.0, sat_to=0.20, sat_k=0.75)
# 2) dull green wall (hue 70..140, low sat) -> muted olive 58 deg, sat 0.22
wall = sm(s, 0.03, 0.08) * sm(h, 64, 80) * (1 - sm(h, 140, 160)) * (1 - sm(s, 0.28, 0.40))
pull(wall, 58, 0.9, sat_to=0.27, sat_k=0.9)
# 3) orange light pools (bright, warm) -> softer yellow-warm 42 deg, less saturated
pool = col * sm(v, 0.55, 0.75) * (1 - sm(h, 34, 46)) * (h < 60)
pull(pool, 42, 0.75, sat_to=0.28, sat_k=0.6)
# 3b) dull blue-grey fabric (the throw blanket) -> warm taupe, only low-saturation pixels so window light stays blue
fab = col * sm(h, 215, 230) * (1 - sm(h, 262, 275)) * (1 - sm(s, 0.20, 0.30)) * (1 - sm(v, 0.45, 0.60))
pull(fab, 32, 0.85, sat_to=0.14, sat_k=0.7)
# 4) violet-blue (hue 225..262) -> clean blue 218 deg, a little less saturated
blu = col * (1 - fab) * sm(h, 222, 232) * (1 - sm(h, 258, 268))
pull(blu, 218, 0.7, sat_to=0.35, sat_k=0.0)
ns = ns * (1 - 0.18 * blu)
out = hsv2rgb(nh, np.clip(ns, 0, 1), v)
Image.fromarray((np.clip(out, 0, 1)*255).astype("uint8")).save(sys.argv[2])
