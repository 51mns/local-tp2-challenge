#!/usr/bin/env python3
"""Independent sparse-Laurent root/first-child audit of reduction_common.md.
Imports only the network lane's arithmetic, not reduction_common.py.
"""
import json
from pathlib import Path
import network_exterior_reproducer as l
P=l.ordinary([2,1]);one=l.O;x=l.X;y=l.Y

def add(*ps):
 out={}
 for p in ps:out=l.add(out,p)
 return out
def mul(*ps):
 out=one
 for p in ps:out=l.mul(out,p)
 return out
def rawchildren(raw):
 X,Y,C=raw
 UX=l.sub(l.sub(l.scale(mul(y,X,C),3),mul(x,add(X,C))),Y)
 UY=l.sub(l.sub(l.scale(mul(y,Y,C),3),mul(x,add(Y,C))),X)
 assert max(UX)<max(UY)
 return [(X,C,UX),(Y,C,UY)]
def build(raw):
 X,Y,C=raw;UX,UY=[z[2] for z in rawchildren(raw)]
 E=l.sub(Y,X);G=l.sub(C,Y);t=l.sub(l.scale(mul(y,X),3),x)
 S=l.sub(UX,C);D=l.sub(UY,UX);M=add(l.scale(mul(y,C),3),one,l.neg(x));R=l.sub(mul(t,G),S)
 Q=l.sub(S,G);Pi=mul(X,P,M);V=add(mul(P,X),mul(P,P,C))
 assert D==mul(E,M)
 assert Q==l.sub(mul(l.sub(t,l.ordinary([2])),C),mul(x,X))
 assert Pi==add(mul(P,Q),V)
 return dict(X=X,Y=Y,C=C,E=E,G=G,t=t,S=S,D=D,M=M,R=R,Q=Q,Pi=Pi,V=V)
def W(p,q):
 h,k=l.half(p),l.half(q)
 z=[l.wedge(h,k,n) for n in range(max(len(h),len(k)))]
 while z and not z[-1]:z.pop()
 return z
def defects(p):return l.defects(l.half(p))
def polarization(p,q):
 hp,hq=l.half(p),l.half(q);N=max(len(hp),len(hq))
 ds=defects(add(p,q));dp=defects(p);dq=defects(q)
 return [(ds[n] if n<len(ds) else 0)-(dp[n] if n<len(dp) else 0)-(dq[n] if n<len(dq) else 0) for n in range(N)]
def report(st):
 return dict(rows={k:l.half(st[k]) for k in ['E','G','R','S','D','Q','Pi','M']},links={a+'_lr_'+b:W(st[a],st[b]) for a,b in [('E','G'),('R','G')]},endpoint_links=dict(XP_lr_E=W(mul(st['X'],P),st['E']),YP_lr_G=W(mul(st['Y'],P),st['G']),CP_lr_S=W(mul(st['C'],P),st['S'])),gates=dict(delta_G=defects(st['G']),delta_M=defects(st['M']),proxy_Q_Pi=W(st['Q'],st['Pi'])),target=W(st['S'],st['D']))
def run():
 raw=(one,P,l.ordinary([5,6,2]));root=build(raw);out={'root':report(root),'children':{}}
 for name,newraw in zip(('short','long'),rawchildren(raw)):
  st=build(newraw);out['children'][name]=report(st)
  old=root;F=add(old['S'],old['D']);tp=add(old['t'],l.scale(mul(y,old['E']),3))
  if name=='short':
   assert st['E']==add(old['E'],old['G']) and st['G']==old['S'] and st['R']==old['G']
   assert st['Q']==l.sub(mul(l.sub(old['t'],one),old['S']),old['G'])
   assert st['Q']==add(old['Q'],mul(l.sub(old['t'],l.ordinary([2])),old['S']))
   assert st['Pi']==add(old['Pi'],l.scale(mul(y,old['X'],P,old['S']),3))
   assert st['V']==add(old['V'],mul(P,P,old['S']))
  else:
   assert st['E']==old['G'] and st['G']==F and st['R']==add(old['E'],old['G'])
   assert st['Q']==l.sub(mul(l.sub(tp,one),F),add(old['E'],old['G']))
   assert st['Q']==add(old['Q'],mul(l.sub(old['t'],l.ordinary([2])),F),mul(old['E'],add(old['M'],l.neg(one),l.scale(mul(y,F),3))))
   assert st['Pi']==add(old['Pi'],mul(P,old['D']),l.scale(mul(y,old['Y'],P,F),3))
   assert st['V']==add(old['V'],mul(P,old['E']),mul(P,P,F))
  assert st['M']==add(old['M'],l.scale(mul(y,st['G']),3))
  hq=l.half(st['Q']);hPi=l.half(st['Pi']);hV=l.half(st['V'])
  for n in range(len(hq)):
   assert l.wedge(hq,hPi,n)==l.defects(hq)[n]+l.wedge(hq,hV,n)
  dg=defects(st['G'])
  if name=='short':
   f=mul(old['t'],old['G']);h=old['R'];pol=polarization(f,h)
   df,dh=defects(f),defects(h)
   for n,v in enumerate(dg):assert v==(df[n] if n<len(df) else 0)+(dh[n] if n<len(dh) else 0)-pol[n]
  else:
   f,h=old['S'],old['D'];pol=polarization(f,h);df,dh=defects(f),defects(h)
   for n,v in enumerate(dg):assert v==(df[n] if n<len(df) else 0)+(dh[n] if n<len(dh) else 0)+pol[n]
  dm=defects(st['M']);h=mul(y,st['G']);pol=polarization(old['M'],h);df,dh=defects(old['M']),defects(h)
  for n,v in enumerate(dm):assert v==(df[n] if n<len(df) else 0)+9*(dh[n] if n<len(dh) else 0)+3*pol[n]
 assert out['root']['target']==[272,352,160,24]
 expected=dict(short=dict(delta_G=[192,256,112,16],delta_M=[11864,19240,9480,2052,144],proxy_Q_Pi=[2004,5772,3448,1008,96]),long=dict(delta_G=[3400,5880,2856,544,36],delta_M=[180320,315160,188820,53568,6624,324],proxy_Q_Pi=[1221944,2423832,1730408,638012,121452,10764,324]))
 for k,v in expected.items():assert out['children'][k]['gates']==v
 out['audit_scope']='Independent root/first-child exact audit and manuscript algebra audit; regular cone/proxy closure remains open.'
 out['imports']=['network_exterior_reproducer.py: independent sparse Laurent arithmetic; no reduction or parent arithmetic import']
 Path(__file__).with_name('network_reduction_audit_results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':run()
