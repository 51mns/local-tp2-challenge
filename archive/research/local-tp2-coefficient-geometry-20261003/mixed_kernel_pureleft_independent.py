"""Independent exact Laurent audit of pure-left strength certificates.

No imports from the author's symbolic, Fourier, or Bernstein modules.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

DIM=6

def constant(c):
    return {(0,)*DIM:F(c)} if c else {}

def monomial(i, exponent=1):
    key=[0]*DIM
    key[i]=exponent
    return {tuple(key):F(1)}

def add(*polys):
    out={}
    for poly in polys:
        for key,value in poly.items():
            out[key]=out.get(key,F(0))+value
    return {k:v for k,v in out.items() if v}

def scale(poly,c):
    return {k:c*v for k,v in poly.items() if c*v}

def mul(a,b):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():
            key=tuple(i+j for i,j in zip(ka,kb))
            out[key]=out.get(key,F(0))+va*vb
    return {k:v for k,v in out.items() if v}

def row(poly,n):
    return {(0,)+k[1:]:v for k,v in poly.items() if k[0]==n}

def defect(poly,n):
    h=lambda i:row(poly,abs(i))
    return add(mul(h(n),h(n)),scale(mul(h(n-1),h(n+1)),-1),
               scale(mul(h(n+1),h(n+1)),-1),mul(h(n),h(n+2)))

def bernstein(poly):
    degrees=[max((key[j] for key in poly),default=0) for j in range(1,DIM)]
    coeffs={}
    for indices in product(*(range(d+1) for d in degrees)):
        value=F(0)
        for key,coefficient in poly.items():
            if all(key[j+1]<=indices[j] for j in range(DIM-1)):
                for j in range(DIM-1):
                    coefficient*=F(comb(indices[j],key[j+1]),comb(degrees[j],key[j+1]))
                value+=coefficient
        coeffs[','.join(map(str,indices))]=str(value)
    return degrees,coeffs

def main():
    x=add(monomial(0),monomial(0,-1))
    u,v,w,z0,t=[monomial(i) for i in range(1,DIM)]
    x2=mul(x,x)
    y=add(x,constant(1))
    y2=mul(y,y)
    central=add(x,constant(F(3,2)))
    def pair(a,b):
        return add(x2,mul(add(constant(3),a),x),constant(F(5,4)),scale(a,F(5,2)),b)
    quartic=mul(pair(u,v),pair(w,z0))
    middle=add(x,constant(F(3,2)),scale(w,F(1,2)))
    fe=add(x2,scale(x,3),constant(2),scale(u,F(1,4)))
    fo=add(x2,scale(x,3),constant(F(7,4)),scale(u,F(1,2)))
    inner=mul(add(x,constant(1),scale(v,F(1,2))),add(x,constant(F(3,2)),w))
    general=pair(v,z0)
    residues={
        'n_mod8_0_pull_quartic':quartic,
        'n_mod8_1_pull_quartic':mul(quartic,add(x,constant(F(3,2)),scale(t,F(1,2)))),
        'n_mod8_2':mul(central,middle),
        'n_mod8_3':mul(central,inner),
        'n_mod8_4':mul(fe,inner),
        'n_mod8_5':mul(mul(fe,middle),general),
        'n_mod8_6':mul(mul(mul(central,fo),middle),general),
        'n_mod8_7':mul(central,fo),
    }
    certificate_path=Path('mixed_kernel_pureleft_certificates.json')
    source=json.loads(certificate_path.read_text())
    cases={'scaled_quartic_one_strong':(scale(quartic,16),1,source['scaled_quartic_one_strong'])}
    for name,residue in residues.items():
        degree=max(k[0] for k in residue)
        assert source[name]['residue_degree']==degree
        assert source[name]['strength']==4
        cases[name]=(scale(mul(y2,residue),2**degree),4,source[name]['certificates'])
    assert set(source)==set(cases)
    centers_path=Path('mixed_kernel_pureleft_centers_certificates.json')
    centers_source=json.loads(centers_path.read_text())
    assert set(centers_source)==set(residues)
    for name,residue in residues.items():
        degree=max(k[0] for k in residue)
        assert centers_source[name]['residue_degree']==degree
        assert centers_source[name]['strength']==3
        cases['centers:'+name]=(scale(mul(y,residue),2**degree),3,
                                centers_source[name]['certificates'])
    results={}
    checked=0
    zero_margins=[]
    for name,(poly,strength,certs) in cases.items():
        degree=max(k[0] for k in poly)
        assert len(certs)==degree+1
        bounds=[]
        for n in range(degree+1):
            h=row(poly,n)
            assert h==row(poly,-n)
            _,row_coefficients=bernstein(h)
            assert min(map(F,row_coefficients.values()))>0
            margin=add(defect(poly,n),scale(h,-strength))
            degrees,coefficients=bernstein(margin)
            lower=min(map(F,coefficients.values()))
            expected=certs[n]
            assert expected['index']==n
            assert expected['degrees']==degrees
            assert expected['power_coefficients']=={','.join(map(str,k[1:])):str(v) for k,v in margin.items()}
            assert expected['bernstein_coefficients']==coefficients
            assert F(expected['lower_bound'])==lower
            assert lower>=0
            if lower==0:
                zero_margins.append([name,n])
                assert not margin, (name,n,'zero bound but nonzero polynomial')
            bounds.append(str(lower))
            checked+=1
        results[name]={'strength':strength,'lower_bounds':bounds,'all_arrays_match':True}
    assert zero_margins==[['n_mod8_2',4]]
    # Independent polynomial checks of the low-index perturbation identities.
    # Here the six exponent positions represent h0,...,h4,c algebraically.
    hh=[monomial(i) for i in range(5)]
    cc=monomial(5)
    def low_defects(h):
        return [add(mul(h[0],h[0]),scale(mul(h[1],h[1]),-2),mul(h[0],h[2])),
                add(mul(h[1],h[1]),scale(mul(h[0],h[2]),-1),
                    scale(mul(h[2],h[2]),-1),mul(h[1],h[3])),
                add(mul(h[2],h[2]),scale(mul(h[1],h[3]),-1),
                    scale(mul(h[3],h[3]),-1),mul(h[2],h[4]))]
    dh=low_defects(hh)
    bb=[add(scale(hh[0],3),cc),add(scale(hh[1],3),constant(2))]+[scale(p,3) for p in hh[2:]]
    db=low_defects(bb)
    assert db[0]==add(scale(dh[0],9),scale(mul(cc,add(scale(hh[0],2),hh[2])),3),
                       scale(hh[1],-24),mul(cc,cc),constant(-8))
    assert db[1]==add(scale(dh[1],9),scale(hh[1],12),scale(mul(cc,hh[2]),-3),
                       scale(hh[3],6),constant(4))
    assert db[2]==add(scale(dh[2],9),scale(hh[3],-6))
    gc=[add(hh[0],constant(1))]+hh[1:]
    dg=low_defects(gc)
    assert dg[0]==add(dh[0],scale(hh[0],2),hh[2],constant(1))
    assert dg[1]==add(dh[1],scale(hh[2],-1))
    gy=[add(hh[0],constant(1)),add(hh[1],constant(1))]+hh[2:]
    assert low_defects(gy)[0]==add(dh[0],scale(hh[0],2),hh[2],scale(hh[1],-4),constant(-1))
    initial_cases={
        'm0_one_fifth':(add(scale(x2,3),scale(x,8),constant(8),scale(u,-4)),F(1,5),[F(0),F(57,5),F(42,5)]),
        'm1_three':(add(scale(mul(y2,add(x,constant(2))),6),scale(x,2),constant(1),scale(u,4)),F(3),[F(2),F(514),F(168),F(18)]),
    }
    initial_results={}
    for name,(poly,strength,expected_bounds) in initial_cases.items():
        bounds=[]
        for n in range(max(k[0] for k in poly)+1):
            _,coefficients=bernstein(add(defect(poly,n),scale(row(poly,n),-strength)))
            lower=min(map(F,coefficients.values()))
            assert lower>=0
            bounds.append(lower)
        assert bounds==expected_bounds,(name,bounds)
        initial_results[name]=[str(b) for b in bounds]
    result={'status':'PASS','method':'fresh direct Laurent and rational Bernstein reconstruction',
            'certificate_sha256':hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
            'centers_certificate_sha256':hashlib.sha256(centers_path.read_bytes()).hexdigest(),
            'verified_blocks':len(cases),'verified_strength_arrays':checked,
            'identically_zero_margins':zero_margins,'low_defect_identities_verified':True,
            'initial_case_lower_bounds':initial_results,'blocks':results}
    Path('mixed_kernel_pureleft_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='blocks'},indent=2))

if __name__=='__main__':
    main()
