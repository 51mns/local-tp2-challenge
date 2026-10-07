"""Independent Laurent audit of the full all-right theorem certificates."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}


def scale(p,c):return {k:v*c for k,v in p.items() if v*c}


def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            k=tuple(x+y for x,y in zip(i,j))
            out[k]=out.get(k,F(0))+a*b
    return {k:v for k,v in out.items() if v}


def row(p,n):return {k[1:]:v for k,v in p.items() if k[0]==n}


def mass(p):
    out={}
    for k,v in p.items():out[k[1:]]=out.get(k[1:],F(0))+v
    return {k:v for k,v in out.items() if v}


def delta(p,n):
    d=lambda j:add(mul(row(p,j),row(p,j)),scale(mul(row(p,j-1),row(p,j+1)),-1))
    return add(d(n),scale(d(n+1),-1))


def checkcert(poly,cert,name):
    expected={tuple(map(int,k.split(','))):F(v) for k,v in cert['power_coefficients'].items()}
    assert poly==expected,(name,'direct Laurent polynomial')
    degrees=tuple(cert['degrees'])
    bc={tuple(map(int,k.split(','))):F(v) for k,v in cert['bernstein_coefficients'].items()}
    assert set(bc)==set(product(*(range(d+1) for d in degrees)))
    reconstructed={}
    for indices,value in bc.items():
        for offsets in product(*(range(d-i+1) for d,i in zip(degrees,indices))):
            val=value
            for d,i,a in zip(degrees,indices,offsets):val*=comb(d,i)*comb(d-i,a)*(-1)**a
            key=tuple(i+a for i,a in zip(indices,offsets))
            reconstructed[key]=reconstructed.get(key,F(0))+val
    assert {k:v for k,v in reconstructed.items() if v}==poly,(name,'Bernstein reconstruction')
    minimum=min(bc.values())
    assert minimum>0 and minimum==F(cert['strict_lower_bound'])
    return len(bc),str(minimum)


def main():
    one={(0,)*5:F(1)}
    x={(-1,0,0,0,0):F(1),(1,0,0,0,0):F(1)}
    u,v,w=[{tuple(1 if j==i else 0 for j in range(5)):F(1)} for i in range(1,4)]
    y=add(x,one);P=add(x,scale(one,2))
    t=add(scale(mul(x,x),3),scale(x,8),scale(one,6))
    e=mul(y,P);A=add(t,scale(one,-2));B=scale(mul(y,mul(P,P)),3)
    Q=add(mul(t,t),scale(mul(u,t),2),scale(v,-4));G=add(t,w)
    certificates=json.loads(Path('resumed_extension_right_certificates.json').read_text())
    count=0;minima={}
    growth=add(delta(Q,0),scale(mass(Q),-4))
    n,m=checkcert(growth,certificates['quartic_growth'],'quartic growth');count+=n;minima['quartic_growth']=m
    for name,R in [('quadratic_in_t',Q),('linear_in_t',G)]:
        lower=mul(mul(A,e),R);upper=mul(mul(B,e),R)
        minima[name]=[]
        for n,hK in enumerate([20,15,6,1]):
            minor=add(mul(row(lower,n),row(upper,n+1)),scale(mul(row(lower,n+1),row(upper,n)),-1))
            margin=add(minor,scale(mass(R),-384*hK))
            amount,minimum=checkcert(margin,certificates[name][n],(name,n))
            count+=amount;minima[name].append(minimum)

    # Fixed pair and both first-sandwich comparisons, computed directly.
    h=lambda p:[p.get((n,0,0,0,0),F(0)) for n in range(max(k[0] for k in p)+1)]
    ae=mul(A,e);be=mul(B,e)
    assert h(ae)==[94,79,46,17,3] and h(be)==[396,339,210,90,24,3]
    pair=lambda aa,bb,n:bb.get((n+1,0,0,0,0),0)*aa.get((n,0,0,0,0),0)-bb.get((n,0,0,0,0),0)*aa.get((n+1,0,0,0,0),0)
    assert [pair(ae,be,n) for n in range(5)]==[582,996,570,138,9]
    E1=mul(y,add(scale(P,2),scale(one,-1)))
    assert [pair(mul(P,P),E1,n) for n in range(3)]==[2,3,0]
    assert [pair(mul(P,P),e,n) for n in range(3)]==[2,1,0]

    # Independent symbolic verification of the multiplier's parameter formulas.
    c=add(scale(one,4),scale(u,4));Qc=add(scale(mul(x,x),3),scale(x,8),c)
    cpoly=lambda p:row(p,0)
    expectedQ=[add(mul(c,c),scale(c,15),scale(one,-74)),add(scale(one,37),scale(c,-3)),scale(one,9)]
    assert [delta(Qc,n) for n in range(3)]==[cpoly(p) for p in expectedQ]
    initial=mul(mul(y,y),Qc)
    expectedInitial=[add(scale(mul(c,c),4),scale(c,85),scale(one,-128)),
                     add(scale(c,17),scale(one,503)),
                     add(mul(c,c),scale(c,37),scale(one,158)),
                     add(scale(one,94),scale(c,-3)),scale(one,9)]
    assert [delta(initial,n) for n in range(5)]==[cpoly(p) for p in expectedInitial]
    assert add(scale(delta(initial,1),3),scale(mass(initial),-1))==cpoly(add(scale(c,42),scale(one,1257)))
    Gc=add(one,scale(initial,3))
    assert delta(Gc,0)==add(scale(delta(initial,0),9),scale(row(initial,0),6),scale(row(initial,2),3),{(0,)*4:F(1)})
    assert delta(Gc,1)==add(scale(delta(initial,1),9),scale(row(initial,2),-3))
    for n in range(2,5):assert delta(Gc,n)==scale(delta(initial,n),9)
    base=mul(P,add(one,scale(mul(y,y),3)))
    assert h(base)==[32,25,12,3]
    assert [delta(base,n)[(0,)*4] for n in range(4)]==[158,172,60,9]

    # Fresh original recurrence checks: orientation, formula matching, root base.
    aa=one;cc=add(scale(mul(x,x),2),scale(x,6),scale(one,5));bb=P
    us=[one,t];prefix=one
    for j in range(1,6):us.append(add(mul(t,us[-1]),scale(us[-2],-1)))
    child=lambda a,c,b:add(scale(mul(mul(y,a),c),3),scale(mul(x,add(a,c)),-1),scale(b,-1))
    checked_states=0
    for k in range(5):
        L=child(aa,cc,bb);R=child(bb,cc,aa)
        low,high=(L,R) if max(j[0] for j in L)<max(j[0] for j in R) else (R,L)
        S=add(low,scale(cc,-1));D=add(high,scale(low,-1))
        assert cc==add(one,scale(mul(e,prefix),2))
        if k==0:
            assert [pair(S,D,n) for n in range(4)]==[272,352,160,24]
        else:
            prevprefix=add(prefix,scale(us[k],-1))
            E=mul(y,add(scale(mul(P,prevprefix),2),scale(one,-1)))
            M=scale(mul(P,add(one,scale(mul(mul(y,y),prefix),3))),2)
            assert S==scale(mul(e,us[k+1]),2) and D==mul(E,M)
            assert max(j[0] for j in low)==2*k+4 and max(j[0] for j in high)==4*k+3
        checked_states+=1
        aa,cc=cc,R
        prefix=add(prefix,us[k+1])
    print(json.dumps({'parameter_margin_polynomials_verified':9,
                      'Bernstein_coefficients_verified':count,
                      'fixed_pair_and_first_sandwich_arrays':'verified',
                      'multiplier_polynomial_identities':'verified independently',
                      'original_right_states_reconstructed':checked_states,
                      'exact_minima':minima},indent=2))


if __name__=='__main__':main()
