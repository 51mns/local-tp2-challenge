# Independent audit: universal canonical first-difference support

Audited manuscript: `resumed_extension_kernel_support.md`.

**Verdict:** the induction is valid for the entire canonical tree. It proves the claimed strict first-difference support and coefficientwise gap dominance. I found no mathematical gap. No finite-depth computation is needed for this conclusion.

## Basis normalization and mutation

The character product identity

`B_i B_j=sum_(k=|i-j|)^(i+j) B_k`

is correct without parity restrictions or extra multiplicities. One direct verification compares each nonnegative Laurent coefficient: both sides count the same overlap of the integer intervals `[-i,i]` and `[n-j,n+j]`. Its first differences give the stated range of coefficient one. Thus multiplication preserves nonnegative `B` coefficients. The special formulas `yB_0=B_1` and `yB_j=B_(j-1)+B_j+B_(j+1)` for `j>=1` are also correct.

The root rows `[1]`, `[1,1]`, `[3,4,2]` and the two root gap rows are correct. All four induction hypotheses hold there, including strict separation of center and endpoint degrees.

For `U=3yAC-x(A+C)-B`, both identities

`U=y(3AC-A-C)+A+C-B`

and

`U-C=(2yC-C-y+1)+y(A-1)(3C-1)+(A-1)+(C-B)`

are exact. Every term following the bracket is nonnegative in the `B` basis. The three displayed bracket coefficient formulas are correct and strictly positive at every index through `deg C+1`. There are no missed exceptions at index zero or at the top of that interval.

## New upper support and degree

The upper-support argument covers both endpoint cases.

- If `deg A=0`, the positive leading coefficient `(3a_0-1)c_c` of `R=3AC-A-C` makes `deg U=c+1`, entirely inside the interval already proved positive.
- If `a=deg A>=1`, the coefficient of `B_a` in `A-1` is positive. In its product with dense positive `3C-1`, the choices `j=n-a` for `n>=a` and `j=a-n` for `n<a` are valid indices in `[0,c]`, because `a<c`. The product rule therefore supplies a strictly positive contribution at every `n` in `[0,a+c]`. Multiplication by `y` preserves dense positivity here, including index zero because the product's coefficient at index one is positive. It reaches degree `a+c+1`.

All remaining terms of `U=yR+A+C-B` have degree at most `c`; consequently the leading degree cannot cancel. This proves both full support and the claimed degree formula. It also proves the child gaps `U-C` and `U-A` strictly positive throughout the full new support.

## Central coefficient inequality

From `U=yR+A+C-B`, the exact difference is

`u_1-u_0=r_0+r_2+(a_1-a_0)+(c_1-c_0)-(b_1-b_0)`.

Here `R=(2C-1)+(A-1)(3C-1)` has nonnegative coefficients, so `r_2>=0`. The coefficient of `B_0` in `AC` equals `sum_i a_i c_i`, hence the bound on `r_0` is legitimate. Using `c_1>=b_1`, `a_1>=0`, `a_0>=1`, and `b_0>=1` gives exactly

`u_1-u_0 >= (a_0-1)(3c_0-2)+c_0-2+b_0 >= c_0-1 >= 2`.

The new constant coefficient is at least the old `c_0`, because `U-C` is strictly positive. Thus every induction hypothesis is preserved. Exchanging the endpoints proves the other mutation, and the invariant is symmetric in the endpoints, so its ordering in the child triple causes no issue.

## Consequences and exact scope

Every nonroot endpoint pair consists of a previous center and one retained previous endpoint. The invariant therefore proves dense strict positivity of `E=Y-X`. At the root, `E=B_1` correctly has the exceptional zero coefficient at index zero.

The displayed coefficients of `M=y(3C-1)+2` are exact and strictly positive through `deg C+1`. The identity `D=EM` follows by subtracting the two mutations; their degree ordering matches that of the two endpoints. For nonroot `E`, dense positive factors give dense positive product by choosing terms with `i+j=n`. At the root, `E=B_1` and the explicit multiplication rule for `y` likewise give strict positivity at every supported index of `D`, including zero.

The endpoint degrees remain distinct because a new endpoint is a previous center of strictly larger degree. The child degree formula then gives `deg D>deg S`. Together with strict full support of `S` and `D`, this globally discharges the positivity/support hypothesis needed for the earlier strict tail-sum argument.

The proof also supplies positive integer first differences for canonical centers, but it does **not** supply their `J`-kernel TP2 condition, either low-coefficient multiplier inequality, or either likelihood-ratio sandwich. The manuscript correctly leaves those separate obligations open. Strict positivity of coefficients is not being promoted to any unproved likelihood-ratio order.
