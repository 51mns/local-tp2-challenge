#!/usr/bin/env python3
"""Exact exploration of normalized canonical state; bounded checks are not proofs."""
from __future__ import annotations
import sys,json,random,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tp2_source import *
y=[1,1]; y2=mul(y,y); z=[3,2]
def normalized(rec):
 X,Y=sorted([rec['A'],rec['B']],key=len)
 a=divide_x_plus_one(sub(X,[1])) if X!=[1] else [0]
 e=divide_x_plus_one(sub(Y,X));g=divide_x_plus_one(sub(rec['C'],Y))
 t=add(z,scale(mul(y2,a),3)); k=mul(X,sub(scale(X,3),[2])); r=sub(sub(g,mul(sub(t,[2]),e)),k)
 return a,e,g,r

def build(a,e,r):
 X=add([1],mul(y,a));t=add(z,scale(mul(y2,a),3));k=mul(X,sub(scale(X,3),[2]));g=add(add(mul(sub(t,[2]),e),k),r)
 ss=sub(mul(t,g),r);M=add(add(t,[1]),scale(mul(y2,add(e,g)),3));d=mul(e,M)
 return X,t,k,g,ss,d

def defects(p):
 h=H(p)
 return [hget(h,n)**2-hget(h,abs(n-1))*hget(h,n+1)-hget(h,n+1)**2+hget(h,n)*hget(h,n+2) for n in range(len(h))]

def cone(p):return min(defects(p))>=0

def lr(p,q):return min(f_values(p,q))>=0

def cross(p,q):
 d,d1,d2=defects(add(p,q)),defects(p),defects(q)
 return [v-hget(d1,n)-hget(d2,n) for n,v in enumerate(d)]

def treecheck(depth):
 fails={};count=0;maxdeg=0;firstcross={}
 for rec in generate_tree(depth):
  a,e,g,r=normalized(rec);X,t,k,gg,ss,d=build(a,e,r)
  assert gg==g and ss==rec['P'] and d==rec['Q']
  assert min(a+e+g+r)>=0
  assert min(sub(add(a,e),r))>=0
  assert mul(r,g)==add(add(mul(sub(t,[2]),mul(e,e)),scale(mul(k,e),2)),scale(mul(a,mul(X,X)),3))
  polys={'a':a,'e':e,'g':g,'r':r,'s':ss,'d':d}
  for name,p in polys.items():
   if not cone(p):fails.setdefault('cone_'+name,{'path':rec['path'],'defects':defects(p)})
  for ni,nj in [('a','e'),('e','g'),('g','s'),('s','d')]:
   if not lr(polys[ni],polys[nj]):fails.setdefault('lr_'+ni+'_'+nj,{'path':rec['path'],'minors':f_values(polys[ni],polys[nj])})
  for ni,nj in [('a','e'),('e','g')]:
   vals=cross(polys[ni],polys[nj])
   if min(vals)<0:firstcross.setdefault(ni+'_'+nj,{'path':rec['path'],'index':vals.index(min(vals)),'value':min(vals),'p':polys[ni],'q':polys[nj]})
  count+=1;maxdeg=max(maxdeg,len(ss)-1)
 return {'scope':'finite exact scan, not a proof','nodes':count,'max_short_quotient_degree':maxdeg,'fails':fails,'polarized_obstructions':firstcross}

def randomcheck(count,seed=803):
 rng=random.Random(seed);candidate_count=0
 for _ in range(count):
  da=rng.randrange(0,3);de=rng.randrange(max(1,da),5)
  a=[rng.randrange(1,20) for _ in range(da+1)];e=[rng.randrange(1,40) for _ in range(de+1)]
  upper=add(a,e);r=[rng.randrange(c+1) for c in upper]
  if not any(r):continue
  if not all(cone(p) for p in [a,e,r,add(a,e)]) or not lr(a,e):continue
  X,t,k,g,ss,d=build(a,e,r)
  if not all(cone(p) for p in [g,ss,d,add(a,add(e,g)),add(e,g)]) or not all(lr(p,q) for p,q in [(e,g),(g,ss),(ss,d)]):continue
  candidate_count+=1
  for action,na,ne,nr in [('short',a,add(e,g),g),('long',add(a,e),g,add(e,g))]:
   _,_,_,ng,ns,nd=build(na,ne,nr)
   pset={'a':na,'e':ne,'r':nr,'g':ng,'s':ns,'d':nd,'a+e':add(na,ne),'e+g':add(ne,ng),'a+e+g':add(na,add(ne,ng))}
   bad={name:defects(p) for name,p in pset.items() if not cone(p)}
   badlr={u+'_'+v:f_values(pset[u],pset[v]) for u,v in [('a','e'),('e','g'),('g','s'),('s','d')] if not lr(pset[u],pset[v])}
   if bad or badlr:
    return {'candidate_count':candidate_count,'a':a,'e':e,'r':r,'g':g,'s':ss,'d':d,'action':action,'badcone':bad,'badlr':badlr,'fricke':sub(mul(r,g),add(add(mul(sub(t,[2]),mul(e,e)),scale(mul(k,e),2)),scale(mul(a,mul(X,X)),3)))}
 return {'candidate_count':candidate_count,'obstruction':None,'trials':count}
if __name__=='__main__':
 result=treecheck(int(sys.argv[1]) if len(sys.argv)>1 else 7)
 if '--random' in sys.argv:result['random']=randomcheck(50000)
 print(json.dumps(result,indent=2))
