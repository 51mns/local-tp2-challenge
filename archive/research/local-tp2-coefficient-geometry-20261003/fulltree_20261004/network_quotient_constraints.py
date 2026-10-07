"""Exact verification of canonical quotient compatibility; not a TP2 proof."""
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import continuation_prefix as v
import tp2_source as p

add, mul, scale, const = v.add, v.mul, v.scale, v.const
sub=lambda a,b: add(a,scale(b,-1))
sq=lambda a:mul(a,a)
x,a,e,r=[v.variable(i) for i in range(4)]
y=add(x,const(1))
t=lambda A:add(scale(x,2),const(3),scale(mul(sq(y),A),3))
k=lambda A:mul(add(const(1),mul(y,A)),add(const(1),scale(mul(y,A),3)))
T=sub(t(a),const(2))
g=add(mul(T,e),k(a),r)
X=add(const(1),mul(y,a));Y=add(X,mul(y,e));C=add(Y,mul(y,g))
mut=lambda A,C,B:sub(sub(scale(mul(mul(y,A),C),3),mul(x,add(A,C))),B)
U,V=mut(X,C,Y),mut(Y,C,X)
s=add(mul(sub(t(a),const(1)),g),mul(T,e),k(a))
M=add(t(a),const(1),scale(mul(sq(y),add(e,g)),3))
assert sub(U,C)==mul(y,s)
assert sub(V,U)==mul(y,mul(e,M))
assert sub(sub(s,mul(T,add(e,g))),k(a))==g
assert sub(sub(add(s,mul(e,M)),mul(sub(t(add(a,e)),const(2)),g)),k(add(a,e)))==add(e,g)
assert sub(k(add(a,e)),k(a))==add(scale(mul(y,e),4),scale(mul(mul(sq(y),a),e),6),scale(mul(sq(y),sq(e)),3))
b=sub(add(a,e),r)
assert sub(k(a),mul(T,a))==add(const(1),mul(add(scale(x,2),const(3)),a))
assert sub(g,mul(sub(t(a),const(1)),r))==add(mul(T,b),const(1),mul(add(scale(x,2),const(3)),a))
assert sub(add(a,add(e,g)),g)==add(a,e)
assert sub(add(add(a,e),g),add(e,g))==a
# Barrier transport uses independent formal T,e,r,k, not a tree scan.
z,E,R,K=[v.variable(i) for i in range(4)]
G=add(mul(z,E),K,R)
P,Q=const(0),const(1)
barrier_checks=0
for m in range(1,10):
    oldP,oldQ=P,Q
    P=add(mul(z,oldQ),oldP)
    Q=add(mul(add(z,const(1)),oldQ),oldP)
    assert sub(Q,P)==oldQ
    assert sub(mul(mul(z,Q),sub(Q,P)),sq(P))==z
    Dnew=sub(mul(Q,G),mul(P,add(E,G)))
    Dold=sub(mul(oldQ,R),mul(oldP,E))
    assert Dnew==add(Dold,mul(oldQ,K))
    assert min(P.values())>0 and min(Q.values())>0
    barrier_checks+=1
# Exact paired-block obstruction at the canonical root.
NN=[[sub(z,const(1)),const(1)],[sub(z,const(2)),const(1)]]
NN2=[[add(*(mul(NN[i][j],NN[j][ell]) for j in range(2))) for ell in range(2)] for i in range(2)]
assert NN2==[[sub(sub(sq(z),z),const(1)),z],[mul(z,sub(z,const(2))),sub(z,const(1))]]
for poly,expected in [([2,2],-4),(p.mul([1,2],[5,2]),-67)]:
    hh=p.H(poly)
    at=lambda n:p.hget(hh,abs(n))
    assert at(0)**2-at(-1)*at(1)-at(1)**2+at(0)*at(2)==expected
# Root short chain constant terms, independently via integer recurrence.
fib=[0,1]
for _ in range(44):fib.append(sum(fib[-2:]))
ee,rr=1,1
for n in range(20):
    assert ee==fib[2*n+3]-1 and rr==fib[2*n+2]
    gg=ee+1+rr
    ee,rr=ee+gg,gg
# Actual canonical scalar identities: these do not prove the universal claims.
node_checks=0
for rec in p.generate_tree(4):
    XX,YY=sorted((rec['A'],rec['B']),key=len)
    aa=[0] if XX==[1] else p.divide_x_plus_one(p.sub(XX,[1]))
    ee=p.divide_x_plus_one(p.sub(YY,XX))
    gg=p.divide_x_plus_one(p.sub(rec['C'],YY))
    tt=p.add([3,2],p.scale(p.mul(p.mul([1,1],[1,1]),aa),3))
    TT=p.sub(tt,[2])
    kk=p.mul(p.add([1],p.mul([1,1],aa)),p.add([1],p.scale(p.mul([1,1],aa),3)))
    rr=p.sub(p.sub(gg,p.mul(TT,ee)),kk)
    assert min(rr)>=0
    assert min(p.sub(p.scale(rr,5),p.scale(ee,3)))>=0
    assert min(p.sub(p.scale(ee,5),p.scale(rr,3)))>=0
    PP,QQ=[0],[1]
    for m in range(5):
        assert min(p.sub(p.mul(QQ,rr),p.mul(PP,ee)))>=0
        PP,QQ=p.add(p.mul(TT,QQ),PP),p.add(p.mul(p.add(TT,[1]),QQ),PP)
    node_checks+=1
out={'status':'PASS','scope':'all-depth coefficient-order lemmas proved in manuscript; Local TP2 remains open',
     'scalar_mutation_child_identities':'PASS',
     'incoming_gap_separation_identity':'PASS',
     'two_step_entry_obstruction_defects':[-4,-67],
     'symbolic_barrier_indices_checked':barrier_checks,
     'Fibonacci_constant_term_indices_checked':20,
     'canonical_implementation_nodes_checked':node_checks}
path=Path(__file__).with_name('network_quotient_constraints_results.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
