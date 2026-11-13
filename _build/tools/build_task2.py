import sys, json, os, re, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cfi, cfi2
def load(p):
    sp = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
taskfile, extrasfile, imgdir, outdir, acsjson = sys.argv[1:6]
task = load(taskfile).TASK; ex = load(extrasfile)
extras = {k: getattr(ex, k, {}) for k in ('SECTIONS', 'CHECKS', 'KNOW', 'MEMORY', 'SCENARIO', 'IMG2', 'PLAIN', 'NEXT')}
titles = {s['title'] for s in task['slides']}
for k, d in extras.items():
    for t in d:
        if t not in titles: print('EXTRAS KEY NOT FOUND:', k, t)
if not task.get('elements'):
    a = json.load(open(acsjson))
    for ar in a['kept']:
        for t in ar['tasks']:
            if f"{ar['num']}.{t['id']}" == task['code']: task['elements'] = t['elements']
slides = cfi2.expand(task, extras, imgdir)
task['slides'] = slides
iss = [i for i in cfi.qa(task, imgdir) if 'bullet' not in i]
for s in slides:
    for k in ('img2',):
        if s.get(k) and not os.path.exists(os.path.join(imgdir, s[k] + '.png')): iss.append('missing img2 ' + s[k])
print('QA issues:', len(iss)); [print('  ', i) for i in iss]
os.makedirs(outdir, exist_ok=True)
base = f"{task['code']} {task['name']}"
n = cfi2.build_deck(slides, imgdir, os.path.join(outdir, base + ' - Slides.pptx'))
cfi.build_lp(task, os.path.join(outdir, base + ' - Lesson Plan.docx'))
json.dump({'code': task['code'], 'name': task['name'], 'slides': n, 'issues': iss, 'cover': task['_cover']}, open(os.path.join(outdir, '_qa.json'), 'w'), indent=1)
print('built', n, 'slides')
