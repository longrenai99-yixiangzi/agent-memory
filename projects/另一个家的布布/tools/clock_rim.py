"""Recolour the wall clock's rim from copper to the light oak of the approved single-item clock (hue ~29 deg), geometry untouched.
usage: python clock_rim.py IN OUT cx cy rx ry [gray_gain]   (bbox ellipse of the OUTER clock in image pixels)"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageFilter
im = Image.open(sys.argv[1]).convert("RGB"); W, H = im.size; a = np.asarray(im, float) / 255.0
cx, cy, rx, ry = [float(v) for v in sys.argv[3:7]]; gg = float(sys.argv[7]) if len(sys.argv) > 7 else None
sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s_,v):
    h=(h%360)/60.0; c=v*s_; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
y0, y1, x0, x1 = int(cy-ry*1.3), int(cy+ry*1.3), int(cx-rx*1.3), int(cx+rx*1.3)
yy, xx = np.mgrid[y0:y1, x0:x1]; d = np.sqrt(((xx-cx)/rx)**2 + ((yy-cy)/ry)**2)
sub = a[y0:y1, x0:x1]; h, s, v = rgb2hsv(sub); L = sub @ np.array([0.2126, 0.7152, 0.0722])
ring = sm(d, 0.80, 0.88) * (1 - sm(d, 1.05, 1.12))                                          # the band where the rim lives
face = sm(L, 0.45, 0.60) * (d < 0.9)                                                         # the bright face is never touched
if gg is None:                                                                                # colour image: copper -> oak
    cop = sm(s, 0.18, 0.30) * sm(h, 0, 6) * (1 - sm(h, 30, 40)) * ring * (1 - face)
    nh = h + (29 - h) * 0.9 * cop; ns = s * (1 - 0.35 * cop) + 0.38 * 0.35 * cop; nv = v * (1 + 0.10 * cop)
    out = hsv2rgb(nh, np.clip(ns, 0, 1), np.clip(nv, 0, 1))
else:                                                                                         # monochrome (monitor): the lighter oak reads brighter than the old dark rim
    w = ring * (1 - face) * sm(1 - L, 0.30, 0.45)
    out = np.clip(sub * (1 + (gg - 1) * w[..., None]), 0, 1)
a[y0:y1, x0:x1] = out
Image.fromarray((np.clip(a, 0, 1)*255).astype("uint8")).save(sys.argv[2])
