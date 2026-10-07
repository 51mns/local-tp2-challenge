#!/usr/bin/env python3
"""Exact continuum viability certificates for fixed canonical records, not closure."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
from falsification_verify import add,sub,mul,fourier,at,canonical
from falsification_packet_verify import rowx
HERE=Path(__file__).resolve().parent

def selectors(p,q=None):
 a=fourier(p);b=rowx(a)
 if q is None:
  return {(k,l):at(a,k)*at(b,l)-at(a,l)*at(b,k) for l in range(1,len(b)) for k in range(l)}
 c=fourier(q);d=rowx(c);n=max(len(b),len(d))
 return {(k,l):at(a,k)*at(d,l)+at(c,k)*at(b,l)-at(a,l)*at(d,k)-at(c,l)*at(b,k) for l in range(1,n) for k in range(l)}

def interpol(v):return [v[1],(v[2]-v[0])/F(2),(v[2]+v[0])/F(2)-v[1]]
def quad_min(cs):
 c,b,a=cs;points=[F(-2),F(2)]
 if a>0 and -2<=-b/(2*a)<=2:points.append(-b/(2*a))
 vals=[c+b*x+a*x*x for x in points];i=vals.index(min(vals));return vals[i],points[i]
def mono_box(cs,lo,hi):
 # Power coefficients after r=lo+(hi-lo)u.
 return [sum(cs[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,3)) for k in range(3)]
def bern1(cs,lo,hi):
 aa=mono_box(cs,lo,hi)
 return [sum(aa[k]*F(comb(i,k),comb(2,k)) for k in range(i+1)) for i in range(3)]
def bern2(cs,rlo,rhi,slo,shi):
 t=[bern1([cs[i][j] for i in range(3)],rlo,rhi) for j in range(3)]
 return [bern1([t[j][i] for j in range(3)],slo,shi) for i in range(3)]
def certify(cs,box=(F(-2),F(2),F(-2),F(2)),depth=0):
 bb=bern2(cs,*box)
 if min(v for row in bb for v in row)>=0:return True,1,depth
 if depth==3:return False,1,depth
 a,b,c,d=box;midr=(a+b)/2;mids=(c+d)/2
 count=0;deep=depth
 for q in [(a,midr,c,mids),(midr,b,c,mids),(a,midr,mids,d),(midr,b,mids,d)]:
  ok,n,dd=certify(cs,q,depth+1);count+=n;deep=max(deep,dd)
  if not ok:return False,count,deep
 return True,count,deep

def uni_gate(build):
 vals=[selectors(build(r)) for r in (F(-1),F(0),F(1))];keys=set().union(*vals);mn=None;fail=None
 for k in sorted(keys):
  cs=interpol([v.get(k,0) for v in vals]);m,r=quad_min(cs)
  if mn is None or m<mn:mn=m
  if m<0:fail={'columns':k,'r':r,'value':m,'polynomial':cs};break
 # Every half-row entry is affine; endpoint minima certify positive support.
 support=min(v for r in (F(-2),F(2)) for v in fourier(build(r)))
 strict0=min(selectors(build(0))[(n,n+1)] for n in range(len(build(0))))
 return dict(minimum_character_on_interval=mn,support_minimum=support,strict0_minimum=strict0,first_failure=fail)
def mix_gate(b0,b1,T,fac):
 data={}
 for r in (F(-1),F(0),F(1)):
  for s in (F(-1),F(0),F(1)):
   pp=mul(fac,add(mul(b0,sub(T,[r])),b1),sub(T,[s]));qq=mul(fac,add(mul(b0,sub(T,[s])),b1),sub(T,[r]));data[r,s]=selectors(pp,qq)
 keys=set().union(*data.values());fail=None;cnt=0;deep=0
 for k in sorted(keys):
  tmp=[interpol([data[r,s].get(k,0) for r in (F(-1),F(0),F(1))]) for s in (F(-1),F(0),F(1))]
  cs=[interpol([tmp[j][i] for j in range(3)]) for i in range(3)]
  ok,n,d=certify(cs);cnt+=n;deep=max(deep,d)
  if not ok:fail={'columns':k,'biquadratic_coefficients':cs};break
 return dict(all_selectors_certified=fail is None,selectors=len(keys),Bernstein_leaf_boxes=cnt,maximum_subdivision_depth=deep,first_uncertified=fail)

def run():
 out=[]
 for path in ('SS','SL','LS','LL','SSS','SSL','SLL','LSL'):
  st=canonical(path);T=st['T'];c=add(st['e'],st['g'],st['s']);e=st['e'];rec={'path':path,'shifted_trace':uni_gate(lambda r:sub(T,[r])),'orientations':{}}
  for orient,b0,b1 in [('forward',c,e),('reverse',e,c)]:
   rec['orientations'][orient]={}
   for mode,fac in [('raw',[1]),('y',[1,1])]:
    single=uni_gate(lambda r:mul(fac,add(mul(b0,sub(T,[r])),b1)))
    mixed=mix_gate(b0,b1,T,fac)
    rec['orientations'][orient][mode]={'single':single,'sharp_mixed':mixed}
  rec['complete_current_paired_MP0']=all(rec['shifted_trace']['first_failure'] is None and rec['shifted_trace']['support_minimum']>0 and part['single']['first_failure'] is None and part['single']['support_minimum']>0 and part['single']['strict0_minimum']>0 and part['sharp_mixed']['all_selectors_certified'] for o in rec['orientations'].values() for part in o.values())
  out.append(rec)
 return {'scope':'Fixed genuine canonical states only; complete current paired MP0 continuum certificates using exact quadratic minima and exact biquadratic Bernstein positivity. Not BOTH preservation or full P0 membership (stored origins/LR/proxy not certified here).','records':out}
if __name__=='__main__':
 result=run();enc=lambda x:str(x) if isinstance(x,F) else x;(HERE/'falsification_continuum_results.json').write_text(json.dumps(result,indent=2,default=enc)+'\n');print(json.dumps([{'path':r['path'],'current_paired_MP0':r['complete_current_paired_MP0'],'unproved_mixed':[(o,m,p['sharp_mixed']['first_uncertified']) for o,a in r['orientations'].items() for m,p in a.items() if not p['sharp_mixed']['all_selectors_certified']]} for r in result['records']],indent=2,default=enc))
