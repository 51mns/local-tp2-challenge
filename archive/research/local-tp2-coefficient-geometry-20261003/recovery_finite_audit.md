# Recovery audit: finite continuum certificates

**PASS, with the exact finite scope below.** All four previous computations had completed before the interruption. No finite range was missing; no extrapolation is used.

Let
\[
T_j=\sum_{i=0}^j U_i(x+3/2),\quad y=1+x,\quad
A=T_{m+1},\quad B=T_{m-1},\quad t=3y^2T_m+2x+3,
\]
\[
P=A(t-r)(t-s)+B(t-c),\qquad (r,s,c)\in[-2,2]^3.
\]
For each integer \(1\le m\le390\), at every supported Fourier index,
\[
\delta_n(H(P))>8H(B)_0 H(P)_n.
\]
The smoothed certificate proves the separate, stronger-threshold statement
\[
\delta_n(H(yP))>8H(yB)_0 H(yP)_n.
\]
Here \(\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}\), with \(h_{-n}=h_n\) and zeros outside support.

## Recovered run comparison

| Variant | m interval | Supported n | Cases | Strictly positive Bernstein margins |
|---|---:|---|---:|---:|
| Plain | 1–390 | 0 through 3m+5 | 390 | 6,239,025 |
| Smoothed by y | 1–390 | 0 through 3m+6 | 390 | 6,249,555 |

All 780 complete case records agree between the primary and independent implementations: degree, count, zero/negative count, minimum, witness, and SHA-256 digest of every ordered exact integer margin. There are no gaps or duplicate case indices. Across both variants the total is **12,488,580 distinct checked coefficients**, each also reproduced by the independent implementation. The global minimum of the eight-times-scaled Bernstein coefficients is 156672 in each variant. Every zero and negative count is zero.

The old plain result files predate the optional smoothing flag and omit `smooth:false`; their formula, degree, and fresh endpoint replay confirm that they are the plain variant. This is a metadata omission, not a mathematical gap.

Fresh recovery-time replays of **m=1 and m=390, for both variants and in both implementations**, match both saved files exactly. The full ranges were already computed twice before recovery; those full computations were not unnecessarily repeated. Source/result fingerprints, case-digest aggregates, and endpoint-replay records are in `recovery_finite_audit.json`.

## Continuum and arithmetic audit

The affine substitution \(r=-2+4u,s=-2+4v,c=-2+4w\) covers the independent closed cube, including its boundary. For \(q=t+2\),
\[
P=Aq^2+Bq-4Aq(u+v)+16Auv-4Bw.
\]
Each defect margin therefore has degree at most two in each parameter. The defining tensor Bernstein coefficient of \(u^iv^jw^k\) at \((a,b,c)\in\{0,1,2\}^3\) is
\[
\frac{\binom ai}{\binom2i}
\frac{\binom bj}{\binom2j}
\frac{\binom ck}{\binom2k}.
\]
Eight clears every denominator. The 27 coefficients checked at each Fourier index are thus an exact certificate over the continuum, not evaluations on a parameter grid. Positive Bernstein coefficients imply a positive margin because the Bernstein basis is nonnegative and sums to one on the entire closed cube.

The primary implementation uses the half-row of the Laurent recurrence. Multiplication by \(2x+3\) gives \(3h_0+4h_1\) at index zero, correctly accounting for reflection. The independent implementation constructs ordinary polynomials and uses the defining binomial transform \(H(x^j)_n=\binom{j}{(j-n)/2}\) with the parity condition. It expands generic parameter monomials instead of importing the primary polarized-defect formula or weight arrays. The inspected weight convention is correct: mixed polarized products already contain both orders, so no extra off-diagonal factor is required.

The two multiplication routines use different, sufficient carry bounds for packed arbitrary-precision integer products. All packed inputs are nonnegative; negative parameter components are introduced after multiplication. The independent routine also checks coefficient sums and the absence of leftover encoded digits. No machine-word or floating-point approximation enters a checked margin.

Both implementations explicitly reflect the negative index at n=0 and insert zero coefficients beyond the polynomial degree. Every index through the exact degree is included. The degree is 3m+5 (3m+6 after smoothing), and the leading coefficient is \(18\cdot8^m\). Positivity of the ordinary factors on the parameter cube supplies positive supported Fourier rows. Smoothing replaces both A and B and uses the corresponding threshold \(8H(yB)_0\), not the plain threshold.

## Scope boundary

This audit establishes the finite continuum certificate only. The tail m>=391, normalized folded-kernel strength theorem, and applications to canonical ray comparisons are separate proof obligations. This result alone is **not** a proof of all one-turn Local TP2 or of full-tree Local TP2.
