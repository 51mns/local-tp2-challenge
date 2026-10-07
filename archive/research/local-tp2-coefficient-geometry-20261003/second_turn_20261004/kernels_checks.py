"""Exact scalar tail and Bernstein-weight checks, plus bridge manifest audit.

This is a reproducible checker of the explicit gates and bookkeeping.
It does not replace the mathematical parent-dependency audits or claim
independence of the finite certificate generator. The separate finite
auditor reconstructs the actual margins independently.
"""
from fractions import Fraction
import hashlib
import itertools
import json
from math import comb
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from kernels_certificate import bernstein_weights


def multiply(a,b):
    out={}
    for e,v in a.items():
        for f,w in b.items():
            g=tuple(x+y for x,y in zip(e,f))
            out[g]=out.get(g,0)+v*w
    return out


def bernstein(poly,index):
    total=Fraction(0)
    for powers,value in poly.items():
        weight=Fraction(value)
        for i,p in zip(index,powers):
            weight*=Fraction(comb(i,p) if i>=p else 0,comb(2,p))
        total+=weight
    return total


def exact_ratio(value):
    return dict(numerator=str(value.numerator),denominator=str(value.denominator))


def main():
    bases=[{(0,0,0):1},{(1,0,0):1,(0,1,0):1},
           {(1,1,0):1},{(0,0,1):1}]
    weight_checks=0
    for index in itertools.product(range(3),repeat=3):
        weights,linear=bernstein_weights(*index)
        expected=[8*bernstein(multiply(bases[i],bases[j]),index)
                  for i in range(4) for j in range(i,4)]
        expected_linear=[8*bernstein(b,index) for b in bases]
        assert weights==expected
        assert linear==expected_linear
        weight_checks+=14

    m=410
    sigma=Fraction(59,100)
    c0=Fraction(1,400000000)
    epsH=Fraction(16*(2*m+3),6**(m+1))
    epsL=epsH/3
    EH=c0**3*sigma**(3*m+2)/(16*(m+2)*(m+4))
    EL=c0**2*sigma**(2*m+1)/(4*(m+2))
    ratioH=6*sigma**3*Fraction((m+2)*(m+4)*(2*m+3),(m+3)*(m+5)*(2*m+5))
    ratioL=6*sigma**2*Fraction((m+2)*(2*m+3),(m+3)*(2*m+5))
    gates={'epsH_below_one':epsH<1,
           'EH_at_least_12epsH':EH>=12*epsH,
           'EL_at_least_12epsL':EL>=12*epsL,
           'EH_epsH_ratio_above_one':ratioH>1,
           'EL_epsL_ratio_above_one':ratioL>1,
           'midpoint_strength_dominates_smoothed_mass':
                9*2**(3*m-3)>=4*(7**(m+3)-1)}
    assert all(gates.values())

    manifest=HERE/'kernels_certificate_results.json'
    result=json.loads(manifest.read_text())
    assert result['scope']==[0,409] and result['status']=='PASS'
    expected={(m,s,label) for m in range(410) for s in (False,True)
              for label in ('single','midpoint')}
    actual={(r['m'],r['smooth'],r['label']) for r in result['cases']}
    assert actual==expected and len(actual)==len(result['cases'])
    for r in result['cases']:
        assert r['negative']==r['zero']==0 and int(r['minimum'])>0
        degree=2*r['m']+3+int(r['smooth']) if r['label']=='single' else 3*r['m']+6+int(r['smooth'])
        assert r['degree']==degree
        assert r['margins']==(3 if r['label']=='single' else 27)*(degree+1)
        if r['label']=='single':
            assert Fraction(int(r['lambda_numerator']),r['lambda_denominator'])==3*Fraction(2)**(2*r['m']-3)
        else:
            assert int(r['alpha'])>0 and int(r['reference_central'])>0

    output=dict(status='PASS',tail_start=m,gates=gates,
                exact_ratios={'EH_over_12epsH':exact_ratio(EH/(12*epsH)),
                              'EL_over_12epsL':exact_ratio(EL/(12*epsL)),
                              'consecutive_H':exact_ratio(ratioH),
                              'consecutive_L':exact_ratio(ratioL)},
                bernstein_weight_equalities=weight_checks,
                finite_scope=result['scope'],finite_cases=len(result['cases']),
                finite_integer_margins=sum(r['margins'] for r in result['cases']),
                manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),
                independent_finite_reconstruction='see separate audit generator/results')
    (HERE/'kernels_checks_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['status','tail_start','gates',
                     'bernstein_weight_equalities','finite_scope','finite_cases','finite_integer_margins']},indent=2))


if __name__=='__main__':
    main()
