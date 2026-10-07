#!/usr/bin/env python3
"""Small off-Fricke regular-row test, not a canonical falsification."""
import json,itertools
from pathlib import Path
from falsification_probe import *

def bad(v):
    X=v['X'];Y=v['Y'];E=mul(y,v['e']);G=mul(y,v['g']);R=mul(y,v['r']);S=mul(y,v['s']);Z=add(v['a'],v['e'],v['g']);M=add(scale(P1,2),scale(mul(y2,Z),3));XP=mul(X,P1);Q=sub(S,G)
    failures={}
    for key,p,q,strict in [('E_G',E,G,False),('R_G',R,G,False),('XP_E',XP,E,False),('YP_G',mul(Y,P1),G,False),('Q_XPM',Q,mul(XP,M),True)]:
        vals=minors(H(p),H(q));vals=vals[:len(p)] if strict else vals
        ix=[i for i,d in enumerate(vals) if d<0 or (strict and d==0)]
        if ix:failures[key]={'index':ix[0],'value':vals[ix[0]],'p':p,'q':q}
    for key,p in [('G_fold',G),('M_fold',M)]:
        h=H(p);ds=defects(h);ix=[i for i,d in enumerate(ds) if d<0]
        if min(h)<0 or ix:failures[key]={'index':ix[0] if ix else h.index(min(h)),'value':ds[ix[0]] if ix else min(h),'p':p,'row':h}
    return failures
def main():
    result={'scope':'Frozen finite abstract class dropping Fricke only; no claim about actual states','tested':0,'accepted':0,'first_closure_obstruction':None}
    for ac in range(3):
        for ec in range(2,11):
            for el in range(1,6):
                for rc in range(ac+ec+1):
                    for rl in range(el+1):
                        if rc==rl==0:continue
                        v=build([ac],[ec,el],trim([rc,rl]));result['tested']+=1
                        assert min(sub(v['e'],v['a']))>=0 and min(sub(add(v['a'],v['e']),v['r']))>=0
                        assert min(sub(v['g'],add(v['a'],v['e'],v['r'],[1])))>=0
                        if bad(v):continue
                        result['accepted']+=1
                        residual=sub(mul(v['r'],v['g']),add(mul(sub(v['t'],[2]),mul(v['e'],v['e'])),scale(mul(v['k'],v['e']),2),scale(mul(v['a'],mul(v['X'],v['X'])),3)))
                        for label,nv in children(v):
                            fails=bad(nv)
                            if fails:
                                result['first_closure_obstruction']={'classification':'abstract off-Fricke obstruction; not canonical','a':v['a'],'e':v['e'],'r':v['r'],'Fricke_residual':residual,'move':label,'child_a':nv['a'],'child_e':nv['e'],'child_r':nv['r'],'failed_gates':fails}
                                assert residual!=[0]
                                return result
    result['rational_scope']={'tested':0,'accepted':0,'first_closure_obstruction':None}
    # Frozen narrow perturbation grid: linear a, quadratic e/r.
    for a0,a1 in itertools.product((Fraction(0),Fraction(1,2),Fraction(1)),repeat=2):
        a=trim([a0,a1])
        for e0extra,e1extra,e2 in itertools.product((Fraction(1),Fraction(2)),(Fraction(1,2),Fraction(1)),(Fraction(1,2),Fraction(1))):
            e=[a0+e0extra,a1+e1extra,e2];upper=add(a,e)
            for weights in itertools.product((Fraction(1,4),Fraction(1,2),Fraction(1)),repeat=3):
                r=[u*w for u,w in zip(upper,weights)];v=build(a,e,r);result['rational_scope']['tested']+=1
                assert min(sub(e,a))>=0 and min(sub(upper,r))>=0
                assert min(sub(v['g'],add(a,e,r,[1])))>=0
                if bad(v):continue
                result['rational_scope']['accepted']+=1
                residual=sub(mul(r,v['g']),add(mul(sub(v['t'],[2]),mul(e,e)),scale(mul(v['k'],e),2),scale(mul(a,mul(v['X'],v['X'])),3)))
                for label,nv in children(v):
                    fails=bad(nv)
                    if fails:
                        result['rational_scope']['first_closure_obstruction']={'classification':'abstract off-Fricke obstruction; not canonical','a':a,'e':e,'r':r,'Fricke_residual':residual,'move':label,'child_a':nv['a'],'child_e':nv['e'],'child_r':nv['r'],'failed_gates':fails}
                        assert residual!=[0]
                        return result
    return result
if __name__=='__main__':
    result=main();kwargs={'indent':2,'default':lambda x:frac(x) if isinstance(x,Fraction) else str(x)}
    Path(__file__).with_name('falsification_abstract_results.json').write_text(json.dumps(result,**kwargs)+'\n');print(json.dumps(result,**kwargs))
