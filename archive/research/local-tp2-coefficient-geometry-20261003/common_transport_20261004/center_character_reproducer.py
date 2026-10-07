#!/usr/bin/env python3
"""Exact character-shape obstruction. Standard library only; no tree scan."""
import json
from fractions import Fraction as F
from pathlib import Path
from math import comb

def add(p,q):
    out=[0]*max(len(p),len(q))
    for i,c in enumerate(p):out[i]+=c
    for i,c in enumerate(q):out[i]+=c
    while len(out)>1 and not out[-1]:out.pop()
    return out
def scale(p,c):return [c*x for x in p]
def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out
def H(p):
    return [sum(p[j]*comb(j,(j-i)//2)for j in range(i,len(p),2))for i in range(len(p))]
def at(h,n):return h[abs(n)]if abs(n)<len(h)else 0
def defects(h):
    return [at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)for n in range(len(h))]
def chars(h):return [at(h,n)-at(h,n+1)for n in range(len(h))]
def main():
    alpha=[10000,24300,32805]
    C=[1495,57105,32805]
    h=H(C);d=defects(h);beta=[F(v,2*n+1)for n,v in enumerate(alpha)]
    assert chars(h)==alpha
    assert min(C)>0 and min(alpha)>0
    assert all(beta[n]>=beta[n+1]for n in range(len(beta)-1))
    assert all(beta[n]**2>=beta[n-1]*beta[n+1]for n in range(1,len(beta)-1))
    assert d==[182498500,-16566525,1076168025]
    assert d[0]>=2*h[0]
    root=[5,6,2];rh=H(root);ra=chars(rh);rb=[F(v,2*n+1)for n,v in enumerate(ra)]
    assert ra==[3,4,2]
    assert all(rb[n]>=rb[n+1]for n in range(len(rb)-1))
    assert all(rb[n]**2>=rb[n-1]*rb[n+1]for n in range(1,len(rb)-1))
    assert defects(rh)[0]>=2*rh[0]
    result={'classification':'Counterexample to a standalone character-shape implication; not a canonical/Fricke state, not a child-closure counterexample.',
            'polynomial':C,'halfrow':h,'characters':alpha,'dimension_normalized_characters':[str(v)for v in beta],
            'folded_defects':d,'central_2_strength_margin':d[0]-2*h[0],
            'root':{'polynomial':root,'halfrow':rh,'characters':ra,'folded_defects':defects(rh)}}
    Path(__file__).with_name('center_character_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
