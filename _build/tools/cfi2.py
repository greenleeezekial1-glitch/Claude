# Version 2 deck design: navy title bar, callout boxes, section dividers, quick checks.
import os, re, math
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = 'Arial'
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
BLUE = RGBColor(0x2E, 0x75, 0xB6)
AMBER = RGBColor(0xE8, 0xA2, 0x00)
INK = RGBColor(0x26, 0x2B, 0x33)
GRAY = RGBColor(0x6B, 0x72, 0x80)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LINE = RGBColor(0xD0, 0xD5, 0xDD)
FILL = {'know': (RGBColor(0xFF, 0xF4, 0xD6), AMBER, 'KNOW THIS FOR THE CHECKRIDE'),
        'memory': (RGBColor(0xEE, 0xE8, 0xFA), RGBColor(0x6B, 0x4F, 0xBB), 'MEMORY AID'),
        'example': (RGBColor(0xE6, 0xF4, 0xEA), RGBColor(0x2E, 0x7D, 0x32), 'EXAMPLE'),
        'analogy': (RGBColor(0xE6, 0xF4, 0xEA), RGBColor(0x2E, 0x7D, 0x32), 'THINK OF IT LIKE THIS'),
        'ask': (RGBColor(0xE8, 0xF1, 0xFA), BLUE, 'ASK YOUR STUDENT'),
        'scenario': (RGBColor(0xFD, 0xEC, 0xEA), RGBColor(0xC6, 0x28, 0x28), 'REAL WORLD SCENARIO')}
SW, SH = Inches(13.333), Inches(7.5)
EMBED = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_embed')


def est_height(paras, pt, width_in, spacing=4):
    """Rough text height in inches for Arial."""
    cpl = max(10, int(width_in * 72 / (pt * 0.50)))
    lines = sum(max(1, math.ceil(len(p) / cpl)) for p in paras)
    return (lines * pt * 1.22 + len(paras) * spacing) / 72


def fit_size(paras, width_in, height_in, hi=16, lo=11, spacing=4):
    for pt in range(hi, lo - 1, -1):
        if est_height(paras, pt, width_in, spacing) <= height_in:
            return pt
    return None


def _font(run, size, color=INK, bold=False, italic=False):
    f = run.font; f.name = FONT; f.size = Pt(size); f.bold = bold; f.italic = italic; f.color.rgb = color


def _box(slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    if fill is None: s.fill.background()
    else: s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None: s.line.fill.background()
    else: s.line.color.rgb = line; s.line.width = Pt(1)
    s.shadow.inherit = False
    s.text_frame.text = ''
    return s


def _tb(slide, x, y, w, h, runs_paras, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT, space=4, margin=0.05):
    """runs_paras: list of paragraphs; each paragraph is list of (text, size, color, bold, italic) or dict with bullet."""
    tb = slide.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(margin); tf.margin_top = tf.margin_bottom = Inches(0.03)
    for i, para in enumerate(runs_paras):
        bullet = False
        if isinstance(para, dict): bullet = para.get('bullet', False); para = para['runs']
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(space)
        if bullet: _bullet(p)
        for (t, sz, col, b, it) in para:
            r = p.add_run(); r.text = t; _font(r, sz, col, b, it)
    return tb


def _bullet(p, char='■', color='2E75B6'):
    pPr = p._p.get_or_add_pPr()
    pPr.set('marL', str(Emu(Inches(0.3)))); pPr.set('indent', str(-Emu(Inches(0.25))))
    bc = OxmlElement('a:buClr'); s = OxmlElement('a:srgbClr'); s.set('val', color); bc.append(s); pPr.append(bc)
    bs = OxmlElement('a:buSzPct'); bs.set('val', '70000'); pPr.append(bs)
    bf = OxmlElement('a:buFont'); bf.set('typeface', FONT); pPr.append(bf)
    ch = OxmlElement('a:buChar'); ch.set('char', char); pPr.append(ch)


def _picture(slide, path, x, y, w, h, frame=True):
    im = Image.open(path); iw, ih = im.size
    sc = min(w / iw, h / ih); pw, ph = int(iw * sc), int(ih * sc)
    r = min(1.0, 1800 / max(iw, ih))
    src = os.path.join(EMBED, os.path.basename(path)[:-4] + '.jpg')
    os.makedirs(EMBED, exist_ok=True)
    if not os.path.exists(src):
        im.convert('RGB').resize((int(iw * r), int(ih * r)), Image.LANCZOS).save(src, quality=88, optimize=True)
    px, py = x + (w - pw) // 2, y + (h - ph) // 2
    pic = slide.shapes.add_picture(src, px, py, pw, ph)
    if frame: pic.line.color.rgb = LINE; pic.line.width = Pt(1)
    return (px, py, pw, ph)


def _title_bar(slide, title, code, n):
    _box(slide, 0, 0, SW, Inches(1.05), NAVY)
    _box(slide, 0, Inches(1.05), SW, Inches(0.06), AMBER)
    sz = 30 if len(title) < 42 else 26 if len(title) < 54 else 22
    _tb(slide, Inches(0.45), Inches(0.12), Inches(9.9), Inches(0.85), [[(title, sz, WHITE, True, False)]], anchor=MSO_ANCHOR.MIDDLE)
    if code:
        pill = _box(slide, Inches(10.45), Inches(0.33), Inches(2.5), Inches(0.42), BLUE, None, MSO_SHAPE.ROUNDED_RECTANGLE)
        tf = pill.text_frame; tf.margin_left = tf.margin_right = Inches(0.05)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = code if len(code) < 40 else code[:38] + '...'; _font(r, 11 if len(code) < 24 else 9, WHITE, True)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE


def _footer(slide, cite, n, dark=False):
    col = RGBColor(0xC8, 0xD3, 0xE3) if dark else GRAY
    if not dark: _box(slide, Inches(0.45), Inches(7.0), Inches(12.43), Emu(9525), LINE)
    _tb(slide, Inches(0.45), Inches(7.03), Inches(11.4), Inches(0.38), [[(('Source: ' + cite) if cite else '', 10, col, False, False)]])
    _tb(slide, Inches(12.1), Inches(7.03), Inches(0.8), Inches(0.38), [[(str(n), 10, col, False, False)]], align=PP_ALIGN.RIGHT)


def _callout(slide, kind, text, x, y, w, max_h, label=None):
    fill, edge, lab = FILL[kind]; lab = label or lab
    pt = fit_size([text], w / 914400 - 0.35, max_h / 914400 - 0.42, hi=14, lo=10)
    if pt is None: pt = 10
    h_in = est_height([text], pt, w / 914400 - 0.35) + 0.45
    h = min(max_h, Inches(h_in))
    _box(slide, x, y, w, h, fill)
    _box(slide, x, y, Inches(0.08), h, edge)
    _tb(slide, x + Inches(0.17), y + Inches(0.05), w - Inches(0.25), h - Inches(0.08),
        [[(lab, 10, edge, True, False)], [(text, pt, INK, False, False)]], space=2)
    return h


def _table(slide, rows, x, y, w, size=14, colw=None, bold_last=False):
    nr, nc = len(rows), len(rows[0]); rh = Inches(0.36)
    shp = slide.shapes.add_table(nr, nc, x, y, w, rh * nr); tbl = shp.table
    tblPr = tbl._tbl.tblPr
    st = tblPr.find(qn('a:tableStyleId'))
    if st is None: st = OxmlElement('a:tableStyleId'); tblPr.append(st)
    st.text = '{5940675A-B579-460E-94D1-54222C63F5DA}'
    if colw:
        for i, c in enumerate(colw): tbl.columns[i].width = int(w * c)
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            cell = tbl.cell(r, c); cell.text = ''
            num = all(re.fullmatch(r'[-0-9.,% ]*', str(rw[c])) for rw in rows[1:])
            p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT if (c > 0 and num) else PP_ALIGN.LEFT
            run = p.add_run(); run.text = str(v)
            _font(run, size, WHITE if r == 0 else INK, bold=(r == 0 or (bold_last and r == nr - 1)))
            cell.margin_left = cell.margin_right = Inches(0.08); cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.fill.solid()
            cell.fill.fore_color.rgb = NAVY if r == 0 else (RGBColor(0xF3, 0xF6, 0xFA) if r % 2 == 0 else WHITE)
    return rh * nr


def _is_tall(paths):
    for p in paths:
        w, h = Image.open(p).size
        if h / w > 0.85: return True
    return False


def _right_panel(slide, s, imgdir, callouts, x, y, w, h):
    """Images on top, callouts underneath. Returns callouts it did not place."""
    imgs = [s['img']] + ([s['img2']] if s.get('img2') else [])
    paths = [os.path.join(imgdir, i + '.png') for i in imgs]
    if _is_tall(paths):
        if len(paths) == 2:
            half = (w - Inches(0.15)) // 2
            _picture(slide, paths[0], x, y, half, h); _picture(slide, paths[1], x + half + Inches(0.15), y, half, h)
        else:
            _picture(slide, paths[0], x, y, w, h)
        return callouts
    reserve = 0
    for kind, text in callouts:
        reserve += min(Inches(1.9), Inches(est_height([text], 13, w / 914400 - 0.35) + 0.5)) + Inches(0.12)
    img_h = max(Inches(2.4), h - reserve)
    each = (img_h - Inches(0.1) * (len(paths) - 1)) // len(paths)
    cy = y
    for p in paths:
        px, py, pw, ph = _picture(slide, p, x, cy, w, each)
        cy = py + ph + Inches(0.1)
    left = []
    for kind, text in callouts:
        room = y + h - cy
        if room < Inches(0.8): left.append((kind, text)); continue
        used = _callout(slide, kind, text, x, cy, w, min(room, Inches(1.9)))
        cy += used + Inches(0.12)
    return left


def _left_text(slide, s, x, y, w, h, callouts=()):
    """Key points (bold) then explanation paragraphs, sized to fit. Callouts go at the bottom."""
    ch = []
    for kind, text in callouts:
        ch.append(Inches(min(1.7, est_height([text], 13, w / 914400 - 0.35) + 0.5)))
    h = h - sum(ch) - Inches(0.12) * len(ch)
    cy = y + h + Inches(0.12)
    for (kind, text), hh in zip(callouts, ch):
        used = _callout(slide, kind, text, x, cy, w, hh); cy += used + Inches(0.12)
    keys = s.get('bullets', [])
    detail = list(s.get('detail', []))
    while True:
        paras = keys + detail
        pt = fit_size(paras, w / 914400 - 0.4, h / 914400, hi=18, lo=12, spacing=6)
        if pt or not detail: break
        detail.pop()
    pt = pt or 12
    out = []
    for k in keys:
        if ': ' in k and len(k.split(': ')[0]) < 26:
            a, b = k.split(': ', 1)
            out.append({'bullet': True, 'runs': [(a + ': ', pt + 1, NAVY, True, False), (b, pt + 1, INK, False, False)]})
        else:
            out.append({'bullet': True, 'runs': [(k, pt + 1, NAVY, True, False)]})
    if detail:
        out.append([(' ', 4, INK, False, False)])
        for d in detail: out.append([(d, pt, INK, False, False)])
    _tb(slide, x, y, w, h, out, space=6)
    return len(detail)


def build_deck(slides, imgdir, out):
    prs = Presentation(); prs.slide_width, prs.slide_height = SW, SH
    blank = prs.slide_layouts[6]
    for n, s in enumerate(slides, 1):
        sl = prs.slides.add_slide(blank); kind = s.get('kind', 'content')
        if kind == 'title':
            _box(sl, 0, 0, Inches(6.2), SH, NAVY); _box(sl, Inches(6.2), 0, Inches(0.08), SH, AMBER)
            _tb(sl, Inches(0.6), Inches(1.3), Inches(5.3), Inches(2.4), [[(s['title'], 38, WHITE, True, False)]], anchor=MSO_ANCHOR.BOTTOM)
            _tb(sl, Inches(0.6), Inches(3.9), Inches(5.3), Inches(2.6), [[(b, 18, RGBColor(0xDC, 0xE6, 0xF2), False, False)] for b in s['bullets']], space=8)
            _picture(sl, os.path.join(imgdir, s['img'] + '.png'), Inches(6.7), Inches(0.7), Inches(6.2), Inches(5.9))
            _footer(sl, s.get('cite'), n, dark=True)
        elif kind == 'section':
            _box(sl, 0, 0, SW, SH, NAVY); _box(sl, 0, Inches(5.05), SW, Inches(0.06), AMBER)
            _tb(sl, Inches(0.7), Inches(0.7), Inches(7.0), Inches(0.5), [[(s.get('code', ''), 16, AMBER, True, False)]])
            _tb(sl, Inches(0.7), Inches(1.2), Inches(7.0), Inches(1.6), [[(s['title'], 36, WHITE, True, False)]], anchor=MSO_ANCHOR.TOP)
            _tb(sl, Inches(0.7), Inches(2.9), Inches(6.8), Inches(2.0),
                [[('What you will learn', 14, AMBER, True, False)]] + [{'bullet': True, 'runs': [(g, 18, WHITE, False, False)]} for g in s['goals']], space=6)
            _tb(sl, Inches(0.7), Inches(5.3), Inches(12.0), Inches(1.4), [[(s.get('why', ''), 16, RGBColor(0xDC, 0xE6, 0xF2), False, True)]])
            _picture(sl, os.path.join(imgdir, s['img'] + '.png'), Inches(7.9), Inches(0.6), Inches(4.9), Inches(4.2), frame=False)
            _footer(sl, s.get('cite'), n, dark=True)
        elif kind == 'check':
            _title_bar(sl, s['title'], s.get('code'), n)
            qs = s['qa']; cols = 1 if len(qs) <= 3 else 2
            colw = Inches(12.4) if cols == 1 else Inches(6.1)
            rows = math.ceil(len(qs) / cols); qpt = 20 if cols == 1 else 16
            tw = colw / 914400 - 1.0
            need = [Inches(est_height([q], qpt, tw) + est_height([a], qpt - 3, tw) + 0.45) for q, a in qs]
            rh = min((Inches(5.5) - Inches(0.2) * (rows - 1)) // rows, max(need))
            for i, (q, a) in enumerate(qs):
                cx = Inches(0.45) + (i // rows) * (colw + Inches(0.2)); cy = Inches(1.4) + (i % rows) * (rh + Inches(0.2))
                _box(sl, cx, cy, colw, rh, RGBColor(0xF3, 0xF6, 0xFA), LINE, MSO_SHAPE.ROUNDED_RECTANGLE)
                num = _box(sl, cx + Inches(0.15), cy + Inches(0.15), Inches(0.5), Inches(0.5), BLUE, None, MSO_SHAPE.OVAL)
                p = num.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; r = p.add_run(); r.text = str(i + 1); _font(r, 16, WHITE, True)
                _tb(sl, cx + Inches(0.8), cy + Inches(0.12), colw - Inches(1.0), rh - Inches(0.2),
                    [[(q, qpt, NAVY, True, False)], [('Answer: ', qpt - 3, RGBColor(0x2E, 0x7D, 0x32), True, False), (a, qpt - 3, INK, False, False)]], space=6)
            if s.get('img'):
                yb = Inches(1.4) + rows * (rh + Inches(0.2))
                if Inches(6.85) - yb > Inches(2.4):
                    _picture(sl, os.path.join(s['_imgdir'], s['img'] + '.png'), Inches(3.5), yb, Inches(6.3), Inches(6.85) - yb)
            _footer(sl, s.get('cite'), n)
        else:
            _title_bar(sl, s['title'], s.get('code'), n)
            lp = s.get('lp', {})
            callouts = []
            for k in ('know', 'memory', 'scenario'):
                if s.get(k): callouts.append((k, s[k]))
            if lp.get('example') and len(callouts) < 2: callouts.append(('example', lp['example']))
            if lp.get('analogy') and len(callouts) < 2: callouts.append(('analogy', lp['analogy'].replace('Analogy: ', '').replace('Analogy from the PHAK: ', '')))
            callouts = callouts[:2]
            top, bottom = Inches(1.35), Inches(6.85)
            if kind == 'definition':
                y = top
                for term, d in s['defs']:
                    txt = '“' + d + '”'
                    pt = fit_size([txt], 6.1, 2.0, hi=17, lo=13) or 13
                    hh = Inches(est_height([txt], pt, 6.1) + 0.55)
                    _box(sl, Inches(0.45), y, Inches(6.6), hh, RGBColor(0xE8, 0xF1, 0xFA))
                    _box(sl, Inches(0.45), y, Inches(0.08), hh, BLUE)
                    _tb(sl, Inches(0.65), y + Inches(0.06), Inches(6.3), hh, [[(term.upper(), 12, BLUE, True, False)], [(txt, pt, INK, False, True)]], space=3)
                    y += hh + Inches(0.15)
                plain = s.get('plain') or (lp.get('teach') or [''])[-1]
                if plain and bottom - y > Inches(0.8):
                    _callout(sl, 'know' if s.get('plain') else 'example', plain, Inches(0.45), y, Inches(6.6), bottom - y,
                             label='IN PLAIN WORDS' if s.get('plain') else 'TEACHING NOTE')
                _right_panel(sl, s, s['_imgdir'], callouts[:1], Inches(7.35), top, Inches(5.53), bottom - top)
            elif kind == 'table':
                y = top
                if s.get('bullets'):
                    _tb(sl, Inches(0.45), y, Inches(6.6), Inches(0.9), [{'bullet': True, 'runs': [(b, 16, NAVY, True, False)]} for b in s['bullets']], space=3)
                    y += Inches(0.42 * len(s['bullets']) + 0.1)
                th = _table(sl, s['table'], Inches(0.45), y, Inches(6.6), size=s.get('tsize', 14), colw=s.get('colw'), bold_last=s.get('bold_last', False))
                y += th + Inches(0.2)
                imgs = [s['img']] + ([s['img2']] if s.get('img2') else [])
                tall = _is_tall([os.path.join(s['_imgdir'], i + '.png') for i in imgs])
                if tall and callouts:
                    for kind, text in callouts:
                        hh = Inches(min(1.6, est_height([text], 13, 6.25) + 0.5))
                        _callout(sl, kind, text, Inches(0.45), bottom - hh, Inches(6.6), hh)
                        bottom_text = bottom - hh - Inches(0.12)
                        bottom = bottom_text
                    callouts = []
                det = s.get('detail', [])
                if det and bottom - y > Inches(0.6):
                    keep = list(det)
                    while keep and not fit_size(keep, 6.2, (bottom - y) / 914400, hi=14, lo=11): keep.pop()
                    if keep:
                        pt = fit_size(keep, 6.2, (bottom - y) / 914400, hi=14, lo=11)
                        _tb(sl, Inches(0.45), y, Inches(6.6), bottom - y, [[(d, pt, INK, False, False)] for d in keep], space=5)
                _right_panel(sl, s, s['_imgdir'], callouts, Inches(7.35), top, Inches(5.53), Inches(6.85) - top)
            else:
                imgs = [s['img']] + ([s['img2']] if s.get('img2') else [])
                tall = _is_tall([os.path.join(s['_imgdir'], i + '.png') for i in imgs])
                _left_text(sl, s, Inches(0.45), top, Inches(6.6), bottom - top, callouts if tall else ())
                _right_panel(sl, s, s['_imgdir'], [] if tall else callouts, Inches(7.35), top, Inches(5.53), bottom - top)
            _footer(sl, s.get('cite'), n)
        sl.notes_slide.notes_text_frame.text = s.get('notes', '')
    prs.save(out)
    return len(slides)


def expand(task, extras, imgdir):
    """Insert section and quick check slides, attach extras, and build per-slide detail text."""
    out = []
    sections = extras.get('SECTIONS', {}); checks = extras.get('CHECKS', {})
    for s in task['slides']:
        t = s['title']
        if t in sections:
            sec = dict(sections[t]); sec['kind'] = 'section'
            sec.setdefault('cite', sec.get('cite', 'FAA-S-ACS-25'))
            sec['notes'] = 'Section: ' + sec['title'] + '. ' + sec.get('why', '')
            sec['lp'] = {'teach': ['Section start: ' + sec['title'] + '. Goals: ' + '; '.join(sec['goals']) + '.']}
            out.append(sec)
        s = dict(s); s['_imgdir'] = imgdir
        for k in ('KNOW', 'MEMORY', 'SCENARIO', 'IMG2', 'PLAIN'):
            v = extras.get(k, {}).get(t)
            if v: s[{'KNOW': 'know', 'MEMORY': 'memory', 'SCENARIO': 'scenario', 'IMG2': 'img2', 'PLAIN': 'plain'}[k]] = v
        teach = (s.get('lp') or {}).get('teach', [])
        s['detail'] = [] if t in ('Review Questions', 'References') else [re.sub(r'\s+', ' ', x) for x in teach]
        out.append(s)
        if t in checks:
            c = dict(checks[t]); c['kind'] = 'check'; c['title'] = c.get('title', 'Quick Check')
            c['notes'] = 'Ask each question and let the student answer before showing the answer. ' + ' '.join(f'Q{i+1}: {q} A: {a}' for i, (q, a) in enumerate(c['qa']))
            c['lp'] = {'teach': ['Quick check. Ask each question, wait for the answer, then confirm.'], 'table': [['Question', 'Answer']] + [list(x) for x in c['qa']]}
            c['img'] = c.get('img', s['img']); c['_imgdir'] = imgdir
            out.append(c)
    return out
