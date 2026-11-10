import sys,json,os,importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cfi
taskfile,imgdir,outdir,acsjson=sys.argv[1:5]
spec=importlib.util.spec_from_file_location('t',taskfile); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
task=m.TASK
a=json.load(open(acsjson))
for ar in a['kept']:
    for t in ar['tasks']:
        if f"{ar['num']}.{t['id']}"==task['code']: task['elements']=t['elements']
iss=cfi.qa(task,imgdir)
print('QA issues:',len(iss)); [print('  ',i) for i in iss]
os.makedirs(outdir,exist_ok=True)
base=f"{task['code']} {task['name']}"
n=cfi.build_deck(task,imgdir,os.path.join(outdir,base+' - Slides.pptx'))
cfi.build_lp(task,os.path.join(outdir,base+' - Lesson Plan.docx'))
json.dump({'code':task['code'],'name':task['name'],'slides':n,'issues':iss,'cover':task['_cover']},open(os.path.join(outdir,'_qa.json'),'w'),indent=1)
print('built',n,'slides')
