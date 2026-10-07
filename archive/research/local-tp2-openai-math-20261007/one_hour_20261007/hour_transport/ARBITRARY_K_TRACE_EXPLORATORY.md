# A separate auxiliary trace lemma after arbitrary right-run length

**Status: PROVED_INTERNAL auxiliary theorem; independent mathematical and
finite-certificate audit PASS.** This is deliberately separate from the
completed and audited `L^mR²L^ell` Local TP2 proof. It is not an additional
dependency of that theorem and does not claim Local TP2 on the larger
three-run family. Its exploratory filename identifies that separate role.
The independent review is
`../hour_invariant/AUDIT_ARBITRARY_K_TRACE.md`.

The result concerns just the shifted and smoothed trace kernels at a
canonical center `C` on `L^mR^k`. The following argument proves their
strict folded-cone property for all `m,k>=0`, subject to the established
one-turn compatible-kernel and quantitative single-block theorems. The
boundary `m=0` is handled separately by pairing the explicit spectral roots.

## 1. Statement

Put `x=q+q^-1`, `y=x+1`, and let `C=C_(L^mR^k)` be the original canonical
center. For every `m,k>=0` and every real `r in [-2,2]`,

\[
\boxed{3yC-x-r\quad\hbox{and}\quad y(3yC-x-r)
\quad\hbox{are at least 1-strong}.}
\tag{1}
\]

Here `lambda`-strong means

\[
\delta_n(h):=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}
\ge\lambda h_n
\]

for each index in the positive interval support of
`h_n=[q^n]P(q+q^-1)`, with reflection at negative indices.

For `m>=1,k>=1`, outside eight explicitly listed small pairs, the following
stronger bound is obtained:

\[
\kappa_{m,k}=
\frac{2^{2m-4}}{k}\bigl(3\,2^{m-1}\bigr)^{k-1}-8>0.
\tag{2}
\]

The bound (2) is at least one whenever it is used. All statements are about
forward multiplication kernels in the original Fourier coefficient basis.

## 2. Central-ratio and smoothing-strength lemmas

### Lemma 2.1: two consecutive cone smoothings bound the central ratio

Suppose `F` and `yF` both have positive interval half-rows and belong to the
folded cone. Then `deg F>=1`, and

\[
\frac{H(F)_0}{H(F)_1}\le\frac{1+\sqrt{17}}2<3.
\tag{3}
\]

Write the first four coefficients as `a,b,c,d`. Cone membership of `F`
implies `a>=b>=c>=d>=0`. Direct expansion gives

\[
\delta_0(yF)=-a^2+ab+4b^2-3ac-2bc-2c^2+ad+2bd
\le-a^2+ab+4b^2.
\]

The inequality uses `d<=c`. Since the left side is nonnegative, `b>0`
and the quadratic gives (3). In particular a nonzero constant `F` cannot
satisfy these hypotheses.

### Lemma 2.2: quantitative smoothing by y²

If `F` is lambda-strong, `deg F>=1`, and `f_0<=3f_1`, then

\[
y^2F\quad\hbox{is}\quad\lambda/9\hbox{-strong}.
\tag{4}
\]

The half-row of `y²` is `(3,2,1)` with defects `(4,0,1)`. Retaining the
two positive minor contributions in Cauchy–Binet gives

\[
\delta_n(y^2F)\ge4\delta_n(F)
+\det K_F[(2,3),(n,n+1)].
\tag{5}
\]

At `n=0`, the new coefficient is at most `9f_0`, while the first term is
at least `4lambda f_0`. At `n=1`, the new coefficient is
`4f_1+2f_0+2f_2+f_3<=13f_1`, and the first term is at least
`4lambda f_1`. At `n>=2`, the interior folded-minor formula bounds the
second term below by `delta_(n-2)(F)>=lambda f_(n-2)`, and the new
coefficient is at most `9f_(n-2)`. This includes both final indices
`deg F+1,deg F+2`. Every case gives (4).

## 3. A fixed addition costs at most eight in strength

Let `h` have positive interval support, be lambda-strong, and have degree
at least three. Assume `lambda>8/3`. For every `a in [1,5]`,

\[
b=3h+(a,2,0,\ldots)
\quad\hbox{is}\quad(3\lambda-8)\hbox{-strong}.
\tag{6}
\]

If `deg h>=4` and also `h_0<=2h_1`, then the same assertion holds for

\[
b=3h+(a+4,a+2,2,0,\ldots).
\tag{7}
\]

These lemmas concern positive additions of fixed degree. They do not
assert closure of the cone under arbitrary positive sums.

For (6), the exact changes from `9delta_n(h)` are

\[
\begin{array}{c|l}
n&\delta_n(b)-9\delta_n(h)\\\hline
0&6ah_0-24h_1+3ah_2+a^2-8\\
1&12h_1-3ah_2+6h_3+4\\
2&-6h_3\\
n\ge3&0.
\end{array}
\]

Subtract `(3lambda-8)b_n`. Using decrease of `h` and the fact that every
supported coefficient is at least `lambda`, the margins are bounded below
by

\[
\begin{array}{c|l}
0&6ah_0+3a(h_2-\lambda)+a^2+8a-8\\
1&(36-3a)h_1+6(h_3-\lambda)+20\\
2&24h_2-6h_3\\
n\ge3&24h_n.
\end{array}
\]

Every line is positive for `a in [1,5]`.

For (7), the exact changes are

\[
\begin{array}{c|l}
0&(6a+30)h_0-(12a+24)h_1+(3a+12)h_2-a^2+2a+16\\
1&(6a+12)h_1-6h_0-(3a+24)h_2+(3a+6)h_3+a^2+2a-8\\
2&12h_2-3(a+2)h_3+6h_4+4\\
3&-6h_4\\
n\ge4&0.
\end{array}
\]

After subtracting `(3lambda-8)b_n`, the respective lower bounds are

\[
\begin{array}{c|l}
0&(30-6a)h_0+(3a+12)(h_2-\lambda)-a^2+10a+48\\
1&3ah_1+(3a+6)(h_3-\lambda)+a^2+10a+8\\
2&(30-3a)h_2+6(h_4-\lambda)+20\\
3&24h_3-6h_4\\
n\ge4&24h_n.
\end{array}
\]

At `n=1`, the bound uses `h_0<=2h_1`; everywhere else decrease suffices.
These quantities are positive on the prescribed interval. The script
verifies all displayed correction identities symbolically, including the
reflected central index and the first unaffected index.

## 4. Quantitative strength of the old one-turn prefix mixtures

Use the already proved one-turn notation

\[
T_j=\sum_{i=0}^jU_i(x+3/2),\quad
P=1+yT_m,\quad t=3yP-x,\quad
A=T_{m+1},\quad B=T_{m-1}.
\]

Write `R_k=sum_(j=0)^k U_j(t/2)` and

\[
Z_k=AR_k+BR_{k-1},\qquad C_{L^mR^k}=1+yZ_k.
\tag{8}
\]

The already established single-block theorem gives, for every `m>=1` and
all `r in [-2,2]`, the common strengths

\[
A(t-r)+B,\ y[A(t-r)+B]
\quad\hbox{are}\quad\lambda_L=3\,2^{2m-3}\hbox{-strong}.
\]

The established sharp trace theorem gives strength
`lambda_t=3·2^(m-1)` for every `t-r`. These are inputs from
`recovery_oneturn_closure.md` and its explicitly cited audited dependencies.

The positive Jacobi-resolvent representation of `Z_k` has at most `k`
active weights `omega_i>0` summing to one, and summands

\[
F_i=[A(t-r_i)+B]\prod_{j\ne i}(t-r_j).
\]

Every summand and every smoothed summand is
`lambda_L lambda_t^(k-1)`-strong. Their raw and smoothed mixed kernel
minors are nonnegative by the existing one-turn midpoint theorem. Since
`B<=A` and every shifted trace has central coefficient greater than one,

\[
AR_k\le F_i\le2AR_k,
\qquad\tfrac12Z_k\le F_i\le2Z_k
\tag{9}
\]

coefficientwise. These comparisons remain valid after multiplication by
`y`. Retaining the squared diagonal weights and using
`sum omega_i²>=1/k` gives the common strength

\[
\boxed{Z_k,\ yZ_k\quad\hbox{are}\quad
\Lambda_{m,k}=\frac{\lambda_L\lambda_t^{k-1}}{2k}
\hbox{-strong}.}
\tag{10}
\]

There is no upper bound on `k` in this argument.

## 5. Apply the lemmas to the actual center trace

Both `Z_k` and `yZ_k` belong to the cone. Since `y²` is a cone polynomial,
`y²Z_k` is also in the cone. Apply Lemma 2.1 first to `F=Z_k` and then
to `F=yZ_k`; both central ratios are below three. Lemma 2.2 and (10)
therefore give strength `Lambda_(m,k)/9` for both

\[
Q=y^2Z_k,\qquad yQ=y^3Z_k.
\]

The exact center identity (8) yields

\[
3yC-x-r=3y^2Z_k+(2x+3-r),
\]

\[
y(3yC-x-r)=3y^3Z_k+y(2x+3-r).
\]

The first correction has half-row `(a,2)` and the second
`(a+4,a+2,2)`, with `a=3-r in [1,5]`. The extra hypothesis of (7) is
automatic for `h=H(y³Z_k)`: if `p=H(y²Z_k)>=0`, then
`h_0=p_0+2p_1<=2(p_0+p_1+p_2)=2h_1`.

Equations (6)–(7) now give precisely the strength (2), whenever it is
positive. Positivity holds in the following four unbounded regions:

| Region | Smallest corner | Strength at that corner |
|---|---|---:|
| `m>=4,k>=1` | `(4,1)` | `8` |
| `m=3,k>=2` | `(3,2)` | `16` |
| `m=2,k>=3` | `(2,3)` | `4` |
| `m=1,k>=6` | `(1,6)` | `17/8` |

For a fixed `m`, the ratio of `lambda_t^(k-1)/k` at consecutive values is
`lambda_t k/(k+1)>=3/2>1`. The remaining increase with `m` is immediate
from (2). Hence the four corner checks rigorously cover their infinite
regions.

## 6. The eight remaining pairs

The exceptional pairs are exactly

\[
(m,k)=(1,1),\ldots,(1,5),(2,1),(2,2),(3,1).
\]

`explore_arbitrary_k_trace.py` reconstructs every center by the original
root mutations. For both the shifted trace and its product with `y`, it
forms `delta_n-h_n` at every supported index and computes the complete
degree-two Bernstein certificate over `r in [-2,2]`.

All **660 Bernstein coefficients for these eight pairs are strictly
positive**. The result file
`arbitrary_k_trace_exploratory_results.json` contains the full ordinary
centers, trace polynomials, coefficient arrays, minima, and all exact tail
corner values. The script also verifies **10 generic symbolic identities**
used in the central-ratio and fixed-addition lemmas. This proves the
remaining 1-strong cases with `m>=1,k>=1`.

## 7. The all-right boundary by paired spectral factors

At `m=0`, the old one-turn representation has

\[
t_*=3x^2+8x+6,\qquad A=2(x+2),\quad B=0,
\qquad Z_k=A R_k(t_*),\quad C=1+yZ_k.
\]

The two fixed seed rows are `H(A)=(4,2)` and `H(yA)=(8,6,2)`; they are
respectively 2-strong and 1-strong. Two small primitive kernel certificates
are enough for all remaining outer lengths:

\[
t_*^2+a t_*+b\quad\hbox{is 9-strong on}
\quad(a,b)\in[0,4]\times[-4,4],
\tag{11}
\]

\[
t_*-r\quad\hbox{is 1-strong for}\quad r\in[-2,0].
\tag{12}
\]

The script certifies (11) with all 45 degree-two tensor Bernstein
coefficients. They are nonnegative; the nine terminal coefficients are
zero because the leading coefficient is exactly 9, and all earlier
coefficients are positive. The polynomial has dense positive coefficients
throughout the box, so positive strength still gives strictly positive
supported defects. The complete nine univariate coefficients for (12)
are strictly positive. Both conversions are checked by exact reverse
evaluation.

To apply (11), use the prefix factorizations

\[
R_{2h}=\mathcal U_h\mathcal V_h,
\qquad R_{2h+1}=\mathcal U_h\mathcal V_{h+1},
\]

where `mathcal U_h(z)=U_h(z/2)` and
`mathcal V_h(z)=mathcal U_h(z)+mathcal U_(h-1)(z)`. The roots of
`mathcal U_h` occur in opposite pairs, with a zero root if `h` is odd.
The roots of `mathcal V_h` are

\[
r_j=2\cos\frac{2\pi j}{2h+1},\qquad j=1,\ldots,h.
\]

Pair the indices `j` and `h+1-j`. Their sum is negative, because

\[
r_j+r_{h+1-j}
=4\cos\frac{\pi(h+1)}{2h+1}
  \cos\frac{\pi(2j-h-1)}{2h+1}<0.
\]

An unpaired central root of `mathcal V_h` is also negative. If both outside
factors have an unpaired root, one is zero and the other is negative;
pair those two as well. Thus every `R_k` has a decomposition into exactly
`floor(k/2)` root pairs whose sums are nonpositive and at most one remaining
nonpositive root. For a pair `r,s`,

\[
(t_*-r)(t_*-s)=t_*^2+a t_*+b,
\qquad a=-(r+s)\in[0,4],\quad b=rs\in[-4,4].
\]

Equations (11)–(12) and multiplicative strength therefore prove

\[
Z_k,\ yZ_k\quad\hbox{are at least}\quad
9^{\lfloor k/2\rfloor}\hbox{-strong}.
\tag{13}
\]

The same central-ratio, smoothing, and fixed-addition lemmas now give
strength

\[
\frac{9^{\lfloor k/2\rfloor}}3-8\ge19
\qquad(k\ge4)
\]

for both target traces. The three remaining cases `(m,k)=(0,1),(0,2),(0,3)`
are reconstructed from the original mutations and have **153 additional
strictly positive Bernstein coefficients** for strength one.

This proves (1) for all `m>=0,k>=1`. For `k=0`, the center is `g_(m+1)`;
the already established pure-left shifted and smoothed trace theorems give
strength at least `3·2^m` and `3·2^(m-1)`, respectively. Both exceed one
for every `m>=0`. Thus (1) also includes the root and all pure-left states.

Across the eleven exceptional pairs and the two primitive kernel boxes,
the script certifies **867 exact Bernstein coefficients**: 813 strict
coefficients at the exceptional center traces, nine strict coefficients
for (12), and 45 nonnegative coefficients for (11). Nine of the latter
are exact terminal zeros.

The independent implementation
`../hour_invariant/audit_arbitrary_k_trace.py` reconstructs the original
mutations directly in full Laurent form and builds symbolic parameter
defects. It imports no author code. Its result JSON independently matches
every one of these 867 coefficients, including all nine terminal zeros.
The separate mathematical review checks the central-ratio, smoothing,
addition, mixture-strength, paired-root, and inherited `k=0` arguments.
The complete independent record is
`../hour_invariant/arbitrary_k_trace_independent_audit.json`.

## 8. Limit and potential use

The earlier notes `common_closure_20261004/invariant_shifted_trace_lemma.md`
and `common_transport_20261004/gap_shifted_trace.md` already give sufficient
conditions for an unsmoothed shifted trace, including a larger shift range
in the latter. They leave preservation of their normalized endpoint gate
open. The present auxiliary result verifies actual one-turn centers and
supplies the smoothed trace as well, with an explicit positive strength;
it is not a new claim that positive polynomial coefficients alone imply
the trace gate.

This lemma removes one particular obstruction to studying general
`L^mR^kL^ell`: the fixed endpoint's shifted and smoothed trace kernel is
available whenever that endpoint is the center of an old one-turn state.
It does not provide the new coupled seed compatibility,
midpoint comparison, normalized correction domination, or proxy surplus
for arbitrary `k`.

The one-factor strength at the inner `m=0` trace is too small for the
unpaired product estimate; the separate paired-root argument above is what
repairs this boundary. The full-tree Local TP2 status remains open.

Reproduce from the parent of `hour_transport`:

```bash
python hour_transport/explore_arbitrary_k_trace.py
```
