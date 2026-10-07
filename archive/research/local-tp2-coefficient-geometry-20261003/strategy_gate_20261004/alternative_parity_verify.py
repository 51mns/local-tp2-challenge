"""Exact parity-transport identities and decisive controls, not a depth scan."""
from math import comb
from pathlib import Path
import json


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p


def at(p,j):return p[j] if 0<=j<len(p) else 0

def add(a,b):return trim([at(a,i)+at(b,i) for i in range(max(len(a),len(b)))])

def scale(a,k):return trim([k*c for c in a])

def sub(a,b):return add(a,scale(b,-1))

def mul(a,b):
    p=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):p[i+j]+=c*d
    return trim(p)

def halfrow(p):
    return [sum(p[k]*comb(k,(k-n)//2) for k in range(n,len(p),2)) for n in range(len(p))]


def direct_laurent(p):
    out={};mon={0:1}
    for c in p:
        for k,v in mon.items():out[k]=out.get(k,0)+c*v
        nxt={}
        for k,v in mon.items():
            nxt[k-1]=nxt.get(k-1,0)+v;nxt[k+1]=nxt.get(k+1,0)+v
        mon=nxt
    return [out.get(k,0) for k in range(len(p))]


def mutate(a,c,b):return sub(sub(scale(mul(mul([1,1],a),c),3),mul([0,1],add(a,c))),b)

def divide_y(p):
    q=[];previous=0
    for c in p[:-1]:previous=c-previous;q.append(previous)
    assert previous==p[-1]
    return trim(q)


def K(k):return halfrow([0]*k+[1,1])

def determinant(a,b,n):return at(a,n)*at(b,n+1)-at(a,n+1)*at(b,n)

def audit_pair(short,long):
    f,g=divide_y(short),divide_y(long)
    hs,hl=halfrow(short),halfrow(long)
    assert hs==direct_laurent(short) and hl==direct_laurent(long)
    parts={'even_even':0,'odd_odd':0,'mixed':0};terms=[]
    for a in range(max(len(f),len(g))):
        for b in range(a+1,max(len(f),len(g))):
            source=at(f,a)*at(g,b)-at(f,b)*at(g,a)
            kernel=determinant(K(a),K(b),0)
            key='mixed' if a%2!=b%2 else 'odd_odd' if a%2 else 'even_even'
            parts[key]+=source*kernel
            terms.append({'a':a,'b':b,'source_minor':source,'kernel_minor':kernel,'product':source*kernel,'sector':key})
    assert sum(parts.values())==determinant(hs,hl,0)
    parity_source={}
    for parity in [0,1]:
        inds=list(range(parity,max(len(f),len(g)),2))
        parity_source[str(parity)]=[{'a':a,'b':b,'minor':at(f,a)*at(g,b)-at(f,b)*at(g,a)} for ia,a in enumerate(inds) for b in inds[ia+1:]]
    return {'f':f,'g':g,'H_short':hs,'H_long':hl,'central_target':determinant(hs,hl,0),'central_parts':parts,'central_terms':terms,'parity_source_minors':parity_source}


def main():
    A,B,C=[1],[2,1],[5,6,2]
    U,V=mutate(A,C,B),mutate(B,C,A)
    S,R=sub(U,C),sub(V,C)
    # Actual canonical ROOT, degree-oriented endpoints X=1,Y=x+2.
    assert S==[8,20,16,4]
    assert R==[24,68,72,34,6]
    root=audit_pair(S,R)
    assert root['central_target']==272
    assert root['central_parts']=={'even_even':128,'odd_odd':0,'mixed':144}
    assert next(t for t in root['central_terms'] if (t['a'],t['b'])==(0,1))['product']==-64
    # Earlier combined shape obstruction, reconstructed from factorizations.
    f=mul(mul([1,1],[1,1]),[5,4])
    g=mul(mul(mul([1,1],[1,1]),[3,2]),[9,4])
    relaxed=audit_pair(f,g)
    assert relaxed['central_target']==-8
    assert relaxed['central_parts']=={'even_even':82,'odd_odd':0,'mixed':-90}
    assert all(t['minor']>=0 for v in relaxed['parity_source_minors'].values() for t in v)
    # Minimal kernel obstruction to mixing the two proved parity sectors.
    assert K(0)==[1,1] and K(1)==[2,1,1]
    assert determinant(K(0),K(1),0)==-1
    payload={'domain':{'root':'canonical ROOT with original scalar mutation','relaxed':'not canonical; shape counterexample only'},'root':root,'relaxed_within_parity_counterexample':relaxed,'mixed_kernel_witness':{'degrees':[0,1],'columns':[0,1],'minor':-1},'universal_proof':'See alternative_parity_audit.md; not inferred from enumeration.'}
    out=Path(__file__).with_name('alternative_parity_results.json')
    out.write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({'ROOT_target':root['central_target'],'ROOT_negative_sourcewise_term':-64,'relaxed_target':relaxed['central_target'],'relaxed_parity_minors_nonnegative':True,'output':str(out)}))

if __name__=='__main__':main()
