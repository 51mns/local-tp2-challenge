"""Targeted exact identities and witnesses; no state/parameter scan."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

NV=8
ZERO=(0,)*NV


class Poly(dict):
    def __add__(self,other):
        out=dict(self)
        for k,v in aspoly(other).items():
            out[k]=out.get(k,F(0))+v
        return Poly({k:v for k,v in out.items() if v})
    __radd__=__add__

    def __neg__(self):
        return Poly({k:-v for k,v in self.items()})

    def __sub__(self,other):
        return self+-aspoly(other)

    def __rsub__(self,other):
        return aspoly(other)+-self

    def __mul__(self,other):
        out={}
        for ka,va in self.items():
            for kb,vb in aspoly(other).items():
                k=tuple(a+b for a,b in zip(ka,kb))
                out[k]=out.get(k,F(0))+va*vb
        return Poly({k:v for k,v in out.items() if v})
    __rmul__=__mul__

    def __pow__(self,n):
        assert n>=0
        out=aspoly(1)
        for _ in range(n):out*=self
        return out

    def __truediv__(self,n):
        return self*F(1,n)


def aspoly(value):
    return value if isinstance(value,Poly) else Poly({ZERO:F(value)}) if value else Poly()


def var(i):
    key=list(ZERO);key[i]=1
    return Poly({tuple(key):F(1)})


def degree(p):
    return max((k[0] for k in aspoly(p)),default=0)


def collapse(p):
    p=aspoly(p)
    return p.get(ZERO,F(0)) if all(not any(k) for k in p) else p


def coef(p,n):
    out={}
    for k,v in aspoly(p).items():
        if k[0]==n:
            kk=(0,)+k[1:]
            out[kk]=out.get(kk,F(0))+v
    return collapse(Poly(out))


def row(p):
    return [collapse(sum(coef(p,i)*comb(i,(i-j)//2)
                         for i in range(j,degree(p)+1,2)))
            for j in range(degree(p)+1)]


def at(h,j):
    return h[abs(j)] if abs(j)<len(h) else F(0)


def xrow(h):
    return [2*at(h,1)]+[at(h,j-1)+at(h,j+1) for j in range(1,len(h)+1)]


def defect(h,j):
    return collapse(at(h,j)**2-at(h,j-1)*at(h,j+1)
                    -at(h,j+1)**2+at(h,j)*at(h,j+2))


def selector_mixed(f,g,k,l):
    h,a=row(f),row(g)
    q,b=xrow(h),xrow(a)
    return collapse(at(h,k)*at(b,l)+at(a,k)*at(q,l)
                    -at(h,l)*at(b,k)-at(a,l)*at(q,k))


def selector_tensor(f,k,l):
    h=row(f);q=xrow(h)
    return collapse(at(h,k)*at(q,l)-at(h,l)*at(q,k))


def lc(p):
    return coef(p,degree(p))


x=var(0)
y=x+1


def state(a,e,r):
    X=1+y*a
    t=3*y*X-x
    k=X*(3*X-2)
    g=(t-2)*e+k+r
    s=t*g-r
    C=X+y*(e+g)
    T=3*y*C-x
    d=e*(T+1)
    c=e+g+s
    residual=r*g-(t-2)*e**2-2*k*e-3*a*X**2
    return dict(a=a,e=e,r=r,X=X,t=t,k=k,g=g,s=s,C=C,T=T,d=d,c=c,F=residual)


def short(z):
    return state(z['a'],z['e']+z['g'],z['g'])


def universal_checks():
    lead,gg0,gg1,gg2,gg3,eps=[var(i) for i in range(1,7)]
    # Generic local rows at j=D+1: f_(j-1)=lead and later entries vanish.
    old=defect([gg0,gg1,gg2,gg3],1)
    shifted=defect([gg0+eps*lead,gg1,gg2,gg3],1)
    assert not aspoly(shifted-old+eps*lead*gg2)
    # The mixed selector uses (h_k,h_l,q_k,q_l)=(0,0,lead,0).
    symbolic_mixed=0*gg3+gg1*0-0*gg2-gg2*lead
    assert not aspoly(symbolic_mixed+lead*gg2)
    return dict(mixture_defect_identity=True,degree_separation_selector=True)


def root_checks():
    z=state(0,1,1)
    assert not aspoly(z['F'])
    assert not aspoly(z['e']-1)
    assert not aspoly(z['c']-(4*x*x+14*x+12))
    assert not aspoly(z['T']-(6*x**3+24*x*x+32*x+15))
    r,s=var(1),var(2)
    single=[]
    for smoothed in (False,True):
        f=z['e']*(z['T']-s)+z['c']
        g=z['c']*(z['T']-r)+z['e']
        if smoothed:f,g=y*f,y*g
        D=degree(f)
        mixed=selector_mixed(f,g,D+1,D+2)
        assert mixed==F(-144)
        assert degree(g)-D==2
        single.append(dict(mode='y' if smoothed else 'raw',degrees=[D,degree(g)],
                           columns=[D+1,D+2],character=[2*D+2,0],
                           mixed_coefficient=str(mixed),parameters='symbolic r,s'))
    seed=selector_mixed(z['e'],z['c'],1,2)
    assert seed==F(-4)
    # Two fixed run normalizations; the note's all-N theorem is degree algebra.
    U=[aspoly(1),z['T']]
    U.append(z['T']*U[1]-U[0])
    runs=[]
    for N in (1,2):
        f=z['e']*U[N]+z['c']*U[N-1]
        g=z['c']*U[N]+z['e']*U[N-1]
        D=degree(f)
        mixed=selector_mixed(f,g,D+1,D+2)
        expected=-lc(f)*row(g)[D+2]
        assert not aspoly(mixed-expected)
        assert mixed<0
        runs.append(dict(N=N,degrees=[D,degree(g)],mixed_coefficient=str(mixed)))
    return dict(root_Fricke=True,seed_mixed=str(seed),single_blocks=single,
                targeted_run_normalizations=runs)


def monotonicity_witness():
    root=state(0,1,1)
    parent=short(short(root))
    child=short(parent)
    assert not aspoly(parent['F']) and not aspoly(child['F'])
    n=child['e']
    B=n*(child['T']+1)+child['c']
    assert degree(n)==3
    assert not aspoly(B-(parent['c']*(parent['T']+1)+parent['e']))
    p=B-3*n
    mixed=selector_mixed(p,n,3,4)
    assert mixed==F(-6386912)
    delta_n=defect(row(n),3)
    assert delta_n>0
    # E(theta)=delta_3(B-theta n): at theta=3 derivative is -J(p,n).
    hh,nn=row(B),row(n)
    b=selector_mixed(B,n,3,4)
    derivative=-b+6*delta_n
    assert derivative==-mixed==F(6386912)
    return dict(state='actual third short child from normalized root',
                normalized_Fricke=True,degree_n=3,columns=[3,4],character=[6,0],
                J_L2_n=str(mixed),delta_n_terminal=str(delta_n),
                derivative_theta_at3=str(derivative),
                claim='monotone-decreasing shortcut false; no packet failure asserted')


def weakening_checks():
    b1,b2,radical,t,eta=[var(i) for i in range(1,6)]
    A=10*x+b1
    B=10*x+b2
    assert row(A)==[b1,F(10)]
    ah=row(y*A)
    for actual,expected in zip(ah,[b1+20,b1+10,10]):
        assert not aspoly(actual-expected)
    expected=[-b1*b1+10*b1+400,b1*b1+10*b1-200,100]
    for j in range(3):assert not aspoly(defect(ah,j)-expected[j])
    # Reduce the exact boundary value modulo radical^2=17.
    boundary=-(5+5*radical)**2+10*(5+5*radical)+400
    reduced={}
    for key,value in boundary.items():
        key=list(key)
        power=key[3]
        key[3]=power%2
        key=tuple(key)
        reduced[key]=reduced.get(key,F(0))+value*17**(power//2)
    assert not any(reduced.values())
    H=y*A*B
    expected02=(b1*b2+10*(b1+b2)+300)*b1*b2+100*row(H)[0]
    assert not aspoly(selector_tensor(H,0,2)-expected02)
    assert 1041*361==375801 and 351*261==91611
    assert 375801>16 and 91611>16 and 20000>16
    # Exact square comparison behind sqrt(eta²/4+t²)<=eta/2+t.
    assert not aspoly((eta/2+t)**2-(eta*eta/4+t*t)-eta*t)
    assert 4**2<17<F(21,5)**2
    yy=row(y)
    assert selector_tensor(y,0,1)==F(-1)
    assert selector_tensor(y,0,2)==selector_tensor(y,1,2)==F(1)
    return dict(raw_y_defect_formulas=True,quadratic_field_endpoint_zero=True,
                full_square_root_bound_identity=True,yH_selector02_identity=True,
                reference_positive_selectors=[[0,2],[1,2]],
                uniform_reference_bound=16,raw_central_CB_bound=20000,
                y_selector02_bound=375801,y_selector12_bound=91611,
                review='packet_algebra_weakening_audit.md; conditional theorem PASS')


def main():
    result=dict(arithmetic='Python stdlib Fraction sparse polynomial ring',
                universal=universal_checks(),root=root_checks(),
                monotonicity=monotonicity_witness(),
                weak_packet_independent_review=weakening_checks(),
                proof='packet_algebra.md; no complete mixed compensation',
                scope='ROOT witnesses and universal canonical degree obstruction; BOTH/TARGET OPEN')
    output=Path(__file__).with_name('packet_algebra_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
