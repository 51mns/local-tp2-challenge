# First-kind Chebyshev ordering and the odd all-left sandwich

This note proves an infinite coefficient comparison. It uses the already
proved folded-kernel criterion and product closure, together with the exact
parameter-box block certificates in `continuation_ray.md` and
`continuation_prefix.md`. It requires no finite-depth extrapolation.

Write `t=2x+3`, `zeta=x+3/2`, `y=x+1`, and

`u_j=U_j(zeta)`, `p_j=y u_j`, `V_j=u_j+u_(j-1)`.

Let `c_j=2 T_j(zeta)` denote twice the Chebyshev polynomial of the first
kind (not the prefix sums). Thus

`c_0=2`, `c_1=t`, `c_(j+1)=t c_j-c_(j-1)`.

For `j>=2`, `c_j=u_j-u_(j-2)`; also `c_1=u_1`, with `u_-1=0`.
For symmetric Fourier rows, use

`M_n(A,B)=H(A)[n] H(B)[n+1]-H(A)[n+1] H(B)[n]`.

## 1. All first-kind rows except c_2 lie in the folded cone

For `j>=1`, the roots of `c_j` are

`cos((2a-1)pi/(2j))-3/2`, `a=1,...,j`.

Pairing opposite cosines therefore factors `c_j`, apart from its positive
leading coefficient `2^j`, into quadratics

`f_c=x^2+3x+c`, `5/4<=c<=9/4`,

and, when j is odd, one factor `zeta=x+3/2`.
All factors have positive ordinary coefficients.

Use the already certified strict folded-cone blocks:

- `f_c f_d`, throughout `c,d in [5/4,9/4]`;
- `zeta f_c`, throughout `c in [5/4,9/4]` (the prefix cubic certificate
  with its parameters `s=3`, `a=3/2`);
- `zeta`, whose defects are `(1/4,1)`;
- `f_c`, throughout `c in [2,9/4]`.

The final block follows directly: its Fourier row is `(c+2,3,1)` and its
defects are

`c^2+5c-12`, `6-c`, `1`,

which are strictly positive on `[2,9/4]`.

For `j` congruent to 0, 1, or 3 modulo 4, respectively, group the factors
as quartics; a linear factor and quartics; or one cubic and quartics.
For `j=4h+2>=6`, isolate the central root pair. Its constant is

`c=9/4-sin^2(pi/(2j)) >= 2`,

because `j>=3` implies `pi/(2j)<=pi/6`. The remaining quadratics group
into quartics. Strict multiplicative closure now proves that every
`c_j`, `j>=1`, `j!=2`, has strictly positive supported folded defects.
The constant `c_0=2` also lies in the cone.

The exceptional row is exactly

`H(c_2)=(15,12,4)`, `delta(c_2)=(-3,68,16)`.

## 2. Consecutive first-kind rows are nevertheless MLR ordered

Their Christoffel-Darboux identity has the modified initial term

`c_(m+1)(X)c_m(Y)-c_m(X)c_(m+1)(Y)`

`=2(X-Y)[2+sum_(j=1)^m c_j(X)c_j(Y)]`.

To verify the normalization, the case `m=0` is
`2(2X+3)-2(2Y+3)=4(X-Y)`. The three-term recurrence adds
`2(X-Y)c_m(X)c_m(Y)` at each succeeding step, proving the identity
inductively for every m.

Substituting `X=q+q^-1`, `Y=r+r^-1` and taking the coefficient of
`q^(n+1)r^n` gives

`M_n(c_m,c_(m+1))=2[2*1_(n=0)+sum_(j=1)^m delta(c_j)(n)]`.

The necessary initial defect rows are

`delta(c_1)=(1,4)`,

`delta(c_2)=(-3,68,16)`,

`delta(c_3)=(972,1224,656,64)`.

Thus at `n=0` the cumulative bracket is 2 for m=0, 3 for m=1, zero
for m=2, and strictly positive for every m>=3. At positive n, all terms
are nonnegative. For `1<=n<=m`, the terminal defect of `c_n` is
`4^n>0`, so the sum is strictly positive there.

Consequently

`H(c_m) <=_lr H(c_(m+1))` for every `m>=0`.

The adjacent supported minors are strict except for `m=2,n=0`.
In particular, no claim of cone membership for the exceptional `c_2`
has been used.

## 3. The odd sandwich

For every `r>=1`, recurrence algebra gives

`c_(r+1)-c_r=(t-2)V_r=(2x+1)V_r`.

The right side has strictly positive supported Fourier coefficients.
Subtracting the narrower row gives the exact determinant identity

`M_n(c_(r+1),(2x+1)V_r)=M_n(c_r,c_(r+1))>=0`.

Hence

`H(c_(r+1)) <=_lr H((2x+1)V_r)`.

Now put `N=2r+1>=3` and `E=y T_(N-1)`, where `T_j=sum_(a=0)^j u_a`
is the prefix sum. The elementary Chebyshev identities give

`u_(2r+1)=u_r c_(r+1)`, `T_(2r)=u_r V_r`.

Therefore the actual all-left smaller increment and the intermediary are

`S=p_N=p_r c_(r+1)`,

`(2x+1)E=p_r (2x+1)V_r`.

Because `p_r` is in the folded cone for every `r>=1`, multiplication by
its TP2 folded kernel preserves MLR order. We conclude, for every odd
`N>=3`,

`H(p_N) <=_lr H((2x+1)y T_(N-1))`.

This establishes the first sandwich for the entire odd family. Combining
it with a separately proved comparison of this intermediary to the
bracket proxy requires that comparison's own margin proof; it is not
inferred merely from cone membership.
