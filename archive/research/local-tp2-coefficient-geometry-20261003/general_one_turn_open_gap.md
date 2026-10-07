# Precise remaining gap for arbitrary initial left-run length

The theorems for all-left, all-right, `LR^k`, `RL^k`, and `L²R^k`
are proved separately. This note identifies the unresolved uniform
step for all `L^mR^k`; it does not infer that step from the fixed-`m`
certificates.

Let `m>=1`, `y=x+1`, `z=2x+3`, and use the inner prefixes
`T_j=sum_{i=0}^j U_i(z/2)`. Put

`A=T_(m+1)`, `B=T_(m-1)`, `P=1+yT_m`, `t=3yP-x`.

For `r,s,c in [-2,2]`, write `f_r=t-r` and

`F=A f_r f_s`, `G=B f_c`, `H=F+G`.

The exact relative-compatibility argument would follow from

`det K_H[rows,cols]>=4 det K_B[rows,cols]`              (target)

for every ordered pair of rows and columns, together with the needed
single-block and smoothed cone assertions. It is enough for the
midpoint application to take `c=(r+s)/2`; the fixed-`m` certificates
currently prove the larger independent parameter cube.

## What is already proved about the dominant term

The sharp strength results give `A` strength at least `2^m`, and each
`f_r` strength at least `3*2^(m-1)`. Multiplicative strength therefore
gives

`delta_n(F)>=lambda_m H(F)_n`,
`lambda_m=9*2^(3m-2)`.

The relative-minor sufficient lemma, together with the elementary
half-row domination `H(F)>=H(B)`, already proves

`det K_F[rows,cols]>=4 det K_B[rows,cols]`.

This assertion concerns `F`, not `H=F+G`. The added positive polynomial
cannot be treated as preserving folded TP2 without controlling its
mixed defects.

## An exact negative mixed defect

Write `f_n=H(F)_n`, `g_n=H(G)_n`. The coefficient of `uv` in
`delta_n(uF+vG)` is

`C_n=2f_n g_n-f_(n-1)g_(n+1)-g_(n-1)f_(n+1)`
`    -2f_(n+1)g_(n+1)+f_n g_(n+2)+g_n f_(n+2)`.

Here `deg F=3m+5`, `deg G=d=2m+1`. At the first index beyond the
support of `G`, namely `n=d+1=2m+2`, the expression is exactly

`C_(2m+2)=-g_(2m+1) f_(2m+3)<0`.                       (1)

Both factors are strictly positive; in particular
`g_(2m+1)=3*2^(2m-1)`. Thus a blanket claim that the two summands
`F,G` have nonnegative mixed defects, or strongly compatible folded
kernels, is false. Equation (1) rules out that proposed route for
every `m>=1`, not merely at a sampled index.

It does **not** show that `H` fails the cone or the target relative
bound: the positive diagonal defect of `F` can absorb a negative
mixed term. That quantitative absorption is the missing argument.

## A proved reduction of the missing strength bound to low indices

The negative term in (1) can in fact be absorbed uniformly. Since
`F` is in the folded cone, its half-row is nonincreasing. Therefore

`delta_(d+1)(H)=delta_(d+1)(F)-g_d f_(d+2)`
`                 >=(lambda_m-g_d) f_(d+1)`.

At every `n>=d+2` all mixed and `G` terms vanish, so
`delta_n(H)=delta_n(F)>=lambda_m f_n`.

These tail estimates already exceed the strength needed by the
relative-minor lemma. To see this without asymptotics, at `x=2` the
inner recurrence parameter is7, and

`B(2)=sum_{j=0}^{m-1}U_j(7/2)<=sum_{j=0}^{m-1}7^j<7^m/6`.

Moreover

`lambda_m-g_d=(9/4)8^m-(3/2)4^m>(4/3)7^m>8H(B)_0`.

For the middle inequality, divide by `8^m`: its left side is at
least `3/2`, whereas the right side is at most `7/6`, for `m>=1`.
Consequently the full desired strong bound

`delta_n(H)>8H(B)_0 H(H)_n`

is already proved for every `n>=2m+2` in the support of `H`.
The unresolved strong-cone route is precisely its low-index range
`0<=n<=2m+1`, together with the single-block/smoothed assertions
needed for all outer initial cases. No tail extrapolation is needed.

## Exact inner structure available for the remaining argument

Set `V_j=U_j(z/2)+U_(j-1)(z/2)`. The coefficient pair has the
factorizations

`A=U_h V_(h+1)`, `B=U_(h-1)V_h` when `m=2h`,
`A=U_(h+1)V_(h+1)`, `B=U_h V_h` when `m=2h+1`.

Thus `B/A` is a product of two positive Jacobi resolvents. After
partial fractions it is a positive sum of

`1/[(z-alpha_i)(z-beta_j)]`, `alpha_i,beta_j in [-2,2]`.

Factoring all other inner roots reduces `(A,B)` to degree-two
coefficient templates. The obstacle is that an individual inner
factor `z-alpha` need not be a cone polynomial; one must repair its
root groups and prove compatibility between distinct inner summands.

Two additional exact identities may be useful. With `T=T_m`,

`A+B=zT+1`, `T²+B²-zTB=T+B`,

and

`A-4y²B=U_m(z/2)+(z-1)U_(m-1)(z/2)+z`.

The last right-hand side has positive ordinary coefficients, but is
not generally a cone polynomial: at `m=1` it equals `3z-1=6x+8`,
whose central folded defect is `-8`. These identities therefore
provide algebraic structure, not a completed cone closure proof.

## The low-band midpoint condition is not the whole theorem

Even a proof of the remaining midpoint strength band would discharge
only one part of the arbitrary-`m` argument. The complete route also
needs uniform treatment of:

- The single blocks `L_r=A(t-r)+B` and their `y` multiples, the
  smoothed propagators `y(t-r)`, and the remaining small outer-index
  mixed-gap blocks such as `y[A(t²-1)+Bt]`.
- Compatible-resolvent propagation to the full mixed gaps and
  prefixes, with their required strict supports.
- Quantitative central-defect versus mass bounds for those prefixes,
  sufficient to control the multiplier `2(x+2)+3y²Z`.
- The fixed-proxy comparisons and their remainder margins uniformly
  as the fixed endpoint `P=g_m` varies with `m`.

The uniform initial likelihood-ratio comparisons and exact recurrence
reduction are already proved in `general_one_turn_reduction.md`; the
inner-prefix and propagator strength bounds are also proved separately.
The midpoint low band is a sharply identified open component, not an
asserted equivalent formulation of the entire one-turn Local TP2
problem. For `m=2`, all the additional components above are supplied
by the dedicated certificates and full theorem; no such all-`m`
conclusion is currently established.
