"""Shift the wall colour of a DAY reference still a little toward olive-yellow-green (no AI, nothing else changes).
The wall is found by colour (measured day wall: hue ~40-55 deg, sat 0.2-0.3, value 0.5-0.7), so it works on any day view.
usage: python day_wall_shift.py IN OUT_PNG [strength=0.35] [target_hue=75]"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageFilter
inp, outp = sys.argv[1], sys.argv[2]
k = float(sys.argv[3]) if len(sys.argv) > 3 else 0.35
th = float(sys.argv[4]) if len(sys.argv) > 4 else 62.0
a = np.asarray(Image.open(inp).convert("RGB"), float) / 255.0
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
# wall = measured day wall colour band; sofa is less saturated, wood more saturated
gate = sm(h, 34, 40) * (1 - sm(h, 58, 66)) * sm(s, 0.14, 0.18) * (1 - sm(s, 0.32, 0.38)) * sm(v, 0.40, 0.46) * (1 - sm(v, 0.78, 0.86))
gate = np.asarray(Image.fromarray((gate*255).astype("uint8")).filter(ImageFilter.GaussianBlur(2)), float) / 255.0
w = gate * k
nh = h + (th - h) * w                                            # hue moves toward olive-yellow-green
ns = s * (1 - w) + np.clip(s * 1.10, 0, 0.36) * w                 # a touch more saturated, capped (muted olive, not lime)
out = hsv2rgb(nh, ns, v)
Image.fromarray((np.clip(out, 0, 1)*255).astype("uint8")).save(outp)
sel = gate > 0.5
print("wall pixels found: %.1f%% of the image" % (sel.mean()*100))
if sel.any():
    h2, s2, v2 = rgb2hsv(out); print("wall hue median: %.0f -> %.0f deg | saturation %.2f -> %.2f" % (np.median(h[sel]), np.median(h2[sel]), np.median(s[sel]), np.median(s2[sel])))

Image.fromarray((gate*255).astype('uint8')).save(outp.replace('.png','_mask.png'))
