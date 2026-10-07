"""Exact certificate: proposed F hypotheses do not close under mutation.
This is an abstract noncanonical triple; no search is run by this verifier.
"""
import sys
sys.path.insert(0, 'kernel_proof')
from canonical_arithmetic import add, sub, mul, scale, H, children

def defect(h):
    def v(n):
        n=abs(n)
        return h[n] if n<len(h) else 0
    d=[v(n)**2-v(n-1)*v(n+1) for n in range(len(h)+1)]
    return [d[n]-d[n+1] for n in range(len(h))]

def alpha(p):
    h=H(p)
    return [h[i]-(h[i+1] if i+1<len(h) else 0) for i in range(len(h))]

def lr_minors(a,b):
    # Include every pair, so interval supports need not be assumed.
    N=max(len(a),len(b))
    a=a+[0]*(N-len(a)); b=b+[0]*(N-len(b))
    return {(i,j):a[i]*b[j]-a[j]*b[i] for i in range(N) for j in range(i+1,N)}

def in_F(p):
    h=H(p); d=defect(h)
    return len(p)>=3 and min(h)>0 and all(dn>=2*hn for dn,hn in zip(d,h)) and defect(H(mul([1,1],p)))[0]>=0

A=[1]
B=[71,128,58]
C=[32,122,120,29]
U=children(A,C,B)[0]
assert U == [25,301,546,327,58]
assert H(U) == [1465,1282,778,327,58]
for label,p in [('A',A),('B',B),('C',C),('U',U)]:
    assert sum(c*(-1)**i for i,c in enumerate(p))==1
    assert min(p)>0 and min(alpha(p))>0
    print(label, 'ordinary',p,'H',H(p),'alpha',alpha(p),'delta',defect(H(p)), 'delta0_y',defect(H(mul([1,1],p)))[0])
assert in_F(B) and in_F(C)
assert len(C)>len(A) and len(C)>len(B)
assert len(C)-1 == (len(A)-1)+(len(B)-1)+1
assert min(alpha(sub(C,A)))>0 and min(alpha(sub(C,B)))>0
assert alpha(C)[0]>=3 and alpha(C)[1]>=alpha(C)[0]
assert alpha(U)[1]>=alpha(U)[0]+2
assert min(alpha(sub(U,C)))>0
assert min(alpha(sub(U,A)))>0
assert defect(H(U))[0] == -1053
P=[2,1]
for label,first,second in [
    ('A <= B', A,B), ('B <= C',B,C),
    ('PA <= C-A',mul(P,A),sub(C,A)),
    ('PB <= C-B',mul(P,B),sub(C,B))]:
    minors=lr_minors(H(first),H(second))
    assert min(minors.values())>=0
    print(label, 'all_pair_minors',minors)
# Original polynomial Fricke residual, identically zero on canonical triples.
res=add(add(mul(C,C),mul([0,1],mul(add(A,B),C))),add(mul(A,A),add(mul(B,B),mul([0,1],mul(A,B)))))
res=sub(res,mul([3,3],mul(mul(A,B),C)))
assert res != [0]
print('Fricke residual ascending',res)
print('PASS: this refutes abstract F mutation closure, not canonical closure.')
