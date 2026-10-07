#!/usr/bin/env python3
"""Frozen gap, reference-band, and spectral corner adversarial probes."""
import argparse,itertools,json
from pathlib import Path
from fractions import Fraction
from falsification_probe import *
from falsification_targeted import state,remainder,frozen_checks

def main():
    out={'scope':'Only frozen bounded scopes; no continuous-parameter or infinite-path inference','first_failures':{},'counts':{},'relative_band':[],'complete_depth6_C':{}}
    def record(key,vals,path,extra):
        out['counts'][key]=out['counts'].get(key,0)+len(vals)
        bad=[i for i,v in enumerate(vals) if v<0]
        if bad and key not in out['first_failures']:
            n=bad[0];out['first_failures'][key]={'path':path,'index':n,'margin':frac(Fraction(vals[n])),**extra}
    paths=[''.join(w) for n in range(7) for w in itertools.product('sl',repeat=n)]
    for path in paths:
        v=state(path);bad,summary=frozen_checks(v)
        for w in bad:
            if w['predicate'] in ('C_raw','C_smoothed'):out['complete_depth6_C'].setdefault(w['predicate'],{'path':path,**w})
    paths=list(dict.fromkeys(paths+['s'*j for j in range(36)]+['l'+'s'*j for j in range(21)]))
    for path in paths:
        v=state(path);G=mul(y,v['g']);S=mul(y,v['s']);R=mul(y,v['r']);D=mul(y,v['d']);h=H(G);lc=G[-1]
        ds=defects(h)
        record('D_G_half',[Fraction(d)-Fraction(lc,2)*hn for d,hn in zip(ds,h)],path,{'p':G,'row':h,'strength':frac(Fraction(lc,2))})
        if path:record('D_G_full_nonroot',[d-lc*hn for d,hn in zip(ds,h)],path,{'p':G,'row':h,'strength':frac(Fraction(lc))})
        f,g,c=H(mul(v['t'],G)),H(R),H(S);delta=defects(c);rem=[remainder(f,g,n) for n in range(len(c))]
        assert all(get(f,n)-get(g,n)==get(c,n) for n in range(len(f))) and min(rem)>=0
        surplus=[Fraction(d)-Fraction(S[-1],2)*cn for d,cn in zip(delta,c)]
        vals=[s-Fraction(r,32) for s,r in zip(surplus,rem)]
        bad=[n for n,z in enumerate(vals) if z<0]
        extra={'p':S,'F':mul(v['t'],G),'R_poly':R,'strength':frac(Fraction(S[-1],2))}
        if bad:extra.update({'surplus':frac(surplus[bad[0]]),'R':rem[bad[0]]})
        record('D_short_R32',vals,path,extra)
        long=add(S,D);lh=H(long);record('D_long_half',[Fraction(d)-Fraction(long[-1],2)*hn for d,hn in zip(defects(lh),lh)],path,{'p':long,'row':lh,'strength':frac(Fraction(long[-1],2))})
        dh=H(D);record('D_outgoing_half',[Fraction(d)-Fraction(D[-1],2)*hn for d,hn in zip(defects(dh),dh)],path,{'p':D,'row':dh,'strength':frac(Fraction(D[-1],2))})
    for j in range(61):
        path='s'*j;v=state(path)
        for sm in (False,True):
            hp=mul(y,v['s']) if sm else v['s'];bp=mul(y,v['r']) if sm else v['r'];h,b=H(hp),H(bp);d=len(b)-1;ds=defects(h)
            alpha=min(Fraction(h[n],bn) for n,bn in enumerate(b));ll=min(Fraction(ds[n],h[n]) for n in range(min(d+2,len(h))))
            bands=[Fraction(ds[a],h[a]) for a in range(d+1)]+[Fraction(sum(get(ds,i) for i in range(a,a+3)),h[a]+get(h,a+2)) for a in range(d+1)]
            band=min(bands)
            for key,strength in [('lambda_local',ll),('L_d',band)]:
                margin=strength*alpha-8*b[0]
                rec={'path':path,'smooth':sm,'candidate':key,'strength':frac(strength),'alpha':frac(alpha),'margin':frac(margin)}
                out['relative_band'].append(rec)
                record(('y' if sm else '')+'band_'+key,[margin],path,{'h':hp,'b':bp,'rows':[h,b],'strength':frac(strength),'alpha':frac(alpha)})
    paths=[''.join(w) for n in range(5) for w in itertools.product('sl',repeat=n)]
    paths=list(dict.fromkeys(paths+['l'+'s'*j for j in range(9)]+['ll'+'s'*j for j in range(7)]))
    for path in paths:
        v=state(path)
        packets=[('Y',add(v['t'],scale(mul(y2,v['e']),3)),add(v['e'],v['g']),sub(v['e'],v['r']))]
        if v['a']!=[0]:packets.append(('X',v['t'],v['g'],scale(v['r'],-1)))
        for label,tau,c,d in packets:
            for r in (-2,2):
                factor=sub(tau,[r]);L=add(mul(c,factor),d)
                for key,p in [('trace',factor),('L',L),('yL',mul(y,L))]:
                    h=H(p); assert min(h)>0
                    record('packet_'+label+'_'+key,defects(h),path,{'parameters':[r],'p':p,'row':h,'tau':tau,'c':c,'d':d})
            for r,s,u in itertools.product((-2,2),repeat=3):
                hp=add(mul(c,mul(sub(tau,[r]),sub(tau,[s]))),mul(d,sub(tau,[u])))
                for key,p in [('H',hp),('yH',mul(y,hp))]:
                    h=H(p); assert min(h)>0
                    record('packet_'+label+'_'+key,defects(h),path,{'parameters':[r,s,u],'p':p,'row':h,'tau':tau,'c':c,'d':d})
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('falsification_extra_results.json'))
    args=ap.parse_args();out=main();args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'first_failures':{k:{z:v[z] for z in ('path','index','margin','strength','alpha') if z in v} for k,v in out['first_failures'].items()},'complete_depth6_C_failures':out['complete_depth6_C'],'counts':out['counts']},indent=2))
