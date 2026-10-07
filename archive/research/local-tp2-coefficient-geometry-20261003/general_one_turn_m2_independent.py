"""Independent m=2 mass and fixed-proxy arithmetic audit.

Derives all seeds from the inner Chebyshev recurrence. Uses independent
ordinary-polynomial and direct-Laurent arithmetic; no author imports.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json

# Ordinary integer x-polynomials, stored low degree first.
def xp_add(*items):
    out=[0]*max(map(len,items),default=1)
    for item in items:
        for i,value in enumerate(item):out[i]+=value
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def xp_scale(p,c):return [c*v for v in p]
def xp_mul(p,r):
    out=[0]*(len(p)+len(r)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(r):out[i+j]+=a*b
    return xp_add(out)

# Laurent polynomials in q, with one unit-interval parameter u.
def constant(c):return {(0,0):Q(c)} if c else {}
def add(*items):
    out={}
    for item in items:
        for key,value in item.items():out[key]=out.get(key,Q(0))+value
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:c*v for k,v in p.items() if c*v}
def mul(p,r):
    out={}
    for (i,a),v in p.items():
        for (j,b),w in r.items():
            k=(i+j,a+b);out[k]=out.get(k,Q(0))+v*w
    return {k:v for k,v in out.items() if v}
def row(p,n):return {(0,j):v for (i,j),v in p.items() if i==n}
def mass(p):return add(*[{(0,j):v} for (i,j),v in p.items()])
def delta0(p):
    h0,h1,h2=[row(p,n) for n in range(3)]
    return add(mul(h0,h0),scale(mul(h1,h1),-2),mul(h0,h2))
def bernstein(p):
    degree=max((j for i,j in p),default=0)
    return degree,[sum((v*Q(comb(k,j),comb(degree,j)) for (i,j),v in p.items() if j<=k),Q(0)) for k in range(degree+1)]
def from_xp(p,x):
    out={};power=constant(1)
    for value in p:
        out=add(out,scale(power,value));power=mul(power,x)
    return out

def fixed_row(p):
    degree=max(i for i,j in p)
    values=[]
    for n in range(degree+1):
        h=row(p,n)
        assert h==row(p,-n)
        assert set(h)=={(0,0)}
        value=h[(0,0)]
        assert value.denominator==1 and value>0
        values.append(int(value))
    return values

def minors(a,b):
    n=max(len(a),len(b))
    a=a+[0]*(n+1-len(a));b=b+[0]*(n+1-len(b))
    return [a[j]*b[j+1]-a[j+1]*b[j] for j in range(n)]


def main():
    xx=[0,1];yy=[1,1];P1x=[2,1];zz=[3,2]
    ix=[[1],zz]
    for _ in range(2,4):ix.append(xp_add(xp_mul(zz,ix[-1]),xp_scale(ix[-2],-1)))
    prefix_x=[xp_add(*ix[:j+1]) for j in range(4)]
    Px=xp_add([1],xp_mul(yy,prefix_x[2]))
    ax,bx=prefix_x[3],prefix_x[1]
    tx=xp_add(xp_scale(xp_mul(yy,Px),3),xp_scale(xx,-1))
    assert Px==[13,26,18,4]
    assert ax==[33,64,40,8] and bx==[4,2]
    assert tx==[39,116,132,66,12]

    x={(1,0):Q(1),(-1,0):Q(1)}
    y=add(x,constant(1));P1=add(x,constant(2));z=add(scale(x,2),constant(3))
    inner=[constant(1),z]
    for _ in range(2,4):inner.append(add(mul(z,inner[-1]),scale(inner[-2],-1)))
    prefix=[add(*inner[:j+1]) for j in range(4)]
    P=add(constant(1),mul(y,prefix[2]));a,b=prefix[3],prefix[1]
    t=add(scale(mul(y,P),3),scale(x,-1))
    for ordinary,laurent in [(Px,P),(ax,a),(bx,b),(tx,t)]:assert from_xp(ordinary,x)==laurent
    assert mass(t)==constant(1519) and mass(a)==constant(385) and mass(b)==constant(8)

    f=add(t,constant(-2),{(0,1):Q(4)})
    L=add(mul(a,f),b)
    source_path=Path('general_one_turn_m2_margin_certificates.json')
    source=json.loads(source_path.read_text())
    certificates={}
    for name,poly,factor in [('propagator',f,4),('resolvent_template',L,800)]:
        difference=add(delta0(poly),scale(mass(poly),-factor))
        degree,coefficients=bernstein(difference)
        assert min(coefficients)>0
        expected=source[name]
        assert expected['mass_factor']==factor
        c=expected['certificate']
        assert c['degrees']==[degree,0,0,0]
        assert c['strict_lower_bound']==str(min(coefficients))
        assert c['power_coefficients']=={f'{j},0,0,0':str(v) for (i,j),v in difference.items()}
        assert c['bernstein_coefficients']=={f'{j},0,0,0':str(v) for j,v in enumerate(coefficients)}
        certificates[name]={'mass_factor':factor,'power_coefficients':c['power_coefficients'],
                            'bernstein_coefficients':[str(v) for v in coefficients],
                            'strict_lower_bound':str(min(coefficients)),'all_arrays_match':True}

    F=mul(y,add(t,constant(-2)))
    G=scale(mul(mul(mul(y,y),P),P1),3)
    K=scale(mul(P,mul(P1,P1)),2)
    Fx=xp_mul(yy,xp_add(tx,[-2]))
    Gx=xp_scale(xp_mul(xp_mul(xp_mul(yy,yy),Px),P1x),3)
    Kx=xp_scale(xp_mul(Px,xp_mul(P1x,P1x)),2)
    for ordinary,laurent in [(Fx,F),(Gx,G),(Kx,K)]:assert from_xp(ordinary,x)==laurent
    hF,hG,hK=map(fixed_row,(F,G,K))
    expected_F=[1001,867,560,258,78,12]
    expected_G=[3750,3306,2250,1155,426,102,12]
    expected_K=[1268,1076,650,268,68,8]
    assert hF==expected_F and hG==expected_G and hK==expected_K
    comparison=minors(hF,hG)[:len(hF)]
    assert comparison==[58056,99390,66300,19818,2844,144]
    assert all(v>0 for v in comparison)
    Fmass=int(mass(F)[(0,0)])
    assert Fmass==4551
    residual=[256*m-Fmass*k for m,k in zip(comparison,hK)]
    assert residual==[9091668,20546964,14014650,3853740,418596,456]
    assert all(v>0 for v in residual)
    result={'status':'PASS','method':'separate ordinary-x and direct-Laurent recurrences plus exact Bernstein reconstruction',
            'mass_certificate_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
            'inner_seeds':{'P':Px,'a':ax,'b':bx,'t':tx},
            'mass_certificates':certificates,
            'fixed_proxy':{'F_x_coefficients':Fx,'G_x_coefficients':Gx,'K_x_coefficients':Kx,
                           'H_F':hF,'H_G':hG,'H_K':hK,'adjacent_minors':comparison,
                           'F_mass':Fmass,'central_margin_factor':256,'residual_margins':residual}}
    Path('general_one_turn_m2_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'mass_certificate_sha256':result['mass_certificate_sha256'],
                      'mass_lower_bounds':{k:v['strict_lower_bound'] for k,v in certificates.items()},
                      'fixed_rows_match':True,'fixed_pair_minors':comparison,'residual_margins':residual},indent=2))

if __name__=='__main__':main()
