# Exact finite-index continuum certificate for the midpoint

This file describes the finite part of the proof in
`fulltree_oneturn_normalized_tail.md`. It treats every integer
`1 <= m <= 390` and every independent `r,s,c in [-2,2]`.
The companion infinite argument treats all `m >= 391`.

Let `T_j=sum_(i=0)^j U_i(x+3/2)`, `y=x+1`,
`A=T_(m+1)`, `B=T_(m-1)`, and `t=3y²T_m+2x+3`.
The certified assertion is

\[
\delta_n\{A(t-r)(t-s)+B(t-c)\}
>8H(B)_0 H\{A(t-r)(t-s)+B(t-c)\}_n
\]

at every supported Fourier index. Thus these are continuum certificates
for a precisely bounded finite interval of inner indices. The final
all-index conclusion uses the separate analytic tail; it is not an
extrapolation from finite calculations.

## Bernstein construction

Set `r=-2+4u`, `s=-2+4v`, `c=-2+4w`, and `T=t+2`.
The half-row of the polynomial to be certified has the exact form

\[
h_n=F_n+P_n(u+v)+Q_nuv+R_nw,
\]

where `F=H(AT²+BT)`, `P=-4H(AT)`, `Q=16H(A)`, `R=-4H(B)`.
Each defect has degree at most two in each of the three parameters.
For Bernstein index `(a,b,c) in {0,1,2}³`, define the symmetric matrix

\[
M=\begin{pmatrix}
8&4(a+b)&2ab&4c\\
4(a+b)&8\binom a2+8\binom b2+4ab&4[b\binom a2+a\binom b2]&2(a+b)c\\
2ab&4[b\binom a2+a\binom b2]&8\binom a2\binom b2&abc\\
4c&2(a+b)c&abc&8\binom c2
\end{pmatrix}.
\]

This is eight times the tensor Bernstein coefficient functional applied
to the products of the basis `(1,u+v,uv,w)`. For example, the functional
on `u` is `a/2`, and on `u²` is `binom(a,2)`. The first row is also
eight times the coefficient functional on the four linear basis terms.

Apply this bilinear functional to

`h_n²-h_(n-1)h_(n+1)-h_(n+1)²+h_n h_(n+2)`

and subtract `8H(B)_0` times the linear functional on `h_n`.
Symmetry gives `h_(-1)=h_1`, and all indices outside the support are
zero. The script checks all 27 resulting integer margins at every
`0 <= n <= 3m+5`. Strict positivity of these coefficients proves the
assertion on the closed parameter cube, including its boundary.

## Exact computation

`fulltree_oneturn_finite.py` constructs the inner prefixes directly in
Laurent half-rows using the original Chebyshev recurrence. Polynomial
products use integer packing with base strictly larger than
`min(input lengths) * max(first input) * max(second input)`. Thus no
convolution coefficient can carry into its neighbor. All arithmetic is
Python arbitrary-precision integer arithmetic.

Run:

```bash
python3 fulltree_oneturn_finite.py --max 390
```

The JSON result contains the checked interval, each degree, the number
of margins, the exact minimum and its index, and a SHA-256 digest of
every margin in lexicographic order. Independent reconstruction is
documented in `fulltree_oneturn_finite_audit.md`.

Together with the analytic tail and the all-minor strength theorem,
this supplies the formerly missing uniform midpoint relative bound
`det K_H >= 4 det K_B`. It does not by itself prove all one-turn
Local TP2 comparisons or the full canonical tree.
