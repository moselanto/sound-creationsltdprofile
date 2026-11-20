#!/usr/bin/env python3
"""Export every profile page to a layered, Illustrator-editable SVG.

Each page becomes illustrator/svg/Page-NN-<name>.svg:
  * page size 297 x 210 mm (same as the PDF)
  * top-level groups = Illustrator layers (Background, Photo, Content ..., Logo, Footer)
  * all text is live <text> (one object per line) using Space Grotesk / Inter
  * cards, bars, lines and gradients are vector shapes; photos are embedded at full resolution
Usage: pip install weasyprint && python3 build/build-svg.py
"""
import base64, math, mimetypes, re, xml.etree.ElementTree as ET
from pathlib import Path
from weasyprint import HTML
from weasyprint.formatting_structure import boxes as B
from weasyprint.layout.replaced import replacedbox_layout

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'illustrator' / 'svg'
FONT_PS = {('Space Grotesk', 400): 'SpaceGrotesk-Regular', ('Space Grotesk', 500): 'SpaceGrotesk-Medium',
           ('Space Grotesk', 600): 'SpaceGrotesk-SemiBold', ('Space Grotesk', 700): 'SpaceGrotesk-Bold',
           ('Inter', 400): 'Inter-Regular', ('Inter', 500): 'Inter-Medium', ('Inter', 600): 'Inter-SemiBold',
           ('Inter', 700): 'Inter-Bold', ('Inter', 800): 'Inter-ExtraBold'}
USED_FONTS = set()
LAYER_NAMES = [
    ('bgimg', 'Photo'), ('sc-bg', 'Photo'), ('full', 'Photo'), ('fx-img', 'Photo'), ('tr-img', 'Photo'),
    ('ap-photo', 'Photo'), ('ct-photo', 'Photo and plan card'), ('side', 'Photo'), ('cv-glow', 'Red glow'),
    ('logo', 'Logo'), ('tag', 'Header label'), ('foot', 'Footer'), ('cbar', 'Footer'),
    ('cv-bottom', 'Company profile line'), ('cv', 'Cover title'), ('glance', 'At a glance'),
    ('sc-hero', 'Headline'), ('sc-band', 'Featured projects'), ('fx-c', 'Project write-up'),
    ('tr-c', 'Project lists'), ('rr-left', 'Headline and head office'), ('rr-right', 'Map and offices'),
    ('ct-left', 'Headline'), ('ct-info', 'Contact details'), ('pflow', 'Process steps'), ('svrow', 'Services'),
    ('acrow', 'Solutions and capabilities'), ('ap', 'Content'), ('bg-groups', 'Brand logos'),
    ('bg-bottom', 'Partners and footprint'), ('jr', 'Headline and photo'), ('tl', 'Timeline'),
]
PAGE_NAMES = {'cover': 'Cover', 'contents': 'Contents', 'journey': 'Our-Journey', 'process': 'How-We-Work',
              'audio': 'Professional-Audio', 'acoustics': 'Acoustics', 'showcase': 'Projects-Showcase',
              'completed': 'Completed-Projects', 'brands': 'Brands-and-Partners', 'reach': 'Regional-Reach',
              'contact': 'Contact'}

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def ai_id(name, used):
    """Illustrator turns ids into layer/object names and decodes _x20_ as a space."""
    base = re.sub(r'[^A-Za-z0-9_-]', lambda m: '_x%02X_' % ord(m.group(0)), name.strip()) or 'item'
    if base[0].isdigit(): base = '_' + base
    n, out = 1, base
    while out in used:
        n += 1; out = '%s_%d_' % (base, n)
    used.add(out); return out

def col(c):
    if c is None: return None, 0
    try: r, g, b = c.to('srgb').coordinates
    except Exception: r, g, b = c.coordinates[:3]
    a = c.alpha
    return '#%02X%02X%02X' % tuple(max(0, min(255, round(v * 255))) for v in (r, g, b)), a

def f(v): return ('%.2f' % v).rstrip('0').rstrip('.')

def rpath(x, y, w, h, radii):
    tl, tr, br, bl = radii
    if not any(r[0] or r[1] for r in radii):
        return 'M%s %sh%sv%sh%sz' % (f(x), f(y), f(w), f(h), f(-w))
    def cl(r): return (min(r[0], w / 2), min(r[1], h / 2))
    tl, tr, br, bl = map(cl, (tl, tr, br, bl))
    return ('M%s %s' % (f(x + tl[0]), f(y)) + 'H%s' % f(x + w - tr[0]) +
            'A%s %s 0 0 1 %s %s' % (f(tr[0]), f(tr[1]), f(x + w), f(y + tr[1])) + 'V%s' % f(y + h - br[1]) +
            'A%s %s 0 0 1 %s %s' % (f(br[0]), f(br[1]), f(x + w - br[0]), f(y + h)) + 'H%s' % f(x + bl[0]) +
            'A%s %s 0 0 1 %s %s' % (f(bl[0]), f(bl[1]), f(x), f(y + h - bl[1])) + 'V%s' % f(y + tl[1]) +
            'A%s %s 0 0 1 %s %s' % (f(tl[0]), f(tl[1]), f(x + tl[0]), f(y)) + 'Z')

class Page:
    def __init__(self):
        self.defs, self.used, self.n = [], set(), 0
    def uid(self, p):
        self.n += 1; return '%s%d' % (p, self.n)

def label(box):
    el = box.element
    cls = (el.get('class') or '') if el is not None else ''
    tag = box.element_tag or 'item'
    return (cls.split()[0] if cls else tag).replace('::', '-')

def gradient(pg, img, w, h, style, ox, oy):
    try:
        lay = img.layout(w, h, style)
    except Exception:
        return None
    scale_y, kind, pts, positions, colors = lay[:5]
    gid = pg.uid('grad')
    stops = ''.join('<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % (f(max(0, min(1, p))), *col(c))
                    for p, c in zip(positions, colors))
    if kind == 'linear':
        x0, y0, x1, y1 = pts
        pg.defs.append('<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient>'
                       % (gid, f(ox + x0), f(oy + y0), f(ox + x1), f(oy + y1), stops))
    elif kind == 'radial':
        cx, cy, r0, cx1, cy1, r1 = pts
        tr = ' gradientTransform="translate(%s %s) scale(1 %s) translate(%s %s)"' % (f(ox + cx1), f(oy + cy1 * scale_y if False else oy + cy1), f(scale_y), f(-(ox + cx1)), f(-(oy + cy1))) if scale_y != 1 else ''
        pg.defs.append('<radialGradient id="%s" gradientUnits="userSpaceOnUse" cx="%s" cy="%s" r="%s"%s>%s</radialGradient>'
                       % (gid, f(ox + cx1), f(oy + cy1), f(r1), tr, stops))
    else:
        return None
    return gid

def draw_background(pg, box, out):
    bg = getattr(box, 'background', None)
    if not bg: return
    c, a = col(bg.color)
    if a and a > 0:
        x, y, w, h, *radii = box.rounded_border_box()
        out.append('<path d="%s" fill="%s"%s/>' % (rpath(x, y, w, h, radii), c, '' if a >= 1 else ' fill-opacity="%s"' % f(a)))
    for layer in reversed(bg.layers):
        if layer.image is None: continue
        px, py, pw, ph = layer.painting_area
        posx, posy, _, _ = layer.positioning_area
        iw, ih = layer.size
        gid = gradient(pg, layer.image, iw, ih, box.style, posx + layer.position[0], posy + layer.position[1])
        if gid:
            x, y, w, h, *radii = box.rounded_border_box()
            out.append('<path d="%s" fill="url(#%s)"/>' % (rpath(x, y, w, h, radii), gid))

def draw_borders(box, out):
    st = box.style
    sides = []
    for s in ('top', 'right', 'bottom', 'left'):
        w = getattr(box, 'border_%s_width' % s, 0) or 0
        c, a = col(st['border_%s_color' % s]) if st['border_%s_style' % s] not in ('none', 'hidden') else (None, 0)
        sides.append((w, c, a))
    if not any(w and a for w, c, a in sides): return
    x, y, w, h, *radii = box.rounded_border_box()
    if w == 0 and h == 0 or (box.width == 0 and box.height == 0):
        # CSS border triangle (arrowheads)
        t, r, b, l = sides
        if l[0] and l[2]:
            out.append('<path d="M%s %sL%s %sL%s %sZ" fill="%s"/>' % (f(x), f(y), f(x + l[0]), f(y + (t[0] + b[0]) / 2), f(x), f(y + t[0] + b[0]), l[1]))
        return
    if len({(s[0], s[1], round(s[2], 3)) for s in sides}) == 1:
        bw, c, a = sides[0]
        ins = [(max(0, r[0] - bw / 2), max(0, r[1] - bw / 2)) for r in radii]
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s/>' % (
            rpath(x + bw / 2, y + bw / 2, w - bw, h - bw, ins), c, f(bw), '' if a >= 1 else ' stroke-opacity="%s"' % f(a)))
        return
    t, r, b, l = sides
    rects = []
    if t[0] and t[2]: rects.append((x, y, w, t[0], t))
    if b[0] and b[2]: rects.append((x, y + h - b[0], w, b[0], b))
    if l[0] and l[2]: rects.append((x, y, l[0], h, l))
    if r[0] and r[2]: rects.append((x + w - r[0], y, r[0], h, r))
    for rx, ry, rw, rh, (bw, c, a) in rects:
        out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"%s/>' % (f(rx), f(ry), f(rw), f(rh), c, '' if a >= 1 else ' fill-opacity="%s"' % f(a)))

def draw_image(pg, box, out):
    rep = box.replacement
    name = type(rep).__name__
    cx, cy = box.content_box_x(), box.content_box_y()
    if name == 'SVGImage' and box.element is not None:
        el = box.element
        ns = '{http://www.w3.org/2000/svg}'
        vb = el.get('viewBox', '0 0 %s %s' % (box.width, box.height))
        inner = ''.join(ET.tostring(ch, encoding='unicode').replace('ns0:', '').replace(':ns0', '').replace(' xmlns="http://www.w3.org/2000/svg"', '') for ch in el)
        out.append('<svg x="%s" y="%s" width="%s" height="%s" viewBox="%s" overflow="visible">%s</svg>' % (f(cx), f(cy), f(box.width), f(box.height), vb, inner))
        return
    src = box.element.get('src') if box.element is not None else None
    if not src: return
    p = ROOT / src
    data = base64.b64encode(p.read_bytes()).decode()
    mime = mimetypes.guess_type(str(p))[0] or 'image/jpeg'
    dw, dh, dx, dy = replacedbox_layout(box)
    x, y, w, h, *radii = box.rounded_padding_box()
    cid = pg.uid('clip')
    pg.defs.append('<clipPath id="%s"><path d="%s"/></clipPath>' % (cid, rpath(x, y, w, h, radii)))
    out.append('<g clip-path="url(#%s)"><image id="%s" x="%s" y="%s" width="%s" height="%s" preserveAspectRatio="none" xlink:href="data:%s;base64,%s"/></g>'
               % (cid, ai_id(Path(src).stem, pg.used), f(dx), f(dy), f(dw), f(dh), mime, data))

def text_attrs(st):
    fam = st['font_family'][0]
    wt = int(st['font_weight']) if str(st['font_weight']).isdigit() else 400
    USED_FONTS.add((fam, wt))
    c, a = col(st['color'])
    ls = st['letter_spacing']
    ls = '' if ls == 'normal' or not ls else ' letter-spacing="%s"' % f(ls)
    italic = ' font-style="italic"' if st['font_style'] == 'italic' else ''
    return ('font-family="%s" font-weight="%d" font-size="%s"%s%s fill="%s"%s'
            % (fam, wt, f(st['font_size']), ls, italic, c, '' if a >= 1 else ' fill-opacity="%s"' % f(a)))

def text_runs(box):
    if isinstance(box, B.TextBox):
        if box.text.strip() or box.text: yield box
        return
    for ch in getattr(box, 'children', []) or []:
        yield from text_runs(ch)

def draw_line(box, out):
    """One editable <text> object per line; each styled run is a <tspan> at its exact position."""
    runs = [r for r in text_runs(box) if r.text]
    if not any(r.text.strip() for r in runs): return
    first = runs[0]
    spans = ''.join('<tspan x="%s" y="%s" %s>%s</tspan>' % (f(r.position_x), f(r.position_y + r.baseline), text_attrs(r.style), esc(r.text)) for r in runs)
    out.append('<text %s xml:space="preserve">%s</text>' % (text_attrs(first.style), spans))

def transform_attr(box):
    tr = box.style['transform']
    if not tr: return ''
    x, y, w, h = box.border_box_x(), box.border_box_y(), box.border_width(), box.border_height()
    ox, oy = x + w / 2, y + h / 2
    parts = []
    for name, args in tr:
        if name == 'rotate': parts.append('rotate(%s %s %s)' % (f(math.degrees(args)), f(ox), f(oy)))
        elif name == 'translate':
            parts.append('translate(%s %s)' % tuple(f(a.value if hasattr(a, 'value') else a) for a in args))
    return ' transform="%s"' % ' '.join(parts) if parts else ''

def draw_box(pg, box, out, depth=0):
    if type(box).__name__ == 'AbsolutePlaceholder':
        box = box._box
    st = box.style
    if st['visibility'] == 'hidden' or st['display'] == ('none',): return
    inner = []
    draw_background(pg, box, inner)
    draw_borders(box, inner)
    if isinstance(box, (B.BlockReplacedBox, B.InlineReplacedBox)):
        draw_image(pg, box, inner)
    kids = []
    if isinstance(box, B.LineBox):
        # backgrounds/borders of inline children first, then the line's text as one object
        for ch in box.children:
            if not isinstance(ch, B.TextBox):
                deco = []; draw_background(pg, ch, deco); draw_borders(ch, deco); kids += deco
        draw_line(box, kids)
    else:
        def zkey(t):
            i, ch = t
            real = ch._box if type(ch).__name__ == 'AbsolutePlaceholder' else ch
            z = real.style['z_index']
            positioned = real.style['position'] not in ('static',)
            return ((0 if z == 'auto' else z) if positioned else -0.5, i) if False else ((0 if z == 'auto' else z), i)
        for i, ch in sorted(enumerate(getattr(box, 'children', []) or []), key=zkey):
            draw_box(pg, ch, kids, depth + 1)
    if kids and st['overflow'] != 'visible' and not isinstance(box, (B.LineBox, B.InlineBox, B.TextBox)):
        x, y, w, h, *radii = box.rounded_padding_box()
        cid = pg.uid('clip')
        pg.defs.append('<clipPath id="%s"><path d="%s"/></clipPath>' % (cid, rpath(x, y, w, h, radii)))
        kids = ['<g clip-path="url(#%s)">' % cid] + kids + ['</g>']
    inner += kids
    if not inner: return
    op = st['opacity']
    attrs = transform_attr(box) + ('' if op is None or op >= 1 else ' opacity="%s"' % f(op))
    named = box.element is not None and box.element.get('class') and not isinstance(box, (B.LineBox, B.TextBox))
    if named or attrs:
        gid = ' id="%s"' % ai_id(label(box), pg.used) if named else ''
        out.append('<g%s%s>' % (gid, attrs)); out += inner; out.append('</g>')
    else:
        out += inner

def layer_name(box):
    el = box.element
    cls = ((el.get('class') or '') if el is not None else '').split()
    for key, name in LAYER_NAMES:
        if key in cls: return name
    return 'Content'

def export():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob('*.svg'): old.unlink()
    doc = HTML(filename=str(ROOT / 'index.html'), base_url=str(ROOT)).render()
    files = []
    for i, page in enumerate(doc.pages, 1):
        pg = Page()
        section = page._page_box.children[0].children[0].children[0]
        sid = section.element.get('id')
        layers = []
        bg = []; draw_background(pg, section, bg)
        if bg: layers.append(('Background', bg))
        kids = []
        for order, ch in enumerate(section.children):
            real = ch._box if type(ch).__name__ == 'AbsolutePlaceholder' else ch
            z = real.style['z_index']; z = 0 if z == 'auto' else z
            kids.append((z, order, real))
        for z, order, real in sorted(kids, key=lambda t: (t[0], t[1])):
            out = []; draw_box(pg, real, out)
            if out: layers.append((layer_name(real), out))
        # merge consecutive layers with the same name (Illustrator layer = contiguous z-range)
        merged = []
        for name, out in layers:
            if merged and merged[-1][0] == name: merged[-1][1].extend(out)
            else: merged.append([name, out])
        body = ''.join('<g id="%s">%s</g>' % (ai_id(name, pg.used), ''.join(out)) for name, out in reversed(list(reversed(merged))))
        W, H = page.width, page.height
        svg = ('<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
               'version="1.1" width="297mm" height="210mm" viewBox="0 0 %s %s">\n<title>Sound Creations Ltd Company Profile 2026 - Page %02d</title>\n<defs>%s</defs>\n%s\n</svg>\n'
               % (f(W), f(H), i, ''.join(pg.defs), body))
        fn = OUT / ('Page-%02d-%s.svg' % (i, PAGE_NAMES.get(sid, re.sub(r'\W+', '-', sid).title() if not re.match(r'fp\d', sid) else 'Featured-Project-%s' % sid[2:])))
        fn.write_text(svg, encoding='utf-8'); files.append(fn)
        print('Wrote', fn.name, '%.1f MB' % (fn.stat().st_size / 1e6), [m[0] for m in merged])
    print('Fonts used:', sorted(USED_FONTS))
    return files

if __name__ == '__main__':
    export()
