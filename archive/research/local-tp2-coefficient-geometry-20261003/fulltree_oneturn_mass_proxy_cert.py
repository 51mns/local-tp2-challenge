"""Exact finite bridge for one-turn central mass and fixed-proxy bounds.

For each m=2,...,390, certifies a whole one-parameter template family
and every supported base-proxy minor. Combined with the separate
uniform tail inequalities this discharges, rather than samples, the
finite remaining interval.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def val(a,n):
    n=abs(n)
    return a[n] if n<len(a) else 0


def add(a,b,scale_b=1):
    return [val(a,n)+scale_b*val(b,n) for n in range(max(len(a),len(b)))]


def mul_low(a,b,n):
    return sum(a[abs(j)]*val(b,n-j) for j in range(1-len(a),len(a)))


def mul_small(a,b):
    # The second factor has degree at most two throughout this verifier.
    return [sum(b[abs(j)]*val(a,n-j) for j in range(1-len(b),len(b)))
            for n in range(len(a)+len(b)-1)]


def scale(a,c):
    return [c*v for v in a]


def mass(a):
    return a[0]+2*sum(a[1:])


def central_margin_bern(row0,row1,mass0,mass1,margin):
    """row(v)=row0+v row1, v in [0,1]; degree-two Bernstein."""
    a,b,c=row0
    d,e,f=row1
    power=[a*a-2*b*b+a*c-margin*mass0,
           2*a*d-4*b*e+a*f+d*c-margin*mass1,
           d*d-2*e*e+d*f]
    return [Q(power[0]),Q(2*power[0]+power[1],2),Q(sum(power))]


def main():
    limit=390
    y=[1,1]
    y2=mul_small(y,y)
    p1=[2,1]
    p1sq=mul_small(p1,p1)
    u=[[1],[3,2]]
    prefixes=[[1],[4,2]]
    for j in range(2,limit+2):
        uj=add(mul_small(u[-1],[3,2]),u[-2],-1)
        assert uj[-1]==2**j and min(uj)>0
        u.append(uj)
        prefixes.append(add(prefixes[-1],uj))
    certificates=[]
    for m in range(2,limit+1):
        T=prefixes[m]
        A=prefixes[m+1]
        B=prefixes[m-1]
        P=add(mul_small(T,y),[1])
        t=add(scale(mul_small(P,y),3),[0,1],-1)
        J=mul_small(add(t,[2],-1),y)
        V=scale(mul_small(mul_small(P,y2),p1),3)
        K=scale(mul_small(P,p1sq),2)
        assert len(J)==len(K)==m+4 and len(V)==m+5
        Jmass=mass(J)
        minors=[val(J,n)*val(V,n+1)-val(J,n+1)*val(V,n)
                for n in range(len(J))]
        assert min(minors)>0,(m,'base proxy')
        ratios=[Q(Jmass*K[n],minors[n]) for n in range(len(J))]
        max_ratio=max(ratios)
        ceil_ratio=(max_ratio.numerator+max_ratio.denominator-1)//max_ratio.denominator
        gamma=2*ceil_ratio+13
        assert gamma>12
        assert all(gamma*minors[n]>2*Jmass*K[n] for n in range(len(J)))
        # L_r=A(t-r)+B and r=2-4v, with v ranging over [0,1].
        L_at_2=[mul_low(A,t,n)+val(B,n)-2*val(A,n) for n in range(3)]
        L_slope=[4*val(A,n) for n in range(3)]
        Lmass_at_2=mass(A)*(mass(t)-2)+mass(B)
        Lmass_slope=4*mass(A)
        template=central_margin_bern(L_at_2,L_slope,Lmass_at_2,Lmass_slope,gamma)
        assert min(template)>0,(m,'template margin',gamma,min(template))
        trace=central_margin_bern([t[0]-2,t[1],t[2]],[4,0,0],mass(t)-2,4,4)
        assert min(trace)>0,(m,'trace margin')
        certificates.append({
            'm':m,
            'gamma':str(gamma),
            'minimum_base_minor':str(min(minors)),
            'maximum_proxy_ratio':str(max_ratio),
            'maximum_proxy_ratio_index':ratios.index(max_ratio),
            'template_margin_bernstein':[str(v) for v in template],
            'trace_margin_bernstein':[str(v) for v in trace],
            'minimum_proxy_remainder':str(min(gamma*minors[n]-2*Jmass*K[n]
                                             for n in range(len(J)))),
        })
    result={'status':'PASS','inner_interval':[2,limit],
            'parameter':'all r in [-2,2]',
            'template_conclusion':'delta_0(A(t-r)+B) > gamma_m * (A(t-r)+B)(2)',
            'trace_conclusion':'delta_0(t-r) > 4*(t-r)(2)',
            'proxy_conclusion':'all base minors positive; gamma_m*minor > 2*J(2)*H(K)_n',
            'certificates':certificates}
    Path('fulltree_oneturn_mass_proxy_certificates.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','inner_interval':[2,limit],
                     'continuum_margin_arrays':2*len(certificates),
                     'fixed_proxy_minors':sum(m+4 for m in range(2,limit+1))}))


if __name__=='__main__':
    main()
