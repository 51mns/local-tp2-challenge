# Analytic far-band bound and exact power-method obstruction

These statements concern actual canonical states. The first holds for
every actual state and all midpoint parameters in `[-2,2]`; it settles
only separated relative minors. The second is an actual root witness
against a sufficient coefficient proof method, not against the packet.

## 1. Positive canonical algebra gives a uniform entry ratio

Use the normalized variables

    y=x+1, z=2x+3, X=1+ya,
    t=z+3y²a, k=X(3X-2),
    g=(t-2)e+k+r, s=tg-r,
    C=X+y(e+g), M=3yC-x+1, T=M-1,
    d=eM, c_A=e+g+s.

The root is `(a,e,r)=(0,1,1)`. The two child updates are

    short: (a,e,r) -> (a,e+g,g),
    long:  (a,e,r) -> (a+e,g,e+g).

Thus `a,e,r` are ordinary coefficient-nonnegative at every actual state,
and `e,r` are nonzero. This uses only elementary coefficient positivity:
`t-2=1+2x+3y²a`, `3X-2=1+3ya`, and hence `g>=0`. Further,

    s=t(t-2)e+tk+(t-1)r >=0.

The next centers satisfy exactly

    C_short=C+ys, C_long=C+y(s+d).

Since `C>=C_root=5+6x+2x²`, the polynomial
`M=3yC-x+1` has nonnegative ordinary coefficients, so `d>=0`.
Induction proves the coefficientwise center bound without using folded
TP2 or a target descendant inequality.

At the root,

    yC_root=5+11x+8x²+2x³,
    H(yC_root)_0=21,
    T_root=15+32x+24x²+6x³,
    H(T_root)_0=63.

Consequently `T>=T_root` ordinarily and `H(T)_0>=63`. For every
`v in [-2,2]`, `T-v` has nonnegative Laurent coefficients and its
constant Laurent coefficient is at least 61. For both actual paired
orders `(b0,b1)=(c_A,e)` and `(e,c_A)`, the seeds have nonnegative
Laurent coefficients. With `u=(r+s)/2`,

    H_rs=b0(T-r)(T-s)+b1(T-u)

therefore satisfies the **Laurent coefficientwise** bounds

    H_rs >= (H(T)_0-u)b1 >=61 b1,
    yH_rs >=61 yb1.                                  (1)

Multiplication by y in (1) uses only its nonnegative Laurent coefficients;
no assertion that y preserves folded TP2 is made.

## 2. All sufficiently separated minors are uniformly dominated

Let h,b be the Fourier half-rows of either pair in (1), with degrees
`D>=d`. Folded kernel entries are positive linear combinations of row
entries, including the central factor 2, so `K_h>=61 K_b` entrywise.

Take any ordered rows `i<j` and columns `k<l` with a positive reference
minor. Then its diagonal entries are positive, which implies
`|k-i|<=d` and `|l-j|<=d`. If `j-i>D+d`, both off-diagonal entries of
K_h and K_b vanish: `l-i>D` and `j-k>D`, and the reflected sums are
at least these displacements. Hence

    det K_h = K_h(i,k)K_h(j,l)
            >=61² K_b(i,k)K_b(j,l)
            =61² det K_b.                            (2)

This proves the stronger factor `3721` for every such separated positive
reference rectangle, for every actual state and every parameter pair in
the whole box. It applies independently after multiplication by y. No
cone premise is required for this separated-rectangle argument.

Equation (2) does **not** settle the overlap band `j-i<=D+d`, establish
H/yH cone membership, or imply current/new-center MP2. Entry domination
alone is not determinant domination when off-diagonals remain present.

## 3. Actual root obstruction to parameter-power positivity

Set `alpha=2-r`, `beta=2-s`, `p=T-2`. Then

    H_rs=U+(alpha+beta)A+alpha beta B,
    U=b0 p²+b1 p, A=b0 p+b1/2, B=b0.

For each ordered folded minor, the sharp polynomial is

    det K_Hrs-(alpha-beta)² det K_b1/4.

Its coefficient at `alpha² beta²` is exactly `det K_B`: the subtraction
has parameter degree 2 and cannot affect this degree-4 term. In the
y-smoothed mode B is replaced by yB.

At the **actual root, reverse paired orientation**, `b0=e=1`, so
`yB=y` has Fourier half-row `(1,1)`. Rows `(0,1)` and columns `(0,1)`
are the exact matrix

    [[1,1],[2,1]],

whose determinant is `-1`. Thus the `alpha² beta²` coefficient of this
central sharp minor is `-1`.

This refutes the proposed sourcewise positivity of all ordinary parameter
power coefficients, even on an actual root seed. It does not show that
the sharp polynomial is negative anywhere in the parameter box; lower
terms can compensate. It also does not obstruct an exact Bernstein or
other whole-polynomial certificate. The frozen fixed-parameter search
passes this root case, and the quantitative lane separately studies
continuum certificates.
