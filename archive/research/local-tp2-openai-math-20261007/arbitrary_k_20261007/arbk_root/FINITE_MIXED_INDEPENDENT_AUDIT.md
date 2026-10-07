# Independent internal audit of all 34 finite mixed prefixes

**Primary status: PROVED_INTERNAL — exact independent reconstruction PASS.**

`audit_finite_mixed.py` independently reconstructs the canonical original
state by ordinary-x mutations. It derives the new seed polynomials from
that state and its inverse mutation, rather than the author's old
one-turn Laurent recurrence. It imports no author implementation, adapter,
or certificate arrays.

For each raw/smoothed single polynomial and actual midpoint polynomial,
the verifier evaluates row entries at the three exact parameter values
`r=2,0,-2` (and the analogous second parameter). Because the row entries
are known to be multilinear, each defect and each row-entry square has
degree at most two in each parameter. These values uniquely reconstruct
its complete degree-two tensor Bernstein coefficients. Every conversion
is reversed exactly. This is polynomial interpolation, not sampled
positivity evidence.

Only after all independent data have been generated does the verifier
read the author JSON for comparison. Every polynomial degree, coefficient,
reference-domination ratio, normalized lower bound, minimum and ordered
digest agrees at all 34 prefixes. The results comprise:

- 51,804 strictly positive defect Bernstein coefficients;
- 42,246 strictly positive relative-minor margin coefficients for the
  raw and smoothed midpoints;
- exact agreement of all 136 individual polynomial certificate records.

The single interval and midpoint square are covered in full. The midpoint
uses `c=(r+s)/2`, exactly as required by spectral compatibility. The
relative margins prove `c_dom² delta(H)-16 H_n²>0`, and the independently
proved normalized all-minor theorem makes their conclusion valid on every
ordered folded-kernel minor; no finite kernel-index truncation is used.

Reproduce with `python arbk_root/audit_finite_mixed.py` from the package
root. The result JSON records the author artifact hash and all 136
independently reconstructed ordered digests.

This is a distinct implementation in the same shared research session.
It is not external replication, blind review, formal proof-assistant
verification, or a canonical-main promotion.
