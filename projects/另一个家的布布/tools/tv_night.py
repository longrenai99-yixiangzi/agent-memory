"""Grade the TV-direction still to the standard night look (no AI): darker marble floor, redder walnut wood, muted olive wall, smaller light pools, lower exposure.
usage: python tv_night.py IN OUT [gamma=1.5] [floor_dark=0.40]    (regions in 1600-wide coords)"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
gam = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5; fd = float(sys.argv[4]) if len(sys.argv) > 4 else 0.40
im = Image.open(sys.argv[1]).convert("RGB"); W, H = im.size; s = W / 1600.0
a = np.asarray(im, float) / 255.0; LW = np.array([0.2126, 0.7152, 0.0722])
sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s_,v):
    h=(h%360)/60.0; c=v*s_; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
def mask(polys, blur, minus=()):
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
    for p in polys: d.polygon([(x*s, y*s) for x, y in p], fill=255)
    for p in minus: d.polygon([(x*s, y*s) for x, y in p], fill=0)
    return np.asarray(m.filter(ImageFilter.GaussianBlur(blur*s)), float) / 255.0
floor = mask([[(0,612),(1595,612),(1595,700),(1362,700),(1358,740),(1362,800),(1210,825),(1030,830),(1000,820),(480,822),(488,775),(487,700),(482,662),(0,655)]], 4)
sofa = mask([[(0,658),(480,660),(488,775),(470,824),(0,830)],[(0,822),(1600,835),(1600,902),(0,902)],[(1362,700),(1600,695),(1600,835),(1215,827),(1358,800)]], 3)
wallz = mask([[(305,92),(1322,92),(1322,606),(305,606)]], 4)
h, sa, v = rgb2hsv(a)
# 1) floor: much darker, less saturated warm grey-brown (the standard floor is dark, glossy, not cream)
fw = floor * (1 - sm(sa, 0.48, 0.60))
v = v * (1 - fw * (1 - fd)); sa = sa * (1 - fw * 0.40)
v = v * (1 - sofa * 0.38); sa = sa * (1 + sofa * 0.12); h = h + (28 - h) * sofa * 0.5   # the sofas sit in the same dim room, not brighter than the walls
white = sm(v, 0.45, 0.60) * (1 - sm(sa, 0.12, 0.20)) * (1 - sm(v, 0.88, 0.96)) * (1 - floor) * (1 - sofa)   # keeps the downlight bulbs bright; door, ceiling, white column: down with the rest
v = v * (1 - 0.42 * white)
dz = mask([[(1322,100),(1582,100),(1582,612),(1322,612)]], 3)          # door and its white frame (warm, so not caught above)
cz = mask([[(0,0),(1600,0),(1600,90),(0,90)]], 3) * (1 - sm(v, 0.88, 0.96))   # ceiling band, bulbs excluded
colz = mask([[(200,90),(262,90),(262,625),(200,625)]], 2)             # the white wall column beside the balcony opening
v = v * (1 - 0.45 * dz * sm(v, 0.25, 0.35)) * (1 - 0.40 * cz) * (1 - 0.35 * colz * sm(v, 0.30, 0.45))
# 2) wood (sat > 0.5, orange) -> redder walnut like the standard
wood = sm(h, 8, 14) * (1 - sm(h, 32, 40)) * sm(sa, 0.50, 0.60) * (1 - floor)
h = h - 9.0 * wood; sa = sa * (1 - 0.22 * wood)
# 3) wall: muted olive, brightness untouched
wl = wallz * sm(h, 30, 42) * (1 - sm(h, 78, 95)) * sm(sa, 0.10, 0.16) * (1 - sm(sa, 0.40, 0.50))
h = h + (60 - h) * wl * 0.8; sa = sa * (1 - wl*0.8) + 0.22 * wl * 0.8
a = hsv2rgb(h, np.clip(sa, 0, 1), np.clip(v, 0, 1))
# 4) exposure: gamma, then a soft shoulder
a = np.power(np.clip(a, 0, 1), gam); a = np.where(a > 0.55, 0.55 + (a - 0.55) * 0.6, a)
# 5) smaller light pools on the wall (Gaussian around each spotlight, smooth)
L = a @ LW
small = Image.fromarray((np.clip(L,0,1)*255).astype("uint8")).resize((W//4, H//4))
base = np.asarray(small.filter(ImageFilter.MinFilter(51)).filter(ImageFilter.GaussianBlur(25)).resize((W, H), Image.BILINEAR), float)/255
yy, xx = np.mgrid[0:H, 0:W]; xx = xx/s; yy = yy/s
gn = np.zeros((H, W)); gw = np.zeros((H, W))
for cx in (558, 1040):
    gn = np.maximum(gn, np.exp(-(((xx-cx)/60)**2 + ((yy-140)/80)**2))); gw = np.maximum(gw, np.exp(-(((xx-cx)/144)**2 + ((yy-215)/240)**2)))
g = 1 - gw * (1 - np.maximum(gn, 0.30)); ex = np.maximum(0, L - base)
fac = np.where(L > 1e-4, (base + ex*g)/np.maximum(L, 1e-4), 1.0)[..., None]; z = wallz[..., None]
a = a * (1 - z) + a * fac * z
Image.fromarray((np.clip(a,0,1)*255).astype("uint8")).save(sys.argv[2])
l = a @ LW; print("mean %.3f P5 %.3f P95 %.3f P99.5 %.3f" % (l.mean(), np.percentile(l,5), np.percentile(l,95), np.percentile(l,99.5)))
