# usage: crop.py spec.json outdir   spec: [{name,pdf,page,box:[x0,y0,x1,y1] fractions,dpi?}]
import json,sys,subprocess,os
from PIL import Image, ImageChops
spec=json.load(open(sys.argv[1])); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
tmp=os.path.join(out,'_render')
cache={}
for s in spec:
    dpi=s.get('dpi',300); key=(s['pdf'],s['page'],dpi)
    if key not in cache:
        subprocess.run(['pdftoppm','-f',str(s['page']),'-l',str(s['page']),'-r',str(dpi),'-png','-singlefile',s['pdf'],tmp],check=True)
        cache[key]=Image.open(tmp+'.png').convert('RGB')
    im=cache[key]; W,H=im.size; x0,y0,x1,y1=s['box']
    c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
    if s.get('trim',True):
        g=c.convert('L').point(lambda v:255 if v>235 else 0)
        bg=Image.new('L',g.size,255); bbox=ImageChops.difference(g,bg).getbbox()
        if bbox:
            p=int(dpi*0.06); bbox=(max(0,bbox[0]-p),max(0,bbox[1]-p),min(c.width,bbox[2]+p),min(c.height,bbox[3]+p)); c=c.crop(bbox)
    c.save(os.path.join(out,s['name']+'.png')); print(s['name'],c.size)
if os.path.exists(tmp+'.png'): os.remove(tmp+'.png')
