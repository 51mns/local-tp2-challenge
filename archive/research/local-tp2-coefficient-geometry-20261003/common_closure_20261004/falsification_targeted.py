#!/usr/bin/env python3
"""Focused exact continuation of frozen predicates; imports new probe only."""
import argparse, json
from pathlib import Path
from fractions import Fraction
from falsification_probe import *

def remainder(f,g,n):
    c=lambda i:get(f,i)-get(g,i)
    return (get(g,n)*(get(f,n)-get(f,n+2))+get(g,n-1)*get(f,n+1)
            +c(n-1)*get(g,n+1)+get(g,n+1)*(get(f,n+1)+c(n+1)))
def bound(f,g,n,lam):
    return (defects(f)[n]-lam*get(f,n)-get(f,n)*(3*get(g,n)+get(g,n+2))
            +get(g,n)*(get(g,n)+get(g,n+2)+lam))
def state(path):
    v=build([0],[1],[1]);scalar=([1],[2,1],[5,6,2])
    for ch in path:
        v=dict(children(v))[ch]; scalar=dict(scalar_children(*scalar))[ch]
    assert tuple(v[k] for k in ('X','Y','C'))==scalar
    return v
def frozen_checks(v):
    C=v['C'];lc=C[-1];F=mul(v['t'],v['Y']);G=sub(F,C)
    rows={};witness=[];ratios={}; summary={}
    for sm,lam in [(False,Fraction(lc)),(True,Fraction(lc,2))]:
        p,q,c=[mul(y,w) for w in (F,G,C)] if sm else (F,G,C)
        f,g,h=H(p),H(q),H(c);ds=defects(h);df=defects(f)
        assert min(g)>=0 and all(f[i]>=get(f,i+1)>=0 for i in range(len(f)))
        rem=[remainder(f,g,n) for n in range(len(h))]
        strength=[Fraction(d)-lam*hn for d,hn in zip(ds,h)]
        coarse=[df[n]-lam*get(f,n)-get(f,n)*(3*get(g,n)+get(g,n+2))+get(g,n)*(get(g,n)+get(g,n+2)+lam) for n in range(len(h))]
        assert all(b+r==s for b,r,s in zip(coarse,rem,strength)) and min(rem)>=0
        key='C_smoothed' if sm else 'C_raw'
        margins=[s-Fraction(r,32) for s,r in zip(strength,rem)]
        vals=[(s/Fraction(r),n) for n,(s,r) in enumerate(zip(strength,rem)) if r]
        ratios[key]=min(vals) if vals else None
        summary[key]={'min_margin':frac(min(margins)),'min_ratio':frac(ratios[key][0]) if ratios[key] else None,'ratio_index':ratios[key][1] if ratios[key] else None}
        for n,m in enumerate(margins):
            if m<0:
                witness.append({'predicate':key,'index':n,'margin':frac(m),'strength':frac(lam),
                  'surplus':frac(strength[n]),'R':rem[n],'B':frac(coarse[n]),
                  'C':C,'F':F,'G':G,'rows':{'f':f,'g':g,'c':h},'smooth':sm})
                break
        rows[key]=h
    Z=add(v['a'],v['e'],v['g']);X=v['X'];J=mul(y,sub(v['t'],[2]));M=add(scale(P1,2),scale(mul(y2,Z),3))
    S=mul(y,v['s']);E=mul(y,v['e']);Ggap=mul(y,v['g']);XP=mul(X,P1)
    b=add(mul(sub(v['t'],[2]),sub(v['e'],v['a'])),scale(v['k'],2),v['r']);Q=sub(S,Ggap)
    comps={'T1':(mul(y,b),S,False),'T2':(XP,E,False),'T3':(mul(J,Z),mul(XP,M),True),
           'T5':(Q,mul(XP,M),True),'T7_G_S':(Ggap,S,False)}
    for key,(p,q,strict) in comps.items():
        vals=minors(H(p),H(q)); vals=vals[:len(p)] if strict else vals
        bad=[i for i,d in enumerate(vals) if d<0 or (strict and d==0)]
        if bad: witness.append({'predicate':key,'index':bad[0],'value':vals[bad[0]],'p':p,'q':q,'rows':[H(p),H(q)]})
    for key,p in [('T4_M',M),('T4_Z',Z),('T6_G',Ggap)]:
        vals=defects(H(p));bad=[i for i,d in enumerate(vals) if d<0]
        if bad:witness.append({'predicate':key,'index':bad[0],'value':vals[bad[0]],'p':p,'row':H(p)})
    return witness,summary

def main():
    out={'scope':'Exact focused fixed-endpoint and switch continuation, not a global proof','records':[],'first_failures':{},'rays':{}}
    paths=set()
    for prefix,maxrun in [('',80),('l',80),('ssl',12),('sll',12),('lll',12),('lsl',12),('slsl',12)]:
        tested=[]
        for j in range(maxrun+1):
            path=prefix+'s'*j;v=state(path)
            if len(v['C'])-1>400:break
            bad,summary=frozen_checks(v);paths.add(path);tested.append(path)
            out['records'].append({'path':path,'degree_C':len(v['C'])-1,'summary':summary})
            for w in bad:out['first_failures'].setdefault(w['predicate'],{'path':path,**w})
            # Stop long rays after locating both remainder modes, not merely one.
            found={w['predicate'] for w in bad}
            if prefix in ('','l') and {'C_raw','C_smoothed'}<=found:break
        out['rays'][prefix]={'paths':tested,'last':tested[-1] if tested else None}
    for prefix in ('sl','ls'):
        for n in range(1,9):
            path=prefix*n
            if path in paths:continue
            v=state(path)
            if len(v['C'])-1>400:break
            bad,summary=frozen_checks(v);paths.add(path)
            out['records'].append({'path':path,'degree_C':len(v['C'])-1,'summary':summary})
            for w in bad:out['first_failures'].setdefault(w['predicate'],{'path':path,**w})
    out['nodes']=len(paths)
    # Known original R13 is degree-ordered ls^12.
    v=state('l'+'s'*12); f=H(mul(v['t'],v['Y']));g=H(sub(mul(v['t'],v['Y']),v['C']));c=H(v['C'])
    out['known_R13_crosscheck']={'path':'l'+'s'*12,'index':0,'B_lambda0':bound(f,g,0,0),'R':remainder(f,g,0),'defect':defects(c)[0]}
    assert out['known_R13_crosscheck']['B_lambda0']==-13255405836475262089110874899224563418
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('falsification_targeted_results.json'))
    args=ap.parse_args();d=main();args.output.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps({'nodes':d['nodes'],'rays':{k:v['last'] for k,v in d['rays'].items()},'first_failures':{k:{z:v[z] for z in ('path','index','margin','surplus','R') if z in v} for k,v in d['first_failures'].items()}},indent=2))
