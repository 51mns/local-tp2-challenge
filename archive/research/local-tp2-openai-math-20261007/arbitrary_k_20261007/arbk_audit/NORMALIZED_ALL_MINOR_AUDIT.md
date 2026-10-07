# Normalized folded defects control every ordered kernel minor

**Status: PROVED_INTERNAL; shared-session independent mathematical audit PASS.**
This note audits the normalized all-minor argument proposed by the root
researcher during the arbitrary-right-length continuation. No finite scan is
used in the proof. The inherited input is the already proved equivalence
between the folded defect criterion and total positivity of order two of the
folded multiplication kernel. This is a sufficient-condition lemma, not a
claim that all canonical prefixes satisfy its hypotheses.

## 1. Definitions and statement

Let `h=(h_0,...,h_D)` be a positive interval half-row, reflected at zero and
extended by zero outside `[-D,D]`. Define

\[
\Delta_n=h_n^2-h_{n-1}h_{n+1},\qquad
\delta_n=\Delta_n-\Delta_{n+1},\qquad
\eta=\min_{0\le n\le D}\frac{\delta_n}{h_n^2}.
\]

Assume all `delta_n>=0`. In the strict case `eta>0`; always `eta<=1`, since
`delta_D=h_D²`. The folded kernel is

\[
K(i,j)=\begin{cases}
h_j,&i=0,\\
2h_i,&j=0<i,\\
h_{|i-j|}+h_{i+j},&i,j>0.
\end{cases}
\]

For every `i<j` and `k<l`,

\[
\boxed{\det K[(i,j),(k,l)]\ge
\frac\eta4 K(i,k)K(j,l).}\tag{1}
\]

The constant is deliberately conservative. The proof keeps the boundary
row and column visible instead of identifying this kernel with an ordinary
Toeplitz kernel.

## 2. Adjacent minors, including the folded boundary

The cone criterion implies `h_0>=h_1>=...>=h_D>0` and ordinary log-concavity.
Indeed `Delta_n=sum_{r=n}^D delta_r>=0`, and the positive interval together
with `Delta_0=h_0²-h_1²>=0` gives the decreasing ratios. For supported `n`, put
`t_n=(h_(n-1)+h_(n+1))/h_n`. Then

\[
h_nh_{n+1}(t_{n+1}-t_n)=\delta_n\ge0.
\]

Write an adjacent minor as `ad-bc`, with `a` the upper-left entry.

* For row pair `(0,1)`, column pair `(v,v+1)`, its determinant is exactly
  `delta_v`, including `v=0`. Thus `ad-bc>=eta a²`. Its lower-right entry
  is `h_v+h_(v+2)<=2a`.
* For column pair `(0,1)` and row pair `(u,u+1)`, `u>0`, its determinant is
  `2delta_u`. Since `a=2h_u`, this is at least `eta a²/2`; its lower-right
  entry is `h_u+h_(u+2)<=a`.
* For interior pairs, put `a_0=|u-v|` and `b_0=u+v`, so `b_0>a_0`.
  If `b_0<D`, direct expansion gives

  \[
  \det K[(u,u+1),(v,v+1)]
  =\Delta_{a_0}-\Delta_{b_0+1}
  +h_{a_0}h_{b_0+1}(t_{b_0+1}-t_{a_0})
  \ge\sum_{r=a_0}^{b_0}\delta_r.
  \]

  The right side is at least `eta(h_(a_0)²+h_(b_0)²)`, hence at least
  `eta(h_(a_0)+h_(b_0))²/2=eta a²/2`. If `b_0=D`, the direct boundary
  formula is `Delta_(a_0)+h_(a_0)h_D`, with the same lower bound. If
  `b_0>D`, it is `Delta_(a_0)`, and `h_(b_0)=0`, again giving the bound.
  The lower-right entry is `h_(a_0)+h_(b_0+2)<=a`.

The statements with a zero upper-left entry are trivial by the exact band
support. Thus every adjacent minor with positive diagonal product satisfies

\[
ad-bc\ge\frac\eta2a^2,\qquad d\le2a,
\qquad\boxed{ad-bc\ge\frac\eta4ad.}\tag{2}
\]

## 3. Arbitrary rectangles

The positive support of `K` is exactly `|i-j|<=D`. If the two off-diagonal
corners of an ordered rectangle are positive, every entry in the rectangle
is positive: the largest and smallest values of `row-column` occur at those
two corners. In that case the exact telescoping identity is

\[
\frac{K(i,k)K(j,l)}{K(i,l)K(j,k)}
=\prod_{u=i}^{j-1}\prod_{v=k}^{l-1}
\frac{K(u,v)K(u+1,v+1)}{K(u,v+1)K(u+1,v)}.
\]

Every factor is at least one by the folded TP2 theorem. By (2), each factor
is also at least `1/(1-eta/4)`. Retaining one factor therefore proves (1).
If an off-diagonal entry is zero, the determinant equals its diagonal
product and (1) follows from `eta<=1`. If the diagonal product is zero,
TP2 forces the off-diagonal product also to be zero. This covers support
edges and degenerate rectangles without division by zero.

## 4. Relative comparison without a reference cone assumption

Let `b` be any **nonnegative** finite half-row, using the same reflection
and folded-kernel convention. It need not be decreasing, log-concave, or
in the folded cone. Suppose `h_n>=c b_n` for every index, where `c>0`.
Then `K_h>=cK_b` entrywise. Since the entries of `K_b` are nonnegative,

\[
\det K_b[I,J]\le K_b(i,k)K_b(j,l).
\]

Combining this with (1) proves

\[
\boxed{\eta(h)c^2\ge16
\quad\Longrightarrow\quad
\det K_h[I,J]\ge4\det K_b[I,J]
\quad\text{for every ordered }I,J.}\tag{3}
\]

Only nonnegativity of the reference row is required. It cannot be dropped:
for a signed reference `b=-M h`, the coefficient inequality is automatic,
whereas its two-by-two kernel determinants scale by `M²` and violate (3)
for sufficiently large `M`. This is the only necessary scope correction
to an unqualified claim that the reference needs no assumptions.

For a raw midpoint use `b=H(B)`; for a smoothed midpoint use `b=H(yB)`.
Both are nonnegative for the canonical positive seeds considered here.

