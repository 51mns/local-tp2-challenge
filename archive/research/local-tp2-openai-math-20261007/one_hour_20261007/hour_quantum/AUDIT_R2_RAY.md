# Independent audit of the all-ell R²L^ell theorem

**Verdict: PASS.** The proof in
`hour_invariant/THEOREM_R2_RAY.md` establishes the original strict Local
TP2 inequality at every canonical node `R²L^ell`, for every integer
`ell>=0`, using the stated inherited folded-kernel lemmas. No gap was
found in the new parameter certificates, low-index propagation, or
connection to the original rows. This conclusion is limited to the
displayed infinite family and does not assert full-tree Local TP2.

## Independent exact computation

The audit implementation is `audit_r2_ray.py`, with results in
`audit_r2_ray_results.json`. It imports **no code from the author lane**.
It reconstructs the canonical root and the two right mutations using
ordinary integer polynomials in `x`, then computes the Fourier half-rows
by binomial expansion. This differs from the author's direct full
Laurent-polynomial expansion. Both independently reconstruct the same
seed data, so the certificate comparison is anchored in the original
problem rather than in saved polynomial arrays.

Every one of the **993** degree-two tensor Bernstein coefficients in
the interval and cube certificates was independently recomputed and
compared exactly to the author's JSON. Every basis conversion was also
inverted by directly expanding its Bernstein basis functions, recovering
the original power coefficients. The dimensional degree bounds, all
supported output indices, and strict positivity were checked.

The independently reproduced smallest kernel margins are:

| Family | Minimum exact Bernstein margin |
|---|---:|
| `tau-r`, strength 1 | 306 |
| `L_r`, strength 1 | 104,652 |
| `yL_r`, strength 1 | 104,652 |
| `H_(r,s,c)`, strength 24 | 33,872,256 |
| `yH_(r,s,c)`, strength 56 | 33,685,632 |

The four `L_r` low-index margins after subtracting `40000L_r(2)` and
the propagator margin after subtracting `22(tau-r)(2)` matched in full.
The initial comparison rows and minors, the two strict proxy thresholds,
the multiplier polarization, and the complete original `ell=0` minor
list also matched exactly.

## Canonical identification and signs

The seed is correctly anchored at `R²`. The inverse center is the
original root center, so the preceding gap is `-yB`. This explains and
confirms the **plus** sign in

\[
q_N=y(Au_N+Bu_{N-1}),\qquad
C_N=P+y(AR_N+BR_{N-1}).
\]

For every `N>=1`, `deg X=4` and `deg C_(N-1)=1+5N>4`.
The next left center is therefore the shorter child. Subtracting the
two mutation formulas, as polynomial identities, gives exactly

\[
S_N=q_{N+1},\qquad D_N=(C_{N-1}-X)(3yC_N-x+1).
\]

The degree formulas in the proof are correct. In particular, the
single state `N=0` has the opposite endpoint orientation and is
properly handled separately. Its smallest exact original minor is
`1,994,544`, and all nine minors are positive.

## Relative compatibility and unbounded spectral mixtures

The strength constants are correctly matched to the references:
`H(B)=(3,2)` gives `24=8H(B)[0]`, and `H(yB)=(7,5,2)` gives
`56=8H(yB)[0]`. The whole-cube certificates and coefficientwise
domination therefore meet the inherited all-minor theorem's hypotheses.
This supplies the required factor-four relative bound at all infinite
kernel indices.

The polarized determinant identity

\[
\operatorname{mixed}(K_F,K_G)
=2\det K_{(F+G)/2}-\frac{(r-s)^2}{2}\det K_B
\]

is exact. The analogous identity with `yB` is also exact. Since
`|r-s|<=4`, the relative bound controls its only adverse term. Common
cone multiplication preserves this property by coefficient extraction
in Cauchy–Binet. Thus the proof uses a verified compatibility condition;
it does not assume closure under arbitrary addition.

The Jacobi matrices for the two Chebyshev families have simple roots
in `[-2,2]` and positive spectral residues summing to one. The prefix
factorizations correctly identify the active denominators. Each active
prefix summand has exactly `N-1` propagator factors, at most `N` active
weights occur, and `N=1` is included. The diagonal terms of the positive
mixtures give strict supported defects, with the correct common degree.
The separately certified smoothed midpoint makes the inclusion of the
factor `y` valid even for the small-degree cases.

## New low-index mass propagation

For two cone polynomials, retaining `(j,j+1)` in the finite
Cauchy–Binet expansion of `K_FK_G` proves

\[
\delta_j(FG)\ge\delta_j(F)\delta_0(G).
\]

The second determinant is an adjacent principal folded-kernel minor,
which is at least the central defect, including `j=0`. The selected
minor is within the valid supported range for all four indices used
in the proof. All omitted terms are nonnegative.

The mass ratio argument is valid: each summand's normalized mass lies
between `A(2)` and `2A(2)`, so it exceeds half of the weighted-average
mass. Crucially, the proof retains the **squares** of the residues and
uses `sum lambda_i²>=1/N`. Together with `22^(N-1)>=N`, this gives

\[
\delta_j(Z_N)>20000Z_N(2),\qquad j=0,1,2,3,
\]

for every `N>=1`. There is no finite-length extrapolation or omitted
initial run length.

## Exact multiplier and correction control

For `K_0=7+8x+3x²`, the half-row is `(13,8,3)`, its defects are
`(80,16,9)`, and the independently derived polarization terms are

\[
\begin{aligned}
\operatorname{Pol}_0&=29h_0-32h_1+13h_2,\\
\operatorname{Pol}_1&=-3h_0+16h_1-19h_2+8h_3,\\
\operatorname{Pol}_2&=6h_2-8h_3+3h_4,\\
\operatorname{Pol}_3&=-3h_4.
\end{aligned}
\]

The negative coefficient totals `(32,22,8,3)` are correct, and all
higher polarizations vanish. Multiplying by `y²` gives
`delta_j(y²Z_N)>=4delta_j(Z_N)` at the four indices. The mass bound
`h_i<=9Z_N(2)` then leaves the strictly positive common surplus

\[
9\cdot4\cdot20000-3\cdot32\cdot9=719136.
\]

The proof's treatment of the last two supported defects of `y²Z_N`
is valid: the selected `y²` kernel minors are both 1. Consequently
the exact multiplier `M_N=K_0+3y²Z_N` has positive supported defects
everywhere, without an addition-closure assumption.

## Strict proxy and original target

All four initial likelihood-ratio comparisons are valid at every
ordered pair because their rows have positive interval support, the
support degrees are ordered, and every adjacent comparison through the
smaller support is positive. The gap recurrence then propagates time
order, and summing rows above the fixed lower row proves the endpoint
comparison. The exact telescoping identity correctly gives
`S_N<=lr JZ_N` by subtracting rows below the same upper row.

The fixed `J,V` adjacent minors are all positive. The proxy thresholds
were independently reproduced as

\[
\frac{234515}{18}<20000,\qquad
\frac{7565}{6}<20000.
\]

The second threshold controls the extra correction index `n=7` using
`delta_1(Z_N)`. This is essential since `deg K=deg J+1`. At later
indices the correction vanishes, and the selected supported adjacent
kernel minor is strictly positive. The support inequality
`0<=n-6<=deg Z_N` includes the final index.

The chain

\[
S_N\le_{\rm lr}JZ_N<_{\rm lr}XpM_N\le_{\rm lr}D_N
\]

therefore gives the original strict minors on the interior support.
At the terminal `S_N` index, the original determinant is a product
of two positive entries because `deg D_N>deg S_N`. This completes
the required strictness and confirms that the theorem reaches the
actual Local TP2 statement, not merely an auxiliary kernel claim.

## Editorial note

The displayed uniform bound in Section 4 contains `Z_N(2)quad`; the
intended spacing command is `Z_N(2)\quad`. This is only a formatting
issue and has been reported to the author. No mathematical amendment
was needed for the verdict above.

