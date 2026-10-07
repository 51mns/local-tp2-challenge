"""Bounded adversarial checks of the proposed first-difference invariant.

Targets a declared list of mixed rays; this is NOT a global proof/search.
The canonical recurrence is imported from the frozen local extraction.
"""
from fractions import Fraction
import json
from math import comb
import canonical_arithmetic as t


def state(path):
    a,c,b=t.G0,t.G12,t.G1
    for side in path:
        if side=='L':a,c,b=a,t.mutation_left(a,c,b),c
        else:a,c,b=c,t.mutation_right(a,c,b),b
    low=t.mutation_left(a,c,b);high=t.mutation_right(a,c,b)
    if len(low)>len(high):low,high=high,low
    x,y=(a,b) if len(a)<len(b) else (b,a)
    E=t.sub(y,x);M=t.add(t.sub(t.scale(t.mul([1,1],c),3),[0,1]),[1])
    A=t.mul([2,1],x)
    return {'C':c,'M':M,'A':A,'E':E,'S':t.sub(low,c),'D':t.sub(high,low),'AM':t.mul(A,M)}


def alpha(poly):
    h=t.H(poly)
    return h,[h[n]-(h[n+1] if n+1<len(h) else 0) for n in range(len(h))]


def exact_abstract_obstruction():
    """Polynomial identities in lambda, not interpolation or sampling.

    Each entry below is itself a low-to-high polynomial in lambda.
    This family is explicitly NOT asserted to be a canonical center.
    """
    zero=[0]
    def entry(row,n):
        return row[abs(n)] if abs(n)<len(row) else zero
    def first_differences(row):
        return [t.sub(entry(row,n),entry(row,n+1)) for n in range(len(row))]
    def tau(row):
        g=first_differences(row)
        return [t.sub(t.mul(entry(g,n),t.sub(entry(row,n),entry(row,n+3))),
                      t.mul(entry(g,n+1),t.sub(entry(row,n-1),entry(row,n+2))))
                for n in range(len(row))]
    def folded_defects(row):
        delta=[t.sub(t.mul(entry(row,n),entry(row,n)),
                     t.mul(entry(row,n-1),entry(row,n+1)))
               for n in range(len(row)+1)]
        return [t.sub(delta[n],delta[n+1]) for n in range(len(row))]
    def fourier_over_lambda(ordinary):
        out=[]
        for n in range(len(ordinary)):
            value=zero
            for j in range(n,len(ordinary),2):
                value=t.add(value,t.scale(ordinary[j],comb(j,(j-n)//2)))
            out.append(value)
        return out
    ordinary_c=[[1,5],[0,8],[0,3]]
    ordinary_yc=[t.add(ordinary_c[n] if n<len(ordinary_c) else zero,
                       ordinary_c[n-1] if n>0 else zero)
                 for n in range(len(ordinary_c)+1)]
    ordinary_m=[t.scale(coefficient,3) for coefficient in ordinary_yc]
    ordinary_m[0]=t.add(ordinary_m[0],[1])
    ordinary_m[1]=t.sub(ordinary_m[1],[1])
    hc=[[1,11],[0,8],[0,3]]
    hyc=[[1,27],[1,22],[0,11],[0,3]]
    hm=[[4,81],[2,66],[0,33],[0,9]]
    assert fourier_over_lambda(ordinary_c)==hc
    assert fourier_over_lambda(ordinary_yc)==hyc
    assert fourier_over_lambda(ordinary_m)==hm
    assert t.add(t.sub(ordinary_c[0],ordinary_c[1]),ordinary_c[2])==[1]
    assert first_differences(hc)==[[1,3],[0,5],[0,3]]
    assert tau(hc)==[[1,14,8],[0,-3,7],[0,0,9]]
    assert folded_defects(hc)==[[1,25,26],[0,-3,22],[0,0,9]]
    assert folded_defects(hyc)[0]==[-1,-23,58]
    assert [t.sub(d,t.scale(h,2)) for d,h in zip(folded_defects(hc),hc)]==[
        [-1,3,26],[0,-19,22],[0,-6,9]]
    assert tau(hm)==[[4,72,-9],[4,102,450],[0,-18,198],[0,0,81]]
    assert t.sub(folded_defects(hc)[0],t.add(hc[0],hc[1]))==[0,6,26]
    lam=9
    C=[5*lam+1,8*lam,3*lam]
    M=t.add(t.sub(t.scale(t.mul([1,1],C),3),[0,1]),[1])
    assert t.eval_poly(C,-1)==1
    assert t.H(C)==[t.eval_poly(h,lam) for h in hc]
    assert t.H(M)==[t.eval_poly(h,lam) for h in hm]
    example={
        'lambda':lam,'C':C,'H_C':t.H(C),'alpha_C':alpha(C)[1],
        'J_C_top_adjacent_minors':[t.eval_poly(p,lam) for p in tau(hc)],
        'M':M,'H_M':t.H(M),'alpha_M':alpha(M)[1],
        'J_M_top_adjacent_minors':[t.eval_poly(p,lam) for p in tau(hm)]}
    assert example['J_M_top_adjacent_minors'][0]==-77
    return {
        'scope':'abstract normalized positive family; NOT a canonical counterexample',
        'family':'C_lambda=3 lambda x^2+8 lambda x+5 lambda+1, integer lambda>=1',
        'identities':'verified exactly in the polynomial ring Z[lambda]',
        'tau_C_coefficients_low_to_high':tau(hc),
        'folded_defect_C_coefficients_low_to_high':folded_defects(hc),
        'central_folded_defect_yC_coefficients_low_to_high':folded_defects(hyc)[0],
        'tau_M_coefficients_low_to_high':tau(hm),
        'failure':'J_M(0,1;0,1)=-9 lambda^2+72 lambda+4<0 for every lambda>=9',
        'example':example}


def main():
    paths=[]
    for prefix,side,limit in [('L','R',30),('R','L',30),('LL','R',20),('RR','L',20),('LR','L',12),('RL','R',12)]:
        paths.extend(prefix+side*k for k in range(1,limit+1))
    paths.extend(word*k for word in ('LR','RL') for k in range(2,5))
    paths=list(dict.fromkeys(paths))
    minima={};failures=[];maxdegree=0
    def check(label,path,n,left,right):
        value=left-right
        if value<0:failures.append({'condition':label,'path':path,'index':n,'left':str(left),'right':str(right),'difference':str(value)})
        norm=Fraction(value,left+right) if left+right>0 else Fraction(value)
        if label not in minima or norm<minima[label][0]:minima[label]=(norm,path,n,value)
    for path in paths:
        rec=state(path);rows={name:alpha(poly) for name,poly in rec.items()}
        maxdegree=max(maxdegree,max(len(poly)-1 for poly in rec.values()))
        for name in ('C','M','A','E','S','D','AM'):
            h,g=rows[name]
            for n,value in enumerate(g):
                if value<=0:failures.append({'condition':'positive alpha_'+name,'path':path,'index':n,'value':str(value)})
        for name in ('C','M'):
            h,g=rows[name];get=lambda n:t.hget(h,abs(n))
            for n in range(len(h)):
                left=g[n]*(get(n)-get(n+3))
                right=(g[n+1] if n+1<len(g) else 0)*(get(n-1)-get(n+2))
                check('J_'+name,path,n,left,right)
        for label,lower,upper in [('alpha_A_to_E','A','E'),('alpha_S_to_AM','S','AM'),('alpha_S_to_D','S','D')]:
            g=rows[lower][1];h=rows[upper][1]
            for n in range(len(g)):
                check(label,path,n,t.hget(g,n)*t.hget(h,n+1),t.hget(g,n+1)*t.hget(h,n))
        if failures:break
    report={'scope':'declared bounded mixed-ray stress cases only; no global conclusion',
            'declared_paths':len(paths),'last_path':path,'maximum_polynomial_degree':maxdegree,
            'failures':failures,
            'smallest_relative_margins':{name:{'path':entry[1],'index':entry[2],
                                               'relative_margin_float':float(entry[0]),
                                               'exact_difference':str(entry[3])}
                                         for name,entry in minima.items()}}
    report['exact_abstract_obstruction']=exact_abstract_obstruction()
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
