"""Exact scalar gates for the analytic all-m mass/proxy tail."""
from fractions import Fraction as Q
from pathlib import Path
import json


def main():
    checks={}
    checks['proxy_scalar_at_106']=Q(8,7)**106/Q(3072*(4*106+7))
    checks['proxy_scalar_ratio_at_106']=Q(8*(4*106+7),7*(4*106+11))
    checks['trace_mass_at_6']=Q(3*2**5,2*6+5)
    checks['trace_mass_ratio_at_6']=Q(2*(2*6+5),2*6+7)
    checks['smoothed_strength_at_6']=Q(3*2**4)
    checks['template_gamma_at_391']=Q(3*2**(2*391-3),4*391+7)
    checks['template_gamma_ratio_at_391']=Q(4*(4*391+7),4*391+11)
    checks['proxy_surplus_at_391']=Q(
        3*2**(2*391-3)*(3*2**(391-2)-14),
        4*(4*391+7)*108*7**391)
    assert checks['proxy_scalar_at_106']>1
    assert checks['proxy_scalar_ratio_at_106']>1
    assert checks['trace_mass_at_6']>=4
    assert checks['trace_mass_ratio_at_6']>1
    assert checks['smoothed_strength_at_6']>=28
    assert checks['template_gamma_at_391']>12
    assert checks['template_gamma_ratio_at_391']>1
    assert checks['proxy_surplus_at_391']>1
    output={'status':'PASS','tail':'all integers m >= 391',
            'strength_inputs':{'template':'3*2^(2m-3)','smoothed_trace':'3*2^(m-2)'},
            'checks':{k:{'exact':str(v),'decimal':float(v)} for k,v in checks.items()}}
    Path('fulltree_oneturn_mass_proxy_tail_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':'PASS','scalar_checks':len(checks)}))


if __name__=='__main__':
    main()
