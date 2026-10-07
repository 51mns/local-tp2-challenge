"""Independent direct-Laurent reconstruction of mixed-ray certificates.

Does not import the author's polynomial, Fourier, or Bernstein routines.
"""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

ZERO = (0, 0, 0, 0)

def term(value, q=0, a=0, b=0, c=0):
    return {(q,a,b,c): Fraction(value)} if value else {}

def plus(*items):
    out = {}
    for item in items:
        for key, coefficient in item.items():
            out[key] = out.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in out.items() if value}

def times(left, right):
    out = {}
    for kl, vl in left.items():
        for kr, vr in right.items():
            key = tuple(kl[i] + kr[i] for i in range(4))
            out[key] = out.get(key, Fraction(0)) + vl*vr
    return {key: value for key, value in out.items() if value}

def scale(item, coefficient):
    return {key: coefficient*value for key, value in item.items() if coefficient*value}

def power(item, n):
    out = term(1)
    for _ in range(n):
        out = times(out, item)
    return out

def row(poly, index):
    return {(0,)+key[1:]: value for key, value in poly.items() if key[0] == index}

def defect(poly, n):
    h = lambda j: row(poly, abs(j))
    return plus(times(h(n), h(n)), scale(times(h(n-1),h(n+1)),-1),
                scale(times(h(n+1),h(n+1)),-1), times(h(n),h(n+2)))

def bernstein(poly):
    degree = tuple(max((key[j] for key in poly), default=0) for j in (1,2,3))
    result = {}
    for indices in product(*(range(d+1) for d in degree)):
        total = Fraction(0)
        for key, coefficient in poly.items():
            if all(key[j+1] <= indices[j] for j in range(3)):
                for j in range(3):
                    coefficient *= Fraction(comb(indices[j], key[j+1]), comb(degree[j], key[j+1]))
                total += coefficient
        result[','.join(map(str,indices))] = str(total)
    return list(degree), result

def main():
    x = plus(term(1,q=1), term(1,q=-1))
    y = plus(x,term(1))
    a = plus(term(-2), term(4,a=1))
    b = plus(term(-2), term(4,b=1))
    c = plus(term(-2), term(4,c=1))
    t = plus(scale(power(x,3),6), scale(power(x,2),24), scale(x,32),term(15))
    w = plus(scale(power(x,2),4),scale(x,14),term(12))
    ta,tb = plus(t,scale(a,-1)),plus(t,scale(b,-1))
    tw=plus(t,w)
    blocks = {
        'cubic':ta,
        'y_cubic':times(y,ta),
        'w':w,
        'w_minus_one':plus(w,term(-1)),
        'y_w':times(y,w),
        't_plus_w':tw,
        't_plus_w_plus_one':plus(tw,term(1)),
        'y_t_plus_w':times(y,tw),
        'y_t_plus_w_plus_one':times(y,plus(tw,term(1))),
        'lr_single':plus(times(w,ta),term(1)),
        'rl_single':plus(times(tw,ta),term(-1)),
        'y_lr_single':times(y,plus(times(w,ta),term(1))),
        'y_rl_single':times(y,plus(times(tw,ta),term(-1))),
        'y_lr_degree_two':times(y,plus(times(w,plus(power(t,2),term(-1))),t)),
        'y_rl_degree_two':times(y,plus(times(tw,plus(power(t,2),term(-1))),scale(t,-1))),
        'lr_pair_midpoint':plus(times(w,times(ta,tb)),t,scale(c,-1)),
        'rl_pair_midpoint':plus(times(tw,times(ta,tb)),scale(t,-1),c),
    }
    certificate_path = Path('mixed_ray_kernel_certificates.json')
    originals = json.loads(certificate_path.read_text())
    assert set(originals) == set(blocks)
    summaries = {}
    for name, poly in blocks.items():
        degree = max(key[0] for key in poly)
        assert min(key[0] for key in poly) == -degree
        assert len(originals[name]) == degree+1
        row_bounds, defect_bounds = [], []
        for n in range(degree+1):
            assert row(poly,n) == row(poly,-n), (name,n,'symmetry')
            _, row_coefficients = bernstein(row(poly,n))
            row_lower = min(map(Fraction,row_coefficients.values()))
            assert row_lower > 0, (name,n,'row')
            row_bounds.append(str(row_lower))
            d = defect(poly,n)
            margin = 8 if name.endswith('midpoint') and n == 0 else 0
            degrees, coefficients = bernstein(plus(d,term(-margin)))
            lower = min(map(Fraction,coefficients.values()))
            expected = originals[name][n]
            assert expected['n'] == n
            assert expected['subtracted_margin'] == margin
            assert expected['parameter_degrees'] == degrees, (name,n,'degrees')
            assert expected['power_coefficients'] == {','.join(map(str,k[1:])):str(v) for k,v in d.items()}, (name,n,'powers')
            assert expected['bernstein_coefficients_after_margin'] == coefficients, (name,n,'Bernstein')
            assert Fraction(expected['bernstein_lower_bound']) == lower
            assert lower > 0, (name,n,'defect')
            defect_bounds.append(str(lower+margin))
        summaries[name] = {
            'degree':degree,
            'positive_row_lower_bounds':row_bounds,
            'defect_lower_bounds':defect_bounds,
            'all_author_arrays_match':True,
        }
    margin_path = Path('mixed_ray_margin_certificates.json')
    margin_originals = json.loads(margin_path.read_text())
    f = plus(t,term(-2),term(4,a=1))
    balanced = plus(power(t,2),times(term(2,a=1),t),term(-4,b=1))
    margin_blocks = {
        'single_root':(f,Fraction(4,5)),
        'balanced_pair':(balanced,Fraction(90)),
        'left_right_resolvent':(plus(times(w,f),term(1)),Fraction(40)),
        'right_left_resolvent':(plus(times(tw,f),term(-1)),Fraction(100)),
    }
    assert set(margin_originals) == set(margin_blocks)
    margin_summaries = {}
    for name,(poly,factor) in margin_blocks.items():
        mass = plus(*[{(0,)+key[1:]:value} for key,value in poly.items()])
        margin = plus(defect(poly,0),scale(mass,-factor))
        degrees,coefficients = bernstein(margin)
        # The author's shared engine carries a fourth, unused parameter.
        padded_coefficients = {key+',0':value for key,value in coefficients.items()}
        padded_powers = {','.join(map(str,key[1:]+(0,))):str(value)
                         for key,value in margin.items()}
        lower = min(map(Fraction,coefficients.values()))
        expected = margin_originals[name]
        assert expected['mass_factor'] == str(factor)
        certificate = expected['certificate']
        assert certificate['degrees'] == degrees+[0]
        assert certificate['power_coefficients'] == padded_powers
        assert certificate['bernstein_coefficients'] == padded_coefficients
        assert Fraction(certificate['strict_lower_bound']) == lower
        assert lower > 0
        margin_summaries[name] = {'mass_factor':str(factor), 'strict_lower_bound':str(lower),
                                  'all_author_arrays_match':True}
    result = {
        'status':'PASS',
        'method':'fresh direct Laurent substitution and exact rational Bernstein reconstruction',
        'certificate_sha256':hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
        'verified_blocks':len(blocks),
        'verified_defect_arrays':sum(len(v) for v in originals.values()),
        'blocks':summaries,
        'margin_certificate_sha256':hashlib.sha256(margin_path.read_bytes()).hexdigest(),
        'verified_mass_margin_arrays':len(margin_blocks),
        'mass_margins':margin_summaries,
    }
    Path('mixed_ray_kernel_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key not in ('blocks','mass_margins')},indent=2))

if __name__=='__main__':
    main()
