#!/usr/bin/env python3
"""Focused fixed-X=P1 midpoint endpoint probe, frozen before execution."""
import json
from pathlib import Path
from falsification_probe import *

def main():
    v=dict(children(build([0],[1],[1])))['l'];sc=dict(scalar_children([1],[2,1],[5,6,2]))['l']
    result={'scope':'ls^j, 0<=j<=80, fixed-X=P1, endpoint parameters(2,2,-2), folded defects only; no relative-minor or continuum conclusion','records':[],'first_failure':None}
    for j in range(81):
        assert tuple(v[k] for k in ('X','Y','C'))==sc and v['X']==P1
        tau=v['t'];c=v['g'];d=scale(v['r'],-1)
        p=add(mul(c,mul(sub(tau,[2]),sub(tau,[2]))),mul(d,add(tau,[2])))
        rec={'path':'l'+'s'*j,'j':j,'degree_H':len(p)-1,'minimum_defects':{}}
        for name,poly in [('H',p),('yH',mul(y,p))]:
            h=H(poly);assert min(h)>0
            vals=defects(h);minimum=min(vals);n=vals.index(minimum);rec['minimum_defects'][name]={'index':n,'value':minimum}
            if minimum<0 and result['first_failure'] is None:result['first_failure']={'j':j,'path':rec['path'],'mode':name,'index':n,'value':minimum,'p':poly,'row':h,'tau':tau,'c':c,'d':d}
        result['records'].append(rec)
        if result['first_failure']:break
        v=dict(children(v))['s'];sc=dict(scalar_children(*sc))['s']
    return result
if __name__=='__main__':
    result=main();Path(__file__).with_name('falsification_packet_ray_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'records':len(result['records']),'max_degree':max(r['degree_H'] for r in result['records']),'first_failure':result['first_failure']},indent=2))
