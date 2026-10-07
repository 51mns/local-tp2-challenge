"""Six finite bases for an all-left Local TP2 proof; exact original recurrence."""
from math import comb
import json


def add(a,b):
    out=[(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
    while len(out)>1 and out[-1]==0:out.pop()
    return out


def scale(a,c):return [v*c for v in a]


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def child(a,c,b):
    return add(add(mul([3,3],mul(a,c)),scale(mul([0,1],add(a,c)),-1)),scale(b,-1))


def halfrow(poly):
    return [sum(poly[j]*comb(j,(j-n)//2) for j in range(n,len(poly),2)) for n in range(len(poly))]


def direct_row(poly):
    out={};power={0:1}
    for coeff in poly:
        for n,v in power.items():out[n]=out.get(n,0)+coeff*v
        nxt={}
        for n,v in power.items():
            nxt[n-1]=nxt.get(n-1,0)+v
            nxt[n+1]=nxt.get(n+1,0)+v
        power=nxt
    return [out.get(n,0) for n in range(len(poly))]


def main():
    a,c,b=[1],[5,6,2],[2,1]
    rows=[]
    for k in range(6):
        low=child(a,c,b);high=child(b,c,a)
        s=add(low,scale(c,-1));d=add(high,scale(low,-1))
        hs,hd=halfrow(s),halfrow(d)
        assert hs==direct_row(s) and hd==direct_row(d)
        vals=[hs[n]*hd[n+1]-(hs[n+1] if n+1<len(hs) else 0)*hd[n] for n in range(len(hs))]
        assert all(v>0 for v in vals)
        rows.append({'k':k,'path':'L'*k,'S':s,'D':d,'H_S':hs,'H_D':hd,'F':vals})
        a,c,b=a,low,c
    print(json.dumps({'scope':'finite bases k=0,...,5 only; infinite step requires separate proof','minors_verified':sum(len(r['F']) for r in rows),'rows':rows},indent=2))


if __name__=='__main__':main()
