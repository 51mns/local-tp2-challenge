#!/usr/bin/env python3
"""Bounded all-ordered-kernel-minor comparisons at frozen actual states."""
import argparse,json,itertools
from pathlib import Path
from falsification_probe import *
from falsification_targeted import state

def K(h,i,j):
    if i==0:return get(h,j)
    if j==0:return 2*get(h,i)
    return get(h,abs(i-j))+get(h,i+j)
def det(h,i,j,k,l):return K(h,i,k)*K(h,j,l)-K(h,i,l)*K(h,j,k)
def one(path,sm):
    v=state(path);p=mul(y,v['s']) if sm else v['s'];q=mul(y,v['r']) if sm else v['r'];h,b=H(p),H(q)
    cutoff=len(h)+1 # rows and columns 0 through deg(h)+2 inclusive
    pairs=list(itertools.combinations(range(cutoff+1),2)); count=0;positive=0;minpos=None;first=None
    for i,j in pairs:
        for k,l in pairs:
            dh,db=det(h,i,j,k,l),det(b,i,j,k,l);count+=1
            margin=dh-4*db
            if margin<0 and first is None:first={'indices':[i,j,k,l],'h_det':dh,'b_det':db,'margin':margin,'h':p,'b':q,'rows':[h,b]}
            if db>0:
                positive+=1
                if minpos is None or margin<minpos['margin']:minpos={'indices':[i,j,k,l],'h_det':dh,'b_det':db,'margin':margin}
    # Any violation is valid globally. A finite pass remains finite.
    return {'path':path,'smooth':sm,'degree_h':len(h)-1,'index_range':[0,cutoff],
        'minors':count,'positive_reference_minors':positive,'minimum_over_positive_reference':minpos,'first_failure':first}
def main():
    paths=[''.join(w) for n in range(5) for w in itertools.product('sl',repeat=n)]
    paths+=['s'*n for n in range(5,13)]+['l'+'s'*n for n in range(4,9)]
    paths=list(dict.fromkeys(paths));records=[one(p,sm) for p in paths for sm in (False,True)]
    return {'scope':'44 actual states; all ordered 2x2 minors with row/column indices 0..deg(h)+2; no infinite-kernel inference',
      'formulas':'K(0,j)=h_j, K(i,0)=2h_i, K(i,j)=h_|i-j|+h_(i+j) for i,j>0; h past degree is zero',
      'records':records,'minors':sum(r['minors'] for r in records),'failures':[r for r in records if r['first_failure']]}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('falsification_relative_results.json'))
    args=ap.parse_args();d=main();args.output.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps({'states':len(d['records'])//2,'minors':d['minors'],'failures':d['failures']},indent=2))
