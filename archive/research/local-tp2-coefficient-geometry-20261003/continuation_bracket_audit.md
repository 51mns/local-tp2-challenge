# Independent audit of the all-left bracket theorem

## Verdict

**PASS.** The theorem in `continuation_bracket.md` is a valid infinite result:

`B_k=2+2(x+1)+3(x+1)^2 T_(k+1)`

has strictly positive supported folded defect differences for every integer `k≥0`.

The quantitative Cauchy–Binet argument, all eight root-residue factorizations, exact scaling, parameter-cube certificates, small-index exception, and final strictness argument have been independently checked. The proof does not infer closure under addition. No mathematical gap was found.

This proves cone membership of an **actual factor of the original all-left D**. It does not itself prove the original comparison with `S`, and the source correctly keeps that final comparison separate.

## Independent exact certificate checks

`continuation_bracket_audit.py` uses direct Laurent multiplication with `x=q+q^-1` and five independent parameters. It imports none of the certificate-producing scripts. Evaluation at `x=2` is independently implemented by setting `q=1`, which sums all Laurent coefficients.

The verifier reconstructs the nine claimed margin polynomials and expands every recorded tensor Bernstein basis function back into ordinary powers. It checked all **609** Bernstein coefficients exactly with rational arithmetic, including completeness of each tensor grid, positivity, and the recorded minimum. All checks passed.

| Certificate | Exact minimum Bernstein coefficient |
|---|---:|
| Scaled quartic margin | `4357/4` |
| Residue `n≡0 (mod 8)` | `765891/16` |
| Residue `n≡1 (mod 8)` | `29925279/32` |
| Residue `n≡2 (mod 8)` | `527/4` |
| Residue `n≡3 (mod 8)` | `4861/2` |
| Residue `n≡4 (mod 8)` | `48812` |
| Residue `n≡5 (mod 8)` | `2216235/2` |
| Residue `n≡6 (mod 8)` | `1341410683/64` |
| Residue `n≡7 (mod 8)` | `25791/8` |

As before, these are proofs on the full closed parameter cubes, not sampled parameter values. The independently computed small-case bracket at `n=1` has defect differences `(632,688,240,36)`.

## Quantitative Cauchy–Binet step

For cone polynomials `P,Q`, use `K_(PQ)=K_Q K_P`. The adjacent minor of rows `(0,1)` and columns `(2,3)` is `delta_(PQ)(2)`. Retaining intermediate indices `(0,1)` gives exactly

`delta_(PQ)(2) ≥ delta_Q(0) delta_P(2)`.

All other summands are nonnegative by the TP2 property. Since the kernels have finite bandwidth, the expansion is finite. Thus a strict bound

`delta_P(2)>(2/3)P(2)`

is preserved by multiplication by a cone factor `Q` satisfying `delta_Q(0)≥Q(2)`. Positivity of the masses ensures strictness is retained.

The quartic factor is `Q=16F` for a monic quartic `F=ff'`. Defects scale quadratically, so

`delta_Q(0)−Q(2)=16[16delta_F(0)−F(2)]`.

This is exactly the source certificate with a positive scalar factor. No power of 2 is missing.

## Root residues and complete coverage

The exact prefix factorization is `T_n=U_h V_j`, where `h=floor(n/2)` and `j=ceil(n/2)`. The previously audited root-pair proofs allow the following monic residues after removing quartic groups:

| Index modulo 4 | Residue of U | Residue of V |
|---|---|---|
| 0 | `1` | `1` |
| 1 | `z=x+3/2` | A middle linear factor |
| 2 | `f_c`, `2≤c≤9/4` | An innermost pair |
| 3 | `zf_c`, `7/4≤c≤9/4` | A middle factor times a general pair |

The lower bound `7/4` in the odd U residue includes `U_3`, and the even residue's lower bound 2 includes `U_2`. The quadratic range `[2,9/4]` was independently audited earlier. The entire `zf_c` range `[7/4,9/4]` is inside the certified middle-linear-times-general-pair family by taking `s=3`, `a=3/2`. Thus every allowed residue is in the cone, including all endpoints of its parameter interval.

Combining the U and V residue tables produces exactly the eight residue polynomials implemented by the script:

| n modulo 8 | Combined residue | Degree |
|---|---|---:|
| 0 | One pulled general quartic | 4 |
| 1 | One pulled quartic times a middle factor | 5 |
| 2 | `z` times a middle factor | 2 |
| 3 | `z` times an innermost pair | 3 |
| 4 | An even U pair times an innermost pair | 4 |
| 5 | An even U pair times a middle factor and general pair | 5 |
| 6 | An odd U residue times a middle factor and general pair | 6 |
| 7 | An odd U residue | 3 |

At residue classes 0 and 1, a quartic is available for every `n≥8` and `n≥9`, respectively. Indeed the two factor degrees are then at least 4, and their residue pattern leaves quartic groups. The sole missing positive index is `n=1`, handled explicitly. Every `n≥2` is covered by a certified residue.

The U root pairs have `s=3`, `c∈[5/4,9/4]`, which is a subset of the general pair domain used for V. Consequently every removed quartic is in the certified generic quartic family, even when the two factors originate from different parts of the root grouping. Independent parameter boxes only enlarge the allowable actual root parameters and do not introduce an assumption of independence between actual roots.

The leading coefficient of `T_n` is `2^n`; equivalently it is the product `2^h2^j`. Each removed monic quartic therefore carries scalar 16, and the retained monic degree-d residue carries scalar `2^d`. These account for the full leading coefficient exactly.

## Residue scaling and the coefficient margin

For a residue `R` of degree `d`, write `P_0=y² 2^d R`, where `y=x+1`. Then

`delta_(P_0)(2)=4^d delta_(y²R)(2)`,

`P_0(2)=9·2^d R(2)`.

Therefore the certified inequality

`2^d delta_(y²R)(2)−6R(2)>0`

is exactly equivalent to `delta_(P_0)(2)>(2/3)P_0(2)`. The initial `P_0` belongs to the cone because both `y²` and the residue do. Multiplying by all remaining scaled quartics and applying the quantitative lemma proves

`delta_(y²T_n)(2)>(2/3)(y²T_n)(2)`

for every `n≥2`. The mass is at least any individual Laurent coefficient, so this implies the weaker margin needed for the bracket.

At `n=1`, the row of `P=y²T_1` is `(20,16,8,2)`, with `delta_P(2)=28`. Thus the needed strict inequality `3delta_P(2)>2H(P)[3]` also holds. The stronger mass inequality is not asserted for this exception.

## Final bracket identities and strict support

Writing `B=3P+(2x+4)`, direct expansion gives the four displayed defect identities in the source. Their constants and signs are correct. The first two are strictly positive because cone membership yields symmetric unimodality and because the additive constants are positive. The third is positive by the margin above. For indices at least 3, the defect is `9delta_P(n)`.

The source correctly avoids applying strict product closure directly to `y²`, whose defect at index 1 is zero. Its replacement Cauchy–Binet argument is valid. With `d=deg T≥1`, the chosen minor of `K_T` is `delta_T(n)>0` for `n≤d`. The second minor, from `K_(y²)`, equals 4, 8, or 5 at `n=0`, `n=1`, or `n≥2`, respectively. For the two terminal indices `n=d+1,d+2`, the intermediate pair `(d,d+1)` gives first minor `delta_T(d)>0` and second minor exactly 1. Hence `P=y²T` has strictly positive defects on its whole support.

It follows that every supported defect of B is strictly positive, including all terminal indices. Since B has positive coefficients throughout its support, the folded-kernel criterion applies without any zero-support exception.

## Research scope

The all-left bracket-cone theorem is verified and suitable for the research continuation branch. The proof uses exact finite certificates for parameterized building blocks and an unbounded factorization argument; it is not a finite-depth extrapolation. A separate argument is still required for the full original Local TP2 comparison between D and S.

## Final sandwich requires only a weak remaining comparison

The root agent's final strictness strengthening is verified. Set `A=x+2`, `E=yT_k`, `Cproxy=AB_k`, and `D=EB_k`. The proved first sandwich comparison gives nonnegative ordered minors between `H(A)` and `H(E)`. Its first minor is strictly positive:

`c01=2H(E)[1]−H(E)[0]>0`.

Indeed E is the sum of p_j from j=0 through k; the p_0 contribution to this expression is 1, the p_1 contribution is 3 when present, and all later contributions are nonnegative by the proved likelihood-ratio comparison.

Cauchy–Binet for the two-row matrix `(H(A),H(E))` multiplied by `K_(B_k)` therefore gives, at every adjacent index n,

`W(Cproxy,D;n)≥c01·delta_(B_k)(n)>0`

for `0≤n≤deg B_k`. The retained intermediate columns are `(0,1)`; all omitted terms are nonnegative.

Here `deg B_k=deg S=k+3`, while Cproxy has degree one greater. Consequently it is enough to establish the **weak** remaining comparison

`H(S)≤lr H(Cproxy)`.

For `n<deg S`, ratio transitivity with the strict Cproxy-to-D comparison gives a strict S-to-D adjacent minor. At `n=deg S`, strictness follows directly from the positive terminal S coefficient and the positive D coefficient at the following index. Thus no additional strictness assumption is needed on the remaining proxy comparison. This verifies a reduction only; the remaining weak comparison is not proved in this package.
