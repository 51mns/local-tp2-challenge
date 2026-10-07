"""Direct Laurent/symbolic audit; no author code or expected-data imports.
This is a second implementation by the same model, not a blind external audit.
"""
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import hashlib,json

# Full Laurent arithmetic, with q^-1 retained instead of a binomial H transform.
def plus(*ps):
    z={}
    for p in ps:
        for k,v in p.items():z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def times(p,q):
    z={}
    for i,v in p.items():
        for j,w in q.items():z[i+j]=z.get(i+j,0)+v*w
    return {k:v for k,v in z.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
I={0:1};xx={-1:1,1:1};yy=plus(xx,I);pp=plus(xx,{0:2})
def mutation(a,c,b):return plus(scale(times(times(yy,a),c),3),scale(times(xx,plus(a,c)),-1),scale(b,-1))
def canonical(word):
    a,c,b=I,plus({0:5},scale(xx,6),scale(times(xx,xx),2)),pp
    for ch in word:
        if ch=='L':a,c,b=a,mutation(a,c,b),c
        elif ch=='R':a,c,b=c,mutation(b,c,a),b
        else:raise ValueError(ch)
    return a,c,b
def divide(p):
    f=dict(p);q={};lower=min(p,default=0)+2
    while f and max(f)>=lower:
        i=max(f)-1;v=f[max(f)];q[i]=q.get(i,0)+v
        f=plus(f,scale({i-1:1,i:1,i+1:1},-v))
    assert not f
    assert all(q.get(-i,0)==v for i,v in q.items())
    return q
def deg(p):return max(p,default=0)
def half(p):return [p.get(n,0) for n in range(deg(p)+1)]
def dd(p,n):return p.get(n,0)**2-p.get(n-1,0)*p.get(n+1,0)-p.get(n+1,0)**2+p.get(n,0)*p.get(n+2,0)
def ww(p,q,n):return p.get(n,0)*q.get(n+1,0)-p.get(n+1,0)*q.get(n,0)

# Sparse ring with exponents (q-power, u-power, v-power).
# r=4u-2, s=4v-2. There are no interpolation nodes in this implementation.
def lift(p):return {(i,0,0):v for i,v in p.items()}
def aa(*ps):
    z={}
    for p in ps:
        for k,v in p.items():z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def ss(p,c):return {k:v*c for k,v in p.items() if v*c}
def mm(p,q):
    z={}
    for (a,b,c),v in p.items():
        for (d,e,f),w in q.items():
            k=(a+d,b+e,c+f);z[k]=z.get(k,0)+v*w
    return {k:v for k,v in z.items() if v}
def rowat(p,n):return {(0,j,k):v for (i,j,k),v in p.items() if i==abs(n)}
def sk(p,i,j):
    if i==0:return rowat(p,j)
    if j==0:return ss(rowat(p,i),2)
    return aa(rowat(p,i-j),rowat(p,i+j))
def minor(p,i,j):return aa(mm(sk(p,i,j),sk(p,i+1,j+1)),ss(mm(sk(p,i,j+1),sk(p,i+1,j)),-1))
def delta(p,n):
    a,b,c,d=(rowat(p,k) for k in (n-1,n,n+1,n+2))
    return aa(mm(b,b),ss(mm(a,c),-1),ss(mm(c,c),-1),mm(b,d))
def wedge(p,q,n):return aa(mm(rowat(p,n),rowat(q,n+1)),ss(mm(rowat(p,n+1),rowat(q,n)),-1))
def mass(p):
    out={}
    for (_,u,v),c in p.items():out[0,u,v]=out.get((0,u,v),0)+c
    return {k:v for k,v in out.items() if v}
def degree(p):return max((i for i,_,_ in p),default=0)
def bern(p,dim):
    assert all(i==0 and 0<=u<=2 and 0<=v<=2 and (dim==2 or v==0) for i,u,v in p)
    out=[]
    for ix in product(range(3),repeat=dim):
        i=ix[0];j=ix[1] if dim==2 else 0
        out.append(sum((F(c*comb(i,u)*comb(j,v),comb(2,u)*comb(2,v))
                        for (_,u,v),c in p.items() if u<=i and v<=j),F(0)))
    return out

def run(word,direction):
    X,C,Y=canonical(word)
    if direction=='R':X,Y=Y,X
    t=plus(scale(times(yy,X),3),scale(xx,-1))
    T=plus(times(t,Y),scale(times(xx,X),-1),scale(C,-1))
    A=divide(plus(C,scale(Y,-1)));B=divide(plus(T,scale(Y,-1)))
    sign=1 if all(c>=0 for c in B.values()) else -1
    assert all(sign*c>=0 for c in B.values());Q=scale(B,sign)
    P=times(pp,X);J=times(yy,plus(t,{0:-2}));V=scale(times(times(yy,yy),P),3)
    M0=plus(scale(times(yy,Y),3),scale(xx,-1),I);K=times(P,M0)
    q0=times(yy,A);q1=times(yy,plus(times(t,A),B));beta=times(yy,plus(A,B));E1=plus(C,scale(X,-1))
    r=dict(X=X,Y=Y,C=C,A=A,P=P,J=J,V=V,M0=M0,K=K,q0=q0,q1=q1,beta=beta,E1=E1)
    arrays={}
    def put(name,vals,strict=True):
        vals=list(map(F,vals));assert vals and (min(vals)>0 if strict else min(vals)>=0),(name,min(vals))
        arrays[name]=vals
    for name,poly in r.items():put('support_'+name,half(poly))
    put('abs_B_le_A',half(plus(A,scale(Q,-1))),False)
    put('Q_nonnegative',half(Q),False)
    for name,poly in [('A',A),('yA',times(yy,A))]:put(name+'_delta',[dd(poly,n) for n in range(deg(poly)+1)])
    for lo,hi in [('q0','q1'),('beta','q1'),('P','E1'),('P','q1')]:
        put('initial_'+lo+'_'+hi,[ww(r[lo],r[hi],n) for n in range(deg(r[lo])+1)],False)
    put('proxy_J_V',[ww(J,V,n) for n in range(deg(J)+1)])
    a,b=deg(X),deg(Y)
    assert a>=1 and deg(C)==a+b+1 and deg(t)==a+1 and deg(A)==a+b and deg(B)<deg(A)+a+1
    assert sum(t.values())>=6
    f=aa(lift(plus(t,{0:2})),{(0,1,0):-4})
    fs=aa(lift(plus(t,{0:2})),{(0,0,1):-4})
    L=aa(mm(lift(A),f),lift(B));Ls=aa(mm(lift(A),fs),lift(B))
    sy=lift(yy);sy2=mm(sy,sy)
    for name,poly,defect in [('f_support',f,False),('f_delta',f,True),('L_support',L,False),
                             ('L_delta',L,True),('yL_support',mm(sy,L),False),('yL_delta',mm(sy,L),True)]:
        put(name,[c for n in range(degree(poly)+1) for c in bern(delta(poly,n) if defect else rowat(poly,n),1)])
    gamma=F(2);channels=deg(K)+1
    for j in range(channels):
        put('channel_'+str(j),bern(aa(*(minor(f,i,j) for i in range(channels)),ss(mass(f),-gamma)),1),False)
    Lmass=bern(mass(L),1);put('L_mass',Lmass)
    proxy_diag=[c for n in range(channels) for c in bern(wedge(mm(lift(J),L),mm(lift(V),L),n),1)]
    multi_diag=[c for n in range(channels) for c in bern(delta(mm(sy2,L),n),1)]
    put('proxy_diagonal',proxy_diag);put('multiplier_diagonal',multi_diag)
    E=mm(L,fs);G=mm(Ls,f);mid=ss(aa(E,G),F(1,2))
    for label,smooth in [('midpoint',lift(I)),('midpoint_y',sy)]:
        poly=mm(smooth,mid);qr=mm(smooth,lift(Q))
        # qr has no parameter dependence.
        bound=8*max((v for (i,_,_),v in qr.items() if i>=0),default=0)
        size=degree(poly)+1
        put(label+'_strength',[c for n in range(size) for c in bern(aa(delta(poly,n),ss(rowat(poly,n),-bound)),2)])
        put(label+'_domination',[c for n in range(size) for c in bern(aa(rowat(poly,n),ss(rowat(qr,n),-1)),2)],False)
        put(label+'_support',[c for n in range(size) for c in bern(rowat(poly,n),2)])
    denom=bern(ss(aa(mass(E),mass(G)),gamma),2);put('mixed_mass',denom)
    jE,jG,vE,vG=(mm(lift(a),b) for a,b in [(J,E),(J,G),(V,E),(V,G)])
    yE,yG=mm(sy2,E),mm(sy2,G)
    px=[c for n in range(channels) for c in bern(aa(wedge(jE,vG,n),wedge(jG,vE,n)),2)]
    mx=[c for n in range(channels) for c in bern(aa(delta(aa(yE,yG),n),ss(delta(yE,n),-1),ss(delta(yG,n),-1)),2)]
    put('proxy_mixed',px);put('multiplier_mixed',mx)
    cp=min([v/Lmass[i%3] for i,v in enumerate(proxy_diag)]+[v/denom[i%9] for i,v in enumerate(px)])
    cm=min([v/Lmass[i%3] for i,v in enumerate(multi_diag)]+[v/denom[i%9] for i,v in enumerate(mx)])
    for name,vals,bound,ds in [('proxy_normalized_margin',proxy_diag,cp,Lmass),('multiplier_normalized_margin',multi_diag,cm,Lmass),
                             ('proxy_mixed_normalized_margin',px,cp,denom),('multiplier_mixed_normalized_margin',mx,cm,denom)]:
        put(name,[v-bound*ds[i%len(ds)] for i,v in enumerate(vals)],False)
    z1=sum(plus(times(A,plus(t,I)),B).values())
    proxy_budget=sum(J.values())*max(K.values())
    mult_budget=max(27*(M0.get(n-1,0)+3*M0.get(n+1,0))+F(max(-dd(M0,n),0),z1) for n in range(deg(M0)+2))
    N0=1
    while cp*gamma**(N0-1)<=proxy_budget or 9*cm*gamma**(N0-1)<=mult_budget:
        N0+=1;assert N0<=100
    put('final_proxy_budget',[cp*gamma**(N0-1)-proxy_budget])
    put('final_multiplier_budget',[9*cm*gamma**(N0-1)-mult_budget])
    for N in range(N0):
        X0,C0,Y0=canonical(word+direction*N)
        U,V0=sorted((mutation(X0,C0,Y0),mutation(Y0,C0,X0)),key=deg)
        S=plus(U,scale(C0,-1));D=plus(V0,scale(U,-1))
        put('transient_target_'+str(N),[ww(S,D,n) for n in range(deg(S)+1)])
    encoded={name:[str(v) for v in vals] for name,vals in arrays.items()}
    digest=hashlib.sha256(json.dumps(encoded,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return dict(summary=dict(status='PASS',word=word,direction=direction,channels=channels,gamma=str(gamma),
                             c_proxy=str(cp),c_multiplier=str(cm),tail_starts=N0,
                             proxy_budget=str(proxy_budget),multiplier_budget=str(mult_budget),
                             coefficient_count=sum(map(len,arrays.values())),all_array_sha256=digest),arrays=encoded)

if __name__=='__main__':
    out=Path(__file__).resolve().parent/'generated';out.mkdir(exist_ok=True)
    for word,direction in [('', 'R'),('LRL','R')]:
        z=run(word,direction)
        (out/f'verifier_{word or "root"}_{direction}.json').write_text(json.dumps(z,sort_keys=True,indent=2)+'\n')
        print(json.dumps(z['summary'],sort_keys=True))
