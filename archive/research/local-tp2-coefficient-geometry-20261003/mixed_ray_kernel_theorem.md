# Folded-kernel closure for the first mixed canonical rays

**Status: proved for every index.** The result below proves folded TP2 for both mixed increment families and both mixed prefix families. It uses certified pairwise compatibility, not closure of the folded cone under arbitrary positive sums.

Set

`y=x+1`, `P=2x^2+6x+5`,

`t=3yP-x=6x^3+24x^2+32x+15`,

`w=2(x+2)(2x+3)=4x^2+14x+12`.

Write `u_j=U_j(t/2)`, so `u_0=1`, `u_1=t`, `u_(j+1)=t u_j-u_(j-1)`, and `u_(-1)=0`. Set `v_j=u_j+u_(j-1)` for `j>=0` and `T_k=sum_(j=0)^k u_j`, with `T_(-1)=0`.

The folded cone means the class of positive supported Laurent half-rows `h` for which every `delta_n=(h_n^2-h_(n-1)h_(n+1))-(h_(n+1)^2-h_n h_(n+2))` is nonnegative, with `h_(-1)=h_1`. Equivalently the folded multiplication kernel `K_h` is TP2. We use its already proved multiplicative closure.

## 1. Exact parameter certificates

The standalone script `mixed_ray_kernel_cert.py` uses exact rational arithmetic. It expands every defect in the tensor Bernstein basis on the cube obtained from `a=-2+4r`, `b=-2+4s`, `c=-2+4z`, where `r,s,z` independently range over `[0,1]`. Its complete power coefficients and Bernstein coefficients are saved in `mixed_ray_kernel_certificates.json`.

It proves strict folded-cone membership for all of these blocks:

- `t-a` and `y(t-a)`, for `a in [-2,2]`;
- `w`, `w-1`, `yw`, `t+w`, `t+w+1`, `y(t+w)`, and `y(t+w+1)`;
- `L_a=w(t-a)+1` and `R_a=(t+w)(t-a)-1`, including `yL_a` and `yR_a`;
- `L_(a,b,c)=w(t-a)(t-b)+t-c`;
- `R_(a,b,c)=(t+w)(t-a)(t-b)-t+c`.

For the last two families it proves the stronger uniform bound `delta_0>8`. Every Bernstein coefficient of `delta_0-8` is strictly positive. All parameters in these three-parameter statements are independent.

The same script directly certifies the two degree-two increment cases

`y[w(t^2-1)+t]`,

`y[(t+w)(t^2-1)-t]`.

All listed blocks have strictly positive ordinary `x` coefficients throughout their support. For the only subtractions requiring comment, `t-a` has constant coefficient at least13; hence `(t+w)(t-a)-1` has positive coefficients, and `(t+w)(t-a)(t-b)-t+c` dominates `168t+w(t-a)(t-b)+c`, whose constant coefficient is positive. Thus the positive-support assumption of the folded criterion is satisfied.

For reference the easiest defect lists are explicit:

`H(t-a)=[63-a,50,24,6]`,

`delta(t-a)=[a^2-150a+481,24a+712,240,36]`,

`H(y(t-a))=[163-a,137-a,80,30,6]`,

`delta(y(t-a))=[2071+142a-a^2,3439-224a+a^2,1870+30a,384,36]`.

The finite coefficient certificates prove whole parameter families; they are not finite numerical sampling.

## 2. A principal-minor lower bound

**Lemma.** If `K_h` is folded TP2, then every two-by-two principal minor is at least `delta_0(h)/2`.

First, every adjacent principal minor is at least `delta_0`. For indices `(0,1)` it equals `delta_0`. For later adjacent principal minors this follows directly from the proved interior folded-minor formula, whose two summands are nonnegative and whose defect difference is at least `Delta_0-Delta_1=delta_0`; the support-boundary formula gives the same bound.

The cone implies `Delta_n>=0`, and therefore `h_0>=h_1>=...>=0`. Symmetrize the folded matrix by conjugating with `diag(sqrt(2),1,1,...)`; call the resulting symmetric TP2 matrix `A`, and write `d_i=A(i,i)`. Every diagonal entry lies in `[h_0,2h_0]`.

For `i<j-1`, TP2 applied to rows `(i,i+1)` and columns `(i+1,j)`, followed by the principal minor at `(i+1,j)`, gives

`A(i,j)^2 <= A(i,i+1)^2 d_j/d_(i+1)`.

Consequently

`d_i d_j-A(i,j)^2 >= (d_j/d_(i+1)) [d_i d_(i+1)-A(i,i+1)^2] >= delta_0/2`.

Adjacent pairs already have the stronger bound. Positive diagonal conjugation leaves principal minors unchanged, completing the proof.

## 3. Strong pairwise compatibility

For matrices `A,B`, define their symmetrized mixed two-by-two minor at any fixed ordered row and column pairs by the coefficient of `rs` in `det(rA+sB)`. Explicitly it is

`A11 B22+B11 A22-A12 B21-B12 A21`.

Suppose polynomials `F,G` differ only by a constant `d`. With `H=(F+G)/2`, linearity of folded kernels gives the exact identity

`mixed(K_F,K_G)=2 det(K_H)-(d^2/2) det(I)`

on any chosen row and column pairs. Here `det(I)` vanishes unless the pair is principal, in which case it equals1. Thus if `H` is folded TP2, `delta_0(H)>=8`, and `|d|<=4`, every symmetrized mixed minor is nonnegative by the preceding lemma.

Apply this to the pair

`F=w(t-a)(t-b)+(t-b)`,

`G=w(t-a)(t-b)+(t-a)`.

Its midpoint is `L_(a,b,(a+b)/2)` and `|F-G|=|a-b|<=4`. The certificate proves compatibility. Likewise the pair

`F=(t+w)(t-a)(t-b)-(t-b)`,

`G=(t+w)(t-a)(t-b)-(t-a)`

has midpoint `R_(a,b,(a+b)/2)` and is compatible.

Compatibility is preserved on multiplying both polynomials by a common folded-cone factor. To see this, apply Cauchy–Binet to `det((rK_F+sK_G)K_Q)` and compare the coefficient of `rs`: it is a sum of nonnegative mixed minors multiplied by nonnegative minors of `K_Q`. All sums are finite by bandwidth.

## 4. Jacobi resolvents prove the mixed sum theorem

Let `p_N(z)` be a monic polynomial of degree `N>=1` with simple roots `a_i in [-2,2]`, and suppose

`p_(N-1)(z)/p_N(z)=sum_i lambda_i/(z-a_i)`,

where all `lambda_i>0` and `sum_i lambda_i=1`.

Then both polynomials

`F_N=w p_N(t)+p_(N-1)(t)`,

`G_N=(t+w)p_N(t)-p_(N-1)(t)`

are in the folded cone, with strictly positive defects at every supported index.

Indeed the resolvent identity writes the first as the positive weighted sum of

`F_i=[w(t-a_i)+1] product_(l!=i)(t-a_l)`.

Each summand belongs to the cone by the single-block certificate and product closure. For `i!=j`, remove the common factor `product_(l!=i,j)(t-a_l)`. The remaining pair is exactly the compatible pair in Section3. Thus every pair of summands has nonnegative symmetrized mixed minors. Expanding a minor of `sum_i lambda_i K_(F_i)` into diagonal and pairwise mixed terms proves its nonnegativity. The proof for `G_N` is identical using `R_a` and the second compatible pair. Dense positive support follows from the same decomposition into positive supported blocks.

Strictness follows from the same expansion. Every diagonal summand `F_i` is a product of blocks with strictly positive supported defects; the proved strict multiplicative-closure lemma therefore gives `delta_n(F_i)>0` throughout its support. All summands have the same degree. Since the residues are positive and all mixed minors are nonnegative,

`delta_n(F_N)>=sum_i lambda_i^2 delta_n(F_i)>0`

for every supported `n`, including the terminal index. The identical argument applies to `G_N`.

This applies to both Chebyshev sequences `p_N=u_N` and `p_N=v_N` when viewed as polynomials in the independent variable `z` before substituting `t`. For `u_N`, take the Jacobi matrix with zero diagonal and unit off-diagonals. For `v_N`, take diagonal `(-1,0,...,0)` and unit off-diagonals. Their characteristic polynomials have exactly the stated initial values and recurrence. Their spectra lie in `[-2,2]` by the row-sum bounds. Irreducibility gives simple eigenvalues and nonzero last components of every eigenvector. The last diagonal entry of the resolvent is the ratio of the preceding leading characteristic polynomial to the full polynomial, so spectral decomposition gives the positive residues with sum1.

The needed degree-zero cases are `F_0^u=w`, `G_0^u=t+w`, and `G_0^v=t+w+1`, all separately certified.

## 5. Both actual increment families

For all `j>=0`, define

`q_j^L=y(wu_j+u_(j-1))`,

`q_j^R=y(u_(j+1)+wu_j)`.

Both families belong to the folded cone for every `j`, with strictly positive defects at every supported index.

For `j>=3`, repeat the resolvent proof with an additional factor `y`. In each off-diagonal pair there are `j-2>=1` omitted root factors in common. Absorb `y` into one of them, using the certified cone membership of `y(t-a)`. The remaining common factors are also in the cone, so the same compatibility proof applies. Diagonal terms are products of `yL_a` or `yR_a` with cubic factors and hence are in the cone as well.

The cases `j=0,1,2` are exactly `yw`, `y(t+w)`, the single-block cases with `a=0`, and the two degree-two cases already certified in Section1. Strictness in the resolvent argument follows again from the same-degree diagonal terms, now strict products containing `yL_a` or `yR_a`; the initial cases have explicit strict certificates. This proves the assertion at every index, with no omitted initial case.

## 6. Both mixed prefix families

Set

`Z_k^L=wT_k+T_(k-1)`,

`Z_k^R=T_(k+1)+wT_k`.

Both `Z_k^L,Z_k^R`, and both `yZ_k^L,yZ_k^R`, are in the folded cone for every `k>=0`, with strictly positive defects at every supported index.

Use the exact prefix identities

`T_(2h)=u_h v_h`,

`T_(2h+1)=u_h v_(h+1)`.

They give the factorizations

`Z_(2h)^L=v_h [w u_h+u_(h-1)]`,

`Z_(2h+1)^L=u_h [w v_(h+1)+v_h]`,

`Z_(2h)^R=u_h [v_(h+1)+w v_h]`,

`Z_(2h+1)^R=v_(h+1) [u_(h+1)+w u_h]`.

Every bracket is covered by Section4, including its listed degree-zero cases. Every outside factor is a product of `t-a` with `a in [-2,2]`, so multiplication proves the assertions without `y`.

When the outside factor has positive degree, absorb `y` into one cubic root factor to obtain the assertion with `y`. The only remaining cases are `yZ_0^L=yw`, `yZ_1^L=y[w(t+1)+1]`, and `yZ_0^R=y(t+w+1)`; these were certified explicitly. Thus all cases are covered.

Every nonconstant root factor and every bracket used here has strictly positive supported defects, so strict product closure proves the stated strictness, including cases with the scalar outside factor1. The remaining low-index products have their explicit strict certificates.

In particular `y^2 Z_k` also belongs to the folded cone by multiplication with the known folded-cone factor `y^2`, whose Laurent row is `[3,2,1]` and whose defects are `[4,0,1]`.

## 7. Scope

These are genuinely infinite mixed-ray kernel theorems. They provide the folded-kernel hypotheses for the increment families and their mixed prefixes. They do not by themselves prove that adding `2(x+2)` to `3y^2 Z_k` preserves the cone; that last multiplier claim still requires its quantitative low-index defect margin. They also do not alone establish the full mixed-ray Local TP2 comparison or any full-tree induction.
