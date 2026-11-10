# print fractional positions of words matching regex on a page: wordpos.py pdf page regex
import sys,subprocess,re
pdf,pg,pat=sys.argv[1],sys.argv[2],sys.argv[3]
x=subprocess.run(['pdftotext','-f',pg,'-l',pg,'-bbox',pdf,'-'],capture_output=True,text=True).stdout
m=re.search(r'<page width="([\d.]+)" height="([\d.]+)"',x); W,H=float(m.group(1)),float(m.group(2))
for w in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>',x):
    if re.search(pat,w.group(5)): print(w.group(5), 'x %.3f-%.3f y %.3f-%.3f'%(float(w.group(1))/W,float(w.group(3))/W,float(w.group(2))/H,float(w.group(4))/H))
