import json,sys,os,glob
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,PatternFill
asel=json.load(open(sys.argv[1])); repo=sys.argv[2]
wb=Workbook(); ws=wb.active; ws.title='Master Index'
hdr=['Area','Area Name','Task','Task Name','ACS Code','Elements (K/R/S)','Slide File','Lesson Plan File','Slides','Status','Elements covered','Pictures on every slide','Bullet limits','Citations','Definitions word for word','LP matches deck','Dashes and banned words','Render check','Notes']
ws.append(hdr)
for c in ws[1]: c.font=Font(name='Arial',bold=True); c.fill=PatternFill('solid',fgColor='EEEEEE'); c.alignment=Alignment(wrap_text=True,vertical='top')
for ar in asel['kept']:
    folder=f"Area {ar['num']} - {ar['name']}"
    for t in ar['tasks']:
        code=f"{ar['num']}.{t['id']}"; base=f"{code} {t['name']}"
        q=os.path.join(repo,folder,f'.qa_{code}.json')
        row=[ar['num'],ar['name'],code,t['name'],f"{t['elements'][0]['code'].split('.')[0]}.{ar['num']}.{t['id']}",len(t['elements']),base+' - Slides',base+' - Lesson Plan']
        if os.path.exists(q):
            d=json.load(open(q)); ok='Pass' if not d['issues'] else 'Fix'
            row+= [d['slides'], d.get('status','Built')]+[ok]*7+['Pass', d.get('note','')]
        else:
            row+= ['', 'Not started']+['']*9
        ws.append(row)
for col,w in zip('ABCDEFGHIJKLMNOPQRS',[6,30,6,40,10,10,44,48,7,22,10,10,10,10,10,10,10,10,40]):
    ws.column_dimensions[col].width=w
for r in ws.iter_rows(min_row=2):
    for c in r: c.font=Font(name='Arial'); c.alignment=Alignment(wrap_text=True,vertical='top')
ws.freeze_panes='C2'
wb.save(os.path.join(repo,'Master Index.xlsx')); print('ok')
