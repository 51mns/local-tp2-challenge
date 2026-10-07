# The entire all-right multiplier family has a strict folded-TP2 kernel

Put `y=x+1`, `P=x+2`, `t=3x^2+8x+6`, and let

`T_k(t/2)=sum_(j=0)^k U_j(t/2)`.

Then, for every integer `k>=0`,

`M_k=2P[1+3y^2 T_k(t/2)]`

has strictly positive supported folded defects. Thus its folded
convolution kernel is TP2. This is an infinite factorization argument;
the certificates below hold on an entire real parameter interval.

## 1. Root factors

The established prefix identities

`T_(2h)=U_h(U_h+U_(h-1))`,

`T_(2h+1)=U_h(U_(h+1)+U_h)`

show that all k roots of the monic degree-k polynomial `T_k(t/2)` lie
in `[-2,2]` as roots in the variable t. The individual root descriptions
are the usual real roots of second-kind Chebyshev polynomials and their
adjacent sums. Therefore, when `k>=1`,

`T_k(t/2)=product_(i=1)^k Q_(c_i)(x)`,

where

`Q_c=3x^2+8x+c`, `4<=c<=8`.

There is no additional scalar factor: `U_j(t/2)` is monic in t.

The Fourier row and folded defects of a root factor are

`H(Q_c)=(c+6,8,3)`,

`delta(Q_c)=(c^2+15c-74,37-3c,9)`.

On `[4,8]` these defects are at least `2`, `13`, and `9`, respectively.
Every root factor is therefore in the strict folded cone.

## 2. A quantitative product lemma at index one

For any folded-cone polynomial A, apply Cauchy-Binet to

`K_(AQ)=K_A K_Q`,

using outer rows `(0,1)`, outer columns `(1,2)`, and retaining the single
intermediate pair `(1,2)`. Since all other summands are nonnegative,

`delta_(AQ)(1) >= delta_A(1) D_Q`,

where

`D_Q=det K_Q[(1,2),(1,2)]`

`=(c+9)(c+6)-64=c^2+15c-10`.

Ordinary evaluation at x=2 gives the total symmetric Fourier mass:

`Q_c(2)=c+28`.

The decisive uniform inequality is

`D_Q-Q_c(2)=c^2+14c-38 >= 34 > 0`.

Consequently the strict mass margin

`3 delta_A(1) > A(2)`

is preserved by multiplication by every root factor Q_c. Indeed,

`3 delta_(AQ)(1) >= 3 delta_A(1) D_Q`

`> A(2) D_Q > A(2) Q_c(2)=(AQ_c)(2)`.

## 3. Uniform initial block

Take `A=y^2 Q_c`. Its Fourier row is

`H(A)=(3c+56,2c+50,c+31,14,3)`.

Its folded defects are

`4c^2+85c-128`,

`17c+503`,

`c^2+37c+158`,

`94-3c`,

`9`.

These are strictly positive throughout `[4,8]`, with respective lower
bounds `276,571,322,70,9`. Moreover,

`A(2)=9(c+28)`,

`3 delta_A(1)-A(2)=42c+1257 >= 1425 > 0`.

Starting from this block and multiplying by the remaining k-1 root
factors proves, for every `k>=1`, that

`A_k=y^2 T_k(t/2)`

lies in the strict folded cone and satisfies

`3 delta_(A_k)(1)>A_k(2)>=H(A_k)[2]`.

The strict cone conclusion uses the already proved strict multiplicative
closure; both the initial block and every subsequent Q_c are strict.

## 4. Adding the constant and completing the multiplier

Write `a_n=H(A_k)[n]` and `G_k=1+3A_k`. Direct expansion gives

`delta_(G_k)(0)=9delta_(A_k)(0)+6a_0+3a_2+1`,

`delta_(G_k)(1)=9delta_(A_k)(1)-3a_2`,

`delta_(G_k)(n)=9delta_(A_k)(n)` for `n>=2`.

Every expression is strictly positive when `k>=1`, using the mass
margin at index one. The factor P has Fourier row `(2,1)` and defects
`(2,1)`, so strict product closure proves the result for `M_k=2P G_k`.

The exceptional index `k=0` must be handled after multiplication by P:
`G_0=1+3y^2` alone is not in the cone. Directly,

`H(M_0/2)=(32,25,12,3)`,

`delta(M_0/2)=(158,172,60,9)`.

This proves the stated strict folded-cone theorem for every `k>=0`.

The accompanying standard-library Python verifier
`resumed_extension_right_multiplier.py` verifies all displayed polynomial
identities and interval bounds exactly, using the existing rational
polynomial/Bernstein utility module. No k-cutoff or numerical sample of
the parameter interval occurs in the proof.
