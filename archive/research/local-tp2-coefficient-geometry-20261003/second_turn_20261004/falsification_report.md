# Targeted independent falsification and small-case proxy audit

The reversed pair survives exact independent checks. The originally suggested
raw midpoint strength does not. Its revised scaled form passes the complete
parameter cube for inner indices 0 through 8, with exact Bernstein validation.
These finite inner-index certificates are not an infinite-inner-index proof.

## Source and independence

The frozen canonical mutation and root are `verify.py: child` and `verify.py:
main`: the root triple is `(1, 5+6x+2x², 2+x)` and mutation is
`3(x+1)TC-x(T+C)-Z`. The candidate formulas were read from `BRIEF.md` first.
Mathematical proof dependencies are `general_one_turn_reduction.md`,
`mixed_kernel_all_minor_strength.md`, and `fulltree_oneturn_mass_proxy.md`.
Their exact SHA-256 values are in `falsification_summary.json`.

`falsification_targeted.py` imports no parent arithmetic modules. Its ordinary
polynomial recurrences, Laurent substitution by repeated multiplication with
`w+w^-1`, parameter-polynomial operations, and rational tensor Bernstein
conversion were implemented independently. It does not use the parent's
binomial Fourier formula or Laurent convolution. The small-case proxy audit
imports these own independent primitives, and imports no proxy-author code.

## Exact reversal identity and ray formulas

Put `y=x+1`, `z=2x+3`, `P=g_m=1+yc`, `X=g_(m+1)`, `c=T_m`,
`d=T_(m+2)`, and `tau=3yX-x`. Pure-left canonical mutation gives
`g_(m+2)=zX-P-x`, hence

`yd=zX-P-y` and `y(c+d)=tau-2-xX`.

The first right center is `C1=(3yP-x)X-1-xP`. Direct algebra gives

`C1-P-tau(P-1)=zX-P-y=yd`.

Consequently `(C1-P)/y=tau*c+d` for every inner index, including `m=0`.
The original mutation retaining `X` is
`Q_(ell+1)=tau Q_ell-Q_(ell-1)-xX`, with `Q_-1=P,Q_0=C1`.
For the outer prefix, `R_(j+1)-tau R_j+R_(j-1)=1`. Substitution of
`Q_ell=1+y[cR_(ell+1)+dR_ell]` yields the same affine forcing because
`2-tau+y(c+d)=-xX`; its initial two values agree. Subtraction gives
`Q_ell-Q_(ell-1)=y[cU_(ell+1)+dU_ell]`. Thus the candidate identities hold
by recurrence uniqueness, not merely by finite fitting.

For `ell>=1`, the previous center has degree greater than that of `X`, so
the child retaining `X` is the shorter-degree child. At `ell=0` the other
endpoint is `P`, and that child orientation must not be reused.

The independent canonical regression covered `m=0,...,8` and
`ell=0,1,2,3,5,8,13`. All identities agreed coefficient by coefficient.
At the 54 states with `ell>=1`, actual Local TP2 and the final proxy were
strict, the short upper comparison was weak, and the proxy lower comparison
was strict at every supported adjacent comparison index. All six listed
initial LR comparisons also passed for `m=0,...,8`.

## Exact smallest obstruction to the discarded midpoint strength

For `m=0`, `c=1`, `d=12+14x+4x²`, and
`H(tau)=(63,50,24,6)`. Let
`H=c(tau-r)(tau-s)+d(tau-u)`.
Then `H(d)_0=20`, so the discarded sufficient target is strength 160.
At Fourier index 5, independently of all three parameters,

`h_5=312`, `delta_5=47232`, and `delta_5-160h_5=-2688`.

The terminal index 6 also gives `h_6=36`, `delta_6=1296`, and margin
`-4464`. Indices 0 through 4 have positive exact Bernstein margins over
the entire parameter cube; index 5 is therefore the first failing index at
the smallest allowed inner index. This refutes that sufficient strength
premise, not the relative-minor condition or Local TP2.

The revised condition uses `alpha=H(tau)_0-2` and tests
`alpha*delta_n(H)-8H(d)_0*h_n>=0`. This condition, its correctly smoothed
analogue with baseline `yd`, both proposed single strengths, and midpoint
cone membership passed every Bernstein coefficient for `m=0,...,8`.
Complete reproducible arrays remain in the intermediate continuum file;
the final summary records bounds and scopes.

An unneeded time-zero extension fails at `m=0`: the new `q0` has row
`(1,1)` and `q1` has row `(211,175,98,34,6)`, with adjacent minor `-36`
at index 0. The required initial comparison starts at `q1<=lr q2`, which
passes. This negative control must not be promoted to a theorem obligation.

## Independent small-case final proxy closure

`falsification_proxy_audit.py` independently reproduced every small-case
numerical quantity in the author's `proxy_mass_results.json`. The complete
arrays and source hashes are retained in `falsification_proxy_audit_results.json`.

| Inner index | Trace bound | Single bound | Fixed proxy threshold | Outer tail starts | Tail central/mass lower |
|---:|---:|---:|---:|---:|---:|
| 0 | 4/5 | 2 | 221/3 | 5 | 2560/3 |
| 1 | 5 | 40 | 1517/6 | 4 | 625 |
| 2 | 5 | 707 | 2600/3 | 2 | 3535/4 |

At `m=0`, all nine exact paired-trace Bernstein coefficients for
`delta0((tau-r)(tau-s))-80*((tau-r)(tau-s))(2)` match:
`(486317,575113,666869,575113,768741,970001,666869,970001,1285693)`.
The direct outer rows `m0:N=2,3,4` and `m1:N=2,3` also match completely,
including exact central defects, masses, residuals, and full-row hashes.
The minimum fixed-proxy remainders are respectively `28068`, `53592`,
and `9840`. All are positive.

These checks certify the small numerical hypotheses. The folded-cone,
product, Jacobi-mixture compatibility, relative-minor and infinite-inner
analytic arguments remain separate mathematical dependencies.

## Complete independent finite proxy bridge

The later root-requested full replay in `falsification_proxy_full_audit.py`
passed every inner index `m=0,...,409`. It recomputed all **85,895** fixed
base-proxy minors and all **820** central-margin Bernstein arrays
(2,460 exact coefficients). Every minor and coefficient was positive.
Every beta, gamma, trace constant, outer-tail threshold, minimum base minor,
central-margin array, tail lower bound and proxy residual matched the author's
complete output exactly. Recalculation finished before the expected complete
output was opened for comparison.

This full replay retains the ordinary-polynomial route. To keep its runtime
bounded it uses carry-free homogeneous Horner Laurent substitution, disclosed
from the independent `finite_audit_independent.py` foundation rather than the
proxy author's Laurent convolution. The packing formula is proved in its
docstring and independently checked against direct Laurent substitution at
small degrees and the defining binomial formula through selected degrees up
to 411. The run took 42.8 seconds. Its complete exact arrays, source hashes
and the digest of every reconstructed base minor are saved in
`falsification_proxy_full_audit_results.json`.

## Final artifact designation

Final evidence consists of `falsification_targeted.py`, this report,
`falsification_summary.json`, `falsification_proxy_audit.py`, and
`falsification_proxy_audit_results.json`, plus
`falsification_proxy_full_audit.py` and
`falsification_proxy_full_audit_results.json`. Bulky continuum arrays and earlier
bounded-result files are retained locally as reproducible intermediate
evidence and need not enter the final manifest. No parent files were changed.
