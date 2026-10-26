"""Rebuild the authorized fur-only composite; never call a generation model."""
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

work = Path(__file__).resolve().parent
root = work.parent
cfg = json.loads((work / 'alignment.json').read_text(encoding='utf-8'))
base = Image.open(root / cfg['base']).convert('RGB')
source = Image.open(root / cfg['source']).convert('RGB')
scale = cfg['scale']
layer = Image.new('RGB', base.size)
layer.paste(source.resize((round(source.width * scale), round(source.height * scale)),
                          Image.Resampling.LANCZOS), tuple(cfg['offset']))
support = Image.new('L', base.size)
draw = ImageDraw.Draw(support)
for polygon in cfg['polygons']:
    draw.polygon([tuple(p) for p in polygon], fill=255)
protected = Image.new('L', base.size)
draw = ImageDraw.Draw(protected)
draw.rectangle((0, 0, base.width, 200), fill=255)
for polygon in cfg['protected_hands']:
    draw.polygon([tuple(p) for p in polygon], fill=255)

def cream_fur(pixels):
    z = pixels.astype(float)
    clip = cfg['fur_color_clip']
    return ((z[:, :, 0] - z[:, :, 1] < clip['max_r_minus_g']) &
            (z[:, :, 1] - z[:, :, 2] < clip['max_g_minus_b']) &
            (z[:, :, 1] > clip['min_g']))

b, s = np.asarray(base), np.asarray(layer)
allowed = (np.array(support) > 0) & (np.array(protected) == 0)
safe = allowed & cream_fur(b) & cream_fur(s)
mask = Image.fromarray((safe * 255).astype('uint8')).filter(ImageFilter.MinFilter(3))
alpha = np.minimum(np.array(mask), np.array(mask.filter(ImageFilter.GaussianBlur(cfg['feather_px']))))
mask = Image.fromarray(alpha.astype('uint8'))
result = Image.composite(layer, base, mask)
changed = np.any(np.asarray(result) != b, axis=2)
assert int(changed.sum()) > 1000, 'No meaningful fur transfer'
assert not changed[~allowed].any(), 'Protected face, hands or background changed'
assert not changed[alpha == 0].any(), 'Pixels outside mask changed'
result.save(root / 'assets/K05-H1_v07.png')
mask.save(work / 'fur-mask.png')
layer = layer.convert('RGBA')
layer.putalpha(mask)
layer.save(work / 'fur-layer.png')
box = (480, 130, 650, 405)
before = base.crop(box).resize((680, 1100))
after = result.crop(box).resize((680, 1100))
comparison = Image.new('RGB', (1360, 1130), 'white')
comparison.paste(before, (0, 30))
comparison.paste(after, (680, 30))
draw = ImageDraw.Draw(comparison)
draw.text((12, 8), 'BEFORE: v03', fill='black')
draw.text((692, 8), 'AFTER: v07 composite', fill='black')
comparison.save(work / 'before-after.png')
report = {'changed_pixels': int(changed.sum()), 'outside_mask_changed_pixels': 0,
          'protected_face_and_hands_changed_pixels': 0,
          'source_resampling': 'Lanczos at 0.29 scale; no generative redraw',
          'status': 'candidate_pending_user_review'}
(work / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report))
