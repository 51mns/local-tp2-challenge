# Independent audit: strict Local TP2 on the entire all-right ray

## Verdict and scope

**PASS.** The revised `resumed_extension_right.md`, together with the multiplier theorem in `resumed_extension_right_multiplier.md`, proves the original strict Local TP2 inequalities at every canonical all-right state `R^k`, for every integer `k≥0`.

No mathematical gap remains in the reviewed argument. A hand-arithmetic typo in an unnecessary p_1 row was found during review and removed; the final manuscript uses the correct and simpler p_0 comparison. This audit refers to that corrected manuscript.

The result concerns the actual canonical S,D differences on the whole infinite all-right ray. It does not establish the theorem at mixed left/right paths or on the full tree.

## Independent arithmetic checks

`resumed_audit_right.py` constructs products directly as Laurent polynomials with `x=q+q^-1`. It imports neither the source certificate producer nor its Fourier-transform utilities.

The independent verifier:

* Reconstructs all **9** right-comparison margin polynomials and all **57** rational Bernstein coefficients, including complete basis grids, signs, and exact minima.
* Verifies the fixed Ae/Be pair arrays and all five adjacent minors.
* Verifies both first-sandwich comparisons against P².
* Independently reconstructs the multiplier's root-factor defects, the y²Q initial-block defects, the initial mass margin, the constant-perturbation formulas, and the exceptional k=0 multiplier.
* Evolves five original right states directly in Laurent form, checking the canonical formulas, child degree orientation, and the original root minors `(272,352,160,24)`.

Every check passes. The finite recurrence checks supplement the general identities; they are not the basis of the infinite theorem.

The independently verified Bernstein minima are:

| Certificate | Exact lower bounds |
|---|---|
| Quartic amplification | `884` |
| Initial quartic Q, indices 0–3 | `151266414, 338478852, 290971872, 145555380` |
| Initial linear-in-t G, indices 0–3 | `17268, 358599, 322626, 138210` |

These establish the stated bounds throughout the complete closed parameter rectangles and intervals, not at sampled roots.

## Original recurrence, orientation, and target identities

With `P=x+2`, `y=x+1`, `e=yP`, `t=3x²+8x+6`, and fixed right boundary P, the original recurrence is

`C_(k+1)=tC_k−C_(k-1)−xP`,

with `C_-1=1`, `C_0=1+2e`. The formula `C_k=1+2eT_k` follows from the Chebyshev prefix recurrence `T_(k+1)=tT_k−T_(k-1)+1`. Its constant term balances because `t−xP−2e−1=1`.

For k≥1, the two endpoint degrees are 1 and 2k. The child retaining P has degree `2k+4`; the other has degree `4k+3`, which is larger for every k≥1. Thus the source correctly identifies the short child and derives the original differences

`S_k=2e u_(k+1)`,

`E_k=y(2P T_(k-1)−1)`,

`M_k=2P(1+3y²T_k)`, `D_k=E_kM_k`.

The root has the opposite endpoint orientation and is correctly checked separately. No endpoint-order convention is silently continued through k=0.

## Strict cone factors and the multiplier theorem

For `Q_c=3x²+8x+c`, the exact half-row `(c+6,8,3)` has defects

`c²+15c−74`, `37−3c`, `9`.

These are strictly positive throughout `[4,8]`. Every Chebyshev root factor t−a with a in `[-2,2]` is such a Q_c. This establishes cone membership for the u, V, W, first-kind, and prefix families used in the proof. Their ordinary coefficients and Fourier supports are positive and uninterrupted. Positive leading constants, including the constant first-kind initial value 2, do not change the argument.

The multiplier proof's Cauchy–Binet term at index 1 uses exactly the intermediate columns `(1,2)`. Its second determinant is

`D_Q=(c+9)(c+6)−64=c²+15c−10`,

and `D_Q−Q_c(2)=c²+14c−38≥34`. The independently checked initial block `A=y²Q_c` is strict and satisfies

`3delta_A(1)−A(2)=42c+1257≥1425`.

Thus this strict mass margin propagates through every remaining root factor. Adding the constant in `1+3A` changes only the defects at indices 0 and 1; the displayed corrections are exact, and the index-1 mass margin makes its only negative correction harmless. Multiplying by the strict cone factor P proves the multiplier theorem for k≥1.

The k=0 case is handled after multiplication by P, as required: `1+3y²` alone is not incorrectly asserted to lie in the cone. The recorded row `(32,25,12,3)` for `M_0/2` and defect row `(158,172,60,9)` are correct. Hence the multiplier theorem holds at every k≥0.

## First sandwich and time ordering

For `p_j=e u_j`, bilinearity and the recurrence give exactly

`M_n(p_j,p_(j+1))=M_n(p_j,tp_j)+M_n(p_(j-1),p_j)`.

The first term is nonnegative by the already proved broadening property of the cone polynomial p_j and the nonnegative symmetric Laurent multiplier t. The base p_0≤lr p_1 follows by the same broadening property. Thus the induction establishes time MLR without importing the different coefficient formula from the earlier linear-shift Chebyshev case.

The final manuscript's first-sandwich data are correct:

`H(P²)=(6,4,1)`, `H(E_1)=(7,5,2)`, `H(p_0)=(4,3,1)`.

Their adjacent minors are `(2,3,0)` and `(2,1,0)`, respectively. Time ordering and

`E_k=E_1+2sum_(j=1)^(k-1)p_j`

therefore give P²≤lr E_k. Linearity is applied to a fixed lower row, so no unjustified closure of the cone under sums is used. Multiplication by M_k's folded kernel yields `Z_k=P²M_k≤lr D_k`.

## Both parity comparisons

The same recurrence-and-broadening induction establishes W time ordering here because every W_r is a cone polynomial, including W_1=t−1. Its initial comparison with W_0=1 is valid. The correct subtraction identity is

`W_r−W_(r-1)=(t−2)u_(r-1)`.

The difference is positive, so subtracting the narrower row and multiplying by the cone factor eV_r gives the even-index intermediary.

For first-kind `c_0=2`, `c_1=t`, the base comparison is also immediate, and all c_r lie in the cone in this quadratic-substitution setting. The identity

`c_(r+1)−c_r=(t−2)V_r`

and the standard u/V factorizations give the odd-index intermediary. There is no exceptional first-kind c_2 in this new setting; its roots in t still give strict Q_c factors.

The result is the required weak comparison

`S_k≤lr 2(t−2)eT_k`

for every k≥1. The common multiplier and both lower/intermediary rows have the exact supports stated in the manuscript.

## Root blocks and the quantitative actual comparison

The proposed decomposition of T_k into Q and at most one G is valid. Opposite u roots give quadratic-in-t blocks with s=0. Opposite V roots have magnitudes `0≤a≤b≤2`, hence

`(t−a)(t+b)=t²+(b−a)t−ab`

lies in the certified rectangle `0≤s≤2`, `0≤c≤4`. An odd V factor leaves a negative middle root of magnitude at most 1. If both u and V leave linear factors, their product t(t+b) is itself an allowed Q block. Consequently there is at most one remaining G=t+b.

Each **actual** Q is a product of two strict factors t−a with roots in `[-2,2]`. The larger rectangular certificate domain need not share that exact root bound at unattained parameter points; the source expressly distinguishes these claims. This is sufficient for every propagation step. Every actual G is likewise a strict factor.

The fixed rows

`H(Ae)=(94,79,46,17,3)`,

`H(Be)=(396,339,210,90,24,3)`

have adjacent minors `(582,996,570,138,9)`. Hence the full ordered-minor comparison is established before discarding any Cauchy–Binet summands. Multiplication by an actual initial R and subsequent Q blocks preserves it.

The certified amplification `delta_0(Q)>4Q(2)` and the principal-kernel bound give the claimed mass-margin propagation. If G is present it is chosen as initial R; otherwise one Q is available because k≥1. All remaining factors are Q. Thus the two initial margin families cover every positive k, without an omitted small index.

Strictness at every supported output index follows by retaining the input pair `i=min(n,4)` in multiplication of the fixed Ae/Be pair by T_k. The input pair minor is positive, and the corresponding kernel minor is positive because `0≤n−i≤deg T_k`. The folded interior formula and its boundary version apply exactly as in the previously audited strict propagation lemma. This includes all new terminal indices.

## Remainder absorption and final target

For `K=P³`, the half-row is `(20,15,6,1)`. Since `(Ae)(2)=384`, the negative remainder contribution at n=0,1,2,3 is bounded in magnitude by `384H(K)[n]T_k(2)`. The eight independently reconstructed initial margins and their propagation dominate precisely these bounds. At n≥4 both K coefficients vanish.

Thus `AeT_k<lr BeT_k+K` throughout the lower support. The proxy identity

`Z_k=2(BeT_k+K)`

is exact. Combining the comparisons gives

`S_k≤lr 2AeT_k<lr Z_k≤lr D_k`.

All entries within the relevant supports are positive. Ratio transitivity therefore gives strict interior target minors. The terminal S index is also valid: `deg S=2k+4`, while D has positive coefficient at `2k+5`, since `deg D=4k+3≥2k+5` for k≥1. The root's four original minors are directly positive.

This completes the original strict Local TP2 theorem for every all-right path R^k. It adds a second proven infinite ray to the all-left result; arbitrary mixed paths remain outside the reviewed proof.
