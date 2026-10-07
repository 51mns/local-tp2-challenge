# An infinite Chebyshev-ray Fourier MLR theorem

**Later update:** The original all-left Local TP2 comparison left open at this stage is now proved in `resumed_comparison_all_left.md`, audited in `resumed_audit_all_left.md`. The full tree remains open. The earlier derivations below are retained as proof ingredients.

This note proves a genuine infinite statement, conditional only on the separately proved folded-kernel product-closure lemma in `continuation_kernel/folded_kernel_theorem.md`. It does **not** yet prove the original Local TP2 comparison between the ray's `D` and `S`.

## Theorem

Let

`p_m(x)=(x+1)U_m(x+3/2)`,

where `U_m` is the standard Chebyshev polynomial of the second kind. Let

`a_m(n)=[q^n]p_m(q+q^{-1})`,

extended symmetrically to negative `n` and by zero outside the support. Then for every integer `m>=1` and `0<=n<=m+1`,

`a_{m+1}(n+1)a_m(n)-a_{m+1}(n)a_m(n+1)>0`.

Explicit lower bounds are `24` at `n=0`, `2` at `n=1`, and `2*4^(n-1)` for `2<=n<=m+1`.

The restriction `m>=1` is necessary: `a_0=(1,1)` and `a_1=(7,5,2)` have first adjacent minor `-2`.

## Folded-kernel cone used in the proof

For a dense symmetric nonnegative Laurent row `h`, set

`Delta_h(n)=h(n)^2-h(n-1)h(n+1)`,

`delta_h(n)=Delta_h(n)-Delta_h(n+1)`.

The folded-kernel theorem establishes that `delta_h(n)>=0` for all `n>=0` is equivalent to TP2 of the folded convolution kernel. Since kernels compose under multiplication of symmetric Laurent polynomials, this class is closed under polynomial multiplication. Only nonnegative product closure is needed below; strict product closure is available but unnecessary for the final strictness argument.

## Five exact blocks

Put `y=x+1`, `z=x+3/2`, `f_c=x²+3x+c`, and let `5/4<=c,d<=9/4`. Every one of the following polynomials has **strictly positive** `delta_H(P)(n)` throughout `0<=n<=deg P`:

| Block | Polynomial | Certified lower bounds, in order `n=0,...,deg P` |
|---|---|---|
| B0 | `yz` | `13/4, 7/4, 1` |
| B1 | `yf_c` | `159/16, 109/16, 27/4, 1` |
| B2 | `f_cf_d` | `19633/256, 2857/32, 267/4, 35/2, 1` |
| B3 | `yf_cf_d` | `62335/256, 176361/256, 13491/32, 603/4, 47/2, 1` |
| B4 | `yzf_c` | `2909/64, 6867/64, 435/8, 14, 1` |

These are exact polynomial certificates over an entire real parameter box, not checks at finitely many parameter values. Substitute `c=5/4+u`, `d=5/4+v`, with `u,v` in `[0,1]`. Each defect is a polynomial `P(u,v)`. Express it in its bivariate Bernstein basis of degrees `(r,s)`:

`P(u,v)=sum_(i=0)^r sum_(j=0)^s b_ij binom(r,i)u^i(1-u)^(r-i) binom(s,j)v^j(1-v)^(s-j)`.

All basis functions are nonnegative and their sum is one. Every exact rational coefficient `b_ij` is positive. The lower bounds in the table are the minimum Bernstein coefficient of each corresponding defect. The complete coefficient arrays, with their power-basis polynomials, are recorded in `continuation_ray_certificates.json`; the standalone standard-library Python script `continuation_ray.py` regenerates and asserts them using rational arithmetic only.

For audit, if `P=sum p_ab u^a v^b`, the script uses the exact change-of-basis formula

`b_ij=sum_(a<=i,b<=j) p_ab * binom(i,a)/binom(r,a) * binom(j,b)/binom(s,b)`.

For example, the three nonterminal defects of B1 are

`24-4c-c²`, `c²+9c-6`, `9-c`;

its terminal defect is `1`. Their listed rational bounds follow immediately on the parameter interval and also from the recorded Bernstein coefficients.

## Factorization proves cone membership for every m

The Chebyshev roots are `cos(j*pi/(m+1))`, `j=1,...,m`. Pairing the roots with opposite cosines gives

`U_m(x+3/2)=2^m product_j f_(c_j)(x)` when `m` is even,

and

`U_m(x+3/2)=2^m z product_j f_(c_j)(x)` when `m` is odd,

where each `c_j=9/4-cos²(j*pi/(m+1))` belongs to `[5/4,9/4]`.

Therefore, apart from its positive scalar `2^m`, `p_m` factors as follows:

| m | Block factorization |
|---|---|
| `4t+1` | one B0 and `t` B2 blocks |
| `4t+2` | one B1 and `t` B2 blocks |
| `4t+3` | one B4 and `t` B2 blocks |
| `4t+4` | one B3 and `t` B2 blocks |

The `c_j` values can be assigned arbitrarily to the displayed blocks because their certificates hold on the full parameter box. Product closure now gives

`delta_(a_m)(n)>=0` for all `m>=1`, `n>=0`.

This is an infinite algebraic proof: there is no truncation in `m`.

## Christoffel–Darboux gives strict MLR

The Chebyshev Christoffel–Darboux identity, multiplied by `(X+1)(Y+1)`, gives

`p_(m+1)(X)p_m(Y)-p_m(X)p_(m+1)(Y)=2(X-Y)sum_(j=0)^m p_j(X)p_j(Y)`.

Set `X=q+q^{-1}` and `Y=r+r^{-1}`, then take the coefficient of `q^(n+1)r^n`. Symmetry of the Fourier rows gives exactly

`a_(m+1)(n+1)a_m(n)-a_(m+1)(n)a_m(n+1)=2sum_(j=0)^m delta_(a_j)(n)`.

The only exceptional row is `p_0=y`, for which

`delta_(a_0)=(-1,1,0,0,...)`.

For `p_1=y(2x+3)`, the Fourier row is `(7,5,2)` and

`delta_(a_1)=(13,7,4,0,...)`.

Hence at `n=0`, the sum is at least `-1+13=12`; at `n=1`, it is at least `1`. If `2<=n<=m+1`, use the term `j=n-1`: since `deg p_j=j+1=n` and its leading coefficient is `2^j`, its terminal defect is exactly `4^(n-1)>0`. Every other included term is nonnegative. This proves the theorem and all stated strict lower bounds.

## Positive transfer matrix (independent exact representation)

Let `A(q)=[[1+q,1],[q,1]]`, and `M(q)=A(q)A(q^{-1})`. Then

`M=[[2+q+2q^{-1},2+q],[1+q+q^{-1},1+q]]`,

`det M=1`, `tr M=3+2(q+q^{-1})`, and `M_21=1+q+q^{-1}`.

Cayley–Hamilton yields

`p_m(q+q^{-1})=(M(q)^(m+1))_21`.

Thus these Laurent rows also admit a positive finite-state path model. Its existence alone would not establish the theorem, as the `m=0` counterexample shows; the proof above uses factorization and the folded cone.

## Two further exact comparison lemmas

Write `f >=lr g` when all ordered supported Fourier-row minors have the nonnegative orientation `f(j)g(i)-f(i)g(j)>=0` for `i<j`. All multiplier polynomials below have finite nonnegative symmetric Laurent coefficient rows.

### Symmetric-index broadening

For `m>=1` and `1<=r<=m`,

`p_(m+r)+p_(m-r)=2 C_r(x+3/2) p_m`,

where `C_r` denotes the Chebyshev polynomial of the first kind (distinct from the prefix sums `T_k` below). This follows from the sine addition identity for `U_m`, or directly from their recurrences. Every root of `C_r(x+3/2)` is negative, so its positive-leading-coefficient polynomial has strictly positive ordinary coefficients and hence nonnegative Fourier coefficients.

The row supported only at index zero is below any finite nonnegative row in non-strict MLR order. Applying the TP2 folded multiplication kernel of `p_m` therefore proves

`H(p_(m+r)+p_(m-r)) >=lr H(p_m)`.

In particular, defining `W(f,g;n)=H(f)[n+1]H(g)[n]-H(f)[n]H(g)[n+1]`,

`W(p_(m+r),p_m;n) >= -W(p_(m-r),p_m;n)`.

This does not require `p_0` itself to lie in the folded cone.

### Uniform coefficientwise growth

For all `l>=0` and all integer `n`,

`a_(l+1)(n)>=4 a_l(n)`.

Here is an exact proof using the transfer matrix. Put `(f_l,g_l)^T=M^(l+1)(1,0)^T`, so `g_l=p_l(q+q^{-1})`. All matrix entries have nonnegative Laurent coefficients, and the first row of `M` minus its second row is `[1+q^{-1},1]`. Consequently `f_l>=g_l` coefficientwise. The second row update is

`g_(l+1)=(1+q+q^{-1})f_l+(1+q)g_l`,

so

`a_(l+1)(n)>=a_l(n+1)+2a_l(n)+2a_l(n-1)`.

For `l>=1`, folded-cone membership implies `Delta_(a_l)(n)>=0`, by summing the nonnegative defects to the zero tail. Thus the symmetric row is log-concave and unimodal. At `n>=1`, `a_l(n-1)>=a_l(n)`, giving the stated factor `4`. At `n=0`, the already-proved MLR theorem gives

`a_l(1)/a_l(0)>=a_1(1)/a_1(0)=5/7`,

so the lower bound is `(2+3*5/7)a_l(0)=29a_l(0)/7>4a_l(0)`. Negative `n` follow by symmetry. The case `l=0` follows directly from `(1,1)` and `(7,5,2)`.

Combining growth with the MLR theorem gives, for `l>=m>=1` and `0<=n<=m+1`,

`W(p_(l+1),p_m;n)>=4 W(p_l,p_m;n)`.

For `n<=m`, use the nondecreasing ratios `a_l(n+1)/a_l(n)` and write the determinant as `a_l(n)a_m(n)` times their ratio difference; both the difference and the prefactor have the claimed monotonicity. At `n=m+1`, the determinant is simply `a_l(m+2)a_m(m+1)`, and the coefficientwise growth applies directly.

## What remains for original Local TP2

At the all-left state `L^k`, the original pair is

`S=p_(k+2)`,

`D=(x+1)T_k[2+2(x+1)+3(x+1)² T_(k+1)]`,

where `T_k=sum_(j=0)^k U_j(x+3/2)`.

The theorem compares consecutive `p_m` rows, and by transitivity compares any ordered pair with indices at least one. It does not automatically compare this `D` with `S`: the expansion of `D` contains lower-degree Chebyshev terms as well as higher-degree terms. A further decomposition or inequality is required. No full ray or full tree Local TP2 claim is made here.
