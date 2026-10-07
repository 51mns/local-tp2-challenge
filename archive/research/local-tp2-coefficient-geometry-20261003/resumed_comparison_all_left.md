# Strict Local TP2 on the entire canonical all-left ray

## Statement and scope

Use the frozen AIMath recurrence at commit `c8e61e0e398f540bc8c5de79663398d689f37473`. For every canonical state obtained by `k>=0` successive left moves from the root, let `S=U-C` and `D=V-U` be the original degree-oriented differences. Then

`H(D)[n+1]H(S)[n]-H(D)[n]H(S)[n+1]>0`

for every `0<=n<=deg S`.

This is an infinite theorem for **all-left paths only**. It does not establish the theorem for arbitrary mixed left/right paths or the entire Farey tree.

The proof uses exact parameter-box certificates, not finite-depth extrapolation. The six small path lengths are checked exactly against the original recurrence; the remaining infinitely many lengths follow uniformly from the factorization and kernel argument below.

## Notation and established ingredients

Write

`y=x+1`, `u_j=U_j(x+3/2)`, `p_j=y u_j`,

`V_j=u_j+u_(j-1)`, `W_j=u_j-u_(j-1)`,

`T_j=sum_(a=0)^j u_a`.

For a polynomial `P`, `H(P)[n]=[q^n]P(q+q^(-1))`, extended symmetrically and by zero outside its support. Define

`M_n(P,Q)=H(Q)[n+1]H(P)[n]-H(Q)[n]H(P)[n+1]`.

Thus `M_n(P,Q)>=0` has the orientation `H(P)<=lr H(Q)`. Full-support nonnegative adjacent minors imply the ordered-minor MLR comparison. We use the folded-kernel theorem and product closure from `continuation_kernel/folded_kernel_theorem.md`.

The exact all-left formulas are

`S=p_(k+2)`,

`D=yT_k B_k`,

`B_k=2+2y+3y²T_(k+1)`.

These formulas follow directly along the fixed boundary `A=1`. Set `C_(-1)=x+2` and let `C_k` be the center at `L^k`. The original recurrence becomes

`C_(k+1)=(2x+3)C_k-C_(k-1)-x`.

The initial values and the Chebyshev recurrence give `C_k=1+yT_(k+1)` and the other boundary `C_(k-1)=1+yT_k`. Thus `C_(k+1)-C_k=y u_(k+2)`. The universal long-minus-short factorization gives

`D=(C_(k-1)-1)(3yC_k-x+1)=yT_k B_k`.

The left child has degree `k+3`, whereas the right child has degree `2k+4`; hence their lower/higher ordering agrees with the original definitions at every `k>=0`.

The earlier audited results establish:

1. `H(x+2)<=lr H(yT_k)` for every `k>=0` (`continuation_ray_external.md`).
2. `B_k` has a TP2 folded multiplication kernel, with strictly positive supported defect differences, for every `k>=0` (`continuation_bracket.md`).
3. The common factors `p_r` and `yV_r` have TP2 folded kernels (`continuation_ray.md`, `resumed_external_yV.md`).
4. The difference-polynomial time ordering and first-kind time ordering give the parity comparisons stated next (`continuation_difference.md`, `resumed_ray_firstkind.md`).

From items 1 and 2, convolution preserves the comparison and gives

`H((x+2)B_k)<=lr H(D)`.

It remains to show the strict proxy comparison `H(S)<lr H((x+2)B_k)`.

## A common intermediary for both parities

Put `m=k+2`, `N=k+1=m-1`,

`E=yT_N`, `A=2x+1`, `U=u_2=4x²+12x+8`.

For even `m=2r`, the exact factorizations are

`S=yV_r W_r`, `E=yV_r u_(r-1)`.

The correct difference identity is

`W_r-W_(r-1)=(2x+1)u_(r-1)`.

The audited W time-ordering theorem therefore gives `H(W_r)<=lr H(Au_(r-1))` for `r>=3`. Apply the TP2 folded multiplier `yV_r` to obtain `H(S)<=lr H(AE)`.

For odd `m=2r+1`, let `c_j=2T_j^(first)(x+3/2)`, distinct from the prefix sums. Then

`u_(2r+1)=u_r c_(r+1)`, `T_(2r)=u_r V_r`,

`c_(r+1)-c_r=(2x+1)V_r`.

The first-kind time-ordering theorem gives `H(c_(r+1))<=lr H(AV_r)`. Applying the TP2 folded multiplier `p_r` gives `H(S)<=lr H(AE)` for `r>=1`.

Consequently the weak comparison

`H(S)<=lr H(AE)`

holds for both parities when `k>=6`. All polynomials here have dense positive Fourier rows, and `deg S=deg(AE)=k+3`.

## The fixed comparison certified on root residues

The proxy is exactly

`Z=(x+2)B_k=(3/4)UE+K`, `K=2(x+2)²`.

The half-row of `K` is `(12,8,2)`. We will prove, for every prefix index `N>=7`,

`M_n(AE,UE)>0` for every `0<=n<=deg(AE)`,

and the stronger three low-mode estimates

`M_0(AE,UE)>80E(2)`,

`M_1(AE,UE)>(160/3)E(2)`,

`M_2(AE,UE)>(40/3)E(2)`.

Here `E(2)` is ordinary evaluation at `x=2`, equal to the total mass of the symmetric Laurent row. These claims concern the actual prefix-family intermediary, not arbitrary cone polynomials.

### Root residues and exact scaling

Use `T_N=u_h V_j`, `h=floor(N/2)`, `j=ceil(N/2)`. The established root pairing expresses

`T_N=2^d R product Q_i`,

where each `Q_i` is a scaled quartic

`Q_i=16 f_(s,c) f_(s',c')`,

with `f_(s,c)=x²+s x+c`, `s=3+u`, `c=5/4+5u/2+v`, `u,v in [0,1]`, and independent primed parameters. Every `Q_i` is strictly in the folded cone. The monic residue `R` is one of the eight bounded-degree parameter families in `continuation_bracket.md`.

The residue degrees for `N mod 8=0,1,...,7` are respectively

`d=(4,5,2,3,4,5,6,3)`.

For residue classes zero and one, a quartic has already been pulled into `R`. This is available for the relevant indices `N>=8` or `N>=9`. Put `e=yR`; the actually scaled initial factor in `E` is `E_0=2^d e`.

The script `resumed_comparison_margin.py` forms the exact Fourier rows of `Ae` and `Ue` and verifies a positive Bernstein-basis certificate for every adjacent minor throughout the lower support, including its terminal index `d+2`. It additionally certifies

`b*2^d M_n(Ae,Ue)-c_n e(2)>0`, `n=0,1,2`,

where `c=(80,160/3,40/3)` and the boost `b` is `4` for residue classes two and three, and `1` otherwise. Every coefficient is an exact rational number. The full power-basis and Bernstein-basis arrays are recorded in `resumed_comparison_margin_certificates.json`. A positive Bernstein certificate proves the inequality on the entire real parameter cube.

The scaling is essential: `M_n(AE_0,UE_0)=2^(2d)M_n(Ae,Ue)`, whereas `E_0(2)=2^d e(2)`. Dividing the desired actual margin by `2^d` gives exactly the polynomial certified above.

### Quartic propagation, including strictness

For every generic monic quartic root block, the existing exact certificate gives `delta(0)>=19633/256`. Thus each scaled `Q=16ff'` satisfies

`delta_Q(0)>=19633`.

Also `f(2)<=67/4`, so `Q(2)<=4489`. Therefore

`delta_Q(0)>=4Q(2)`.

If the full MLR comparison `H(AE_0)<=lr H(UE_0)` holds, Cauchy–Binet and TP2 of `K_Q` allow all summands but one to be discarded:

`M_n(AE_0Q,UE_0Q)>=M_n(AE_0,UE_0) det K_Q[{n,n+1},{n,n+1}]`.

The principal folded-kernel minor is at least `delta_Q(0)`. This follows from the folded-minor formula and monotonicity of the folded defect ratios; a detailed proof is in `resumed_external_yV.md`. Thus every retained low-mode ratio `M_n/E(2)` grows by a factor at least four upon adjoining a quartic. The certificates with boost four in classes two and three are therefore sufficient after adjoining one quartic. Such a quartic always exists for those classes when `N>=7`: their first relevant indices are `N=10` and `N=11`. All remaining factors preserve the already-achieved margins.

For strictness at all higher indices, suppose the current lower polynomial `AE_0` has degree `a` and `Q` has degree `t`. For an output index `0<=n<=a+t`, retain the input pair `(i,i+1)` with `i=min(n,a)`. The certified current pair minor is positive. The corresponding adjacent folded-kernel minor is positive because `0<=n-i<=t` and `Q` has strict supported defects. Explicitly, for `i=0` it is `delta_Q(n)`; for `i>=1` the interior formula contains `Delta_(n-i)-Delta_(n+i+1)` and a nonnegative additional term, so it is at least `delta_Q(n-i)>0`, with the same conclusion at support boundaries. This proves strict adjacent comparison throughout the expanded support after every quartic multiplication.

The three mass margins and the full strict comparison are now proved for every `N>=7`.

## The additive low-degree term is dominated

Since `A(2)=5`, each individual coefficient of `AE` is at most `5E(2)`. For `n=0,1,2`,

`M_n(AE,K)>=-H(K)[n]*5E(2)`.

The three upper bounds on the negative contribution are respectively `60E(2)`, `40E(2)`, and `10E(2)`. Therefore

`M_n(AE,Z)=(3/4)M_n(AE,UE)+M_n(AE,K)>0`

at those indices, by the three certified thresholds. At `n>=3`, both relevant coefficients of `K` vanish, so the same determinant is simply `(3/4)M_n(AE,UE)>0` throughout the lower support.

Hence, for every `k>=6`,

`H(S)<=lr H(AE)<lr H(Z)<=lr H(D)`.

For interior supported indices, strictness of the resulting `S,D` comparison follows immediately by multiplying the positive row entries and comparing consecutive ratios. At the terminal index `deg S=deg(AE)`, `Z` has a positive next coefficient because `deg Z=deg S+1`; `D` does also. The terminal desired determinant is therefore positive as well.

## Exact small cases and conclusion

The script `resumed_ray_bases.py` checks path lengths `k=0,...,5` directly from the frozen original left/right mutation recurrence, with two exact constructions of the Fourier map. The companion `resumed_ray_bases.json` records all 39 original Local TP2 minors; every one is a positive integer. For example the root row is `(272,352,160,24)` and the next left state gives `(70840,132944,74520,19024,1632)`.

These six exact cases, together with the uniform argument for every `k>=6`, prove strict Local TP2 on the complete infinite all-left ray. Nothing in this proof asserts Local TP2 for canonical states whose paths include a right turn.
