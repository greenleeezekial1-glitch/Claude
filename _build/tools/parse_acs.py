import re, json, sys
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
start = next(i for i,l in enumerate(lines) if l.startswith('Area of Operation I. Fundamentals of Instructing') and i>200)
end = next(i for i,l in enumerate(lines) if i>start and l.strip().startswith('Appendix 1: Practical Test Roles'))
areas=[]; area=None; task=None; last=None; mode=None
code_re = re.compile(r'^\s*((?:FI|AI)\.[IVX]+\.[A-Z]\.[KRS] ?\d+[a-z]?)\s+(.*)$')
for l in lines[start:end]:
    s=l.strip()
    if not s or s.startswith('Flight Instructor for Airplane Category ACS') : continue
    m=re.match(r'^Area of Operation ([IVX]+)\. (.+)$', s)
    if m:
        if area is None or area['num']!=m.group(1):
            area={'num':m.group(1),'name':m.group(2),'note':'','tasks':[]}; areas.append(area); mode='areanote'; task=None
        continue
    m=re.match(r'^Task ([A-Z])\. (.+)$', s)
    if m:
        task={'id':m.group(1),'name':m.group(2),'refs':'','objective':'','notes':[],'elements':[]}; area['tasks'].append(task); mode='taskname'; last=None; continue
    if s.startswith('Note:'):
        tgt = task['notes'] if task else None
        if task: task['notes'].append(s[5:].strip()); mode='note'
        else: area['note']=s[5:].strip(); mode='areanote'
        continue
    if s.startswith('References:'):
        task['refs']=s[11:].strip(); mode='refs'; continue
    if s.startswith('Objective:'):
        task['objective']=s[10:].strip(); mode='obj'; continue
    m=code_re.match(l)
    if m:
        last={'code':m.group(1),'text':m.group(2).strip()}; task['elements'].append(last); mode='el'; continue
    if re.match(r'^(Knowledge:|Risk$|Management:|Skills:)', s): mode='hdr'; continue
    # continuation
    if mode=='el' and last: last['text']+=' '+s
    elif mode=='obj': task['objective']+=' '+s
    elif mode=='refs': task['refs']+=' '+s
    elif mode=='note' and task: task['notes'][-1]+=' '+s
    elif mode=='areanote' and not task: area['note']+=' '+s
    elif mode=='taskname' and task: task['name']+=' '+s
    elif mode=='areanote' and task is not None and area['tasks']==[]: area['note']+=' '+s
    else:
        if task and mode=='areanote': area['note']+=' '+s
        else: print('UNPLACED:',repr(s), file=sys.stderr)
    if mode=='hdr' : pass
json.dump(areas, open(sys.argv[2],'w'), indent=1)
for a in areas:
    print(a['num'],a['name'],len(a['tasks']))
    for t in a['tasks']: print('  ',t['id'],t['name'],len(t['elements']))
