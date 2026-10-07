# Independent audit of the finite one-turn continuum certificate

The exact mathematical scope is the following. Put

\[
T_j(x)=\sum_{i=0}^j U_i(x+3/2),\quad y=x+1,\quad
A=T_{m+1},\quad B=T_{m-1},\quad
 t=3y^2T_m+2x+3,
\]
\[
P_{m;r,s,c}=A(t-r)(t-s)+B(t-c),\qquad r,s,c\in[-2,2].
\]
For each integer `1 <= m <= 390`, the primary certificate tests, at every
supported index `0 <= n <= 3m+5`,

\[
\delta_n\bigl(H(P_{m;r,s,c})\bigr)
   > 8H(B)[0]\,H(P_{m;r,s,c})[n]. \tag{1}
\]
Here `H` is the symmetric Fourier half-row, with negative indices reflected
and coefficients past the degree set to zero, and

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}.
\]

The optional smoothed certificate replaces `A,B` by `yA,yB`. Thus it tests
`y P_{m;r,s,c}`, degree `3m+6`, with the stronger corresponding threshold
`8H(yB)[0]`. It does not silently reuse the unsmoothed threshold.

## Algebraic and boundary audit

The substitution `r=-2+4u`, `s=-2+4v`, `c=-2+4w` maps the complete closed
parameter cube to `[0,1]^3`. With `q=t+2`, the polynomial to be transformed is

\[
Aq^2+Bq-4Aq(u+v)+16Auv-4Bw. \tag{2}
\]
Consequently every defect margin has degree at most two in each of the three
parameters. A complete tensor Bernstein certificate has exactly 27
coefficients. No correlation such as `c=(r+s)/2` is used or required.

For a parameter monomial `u^i v^j w^k`, its Bernstein coefficient at
`(a,b,c)` is

\[
\frac{\binom ai}{\binom2i}
\frac{\binom bj}{\binom2j}
\frac{\binom ck}{\binom2k},
\]
with value zero when a lower index exceeds its upper index. Multiplication
by 8 clears every denominator. Expanding (2) and applying this defining
formula independently reproduces the primary verifier's ten quadratic
weights and four linear weights. In particular, its off-diagonal polarized
terms already contain both orders, so the weight matrix must not contain an
additional factor of two. The supplied matrix has the correct convention.

The primary `prefixes` recurrence is multiplication by `2x+3` minus the
previous Chebyshev polynomial. Its reflected index at zero correctly counts
both Fourier contributions, giving `3h_0+4h_1`, not `3h_0+2h_1`.
`H(y^2)=(3,2,1)`, and adding 5 at index zero and 2 at index one gives
`t+2=3y^2 T_m+2x+5`, as required by (2).

At `n=0`, the negative index in the defect is `h_{-1}=h_1`; at the top two
indices, the missing coefficients are zero. Both implementations apply these
conventions explicitly. The degree is exactly `3m+5` (or `3m+6` after
smoothing), and the leading coefficient is `18*8^m`, independently checked
by the second implementation. Every index through that degree is included.

The factors `t-r,t-s,t-c` have positive ordinary coefficients throughout
the cube, with positive constant terms. Thus the polynomial has a dense
positive supported half-row. There is no unverified support or sign
hypothesis needed to interpret (1) as folded-kernel strength.

## Integer arithmetic audit

The primary Fourier multiplication expands the two full symmetric Laurent
rows. If their lengths are `a,b` and their maximum entries are `M,N`, each
convolution coefficient is at most `min(a,b)MN`. The chosen byte base is
strictly larger than this bound, so packed integer multiplication cannot
carry between coefficients. The extracted center index is the sum of the
two Laurent radii. All packed inputs are nonnegative; negative parameter
components are introduced only after multiplication. Python integers remove
any machine-word overflow issue.

The independent implementation uses ordinary `x` coefficients instead.
Its packing base is a power of two strictly exceeding the product of the
two coefficient sums. That bounds every ordinary product coefficient.
It checks the product's coefficient sum and that no encoded remainder is
left after extraction. This is a distinct coefficient basis and carry
bound, rather than a call to the primary Fourier convolution routine.

## Independent implementation

`fulltree_oneturn_finite_independent.py` imports no primary routines, arrays,
weights, or expected answers. It performs these steps:

1. Build `T_j` from the ordinary recurrence `(2x+3)U_j-U_{j-1}`.
2. Construct (2) with ordinary polynomial products. For `--smooth`, multiply
   both `A` and `B` by the ordinary polynomial `1+x` at this stage.
3. Transform ordinary coefficients using the defining binomial formula
   `H(x^j)[n]=binom(j,(j-n)/2)` when parity and support permit it.
4. Multiply the generic parameter polynomials in the five monomials
   `1,u,v,uv,w` to form the four terms of the defect. It does not use the
   primary polarized-defect shortcut.
5. Apply the defining rational Bernstein transform and subtract the linear
   strength term. Every arithmetic entry is a Python arbitrary-precision
   integer; NumPy object arrays merely organize those exact operations.
6. Test every coefficient's sign, independently record minima and witnesses,
   and hash the complete ordered list of exact integer margins.

The source theorem for normalized blocks, the tail inequality for
`m >= 391`, and any application to a canonical ray are separate mathematical
obligations. This finite certificate alone does not claim a full-tree Local
TP2 theorem.

## Replay record

The final full-run results and comparison record are appended after both
independent runs finish. The mathematical and implementation checks above
have no outstanding gap.
