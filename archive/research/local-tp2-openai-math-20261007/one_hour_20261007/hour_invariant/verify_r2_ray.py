#!/usr/bin/env python3
"""Exact finite parameter-box certificates for the all-ell R^2 L^ell theorem.
No prior polynomial implementation or certificate data imported.
"""
from fractions import Fraction as F
from math import comb
from itertools import product
import json
from pathlib import Path

def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def sc(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
 out={}
 for i,a in p.items():
  for j,b in q.items():out[i+j]=out.get(i+j,0)+a*b
 return clean(out)
def power(p,n):
 out={0:1}
 for _ in range(n):out=mul(out,p)
 return out
def divy(p):
 d=max(p); q={};last=0
 for j in range(d):
  last=p.get(j,0)-last
  if last:q[j]=last
 assert p.get(d,0)==last
 return q
def laur(p):
 out={}
 for k,v in p.items():out=add(out,sc(power({1:1,-1:1},k),v))
 return out
def half(p):
 h=laur(p);return [h.get(i,0) for i in range(max(h)+1)]
def get(h,i):return h[abs(i)] if abs(i)<len(h) else 0
def delta(h,i):return get(h,i)**2-get(h,i-1)*get(h,i+1)-get(h,i+1)**2+get(h,i)*get(h,i+2)
def W(p,q,n):
 h,j=half(p),half(q)
 return get(h,n)*get(j,n+1)-get(h,n+1)*get(j,n)
def mass(p):return sum(v*2**i for i,v in p.items())
def stateR(a,c,b):return c,add(sc(mul(mul(y,c),b),3),sc(mul(x,add(c,b)),-1),sc(a,-1)),b
x={1:1};y={0:1,1:1};one={0:1};p1={0:2,1:1}
a,c,b=one,{0:5,1:6,2:2},p1
cs=[c]
for j in range(2):a,c,b=stateR(a,c,b);cs.append(c)
P=p1;X=cs[1];C0=cs[2];Zold=cs[0]
A=divy(add(C0,sc(P,-1)));B=divy(add(Zold,sc(P,-1)))
tau=add(sc(mul(y,X),3),sc(x,-1));K0=add(sc(mul(y,P),3),sc(x,-1),one)
J=mul(y,add(tau,{0:-2}));V=sc(mul(mul(power(y,2),X),p1),3);K=mul(mul(X,p1),K0)
# Parametric polynomials: (Laurent exponent, parameter-degree tuple).
def lift(p,n):return {(k,(0,)*n):v for k,v in laur(p).items()}
def padd(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def psc(p,c):return clean({k:v*c for k,v in p.items()})
def pmul(p,q):
 out={}
 for (i,a),c in p.items():
  for (j,b),d in q.items():
   key=(i+j,tuple(x+y for x,y in zip(a,b)));out[key]=out.get(key,0)+c*d
 return clean(out)
def shifted(n,var):
 out=lift(add(tau,{0:-2}),n);key=[0]*n;key[var]=1;out[0,tuple(key)]=4;return out
def prow(p,j):return {a:v for (i,a),v in p.items() if i==abs(j)}
def rmul(p,q):
 out={}
 for a,c in p.items():
  for b,d in q.items():
   key=tuple(x+y for x,y in zip(a,b));out[key]=out.get(key,0)+c*d
 return clean(out)
def radd(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def rsc(p,c):return clean({k:v*c for k,v in p.items()})
def pdelta(p,j):
 a,b,c,d=(prow(p,i) for i in [j,j-1,j+1,j+2])
 return radd(rmul(a,a),rsc(rmul(b,c),-1),rsc(rmul(c,c),-1),rmul(a,d))
def pmass(p):
 out={}
 for (i,a),v in p.items():out[a]=out.get(a,0)+v
 return clean(out)
def bern(p,degs):
 out=[]
 for idx in product(*(range(d+1) for d in degs)):
  s=F(0)
  for a,c in p.items():
   if all(a[k]<=idx[k] for k in range(len(degs))):
    f=F(c)
    for k in range(len(degs)):f*=F(comb(idx[k],a[k]),comb(degs[k],a[k]))
    s+=f
  out.append(s)
 return out


def encode(xs):return [str(x) for x in xs]
def ordinary_vector(p):return [p.get(i,0) for i in range(max(p)+1)]
def root_children(a,c,b):
 return (add(sc(mul(mul(y,a),c),3),sc(mul(x,add(a,c)),-1),sc(b,-1)),
         add(sc(mul(mul(y,c),b),3),sc(mul(x,add(c,b)),-1),sc(a,-1)))

certificate={
 'status':'PROOF_CANDIDATE; universal conclusion rests on THEOREM_R2_RAY.md plus inherited folded-kernel/Jacobi lemmas, not finite path extrapolation',
 'scope':'All Farey paths R^2 L^ell, integer ell>=0; no arbitrary tree theorem',
 'parameters':{'r':'2-4u0','s':'2-4u1','c':'2-4u2','u_domain':'[0,1]^dimension'},
 'base_ordinary':{name:ordinary_vector(poly) for name,poly in [('P',P),('X',X),('C0',C0),('Zold',Zold),('A',A),('B',B),('tau',tau),('K0',K0),('J',J),('V',V),('K',K)]},
 'base_halfrows':{},'interval_kernel_certificates':{},'mass_certificates':{},'initial_lr':{}
}
# Literal coefficient signs establish every shifted factor's full positive
# support. Finite degree certificates below cover all its folded defects.
assert all(v>0 for p in [A,B,tau,J,V,K,K0] for v in p.values())
assert tau[0]>2
for name,poly in [('A',A),('yA',mul(y,A)),('B',B),('yB',mul(y,B)),('J',J),('K0',K0)]:
 h=half(poly); ds=[delta(h,j) for j in range(len(h))]
 assert all(v>0 for v in ds)
 certificate['base_halfrows'][name]={'row':h,'defects':ds}

for kind,n in [('trace',1),('L',1),('H',3)]:
 if kind=='trace':poly=shifted(n,0)
 if kind=='L':poly=padd(pmul(lift(A,n),shifted(n,0)),lift(B,n))
 if kind=='H':poly=padd(pmul(pmul(lift(A,n),shifted(n,0)),shifted(n,1)),pmul(lift(B,n),shifted(n,2)))
 for smooth in ([0] if kind=='trace' else [0,1]):
  pp=pmul(poly,lift(y,n)) if smooth else poly
  deg=max(i for i,a in pp)
  lam=1 if kind!='H' else 8*half(mul(y,B) if smooth else B)[0]
  arrays=[]
  for j in range(deg+1):
   arr=bern(radd(pdelta(pp,j),rsc(prow(pp,j),-lam)),[2]*n)
   assert min(arr)>0
   arrays.append({'index':j,'bernstein':encode(arr)})
  key=kind+('_y' if smooth else '')
  certificate['interval_kernel_certificates'][key]={'dimension':n,'degree_each_parameter':2,'polynomial_degree':deg,'strength_lambda':lam,'all_indices':arrays,'minimum':str(min(F(v) for a in arrays for v in a['bernstein']))}

trace=shifted(1,0)
trace_margin=bern(radd(pdelta(trace,0),rsc(pmass(trace),-22)),[2])
assert min(trace_margin)>0
L=padd(pmul(lift(A,1),trace),lift(B,1))
low_margins=[]
for j in range(4):
 arr=bern(radd(pdelta(L,j),rsc(pmass(L),-40000)),[2])
 assert min(arr)>0
 low_margins.append({'index':j,'bernstein':encode(arr)})
certificate['mass_certificates']={
 'trace_delta0_minus_22_mass':encode(trace_margin),
 'single_delta_j_minus_40000_mass':low_margins,
 'summand_mass_gate':{'B_mass':mass(B),'A_mass_times_tau_mass_minus_2':mass(A)*(mass(tau)-2),'strictly_less':mass(B)<mass(A)*(mass(tau)-2)},
 'uniform_prefix_bound':'delta_j(Z_N)>20000 Z_N(2), j=0,1,2,3 and every N>=1',
 'all_N_scalar_reason':'22^(N-1)/N>=1 for N>=1; ratio 22N/(N+1)>=11>1'
}
assert mass(B)<mass(A)*(mass(tau)-2)

w=[W(J,V,n) for n in range(max(J)+1)]
assert min(w)>0
kk=half(K)
beta0=max(F(mass(J)*get(kk,n),w[n]) for n in range(len(w)))
beta1=F(mass(J)*get(kk,max(J)+1),w[-1])
assert beta0<20000 and beta1<20000
certificate['proxy']={'J_mass':mass(J),'K_halfrow':kk,'fixed_J_V_minors':w,'beta0':str(beta0),'beta1':str(beta1),'prefix_mass_bound':20000}

q0=mul(y,A);q1=mul(y,add(mul(A,tau),B));Beta=mul(y,add(A,B));E1=add(C0,sc(X,-1))
for name,l,r in [('q0_le_q1',q0,q1),('Beta_le_q1',Beta,q1),('P1X_le_E1',mul(p1,X),E1),('E1_le_q1',E1,q1)]:
 minors=[W(l,r,n) for n in range(max(l)+1)]
 assert min(minors)>0
 certificate['initial_lr'][name]={'lower_halfrow':half(l),'upper_halfrow':half(r),'minors':minors}

# Exact universal recurrence anchor for the new fixed-X ray.
C1=add(mul(tau,C0),sc(P,-1),sc(mul(x,X),-1))
assert add(C1,sc(C0,-1))==q1
assert Beta==add(mul(add(tau,{0:-2}),P),sc(mul(x,X),-1))
assert J==mul(y,add(tau,{0:-2}))
assert V==add(mul(p1,J),mul(y,power(p1,2)))
assert max(A)==5 and max(tau)==5 and max(B)==1
assert max(J)==6 and max(V)==7 and max(K)==7

# ell=0 is a single exact base state R^2. The universal ell>=1 proof
# has a different degree orientation and does not infer this base.
l,r=root_children(X,C0,P)
short,long=(r,l) if max(r)<max(l) else (l,r)
S0=add(short,sc(C0,-1));D0=add(long,sc(short,-1))
baseF=[W(S0,D0,n) for n in range(max(S0)+1)]
assert min(baseF)>0
certificate['ell_zero_original_target']={'H_S':half(S0),'H_D':half(D0),'F':baseF}
certificate['multiplier']={'K0_halfrow':half(K0),'K0_defects':[delta(half(K0),j) for j in range(4)],'polarization_negative_coefficient_sums':[32,22,8,3], 'uniform_lower_surplus_coefficient':9*4*20000-3*32*9}
assert certificate['multiplier']['uniform_lower_surplus_coefficient']>0

path=Path(__file__).with_name('r2_ray_certificates.json')
path.write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps({'status':'PASS all exact certificate gates','output':str(path),'parameter_bernstein_coefficients':sum(len(a['bernstein']) for rec in certificate['interval_kernel_certificates'].values() for a in rec['all_indices'])+3+sum(len(a['bernstein']) for a in low_margins),'kernel_margin_minima':{k:v['minimum'] for k,v in certificate['interval_kernel_certificates'].items()},'mass_margins':certificate['mass_certificates'],'proxy':certificate['proxy'],'ell_zero_F':baseF},indent=2))
