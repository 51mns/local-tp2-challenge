"""Independent audit of actual ray-comparison certificates and original bases.

All polynomial products are direct Laurent products. Certificate producers and
their Fourier-transform routines are not imported.
"""
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


def check_certificate(actual,cert,label):
    recorded={tuple(map(int,k.split(','))):F(v) for k,v in cert['power_coefficients'].items()}
    assert actual==recorded,(label,'Laurent polynomial')
    degrees=tuple(cert['degrees'])
    bc={tuple(map(int,k.split(','))):F(v) for k,v in cert['bernstein_coefficients'].items()}
    assert set(bc)==set(product(*(range(d+1) for d in degrees)))
    expansion={}
    for indices,value in bc.items():
        for offsets in product(*(range(d-i+1) for d,i in zip(degrees,indices))):
            coeff=value
            for d,i,a in zip(degrees,indices,offsets):coeff*=comb(d,i)*comb(d-i,a)*(-1)**a
            key=tuple(i+a for i,a in zip(indices,offsets))
            expansion[key]=expansion.get(key,F(0))+coeff
    expansion={k:v for k,v in expansion.items() if v}
    assert expansion==actual,(label,'Bernstein reconstruction')
    minimum=min(bc.values())
    assert minimum>0 and minimum==F(cert['strict_lower_bound'])
    return len(bc)


def main():
    one={(0,)*6:F(1)}
    x={(-1,0,0,0,0,0):F(1),(1,0,0,0,0,0):F(1)}
    u,v,w,z,t=[{tuple(1 if j==i else 0 for j in range(6)):F(1)} for i in range(1,6)]
    y=add(x,one)
    def pair(a,b):return add(mul(x,x),mul(add(scale(one,3),a),x),scale(one,F(5,4)),scale(a,F(5,2)),b)
    quartic=mul(pair(u,v),pair(w,z))
    central=add(x,scale(one,F(3,2)))
    middle=add(central,scale(w,F(1,2)))
    even=add(mul(x,x),scale(x,3),scale(one,2),scale(u,F(1,4)))
    odd=add(mul(x,x),scale(x,3),scale(one,F(7,4)),scale(u,F(1,2)))
    inner=mul(add(x,one,scale(v,F(1,2))),add(central,w))
    independent=pair(v,z)
    residues={0:quartic,
              1:mul(quartic,add(central,scale(t,F(1,2)))),
              2:mul(central,middle),
              3:mul(central,inner),
              4:mul(even,inner),
              5:mul(mul(even,middle),independent),
              6:mul(mul(mul(central,odd),middle),independent),
              7:mul(central,odd)}
    A=add(one,scale(x,2))
    U2=add(scale(mul(x,x),4),scale(x,12),scale(one,8))
    certificates=json.loads(Path('resumed_comparison_margin_certificates.json').read_text())
    bernstein_count=pair_count=margin_count=0
    thresholds=[F(80),F(160,3),F(40,3)]
    for key,R in residues.items():
        cert=certificates[str(key)]
        d=max(k[0] for k in R)
        assert cert['monic_residue_degree']==d
        e=mul(y,R);lower=mul(A,e);upper=mul(U2,e)
        boost=4 if key in (2,3) else 1
        assert cert['required_quartic_boost']==boost
        assert len(cert['pair_certificates'])==d+3
        minors=[]
        for n,pc in enumerate(cert['pair_certificates']):
            minor=add(mul(row(lower,n),row(upper,n+1)),scale(mul(row(lower,n+1),row(upper,n)),-1))
            minors.append(minor)
            bernstein_count+=check_certificate(minor,pc,('pair',key,n));pair_count+=1
        assert len(cert['margin_certificates'])==3
        for n,mc in enumerate(cert['margin_certificates']):
            margin=add(scale(minors[n],boost*2**d),scale(mass(e),-thresholds[n]))
            bernstein_count+=check_certificate(margin,mc,('margin',key,n));margin_count+=1

    # Independent quartic amplification arithmetic from earlier verified bounds.
    quartic_delta_lower=F(16)**2*F(19633,256)
    quartic_mass_upper=F(16)*(F(4)+F(2)*4+F(19,4))**2
    assert quartic_delta_lower>4*quartic_mass_upper

    # Recompute the ORIGINAL canonical recurrence directly in Laurent form.
    bases=json.loads(Path('resumed_ray_bases.json').read_text())
    aa=one;cc=add(scale(mul(x,x),2),scale(x,6),scale(one,5));bb=add(x,scale(one,2))
    def child(a,c,b):return add(scale(mul(mul(y,a),c),3),scale(mul(x,add(a,c)),-1),scale(b,-1))
    def from_power(coeffs):
        result={};power=one
        for coefficient in coeffs:
            result=add(result,scale(power,coefficient));power=mul(power,x)
        return result
    base_count=0
    for k,record in enumerate(bases['rows']):
        assert record['k']==k and record['path']=='L'*k
        low=child(aa,cc,bb);high=child(bb,cc,aa)
        S=add(low,scale(cc,-1));D=add(high,scale(low,-1))
        assert S==from_power(record['S']) and D==from_power(record['D'])
        ds=max(a[0] for a in S);dd=max(a[0] for a in D)
        hs=[S.get((n,0,0,0,0,0),F(0)) for n in range(ds+1)]
        hd=[D.get((n,0,0,0,0,0),F(0)) for n in range(dd+1)]
        assert hs==record['H_S'] and hd==record['H_D']
        minors=[hs[n]*hd[n+1]-(hs[n+1] if n<ds else 0)*hd[n] for n in range(ds+1)]
        assert minors==record['F'] and all(v>0 for v in minors)
        base_count+=len(minors)
        aa,cc,bb=aa,low,cc
    assert len(bases['rows'])==6 and base_count==bases['minors_verified']==39
    print(json.dumps({'pair_polynomials_verified':pair_count,
                      'margin_polynomials_verified':margin_count,
                      'Bernstein_coefficients_verified':bernstein_count,
                      'quartic_delta_lower':str(quartic_delta_lower),
                      'quartic_mass_upper':str(quartic_mass_upper),
                      'original_base_minors_reconstructed':base_count},indent=2))


if __name__=='__main__':main()
