# Audit of the all-left comparison chain

This note checks the algebra, orientations, support indices, and strictness
in the resumed all-left proof. The parameter-box certificate arrays have
their own independent audit; this note does not replace that audit.

Write `y=x+1`, `u_j=U_j(x+3/2)`, `T_n=sum_(j=0)^n u_j`,
`V_r=u_r+u_(r-1)`, `W_r=u_r-u_(r-1)`, and `H(P)_n=[q^n]P(q+q^-1)`.
Use `P<=lr Q` to mean

`H(P)_i H(Q)_j-H(P)_j H(Q)_i>=0` for all `i<j`.

## Exact canonical identification

At the canonical node `L^k`, put `C_k=1+yT_(k+1)` and
`C_(-1)=x+2=1+yT_0`. The endpoint polynomials are `A=1` and
`B=C_(k-1)`. Indeed, the left-child recurrence is exactly

`C_(k+1)=(2x+3)C_k-C_(k-1)-x`.

Its successive gaps have initial values `y u_1,y u_2` and obey the
homogeneous Chebyshev recurrence, giving

`S=C_(k+1)-C_k=y u_(k+2)`.

The two children have degrees `k+3` and `2k+4`, respectively, so the
left child is the shorter one for every `k>=0`. Subtracting their
canonical formulas gives

`D=(B-1)(3yC_k-x+1)=yT_k B_k`,

where `B_k=2+2y+3y^2 T_(k+1)`.

## The common intermediary

Put `m=k+2`, `E=yT_(m-1)`, `A_*=2x+1`, `U_*=u_2=4x^2+12x+8`,
and `K=2(x+2)^2`. The bracket proxy has the exact normalization

`C_*=(x+2)B_k=(3/4)U_* E+K`.

Here `deg S=deg(A_*E)=m+1`, `deg C_*=m+2`, and `deg D=2m`.
For the infinite step `k>=6`, all these half-rows are positive
throughout their respective supports.

For even `m=2r` and `r>=3`, the audited difference-polynomial theorem
gives `W_r<=lr (2x+1)u_(r-1)`. The multiplier `yV_r` has a folded-TP2
kernel by `resumed_external_yV.md`; thus

`S=yV_r W_r <=lr yV_r (2x+1)u_(r-1)=A_*E`.

For odd `m=2r+1`, the first-kind theorem in
`resumed_ray_firstkind.md` gives the same conclusion. Its identities are

`u_(2r+1)=u_r c_(r+1)`, `T_(2r)=u_r V_r`,

`c_(r+1)-c_r=(2x+1)V_r`,

where `c_j=2T_j^(first kind)(x+3/2)`. Consecutive `c_j` rows are weakly
MLR ordered, and the common factor `yu_r` is in the folded cone.

The already proved first actual-ray sandwich is

`H(x+2)<=lr H(yT_k)`.

Multiplying by the folded kernel of `B_k` consequently gives

`C_*<=lr D`.

Thus the single remaining comparison in this chain is `A_*E<C_*`.

## Strictness after multiplication of a certified residue

Suppose `e` is a positive residue of degree `d+1`. Then
`deg(A_*e)=a=d+2` and `deg(U_*e)=a+1`. The finite-residue certificate
must include indices `0,...,a`, including the terminal pair minor.
The loop `range(d+3)` in `resumed_comparison_margin.py` does exactly
this.

Assume all these minors are strictly positive and let `Q` be a factor
of degree `t` with strictly positive folded defect differences
`delta_Q(j)` for every `0<=j<=t`. For a desired product index
`0<=n<=a+t`, retain the Cauchy--Binet intermediate pair

`i=min(n,a)`, `i+1`.

The input pair minor is positive. In the corresponding folded-kernel
minor, `0<=n-i<=t`. If `i=0`, that minor equals `delta_Q(n)>0`.
If `i>=1`, the interior formula from the folded-kernel theorem bounds
it below by

`Delta_Q(n-i)-Delta_Q(n+i+1)>=delta_Q(n-i)>0`.

If the second index lies outside support, the boundary formula gives
the same lower bound. All other Cauchy--Binet terms are nonnegative.
Consequently multiplying by `Q` preserves strict pair minors through
the full enlarged support, not merely through the residue's support.

For quantitative low-index margins, the principal kernel minor is at
least `delta_Q(0)`. Hence a bound `delta_Q(0)>=c Q(2)` multiplies the
ratio of the selected pair minor to polynomial mass by at least `c`.
This justifies the additional quartic boost `c=4` in residue classes
two and three, once the quartic certificate has been verified.

## Low-index correction and final strictness

Let `M_n(E)` be the pair minor of `A_*E,U_*E`. Since `H(K)=(12,8,2)`
and `A_*(2)=5`,

`M_n(A_*E,K)>=-5 H(K)_n E(2)`.

Thus the respective strict margins

`M_0(E)>80E(2)`, `M_1(E)>(160/3)E(2)`,
`M_2(E)>(40/3)E(2)`

imply `M_n(A_*E,C_*)>0` at indices zero, one, and two. The correction
vanishes for `n>=3`, where strictness is supplied by the preceding
Cauchy--Binet argument.

The chain `S<=lr A_*E<lr C_*<=lr D` gives strict original Local TP2
for `n<deg S` by monotonicity of the positive adjacent coefficient
ratios. At `n=deg S`, the desired minor is simply
`H(S)_(deg S) H(D)_(deg S+1)>0`. Thus no unsupported extension of
ratio arguments past a zero coefficient is needed.

The residue construction and additional quartic are available for
every `n=k+1>=7`: classes zero and one begin at eight and nine;
classes two and three, where an extra quartic is used, begin at ten
and eleven. The exceptional actual-ray indices are exactly `k=0,...,5`,
which are covered by the separate exact base calculation.

Conclusion of this audit: the chain, degree accounting, normalization,
and strictness argument are valid. Conditional on the separately
audited eight residue and strengthened quartic certificates, they
prove Local TP2 at every all-left node. This does not cover arbitrary
mixed Farey paths.
