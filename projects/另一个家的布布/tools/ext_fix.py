"""Exterior-window stills: (fig) recolour the figure's warm clothes to silver-grey and blur it to a silhouette; (flash) add a cool lightning glow over the glass.
usage: python ext_fix.py fig IN OUT 'x,y;x,y;...' [blur=9]     |     python ext_fix.py flash IN OUT cx cy [strength=0.35]"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
mode, inp, outp = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(inp).convert("RGB"); W, H = im.size; a = np.asarray(im, float) / 255.0
sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s_,v):
    h=(h%360)/60.0; c=v*s_; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
if mode == "fig":
    pts = [tuple(float(v) for v in p.split(",")) for p in sys.argv[4].split(";")]; bl = float(sys.argv[5]) if len(sys.argv) > 5 else 9
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon(pts, fill=255); m = np.asarray(m.filter(ImageFilter.GaussianBlur(10)), float)[..., None] / 255.0
    h, sa, v = rgb2hsv(a); lum = (a @ np.array([0.2126, 0.7152, 0.0722]))[..., None]
    cloth = (sm(sa, 0.08, 0.14) * sm(v, 0.12, 0.20) * sm(h, 3, 9) * (1 - sm(h, 42, 50)))[..., None]    # warm beige / brown only; olive wall and black hair stay
    w = cloth * m
    silver = lum * np.array([0.97, 0.99, 1.06])[None, None, :] * 1.06                                  # silver-grey with a faint cool cast, same brightness
    a2 = a * (1 - 0.85 * w) + silver * (0.85 * w)
    blur = np.asarray(Image.fromarray((np.clip(a2,0,1)*255).astype("uint8")).filter(ImageFilter.GaussianBlur(bl)), float) / 255.0
    out = a2 * (1 - m) + blur * m
else:
    cx, cy = float(sys.argv[4]), float(sys.argv[5]); k = float(sys.argv[6]) if len(sys.argv) > 6 else 0.35
    yy, xx = np.mgrid[0:H, 0:W]; r = np.hypot(xx-cx, (yy-cy)*0.8) / (0.55 * W)
    glow = np.clip(1 - r, 0, 1) ** 1.6                                                        # strongest around the bolt, gone toward the far edge
    v = a.max(-1); glass = 1 - sm(v, 0.02, 0.14)*0                                           # same weight on glass and mullions: a flash lights both
    cool = np.array([0.70, 0.82, 1.0])[None, None, :]
    f = (glow * k)[..., None] * cool
    out = 1 - (1 - a) * (1 - f)
Image.fromarray((np.clip(out,0,1)*255).astype("uint8")).save(outp)
l = out @ np.array([0.2126, 0.7152, 0.0722]); print("mean %.3f P95 %.3f" % (l.mean(), np.percentile(l, 95)))
