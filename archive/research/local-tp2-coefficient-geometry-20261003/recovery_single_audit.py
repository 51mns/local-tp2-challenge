"""Independent exact audit of recovered one-turn single and residue certificates.

No imports of research code. Expected certificates are loaded only after all
mathematical objects have been reconstructed and checked.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import time


def trim(a):
    a = a[:]
    while len(a)>1 and a[-1]==0: a.pop()
    return a


def ordinary_add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)


def convolution(a,b):
    """Exact ordinary coefficient convolution; independent sum carry bound."""
    assert min(a)>=0 and min(b)>=0
    bound=sum(a)*sum(b)
    bits=max(1,bound.bit_length())
    av=bv=0
    for v in reversed(a): av=(av<<bits)+v
    for v in reversed(b): bv=(bv<<bits)+v
    c=av*bv; mask=(1<<bits)-1; out=[]
    for _ in range(len(a)+len(b)-1):
        out.append(c&mask); c>>=bits
    assert c==0 and sum(out)==bound
    return out


def align_add(a,b):
    assert len(a)%2==len(b)%2==1
    n=max(len(a),len(b)); out=[0]*n
    for row in (a,b):
        offset=(n-len(row))//2
        for i,v in enumerate(row): out[offset+i]+=v
    return out


def direct_prefixes(maximum):
    """T_m=(3+2x)T_(m-1)-T_(m-2)+1, with x=z+z^-1."""
    all_t=[[1]]; previous=[0]; current=[1]
    for m in range(1,maximum+1):
        following=convolution([2,3,2],current)
        offset=(len(following)-len(previous))//2
        for i,v in enumerate(previous): following[offset+i]-=v
        following[len(following)//2]+=1
        assert len(following)==2*m+1 and following==following[::-1]
        assert min(following)>0
        all_t.append(following)
        previous,current=current,following
    return all_t


def ordinary_prefix(m):
    previous=[0]; current=[1]; total=[1]
    for _ in range(m):
        following=[0]*(len(current)+1)
        for j,v in enumerate(current):
            following[j]+=3*v; following[j+1]+=2*v
        for j,v in enumerate(previous): following[j]-=v
        total=ordinary_add(total,following)
        previous,current=current,following
    return total


def binomial_laurent(a):
    degree=len(a)-1; out=[0]*(2*degree+1)
    for j,v in enumerate(a):
        for k in range(j+1): out[degree+j-2*k]+=v*comb(j,k)
    return out


def single_certificate(base,sl,twice_strength):
    d=len(base)//2; sd=len(sl)//2
    def row(n):
        return [base[d+n] if -d<=n<=d else 0,
                sl[sd+n] if -sd<=n<=sd else 0]
    result=[]; minima=[None]*3; digest=hashlib.sha256(); bad=zero=0
    positivity=True
    for n in range(d+1):
        h=row(n)
        positivity &= min(h[0],sum(h))>0
        # The generic power polynomial 2 delta_n(H)-twice_strength H_n.
        coeff=[0,0,0]
        for sign,aa,bb in [(1,h,h),(-1,row(n-1),row(n+1)),
                           (-1,row(n+1),row(n+1)),(1,h,row(n+2))]:
            for i,a in enumerate(aa):
                for j,b in enumerate(bb): coeff[i+j]+=2*sign*a*b
        for j,v in enumerate(h): coeff[j]-=twice_strength*v
        for a in range(3):
            value=sum(Q(2*comb(a,j),comb(2,j))*coeff[j] for j in range(a+1))
            assert value.denominator==1
            value=value.numerator
            minima[a]=value if minima[a] is None else min(minima[a],value)
            bad+=value<0; zero+=value==0
            digest.update((str(value)+'\n').encode())
    # At and beyond the next Fourier index all margins are identically zero.
    for n in [d+1,d+2]:
        h=row(n)
        assert h==[0,0] and row(n+1)==[0,0] and row(n+2)==[0,0]
    assert positivity and bad==zero==0
    return dict(degree=d,margins=3*(d+1),twice_strength=str(twice_strength),
                negative=bad,zero=zero,minima=list(map(str,minima)),sha256=digest.hexdigest())


DIM=6
def constant(c): return {(0,)*DIM:Q(c)} if c else {}
def variable(i,exponent=1):
    k=[0]*DIM; k[i]=exponent; return {tuple(k):Q(1)}
def add(*polys):
    out={}
    for poly in polys:
        for k,v in poly.items(): out[k]=out.get(k,Q(0))+v
    return {k:v for k,v in out.items() if v}
def scale(a,c): return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb))
            out[k]=out.get(k,Q(0))+va*vb
    return {k:v for k,v in out.items() if v}
def row(a,n): return {(0,)+k[1:]:v for k,v in a.items() if k[0]==n}
def bernstein(a):
    degrees=[max((k[j] for k in a),default=0) for j in range(1,DIM)]
    out={}
    for idx in product(*(range(d+1) for d in degrees)):
        value=Q(0)
        for k,v in a.items():
            if all(k[j+1]<=idx[j] for j in range(DIM-1)):
                for j in range(DIM-1): v*=Q(comb(idx[j],k[j+1]),comb(degrees[j],k[j+1]))
                value+=v
        out[','.join(map(str,idx))]=str(value)
    return degrees,out


def residue_certificate(poly,strength,require_strict=True):
    d=max(k[0] for k in poly); result=[]
    for n in range(d+1):
        h=row(poly,n)
        assert h==row(poly,-n)
        _,hc=bernstein(h)
        assert min(map(Q,hc.values()))>0
        margin=add(mul(h,h),scale(mul(row(poly,n-1),row(poly,n+1)),-1),
                   scale(mul(row(poly,n+1),row(poly,n+1)),-1),
                   mul(h,row(poly,n+2)),scale(h,-strength))
        degrees,coefficients=bernstein(margin); lower=min(map(Q,coefficients.values()))
        assert lower>0 if require_strict else lower>=0
        result.append(dict(index=n,degrees=degrees,lower_bound=str(lower),
                      power_coefficients={','.join(map(str,k[1:])):str(v) for k,v in margin.items()},
                      bernstein_coefficients=coefficients))
    assert row(poly,d+1)==row(poly,d+2)=={}
    return result


def residues():
    x=add(variable(0),variable(0,-1))
    u,v,w,z,t=[variable(j) for j in range(1,DIM)]
    x2=mul(x,x); y=add(x,constant(1)); central=add(x,constant(Q(3,2)))
    def pair(a,b):
        return add(x2,mul(add(constant(3),a),x),constant(Q(5,4)),scale(a,Q(5,2)),b)
    quartic=mul(pair(u,v),pair(w,z))
    middle=add(central,scale(w,Q(1,2)))
    even=add(x2,scale(x,3),constant(2),scale(u,Q(1,4)))
    odd=add(x2,scale(x,3),constant(Q(7,4)),scale(u,Q(1,2)))
    inner=mul(add(x,constant(1),scale(v,Q(1,2))),add(central,w))
    rr={
        'n_mod8_0_pull_quartic':quartic,
        'n_mod8_1_pull_quartic':mul(quartic,add(central,scale(t,Q(1,2)))),
        'n_mod8_2':mul(central,middle),
        'n_mod8_3':mul(central,inner),
        'n_mod8_4':mul(even,inner),
        'n_mod8_5':mul(mul(even,middle),pair(v,z)),
        'n_mod8_6':mul(mul(mul(central,odd),middle),pair(v,z)),
        'n_mod8_7':mul(central,odd),
    }
    result={}
    for name,r in rr.items():
        d=max(k[0] for k in r); strength=Q(2**d,2)
        result[name]=dict(residue_degree=d,strength=str(strength))
        for j in [1,3]:
            yp=constant(1)
            for _ in range(j): yp=mul(yp,y)
            result[name]['y'+str(j)]=residue_certificate(scale(mul(yp,r),2**d),strength)
        print(json.dumps({'audited_residue':name}),flush=True)
    initial={}
    for j in [1,3]:
        yp=constant(1)
        for _ in range(j): yp=mul(yp,y)
        initial['y'+str(j)]=residue_certificate(mul(yp,add(scale(x,2),constant(4))),1,False)
    return result,initial


def scalar_checks():
    sigma=Q(59,100); c0=Q(1,400000000); m=391
    epsilon=Q(2*m+5,9*6**m)
    ey=c0**3*sigma**(3*m+1)/Q(16*(m+3)**2)
    el=c0**2*sigma**(2*m+1)/Q(4*(m+3))
    ratio_y=6*sigma**3*Q((m+3)**2*(2*m+5),(m+4)**2*(2*m+7))
    ratio_l=6*sigma**2*Q((m+3)*(2*m+5),(m+4)*(2*m+7))
    lambda_ratio=Q(9*2**(3*m-2),96*Q(7**m-1,6))
    assert ey>=12*epsilon and el>=12*epsilon and epsilon<1
    assert min(ratio_y,ratio_l,lambda_ratio)>1
    assert 4352*sigma**16<1 and 6*c0*(Q(9,2)*sigma)**18<1
    return dict(threshold=m,EyH_over_12epsilon=str(ey/(12*epsilon)),
        EL_over_12epsilon=str(el/(12*epsilon)),EyH_ratio_next_lower=str(ratio_y),
        EL_ratio_next_lower=str(ratio_l),lambdaF_over_yB_bound=str(lambda_ratio))


def trace_identity_checks():
    """Symbolic proof of Section 2's perturbation formulas and lower bounds."""
    global DIM
    DIM=7
    h=[variable(j) for j in range(6)]; a=variable(6)
    perturb=[add(a,constant(4)),add(a,constant(2)),constant(2)]+[{}]*3
    b=[add(scale(v,3),c) for v,c in zip(h,perturb)]
    def delta(half,n):
        at=lambda k:half[abs(k)]
        return add(mul(at(n),at(n)),scale(mul(at(n-1),at(n+1)),-1),
                   scale(mul(at(n+1),at(n+1)),-1),mul(at(n),at(n+2)))
    expected=[
        add(mul(add(scale(a,6),constant(30)),h[0]),
            mul(add(scale(a,-12),constant(-24)),h[1]),
            mul(add(scale(a,3),constant(12)),h[2]),
            scale(mul(a,a),-1),scale(a,2),constant(16)),
        add(mul(add(scale(a,6),constant(12)),h[1]),scale(h[0],-6),
            mul(add(scale(a,-3),constant(-24)),h[2]),
            mul(add(scale(a,3),constant(6)),h[3]),mul(a,a),scale(a,2),constant(-8)),
        add(scale(h[2],12),mul(add(scale(a,-3),constant(-6)),h[3]),scale(h[4],6),constant(4)),
        scale(h[4],-6),
    ]
    for n in range(4): assert add(delta(b,n),scale(delta(h,n),-9))==expected[n]
    # Each term on the right is nonnegative under a in [1,5], h decreasing,
    # h >= 0, and h0 <= 2 h1. These are exact polynomial identities.
    difference=lambda aa,bb:add(aa,scale(bb,-1))
    bound_remainders=[
        add(mul(add(constant(30),scale(a,-6)),h[0]),
            mul(add(scale(a,12),constant(24)),difference(h[0],h[1])),
            mul(add(scale(a,3),constant(12)),h[2]),
            mul(add(constant(5),scale(a,-1)),add(a,constant(3)))),
        add(scale(difference(scale(h[1],2),h[0]),6),
            mul(add(scale(a,3),constant(24)),difference(h[1],h[2])),
            mul(add(scale(a,3),constant(-3)),h[1]),
            mul(add(scale(a,3),constant(6)),h[3]),
            mul(add(a,constant(-1)),add(a,constant(3)))),
        add(mul(add(scale(a,3),constant(6)),difference(h[2],h[3])),
            mul(add(constant(15),scale(a,-3)),h[2]),scale(h[4],6)),
        scale(difference(h[3],h[4]),6),
    ]
    corrections=[add(scale(h[0],24),constant(-1)),
                 add(scale(h[1],21),constant(5)),
                 add(scale(h[2],9),constant(-4)),scale(h[3],6)]
    for n in range(4): assert add(expected[n],corrections[n])==bound_remainders[n]
    # Quadratic lower bounds written at lambda=8+s, where s >= 0.
    quadratics=[(Q(9),Q(-123,2),Q(1)),(Q(9),Q(-105,2),Q(-5)),(Q(9),Q(-21),Q(4))]
    shifted=[]
    for qa,qb,qc in quadratics:
        coefficients=[64*qa+8*qb+qc,16*qa+qb,qa]
        assert min(coefficients)>0
        shifted.append(list(map(str,coefficients)))
    DIM=6
    return dict(status='PASS',defect_expansions=4,nonnegative_remainder_identities=4,
                quadratic_coefficients_at_lambda_8_plus_s=shifted,
                assumptions=['1 <= a <= 5','h0 >= h1 >= ... >= 0','h0 <= 2 h1',
                             'lambda >= 8','supported h_n >= 2 lambda',
                             'delta_n(h) >= lambda h_n'])


def main():
    start=time.monotonic(); ts=direct_prefixes(391)
    # Independent ordinary-x recurrence/binomial checks of full Laurent rows.
    crosscheck=[0,1,2,3,7,20,96,200,390,391]
    for m in crosscheck: assert ts[m]==binomial_laurent(ordinary_prefix(m))
    cases=[]
    for m in range(1,391):
        trace=[3*v for v in convolution([1,2,3,2,1],ts[m])]
        center=len(trace)//2
        trace[center]+=5; trace[center-1]+=2; trace[center+1]+=2
        A=ts[m+1]; B=ts[m-1]
        base=align_add(convolution(A,trace),B)
        slope=[-4*v for v in A]
        strength2=3*2**(2*m-2)
        for label,p,s in [('L',base,slope),('yL',convolution([1,1,1],base),[-4*v for v in convolution([1,1,1],A)])]:
            r=single_certificate(p,s,strength2); r.update(m=m,label=label); cases.append(r)
        if m<=3:
            r=single_certificate(convolution([1,1,1],trace),[-4,-4,-4],3*2**(m-1))
            r.update(m=m,label='yf'); cases.append(r)
        if m%30==0: print(json.dumps({'single_m_completed':m}),flush=True)
    rr,initial=residues(); scalars=scalar_checks(); trace_checks=trace_identity_checks()
    # This is the first access to the expected output certificates.
    finite_path=Path('fulltree_oneturn_single_finite_results.json')
    residue_path=Path('fulltree_oneturn_remaining_certificates.json')
    expected_single=json.loads(finite_path.read_text())
    expected_residue=json.loads(residue_path.read_text())
    assert expected_single['status']=='PASS'
    assert cases==expected_single['cases']
    assert rr==expected_residue['residues']
    assert initial==expected_residue['m1']
    assert scalars==expected_residue['scalar_checks']
    results=dict(status='PASS',arithmetic='Python arbitrary precision integers and exact fractions',
        author_code_imports=[],expected_output_loaded_after_recomputation=True,
        single_cases=len(cases),single_margins=sum(r['margins'] for r in cases),
        single_scope_m=[1,390],residue_boxes=len(rr),residue_powers=[1,3],
        residue_arrays=sum(len(v[k]) for v in rr.values() for k in ['y1','y3']),
        initial_arrays=sum(map(len,initial.values())),
        prefix_ordinary_binomial_crosscheck=crosscheck,
        residue_bounds={name:{k:[cc['lower_bound'] for cc in value[k]] for k in ['y1','y3']} for name,value in rr.items()},
        m1_bounds={k:[cc['lower_bound'] for cc in value] for k,value in initial.items()},
        scalar_checks=scalars,smoothed_trace_analytic_checks=trace_checks,full_arrays_match=True,
        input_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [finite_path,residue_path]},
        elapsed_seconds=round(time.monotonic()-start,3),
        scope_limit='Finite Bernstein boxes and scalar inequalities only; root-factor coverage and infinite-tail transfer are separate proof obligations.')
    Path('recovery_single_audit.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:v for k,v in results.items() if k not in ['residue_bounds','scalar_checks']},indent=2))


if __name__=='__main__': main()
