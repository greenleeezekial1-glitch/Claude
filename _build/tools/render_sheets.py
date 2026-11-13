import sys,glob,subprocess,os
from PIL import Image
d=sys.argv[1]; dpi=sys.argv[2] if len(sys.argv)>2 else '40'
r=os.path.join(d,'render'); os.makedirs(r,exist_ok=True)
for f in glob.glob(os.path.join(d,'*.pptx'))+glob.glob(os.path.join(d,'*.docx')):
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',r,f],capture_output=True)
pdf=glob.glob(os.path.join(r,'*Slides.pdf'))[0]
for f in glob.glob(os.path.join(r,'s-*.png'))+glob.glob(os.path.join(r,'sheet*.png')): os.remove(f)
subprocess.run(['pdftoppm','-r',dpi,'-png',pdf,os.path.join(r,'s')])
fs=sorted(glob.glob(os.path.join(r,'s-*.png')))
for k in range(0,len(fs),9):
    ims=[Image.open(f) for f in fs[k:k+9]]; w,h=ims[0].size
    o=Image.new('RGB',(w*3+8,(h+4)*3),'#888')
    for i,im in enumerate(ims): o.paste(im,((i%3)*(w+4),(i//3)*(h+4)))
    o.save(os.path.join(r,f'sheet{k//9:02d}.png'))
print(len(fs))
