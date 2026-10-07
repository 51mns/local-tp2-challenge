#!/usr/bin/env python3
"""Exact canonical selective-row probes. Parent arithmetic import disclosed.
A bounded pass is not a closure proof.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
import continuation_network as p

def get(h,n):return h[abs(n)] if abs(n)<len(h) else 0

def defects(h):
 return [get(h,n)**2-get(h,n-1)*get(h,n+1)-get(h,n+1)**2+get(h,n)*get(h,n+2) for n in range(len(h))]

def wedge(h,k):
 return [get(h,n)*get(k,n+1)-get(h,n+1)*get(k,n) for n in range(max(len(h),len(k))-1)]

def rows(Q):
 G,s,d=Q[0][0],Q[1][0],Q[1][1]
 r=p.sub(G,s);t=p.sub(p.mul([3,3],G),[0,1])
 return dict(G=G,s=s,r=r,d=d,u=p.sub(t,s),v=p.add(t,r))

def violations(Q):
 z=rows(Q);h={k:p.H(v) for k,v in z.items()};out={}
 for k in ['s','r','u','v']:
  ds=defects(h[k])
  bad=next(((n,x) for n,x in enumerate(ds) if x<0),None)
  if bad:out['cone_'+k]={'index':bad[0],'minor':bad[1],'poly':z[k],'halfrow':h[k]}
 for a,b in [('s','r'),('v','u')]:
  w=wedge(h[a],h[b]);bad=next(((n,x) for n,x in enumerate(w) if x<0),None)
  if bad:out[a+'_lr_'+b]={'index':bad[0],'minor':bad[1],'poly_a':z[a],'poly_b':z[b],'halfrow_a':h[a],'halfrow_b':h[b]}
 return out

def run(depth=5):
 queue=[(p.A0,p.medi(p.A0,p.B0),p.B0,'')];first={};count=0;maxdeg=0
 for a,c,b,path in queue:
  count+=1;maxdeg=max(maxdeg,len(c[0][0])-1)
  bad=violations(c)
  for k,v in bad.items():
   if k not in first:first[k]={'path':path,'Q':c,**v}
  if len(path)<depth:
   queue.extend([(a,p.medi(a,c),c,path+'L'),(c,p.medi(c,b),b,path+'R')])
 return dict(nodes=count,maxdepth=depth,maxdegree=maxdeg,first_violations=first,root_rows=rows(queue[0][1]),root_violations=violations(queue[0][1]),scope='bounded evidence only',imports=['../continuation_network.py: exact polynomial/matrix arithmetic and Fourier transform'])

if __name__=='__main__':
 z=run(int(sys.argv[1]) if len(sys.argv)>1 else 5)
 target=Path(__file__).with_name('network_probe_results.json');target.write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))
