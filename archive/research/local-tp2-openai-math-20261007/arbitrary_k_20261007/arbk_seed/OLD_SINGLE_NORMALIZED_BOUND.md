# Normalized old trace and single-template bounds

**Status: PROVED_INTERNAL; separate mathematical and finite-certificate
reconstruction audit PASS.** The finite part consists of complete
degree-two Bernstein certificates on `[-2,2]`; the remaining infinite
tail is an analytic consequence of the previously proved one-turn
normalized product and perturbation lemmas.

Use `t_0=3y g_m-x`, `a=T_(m+1)`, `b=T_(m-1)`, and

\[
L_r=a(t_0-r)+b,\qquad -2\le r\le2.
\]

## 1. The single-template tail already starts at m=70

The existing proof `recovery_oneturn_closure.md`, Sections 1 and 3,
gives

\[
\eta(a),\eta(ya)\ge c_0\sigma^{m+1},\qquad
\eta(t_0-r)\ge c_0\sigma^m/2\quad(m\ge21),
\]

with `c_0=1/400000000`, `sigma=59/100`. The normalized product
theorem gives both dominant products `F=a(t_0-r), ya(t_0-r)` the bound

\[
\eta(F)\ge D_m:=\frac{c_0^2\sigma^{2m+1}}{4(m+3)}.
\]

The correction `G=b` or `yb` obeys

\[
0\le G\le\epsilon_m F,
\qquad\epsilon_m=\frac{2m+5}{9\,6^m}.
\]

This follows from `b<=a` and the established central bound
`H(t_0)_0>=27*6^m/(2m+5)`: every shifted trace contributes its
central coefficient, and `1/(H(t_0)_0-2)<=3/H(t_0)_0`.

The normalized perturbation lemma gives

\[
\delta_n(F+G)\ge\delta_n(F)
-(4\epsilon_m+2\epsilon_m^2)H(F)_n^2.
\]

The exact rational gate `D_70>12epsilon_70` is recorded by
`verify_seed_subtraction.py`. The consecutive ratio of
`D_m/(12epsilon_m)` is

\[
6\sigma^2\frac{(m+3)(2m+5)}{(m+4)(2m+7)},
\]

whose value at 70 is `7369277/3626000>1` and which increases with
`m`. Thus every `m>=70` retains at least half the dominant defect.
Also `epsilon_m<1/3`, so

\[
\boxed{\eta(L_r),\eta(yL_r)\ge
\frac{c_0^2\sigma^{2m+1}}{16(m+3)}\quad(m\ge70).}
\tag{1}
\]

The old common threshold 391 covered the substantially harder midpoint
at the same time. It is not needed for this single-template assertion.
No improvement to the old midpoint theorem is being asserted here.

## 2. Stronger explicit constants for m=0,...,69

For each finite `m`, `verify_old_normalized_constants.py` constructs the
old trace and both single rows from the inner Laurent recurrence. It
uses `r=2-4u`, `0<=u<=1`. Every row entry is affine in `u`, so its
defect and its square are exactly quadratic.

Let `d_(n,i)` and `h_(n,i)` be their degree-two Bernstein coefficients.
Every one of these coefficients is positive in the finite record. Then

\[
\eta\ge\min_{n,i}\frac{d_{n,i}}{h_{n,i}}
\tag{2}
\]

on the **entire** parameter interval, because subtraction of the right
side times the row-entry square leaves nonnegative Bernstein
coefficients. This is a sufficient exact lower bound, not a claim of
the optimal normalized defect.

The three evaluations used to recover each quadratic are at
`r=2,0,-2`; they are exact interpolation data, not a root sample test.
The conversion is inverted for every polynomial. The result JSON
records each exact rational lower bound, its minimizing coefficient
index, the ordered coefficient-pair digest, and the number of pairs.

Define `e_m` to be the trace lower bound and `ell_m` the smaller of the
raw and smoothed single bounds. The complete load-bearing table is
`old_normalized_constants.json`, restricted to `m=0,...,69`. For example,

| m | e_m | ell_m |
|---|---|---|
| 0 | 1/50 | 339/4418 |
| 1 | 185/3721 | 293881/6487209 |
| 2 | 9077/139129 | 2889727513/98998958881 |
| 3 | 152473/2677298 | 443346683755/22027433181728 |

For `m>=70`, one may instead use

\[
e_m=c_0\sigma^m/2,
\qquad\ell_m=c_0^2\sigma^{2m+1}/[16(m+3)].
\]

The table separately labels the old trace's central coefficient and
its mass `t_0(2)`. They are not interchangeable in a coefficient
comparison. Each recorded scalar rate explicitly identifies which
quantity it uses.

The script uses standard Python integer arithmetic and exact `Fraction`
comparisons. Its positive convolution packs coefficients in a rigorously
chosen base exceeding the maximum possible convolution coefficient,
so no carries can corrupt a coefficient.

The separate `../arbk_mixed/audit_seed_bounds.py` uses ordinary
polynomials, direct binomial Fourier conversion, and endpoint
polarization instead of three-point interpolation. It reproduces all
**38,745** ordered Bernstein defect/square coefficient pairs, every
exact normalized lower bound, and the `m=70` tail anchors. See
`../arbk_mixed/SEED_BOUNDS_INDEPENDENT_AUDIT.md` for the audit record.

## Reproduction

```bash
python arbk_seed/verify_old_normalized_constants.py --max-m 69
python arbk_seed/verify_seed_subtraction.py
```

Both commands write only their corresponding result JSON in `arbk_seed`.
The conclusions are auxiliary normalized-kernel bounds; the full
three-run target requires the separate subsequent proof assembly.
