"""Tone the exterior-window night stills down to the interior standard: lower exposure, less orange.
usage: python ext_night.py IN OUT [target_mean=0.22]"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image
a = np.asarray(Image.open(sys.argv[1]).convert("RGB"), float) / 255.0; tgt = float(sys.argv[3]) if len(sys.argv) > 3 else 0.22
LW = np.array([0.2126, 0.7152, 0.0722]); sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s_,v):
    h=(h%360)/60.0; c=v*s_; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
h, s, v = rgb2hsv(a)
warm = sm(h, 8, 16) * (1 - sm(h, 52, 66)) * sm(s, 0.30, 0.45)                    # the golden-orange glow, not the olive walls or the blue outside
a = hsv2rgb(h + (40 - h) * 0.25 * warm, s * (1 - 0.30 * warm), v)
def grade(g):
    y = np.power(a, g); return np.where(y > 0.55, 0.55 + (y - 0.55) * 0.6, y)
lo, hi = 1.0, 3.0
for _ in range(14):
    g = (lo + hi) / 2; m = (grade(g) @ LW).mean()
    lo, hi = (g, hi) if m > tgt else (lo, g)
y = grade(g); Image.fromarray((np.clip(y, 0, 1)*255).astype("uint8")).save(sys.argv[2])
l = y @ LW; print("gamma %.2f mean %.3f P95 %.3f P99.5 %.3f" % (g, l.mean(), np.percentile(l, 95), np.percentile(l, 99.5)))
