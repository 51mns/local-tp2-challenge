# Independent audit of the eight-quadratic normalized-defect certificate

**Verdict: PASS.** For eight independent pairs of parameters
`u_i,v_i in [0,1]`, let

`P(x)=product_(i=1)^8 [x^2+(3+u_i)x+5/4+(5/2)u_i+v_i]`.

Writing h_n=H(P)[n] with symmetric and zero extension, the certificate
proves

`delta_n(P)>h_n^2/128`, for every `0<=n<=16`,

on the entire sixteen-dimensional parameter cube. Both the mathematical
reduction and the exact computation pass independent review.

The independent implementation is
`fulltree_normalized_block_independent.py`; its complete output is
`fulltree_normalized_block_independent_results.json`. It reconstructs
the local tensors from the displayed factor formula and does not import
the author's routines, Laurent arrays, or expected minima.

## 1. Exact local tensor and its normalization

For one factor f, its ordinary x coefficients are

`(5/4+(5/2)u+v, 3+u, 1)`.

The independent implementation forms f(x)f(z) in ordinary bivariate
coefficients. Every coefficient is a polynomial of degree at most two
in each of u and v. For a power monomial u^p v^q, its coefficient in
the tensor Bernstein basis of bidegree (2,2), at index (a,b), is

`[binom(a,p)/binom(2,p)] [binom(b,q)/binom(2,q)]`,

with zero when p>a or q>b. This identity, including degree elevation
for the lower-degree terms, is applied using exact rational arithmetic.
Multiplying each resulting local tensor by 64 gives integers.

The author's Laurent construction gives the same normalization. Put

`4f=g_0+u g_u+v g_v`,

where `g_0=4x^2+12x+5`, `g_u=4x+10`, and `g_v=4`.
Since `64f(x)f(z)=4(4f(x))(4f(z))`, the local integer coefficient is

`4g_0(x)g_0(z)`

` +2a[g_u(x)g_0(z)+g_0(x)g_u(z)]`

` +2b[g_v(x)g_0(z)+g_0(x)g_v(z)]`

` +2a(a-1)g_u(x)g_u(z)`

` +ab[g_u(x)g_v(z)+g_v(x)g_u(z)]`

` +2b(b-1)g_v(x)g_v(z)`.

This agrees with the C++ formula, including the mixed u,v term and
the factors of two. The Laurent rows used there are exactly the
substitutions of these three ordinary polynomials.

Because the eight parameter pairs are independent, the Bernstein
coefficient of P(x)P(z) at any full tensor index is the product of the
eight corresponding local tensors. The total scaling is therefore
exactly `64^8`, not a parameter-dependent multiplicity or factorial.

## 2. Symmetry reduction covers the entire parameter cube

The target polynomial `128delta_n(P)-h_n^2` is unchanged by permuting
the eight factors and their parameter pairs simultaneously. Each
factor has nine local Bernstein index types `(a,b) in {0,1,2}^2`.
Thus full indices are equivalent precisely by permuting a list of
eight such types. It suffices to check every multiset of eight types.

There are

`binom(8+9-1,9-1)=binom(16,8)=12870`

such multisets. Both implementations enumerate each one exactly once.
No multinomial multiplicity is needed when checking a coefficient's
sign: every ordered index in an orbit has the identical coefficient.
The 17 supported defect indices give 218,790 representative margins,
representing `17*3^16=731794257` full tensor coefficients.

Every tensor Bernstein basis function is nonnegative on the cube and
their sum is one. Strict positivity of every coefficient therefore
proves strict positivity at every parameter point, including the
boundary. This is a continuum certificate, not sampling of roots or
parameter values.

## 3. Independent ordinary-bivariate Fourier computation

The C++ implementation substitutes `x=q+q^-1` locally and convolves
a two-dimensional Laurent grid. The independent Python implementation
instead multiplies ordinary polynomials in x and z, retaining their
separate exponent coordinates through all eight factors. Only at the
end does it apply the binomial Fourier functional

`L_n(x^j)=binom(j,(j-|n|)/2)`

when the parity and support permit, and zero otherwise. Symmetry at
n=-1 is therefore handled by the absolute value, independently of
the author's Laurent-array addressing.

For the ordinary monomial x^i z^j, the margin's linear-functional
weight is exactly

`127 L_n(x^i)L_n(z^j)`

` -128 L_(n-1)(x^i)L_(n+1)(z^j)`

` -128 L_(n+1)(x^i)L_(n+1)(z^j)`

` +128 L_n(x^i)L_(n+2)(z^j)`.

The coefficient 127 incorporates the subtraction of h_n^2 from
128delta_n. In particular n=0 subtracts the two equal h_1^2 terms,
and n=16 includes the correct zero extension.

The independent code uses symmetry under x,z interchange and the fact
that opposite parities have zero functional weight to reduce the
ordinary grid to 81 entries for the final linear evaluation. That
reduction is checked explicitly and is unrelated to the parameter
permutation reduction. All integer products and sums use Python's
arbitrary-precision integers; NumPy arrays have dtype=object.

## 4. Independent replay result

The independent run produced:

- 12,870 parameter-index orbits;
- 218,790 checked representative margins;
- zero negative coefficients;
- zero zero coefficients.

After the independent run completed, its output was compared with
`fulltree_normalized_block_results.json`. Every one of the 17 minimum
values and every corresponding minimizing histogram agrees exactly.
The complete local ordinary tensors and all minima are preserved in
the independent result file.

As an endpoint consistency check, P is monic of degree 16, so
delta_16=h_16^2=1. The terminal margin is exactly 127; its scaled
value in both outputs is `35747322042253312=127*64^8`.

All ordinary factor coefficients are positive on the cube, so P has
a positive uninterrupted ordinary and Laurent support. Thus the
normalized inequality has no hidden zero-row or changing-degree
exception.

## 5. C++ overflow and initialization audit

Every entry in every local integer tensor is nonnegative. Its total
Laurent coefficient sum is at most its value for type (2,2), namely

`64 f(2;1,1)^2=64*(67/4)^2=17956`.

At product depth j, the sum of all coefficients is therefore at most
`17956^j`. Every multiplication and intermediate positive accumulation
in the convolution is bounded by that sum at its new depth. Local
expressions evaluated with ordinary C++ int operands are also far
below the signed-int bound before conversion to __int128.

The four signed terms in delta followed by the margin operation are
conservatively bounded in absolute value by

`513*17956^8`

`=5543628756874248623982282216436727808`.

This bound has 123 bits. It is below both the signed-128 limit
`2^127-1` and the initializer `2^126` used for the minima. Thus the
signed arithmetic, decimal conversion, and minima initialization are
all safe. The grid coordinates and allocation sizes also cover the
entire support, and all out-of-support reads return zero.

## Audited artifacts and scope

The audited C++ source has SHA-256
`6314f8d768f40195d9978ead3fec40152d7031518edff3d23cdb6c5a46f44f12`.
Its result file has SHA-256
`8c2451ca4daa83c134661ed6c6c80e2da97722e9392fcf80c5264d39a8233b19`.

This proves the exact eight-factor normalized-defect theorem stated
at the beginning. Any extension to an arbitrary number of factors,
the general one-turn compatibility problem, or the full canonical
tree still requires its subsequent propagation and perturbation
arguments; none of those conclusions is inferred from this block
certificate alone.

Metadata clarification: the 218790 count is named `distinct_Bernstein_margins`; it counts 17 margins for each of the 12870 parameter-index orbits. Renaming this JSON field does not change the arithmetic certificate.
