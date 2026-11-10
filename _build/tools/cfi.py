# Shared builder for CFI task decks (.pptx) and lesson plans (.docx).
# Look matches Google Slides "Simple Light": white, Arial, dark gray text, no effects.
import os, re
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from docx import Document
from docx.shared import Pt as DPt, RGBColor as DRGB, Inches as DIn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Arial"
TITLE_C = RGBColor(0x21, 0x21, 0x21)
BODY_C = RGBColor(0x42, 0x42, 0x42)
SMALL_C = RGBColor(0x75, 0x75, 0x75)
LINE_C = RGBColor(0xBD, 0xBD, 0xBD)
SW, SH = Inches(13.333), Inches(7.5)


def _run_fmt(run, size, color=BODY_C, bold=False, italic=False):
    f = run.font
    f.name = FONT; f.size = Pt(size); f.bold = bold; f.italic = italic; f.color.rgb = color


def _textbox(slide, x, y, w, h, paras, size=24, color=BODY_C, bullets=False, anchor=MSO_ANCHOR.TOP,
             align=PP_ALIGN.LEFT, bold=False, italic=False, space_after=10):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        para.space_after = Pt(space_after)
        if bullets:
            _set_bullet(para)
        r = para.add_run(); r.text = p
        _run_fmt(r, size, color, bold, italic)
    return tb


def _set_bullet(para):
    pPr = para._p.get_or_add_pPr()
    pPr.set('marL', str(Emu(Inches(0.38)))); pPr.set('indent', str(-Emu(Inches(0.32))))
    for tag in ('a:buNone', 'a:buChar', 'a:buAutoNum'):
        for e in pPr.findall(qn(tag)): pPr.remove(e)
    bf = OxmlElement('a:buFont'); bf.set('typeface', FONT); pPr.append(bf)
    bc = OxmlElement('a:buChar'); bc.set('char', '•'); pPr.append(bc)


def _picture(slide, path, x, y, w, h):
    """Place image inside box keeping proportions, centered."""
    im = Image.open(path); iw, ih = im.size
    scale = min(w / iw, h / ih)
    pw, ph = int(iw * scale), int(ih * scale)
    src = path
    # embed a lighter JPEG copy (max 1800 px), same proportions; full-size PNG stays in the images folder
    r = min(1.0, 1800 / max(iw, ih)); small = im.convert('RGB').resize((int(iw * r), int(ih * r)), Image.LANCZOS)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_embed', os.path.basename(path)[:-4] + '.jpg')
    os.makedirs(os.path.dirname(src), exist_ok=True); small.save(src, quality=88, optimize=True)
    pic = slide.shapes.add_picture(src, x + (w - pw) // 2, y + (h - ph) // 2, pw, ph)
    pic.line.color.rgb = LINE_C; pic.line.width = Pt(0.75)
    return pic


def _table(slide, rows, x, y, w, size=16, col_w=None, bold_last=False):
    nr, nc = len(rows), len(rows[0])
    rh = Inches(0.42)
    shp = slide.shapes.add_table(nr, nc, x, y, w, rh * nr)
    tbl = shp.table
    # plain look: no banding, light header
    tblPr = tbl._tbl.tblPr
    tblPr.set('firstRow', '1'); tblPr.set('bandRow', '0')
    style = tblPr.find(qn('a:tableStyleId'))
    if style is None:
        style = OxmlElement('a:tableStyleId'); tblPr.append(style)
    style.text = '{5940675A-B579-460E-94D1-54222C63F5DA}'  # "No Style, Table Grid"
    if col_w:
        for i, cw in enumerate(col_w): tbl.columns[i].width = int(w * cw)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = tbl.cell(r, c); cell.text = ''
            tf = cell.text_frame; p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.RIGHT
            run = p.add_run(); run.text = str(val)
            _run_fmt(run, size, TITLE_C if r == 0 else BODY_C, bold=(r == 0 or (bold_last and r == nr - 1)))
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            if r == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0xEE, 0xEE, 0xEE)
            else:
                cell.fill.background()
    return shp


def _footer(slide, cite, code):
    if cite:
        _textbox(slide, Inches(0.5), Inches(6.98), Inches(10.6), Inches(0.4), [cite], size=11, color=SMALL_C)
    if code:
        _textbox(slide, Inches(9.2), Inches(0.12), Inches(3.9), Inches(0.35), [code], size=11, color=SMALL_C,
                 align=PP_ALIGN.RIGHT)


def _title(slide, text, size=32):
    _textbox(slide, Inches(0.5), Inches(0.45), Inches(12.3), Inches(0.95), [text], size=size, color=TITLE_C,
             anchor=MSO_ANCHOR.MIDDLE)


def build_deck(task, imgdir, out):
    prs = Presentation(); prs.slide_width, prs.slide_height = SW, SH
    blank = prs.slide_layouts[6]
    for n, s in enumerate(task['slides'], 1):
        sl = prs.slides.add_slide(blank)
        kind = s.get('kind', 'content')
        img = os.path.join(imgdir, s['img'] + '.png') if s.get('img') else None
        if kind == 'title':
            iw, ih = Image.open(img).size
            if iw / ih > 1.7:
                _textbox(sl, Inches(0.6), Inches(0.6), Inches(12.0), Inches(1.0), [s['title']], size=36, color=TITLE_C,
                         anchor=MSO_ANCHOR.BOTTOM)
                _textbox(sl, Inches(0.6), Inches(1.7), Inches(6.0), Inches(1.3), s['bullets'][:2], size=20, space_after=4)
                _textbox(sl, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.3), s['bullets'][2:], size=20, space_after=4)
                _picture(sl, img, Inches(0.6), Inches(2.9), Inches(12.1), Inches(3.95))
            else:
                _textbox(sl, Inches(0.6), Inches(1.6), Inches(6.0), Inches(2.0), [s['title']], size=36, color=TITLE_C,
                         anchor=MSO_ANCHOR.BOTTOM)
                _textbox(sl, Inches(0.6), Inches(3.8), Inches(6.0), Inches(2.4), s['bullets'], size=20, color=BODY_C,
                         space_after=6)
                _picture(sl, img, Inches(7.0), Inches(1.0), Inches(5.8), Inches(5.6))
        else:
            _title(sl, s['title'])
            if kind == 'definition':
                paras = []
                for term, d in s['defs']:
                    paras += [term, '“' + d + '”']
                tb = _textbox(sl, Inches(0.5), Inches(1.55), Inches(5.7), Inches(5.3), [], size=20)
                tf = tb.text_frame
                first = True
                for term, d in s['defs']:
                    p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
                    r = p.add_run(); r.text = term; _run_fmt(r, 22, TITLE_C, bold=True); p.space_after = Pt(4)
                    p = tf.add_paragraph(); r = p.add_run(); r.text = '“' + d + '”'
                    _run_fmt(r, s.get('defsize', 19), BODY_C); p.space_after = Pt(16)
                _picture(sl, img, Inches(6.5), Inches(1.5), Inches(6.35), Inches(5.3))
            elif kind == 'table':
                y = Inches(1.55)
                if s.get('bullets'):
                    _textbox(sl, Inches(0.5), y, Inches(5.8), Inches(1.2), s['bullets'], size=20, bullets=True,
                             space_after=4)
                    y = Inches(1.55 + 0.45 * len(s['bullets']) + 0.15)
                _table(sl, s['table'], Inches(0.5), y, Inches(5.8), size=s.get('tsize', 16), col_w=s.get('colw'),
                       bold_last=s.get('bold_last', False))
                _picture(sl, img, Inches(6.6), Inches(1.5), Inches(6.25), Inches(5.35))
            elif kind == 'wide':
                _textbox(sl, Inches(0.5), Inches(1.45), Inches(12.3), Inches(1.0), s['bullets'], size=22,
                         bullets=True, space_after=2)
                _picture(sl, img, Inches(0.5), Inches(1.45 + 0.48 * len(s['bullets']) + 0.15), Inches(12.3),
                         Inches(6.85 - (1.45 + 0.48 * len(s['bullets']) + 0.15)))
            else:
                iw, ih = Image.open(img).size
                if iw / ih > 1.7:
                    b = s['bullets']; half = (len(b) + 1) // 2
                    _textbox(sl, Inches(0.5), Inches(1.45), Inches(6.0), Inches(1.1), b[:half], size=22, bullets=True,
                             space_after=4)
                    _textbox(sl, Inches(6.8), Inches(1.45), Inches(6.0), Inches(1.1), b[half:], size=22, bullets=True,
                             space_after=4)
                    _picture(sl, img, Inches(0.5), Inches(2.6), Inches(12.3), Inches(4.25))
                else:
                    _textbox(sl, Inches(0.5), Inches(1.6), Inches(5.7), Inches(5.2), s['bullets'], size=24, bullets=True,
                             space_after=14)
                    _picture(sl, img, Inches(6.5), Inches(1.5), Inches(6.35), Inches(5.35))
        _footer(sl, s.get('cite'), s.get('code'))
        sl.notes_slide.notes_text_frame.text = s.get('notes', '')
    prs.save(out)
    return len(task['slides'])


# ---------------- lesson plan ----------------
def _d_font(run, size=11, bold=False, italic=False, color=None):
    run.font.name = FONT; run.font.size = DPt(size); run.font.bold = bold; run.font.italic = italic
    run._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
    if color: run.font.color.rgb = DRGB(*color)


def _h(doc, text, lvl=1):
    p = doc.add_paragraph(); r = p.add_run(text)
    _d_font(r, {0: 18, 1: 14, 2: 12}[lvl], bold=True, color=(0x21, 0x21, 0x21))
    p.paragraph_format.space_before = DPt(12 if lvl < 2 else 8); p.paragraph_format.space_after = DPt(4)
    p.paragraph_format.keep_with_next = True
    return p


def _p(doc, text, bold_lead=None, italic=False, style=None):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    if bold_lead:
        r = p.add_run(bold_lead + ' '); _d_font(r, bold=True)
    r = p.add_run(text); _d_font(r, italic=italic)
    p.paragraph_format.space_after = DPt(6)
    return p


def _bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style='List Bullet'); r = p.add_run(it); _d_font(r)
        p.paragraph_format.space_after = DPt(2)


def _dtable(doc, rows, widths=None, header=True):
    t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style = 'Table Grid'; t.autofit = False
    if not widths:
        widths = [6.7 / len(rows[0])] * len(rows[0])
    for j, w in enumerate(widths): t.columns[j].width = DIn(w)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            c = t.cell(i, j); c.text = ''
            r = c.paragraphs[0].add_run(str(v)); _d_font(r, 10, bold=(header and i == 0))
            if widths: c.width = DIn(widths[j])
    doc.add_paragraph()
    return t


def build_lp(task, out):
    doc = Document()
    st = doc.styles['Normal']; st.font.name = FONT; st.font.size = DPt(11)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
    for sec in doc.sections:
        sec.left_margin = sec.right_margin = DIn(0.9); sec.top_margin = sec.bottom_margin = DIn(0.8)
    lp = task['lp']
    # 1 title
    p = doc.add_paragraph(); r = p.add_run(f"{task['code']} {task['name']}"); _d_font(r, 18, bold=True)
    _p(doc, f"Lesson Plan. Area of Operation {task['area_num']}, {task['area_name']}. ACS Task code {task['acs_code']}.")
    _p(doc, task['author'])
    _p(doc, f"Ground lesson. Uses the matching slide deck \"{task['code']} {task['name']} - Slides\" ({len(task['slides'])} slides).", italic=True)
    # 2 objective
    _h(doc, '1. Objective')
    _p(doc, lp['objective'])
    _p(doc, 'ACS objective: ' + task['acs_objective'], italic=True)
    # 3 elements
    _h(doc, '2. Elements')
    rows = [['ACS code', 'Element', 'Slides']]
    for e in task['elements']:
        rows.append([e['code'], e['text'], ', '.join(str(n) for n in task['_cover'].get(e['code'], []))])
    _dtable(doc, rows, [1.4, 4.0, 1.3])
    # 4 schedule
    _h(doc, '3. Schedule')
    _dtable(doc, [['Part', 'Slides', 'Time']] + lp['schedule'], [3.7, 1.8, 1.2])
    # 5 equipment
    _h(doc, '4. Equipment')
    _bullets(doc, lp['equipment'])
    # 6 introduction
    _h(doc, '5. Introduction')
    for k in ('Attention', 'Motivation', 'Overview'):
        _p(doc, lp['intro'][k.lower()], bold_lead=k + ':')
    # 7 development
    _h(doc, '6. Development')
    _p(doc, 'Teach each slide in order. Slide numbers match the deck exactly.', italic=True)
    for n, s in enumerate(task['slides'], 1):
        d = s.get('lp')
        if not d: continue
        _h(doc, f"Slide {n}: {s['title']}", 2)
        if s.get('code'): _p(doc, s['code'], bold_lead='ACS:')
        for para in d.get('teach', []): _p(doc, para)
        if d.get('example'): _p(doc, d['example'], bold_lead='Example:')
        if d.get('analogy'): _p(doc, d['analogy'].replace('Analogy: ', ''), bold_lead='Analogy:')
        if d.get('table'): _dtable(doc, d['table'])
        if d.get('ask'):
            _p(doc, '', bold_lead='Ask the student:')
            _bullets(doc, d['ask'])
        if s.get('cite'): _p(doc, s['cite'], bold_lead='Source:')
    # 8 / 9
    _h(doc, '7. Instructor Actions'); _bullets(doc, lp['instructor'])
    _h(doc, '8. Student Actions'); _bullets(doc, lp['student'])
    # 10
    _h(doc, '9. Common Errors')
    for err, fix in lp['errors']: _p(doc, fix, bold_lead=err + '.')
    # 11
    _h(doc, '10. Conclusion and Review')
    for para in lp['conclusion']: _p(doc, para)
    # 12
    _h(doc, '11. Completion Standards')
    _bullets(doc, lp['completion'])
    # 13
    _h(doc, '12. References')
    _bullets(doc, task['references'])
    doc.save(out)


# ---------------- quality checks ----------------
BANNED = ["delve", "crucial", "pivotal", "robust", "seamless", "leverage", "tapestry", "it's important to note",
          "it is important to note", "in today's world", "let's dive in", "in conclusion", "navigate the complexities",
          "ensure", "furthermore", "moreover"]


def all_text(task):
    out = []
    def walk(o):
        if isinstance(o, str): out.append(o)
        elif isinstance(o, dict): [walk(v) for k, v in o.items() if not k.startswith('_')]
        elif isinstance(o, (list, tuple)): [walk(v) for v in o]
    walk(task); return out


def qa(task, imgdir):
    issues = []
    # coverage
    cover = {}
    for n, s in enumerate(task['slides'], 1):
        for c in re.findall(r'(?:FI|AI)\.[IVX]+\.[A-Z]\.[KRS]\d+[a-z]?', s.get('code', '')):
            cover.setdefault(c, []).append(n)
    task['_cover'] = cover
    for e in task['elements']:
        if e['code'] not in cover:
            # parent element counts as covered when all sub elements are covered
            subs = [x['code'] for x in task['elements'] if x['code'].startswith(e['code']) and x['code'] != e['code']]
            if subs and all(sc in cover for sc in subs):
                cover[e['code']] = sorted({n for sc in subs for n in cover[sc]})
            else:
                issues.append('element not covered: ' + e['code'])
    for n, s in enumerate(task['slides'], 1):
        if not s.get('img') or not os.path.exists(os.path.join(imgdir, s['img'] + '.png')):
            issues.append(f'slide {n}: missing image {s.get("img")}')
        if not s.get('cite'): issues.append(f'slide {n}: no citation')
        if not s.get('notes'): issues.append(f'slide {n}: no speaker notes')
        if s.get('kind') not in ('definition', 'title'):
            b = s.get('bullets', [])
            if len(b) > 4: issues.append(f'slide {n}: {len(b)} bullets')
            for x in b:
                if len(x.split()) > 7: issues.append(f'slide {n}: long bullet ({len(x.split())} words): {x}')
        if s.get('kind') != 'title' and not s.get('lp'): issues.append(f'slide {n}: no lesson plan section')
    for t in all_text(task):
        if re.search('[‒–—―]', t): issues.append('dash found: ' + t[:60])
        low = t.lower()
        for w in BANNED:
            if re.search(r'\b' + re.escape(w) + r'\b', low): issues.append(f'banned word "{w}": ' + t[:70])
    return issues
