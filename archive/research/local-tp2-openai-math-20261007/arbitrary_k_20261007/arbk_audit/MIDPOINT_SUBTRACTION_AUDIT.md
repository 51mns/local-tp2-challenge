# The spectral midpoint requires two parameters, not a full cube

**Status: PROVED_INTERNAL; shared-session independent mathematical audit PASS.**
This validates a narrower sufficient condition for the actual Jacobi
spectral mixture. It does not claim that arbitrary three-parameter mixed
polynomials are in the folded cone.

Let `A,B` have nonnegative Laurent coefficients and let `t-r` have a
positive interval half-row for every `r in [-2,2]`. Put

\[
L_r=A(t-r)+B,\qquad
c=(r+s)/2,\qquad d=(r-s)/2.
\]

The midpoint of `L_r(t-s)` and `L_s(t-r)` is exactly

\[
H_{r,s}=A(t-r)(t-s)+B(t-c)
       =(t-c)L_c-d^2A.\tag{1}
\]

In particular `H_(r,s)` has a positive interval row whenever the original
positive-factor expression does. No third independent parameter occurs
in the spectral compatibility proof.

## Normalized subtraction bound

Suppose `F` is in the folded cone, `f=H(F)`, and
`0<=g=H(G)<=epsilon f` coefficientwise. Reflection at zero and zero
extension are used throughout. Expanding the defect of `f-g` gives

\[
\delta_n(f-g)=\delta_n(f)+\delta_n(g)
-2f_ng_n+f_{n-1}g_{n+1}+g_{n-1}f_{n+1}
+2f_{n+1}g_{n+1}-f_ng_{n+2}-g_nf_{n+2}.
\]

The three potentially negative cross contributions have total magnitude
at most `4epsilon f_n²`, because `f_(n+2)<=f_n`. The purely quadratic
term obeys

\[
\delta_n(g)\ge-g_{n-1}g_{n+1}-g_{n+1}^2
\ge-\epsilon^2(f_{n-1}f_{n+1}+f_{n+1}^2)
\ge-2\epsilon^2 f_n^2.
\]

Here the final step uses log-concavity and decrease of `f`, both consequences
of the folded cone criterion. The reflected case `n=0` satisfies the same
inequalities. Therefore

\[
\boxed{\delta_n(F-G)\ge
\delta_n(F)-(4\epsilon+2\epsilon^2)f_n^2.}\tag{2}
\]

If `F-G` has positive interval support and
`eta(F)>=12epsilon`, then `eta(F)<=1` gives `epsilon<=1/12`; hence
`4epsilon+2epsilon²<=6epsilon<=eta(F)/2`. Since `0<H(F-G)<=f`,

\[
\boxed{\eta(F-G)\ge\eta(F)/2.}\tag{3}
\]

For (1), take `F=(t-c)L_c`, `G=d²A`, and
`s_0=H(t)_0-2>0`. Then `H(t-c)>=s_0` at the central monomial, and

\[
F=A(t-c)^2+B(t-c)\ge s_0^2 A,
\qquad 0\le G\le\frac4{s_0^2}F.
\]

Thus a sufficient raw midpoint condition is

\[
\eta((t-c)L_c)\ge\frac{48}{s_0^2}\quad(-2\le c\le2).
\]

For the smoothed midpoint, replace `A,B,L_c,H_(r,s)` by
`yA,yB,yL_c,yH_(r,s)`. Exactly the same `epsilon=4/s_0²` applies, assuming
`(t-c)yL_c` is in the folded cone. This argument does not assume that `y`
itself is in the folded cone.

## Why this suffices for spectral compatibility

The paired spectral summands, after removing their common cone factors,
are `F_r=L_r(t-s)` and `F_s=L_s(t-r)`. Their midpoint is (1), and their
difference is `(r-s)B`. For any
ordered kernel minor, the coefficient of `ab` in
`det(a K_(F_r)+b K_(F_s))` equals

\[
2\det K_{H_{r,s}}-\frac{(r-s)^2}{2}\det K_B.
\]

Consequently `det K_H>=4det K_B` implies compatibility because
`(r-s)²<=16`; a negative reference determinant only helps. The normalized
all-minor lemma in `NORMALIZED_ALL_MINOR_AUDIT.md` supplies that relative
comparison from coefficient domination and a normalized defect bound.
The identical statement holds for the smoothed pair and reference `yB`.
