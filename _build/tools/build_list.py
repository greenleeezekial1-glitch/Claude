import json,re,sys
a=json.load(open(sys.argv[1]))
fix=lambda s: re.sub(r'(\w)- (\w)', r'\1-\2', s).replace('POH)\\Airplane','POH)/Airplane')
DROP_TASK={('II','L'):'Seaplane only (ASES, AMES).',('II','P'):'Multiengine only (AMEL, AMES).',
 ('V','E'):'Seaplane only (ASES, AMES).',('VII','G'):'Seaplane only (ASES, AMES).',('VII','H'):'Seaplane only (ASES, AMES).',
 ('VII','I'):'Seaplane only (ASES, AMES).',('VII','J'):'Seaplane only (ASES, AMES).',('VII','K'):'Seaplane only (ASES, AMES).',
 ('VII','L'):'Seaplane only (ASES, AMES).',('XII','E'):'Multiengine only (AMEL, AMES).',('XII','F'):'Multiengine only (AMEL, AMES).',
 ('XII','G'):'Multiengine only (AMEL, AMES).',('XIII','A'):'Multiengine only (AMEL, AMES).',('XIII','B'):'Multiengine only (AMEL, AMES).',
 ('XIII','C'):'Multiengine only (AMEL, AMES).',('XIV','B'):'Seaplane only (ASES, AMES).'}
DROP_EL={'AI.II.E.K1k':'Water rudders, marked (ASES, AMES).','AI.VII.A.S7':'Water rudders, marked (ASES, AMES).',
 'AI.VII.A.S9':'Water spray on propeller, marked (ASES, AMES).','AI.VII.A.S10':'Planing attitude and porpoising, marked (ASES, AMES).'}
PARTIAL={'AI.VII.A.S6':'Teach the runway centerline part (ASEL). The takeoff path part is for seaplanes.',
 'AI.X.A.S2':'Use the 1,500 feet AGL value (ASEL). The 3,000 feet AGL value is for multiengine.',
 'AI.X.C.S2':'Use the 1,500 feet AGL value (ASEL). The 3,000 feet AGL value is for multiengine.',
 'AI.X.D.S2':'Use the 1,500 feet AGL value (ASEL). The 3,000 feet AGL value is for multiengine.',
 'AI.VI.B.S1':'Teach the airport part. Seaplane base items do not apply.'}
out={'kept':[], 'dropped_tasks':[], 'dropped_elements':[]}
for x in a:
  ar={'num':x['num'],'name':fix(x['name']),'note':fix(x['note']),'tasks':[]}
  for t in x['tasks']:
    key=(x['num'],t['id'])
    if key in DROP_TASK:
      out['dropped_tasks'].append({'code':f"{x['num']}.{t['id']}",'name':fix(t['name']),'why':DROP_TASK[key]}); continue
    els=[]
    for e in t['elements']:
      if e['code'] in DROP_EL:
        out['dropped_elements'].append({'code':e['code'],'text':fix(e['text']),'why':DROP_EL[e['code']]}); continue
      els.append({'code':e['code'],'text':fix(e['text']),'note':PARTIAL.get(e['code'],'')})
    ar['tasks'].append({'id':t['id'],'name':fix(t['name']),'refs':fix(t['refs']),'objective':fix(t['objective']),
       'notes':[fix(n) for n in t['notes']],'elements':els})
  if ar['tasks']: out['kept'].append(ar)
json.dump(out,open(sys.argv[2],'w'),indent=1)
nt=sum(len(x['tasks']) for x in out['kept']); ne=sum(len(t['elements']) for x in out['kept'] for t in x['tasks'])
print('kept tasks',nt,'elements',ne,'dropped tasks',len(out['dropped_tasks']),'dropped els',len(out['dropped_elements']))
# markdown
L=['# CFI ASEL Initial: ACS Task List','',"Source: Flight Instructor for Airplane Category ACS (FAA-S-ACS-25), November 2023, effective May 31, 2024. Checked on faa.gov: this is the current version and it lists no changes.",'',
 f'Kept for CFI initial, Airplane Single-Engine Land: {len(out["kept"])} Areas of Operation, {nt} Tasks, {ne} elements.','',
 'Element codes: Area I uses the prefix FI (for example FI.I.A.K1). Areas II through XIV use the prefix AI (for example AI.II.C.K2). This matches the ACS.','',
 '## Removed (not ASEL)','','### Whole Tasks','','| Task | Name | Why removed |','|---|---|---|']
for d in out['dropped_tasks']: L.append(f"| {d['code']} | {d['name']} | {d['why']} |")
L+=['','Area XIII (Multiengine Operations) is removed completely because all of its Tasks are multiengine only.','','### Single elements inside kept Tasks','','| Code | Element | Why removed |','|---|---|---|']
for d in out['dropped_elements']: L.append(f"| {d['code']} | {d['text']} | {d['why']} |")
L+=['','### Kept, but only the ASEL part applies','','| Code | What to teach |','|---|---|']
for k,v in PARTIAL.items(): L.append(f'| {k} | {v} |')
L+=['','## Evaluator selection rules (from the ACS notes)','', 'These do not remove anything. They show which Tasks the examiner must pick, so you know your highest priorities. You still need materials for every Task because the examiner can pick any of them.','']
for x in out['kept']:
  if x['note']: L.append(f"- Area {x['num']}: {x['note']}")
L+=['','## Full list','']
for x in out['kept']:
  L+=[f"## Area {x['num']} - {x['name']}",'']
  for t in x['tasks']:
    L+=[f"### {x['num']}.{t['id']} {t['name']}",'',f"References: {t['refs']}",'',f"Objective: {t['objective']}",'']
    for n in t['notes']: L+=[f'Note: {n}','']
    for kind,lab in (('K','Knowledge'),('R','Risk Management'),('S','Skills')):
      es=[e for e in t['elements'] if re.match(r'.*\.'+kind+r'\d',e['code'])]
      if not es: continue
      L.append(f'{lab}:')
      for e in es:
        ind='    ' if re.search(r'\d[a-z]$',e['code']) else ''
        L.append(f"{ind}- {e['code']} {e['text']}"+(f" (ASEL note: {e['note']})" if e['note'] else ''))
      L.append('')
open(sys.argv[3],'w').write('\n'.join(L)+'\n')
