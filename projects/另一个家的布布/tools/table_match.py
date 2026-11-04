"""Match the coffee-table wood colour of the sofa-direction still to the standard night still (redder walnut, not orange).
usage: python table_match.py IN OUT   (table region in 1600-wide coords: x 340-810, y 590-790)"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
im = Image.open(sys.argv[1]).convert("RGB"); W, H = im.size; s = W / 1600.0
a = np.asarray(im, float) / 255.0
sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s_,v):
    h=(h%360)/60.0; c=v*s_; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
reg = Image.new("L", (W, H), 0); ImageDraw.Draw(reg).rectangle([340*s, 590*s, 810*s, 790*s], fill=255)
reg = np.asarray(reg.filter(ImageFilter.GaussianBlur(3*s)), float) / 255.0
h, sa, v = rgb2hsv(a)
wood = sm(h, 4, 10) * (1 - sm(h, 30, 38)) * sm(sa, 0.30, 0.42) * sm(v, 0.06, 0.12) * reg
yy = np.mgrid[0:H, 0:W][0] / s
top = 1 - sm(yy, 636, 646)                                  # top surface above y~640, front panel below
nh = h + (-6.0) * wood                                        # orange -> redder walnut
ns = np.where(top > 0.5, sa * (1 - 0.18 * wood), np.minimum(1, sa * (1 + 0.20 * wood)))   # top slightly less saturated, front a little richer
nv = v * (1 + wood * (0.12 * top + 0.15 * (1 - top)))
out = hsv2rgb(nh, ns, nv)
Image.fromarray((np.clip(out,0,1)*255).astype("uint8")).save(sys.argv[2])
