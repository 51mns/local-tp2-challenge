# The all-left bracket multiplier is strictly folded-TP

**Later update:** The original all-left Local TP2 comparison left open at this stage is now proved in `resumed_comparison_all_left.md`, audited in `resumed_audit_all_left.md`. The full tree remains open. The earlier derivations below are retained as proof ingredients.

Let `U_j=U_j(x+3/2)`, `T_n=sum_(j=0)^n U_j`, `y=x+1`, and

`B_k=2+2y+3y²T_(k+1)`.

This note proves that `B_k` has strictly positive folded defects throughout its support for every `k>=0`. It uses the established folded-kernel product theorem and the root-factor results in `continuation_ray.md` and `continuation_prefix.md`. The original comparison `H(B_k yT_k)>lr H(yU_(k+2))` is a separate question and remains open here.

## A quantitative Cauchy–Binet lemma

For a folded-cone polynomial `P`, write `delta_P(n)` for its folded defect. If `P,Q` are in that cone, the product kernel is `K_(PQ)=K_Q K_P`. Cauchy–Binet applied to rows `(0,1)` and columns `(2,3)`, retaining just intermediate columns `(0,1)`, gives

`delta_(PQ)(2) >= delta_Q(0) delta_P(2)`.

Every discarded summand is nonnegative. Consequently the inequality

`delta_P(2) > (2/3)P(2)`

is preserved under multiplication by any folded-cone `Q` with

`delta_Q(0)>=Q(2)`.

The notation `P(2)` means ordinary evaluation at `x=2`, equivalently the total mass of its symmetric Laurent coefficients. It bounds every individual Fourier coefficient from above.

## Scaled quartic multipliers

All quartic groups arising from the root factorizations of `U_h` and `V_j=U_j+U_(j-1)` are covered by

`Q=16 f_(s,c) f_(s',c')`,

where `f_(s,c)=x²+s x+c` and the parameter domain is

`s=3+u`, `c=5/4+5u/2+v`, `u,v in [0,1]`,

with independent primed parameters. The monic quartic is in the folded cone by the preceding block certificates. The additional exact Bernstein certificate is

`16 delta_(f f')(0) - (f f')(2) > 0`.

After accounting for the factor `16`, this is exactly `delta_Q(0)>Q(2)`.

## Eight residue certificates

Write `n=k+1`, `h=floor(n/2)`, `j=ceil(n/2)`, so `T_n=U_h V_j`. Remove quartic groups from each factor, keeping one residue of degree at most three per factor. Positive leading coefficients are retained exactly: a monic quartic contributes the scaled block `16 f f'`; a monic residue `R` of degree `d` contributes `2^d R`.

The allowed residues of `U_h` according to `h mod 4` are

| h mod 4 | Monic residue |
|---|---|
| 0 | `1` |
| 1 | `z=x+3/2` |
| 2 | `f_c=x²+3x+c`, `2<=c<=9/4` |
| 3 | `z f_c`, `7/4<=c<=9/4` |

For the nontrivial pair residue, choose the root pair nearest to the central angle. For even `h>=2`, its `c` is at least `9/4-sin²(pi/6)=2`. For odd `h>=3`, it is at least `9/4-sin²(pi/4)=7/4`. The upper bound is always `9/4`. These residues are in the folded cone: the quadratic range `[2,9/4]` has positive defects, and `z f_c` is a case of the certified middle-linear-times-quadratic block.

The residues of `V_j`, according to `j mod 4`, are

| j mod 4 | Monic residue |
|---|---|
| 0 | `1` |
| 1 | `x+a`, `3/2<=a<=2` |
| 2 | `(x+a)(x+b)`, `1<=a<=3/2`, `3/2<=b<=5/2` |
| 3 | `(x+a)f_(s,c)`, `3/2<=a<=2`, generic allowed pair |

All are precisely the certified prefix blocks. Combining these residues gives the eight cases below. If `n mod 8` is zero or one, pull one available quartic into the residue. Such a quartic exists when `n>=8` or `n>=9`, respectively. The lone exceptional index `n=1` is handled directly.

| n mod 8 | Residue degree d |
|---|---:|
| 0 | 4 |
| 1 | 5 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 3 |

For each of these parameterized residue families, an exact positive Bernstein certificate proves

`2^d delta_(y²R)(2) - 6R(2) > 0`.

Since `y²(2)=9`, scaling both sides shows exactly

`delta_(y² 2^d R)(2) > (2/3)(y² 2^d R)(2)`.

All coefficients and lower bounds are in `continuation_bracket_certificates.json`; the standalone script `continuation_bracket_certify.py` regenerates them in rational arithmetic. It imports the polynomial/Bernstein routines from `continuation_prefix.py`. There are no sampled parameter values: positive Bernstein coefficients certify each entire parameter cube.

Both `y²` and all residue blocks lie in the folded cone, so the quantitative Cauchy–Binet lemma can be applied successively to the remaining scaled quartic factors. It follows for every `n>=2` that

`delta_(y²T_n)(2) > (2/3)(y²T_n)(2) >= (2/3)H(y²T_n)[3]`.

For `n=1`, `y²T_1=2(x+1)²(x+2)` has Fourier row `(20,16,8,2)` and `delta(2)=28`, so the final, weaker coefficient margin also holds strictly: `3*28>2*2`.

## Bracket conclusion

Put `P=y²T_(k+1)` and `h_n=H(P)[n]`. The exact defect identities from the prefix note are

`delta_B(0)=9delta_P(0)+24(h_0-h_1)+12h_2+8`,

`delta_B(1)=9delta_P(1)+12(h_1-h_2)+6h_3+4`,

`delta_B(2)=9delta_P(2)-6h_3`,

`delta_B(n)=9delta_P(n)` for `n>=3`.

The first two are strictly positive by cone membership and symmetric unimodality of `P`. The coefficient margin just proved makes the third strictly positive.

For completeness, `y²` has a zero defect at index one, so the theorem requiring **both** factors to have all strict supported defects cannot be invoked directly. Instead let `d=deg T_(k+1)>=1`, and apply Cauchy–Binet to `K_T K_(y²)`, rows `(0,1)` and columns `(n,n+1)`. For `0<=n<=d`, retain intermediate pair `(n,n+1)`: the first minor is the strictly positive `delta_T(n)`, and the second minor of `K_(y²)` is `4` if `n=0`, `8` if `n=1`, and `5` if `n>=2`. For `n=d+1` or `n=d+2`, retain intermediate pair `(d,d+1)`; the first minor is `delta_T(d)>0` and the second minor equals `1` in either case. Thus `P=y²T` has strictly positive defects at every supported index. Consequently the remaining expressions `9delta_P(n)`, `n>=3`, are strictly positive as well. This proves the bracket theorem.

The full ray Local TP2 comparison is not a consequence of both factors being in the cone; that unjustified implication is specifically not used.

## Only a weak final comparison is needed

Let `A=x+2`, `E=yT_k`, `Cproxy=AB_k`, and `D=EB_k`.
The proved first sandwich gives `H(A)<=_lr H(E)`. Its minor on columns
`0,1` is strictly positive:

`c01=2H(E)[1]-H(E)[0]>0`.

Indeed `E=sum_(j=0)^k p_j`; the `p_0` contribution to this minor is 1,
the `p_1` contribution is 3 when present, and all subsequent contributions
are nonnegative by the proved ordering. Cauchy–Binet, retaining intermediate
columns `0,1`, therefore gives

`W_n(Cproxy,D)>=c01*delta_(B_k)(n)>0`

for every `0<=n<=deg B_k=deg S=k+3`, where
`W_n(F,G)=H(F)[n]H(G)[n+1]-H(F)[n+1]H(G)[n]`.

Consequently the remaining **weak** inequality

`H(S)<=_lr H(Cproxy)`

would suffice for the original **strict** conclusion. At `n<deg S`, all
relevant coefficients are positive, so likelihood-ratio transitivity with
the strict second step applies. At `n=deg S`, strictness is automatic from
`H(S)[n]>0`, `H(S)[n+1]=0`, and `H(D)[n+1]>0`.
The weak comparison is still unproved; this paragraph resolves only the
strictness requirement in the proposed reduction.
