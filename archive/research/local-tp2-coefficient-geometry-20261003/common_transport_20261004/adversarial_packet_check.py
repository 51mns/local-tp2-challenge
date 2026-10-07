#!/usr/bin/env python3
"""Independent formal Z[x,a,e,r] register identities and exact witness replay."""
import json,hashlib
from pathlib import Path
from fractions import Fraction
import adversarial_probe as ordinary

ZERO=(0,0,0,0)
def c(n):return {ZERO:n} if n else {}
def var(i):
 m=list(ZERO);m[i]=1;return {tuple(m):1}
def plus(*ps):
 d={}
 for p in ps:
  for m,v in p.items():d[m]=d.get(m,0)+v
 return {m:v for m,v in d.items() if v}
def sc(p,n):return {m:v*n for m,v in p.items() if v*n}
def minus(p,q):return plus(p,sc(q,-1))
def times(*ps):
 d=c(1)
 for p in ps:
  new={}
  for m,u in d.items():
   for n,v in p.items():
    k=tuple(a+b for a,b in zip(m,n));new[k]=new.get(k,0)+u*v
  d={m:v for m,v in new.items() if v}
 return d
x,a,e,r=[var(i) for i in range(4)];one=c(1);y=plus(x,one);beta=sc(times(y,y),3);z=plus(sc(x,2),c(3))
def state(a,e,r):
 X=plus(one,times(y,a));t=plus(z,times(beta,a));k=times(X,minus(sc(X,3),c(2)));g=plus(times(minus(t,c(2)),e),k,r);s=minus(times(t,g),r)
 M=plus(t,one,times(beta,plus(e,g)));d=times(e,M);C=plus(one,times(y,plus(a,e,g)));T=minus(M,one);ca=plus(e,g,s);cb=plus(g,s,d)
 return dict(a=a,e=e,r=r,X=X,t=t,k=k,g=g,s=s,M=M,d=d,C=C,T=T,ca=ca,cb=cb)
def main():
 v=state(a,e,r);g,s,d,T,ca,cb=[v[k] for k in ('g','s','d','T','ca','cb')];fout=plus(s,d);tau=plus(v['t'],times(beta,e))
 vs=state(a,plus(e,g),g);vl=state(plus(a,e),g,plus(e,g));claims={
 'short_T':(vs['T'],plus(T,times(beta,s))),
 'long_T':(vl['T'],plus(T,times(beta,fout))),
 'short_ca':(vs['ca'],plus(e,times(plus(v['t'],one),s))),
 'long_ca':(vl['ca'],minus(times(plus(tau,one),fout),e)),
 'short_retained_s':(vs['s'],minus(times(v['t'],s),g)),
 'long_retained_s':(vl['s'],minus(times(tau,fout),plus(e,g))),
 'short_new_previous':(plus(vs['e'],vs['g']),ca),
 'long_new_previous':(plus(vl['e'],vl['g']),cb),
 'short_new_current':(plus(vs['s'],vs['d']),plus(times(T,ca),e)),
 'long_new_current':(plus(vl['s'],vl['d']),plus(times(e,minus(times(T,T),one)),times(T,ca))),
 'pair_shear':(cb,plus(ca,times(T,e))),
 'ancestry_division':(times(minus(T,c(2)),plus(e,g)),minus(minus(times(v['C'],minus(sc(v['C'],3),c(2))),ca),e))}
 out={'status':'EXACT_SYMBOLIC_IDENTITIES_Z_x_a_e_r','identities':{}}
 for name,(lhs,rhs) in claims.items():
  residual=minus(lhs,rhs);assert not residual,name
  out['identities'][name]={'residual_terms':0,'lhs_terms':len(lhs),'rhs_terms':len(rhs)}
 # The independent-u obstruction is one given exact witness, not a new scan.
 t=[Fraction(41,12),Fraction(1)];b0=[Fraction(5,2),Fraction(1)]
 block=ordinary.mul(b0,ordinary.sub(ordinary.mul(t,ordinary.mul(ordinary.sub(t,[2]),ordinary.sub(t,[2]))),ordinary.add(t,[2])))
 middle=ordinary.mul(b0,ordinary.sub(ordinary.mul(t,ordinary.mul(ordinary.sub(t,[2]),ordinary.sub(t,[2]))),ordinary.sub(t,[2])))
 dv=ordinary.defects(ordinary.H(block))[0];dm=ordinary.defects(ordinary.H(middle))[0]
 assert dv==Fraction(-1939833799,11943936) and dm==Fraction(6959573561,11943936)
 out['independent_u_obstruction']={'central_defect':str(dv),'actual_midpoint_central_defect':str(dm),'classification':'ABSTRACT, NOT CANONICAL OR FRICKE-COMPLETED'}
 return out
if __name__=='__main__':
 out=main();Path(__file__).with_name('adversarial_packet_check_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
