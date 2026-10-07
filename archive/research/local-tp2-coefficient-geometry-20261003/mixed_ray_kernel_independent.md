# Independent audit of the mixed-ray kernel theorem

**Verdict: PASS.** The current theorem in `mixed_ray_kernel_theorem.md`
is supported by exact parameter certificates and an unbounded argument.
The audit found no use of arbitrary positive-sum closure of the folded
cone. This verdict covers the mixed increments and mixed prefixes; it
does not extend to the final constant-perturbed multiplier or Local TP2.

## Independently reconstructed arithmetic

`mixed_ray_kernel_independent.py` does not import any polynomial,
Fourier, or Bernstein routine from the author's certificate generator.
It constructs `x=q+q^-1` directly as a Laurent polynomial, multiplies
Laurent polynomials with exact rational coefficients, extracts each
Fourier row, and recomputes the folded defects and tensor Bernstein
arrays.

Every power coefficient and every Bernstein coefficient matches the
author's JSON for all **17 blocks and 105 defect arrays**. The verifier
also checks symmetry and independently certifies strict positivity of
every supported Laurent half-row throughout the parameter cube.

The checked certificate file has SHA-256

`31e3870b07019bd7ea50df60d8ac0297ffbb97c1b50f4070d77ecb7fa9c50e2b`.

Results and all independently obtained lower bounds are recorded in
`mixed_ray_kernel_independent_results.json`.

The verifier additionally reconstructs all four quantitative mass-margin
certificates in `mixed_ray_margin_certificates.json`, whose SHA-256 is
`68146b0d79d44752ea55a11e2cce12d795a927a11f53bfcfbb7eb8cda98ebc95`.
It independently evaluates mass by substituting q=1 into its Laurent
polynomials, then reproduces every power and Bernstein coefficient. The
four strict lower bounds are exactly `41/5`, `169619`, `5101`, and
`1873428`, for respective mass factors `4/5`, `90`, `40`, and `100`.
This verifies those four arithmetic certificates; their use in the
separate actual mixed-ray comparison is covered by that theorem's
logical audit, not inferred from kernel membership alone.

In particular, both paired midpoint families have `delta_0>8` on the
entire independent parameter cube `a,b,c in [-2,2]`. This uniform
margin is materially used in the compatibility argument below; it is
not merely a strict-positivity certificate.

## Principal-minor bound

The claimed lower bound, every principal minor being at least
`delta_0/2`, is valid for the folded kernel.

For adjacent principal indices beyond zero, the interior folded-minor
formula has `a=0`; its first term is at least
`Delta_0-Delta_1=delta_0`, and its second term is nonnegative. The
support-boundary formula gives at least `Delta_0>=delta_0`. The first
principal adjacent minor is exactly `delta_0`.

Conjugation by `diag(sqrt(2),1,1,...)` correctly symmetrizes the special
first row/column of the folded kernel. Its diagonal entries are h_0 at
zero and `h_0+h_(2i)` elsewhere, hence lie in `[h_0,2h_0]`.

For the symmetric conjugate A, TP2 gives

`A(i,i+1) A(i+1,j) >= A(i,j) d_(i+1)`.

Its principal minor on `(i+1,j)` also gives

`A(i+1,j)^2<=d_(i+1)d_j`.

Squaring the former and applying the latter proves the manuscript's
bound, including cases with zero off-diagonal entries. Only positive
diagonal entries are divided by. The diagonal ratio is at least 1/2,
which proves the desired lower bound for arbitrary principal pairs.

## Constant differences and compatibility

If F-G is a constant d, the multiplication kernels differ by dI.
Expanding the mixed determinant independently gives

`mixed(K_F,K_G)=2 det(K_((F+G)/2))-(d^2/2) det(I)`.

For ordered row/column pairs, the identity submatrix has determinant
one exactly on a principal pair and zero otherwise. On a principal
pair, `delta_0>=8` gives a midpoint minor at least 4, while `|d|<=4`
makes the subtraction at most 8. Thus the mixed determinant is
nonnegative. Nonprincipal pairs follow simply from midpoint TP2.

The two reduced summands in the left family differ by `a-b`; those in
the right family differ by `b-a`. Their midpoints use
`c=(a+b)/2`, which belongs to the certified interval. Therefore the
three-independent-parameter certificates apply without any additional
assumption.

The Cauchy-Binet argument for common factors is also valid: take the
coefficient of rs in the determinant of
`(rK_F+sK_G)K_Q`. Every resulting summand is a certified nonnegative
mixed minor times a nonnegative minor of K_Q. Bandwidth makes each
sum finite.

Finally, a two-by-two determinant of a positive weighted sum has only
diagonal quadratic terms and pairwise mixed terms. Their nonnegativity
is precisely what has been established. No inference that all cone
polynomials can be positively added is needed.

## Resolvent weights for both polynomial sequences

For u_N in the independent variable z, the specified symmetric Jacobi
matrix has zero diagonal and unit off-diagonals. For v_N it has diagonal
`(-1,0,...,0)` and unit off-diagonals. Expanding the characteristic
determinant from the last row gives the required initial values
`1,z` or `1,z+1` and recurrence
`p_N=z p_(N-1)-p_(N-2)`.

Both matrices have spectrum in `[-2,2]`: the first row interval for the
second matrix is `[-2,0]`, and every other row interval is contained in
`[-2,2]`. This includes N=1. An eigenvector's last component cannot
vanish, since the last-row equation would force the preceding component
to vanish and recurrence would force the entire vector to be zero.
The same recurrence shows each eigenspace is one-dimensional; symmetry
then gives simple eigenvalues.

Cofactor expansion of the last diagonal resolvent entry gives exactly
`p_(N-1)(z)/p_N(z)`. Its spectral weights are the squares of the last
components of an orthonormal eigenbasis: all are strictly positive and
their sum is one. This proves the residue hypotheses for every N>=1.

The normalization `sum lambda_i=1` is essential: it is what reproduces
the w times p_N term, rather than an unspecified scalar multiple of it.
It is present and justified in the proof.

The degree-zero u cases are w and t+w. The required degree-zero v case
is t+w+1. The manuscript correctly treats these separately; no false
identification of v_(-1) with zero is used. Indeed the recurrence
extension would have v_(-1)=-1, but no such extension is needed.

## Extra y factors and every initial case

For increments with j>=3, any two distinct resolvent summands have
`j-2>=1` omitted root factors in common. Thus y can be absorbed into one
such factor using the certified block `y(t-a)`. The remaining common
product is a cone polynomial. The individual, diagonal terms use
`yL_a` or `yR_a`, also explicitly certified.

There is no missing j=2 boundary: its two actual polynomials are the
separately certified degree-two increment blocks. The j=1 cases are
the y-single blocks at a=0; j=0 uses yw and y(t+w). Consequently all
increment indices are covered without multiplying an arbitrary cone
polynomial by y.

## Prefix parity and low-degree boundaries

The four displayed factorizations follow directly from
`T_(2h)=u_h v_h` and `T_(2h+1)=u_h v_(h+1)`. Their inside brackets use
exactly the u or v mixed resolvent families, with the indicated indices.
Their outside factors are products of certified cubic root factors.

For an extra y, all positive-degree outside factors can absorb it.
The only zero-degree outside-factor cases are exactly:

- left k=0: yw;
- left k=1: `y[w(t+1)+1]`, the y-left-single block at a=-1;
- right k=0: y(t+w+1).

All three are explicitly certified. Right k=1 already has the positive
degree outside factor v_1=t+1, so it causes no additional exception.

The final statement about `y^2 Z_k` is justified directly by multiplying
the proved cone polynomial Z_k by the known cone factor y^2. It does
not require closure under multiplication by y.

## Scope of the conclusion

The mixed increment families q_j and the four families
`Z_k^L,Z_k^R,yZ_k^L,yZ_k^R` belong to the folded cone for every index.
The same holds for `y^2 Z_k`. The theorem does not yet cover adding
`2(x+2)` to `3y^2 Z_k`, and it does not independently prove the actual
mixed-ray Local TP2 comparison or full-tree closure.
