#!/usr/bin/env python3
"""Independent bounded current MP0 viability probe; exact rational samples only."""
from fractions import Fraction as F
from pathlib import Path
import json
from falsification_verify import add,sub,mul,scale,fourier,at,canonical,defect
HERE=Path(__file__).resolve().parent

def rowx(a):return [at(a,i-1)+at(a,i+1) for i in range(len(a)+1)]
def single(p):
 a=fourier(p);b=rowx(a)
 for l in range(1,len(b)):
  for k in range(l):
   v=at(a,k)*b[l]-at(a,l)*b[k]
   if v<0:return dict(columns=[k,l],character=[k+l-1,l-k-1],value=v)
 return None
def mixed(p,q):
 a,c=fourier(p),fourier(q);b,d=rowx(a),rowx(c);n=max(len(b),len(d))
 for l in range(1,n):
  for k in range(l):
   v=at(a,k)*at(d,l)+at(c,k)*at(b,l)-at(a,l)*at(d,k)-at(c,l)*at(b,k)
   if v<0:return dict(columns=[k,l],character=[k+l-1,l-k-1],value=v)
 return None

def run():
 out=[];parameters=[F(-2),F(-3,2),F(0),F(3,2),F(2)]
 # Diagonal and opposed extremes distinguish the midpoint/variance terms;
 # three off-diagonal half shifts catch signs masked by r=s.
 pairs=[(F(-2),F(-2)),(F(-2),F(2)),(F(2),F(2)),(F(-3,2),F(3,2)),(F(-2),F(0)),(F(0),F(2)),(F(-1,2),F(3,2))]
 for path in ('SS','SL','LS','LL','SSS','SSL','SLL','LSL'):
  st=canonical(path);T=st['T'];c=add(st['e'],st['g'],st['s']);e=st['e'];failure=None;count=0
  for r in parameters:
   pp=sub(T,[r]);count+=1;neg=single(pp)
   if neg:failure=dict(gate='shifted_trace',r=r,negative=neg);break
  for orient,b0,b1 in [('forward',c,e),('reverse',e,c)]:
   if failure:break
   assert len(b1)<len(b0)+len(T)-1
   for mode,fac in [('raw',[1]),('y',[1,1])]:
    for r in parameters:
     p=mul(fac,add(mul(b0,sub(T,[r])),b1));count+=1;neg=single(p)
     if neg:failure=dict(gate='weak_single',orientation=orient,mode=mode,r=r,negative=neg);break
    if failure:break
    for r,s in pairs:
     Lr=add(mul(b0,sub(T,[r])),b1);Ls=add(mul(b0,sub(T,[s])),b1)
     pp=mul(fac,Lr,sub(T,[s]));qq=mul(fac,Ls,sub(T,[r]));count+=1;neg=mixed(pp,qq)
     if neg:failure=dict(gate='sharp_mixed',orientation=orient,mode=mode,r=r,s=s,negative=neg);break
    if failure:break
  out.append(dict(path=path,degree_T=len(T)-1,exact_sample_cases=count,first_failure=failure,complete_P0='not certified by finite rational testing'))
  if failure:
   out[-1]['a']=st['a'];out[-1]['e']=st['e'];out[-1]['r']=st['r'];out[-1]['T']=T;out[-1]['c']=c
   break
 return {'scope':'Current paired MP0 candidate at actual canonical records; all characters checked at prescribed rational points; not a continuous-domain certificate','parameter_shifts':parameters,'parameter_pairs':pairs,'records':out}
if __name__=='__main__':
 result=run();enc=lambda x:str(x) if isinstance(x,F) else x;(HERE/'falsification_packet_results.json').write_text(json.dumps(result,indent=2,default=enc)+'\n');print(json.dumps(result,indent=2,default=enc))
