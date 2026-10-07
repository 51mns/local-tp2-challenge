# Independent audit of the exponential pure-left strength bounds

**Verdict: PASS** for `mixed_kernel_sharp_strength.md`, its exact
certificate package, and its application of the all-minor theorem in
`mixed_kernel_all_minor_strength.md`.

The verified result concerns the sharp-scale strengths and the dominant
product F. It does not prove the required midpoint sum F+G or full
arbitrary-inner-index Local TP2. The manuscript explicitly preserves
that distinction.

## Exact independent reweighting

`mixed_kernel_sharp_strength_independent.py` uses the auditor's own
direct-Laurent and exact Bernstein primitives. It imports no polynomial,
Fourier, Bernstein, or residue routine from the author's implementation.
The eight residue polynomials are reconstructed independently from their
parameter formulas before applying the new strengths.

All **17 blocks and 101 complete power/Bernstein arrays** match
`mixed_kernel_sharp_strength_certificates.json`. Its checked SHA-256 is

`d74d17986b4dc58fde23dca8e8b94bb4729498fefdf6260718ec1bf7d7c93b0e`.

The independently obtained arrays and lower bounds are recorded in
`mixed_kernel_sharp_strength_independent_results.json`.

The scaled quartic's strength-16 margins have lower bounds

`(10977,16328,13120,2944,0)`.

There are exactly nine zero margins: this quartic's terminal margin
and the terminal margin of each of the eight `2^d y²R` residue blocks.
Every one is identically the zero polynomial. All preceding margin
coefficients are strictly positive. Every margin in the ordinary
prefix-residue family is strictly positive, including its terminal
margin. Positivity and symmetry of the supported rows were also checked
independently throughout each parameter box.

The root grouping and scalar bookkeeping remain those independently
audited in `mixed_kernel_pureleft_independent.md`. In particular,
`m=d+4k`, the residue scale is `2^d`, and each removed quartic has
scale 16. Multiplication of strengths gives exactly

`2^d*16^k=2^m` for `P_m=y²T_m`,

`2^(d-1)*16^k=2^(m-1)` for `T_m`.

There is no suppressed scalar or exceptional residue class. The m=1
checks independently give margin rows `(8,32,12,0)` for P_1 at
strength 2 and `(4,2)` for T_1 at strength 1.

The claimed optimality for P_m is correct: its last Fourier entry is
`2^m`, and the terminal defect divided by that entry equals `2^m`.

## Analytic propagation to the trace

Let `lambda=2^m>=4`, `mu=3lambda/2`, and `h=H(P_m)`.
The positive-strength condition gives strictly positive defects and
therefore a strictly decreasing supported row. The actual polynomial
has integer coefficients. Its terminal entry is lambda and its degree
is m+2>=4, so `h_2>=lambda+1` is valid.

The low-index perturbation identities were already reconstructed
independently in the preceding audit. For
`b_0=3h_0+c`, `b_1=3h_1+2`, `b_n=3h_n` otherwise, the derivative of
`delta_0(b)-mu b_0` in c is

`6h_0+3h_2+2c-mu`.

It is positive on c in `[1,5]`; for example the stated entry bounds
make it at least `15lambda/2+11`. Evaluation at c=1 and monotonicity
of h give exactly the manuscript's lower bound

`(9lambda/2-18)h_0+3h_2-7-3lambda/2`

`>=3lambda/2-4>=2`.

At index one the derived lower bound is

`(9lambda/2-3)h_1+6h_3+4-3lambda`,

which is positive already from h_1>=1: ignoring the favorable h_3
term leaves `3lambda/2+1`. At index two the bound is
`(9lambda/2-6)h_2>0`; at every higher supported index it is
`9lambda h_n/2>0`. These are unbounded analytic estimates in m,
not checks at particular m values.

The m=1 trace conclusion is exactly the separately audited uniform
3-strong interval certificate. Thus `t_m-a` is
`3*2^(m-1)`-strong for every m>=1 and every a in `[-2,2]`.

## All-minor theorem and its support qualification

The all-minor theorem is valid with its stated positive-diagonal-entry
restriction. The terminal inequality gives `h_degree>=lambda`, and
decrease of h makes every positive kernel entry at least lambda.
Thus if an off-diagonal entry of the selected minor is zero, the
diagonal product proves the estimate immediately.

If both off-diagonal entries are positive, band support makes the
entire row/column rectangle positive. The product of all adjacent
cross-ratios in that rectangle telescopes to its four-corner ratio.
Keeping the bottom-right adjacent cross-ratio and using its quantitative
adjacent-minor bound proves

`det K_h[(i,j),(k,l)]>=lambda K_h(i,k)`.

No division by a possibly zero entry is made. The relative-minor
corollary correctly applies this theorem only when the B minor is
positive. Coefficientwise domination then supplies both positive
diagonal entries of H. Since every B-kernel entry is at most `2b_0`,
the assumption `lambda>=8b_0` gives the claimed factor four.

## Dominant product estimate

For `A=T_(m+1)`, `B=T_(m-1)`, and
`F=A(t_m-r)(t_m-s)`, strength multiplication gives

`lambda_F=2^m*(3*2^(m-1))²=9*2^(3m-2)`.

The evaluation bound is also correct at every m>=1, including m=1.
The recurrence with multiplier 7 gives `U_j(7/2)<=7^j`; hence

`8H(B)[0]<=8B(2)<=4(7^m-1)/3 < (9/4)8^m=lambda_F`.

The inner shifted Chebyshev polynomials have positive ordinary
coefficients, so the longer prefix A dominates B coefficientwise.
Each trace factor has positive ordinary coefficients and constant at
least one. Therefore F dominates B first in ordinary coefficients and
then in Fourier half-rows. All hypotheses of the relative-minor
corollary are met, proving `det K_F>=4 det K_B` at every pair of
ordered row and column indices, without kernel truncation.

## The addition obstruction remains real

The final scope correction is exact. If
`G=B(t_m-c)`, then `deg G=d=2m+1` and `deg F=3m+5`.
At index d+1, the polarized defect is

`delta_(d+1)(F+G)-delta_(d+1)(F)-delta_(d+1)(G)`

`=-H(G)[d]H(F)[d+2]<0`.

Thus complete nonnegative pairwise compatibility of F and G is
impossible. This does not refute a strength bound for F+G, but any
such proof must absorb this negative cross contribution quantitatively.
The audited manuscript makes no claim that the dominant-product bound
already passes to the sum.
