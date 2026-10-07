"""Independent exact reweight audit for exponential pure-left strength.

Uses only the auditor's previously independent direct-Laurent primitives,
not the author's symbolic, Fourier, Bernstein, or residue modules.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from mixed_kernel_pureleft_independent import (
    add, bernstein, constant, defect, monomial, mul, row, scale,
)


def main():
    x=add(monomial(0),monomial(0,-1))
    u,v,w,z0,t=[monomial(i) for i in range(1,6)]
    x2=mul(x,x); y=add(x,constant(1)); y2=mul(y,y)
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
    source_path=Path('mixed_kernel_sharp_strength_certificates.json')
    source=json.loads(source_path.read_text())
    assert source['quartic']['strength']==16
    assert set(source['residues'])==set(residues)
    cases={'quartic':(scale(quartic,16),16,source['quartic']['certificates'],True)}
    for name,residue in residues.items():
        degree=max(k[0] for k in residue)
        item=source['residues'][name]
        assert item['degree']==degree
        assert item['y2_prefix']['strength']==2**degree
        assert item['prefix']['strength']==2**(degree-1)
        cases[name+':y2_prefix']=(scale(mul(y2,residue),2**degree),2**degree,
                                  item['y2_prefix']['certificates'],True)
        cases[name+':prefix']=(scale(residue,2**degree),2**(degree-1),
                               item['prefix']['certificates'],False)
    results={}; checked=0; zeros=[]
    for name,(poly,strength,certs,terminal_zero) in cases.items():
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
            if terminal_zero and n==degree:
                assert lower==0 and not margin
                zeros.append([name,n])
            else:
                assert lower>0,(name,n,lower)
            bounds.append(str(lower));checked+=1
        results[name]={'strength':strength,'lower_bounds':bounds,'all_arrays_match':True}
    assert len(zeros)==9
    assert results['quartic']['lower_bounds']==['10977','16328','13120','2944','0']
    # The omitted m=1 is an exact initial case, not an index scan.
    P1=scale(mul(y2,add(x,constant(2))),2)
    T1=scale(add(x,constant(2)),2)
    initial={}
    for name,poly,strength in [('P1',P1,2),('T1',T1,1)]:
        degree=max(k[0] for k in poly); margins=[]
        for n in range(degree+1):
            difference=add(defect(poly,n),scale(row(poly,n),-strength))
            value=difference.get((0,)*6,F(0))
            assert difference in ({}, {(0,)*6:value})
            assert value>=0;margins.append(str(value))
        initial[name]={'strength':strength,'margins':margins}
    result={'status':'PASS','method':'independent direct-Laurent reconstruction with exact rational Bernstein reweighting',
            'certificate_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
            'verified_blocks':len(cases),'verified_strength_arrays':checked,
            'identically_zero_terminal_margins':zeros,'initial_case_margins':initial,'blocks':results}
    Path('mixed_kernel_sharp_strength_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('blocks','identically_zero_terminal_margins')},indent=2))

if __name__=='__main__':main()
