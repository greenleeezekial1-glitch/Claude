import json,re,sys
book,pat=sys.argv[1],sys.argv[2]; ctx=int(sys.argv[3]) if len(sys.argv)>3 else 200
d=json.load(open(f'{sys.argv[4] if len(sys.argv)>4 else "."}/{book}.json'))
for k,v in d.items():
    t=re.sub(r'\s+',' ',v['text'])
    for m in re.finditer(pat,t,re.I):
        print(f"[{book} pdf{k} p{v['label']}] ...{t[max(0,m.start()-ctx//4):m.end()+ctx]}...")
