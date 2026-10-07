# Independent audit of the adjacent-sum and prefix-sum cone theorem

## Verdict

**PASS.** The infinite theorem in `continuation_prefix.md` is proved by the stated root-pairing argument, the exact parameter-box certificates, and the previously verified strict product-closure theorem. No root-parameter gap or support exception was found.

With `u_r=U_r(x+3/2)` and `u_-1=0`, the verified statements are:

* Every `V_r=u_r+u_(r-1)`, `r≥0`, belongs to the folded-kernel cone.
* Every prefix sum `T_n=sum_(j=0)^n u_j`, `n≥0`, belongs to the cone.
* Every `(x+1)T_n`, `n≥1`, belongs to the cone.
* Every supported defect difference of the nonconstant rows in these statements is strictly positive.

The exclusion of `(x+1)T_0` is necessary. These results do not prove the remaining original Local TP2 comparison or cone membership of the separate bracket `2+2(x+1)+3(x+1)^2T_(k+1)`.

## Exact certificate verification

The verifier `continuation_prefix_audit.py` independently constructs each block by multiplying Laurent polynomials in `q` and four real parameters, with `x=q+q^-1`. It does not import `continuation_prefix.py`, and it does not reuse that script's binomial formula for the Fourier transformation.

For each of the **14** defect polynomials, it verified:

1. Direct Laurent multiplication gives the recorded power-basis polynomial.
2. Expansion of every recorded tensor Bernstein basis function back into ordinary powers reconstructs the same polynomial exactly.
3. The complete tensor of Bernstein coefficients is present, every coefficient is positive, and the recorded lower bound is its exact minimum.

All **376** rational Bernstein coefficients passed these checks. The exact lower bounds are:

| Block | Lower bounds by supported index |
|---|---|
| Two general quadratics | `19633/256, 2857/32, 267/4, 35/2, 1` |
| Middle linear factor times one general quadratic | `69/8, 129/8, 19/2, 1` |
| Isolated innermost pair | `1/4, 7/4, 1` |
| Middle linear factor | `1/4, 1` |

Because tensor Bernstein basis functions are nonnegative and sum to one on the full closed unit cube, these are strict lower bounds throughout the entire parameter domain, including boundaries. No floating-point or parameter-grid assumption is involved.

## Root formula and parameter domain

For `r≥1`, the identity

`U_r(cos theta)+U_(r-1)(cos theta)=sin((2r+1)theta/2)/sin(theta/2)`

gives exactly `r` roots `cos(2j*pi/(2r+1))`, `j=1,…,r`. They are distinct and account for the full degree; the leading coefficient is `2^r`.

Set `epsilon=pi/(2r+1)`. A paired lower-half angle is `theta=2j*epsilon`, and its partner is `pi+epsilon−theta`. Their shifted linear factors are `(x+a)(x+b)`, where

`a=3/2−cos theta`,

`b=3/2+cos(theta−epsilon)`.

For every lower-half index, both `theta` and `theta−epsilon` lie in `(0,pi/2)`, and the second angle is smaller. Therefore

`1/2≤a≤3/2`, `3/2≤b≤5/2`,

and

`s=a+b=3+cos(theta−epsilon)−cos theta≥3`.

The upper bound `s≤4` follows at once from the two shift intervals. For `c=ab`, the required unit-cube parameter is

`v=c−5s/2+25/4=(5/2−a)(5/2−b)`.

It is nonnegative. The source proof's arithmetic–geometric-mean bound is valid:

`v≤s²/4−5s/2+25/4=(s−5)²/4≤1`,

since `3≤s≤4`. There is also a direct trigonometric verification:

`v=(1+cos theta)(1−cos(theta−epsilon))≤(1+cos theta)(1−cos theta)=sin² theta≤1`.

Thus every pair really has the certified form

`s=3+u`, `c=5/4+5u/2+v`, `u,v∈[0,1]`.

This step is an exact domain inclusion, not an empirical fit to computed roots.

## Exhaustive grouping of factors

For odd `r`, the unpaired middle shift is

`a_mid=3/2+sin(epsilon/2)∈[3/2,2]`.

If the number of quadratic pairs is even, use the certified middle linear block and group all quadratics into certified quartics. If that number is odd, use one certified cubic consisting of the middle linear factor and one arbitrary general quadratic; pair all remaining quadratics into quartics. This includes `r=1`, which has just the middle linear factor.

For even `r`, an even number of quadratic pairs is grouped entirely into quartics. If their number is odd, write `r=2h`, `h≥1`, and isolate the innermost pair. Its lower angle is

`theta=2h*pi/(4h+1)≥pi/3`,

because `6h≥4h+1` for every integer `h≥1`. Hence its lower shift is at least 1. The pair therefore falls inside the rectangle

`1≤a≤3/2`, `3/2≤b≤5/2`,

covered by the isolated-pair certificate. All remaining quadratics pair into quartics. This also handles the smallest even case `r=2`.

The constant case `r=0` is `V_0=1`. Every index is now covered, and positive scalar factors preserve defect signs. Previously verified strict product closure proves the claimed infinite `V_r` theorem.

## Prefix-sum deductions and support

The exact identities

`T_(2h)=u_h V_h`,

`T_(2h+1)=u_h V_(h+1)`

follow from the second-kind Chebyshev product-to-sum identity. For example, `u_h²` contributes precisely the even-index terms from `u_0` through `u_(2h)`, and `u_h u_(h-1)` contributes the intervening odd-index terms. The odd-prefix identity is analogous.

The audited theorem for all unweighted `u_h` and the just-proved theorem for `V_r` give cone membership, and strict supported defects, for these products. To include a factor `y=x+1` when `n≥2`, use `p_h=y u_h` with `h=floor(n/2)≥1`; the previously audited `p_h` theorem applies. The small remaining case is

`yT_1=2(x+1)(x+2)`,

with Fourier row `(8,6,2)` and defect differences `(8,16,4)`. The omitted `yT_0=x+1` has defect difference `−1` at index zero, as stated.

Every factor under discussion has positive ordinary coefficients, or is a product of factors with positive ordinary coefficients, so its Fourier half-row has positive coefficients at every index within its degree. Thus the support hypotheses of the folded-kernel and strict-closure theorems are satisfied. “Strict” here concerns supported defect differences; minors forced to vanish outside support remain zero.

The independent verifier also checked 17 prefix-factorization identities by exact Laurent recurrence as a supplementary arithmetic check. The root grouping and algebraic identities above provide the unbounded proof.

## Scope

These additions are valid infinite cone-membership theorems, and are suitable for inclusion in the continuation research branch with their exact certificates. They do not justify assuming cone closure under arbitrary positive sums, nor do they close the original `D,S` comparison. The source note states that remaining limitation correctly.
