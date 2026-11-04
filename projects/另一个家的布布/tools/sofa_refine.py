"""Second pass on the sofa-direction night still: smaller light pools, taupe throw, brighter olive wall, softer highlights, calmer sofa chroma.
Regions are polygons in 1600-wide coordinates (scaled). usage: python sofa_refine.py IN OUT [sigma_x=50] [sigma_y=70]"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
inp, outp = sys.argv[1], sys.argv[2]; SX = float(sys.argv[3]) if len(sys.argv) > 3 else 50; SY = float(sys.argv[4]) if len(sys.argv) > 4 else 70
im = Image.open(inp).convert("RGB"); W, H = im.size; s = W / 1600.0
a = np.asarray(im, float) / 255.0
LW = np.array([0.2126, 0.7152, 0.0722]); sm = lambda x, e0, e1: (lambda t: t*t*(3-2*t))(np.clip((x-e0)/(e1-e0), 0, 1))
def mask(polys, blur, minus=()):
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
    for p in polys: d.polygon([(x*s, y*s) for x, y in p], fill=255)
    for p in minus: d.polygon([(x*s, y*s) for x, y in p], fill=0)
    return np.asarray(m.filter(ImageFilter.GaussianBlur(blur*s)), float)[..., None] / 255.0
def rgb2hsv(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; mx=a.max(-1); mn=a.min(-1); d=mx-mn; h=np.zeros_like(mx); m=d>1e-6
    rc=(mx==r)&m; gc=(mx==g)&m&~rc; bc=(mx==b)&m&~rc&~gc
    h[rc]=((g-b)[rc]/d[rc])%6; h[gc]=(b-r)[gc]/d[gc]+2; h[bc]=(r-g)[bc]/d[bc]+4
    return h*60.0, np.where(mx>0,d/np.maximum(mx,1e-6),0), mx
def hsv2rgb(h,s_,v):
    h=(h%360)/60.0; c=v*s_; x=c*(1-np.abs(h%2-1)); m=v-c; z=np.zeros_like(h); q=[h<1,h<2,h<3,h<4,h<5,h<6]
    return np.stack([np.select(q,[c,x,z,z,x,c])+m,np.select(q,[x,c,c,x,z,z])+m,np.select(q,[z,z,x,c,c,x])+m],-1)
L = a @ LW
wall = mask([[(190,86),(1085,86),(1085,408),(190,408)]], 6)
rad  = mask([[(26,86),(190,86),(190,300),(26,300)]], 4)
clock = mask([[(673-70,215-70),(673+70,215+70)]], 4)   # placeholder, replaced by ellipse below
c = Image.new("L", (W, H), 0); ImageDraw.Draw(c).ellipse([(673-68)*s,(215-68)*s,(673+68)*s,(215+68)*s], fill=255)
clock = np.asarray(c.filter(ImageFilter.GaussianBlur(3*s)), float)[..., None] / 255.0
# 1) smaller light pools: scale the glow above the local wall base by a Gaussian around each spotlight (smooth, no new edges)
small = im.resize((W//4, H//4)); gl = np.asarray(small.convert("L"), float)/255
base = np.asarray(Image.fromarray((gl*255).astype("uint8")).filter(ImageFilter.MinFilter(51)).filter(ImageFilter.GaussianBlur(25)), float)/255
base = np.asarray(Image.fromarray((base*255).astype("uint8")).resize((W, H), Image.BILINEAR), float)/255
yy, xx = np.mgrid[0:H, 0:W]; xx = xx / s; yy = yy / s
gn = np.zeros((H, W)); gw = np.zeros((H, W))
for cx in (534, 855):
    gn = np.maximum(gn, np.exp(-(((xx-cx)/SX)**2 + ((yy-150)/SY)**2)))       # the part of the pool we keep
    gw = np.maximum(gw, np.exp(-(((xx-cx)/(SX*2.4))**2 + ((yy-230)/(SY*3.0))**2)))   # the whole area the pool used to cover
g = 1 - gw * (1 - np.maximum(gn, 0.30))
ex = np.maximum(0, L - base)
fac = np.where(L > 1e-4, (base + ex * g) / np.maximum(L, 1e-4), 1.0)[..., None]
zone = np.clip(wall, 0, 1) * (1 - clock)
zone = np.where((xx[..., None] < 190), 0, zone)                 # leave the radiator glare alone
a = a * (1 - zone) + a * fac * zone
# 2a) wall colour: muted olive, brightness untouched
h, sa, v = rgb2hsv(a); wk = wall[..., 0] * (1 - clock[..., 0]) * (1 - sm(np.maximum(0, L - base), 0.05, 0.30)) * 0.65
nh = h + ((58 - h + 180) % 360 - 180) * wk; ns = sa * (1 - wk) + 0.26 * wk
a = hsv2rgb(nh, np.clip(ns, 0, 1), v)
# 2b) purple blotches on the wall: pull violet/magenta hues in the wall to muted olive, then even out the colour
h, sa, v = rgb2hsv(a)
vio = sm(h, 225, 250) * (1 - sm(h, 345, 358)) * sm(sa, 0.04, 0.10) * wall[..., 0]
nh = h + ((58 - h + 180) % 360 - 180) * vio
ns = sa * (1 - vio*0.8) + 0.20 * vio * 0.8
a = hsv2rgb(nh, np.clip(ns, 0, 1), v)
yc = Image.fromarray((np.clip(a,0,1)*255).astype("uint8")).convert("YCbCr"); Yw, Cbw, Crw = yc.split()
cbb = np.asarray(Cbw.filter(ImageFilter.GaussianBlur(18*s)), float); crb = np.asarray(Crw.filter(ImageFilter.GaussianBlur(18*s)), float)
wm = wall[..., 0] * (1 - clock[..., 0])
Cb3 = np.asarray(Cbw, float)*(1-wm) + cbb*wm; Cr3 = np.asarray(Crw, float)*(1-wm) + crb*wm
a = np.asarray(Image.merge("YCbCr", (Yw, Image.fromarray(Cb3.astype("uint8")), Image.fromarray(Cr3.astype("uint8")))).convert("RGB"), float)/255
# 3) throw blanket: blue-grey -> warm taupe (only blue-ish pixels inside the blanket polygon)
bl = mask([[(795,548),(868,514),(1002,512),(1118,550),(1040,566),(935,592),(872,690),(820,692)]], 3)
h, sa, v = rgb2hsv(a)
bluish = sm(h, 195, 215) * (1 - sm(h, 275, 290)) * sm(sa, 0.05, 0.12) * bl[..., 0]
nh = h + ((34 - h + 180) % 360 - 180) * bluish * 0.95
ns = sa * (1 - bluish*0.8) + 0.16 * bluish * 0.8
a = hsv2rgb(nh, np.clip(ns, 0, 1), v)
# 4) sofa chroma: blur the colour (not the brightness) so purple specks even out; table excluded
so = mask([[(228,408),(1182,408),(1182,712),(228,712)]], 4, minus=[[(335,592),(812,592),(812,800),(335,800)]])
ycc = Image.fromarray((np.clip(a,0,1)*255).astype("uint8")).convert("YCbCr"); Y, Cb, Cr = ycc.split()
cb = np.asarray(Cb.filter(ImageFilter.GaussianBlur(10*s)), float); cr = np.asarray(Cr.filter(ImageFilter.GaussianBlur(10*s)), float)
Cb0, Cr0 = np.asarray(Cb, float), np.asarray(Cr, float)
Cb2 = Cb0*(1-so[...,0]) + cb*so[...,0]; Cr2 = Cr0*(1-so[...,0]) + cr*so[...,0]
a = np.asarray(Image.merge("YCbCr", (Y, Image.fromarray(Cb2.astype("uint8")), Image.fromarray(Cr2.astype("uint8")))).convert("RGB"), float)/255
# 4b) clock face: even out the colour to a warm white (keeps the hands and tick marks)
fc = Image.new("L", (W, H), 0); ImageDraw.Draw(fc).ellipse([(673-50)*s,(215-50)*s,(673+50)*s,(215+50)*s], fill=255)
fc = np.asarray(fc.filter(ImageFilter.GaussianBlur(1.5*s)), float) / 255.0
h, sa, v = rgb2hsv(a); fw = fc * sm(v, 0.40, 0.55)
nh = h + ((40 - h + 180) % 360 - 180) * fw; ns = sa * (1 - fw) + 0.06 * fw
a = hsv2rgb(nh, np.clip(ns, 0, 1), v)
# 5) soft shoulder on highlights
y = np.where(a > 0.55, 0.55 + (a - 0.55) * 0.6, a)
Image.fromarray((np.clip(y,0,1)*255).astype("uint8")).save(outp)
l = y @ LW; print("mean %.3f P5 %.3f P95 %.3f P99.5 %.3f" % (l.mean(), np.percentile(l,5), np.percentile(l,95), np.percentile(l,99.5)))
