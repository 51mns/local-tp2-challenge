# A canonical multiplicative strip

This is a global induction theorem for every canonical state. It is a
coefficientwise support theorem, not a proof of Local TP2 or folded-kernel
membership.

Put `y=x+1` and let `B_j=sum_{i=-j}^j q^i`, with `x=q+q^{-1}`. Write
`F>=_B G` when every coefficient of `F-G` in this character basis is
nonnegative. The character product rule is

`B_i B_j=sum_{r=|i-j|}^{i+j} B_r`.

The universal positivity theorem in `resumed_extension_kernel_support.md`
gives dense positive character rows for every canonical polynomial and
every center-endpoint gap. Every endpoint `T` also satisfies

`alpha_T(1)>=alpha_T(0)-1`.                           (1)

Indeed the two original endpoints `1,x+2` have rows `(1)` and `(1,1)`;
every other endpoint is a previous center, whose first character
coefficient is at least its zeroth coefficient. Consequently

`1+xT>=_B0`.                                        (2)

To check (2) explicitly, its character coefficients are
`1+t_1-t_0` at zero, `t_0+t_2` at one, and
`t_{n-1}+t_{n+1}` at `n>=2`.

## 1. Strengthened additive separation

Every canonical triple `(A,C,B)` satisfies

`C-y(A+B)>_B0`,                                     (3)

with strict positivity at every character index through `deg C`.

At the root, the difference is `x^2+2x+2`, with character row `(2,1,1)`.
For the child `U=3yAC-x(A+C)-B`, the exact identity is

`U-y(A+C)=y(C-2)+y(A-1)(3C-2)+A+(C-B)`.              (4)

Every term is character-nonnegative: the prior universal theorem gives
`C>=_B3`, `A>=_B1`, and `C-B>_B0`. The first term is dense and positive
through `deg C+1`: `C-2` is dense positive, and its positive coefficient
at index one supplies the zeroth coefficient after multiplying by `y`.
If `deg A>=1`, the product term is dense positive through
`deg A+deg C+1=deg U`, using the character product rule exactly as in
the universal support proof. If `deg A=0`, the first term already reaches
`deg U`. The right child has the same proof after interchanging the
endpoints. This proves (3) throughout the tree.

## 2. Multiplicative strip

At any canonical state, sort the endpoints by degree as `X,Y`, where
`deg X<deg Y`, and set

`t_X=3yX-x`.

Then

`(t_X-1)Y <_B C <=_B t_XY`.                         (5)

Here the left inequality means that the difference is dense and strictly
positive through its own degree, not through the larger degree of `C`.
At every nonroot state this difference has degree `deg Y`; at the root
it is the constant `1`.

Proof: in a nonroot state, `Y` is the preceding center. Let `T` be the
endpoint replaced in the previous mutation, so the preceding endpoints
were `X,T`. The exact mutation equation is

`C=t_XY-xX-T`.

Therefore the lower-strip remainder is

`rho=C-(t_X-1)Y=Y-T-xX`
`   =[Y-y(X+T)]+X+xT`.                              (6)

The bracket is dense positive through `deg Y` by (3), applied to the
preceding triple. Also

`X+xT=(X-1)+(1+xT)>=_B0`

by (2). Thus `rho` is dense positive through `deg Y`.
On the other hand,

`Y-rho=T+xX=(T-1)+(1+xX)>=_B0`,                     (7)

so `rho<=_B Y`. Equations (6)-(7) prove the strip and, more precisely,

`C=(t_X-1)Y+rho`, `0<_B rho<=_B Y`.                 (8)

At the root `X=1`, `Y=x+2`, `t_X=2x+3`, and
`C-(t_X-1)Y=1`, while `t_XY-C=y`; hence the same assertion holds there.

The ordering of the endpoints is essential: the argument uses that the
larger endpoint is the preceding center. No assertion with `X,Y`
interchanged is made.

## 3. Relation to the unresolved kernel problem

The strip gives a canonical correlation between consecutive polynomials
which is absent from the previously refuted abstract mutation bundle.
For its explicit noncanonical counterexample with `X=1`,
`Y=71+128x+58x^2`, `C=32+122x+120x^2+29x^3`, the difference
`C-2yY` has a negative leading coefficient `29-116=-87`.

Nevertheless (5) is a comparison of linear character coefficients.
Folded TP2 concerns quadratic defect differences, and is not monotone
under this coefficientwise order. Thus (5) does not by itself prove
that `K_C` or either child kernel is TP2. The remaining task is a
quantitative mutation estimate using this strip together with the exact
Fricke relation; no such estimate is asserted here.

The residual is not even a folded-cone polynomial in general. At the
first left node, `X=1`, `Y=2x^2+6x+5`, and

`rho=2x^2+4x+3`, `H(rho)=(7,4,2)`.

Its defect differences are `(31,-2,4)`. Its two adjacent LR minors
against `H(Y)=(9,6,2)` are `(6,-4)`. Thus neither cone membership of
the positive residual nor a uniform LR order between `rho` and `Y`
can be used to complete a positive-sum argument. This obstruction occurs
at a canonical state, although the center at that state is in the cone.
