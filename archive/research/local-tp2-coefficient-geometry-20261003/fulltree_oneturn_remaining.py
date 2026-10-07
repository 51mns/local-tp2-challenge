"""Exact residue certificates and scalar bounds for the remaining one-turn kernels.

This is an infinite root-factor proof's finite box component, not an index scan.
"""
import json
from fractions import Fraction as Q
import mixed_kernel_pureleft_margin as c
p=c.p


def direct_y_power(j):
    yy=p.const(1)
    for _ in range(j): yy=p.mul(yy,c.b.y)
    return yy


def scalar_checks():
    sigma=Q(59,100); c0=Q(1,400000000); m=391
    eps=Q(2*m+5,9*6**m)
    EyH=c0**3*sigma**(3*m+1)/(16*(m+3)**2)
    EL=c0**2*sigma**(2*m+1)/(4*(m+3))
    # L and yL: B <= epsilon F, using t0 >= 27*6^m/(2m+5)
    # and 1/(t0-2) <= 3/t0.
    assert EyH >= 12*eps
    assert EL >= 12*eps
    assert eps < 1
    # Consecutive ratios of E/(12 eps); factors individually increase in m.
    assert 6*sigma**3*Q((m+3)**2*(2*m+5),(m+4)**2*(2*m+7)) > 1
    assert 6*sigma**2*Q((m+3)*(2*m+5),(m+4)*(2*m+7)) > 1
    # yH needs lambdaF >=32 H(yB)[0], whose central mass is <=3 B(2).
    lamF=9*2**(3*m-2)
    assert lamF >= 96*Q(7**m-1,6)
    # Normalized y-prefix residue bound, d<=18.
    assert 4352*sigma**16 < 1
    assert 6*c0*(Q(9,2)*sigma)**18 < 1
    return {'threshold':m,'EyH_over_12epsilon':str(EyH/(12*eps)),
            'EL_over_12epsilon':str(EL/(12*eps)),
            'EyH_ratio_next_lower':str(6*sigma**3*Q((m+3)**2*(2*m+5),(m+4)**2*(2*m+7))),
            'EL_ratio_next_lower':str(6*sigma**2*Q((m+3)*(2*m+5),(m+4)*(2*m+7))),
            'lambdaF_over_yB_bound':str(Q(lamF,1)/(96*Q(7**m-1,6)))}


if __name__=='__main__':
    result={'description':'All tensor Bernstein coefficients are exact rational numbers.',
            'residues':{},'scalar_checks':scalar_checks(),'m1':{}}
    for name,R in c.residues.items():
        d=max(k[0] for k in R); leading=2**d
        result['residues'][name]={'residue_degree':d,'strength':str(Q(leading,2))}
        for j in (1,3):
            poly=p.scale(p.mul(direct_y_power(j),R),leading)
            cert=c.cert_strength(name+'_y'+str(j),poly,Q(leading,2))
            assert all(Q(cc['lower_bound'])>0 for cc in cert)
            result['residues'][name]['y'+str(j)]=cert
    # T1 = 2x+4. These explicit polynomials handle the exceptional small prefix.
    T1=p.add(p.scale(c.x,2),p.const(4))
    for j in (1,3):
        result['m1']['y'+str(j)]=c.cert_strength('m1_y'+str(j),p.mul(direct_y_power(j),T1),1)
    with open('fulltree_oneturn_remaining_certificates.json','w') as out:
        json.dump(result,out,indent=2)
