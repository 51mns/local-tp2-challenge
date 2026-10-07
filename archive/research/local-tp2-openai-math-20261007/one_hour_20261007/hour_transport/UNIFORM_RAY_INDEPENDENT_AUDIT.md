# Independent audit of the all-m, all-ell two-turn theorem

**Audit status: PASS.** The primary proof in
`../hour_root/UNIFORM_RAY_CLOSURE.md` establishes strict Local TP2 at every
canonical path `L^mR²L^ell`, for all integers `m,ell>=0`, using its stated
previously proved foundation lemmas. I independently reconstructed and
matched every finite ray-extension certificate, checked the unbounded
normalized argument, and checked the structural initial-order transport.

This is a shared-session internal audit. It is neither blind external
replication nor a proof-assistant verification. It does not establish the
full canonical-tree conjecture or paths `L^mR^kL^ell` for arbitrary `k>=3`.

## 1. Independent finite reconstruction

The primary generator builds ordinary polynomials from the root mutations,
then obtains Fourier coefficients by binomial expansion. The independent
script `audit_uniform_ray_closure.py` uses a different representation and
construction:

1. It constructs `u_m=U_m(x+3/2)` by the inner Chebyshev recurrence directly
   in the basis `1,q^n+q^-n`, with `x=q+q^-1`.
2. It constructs `T_m`, `t_0`, `a_X`, `A`, `B`, the endpoint `X`, and the
   center from their exact inner-seed identities. No original mutation
   implementation or primary certificate module is imported.
3. Products use direct symmetric Laurent convolution. No ordinary-`x`
   coefficient vector or binomial Fourier transform is constructed.
4. It evaluates each quadratic margin exactly at the parameter values
   `r=2,0,-2`, recovering twice the Bernstein coefficients as

   `2f(2), 4f(0)-f(2)-f(-2), 2f(-2)`.

   This is exact interpolation of a known quadratic, not a sign inference
   from three samples. It differs from the primary power-basis conversion.

For every `0<=m<=76`, the independent script recomputes all thresholds
`alpha_n,beta_n`, every selected folded-kernel minor, the trace mass gate,
all four initial-order lists, the complete coefficient digest, and the
complete primary record. Every record agrees exactly.

| Independently reconstructed item | Count | Result |
|---|---:|---|
| Initial indices `m` | 77 | Complete range `0,...,76` |
| Strictly positive Bernstein coefficients | 38,115 | Every value and ordering matched |
| Initial likelihood-ratio minors | 34,265 | All positive; every list digest matched |
| Initial-order SHA-256 digests | 308 | All four per initial index matched |
| Primary per-case records | 77 | Exact structural equality |
| Exact tail scalar values | 5 | Exact rational equality |

The result is recorded in `uniform_ray_closure_independent_audit.json`.
The original large certificate arrays remain in the primary result file;
the audit independently regenerates them and compares the entire records,
not merely their hashes or minima.

## 2. The finite bridge really covers every outer length

I checked the use of
`../hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md` in the primary
proof. Its hypotheses are supplied by the uniform seed, trace, and mixed
kernel theorems, together with the fixed-polynomial certificates just
reconstructed.

The relevant numerical choices are `gamma=2` and `rho=1/2`. In the prefix
resolvent each active summand has exactly `N-1` propagators, at most `N`
positive weights, and weights sum to one. Its proof retains
`sum lambda_i²>=1/N`; it does not replace squared weights by weights.
The elementary bound `2^(N-1)>=N` removes every dependence on an upper
cutoff for `N`.

The multiplier certificates include indices through `deg K_0+1`. The last
one is necessary because the polarization still contains the terminal
coefficient of `K_0`. The proxy certificates include the full range through
`deg K`, including the part above `deg J`; none of those indices is dropped.
Above `deg K`, the correction vanishes and the selected supported adjacent
kernel minor is positive through the final index of `JZ_N`.

These support checks justify applying the finite criterion to all
`N>=1`, not just to finitely many computed outer lengths.

## 3. Audit of the normalized smoothing lemma

The polynomial `y²` has half-row `(3,2,1)` and defects `(4,0,1)`. Its
normalized defect is zero, so applying the usual normalized-product theorem
directly with `y²` would give no useful bound. The primary proof avoids that
error with its separate lemma.

For a strict cone row `f` with `f_0<=C f_1`, Cauchy–Binet retains the
two positive minors of the `y²` kernel and gives

\[
\delta_n(y^2F)\ge4\delta_n(F)
+\det K_F[(2,3),(n,n+1)].
\]

For `n>=2`, the established interior folded-minor formula bounds the second
term below by `delta_(n-2)(F)`. Also `H(y²F)_n<=9f_(n-2)`. This applies
at both final indices `deg F+1,deg F+2`. For `n=0`, the first term and
`H(y²F)_0<=9f_0` suffice. For `n=1`, use
`f_1>=f_0/C` and `H(y²F)_1<=9f_0`. Thus

\[
\eta(y^2F)\ge\frac{\min(1,4/C^2)}{81}\eta(F).
\]

The canonical single block has `C=8`. Indeed, writing `a=H(yX)`,
`a_0<=2a_1` follows directly from nonnegativity of `H(X)`. For
`f=H(t-r)`,

\[
f_0\le6a_1+2\le4(3a_1-1)=4f_1.
\]

Decrease of `f` extends this central bound to
`K_f(i,0)<=4K_f(i,1)` for every input index. Multiplication by the
nonnegative row of `A` preserves it. Finally `B<=A(t-r)` gives
`H(L_r)_0<=8H(L_r)_1`. Therefore the claimed lower bound
`eta(y²L_r)>=eta(L_r)/1296` is valid.

## 4. Audit of the coefficient-domination constant

Let

\[
b_m=H(t_0)_0,\quad d_m=H(T_{m+1})_0,\quad
s_m=H(t)_0-2.
\]

The primary proof's central-convolution selections are valid:

\[
A=t_0a_X-u_m\ge(b_m-1)a_X
\ge(b_m-1)d_mK_0,
\]

\[
L_r\ge(b_m-1)d_ms_mK_0.
\]

The first subtraction is legitimate because `a_X>=u_m` before it is made.
The comparisons `J>=2y²X` and `y²>=p=x+2` are valid in the stated
Laurent-half-row order. In particular `H(y²-p)=(1,1,1)`; no claim of
ordinary-coefficient positivity for that difference is needed. Therefore

\[
JL_r\ge2(b_m-1)d_ms_mK,\qquad
y^2L_r\ge3(b_m-1)d_ms_mK_0.
\]

The lower bounds

\[
b_m\ge\frac{27\,6^m}{2m+5},\qquad
d_m\ge\frac{6^{m+1}}{2m+3},\qquad
b_m-1\ge b_m/2,\quad
s_m\ge b_mb_{m+1}/2
\]

give exactly

\[
c_m=\frac{27^3\,6^{4m+2}}
{2(2m+3)(2m+5)^2(2m+7)}.
\]

For the second central bound, decrease of the `T_(m+1)` half-row gives
`T_(m+1)(2)<=(2m+3)d_m`; the inner recurrence at `x=2` gives
`T_(m+1)(2)>=6^(m+1)`. Thus that bound is not an unsupported growth
assumption. Both resulting base polynomials dominate their fixed
corrections pointwise, at every coefficient index.

## 5. Audit of propagation through arbitrary N

The bound for `eta(J)` follows from its established strength and
`J(2)<=27216·49^m`; for `m>=3` its strength is at least
`(9/2)4^m`. Combining this with the normalized-product theorem gives
the stated base bound

\[
E_m=E_L(m)\frac{(4/49)^m}{6048(4m+14)}.
\]

It also lies below the smoothing bound from Section 3, so the same `E_m`
applies to both `C=J` and `C=y²`.

For each spectral summand `F_i=CZ_i`, the exact common leading term is
`C A R_N`. Since `B<=A` and every omitted trace has central coefficient
at least `s_m>1`,

\[
\tfrac12H(F)\le H(F_i)\le2H(F),\qquad F=CZ_N.
\]

This coefficient comparison has a constant independent of `N`. Repeated
normalized multiplication and central convolution give

\[
\eta(F_i)\ge E_m(E_t/D_m)^{N-1},\qquad
F_i\ge c_ms_m^{N-1}Q.
\]

All mixed minors are nonnegative. Retaining the squared diagonal weights
therefore gives

\[
\eta(F)\ge\frac{E_m}{4N}(E_t/D_m)^{N-1},\qquad
H(Q)\le\frac2{c_ms_m^{N-1}}H(F).
\]

The latter bound is conservative; averaging the stronger individual
domination would even remove its factor two. The weaker form used in the
primary proof is fully sufficient.

At `m=77`, the independently recomputed rational gates give
`E_mc_m>96`, `E_t s_m/D_m>2`, and `c_m>2`. Their subsequent ratios are
products of increasing positive rational factors and the displayed fixed
exponential factors. The first ratio is greater than 6 and the propagation
ratio greater than 11 at the threshold. Hence the gates hold at every
larger `m`. Combined with `2^(N-1)>=N`, they imply

\[
\eta(F)>12\varepsilon_N,\qquad
\varepsilon_N=2/(c_ms_m^{N-1})\le1
\]

for every unbounded outer index `N>=1`.

## 6. Audit of the actual multiplier and strict proxy

The multiplier proof applies the normalized perturbation inequality to a
**folded-cone dominant row** `F=y²Z_N` and the nonnegative correction
`K_0/3`. These hypotheses are established before the inequality is used.
The bound `eta(F)>12epsilon_N` retains a positive supported defect of the
actual multiplier `3F+K_0` at every index.

For the proxy, `V=pJ+R`, where `R=yp²` has half-row `(14,11,5,1)`.
Using decrease of `H(J)` and its strength `mu_m`,

\[
W_n(J,V-pJ/2)
=\delta_n(J)/2+W_n(J,R)
\ge(\mu_m/2-14)H(J)_n\ge0.
\]

The supported adjacent comparisons extend to every ordered minor because
both rows have positive interval support and the second degree is larger.
Common multiplication by the cone kernel of `Z_N` then yields

\[
W_n(JZ_N,VZ_N)\ge\delta_n(JZ_N)/2.
\]

This retains half of the actual normalized defect, not merely a weak
fixed strength. The possible negative correction is at most
`epsilon_N H(JZ_N)_n²`, so the strict normalized bound absorbs it. The
argument includes all indices above the correction support and the final
supported index.

## 7. Initial comparisons and return to the original determinant

I separately checked `../hour_invariant/ALL_M_INITIAL_COMPARISONS.md`
against `common_closure_20261004/reduction_common.md` in the earlier
research. The latter contains explicit valid four-link seeds at both
first-level children; its root exceptions are not ignored.

The companion transport uses only the parent's `G` kernel and the
parent's already established Local TP2 conclusion. Both are available
along every old one-turn path `L^mR^k`. The new two-turn conclusion is not
assumed. Hence the induction supplies the higher-endpoint companion
comparison at `L^mR²`. Old right-gap time order and old Local TP2 at that
same one-turn state then give all four initial comparisons required by
the new ray argument. This dependency is noncircular.

The weak sandwich sides follow by the exact gap recurrence, common
multiplication, and bilinearity against one fixed upper or lower row.
Together with the strict proxy and actual multiplier they give

\[
S_N\le_{lr}JZ_N<_{lr}\Pi M_N\le_{lr}D_N.
\]

The displayed degree formulas are consistent with the canonical child
ordering. In particular

\[
\deg D_N-\deg S_N=(2m+5)N-m-3\ge m+2>0.
\]

Thus ratio transitivity gives every interior strict determinant, and the
terminal determinant is a product of positive entries because the next
`S_N` entry vanishes while the next `D_N` entry is positive. The opposite
orientation at `N=0` is correctly delegated to the already proved
one-turn theorem with `k=2`.

## 8. Editorial corrections reported to the primary author

The audit found no remaining mathematical obstruction. It reported three
small precision fixes: use the actual initial-order note's filename;
identify the `b_mb_(m+1)>=14` condition with the first, rather than second,
inequality in the displayed pair; and state the cone hypothesis explicitly
when quoting the normalized perturbation inequality. None changes the
argument or any certificate.

The separately authored uniform mixed-kernel theorem is a dependency of
this audit and is being reviewed by another lane; this document does not
present a self-review of that theorem as independent verification.

## Reproduce the independent computation

```bash
python hour_transport/audit_uniform_ray_closure.py
```

Run from the parent of `hour_transport` and `hour_root`. The script uses
only the Python standard library and compares the primary JSON only after
independently constructing each candidate record. Its input location is
resolved relative to the script, so the package can be moved. It writes
its audit result under the current transport-work directory.
