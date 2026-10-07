# Independent adversarial audit: strict Local TP2 on every all-left path

## Verdict and exact scope

**PASS.** The assembled proof in `resumed_comparison_all_left.md` establishes the original strict Local TP2 inequalities at every canonical state on the infinite all-left ray:

`path=L^k`, for every integer `k≥0`.

For the original degree-oriented differences `S=U-C`, `D=V-U`, it proves

`H(S)[n]H(D)[n+1]−H(S)[n+1]H(D)[n]>0`

at every `0≤n≤deg S`.

This is an infinite theorem for actual canonical S,D pairs. It is neither finite-depth evidence nor merely a comparison between auxiliary Chebyshev rows. It does **not** prove Local TP2 for arbitrary mixed left/right paths or the full canonical tree.

No mathematical gap was found in the assembled argument. A terminology clarification identified during review was applied to the source: the kernel is TP2 with strictly positive supported defect differences; finite-band kernels have forced zero minors outside support. All uses of strictness in the proof employ the precise supported statement.

## Independently verified new arithmetic

Two fresh verifiers construct Laurent products directly with `x=q+q^-1`; neither imports the certificate-generating scripts or their Fourier-transform implementations.

* `resumed_audit_yV.py` verifies all **18** new helper defect polynomials and all **496** Bernstein coefficients for the common factor `yV_r`.
* `resumed_audit_actual.py` verifies all **56** actual pair-minor polynomials and **24** quantitative margin polynomials, reconstructing all **4,948** Bernstein coefficients into the power basis exactly.
* The latter verifier independently evolves the **original Markov recurrence directly in Laurent form**, and reconstructs every S, D, H(S), H(D), and F array in `resumed_ray_bases.json`. All **39** minors at the six original base states `k=0,…,5` agree exactly and are positive.
* It also verifies the strengthened quartic arithmetic: `delta_Q(0)≥19633`, `Q(2)≤4489`, and `19633>4·4489`.

Every certificate grid is checked for completeness; all rational Bernstein coefficients are positive and all recorded minima agree. Thus the certificates prove inequalities on complete closed parameter cubes. No root approximation, floating-point sign test, or finite parameter sampling is used in the infinite step.

## Connection to the original canonical recurrence

On this ray the fixed boundary is 1. If `C_k` is the center after k left moves, with `C_-1=x+2`, direct substitution into the original mutation gives

`C_(k+1)=(2x+3)C_k−C_(k-1)−x`.

Writing `u_j=U_j(x+3/2)`, `T_j=sum_(a=0)^j u_a`, and `y=x+1`, the root values and recurrence give

`C_k=1+yT_(k+1)`, `C_(k-1)=1+yT_k`.

Consequently the actual short-child difference is `S=yu_(k+2)`. The actual long-minus-short factorization gives

`D=yT_k B_k`, `B_k=2+2y+3y²T_(k+1)`.

The child degrees are `k+3` and `2k+4`, respectively, so the short/long identification agrees with the original degree convention at every k. No change of the target problem occurs in these identities.

## Common kernels and the parity intermediary

The new theorem that `yV_r`, where `V_r=u_r+u_(r-1)`, is in the strict supported folded cone for every `r≥1` is valid. Its four residue blocks are precisely the previously proved V-root residue types with an extra y factor. For `r≡0 mod 4`, a quartic is available to reserve because r≥4. The other three residue classes use the middle linear, innermost quadratic, or middle-times-quadratic factors. All remaining factors are certified quartics. The positive leading scalar is harmless. The excluded r=0 would give y, which is correctly not included.

Set `m=k+2`, `N=k+1`, `E=yT_N`, and `A=2x+1`.

For even m=2r, the factorizations

`S=(yV_r)W_r`, `E=(yV_r)u_(r-1)`

are exact, with `W_r=u_r-u_(r-1)`. The already audited consecutive-W comparison and the **correct** difference identity

`W_r−W_(r-1)=(2x+1)u_(r-1)`

give `H(W_r)≤lr H(Au_(r-1))` for r≥3. Multiplication by the now-proved common kernel `yV_r` yields `H(S)≤lr H(AE)`.

For odd m=2r+1, the first-kind argument in `resumed_ray_firstkind.md` is also sound. Let `c_j=2T_j^(first)(x+3/2)`. Its paired roots lie in the already certified quadratic parameter range. All indices except j=2 group into existing strict blocks: quartics, a linear factor plus quartics, a certified cubic plus quartics, or—when `j≡2 mod 4` and j≥6—a central singleton with parameter at least 2 plus quartics.

The exceptional `c_2` has defect row `(-3,68,16)` and is not incorrectly declared a cone polynomial. The properly normalized CD identity is

`M_n(c_m,c_(m+1))=2[2·1_(n=0)+sum_(j=1)^m delta_(c_j)(n)]`.

At index zero, the exceptional negative contribution cancels exactly against `2+delta_(c_1)(0)=3` when m=2. The result is zero, not negative. All subsequent contributions are nonnegative. At every positive supported index, the terminal defect of c_n gives a positive summand. Thus the needed **weak** consecutive ordering holds for all indices, including the exceptional pair.

The exact identity

`c_(r+1)−c_r=(2x+1)V_r`

then gives the weak comparison to the positive difference. The identities

`u_(2r+1)=u_r c_(r+1)`, `T_(2r)=u_rV_r`

and the proved common kernel `p_r=yu_r` imply `H(S)≤lr H(AE)` for odd m≥3. Therefore both parity arguments apply throughout the infinite range k≥6. The six remaining k values are covered by direct original-recurrence bases.

## Actual pair comparison on residues

Put `U=u_2=4x²+12x+8`. The exact proxy identity is

`Z=(x+2)B_k=(3/4)UE+K`, `K=2(x+2)²`.

The target new certificates compare **AE with UE** on the actual prefix-family factorization. Write

`T_N=2^d R product Q_i`,

where every `Q_i=16ff'` is a scaled generic quartic, and R is a bounded-degree residue from the previously audited U/V root decompositions. The eight degrees are exactly `(4,5,2,3,4,5,6,3)` in order of N modulo 8. The pulled quartics in classes zero and one are available at all relevant N≥8 and N≥9. The four independent residue parameters and optional fifth parameter correctly cover all actual root choices; allowing a larger independent cube introduces no missing hypothesis.

With `e=yR`, the initial factor is `E_0=2^d e`. Every adjacent pair minor between Ae and Ue, including the terminal lower-support index, is strictly positive by the independently reconstructed certificates. Dense positive support then implies the full ordered-minor comparison needed for Cauchy–Binet.

The low-mode certificates are

`b·2^d M_n(Ae,Ue)−c_n e(2)>0`,

where `c=(80,160/3,40/3)` and b is 4 only in residue classes two and three. The scaling is correct because the pair minor scales by `2^(2d)`, whereas the mass scales by `2^d`. Thus these certificates give the desired initial margins, or one-quarter of them in the two designated classes.

## Quartic propagation and all support indices

For a cone multiplier Q, Cauchy–Binet gives

`M_n(AE_0Q,UE_0Q)≥M_n(AE_0,UE_0) det K_Q[{n,n+1},{n,n+1}]`.

This step is legitimate because the full input MLR comparison has already been proved. The retained principal kernel minor is at least `delta_Q(0)`: the interior formula gives `Delta_0−Delta_(2n+1)` plus a nonnegative term, and `Delta_(2n+1)≤Delta_1`; the n=0 case is equality. The support-boundary formula gives the same inequality.

Since `delta_Q(0)≥4Q(2)`, adjoining a quartic multiplies the ratio of a pair minor to mass by at least 4. In residue classes two and three, at least one unused quartic is available for N≥7: their first applicable indices are N=10 and N=11. Therefore their one-quarter initial margins become the full required margins. Every remaining factor preserves those bounds.

The source's strictness proof also covers all newly created indices. If the current lower degree is a and Q has degree t, take intermediate indices `(i,i+1)`, `i=min(n,a)`, for each `0≤n≤a+t`. The input pair minor is positive. For i=0 the second minor is `delta_Q(n)>0`. For i≥1, its folded interior formula is at least `delta_Q(n-i)>0`, because `0≤n-i≤t`; the boundary formula remains positive. This includes the input terminal index and every new output terminal index. Hence strict comparison between AE and UE is maintained through every quartic multiplication.

There is no inference of strictness merely from a weak TP2 multiplier: the proof explicitly selects a strictly positive term at each index.

## Low-degree term and final chain

The half-row of K is `(12,8,2)`, and `A(2)=5`. Therefore its possibly negative determinant contribution is bounded below by

`M_n(AE,K)≥−5H(K)[n]E(2)`.

For n=0,1,2 these magnitudes are `60E(2)`, `40E(2)`, and `10E(2)`. Multiplying the certified thresholds by 3/4 gives exactly those three values, with strict inequalities. Thus K is absorbed at every affected index. For n≥3, both relevant K coefficients vanish and the determinant remains positive by the AE-to-UE comparison.

This proves `H(AE)<lr H(Z)` on every adjacent index within the AE support. The previously audited comparison `H(x+2)≤lr H(yT_k)`, multiplied by the folded kernel of B_k, gives `H(Z)≤lr H(D)`. Combining it with the parity result yields

`H(S)≤lr H(AE)<lr H(Z)≤lr H(D)`.

At interior S indices, positive support makes ratio transitivity valid and supplies the strict target determinant. At the terminal S index, `H(S)[n+1]=0`, while D has a positive next coefficient, so strictness holds directly. All supports and degree gaps match the original canonical problem.

## Exact bases and final scope

The independent original-Laurent recurrence verifies all 39 entries for k=0,…,5 against the recorded S,D and transformed rows, not merely the verifier's exit status. Together with the uniform proof for every k≥6, this completes the strict Local TP2 theorem on **all** canonical all-left states.

The evidence and proof reviewed here do not include arbitrary mixed paths. The full-tree Local TP2 problem must retain its unproved status unless a separate extension is established.
