# A uniform normalized-defect tail for every inner index

This proves the arbitrary-inner-index midpoint obligation for every integer
`m >= 391`, uniformly over the **entire independent cube** `r,s,c in [-2,2]`.
The indices `1 <= m <= 390` are an explicitly bounded finite continuum
certificate obligation, not assumed in this note.

Write `x=q+q^-1`, `y=x+1`,

\[
T_m=\sum_{j=0}^mU_j(x+3/2),\qquad
t=3y^2T_m+2x+3,\qquad A=T_{m+1},\quad B=T_{m-1},
\]
\[
F=A(t-r)(t-s),\qquad G=B(t-c),\qquad H=F+G,
\qquad b_0=H(B)[0].
\]

The conclusion is that `H` is `8 b_0`-strong. In particular its folded
multiplication kernel is TP2 and, by the already proved all-minor strength
theorem, every ordered minor satisfies `det K_H >= 4 det K_B`.

## 1. Normalized defects and product closure

For a positive supported Laurent half-row `h`, put

\[
\eta(h)=\min_{0\le n\le\deg h}\frac{\delta_n(h)}{h_n^2}.
\]

If `P,Q` are folded-cone polynomials of degrees `p,q`, then

\[
\eta(PQ)\ge
\frac{\eta(P)\eta(Q)}{2(\min(p,q)+1)}. \tag{1}
\]

Here is the boundary-aware proof of the constant 2. Every adjacent minor
of `K_Q`, with upper-left entry `K_Q(i,j)`, is at least
`eta(Q) K_Q(i,j)^2/2`. For row zero the minor is `delta_j(Q)` and
`K_Q(0,j)=q_j`; for column zero it is `2 delta_i(Q)` and
`K_Q(i,0)=2q_i`. For positive row and column indices put
`a=|i-j|`, `b=i+j`; then `b>=a+2`. The folded-cone characterization writes
this minor as

\[
\sum_{\ell=a}^{b}\delta_\ell(Q)+C_{a,b},\qquad
C_{a,b}=q_a(q_b+q_{b+2})-(q_{a-1}+q_{a+1})q_{b+1}\ge0.
\]

The last inequality is precisely the monotonicity of
`(q_(j-1)+q_(j+1))/q_j` in the positive support; beyond it the displayed
formula directly has the same sign. Thus the minor is at least

\[
\eta(Q)(q_a^2+q_b^2)
\ge\tfrac12\eta(Q)(q_a+q_b)^2.
\]

Use `K_(PQ)=K_P K_Q` and retain the intermediate adjacent pairs in
Cauchy--Binet for rows `(0,1)` and columns `(n,n+1)`. All omitted terms
are nonnegative. This gives

\[
\delta_n(PQ)\ge\frac{\eta(P)\eta(Q)}2
\sum_{k=0}^{p}\bigl(p_kK_Q(k,n)\bigr)^2
\ge\frac{\eta(P)\eta(Q)}{2(p+1)}H(PQ)[n]^2.
\]

Interchange the two factors for (1). No arbitrary-sum closure is used.

## 2. Explicit normalized bounds on all inner prefixes

Set

\[
\sigma=\frac{59}{100},\qquad c_0=\frac1{400000000}.
\]

Then, for every `m>=1`,

\[
\eta(T_m)\ge c_0\sigma^m,\qquad
\eta(y^2T_m)\ge c_0\sigma^m. \tag{2}
\]

The exact certificate `fulltree_normalized_block.cpp` with its result
`fulltree_normalized_block_results.json` proves that a product of eight
independent factors

\[
f_{u,v}=x^2+(3+u)x+\tfrac54+\tfrac52u+v,
\quad 0\le u,v\le1,
\]

has normalized defect strictly greater than `1/128`. There are 12870
distinct tensor-Bernstein histograms and 218790 positive margins; the
permutation symmetry represents every Bernstein coefficient, without
parameter sampling.

Group the removed quartics in the existing eight-case prefix
factorization into groups of four quartics, hence groups of eight
quadratics and degree 16. The remaining residue has degree
`d=d_base+4r<=18`, where `0<=r<=3` and `d_base<=6`. The sharp-strength
certificates and product closure show that the scaled residue has
strength `2^(d-1)` for `T_m`, and strength `2^d` after multiplication by
`y^2`. Every monic linear residue factor has value at 2 at most `9/2`;
every monic quadratic residue factor has value at 2 at most `(9/2)^2`.
These inequalities follow directly from the listed residue boxes. The
residue masses therefore give normalized bounds

\[
\eta(R_T)\ge\frac1{2(9/2)^d},\qquad
\eta(R_P)\ge\frac1{9(9/2)^d}. \tag{3}
\]

If there are `k` degree-16 blocks, (1) loses at most a factor 34 on each
multiplication, since one factor has degree 16. Thus the product has
normalized defect at least its residue bound times `(1/4352)^k`.
The following exact rational inequalities prove (2), since `m=d+16k`:

\[
4352\sigma^{16}<1,\qquad
9c_0((9/2)\sigma)^{18}<1. \tag{4}
\]

The case `m=1` follows directly from the already recorded rows of
`T_1` and `y^2T_1` and satisfies the same very conservative constants.

## 3. Shifted traces retain half the normalized margin

For every `m>=21` and `r in [-2,2]`,

\[
\eta(t-r)\ge\tfrac12c_0\sigma^m. \tag{5}
\]

Write `h=H(y^2T_m)`, `eta=c_0 sigma^m`, and `a=3-r in [1,5]`.
The shifted trace row is
`b_0=3h_0+a`, `b_1=3h_1+2`, `b_n=3h_n` for `n>=2`.
Every monic factor in the established prefix boxes dominates the
corresponding power of `y` coefficientwise in the ordinary `x` basis.
Consequently `T_m >= 2^m y^m`. Taking the `q^2` term of `y^2` and the
central term of `y^m` gives

\[
h_2\ge\frac{6^m}{2m+1}.
\]

The central trinomial coefficient is at least the average of its
`2m+1` supported coefficients; their sum is `3^m`. Exact arithmetic
at `m=21`, followed by a ratio greater than one, gives

\[
\eta h_2\ge c_0\frac{(6\sigma)^m}{2m+1}\ge8.
\tag{6}
\]

Also `h_0>=20` and `h_1>=8`. The previously proved trace defect
identities imply

\[
\begin{aligned}
\delta_0(b)&\ge9\eta h_0^2-24h_0-8
             \ge\tfrac{23}4\eta h_0^2,\\
\delta_1(b)&\ge9\eta h_1^2-15h_1
             \ge\tfrac{57}8\eta h_1^2,\\
\delta_2(b)&\ge9\eta h_2^2-6h_2
             \ge\tfrac{33}4\eta h_2^2.
\end{aligned}
\]

Since `b_0<=13h_0/4`, `b_1<=13h_1/4`, and `b_2=3h_2`, the normalized
margins are at least `92eta/169`, `114eta/169`, and `11eta/12`.
All are at least `eta/2`. The higher margins equal the normalized
margins of `h`, proving (5).

Combining (2), (5), and (1) twice now yields

\[
\eta(F)\ge E_m:=
\frac{c_0^3\sigma^{3m+1}}{16(m+2)(m+3)}
\qquad(m\ge21). \tag{7}
\]

## 4. Uniform coefficient domination of the correction

Let `t_0=H(t)[0]`. The same coefficient domination and the average
central-trinomial bound give

\[
t_0\ge\frac{27\,6^m}{2m+5}.
\]

Write `t=t_0+R`, with `R` Laurent nonnegative and central coefficient
zero. For

\[
\kappa=\frac{(t_0-2)^2}{t_0+2},
\]

the Laurent polynomial

\[
(t-2)^2-\kappa(t+2)
=[2(t_0-2)-\kappa]R+R^2
\]

has nonnegative coefficients. Also `A>=B` coefficientwise,
`(t-r)(t-s)>=(t-2)^2`, and `t-c<=t+2`. Hence `F>=kappa G`
coefficientwise. As `t_0>=6`, one has `kappa>=t_0/3`, and therefore

\[
0\le g_n\le\epsilon_m f_n,\qquad
\epsilon_m:=\frac{2m+5}{9\,6^m}<1. \tag{8}
\]

## 5. Absorbing the mixed defect, including the support boundary

If `F` is in the folded cone and `0<=g_n<=epsilon f_n`, symmetry,
log-concavity and decrease of the row `f` give

\[
\delta_n(F+G)\ge\delta_n(F)
                  -(4\epsilon+2\epsilon^2)f_n^2. \tag{9}
\]

Indeed the negative mixed terms are bounded below by
`-2epsilon(f_(n-1)f_(n+1)+f_(n+1)^2)>=-4epsilon f_n^2`;
the two negative terms of `delta_n(G)` are bounded below by
`-2epsilon^2 f_n^2`. All omitted terms are nonnegative. This proof
does not even require `G` to be in the folded cone. It applies unchanged
at zero and at either support boundary.

The exact rational verifier accompanying this note checks

\[
E_{391}\ge12\epsilon_{391}.
\]

The ratio of `E_m/(12epsilon_m)` at consecutive integers is

\[
6\sigma^3\frac{(m+2)(2m+5)}{(m+4)(2m+7)}.
\]

It is increasing in `m` and exceeds one already at 391. Thus
`E_m>=12epsilon_m` for every `m>=391`. Equations (7)--(9) imply

\[
\delta_n(H)\ge\tfrac12\delta_n(F)
\ge\tfrac12\lambda_F f_n
\ge\tfrac14\lambda_F h_n,
\qquad \lambda_F=9\,2^{3m-2}.
\]

Finally, the established prefix mass bound gives
`b_0 <= (7^m-1)/6`. The exact inequality
`lambda_F >= 32(7^m-1)/6` holds for every `m>=7`: check 7 and use
`8(7^m-1)-(7^(m+1)-1)=7^m-7>=0` to propagate the inequality.
Consequently

\[
\boxed{\delta_n(H)\ge8b_0 h_n}
\]

through the entire support, for every `m>=391` and every parameter in
the independent cube. Since `H>=F>=B`, the all-minor strength theorem
supplies the relative minor conclusion stated at the beginning.

The file `fulltree_oneturn_normalized_tail.py` verifies all exact scalar
thresholds and records their values. This is an infinite argument with
a finite explicit remaining inner-index interval; the interval is not
silently supplied by numerical evidence.
