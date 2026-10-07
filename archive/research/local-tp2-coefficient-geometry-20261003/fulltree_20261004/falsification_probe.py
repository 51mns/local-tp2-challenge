"""Bounded, exact falsification probes; no claim of an infinite proof.

Directly use symmetric Laurent half rows, cross-checked against the original
ordinary-polynomial recurrence and its binomial coefficient transform.
"""
import hashlib
import itertools
import json
from pathlib import Path
import sys
import time
from fractions import Fraction

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))
from fulltree_oneturn_finite import times, at
import tp2_source as src

sys.set_int_max_str_digits(0)

def linear(*terms):
    n = max(len(a) for c,a in terms)
    ans = [sum(c*at(a,i) for c,a in terms) for i in range(n)]
    while len(ans)>1 and ans[-1]==0:
        ans.pop()
    return ans

def x_times(a):
    return [at(a,i-1)+at(a,i+1) for i in range(len(a)+1)]

def mutation(a,c,b):
    ac = times(a,c)
    ans = linear((3,ac),(3,x_times(ac)),(-1,x_times(a)),(-1,x_times(c)),(-1,b))
    assert min(ans)>0
    return ans

def children(node):
    a,c,b=node
    return mutation(a,c,b), mutation(b,c,a)

ROOT = ([1],[9,6,2],[2,1])

def state(path):
    a,c,b=ROOT
    for side in path:
        if side=='L':
            a,c,b=a,mutation(a,c,b),c
        else:
            a,c,b=c,mutation(b,c,a),b
    return a,c,b

def pair(node):
    left,right=children(node)
    u,v=sorted([left,right],key=len)
    s=linear((1,u),(-1,node[1]))
    d=linear((1,v),(-1,u))
    assert min(s)>0 and min(d)>0
    return s,d

def degree(path):
    a,c,b=0,2,1
    for side in path:
        if side=='L': a,c,b=a,a+c+1,c
        else: a,c,b=c,b+c+1,b
    return max(a+c+1,b+c+1)

def choose_paths():
    paths=[]
    # Pure alternation, its mirror, balanced pairs, and runs around two switches.
    for repeat in [4,5,6,7,8]:
        paths += ['LR'*repeat,'RL'*repeat]
    for repeat in [2,3,4]:
        paths += ['LLRR'*repeat,'RRLL'*repeat]
    for a,b,c in [(1,12,1),(1,25,1),(1,50,1),(1,80,1),
                  (2,10,2),(2,20,2),(3,8,3),(4,6,4),
                  (8,3,8),(12,2,12),(20,1,20),(30,1,30),
                  (2,6,20),(20,6,2),(7,7,7),(10,5,10),(5,12,5)]:
        paths += ['L'*a+'R'*b+'L'*c, 'R'*a+'L'*b+'R'*c]
    return [p for p in dict.fromkeys(paths) if degree(p)<=5000]

def source_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    start=time.monotonic()
    records=src.generate_tree(4)
    for rec in records:
        s,d=pair(state(rec['path']))
        assert s==rec['H_S'] and d==rec['H_D'],rec['path']
        ff=[at(d,n+1)*at(s,n)-at(d,n)*at(s,n+1) for n in range(len(s))]
        assert ff==rec['F']
    print('original recurrence/transform crosscheck: 31 nodes PASS',flush=True)
    minimum=None
    witness=None
    negative=zero=checked=0
    results=[]
    digest=hashlib.sha256()
    for path in choose_paths():
        s,d=pair(state(path))
        local_min=None
        local_n=None
        for n in range(len(s)):
            pos=at(d,n+1)*at(s,n)
            neg=at(d,n)*at(s,n+1)
            f=pos-neg
            digest.update((path+':'+str(n)+':'+str(f)+'\n').encode())
            negative+=f<0
            zero+=f==0
            checked+=1
            # Compare exact unreduced fractions first, avoiding thousands of gcds.
            if local_min is None or f*local_min[1]<local_min[0]*pos:
                local_min=(f,pos); local_n=n
        if minimum is None or local_min[0]*minimum[1]<minimum[0]*local_min[1]:
            minimum=local_min
            witness={'path':path,'n':local_n,'degS':len(s)-1,'degD':len(d)-1}
        results.append({'path':path,'degS':len(s)-1,'degD':len(d)-1,'minimum_n':local_n})
        print(json.dumps({'case':len(results),'path':path,'degD':len(d)-1,'min_n':local_n,'elapsed':round(time.monotonic()-start,2)}),flush=True)
        if negative or zero:
            break
    normalized=Fraction(*minimum)
    payload={
        'status':'NO_COUNTEREXAMPLE_FOUND' if negative==zero==0 else 'COUNTEREXAMPLE',
        'scope':'Bounded exact probes only; not a proof of general Local TP2.',
        'original_crosscheck_nodes':len(records),'paths_tested':len(results),
        'minors_checked':checked,'negative':negative,'zero':zero,
        'normalization':'F_n / (H(D)_(n+1) H(S)_n)',
        'minimum_normalized':{'numerator':str(normalized.numerator),'denominator':str(normalized.denominator)},
        'witness':witness,'margin_sha256':digest.hexdigest(),
        'sources':{str(p.relative_to(PARENT)):source_hash(p) for p in [Path(__file__).resolve(),PARENT/'tp2_source.py',PARENT/'fulltree_oneturn_finite.py']},
        'elapsed_seconds':round(time.monotonic()-start,3),'cases':results}
    (HERE/'falsification_results.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:payload[k] for k in ['status','paths_tested','minors_checked','negative','zero','witness','elapsed_seconds']}),flush=True)

if __name__=='__main__':
    main()
