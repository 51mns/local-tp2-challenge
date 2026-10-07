# Review of the general finite ray-extension criterion

**Verdict: PASS as a sufficient-condition theorem.** The criterion in
`hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md` correctly extends
the two audited concrete proofs to any canonical prefix satisfying its
explicit finite gates. It does not assert that every prefix satisfies
those gates. The shared folded-kernel foundation and the unbounded
resolvent assembly are the same verified inputs as in the two family
proofs; the following newly generalized points were checked separately.

## 1. Exact mass ratio

The normalized summand mass is

\[
A_*+\frac{B_*}{\tau-r},\qquad -2\le r\le2,
\]

with `A_*>0`, `B_*>=0`, and `tau>2`. It is increasing in `r`.
Its exact minimum and maximum are therefore
`A_*+B_*/(tau+2)` and `A_*+B_*/(tau-2)`. The ratio `rho` in
the criterion proves `Z_i(2)>=rho Z_N(2)` by comparison with the
positive weighted average. This includes `B=0`, for which `rho=1`.
No assumption on the location of individual roots beyond `[-2,2]`
is used.

## 2. The finite minimum for every gamma greater than one

For `f_N=gamma^(N-1)/N`,

\[
\frac{f_{N+1}}{f_N}=\frac{\gamma N}{N+1}.
\]

This ratio is less than one when `N<1/(gamma-1)` and greater than
one when `N>1/(gamma-1)`. Hence the global integer minimum is
attained at

\[
N_*=\max(1,\lceil1/(\gamma-1)\rceil).
\]

If `1/(gamma-1)` is an integer, there is a tie at that integer and
the next one; the displayed choice still gives the exact minimum.
For `gamma>=2`, it correctly reduces to `eta=1`. Thus the general
rate compensates for the retained squared-residue factor `1/N`
without an unproved monotonicity assumption near `N=1`.

## 3. Allowing negative defects of the fixed base multiplier

The exact polarization gives

\[
\delta_n(M_N)\ge
(9\theta\beta_n-27\nu_n)Z_N(2)+\delta_n(M_0),
\quad\nu_n=m_{n-1}+3m_{n+1}.
\]

For `tau>2`, the Chebyshev sequence and its prefix sums are positive
and increasing. Since `A_*>0,B_*>=0`, `Z_N(2)>=Z_1(2)>0` for
every `N>=1`. The finite gate

\[
9\theta\beta_n>
27\nu_n+\frac{\max(-\delta_n(M_0),0)}{Z_1(2)}
\]

therefore absorbs a negative constant defect at the smallest possible
mass and stays strict at every later run length. If the base defect
is nonnegative, the same gate leaves a strictly positive coefficient
of the mass. This correctly removes the unnecessary requirement that
`M_0` itself be in the cone while retaining its required nonnegative
coefficient support.

If `m=deg M_0`, the only possible last negative polarization occurs
at `n=m+1`, through `-m_mh_(m+2)`. For `n>=m+2`, every base and
polarization term vanishes. The stated finite range includes precisely
the needed support boundary.

## 4. Canonical degree and support bookkeeping

With `a=deg X`, `b=deg Y`, and `h=a+1`, the criterion's equations give

\[
\deg Z_N=a+b+Nh,\qquad
\deg C_{N-1}=b+Nh>a\quad(N\ge1).
\]

The degree of the `B` contribution is strictly smaller by the explicit
gate `deg B<deg A+h`, so the leading terms cannot cancel. The actual
short child is therefore correctly identified. The target degrees are

\[
\deg S_N=2a+b+2+Nh,\qquad
\deg D_N=a+2b+2+2Nh.
\]

Their difference is

\[
b+Nh-a=b+1+(N-1)h>0.
\]

Also `e-d=b` is correct for the fixed proxy correction. The additional
indices `d+1,...,e` are included explicitly in the nonprincipal-template
gate; none is lost at the support edge. Even at `N=1`,
`deg S_N-e=2a+1>0`, so every low correction index occurs within the
required target support.

The proof of strictness for `y²Z_N` uses `deg Z_N>=1`. This follows
from `N>=1,h>=1`, even at the smallest allowed degrees. Hence the
last two indices are at least 2, and the selected kernel rows `(2,3)`
are valid for the stated lower bound. No degree-zero exception is
silently used.

## 5. Remaining assembly

The raw compatibility identity, both alternative smoothing mechanisms,
the active-residue count, nonprincipal Cauchy–Binet propagation,
initial-order transport, strict proxy absorption, and final terminal
determinant agree with the two independently checked family proofs.
The gates contain no later-ray Local TP2 conclusion and no assumed
universal mutation closure.

The theorem is therefore a valid finite, reviewable sufficient
certificate for an unbounded canonical ray. Whether the gates hold
uniformly as the prefix varies remains a separate mathematical task.

