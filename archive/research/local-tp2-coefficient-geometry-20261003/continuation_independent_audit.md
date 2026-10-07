# Independent audit: folded-kernel criterion and infinite Chebyshev-ray theorem

## Verdict

**Verified as stated, under the explicit positive finite interval-support assumptions.** No mathematical gap was found in the folded-kernel criterion, nonnegative or strict multiplicative closure, the five parameter-box certificates, the Chebyshev factor grouping, or the Christoffel–Darboux strictness argument.

This verifies a genuine infinite theorem for the consecutive rows

`p_m(x)=(x+1)U_m(x+3/2)`, `m≥1`.

It does **not** establish original Local TP2, even along the all-left ray: the original `S,D` pair differs from the consecutive `p_m,p_(m+1)` pair. The source note correctly preserves this distinction.

Reviewed sources:

* `continuation_kernel/folded_kernel_theorem.md`
* `continuation_ray.md`
* `continuation_ray.py`
* `continuation_ray_certificates.json`

## Folded-kernel criterion

For `h_n>0` on `0,…,m`, symmetric extension, and zero values outside `[-m,m]`, the stated kernel represents multiplication of symmetric Laurent polynomials correctly, including the factors of 2 in column zero. Its `(rows 0,1; columns n,n+1)` minor is exactly `Delta_n−Delta_(n+1)`, including `n=0`, where `h_-1=h_1` is essential.

For interior adjacent minors, transposing within the symmetric interior block allows `j≥i`. With `a=j−i`, `b=i+j`, direct expansion gives precisely

`Delta_a−Delta_(b+1)+h_a h_(b+1)(t_(b+1)−t_a)`.

The recurrence

`t_(n+1)−t_n=(Delta_n−Delta_(n+1))/(h_n h_(n+1))`

also holds at `n=0` with the symmetric convention. Whenever both denominators are in support, the monotone-defect assumption implies nonnegativity. At the support boundary `b+1>m`, the original un-divided expression reduces to `Delta_a+h_a h_b≥0`. If `a>m`, the minor is zero. First-column minors carry exactly the additional factor 2 claimed in the note. The constant-polynomial case `m=0` is included and gives a scalar identity matrix.

The support-to-all-minors step is sound; the following explicit argument can make it especially transparent. Row `i` has positive support interval

`[max(0,i−m),i+m]`.

For arbitrary rows `r<s` and columns `j<k`, a negative minor would require the cross product `K(r,k)K(s,j)` to be positive. These two positive entries imply that **every** entry in the rectangle of rows `r,…,s` and columns `j,…,k` is positive: each row's left endpoint is at most `j`, and each row's right endpoint is at least `k`. On this rectangle the usual adjacent ratio inequalities telescope in the column and row directions, contradicting a negative minor. This supplies a complete support argument without relying on unqualified transitivity across zeros.

Thus the necessary-and-sufficient criterion is valid. It should not be silently generalized to half-rows with internal zeros, or to infinite-support rows, since those cases are outside the stated proof.

## Closure and strict closure

`K_(PQ)=K_P K_Q` follows from their exact multiplication action. The kernels are banded and each relevant Cauchy–Binet expansion is finite, so no infinite-series convergence assumption is needed. Products retain strictly positive interval support.

For strict closure, the selected intermediate columns `k,k+1`, with `k=min(n,p)`, are valid for every `0≤n≤p+q`. The first determinant is `delta_k(P)>0`. If `k=0`, the second is `delta_n(Q)>0`, and indeed `n≤q`. If `k>0`, set `a=n−k≤q`, `b=n+k`; then `b+1≥a+1`. The interior bound `Delta_a−Delta_(b+1)≥delta_a>0` is valid whenever applicable. Beyond the support boundary the alternate formula is at least `Delta_a≥delta_a>0`. All other terms are nonnegative, completing strict closure.

The broadening result and its converse via multiplier `Q=x` are also valid when `Q` is a **finite** symmetric Laurent polynomial with nonnegative coefficients. Stating finiteness explicitly would remove any ambiguity about convergence; the note's polynomial setting already provides it.

## Independent exact verification of certificates

The separate verifier `continuation_independent_audit.py` does **not** import `continuation_ray.py`. It constructs the blocks directly as Laurent polynomials in `q,u,v`, using `x=q+q^-1`, and extracts Laurent coefficients directly. Thus it does not reuse the source script's binomial Fourier transformation.

For every one of the **23** claimed defects, the verifier independently checks:

1. The recorded power polynomial equals the defect obtained by direct Laurent multiplication.
2. Expanding the recorded Bernstein basis coefficients back into the power basis reproduces that polynomial exactly.
3. Every rational Bernstein coefficient is positive and the recorded lower bound is their exact minimum.

All 23 checks passed. The claimed certificate minima agree exactly, not approximately. Positivity of Bernstein basis functions and their partition-of-unity property then proves positivity over the entire real parameter square `[0,1]^2`, including its boundary. This is a parameter-box proof, not a grid sample.

## Infinite factorization and strict CD conclusion

The paired-root factorization of `U_m(x+3/2)` is correct: paired roots yield `x²+3x+c_j`, where `c_j=9/4−cos²(theta_j)` belongs to `[5/4,9/4]`; an odd degree contributes the additional factor `x+3/2`. The four residue classes of `m` have the exact factor counts stated in the theorem. Positive scalar factors do not affect the sign of defects. Consequently the five block certificates plus closure prove folded-kernel membership for every `p_m`, `m≥1`, with no bound on `m`.

The Christoffel–Darboux identity is correctly normalized with factor 2. Taking the coefficient of `q^(n+1)r^n` in its right-hand side produces

`2 sum_j [a_j(n)^2+a_j(n)a_j(n+2)−a_j(n+1)a_j(n−1)−a_j(n+1)^2]`

`=2 sum_j delta_(a_j)(n)`.

At `n=0`, the negative index is handled by `a_j(-1)=a_j(1)`, so no boundary term is missing.

The exceptional row `a_0=(1,1)` has defects `(-1,1,0,…)`, while `a_1=(7,5,2)` has defects `(13,7,4,0,…)`. The lower bound at `n=0` is therefore `2(-1+13)=24`; all remaining included terms are nonnegative. At `n=1`, the bound 2 is valid (though not optimal). For `2≤n≤m+1`, the chosen summand `j=n−1` lies inside `0,…,m`; its terminal defect is exactly `4^(n−1)`. This proves the claimed positive bound `2·4^(n−1)`. There are no missing cases within the stated range.

As an additional arithmetic check, the independent verifier generated the rows by their integer Laurent recurrence and verified 88 CD equalities and lower bounds through `m=11`. These finite checks are supplementary; the preceding algebraic argument is the infinite proof.

The transfer-matrix identity is also correct: the displayed matrix has trace `3+2x`, determinant 1, and `(2,1)` entry `x+1`; Cayley–Hamilton gives its `(m+1)`st power's `(2,1)` entry as `(x+1)U_m(x+3/2)`.

## Scope and suggested presentation precision

The verified theorem is:

For every `m≥1` and `0≤n≤m+1`, the adjacent coefficient minor between `H(p_m)` and `H(p_(m+1))` is strictly positive, with the stated explicit lower bounds. All ordered minors then follow with the usual support qualifications; zeros forced outside support are not strict.

The `m=0` exclusion is necessary, and the recorded negative first minor is correct. The original all-left formulas `S=p_(k+2)` and the displayed nonconsecutive expression for `D` are consistent with the recurrence. Since no proved comparison transfers the latter expression to the consecutive-row theorem, original ray Local TP2 and full canonical Local TP2 remain open in this package. No canonical promotion or full-Local-TP2 claim is justified solely by these results.

## Additional audit: every shifted U polynomial has a strict folded kernel

The further theorem supplied by `external_structure` is sound:

`H(U_m(x+3/2))` belongs to the strict folded-kernel class for every integer `m≥0`.

Here “strict” means that every defect difference through the polynomial degree is positive, not that minors forced to vanish outside support are positive.

To verify the proof, pair the quadratic factors `f_c` in the Chebyshev root factorization into the already certified B2 blocks. The linear factor `z=x+3/2`, when present, has defect differences `(1/4,1)`. If an odd number of quadratic factors remains, isolate the one with largest constant coefficient.

* For even `m≥2`, its parameter is `c=9/4−sin²(pi/(2(m+1)))≥2`, because the angle is at most `pi/6`.
* For odd `m` with an odd number of quadratic factors, `m≡3 (mod 4)`. Apart from `m=3`, such an index has `m≥7`, and the largest parameter is `c=9/4−sin²(pi/(m+1))>2`, because the angle is at most `pi/8`.

The isolated factor has exact defect differences

`(c²+5c−12, 6−c, 1)`.

These are strictly positive for `2≤c≤9/4`: the first polynomial is increasing there and equals 2 at the left endpoint; the second is at least `15/4`. The remaining `m=3` exception is handled directly:

`U_3(x+3/2)/8 = z f_(7/4)`,

whose Fourier row is `(93/8,37/4,9/2,1)` and whose exact defect differences are

`(1045/64,89/4,10,1)`.

The base cases `m=0` and `m=1` are respectively a positive constant and a positive multiple of `z`. These facts, the B2 parameter-box certificate, and strict product closure cover every integer `m≥0`. The singleton and exceptional defect computations were checked independently with Python rational arithmetic.

## Additional audit: symmetric-index broadening and factor-4 growth

Both new comparison lemmas in `continuation_ray.md` are correct.

### Symmetric-index broadening

For `m≥1` and `1≤r≤m`, the identity

`p_(m+r)+p_(m-r)=2 T_r(x+3/2) p_m`

is the ordinary Chebyshev addition identity. All roots of the shifted first-kind factor `T_r(x+3/2)` are negative, and its leading coefficient is positive. Consequently all of its ordinary coefficients are positive, and its Laurent coefficients after `x=q+q^-1` are nonnegative. The already verified broadening property of the folded kernel of `p_m` applies. It does not require `p_(m-r)` separately to belong to the folded class, and hence covers `m=r`, where that summand is `p_0`.

### Coefficientwise growth

Let `(f_l,g_l)^T=M^(l+1)(1,0)^T`. Since the first row minus the second row of `M` is `(1+q^-1,1)`, and `M^l(1,0)^T` has nonnegative Laurent coefficients, `f_l≥g_l` coefficientwise for every `l≥0`. The second-row recurrence therefore gives

`a_(l+1)(n) ≥ a_l(n+1)+2a_l(n)+2a_l(n−1)`.

For `l≥1`, cone membership gives ordinary log-concavity on the half-row as well as `a_l(0)≥a_l(1)`. The positive interval support then propagates monotone decrease to all nonnegative indices. Thus the displayed expression is at least `4a_l(n)` for `n≥1`; indices beyond support are harmless because the claimed right-hand side is zero. Symmetry handles negative indices.

At the central index, the consecutive-row strict MLR theorem implies the nondecreasing ratios

`a_l(1)/a_l(0) ≥ a_1(1)/a_1(0)=5/7`.

The recurrence lower bound is consequently at least `(2+3·5/7)a_l(0)=(29/7)a_l(0)>4a_l(0)`. The `l=0` case is verified directly from the two stated initial rows. Hence `a_(l+1)(n)≥4a_l(n)` holds for all integer `n` and all `l≥0`.

Finally, for `l≥m≥1`, the ratios `a_l(n+1)/a_l(n)` are nondecreasing as `l` increases at every `0≤n≤m`; their differences from the fixed `m`th-row ratio are nonnegative. Multiplying this ratio comparison by the coefficientwise growth bound proves

`W(p_(l+1),p_m;n)≥4W(p_l,p_m;n)`.

At `n=m+1`, the second term of the determinant vanishes and the same conclusion follows directly from coefficientwise growth of `a_l(m+2)`. This includes `l=m`, when that coefficient is initially zero. No denominator outside support is used.

These additions are independent proved lemmas; their correctness does not by itself close the original `D,S` comparison. One minor presentation improvement would be to distinguish the first-kind `T_r` used here from the separately defined partial sum called `T_k` in the final original-ray formulas.
