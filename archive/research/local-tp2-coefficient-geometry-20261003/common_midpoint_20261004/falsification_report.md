# Actual paired-midpoint challenge: frozen result

**No actual counterexample was found in the frozen scope.** Both the
uniform reference factor 4 and the sharp factor `(r-s)^2/4` hold at every
tested fixed parameter pair, in both seed orientations and raw/y-smoothed
modes. Each such pass covers **all ordered folded-kernel indices**, by
the proved all-minor strength criterion and independently by the audited
finite character equivalence. This is not a parameter-continuum result,
a child-closure proof, or an all-tree MP2 result.

## Exact scope and evidence

The normalized recurrence is rebuilt from `(a,e,r)=(0,1,1)`. At every
step it is crosschecked against the original scalar mutation of `(X,Y,C)`,
and the exact Fricke polynomial is asserted zero. The frozen path set,
parameter grid, order, and degree cap are in `falsification_frozen.md`.

| Quantity | Exact scope/result |
|---|---|
| Actual states | 33; all seven through depth 2 plus frozen short, long, and alternating paths |
| Midpoint parameter pairs | 12 exact rational pairs, including all three distinct symmetric corners |
| Seed orders | `(c_A,e)` and `(e,c_A)`, where `c_A=e+g+s` |
| Modes | Raw and multiplication by `y=x+1`, checked independently |
| Fixed midpoint cases | 1,584 |
| Complete rows `(0,1)` column-pair comparisons | 2,173,464 |
| All-index strength certificates | 1,584; no scalar-certificate failures |
| Tested trace/L/yL/H failures | None |
| Uniform-factor-4 / sharp-factor failures | None |
| Omitted paths | Five paths exceed the frozen smoothed midpoint degree cap 160; listed in the result JSON |

The certificate uses reflected/zero-extended folded defects and
`lambda=min delta_n(h)/h_n`, `alpha=min h_n/b_n`. It verifies
`lambda>0`, `alpha>=2`, `deg h>=deg b`, `max b_n<=b_0`, and
`lambda*alpha>=8b_0`. The global minima over all fixed cases are
`lambda=36` and `alpha=12757/20`, so the explicitly checked
`alpha>=2` premise has substantial slack. The proof underlying this
sufficient criterion is the reference-band theorem in the read-only
`../common_closure_20261004/quantitative_common_gates.md`, Section 2;
the global strength used here bounds its local reference-band constant.

The complete rows `(0,1)` comparisons also give every coefficient of
`T_H-gamma*T_b`. The independent proof audit in
`falsification_network_audit.md` confirms that character positivity is
equivalent to **all** ordered folded relative minors, including unbounded
row/column indices. No finite kernel-index extrapolation is used.

## Exact margins

| Minimum over fixed cases | Value | Earliest attaining case |
|---|---:|---|
| `lambda*alpha-8b_0` | `114013/5` | Root, reverse, `(r,s)=(2,2)`, raw |
| `lambda*alpha/(8b_0)` | `35161/512` | Root, reverse, `(2,2)`, y-smoothed |
| Complete rows `(0,1)` uniform margin | `1296` | Root, reverse, `(-2,-2)`, raw |
| Complete rows `(0,1)` sharp margin | `1296` | Same case |

For the last two minima, the actual root polynomials are

    T = 15+32x+24x²+6x³,
    c_A = 12+14x+4x²,
    H = (T+2)²+c_A(T+2)
      = 493+1710x+2644x²+2276x³+1140x⁴+312x⁵+36x⁶.

Its Fourier half-row is `(13341,11658,7744,3836,1356,312,36)`.
Rows `(0,1)` and columns `(6,7)` have determinant `36²=1296`;
the reference `c_A` ends at degree 2 and contributes zero there.

## Precisely classified exceptions and obstruction

Twelve cases record the same unused auxiliary reference-cone failure:
the forward root y-smoothed reference is `ye=y`, with half-row `(1,1)`
and central folded defect `-1`. Reference-cone membership is **not** an
MP2 or relative-character premise, and this does not invalidate any pass.

There is a genuine exact obstruction to an overly strong proof method:
ordinary parameter-power coefficient positivity for every sharp tensor
coefficient fails at the actual root, reverse orientation, y-smoothed.
Its `alpha² beta²` coefficient at the central minor equals `-1`, since
the highest midpoint term has seed `y e=y`. This is a failure of that
sufficient coefficient method, not an MP2, mixed-compatibility, or
child-closure counterexample. Details and the all-state far-band lemma
are in `falsification_extremal.md`.

## Reproduction and freeze scope

Run from this directory:

    python falsification_probe.py

The script uses only the standard library and the read-only exact
arithmetic module `../common_transport_20261004/adversarial_probe.py`.
Its hash and the generator hash are recorded in the concise
`falsification_results.json`. Deterministic detailed records are retained
as `falsification_records.json.gz`; both compressed and uncompressed
hashes are recorded in the summary. The final consolidation checked
every saved certificate's support/alpha premises and replayed the root
margin identity without expanding the frozen search.

The bounded search has stopped. Continuous midpoint parameters, arbitrary
actual paths, new-center paired-packet preservation, and the regular
strict proxy remain outside its conclusion.
