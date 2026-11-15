# Lesson plan .docx styled to match a document typed in Google Docs with its default
# styles: Arial, Normal text 11 pt at 1.15 spacing, Title 26, Subtitle 15 gray,
# Heading 1 20, Heading 2 16, Heading 3 14 dark gray, headings not bold, 1 inch margins.
# Uses the real Title/Heading styles so Google Docs maps them and builds the outline.
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = 'Arial'
BLACK = RGBColor(0, 0, 0)


def _style(doc, name, size, color=BLACK, before=0, after=0, bold=False, italic=False):
    st = doc.styles[name]
    f = st.font; f.name = FONT; f.size = Pt(size); f.bold = bold; f.italic = italic; f.color.rgb = color
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    if rf is None: rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'): rf.set(qn(a), FONT)
    for t in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(t)) is not None: del rf.attrib[qn(t)]
    pf = st.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE; pf.line_spacing = 1.15
    # remove the Word heading border/underline and theme color on Title
    ppr = st.element.get_or_add_pPr()
    b = ppr.find(qn('w:pBdr'))
    if b is not None: ppr.remove(b)
    return st


def _setup(doc):
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(1)
    _style(doc, 'Normal', 11)
    _style(doc, 'Title', 26, after=3)
    _style(doc, 'Subtitle', 15, RGBColor(0x66, 0x66, 0x66), after=16)
    _style(doc, 'Heading 1', 20, before=20, after=6)
    _style(doc, 'Heading 2', 16, before=18, after=6)
    _style(doc, 'Heading 3', 14, RGBColor(0x43, 0x43, 0x43), before=16, after=4)
    lb = _style(doc, 'List Bullet', 11)
    for n in ('Heading 1', 'Heading 2', 'Heading 3'):
        doc.styles[n].paragraph_format.keep_with_next = True


def _p(doc, text='', lead=None, italic=False, style=None):
    p = doc.add_paragraph(style=style)
    if lead:
        r = p.add_run(lead + ' '); r.bold = True
    if text:
        r = p.add_run(text); r.italic = italic
    return p


def _bul(doc, items):
    for it in items:
        doc.add_paragraph(it, style='List Bullet')


def _table(doc, rows, widths):
    t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style = 'Table Grid'; t.autofit = False
    for j, w in enumerate(widths): t.columns[j].width = Inches(w)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            c = t.cell(i, j); c.width = Inches(widths[j]); c.text = ''
            par = c.paragraphs[0]; r = par.add_run(str(v)); r.bold = (i == 0)
    # Google Docs default table: 1 pt black borders
    tblPr = t._tbl.tblPr; borders = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{e}'); el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), '8'); el.set(qn('w:color'), '000000'); borders.append(el)
    tblPr.append(borders)
    doc.add_paragraph()
    return t


def build_lp(task, out):
    doc = Document(); _setup(doc)
    lp = task['lp']; slides = task['slides']
    doc.add_paragraph(f"{task['code']} {task['name']}", style='Title')
    doc.add_paragraph(f"Lesson Plan  |  ACS Task {task['acs_code']}  |  {task['author']}", style='Subtitle')
    total = lp['schedule'][-1][-1] if lp.get('schedule') else ''
    _p(doc, f"Area of Operation {task['area_num']}, {task['area_name']}. Cessna 172S NAV III (G1000). "
            f"Ground lesson, about {total}, taught with the matching slide deck ({len(slides)} slides).")

    doc.add_paragraph('Objective', style='Heading 1')
    _p(doc, lp['objective'])
    _p(doc, 'ACS objective: ' + task['acs_objective'], italic=True)

    doc.add_paragraph('Elements', style='Heading 1')
    rows = [['ACS code', 'Element', 'Slides']]
    for e in task['elements']:
        rows.append([e['code'], e['text'], ', '.join(str(n) for n in task['_cover'].get(e['code'], []))])
    _table(doc, rows, [1.3, 3.9, 1.3])

    doc.add_paragraph('Schedule', style='Heading 1')
    _table(doc, [['Part', 'Slides', 'Time']] + lp['schedule'], [3.6, 1.8, 1.1])

    doc.add_paragraph('Equipment', style='Heading 1')
    _bul(doc, lp['equipment'])

    doc.add_paragraph('Introduction', style='Heading 1')
    for k in ('Attention', 'Motivation', 'Overview'):
        _p(doc, lp['intro'][k.lower()], lead=k + ':')

    doc.add_paragraph('Development', style='Heading 1')
    _p(doc, 'Teach the slides in order. Slide numbers match the deck.', italic=True)
    for n, s in enumerate(slides, 1):
        d = s.get('lp')
        if not d: continue
        kind = s.get('kind')
        if kind == 'section':
            doc.add_paragraph(f"Slide {n}: {s['title']}", style='Heading 2')
            _p(doc, s.get('why', ''), italic=True)
            _p(doc, '', lead='Goals for this step:')
            _bul(doc, s.get('goals', []))
            continue
        doc.add_paragraph(f"Slide {n}: {s['title']}", style='Heading 3' if kind == 'check' else 'Heading 2')
        if s.get('code') and kind != 'check': _p(doc, f"ACS {s['code']}", italic=True)
        if kind == 'check':
            _p(doc, 'Ask each question and wait for the answer before showing it.')
            _table(doc, [['Question', 'Answer']] + [list(x) for x in s['qa']], [3.0, 3.5])
        else:
            teach = []
            for t in d.get('teach', []):
                t = re.sub(r'^Read (both |the )?(PHAK )?definitions?( from [^.]*?)?( word for word)?( \([^)]*\))?\.\s*', '', t)
                if t: teach.append(t)
            if s.get('defs'):
                for term, df in s['defs']:
                    dp = doc.add_paragraph(style='List Bullet'); r = dp.add_run(term + ': '); r.bold = True
                    dp.add_run('\u201c' + df + '\u201d')
            if s.get('plain'): teach.insert(0, 'In plain words: ' + s['plain'])
            _bul(doc, teach)
            if d.get('example'): _p(doc, d['example'].replace('Example: ', ''), lead='Example:')
            if d.get('analogy'): _p(doc, d['analogy'].replace('Analogy: ', ''), lead='Analogy:')
            if d.get('table'): _table(doc, d['table'], [6.5 / len(d['table'][0])] * len(d['table'][0]))
            if d.get('ask'):
                _p(doc, '', lead='Ask the student:')
                _bul(doc, d['ask'])
        if d.get('next'): _p(doc, d['next'], lead='Transition:')
        if s.get('cite'): _p(doc, 'Source: ' + s['cite'], italic=True)

    doc.add_paragraph('Instructor Actions', style='Heading 1'); _bul(doc, lp['instructor'])
    doc.add_paragraph('Student Actions', style='Heading 1'); _bul(doc, lp['student'])
    doc.add_paragraph('Common Errors', style='Heading 1')
    for err, fix in lp['errors']: _p(doc, fix, lead=err + '.')
    doc.add_paragraph('Conclusion and Review', style='Heading 1')
    for para in lp['conclusion']: _p(doc, para)
    doc.add_paragraph('Completion Standards', style='Heading 1'); _bul(doc, lp['completion'])
    doc.add_paragraph('References', style='Heading 1'); _bul(doc, task['references'])
    doc.save(out)
