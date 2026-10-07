# Independent recovery audit: one-turn single blocks and smoothed residues

**Verdict: PASS for the exact finite certificates and the additional analytic
smoothed-trace estimates described here.** This audit does not assert the full
canonical-tree Local TP2 conjecture, nor does a finite range alone prove an
infinite range.

The reproducible verifier is `recovery_single_audit.py`; its machine-readable
report is `recovery_single_audit.json`. It imports no author research modules.
All arithmetic uses Python integers or exact rational fractions.

## 1. Finite single-block certificates

Write `x=q+q^-1`, `y=x+1`,

`T_m=sum_(j=0)^m U_j(x+3/2)`,

`t=3y^2 T_m+2x+3`, `A=T_(m+1)`, `B=T_(m-1)`.

The audit reconstructs full Laurent rows from the direct inhomogeneous
recurrence

`T_m=(3+2x)T_(m-1)-T_(m-2)+1`, `T_-1=0`, `T_0=1`.

This differs from the author's half-row recurrence for `U_m` followed by
summation. An independent ordinary-`x` recurrence and the binomial Laurent
substitution cross-check full rows at indices
`0,1,2,3,7,20,96,200,390,391`.

The generic parameter `u in [0,1]` represents `r=-2+4u`, so that the
single block is `A(t+2-4u)+B`. The verifier forms the defect polynomial
by ordinary multiplication of parameter coefficient arrays and applies the
defining power-to-Bernstein formula

`b_a=sum_(j<=a) c_j binom(a,j)/binom(2,j)`.

It does not use the author's hand-expanded quadratic margin formula.
For every supported index it checks four times the Bernstein coefficients
of `delta_n(H)-lambda H_n`.

| Block | Complete inner-index range | Strength lambda |
|---|---:|---:|
| `A(t-r)+B` | `1 <= m <= 390` | `3*2^(2m-3)` |
| `y[A(t-r)+B]` | `1 <= m <= 390` | `3*2^(2m-3)` |
| `y(t-r)` | `1 <= m <= 3` | `3*2^(m-2)` |

There are **783 cases and 925,524 strictly positive integer Bernstein
margins**. Every stored minimum and every ordered margin SHA-256 digest
matches the author's output exactly. The closed parameter interval is
covered, including its endpoints. The verifier also checks positivity of
every supported coefficient at both parameter endpoints.

The audit uses negative Laurent indices directly, so index `n=0` is checked
with the correct reflection. At and beyond the first unsupported index,
all relevant margins vanish identically; no strict claim is made there.

## 2. Residue-box certificates

The verifier independently builds the eight explicitly stated residue
polynomials in five independent parameters. It uses full Laurent
polynomials, extracts Laurent coefficients directly, forms their quadratic
defects, and applies the defining tensor Bernstein transform using exact
binomial ratios. The source symbolic/Fourier/Bernstein functions are not
imported.

For a residue of degree `d`, it verifies that both `2^d yR` and
`2^d y^3R` have strength `2^(d-1)` on the complete closed parameter box.
There are **112 supported-index arrays**, all with strictly positive
Bernstein lower bounds. Every power coefficient, every Bernstein
coefficient, every degree tuple, and every recorded lower bound matches
the stored certificate exactly. Each supported Laurent coefficient is
also Bernstein-positive.

The exceptional `m=1` cases add eight exact arrays. Their strength-one
margins are:

| Polynomial | Supported-index margins |
|---|---|
| `yT_1` | `0, 10, 2` |
| `y^3T_1` | `132, 304, 162, 34, 2` |

The zero at `yT_1`, `n=0` is correct: the strength assertion is
non-strict. The defect itself remains positive. It must not be described
as a strictly positive *strength margin*.

Both expected output JSON files are first opened only after all cases,
residue arrays, and scalar inequalities have been independently
recomputed and validated.

## 3. Scalar tail thresholds

The audit exactly recomputes the recorded inequalities at `m=391`, with
`sigma=59/100` and `c0=1/400000000`. Both normalized defect bounds exceed
`12 epsilon_m`, `epsilon_m<1`, and the required strength-to-mass bound
holds. The two consecutive-ratio lower bounds are greater than one.

Their propagation to later integers follows because `(m+3)/(m+4)` and
`(2m+5)/(2m+7)` increase. The strength-to-mass ratio propagates because

`8(7^m-1)-(7^(m+1)-1)=7^m-7>0` for `m>1`.

The two normalized-residue inequalities
`4352 sigma^16<1` and `6c0((9/2)sigma)^18<1` also pass exactly.
These checks verify the scalar arithmetic and monotonicity; the
root-factor decomposition and the product/perturbation lemmas supplying
these scalar formulas are separate dependencies.

## 4. Additional analytic audit of the smoothed trace

Section 2 of `recovery_oneturn_closure.md` sets
`b=3h+(a+4,a+2,2,0,...)`, `1<=a<=5`. The independent symbolic checker
verifies all four expansions of `delta_n(b)-9delta_n(h)` for
`n=0,1,2,3` as polynomial identities in six free half-row entries and `a`.
For `n>=4` the perturbation has no overlap with the defect and its
contribution is zero.

Let `E_n=delta_n(b)-9delta_n(h)`. The claimed lower estimates have the
following exact nonnegative remainders:

```
E_0+24h_0-1
 =6(5-a)h_0+(12a+24)(h_0-h_1)+(3a+12)h_2+(5-a)(a+3),

E_1+21h_1+5
 =6(2h_1-h_0)+(3a+24)(h_1-h_2)
  +3(a-1)h_1+(3a+6)h_3+(a-1)(a+3),

E_2+9h_2-4
 =3(a+2)(h_2-h_3)+3(5-a)h_2+6h_4,

E_3+6h_3=6(h_3-h_4).
```

Each identity is independently checked symbolically. All terms are
nonnegative under the manuscript's decrease, positivity, and
`h_0<=2h_1` hypotheses.

Using `delta_n(h)>=lambda h_n`, `h_n>=2lambda` on support, and
`lambda>=8`, subtracting `(3lambda/2)b_n` yields the three quadratic
lower bounds used at `n=0,1,2`. With `lambda=8+s`, their constant,
linear, and quadratic coefficients are respectively

`(85,165/2,9)`, `(151,183/2,9)`, `(412,123,9)`.

All are strictly positive for `s>=0`. The estimates for indices three
and above also have strictly positive coefficients. Thus the analytic
smoothed-trace step is valid under its explicitly listed prefix-strength
and monotonicity hypotheses, including the upper support boundary.

## 5. Scope and remaining dependencies

No arithmetic or boundary defect was found in this audit. Its results
remove the independent-verification gap in the new single-block and
residue certificates and verify the added smoothed-trace argument.

A complete arbitrary-`m` one-turn theorem still relies on the cited
root-factor residue coverage, normalized degree-16 blocks, strength
product theorem, perturbation theorem, Jacobi compatibility, and final
mass/proxy reduction. These broader dependencies are reviewed separately
in the closure audit. Paths with further changes of direction are
outside the one-turn theorem.
