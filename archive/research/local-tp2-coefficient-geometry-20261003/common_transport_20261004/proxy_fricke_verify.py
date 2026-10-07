#!/usr/bin/env python3
"""Exact proxy exchange, center-block reduction, and curvature obstacle."""
from pathlib import Path
import json
from proxy_curvature_verify import (
    spvar,spconst,spadd,spmul,bscale,minus,plus,cprod,dd,kap,state,R,
)
from tp2_source import add,sub,mul,H,hget,generate_tree

HERE=Path(__file__).resolve().parent


def defect(row,n):
    f=lambda k:hget(row,abs(k))
    return f(n)**2-f(n-1)*f(n+1)-f(n+1)**2+f(n)*f(n+2)


def symbolic_children():
    x,X,Y,C=[spvar(i,4) for i in range(4)]
    one,two=spconst(1,4),spconst(2,4)
    y,p=spadd(x,one),spadd(x,two)
    I=minus(spadd(spmul(X,X),spmul(Y,Y),spmul(C,C),
                  spmul(x,spadd(spmul(X,Y),spmul(X,C),spmul(Y,C)))),
            bscale(spmul(y,X,Y,C),3))
    U=minus(minus(bscale(spmul(y,X,C),3),spmul(x,spadd(X,C))),Y)
    V=minus(minus(bscale(spmul(y,Y,C),3),spmul(x,spadd(Y,C))),X)
    S,F=minus(U,C),minus(V,C)
    qs=minus(spmul(minus(minus(bscale(spmul(y,X),3),x),two),U),spmul(x,X))
    ql=minus(spmul(minus(minus(bscale(spmul(y,Y),3),x),two),V),spmul(x,Y))
    errors={
        'short_proxy_positive_exchange':spadd(minus(spmul(C,qs),
                       spadd(spmul(S,S),spmul(X,X),spmul(x,X,U))),I),
        'long_proxy_positive_exchange':spadd(minus(spmul(C,ql),
                       spadd(spmul(F,F),spmul(Y,Y),spmul(x,Y,V))),I),
    }
    assert all(not e for e in errors.values())
    return list(errors)


def run():
    symbols=symbolic_children()
    recs={rec['path']:rec for rec in generate_tree(1)}
    st=state(recs['L'])
    k=st['kX']
    L={(2,2):1,(2,0):-3,(0,2):-3,(0,0):9}
    correction=bscale(cprod(L,k),-1)
    boundary=[correction.get((2*n,0),0) for n in range(4)]
    assert boundary==[-245,43,-44,48]
    b=[k.get((2*n,0),0) for n in range(3)]
    c=[k.get((2*n,2),0) for n in range(3)]
    assert b==[45,36,16] and c==[36,56,0]
    gd=[defect(H(st['G']),n) for n in range(len(st['G']))]
    assert gd==[192,256,112,16]
    C=[5,6,2];M=[16,32,24,6];p=[2,1];one=[1]
    centerbase=R(sub(M,one),mul(p,M))
    assert centerbase==minus(R(M,[0]+M),dd(mul(p,M)))
    h=H(mul([1,1],C));m=H(M)
    central=defect(m,0)-H(mul(p,M))[1]
    assert central==9*defect(h,0)+3*h[0]+6*h[1]==444
    # Exact obstruction to universal LR reflection through the fixed
    # actual canonical multiplier Croot. The pair y,xy is not a proxy pair.
    f=[1,1];g=[0,1,1]
    before=R(f,g);after=R(mul(C,f),mul(C,g))
    assert before[(0,0)]==-1 and all(v>=0 for v in after.values())
    return dict(status='universal exchange identities and exact obstacles checked',
                symbolic_checks=symbols,
                canonical_curvature_forcing_obstacle={
                    'path':'first-short','curvature_char_nonnegative':all(v>=0 for v in k.values()),
                    'kappa_boundary0':b,'kappa_boundary2':c,
                    'minus_L_kappa_boundary':boundary,'actual_G_defects':gd,
                    'scope':'refutes nonnegative signed-Cassini-forcing inference, not G cone or proxy'},
                root_centerbase={'central_coefficient':central,
                                 'M_defects':[defect(m,n) for n in range(len(m))],
                                 'boundary':[centerbase.get((2*n,0),0) for n in range(len(M))]},
                convolution_reflection_obstacle={
                    'actual_canonical_multiplier_C':C,'input_pair':[f,g],
                    'input_central_minor':-1,
                    'multiplied_defects':[defect(H(mul(C,f)),n) for n in range(len(mul(C,f)))],
                    'multiplied_character_nonnegative':True,
                    'scope':'noncanonical test pair; no proxy-child counterexample'},
                strict_proxy_BOTH_preservation='OPEN',full_tree_Local_TP2='OPEN')


if __name__=='__main__':
    data=run()
    HERE.joinpath('proxy_fricke_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
