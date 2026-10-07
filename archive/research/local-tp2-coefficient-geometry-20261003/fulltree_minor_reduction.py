"""Exact gap identities and an abstract obstruction for full-tree induction.

The multivariate identities are checked before imposing the Fricke equation.
The counterexample is explicitly a noncanonical S,D pair, not a tree state.
"""
import json
import continuation_prefix as r
import tp2_source as p


def symbolic_identities():
    x,X,Y,C=[r.variable(n) for n in range(4)]
    one=r.const(1); y=r.add(x,one)
    sub=lambda a,b:r.add(a,r.scale(b,-1))
    sq=lambda a:r.mul(a,a)
    def mutate(a,c,b):
        return r.add(r.scale(r.mul(r.mul(y,a),c),3),
                     r.scale(r.mul(x,r.add(a,c)),-1),r.scale(b,-1))
    tx=sub(r.scale(r.mul(y,X),3),x)
    ty=sub(r.scale(r.mul(y,Y),3),x)
    M=r.add(sub(r.scale(r.mul(y,C),3),x),one)
    E=sub(Y,X); G=sub(C,Y); Hgap=sub(C,X)
    U=mutate(X,C,Y); V=mutate(Y,C,X)
    S=sub(U,C); D=sub(V,U); Q=r.add(S,D)
    assert D==r.mul(E,M)
    SL=sub(mutate(X,U,C),U)
    DL=sub(mutate(C,U,X),mutate(X,U,C))
    SR=sub(mutate(Y,V,C),V)
    DR=sub(mutate(C,V,Y),mutate(Y,V,C))
    assert SL==sub(r.mul(tx,S),G)
    assert DL==r.mul(Hgap,r.add(M,r.scale(r.mul(y,S),3)))
    assert SR==sub(r.mul(ty,Q),Hgap)
    assert DR==r.mul(G,r.add(M,r.scale(r.mul(y,Q),3)))
    assert r.add(SL,DL)==r.add(r.mul(sub(M,one),r.add(S,G)),D)
    assert r.add(SR,DR)==sub(r.mul(sub(M,one),r.add(Q,G)),E)

    fricke=r.add(sq(X),sq(Y),sq(C),
                 r.mul(x,r.add(r.mul(X,Y),r.mul(X,C),r.mul(Y,C))),
                 r.scale(r.mul(r.mul(r.mul(y,X),Y),C),-3))
    Kx=r.mul(r.mul(y,sq(X)),r.add(r.scale(X,3),x,r.const(-2)))
    Ky=r.mul(r.mul(y,sq(Y)),r.add(r.scale(Y,3),x,r.const(-2)))
    qprev=r.add(C,r.scale(r.mul(sub(tx,one),Y),-1),r.mul(x,X))
    assert qprev==sub(r.mul(tx,G),S)
    assert r.add(sq(G),r.scale(r.mul(qprev,S),-1),r.scale(Kx,-1))==r.scale(r.mul(sub(tx,r.const(2)),fricke),-1)
    assert r.add(r.mul(G,SL),r.scale(sq(S),-1),Kx)==r.mul(sub(tx,r.const(2)),fricke)
    assert r.add(r.mul(Hgap,SR),r.scale(sq(Q),-1),Ky)==r.mul(sub(ty,r.const(2)),fricke)
    return {'child_gap_pairs':'PASS', 'child_gap_sums':'PASS',
            'Cassini_with_explicit_Fricke_residual':'PASS',
            'both_child_gap_exchange_identities':'PASS'}


def differences(poly):
    h=p.H(poly)
    return [h[n]-p.hget(h,n+1) for n in range(len(h))]


def defects(poly):
    h=p.H(poly); at=lambda n:p.hget(h,abs(n))
    delta=[at(n)**2-at(n-1)*at(n+1) for n in range(len(h)+1)]
    return [delta[n]-delta[n+1] for n in range(len(h))]


def exact_obstruction():
    S=p.mul([1,1],[100,50,1])
    D0=p.scale(p.mul([1,1],p.mul([2,1],p.mul([2,1],[2,1]))),2)
    D=p.add(S,D0)
    assert S==[100,150,51,1] and D==[116,190,87,15,2]
    rows={name:p.H(poly) for name,poly in [('S',S),('D',D),('D_minus_S',D0)]}
    alpha={name:differences(poly) for name,poly in [('S',S),('D',D),('D_minus_S',D0)]}
    delta={name:defects(poly) for name,poly in [('S',S),('D',D),('D_minus_S',D0)]}
    for name,poly in [('S',S),('D',D),('D_minus_S',D0)]:
        assert min(poly)>0 and min(alpha[name])>0
        assert p.eval_poly(poly,-1)==0
        assert all(d>=poly[-1]*h for d,h in zip(delta[name],rows[name]))
    h,g=alpha['S'],alpha['D']
    adjacent=[p.W(h,g,n,n+1) for n in range(len(h))]
    assert adjacent==[26,1160,570,2]
    assert all(p.W(h,g,i,j)>0 for i in range(len(h)) for j in range(i+1,len(g)))
    original=[p.W(rows['S'],rows['D'],n,n+1) for n in range(len(rows['S']))]
    assert original==[1264,2550,670,2]
    total=p.add(S,D)
    assert defects(total)[3]==-40
    return {
        'scope':'abstract noncanonical pair; NOT a counterexample to canonical Local TP2',
        'S':S,'D':D,'D_minus_S':D0,
        'half_rows':rows,'character_rows':alpha,'folded_defects':delta,
        'strict_first_difference_adjacent_minors':adjacent,
        'strict_original_adjacent_minors':original,
        'sum_half_row':p.H(total),'sum_folded_defects':defects(total),
        'failure_index':3,'negative_sum_defect':-40,
        'scaling':'Every positive integer common scaling preserves all hypotheses and the failure.'}


def main():
    print(json.dumps({'status':'PASS','symbolic':symbolic_identities(),
                      'obstruction':exact_obstruction()},indent=2))


if __name__=='__main__':
    main()
