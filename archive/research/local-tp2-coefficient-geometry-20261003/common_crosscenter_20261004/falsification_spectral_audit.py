#!/usr/bin/env python3
"""Independent exact check of the spectral lane's strict border witness."""
import json
from fractions import Fraction as F
from pathlib import Path
from falsification_crosscenter import H, add, defects, first_negative, mul, scale, tensor, y, y2


v = [F(3, 200), F(1781, 500), F(349, 200), F(-1249, 200),
     F(-3141, 1000), F(1971, 1000), F(1)]
f = [16, 8, 1]
beta_v = mul(scale(y2, 3), v)
assert H(v) == [F(n, 1000) for n in (4659, 4537, 4181, 3610, 2859, 1971, 1000)]
modes = []
for smooth in (False, True):
    p = mul(y, v) if smooth else v
    tt, dd = tensor(p), defects(H(p))
    assert min(H(p)) > 0 and min(dd) > 0 and first_negative(tt) is None
    modes.append({'mode': 'y' if smooth else 'raw', 'degree': len(p) - 1,
                  'minimum_defect': min(dd), 'minimum_nonzero_character': min(tt.values()),
                  'character_count': len(tt)})
assert v[-1] == f[-1] == 1
assert min(defects(H(beta_v))) > 0
margin = defects(H(add(f, beta_v)))[3]
assert margin == defects(H(beta_v))[3] - H(beta_v)[4]
assert margin == F(-29300421, 500000)
# Exact full-interval parent shifted-trace certificate: its central
# coefficient is decreasing on [-2,2]; the other five are affine/constant.
parent_bounds = [16 * 17 - 128, 128 - 8 * 2, 18 - 2, 45 - 2, 8, 1]
assert parent_bounds == [144, 112, 16, 43, 8, 1]
results = {'classification': 'RELAXED STRICT CONE/LC/SHIFTED-TRACE COUNTEREXAMPLE; NOT MP_sharp OR CANONICAL',
           'modes': modes, 'parent_shifted_trace_character_lower_bounds': parent_bounds,
           'beta_v_border_defect': defects(H(beta_v))[3],
           'beta_v_border_correction': H(beta_v)[4], 'failed_border_defect': margin}
out = Path(__file__).with_name('falsification_spectral_audit_results.json')
out.write_text(json.dumps(results, indent=2, default=str) + '\n')
print(json.dumps(results, indent=2, default=str))
