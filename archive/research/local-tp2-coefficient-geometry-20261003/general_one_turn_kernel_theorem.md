# Relative kernel compatibility and the entire L²Rᵏ increment family

**Status: proved for every outer index `k>=0` with the fixed inner index `m=2`.** This establishes strict folded-cone membership for the increment and prefix polynomials associated with `L²R^k`. It is not a proof of all inner indices or of Local TP2 on this ray.

## Fixed boundary and exact coefficient data

Let `y=x+1`, `z=2x+3`, and let `I_j=sum_(i=0)^j U_i(z/2)` denote the inner prefix polynomials. For `m=2`, put

`A=I_3=33+64x+40x²+8x³`,

`B=I_1=4+2x`,

`P=1+yI_2=13+26x+18x²+4x³`,

`t=3yP-x=39+116x+132x²+66x³+12x⁴`.

For the outer recurrence put `u_j=U_j(t/2)`, `u_-1=0`, `T_j=sum_(i=0)^j u_i`, and `T_-1=0`. The exact canonical formulas established by the one-turn recurrence are

`q_k=y[A u_k+B u_(k-1)]`,

`C_k=1+yZ_k`, `Z_k=A T_k+B T_(k-1)`.

Here `C_0=1+yI_3` is the center at `L²`, and the fixed endpoint is `P=1+yI_2`.

## Certified polynomial families

For independent parameters `r,s,c in [-2,2]`, define

`f_r=t-r`,

`L_r=A(t-r)+B`,

`H_(r,s,c)=A(t-r)(t-s)+B(t-c)`.

The exact rational Bernstein computation in `general_one_turn_kernel_cert.py` certifies:

- Strictly positive supported Laurent half-rows and strictly positive supported folded defects for `A`, `B`, `f_r`, `yf_r`, `L_r`, `yL_r`, `yA`, and `H_(r,s,c)`.
- The same strict properties for `y[A(t²-1)+Bt]`, the outer degree-two increment.
- The relative minor bound

  `det K_(H_(r,s,c))[rows,cols] >= 4 det K_B[rows,cols]`

  for every ordered pair of rows and every ordered pair of columns of the infinite folded multiplication kernels.

All parameter substitutions are `-2+4u` on independent unit intervals. Defects and relative minors are expanded in the tensor Bernstein basis with exact rational coefficients. The exported defect certificates and the complete list of representative minor bounds are in `general_one_turn_kernel_certificates.json`. The script imports only the already audited elementary polynomial/Bernstein routines from `mixed_ray_kernel_cert.py`.

The relative assertion is a continuum theorem about infinite kernels, not a scan in the outer recurrence index. Its exact finite reduction is proved next.

## Why the 1,543 representative minors cover all indices

The half-row of `B` is `(4,2)`, so `K_B` has bandwidth1 and is TP2. The degree of `H` is11. Consider rows `i<j` and columns `k<l`.

If the `B` minor is zero, the desired comparison follows from the separately certified TP2 of `K_H`. If the `B` minor is positive, both diagonal entries of its two-by-two submatrix must be positive, because all entries are nonnegative. Thus

`k=i+e`, `l=j+f`, where `e,f in {-1,0,1}`.

Write `d=j-i>=1`. It suffices to consider `0<=i<=13` and `1<=d<=13`:

1. If `i>13`, shift all four indices down by `i-13`. Before and after this shift every index is positive. Every Hankel index (row plus column) exceeds11, so every entry of `K_H` is just its Toeplitz term `h_(|row-column|)`. The same holds for `K_B`. Differences of indices are preserved, so both minors are unchanged.
2. If `d>13`, replace `d` by13, leaving `i,e,f` fixed. The two off-diagonal distances are `d+f` and `d-e`, both greater than11 before and after replacement. Thus the off-diagonal entries of `K_H` vanish, as do those of `K_B`. The lower diagonal indices are both positive and have sum greater than11, so their entry is exactly `h_(|f|)`, independent of `d`; the upper diagonal entry is unchanged. Both minors are therefore unchanged. The required order `k<l` remains valid because the new difference `l-k=13+f-e` is positive.

Apply these reductions successively. They preserve nonnegative indices, ordered pairs, and both kernel minors. The generator enumerates all resulting `i,d,e,f`, retaining the valid column indices and the cases with a positive `B` minor. There are exactly1,543 such patterns.

For each pattern the generator proves that every Bernstein coefficient of `det K_H-4det K_B` is strictly positive. The smallest coefficient over all patterns is

`327364154597925`,

attained for rows and columns `(0,1)`. Consequently the relative minor inequality holds for every infinite-kernel index pair and every independent parameter triple in the entire cube.

## General relative compatibility lemma

For any two folded kernels define their symmetrized mixed minor as the coefficient of `ab` in a selected minor of `aK_F+bK_G`.

Let

`F=A(t-r)(t-s)+B(t-s)`,

`G=A(t-r)(t-s)+B(t-r)`.

Their difference is `(r-s)B`, and their midpoint is `H_(r,s,(r+s)/2)`. Linearity of the folded kernel gives, on every ordered row/column pair,

`mixed(K_F,K_G)=2det K_H-((r-s)²/2)det K_B`.

Because `K_B` is TP2, `|r-s|<=4`, and `det K_H>=4det K_B`, every such mixed minor is nonnegative. This is the needed pairwise compatibility. It is stronger than individual cone membership and is not inferred from arbitrary positive-sum closure.

As in the mixed-ray theorem, multiplication of both polynomials by a common folded-cone factor preserves compatibility: compare the coefficient of `ab` in Cauchy–Binet for `(aK_F+bK_G)K_Q`.

## All outer indices

Let `p_N` be either the ordinary outer Chebyshev sequence or its adjacent-sum sequence `v_N=u_N+u_(N-1)`, with `N>=1`. Their Jacobi resolvents give

`p_(N-1)(t)/p_N(t)=sum_i lambda_i/(t-r_i)`,

where all roots lie in `[-2,2]`, the residues are positive, and they sum to1. These facts and the boundary cases are proved in `mixed_ray_kernel_theorem.md`.

Consequently

`A p_N(t)+B p_(N-1)(t)`

is the positive weighted sum of

`[A(t-r_i)+B] product_(l!=i)(t-r_l)`.

Every summand is a strict folded-cone product. For two distinct summands, removing the common omitted-root product leaves exactly the pair `F,G` above, so every pair has nonnegative mixed minors. Expanding every kernel minor into its diagonal and mixed terms proves TP2. All summands have the same degree and all diagonal terms have strictly positive supported defects, hence

`delta_n(sum_i lambda_i F_i)>=sum_i lambda_i²delta_n(F_i)>0`

at every supported index.

For the actual increments `q_k`, when `k>=3` an additional factor `y` can be absorbed into one of the at least one common omitted-root factors in every off-diagonal pair; `y(t-r)` is certified in the cone. The diagonal terms use the certified `yL_r`. For `k=0,1,2`, the required polynomials are `yA`, `yL_0`, and `y[A(t²-1)+Bt]`, already certified. Thus every `q_k` has strictly positive supported folded defects.

Finally use the exact outer prefix identities

`T_(2h)=u_h v_h`, `T_(2h+1)=u_h v_(h+1)`.

They give

`Z_(2h)=v_h[A u_h+B u_(h-1)]`,

`Z_(2h+1)=u_h[A v_(h+1)+B v_h]`.

The bracketed factors are covered by the preceding resolvent argument, and every outer root factor `t-r` is in the strict cone. This proves the assertion for `Z_k`. Absorbing `y` into an outside root factor proves it for `yZ_k` whenever that factor is nonconstant; the remaining cases are `yZ_0=yA` and `yZ_1=y[A(t+1)+B]=yL_(-1)`, both already certified.

Therefore `q_k`, `Z_k`, and `yZ_k` have strictly positive supported folded defects for every `k>=0` on `L²R^k`.

## Remaining scope

The relative compatibility identity itself applies to any `A,B,t` satisfying the certified hypotheses. The continuum block and relative-minor certificates here are for `m=2` only. No all-`m` assertion follows from them.

The multiplier `M_k=2(x+2)+3y²Z_k` still requires its quantitative low-index defect bound, and the original Local TP2 comparison additionally needs the appropriate proxy and endpoint comparisons. The theorem above supplies the infinite family of folded kernels; it does not silently identify these with the entire original conclusion.
