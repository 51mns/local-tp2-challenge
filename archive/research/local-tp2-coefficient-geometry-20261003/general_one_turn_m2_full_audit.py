"""Independent exact constants and interval margins for the L^2 R^k proof.

Uses frozen canonical polynomial arithmetic, not the certificate generator.
Parameter polynomials are represented directly in Z[u]; no interpolation.
"""
import json
from math import comb
import canonical_arithmetic as p


def ring_fourier(ordinary):
    return [sum_ring(p.scale(ordinary[j],comb(j,(j-n)//2))
                     for j in range(n,len(ordinary),2))
            for n in range(len(ordinary))]


def sum_ring(polys):
    out=[0]
    for polynomial in polys:
        out=p.add(out,polynomial)
    return out


def ring_product(a,b):
    out=[[0] for _ in range(len(a)+len(b)-1)]
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            out[i+j]=p.add(out[i+j],p.mul(ai,bj))
    return out


def mass_margin(ordinary,factor):
    h=ring_fourier(ordinary)
    delta0=p.sub(p.add(p.mul(h[0],h[0]),p.mul(h[0],h[2])),
                 p.scale(p.mul(h[1],h[1]),2))
    mass=sum_ring(p.scale(value,2**j) for j,value in enumerate(ordinary))
    return p.sub(delta0,p.scale(mass,factor))


def main():
    y=[1,1]; P1=[2,1]; z=[3,2]
    inner=[[1],z]
    for n in (2,3):
        inner.append(p.sub(p.mul(z,inner[-1]),inner[-2]))
    prefix=[sum_ring(inner[:n+1]) for n in range(4)]
    a=prefix[3]; b=prefix[1]
    P=p.add([1],p.mul(y,prefix[2]))
    t=p.sub(p.scale(p.mul(y,P),3),[0,1])
    assert a==[33,64,40,8] and b==[4,2]
    assert P==[13,26,18,4] and t==[39,116,132,66,12]
    first_left=p.mutation_left(p.G0,p.G12,p.G1)
    second_left=p.mutation_left(p.G0,first_left,p.G12)
    first_right=p.mutation_right(p.G0,second_left,first_left)
    assert P==first_left
    assert second_left==p.add([1],p.mul(y,a))
    assert p.sub(first_right,second_left)==p.mul(y,p.add(p.mul(a,t),b))

    # r=2-4u ranges over [-2,2] when 0<=u<=1.
    f=[[t[0]-2,4]]+[[value] for value in t[1:]]
    L=ring_product([[value] for value in a],f)
    for n,value in enumerate(b):
        L[n]=p.add(L[n],[value])
    margins={'propagator':mass_margin(f,4),
             'resolvent_template':mass_margin(L,800)}
    assert margins=={'propagator':[3009,3688,16],
                     'resolvent_template':[9999933,9224984,28816]}
    assert all(min(values)>0 for values in margins.values())

    F=p.mul(p.sub(t,[2]),y)
    G=p.scale(p.mul(p.mul(p.mul(y,y),P),P1),3)
    K=p.scale(p.mul(P,p.mul(P1,P1)),2)
    hf,hg,hk=map(p.H,(F,G,K))
    adjacent=[p.W(hf,hg,n,n+1) for n in range(len(hf))]
    mass_f=p.eval_poly(F,2)
    corrections=[256*adjacent[n]-mass_f*p.hget(hk,n)
                 for n in range(len(hf))]
    assert all(value>0 for value in adjacent+corrections)
    assert len(F)==6 and len(G)==7 and len(K)==6
    assert mass_f==4551
    assert [p.eval_poly(poly,2) for poly in (t,a,b)]==[1519,385,8]
    result={
        'status':'PASS',
        'scope':'exact fixed rows and two interval mass-margin identities; all-k proof in audit note',
        'ordinary':{'P':P,'t':t,'a':a,'b':b,'F':F,'G':G,'K':K},
        'half_rows':{'F':hf,'G':hg,'K':hk},
        'adjacent_fixed_minors':adjacent,
        'mass_F':mass_f,
        'proxy_corrections_at_256':corrections,
        'interval_margin_coefficients_in_u':margins,
        'parameterization':'r=2-4u, 0<=u<=1',
        'mass_values':{'t':1519,'a':385,'b':8},
        'canonical_LL_seed_and_first_right_gap':'PASS'}
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
