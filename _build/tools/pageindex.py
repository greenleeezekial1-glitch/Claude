# Build {pdf_page: printed_label} plus per-page text for a PDF, using footer labels like "10-3".
import subprocess,re,json,sys
pdf,out=sys.argv[1],sys.argv[2]
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
res={}
for i in range(1,n+1):
    t=subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'-layout',pdf,'-'],capture_output=True,text=True).stdout
    lines=[l.strip() for l in t.split('\n') if l.strip()]
    lab=None
    for l in (lines[-3:]+lines[:2])[::-1]:
        m=re.search(r'(?:^|\s)([0-9A-Z]{1,2}-\d{1,3})(?:\s|$)',l)
        if m: lab=m.group(1); break
    res[i]={'label':lab,'text':t}
json.dump(res,open(out,'w'))
print(n, sum(1 for v in res.values() if v['label']))
