# Additional mathematical review of the uniform ray assembly

**Verdict: PASS for the analytic assembly reviewed below.**

This is an additional mathematical review of Sections 5–9 of
`../hour_root/UNIFORM_RAY_CLOSURE.md`, after the independent reviews of
its seed, trace, mixed-template, initial-order, and finite-criterion
dependencies. The separate root/rayleigh implementations certify the
finite bridge; this note does not claim a third execution of that bridge.

## Smoothing and base comparisons

The smoothing argument uses the two nonzero first-row minors of
`K_(y^2)`: weights 4 on columns `(0,1)` and 1 on `(2,3)`. For `n>=2`,
the second selected minor retains `delta_(n-2)(F)`, including the two
new terminal indices. The separate `n=0,1` estimates cover reflection.
The bound `H(L_r)_0<=8H(L_r)_1` follows from
`H(t-r)_0<=4H(t-r)_1`, kernel multiplication, and `B<=A(t-r)`.
Thus the normalized factor `1/1296` has no missing boundary case.

In the correction domination argument, let
`b=H(t_0)_0`, `d=H(T_(m+1))_0`, and `s=H(t)_0-2`.
The displayed Laurent comparisons give

\[
JL_r\ge2(b-1)dsK,
\qquad y^2L_r\ge3(b-1)dsK_0.
\]

The weaker common constant is

\[
2(b-1)ds\ge\tfrac12 b^2 b_{m+1}d,
\]

which yields precisely

\[
c_m=\frac{27^3 6^{4m+2}}
{2(2m+3)(2m+5)^2(2m+7)}.
\]

Here the comparison `y^2>=x+2` is in the Laurent basis, as required;
it need not hold in the ordinary monomial basis. The statement clearly
specifies the basis.

## Uniformity in the outer length

The resolvent summands have the exact decomposition

\[
Z_i=A R_N+B\frac{R_N}{t-r_i}.
\]

All products have nonnegative Laurent coefficients. The omitted factor
has central coefficient at least `s>1`, while `B<=A`. Consequently
`A R_N<=Z_i<=2A R_N`, with a constant independent of `N`. This proves
the factor-two comparison with their convex average. It also remains
valid after common positive convolution.

Compatibility retains the squared residue weights. The estimates
`sum lambda_i^2>=1/N` and `H(F_i)>=H(F)/2` therefore give exactly the
factor `1/(4N)` in the normalized lower bound. The constant in the
correction estimate is conservative: averaging the individual
coefficient dominations already suffices, so the additional factor
two in `epsilon_N` is harmless.

Substitution of the lower bound for `s` into `E_t s/D_m` gives the
stated denominator

\[
128(m+3)^2(2m+5)(2m+7).
\]

Both occurrences of `(2m+7)/(2m+9)` in the consecutive ratio of
`E_m c_m` are required: one comes from the base normalized-product
denominator and the other from the coefficient-domination denominator.
Thus the ratio formula has no accidentally repeated or omitted factor.
The increasing scalar-factor argument correctly turns its exact
`m=77` gate into an infinite tail theorem.

## Perturbation and strictness

For a nonincreasing log-concave positive base row `f` and
`0<=g<=epsilon f`, dropping the favorable terms in the polarized
defect leaves at most `4 epsilon f_n^2` from the cross terms and
`2 epsilon^2 f_n^2` from the perturbation's own defect. This verifies
the sign and constants in the normalized perturbation bound, including
the reflected zero index. Positive supported defects together with
dense positive finite support imply the required cone property by the
existing folded criterion; no independent assertion that the correction
itself is cone is needed.

For the proxy, `R=y(x+2)^2` has maximum half-row entry 14, and

\[
W_n(J,R)\ge-14H(J)_n.
\]

Thus `mu_m>=28` yields the claimed comparison with
`V-(x+2)J/2`. Multiplication by the established cone kernel of `Z_N`
gives

\[
W_n(JZ_N,VZ_N)\ge\tfrac12\delta_n(JZ_N).
\]

The correction costs at most `epsilon_N H(JZ_N)_n^2`. The strict
normalized bound therefore proves the proxy inequality throughout the
support, including the last index.

Finally, the degrees in the original target satisfy

\[
\deg D_N-\deg S_N=(2m+5)N-m-3\ge m+2>0.
\]

The strict middle comparison has the same shorter degree as `S_N`, so
the final LR chain loses no supported target index. The case `N=0` is
correctly delegated to the old one-turn theorem with its opposite
endpoint orientation.

## Scope

This review supports the stated theorem for all `L^m R^2 L^ell`,
`m,ell>=0`, conditional on the explicitly identified prior foundation
theorems and exact certificates. It establishes no arbitrary-path
theorem. It is a separate mathematical check within the shared research
session, not external peer review or formal verification.
