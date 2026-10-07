# Independent audit: all LR²L^ell original Local TP2

## Verdict and scope

**PASS for the stated infinite family `LR²L^ell`, every integer ell>=0**, conditional only on the explicitly cited, previously established folded-kernel criterion, all-minor strength theorem, product/Cauchy–Binet lemmas and elementary Jacobi resolvent facts. No gap was found in the new proof assembly. This does not verify Local TP2 for arbitrary words or promote the canonical repository claim.

This is a **shared-session independent audit, not blind external review**. The auditor read the proposed theorem and its constants. The author implementation and expected JSON were not imported. The independent verifier starts from the original canonical root and performs L,R,R with its own Laurent/integer polynomial arithmetic. It computes all needed tensor Bernstein coefficients in degree at most two per variable. The parameter orientation is r=2-4u, opposite to the author's r=-2+4u, so the arrays are independently reversed, with identical minima and the same exact sign statements.

Files in this audit lane:

- `audit_lrr_independent.py`: standalone standard-library verifier, with no author code or previous-research imports.
- `lrr_independent_results.json`: every independently computed parameter array used in this audit, all fixed rows/minors and exact scalar residuals.

The inspected authored proof was `/workspace/scratch/c5e089f1e02b/hour_quantum/lrrl_theorem.md`. No file in that author's directory was modified.

## 1. Canonical identity and support checks

Independent original mutations reproduce the displayed X,Y,C_0,t,T,A,B exactly. The recurrence anchors

- C_1=t C_0-Y-xX,
- C_1-C_0=y(At+B),
- y(A+B)=(t-2)Y-xX

hold as integer polynomial identities. They establish the all-N Chebyshev recurrence and center-prefix formula with two initial conditions; the formula is not inferred from an outer-depth scan.

The degree formulas are correct. For ell>=1 the endpoints have degrees 6 and 7ell+2, so the retained endpoint X is the lower-degree endpoint. The actual original gap is q_(ell+1), with degree 7ell+16. The other target row D has degree 14ell+12, which is larger by 7ell-4>=3.

All required ordinary coefficient supports are dense and positive. In particular t-r has constant coefficient at least 580 for every r in [-2,2]. A,B are positive; H_(r,s,c)-B is positive because its second summand can be written B(t-c-1), whose constant coefficient is at least 579. The Chebyshev factors are products of t-r at real roots in [-2,2], so the same positivity persists for every length.

## 2. Independent continuous-parameter certification

Every Bernstein coefficient needed for the raw and smoothed trace and single blocks, the strength-128 midpoint block, and the direct low-index q_2 exception was reconstructed. The independent minima exactly match the theorem:

| Object | Independent minimum |
|---|---:|
| delta(A) | 20736 |
| delta(B) | 16 |
| delta(yA) | 20736 |
| delta(t-r) | 5184 |
| delta(y(t-r)) | 5184 |
| delta(L_r) | 107495424 |
| delta(yL_r) | 107495424 |
| delta(H)-128H_n | 557160726528 |
| delta(y[A(t²-1)+Bt]) | 557256278016 |

The entire parameter cube is covered by the fixed degree-two tensor Bernstein conversion; no parameter sampling is used. Reference B has row (16,12,4), is a folded-cone row, and 128=8B_0. Hence the stated all-minor relative bound follows from the cited theorem, with both its coefficient domination and reference hypotheses met.

## 3. Compatibility, smoothing and the number of residues

The exact mixed-minor polarization has the correct sign and factor:

`mixed(F,G)=2 det K_H - (r-s)^2 det K_B/2`.

Since |r-s|<=4, strength-128 and reference domination supply the factor-4 relative bound needed for every ordered kernel minor. Positive sum closure is not being assumed; it is established for these particular summands by their pairwise mixed-minor inequality.

The extra y is handled correctly. For q_k with k>=3 a pair of resolvent summands has at least one common propagator, and y(t-r) is independently certified. The q_0,q_1,q_2 cases are handled separately by yA, yL_0, and the displayed direct q_2 polynomial. Thus there is no missing two-residue smoothing case. For yZ_k, the prefix outside factors supply a propagator for every k>=2; k=0,1 are again explicit bases.

The prefix factorization is correct:

`T_(2h)=u_h v_h`, `T_(2h+1)=u_h v_(h+1)`.

For even k the active resolvent denominator is u_h and for odd k it is v_(h+1). Each has simple real spectrum in [-2,2], positive endpoint spectral weights summing to one, and at most k active poles. Restoring the outside factors gives **exactly k-1 propagators** per summand. There is no loss of a factor or uncounted residue. The factors have no common root: the Chebyshev three-term recurrence and the definitions of v give this directly.

The resulting squared-weight estimate is correctly retained:

`sum_i lambda_i^2 >=1/|I| >=1/k`.

The proof does not replace it by an unjustified constant-one lower bound.

## 4. Low-index quantitative propagation

The independent trace mass certificate for

`delta_0(t-r)-435(t(2)-r)`

is `(163250,503202,843170)` in the auditor's parameter orientation, all positive. The exact masses and mass upper bound in the theorem are reproduced.

The summand-to-total mass lower bound is valid: each ratio lies strictly between A(2) and 2A(2), and the total ratio is their positive weighted average. Thus Z_i(2)>Z_k(2)/2.

For the nonprincipal template minor, the Cauchy–Binet selection is correct. After the template minor with rows (a,a+1) and columns (n,n+1), retaining (n,n+1) through every propagator yields a principal propagator minor, bounded below by its central defect. Both diagonals are supported in every finite template certificate. All omitted terms are nonnegative. Combining this with squared weights gives precisely alpha*435^(k-1)/(2k), and 435^(k-1)>=k for all k>=1.

The same argument for y²L_r is valid because y² is a common folded-cone multiplier. It does not assume that y itself preserves the cone.

All eleven alpha-template continuum margins and all five beta-template continuum margins are independently nonnegative. Their resulting proxy and multiplier residuals agree exactly with the theorem, including the two proxy indices beyond deg f.

## 5. Actual multiplier and final proxy

The multiplier base has half-row (64,50,24,6) and defects (632,688,240,36), independently reproduced. The sign and factor in

`delta_n(M_k)>=9delta_n(y²Z_k)-27 Z_k(2)(m_(n-1)+3m_(n+1))+delta_n(M_0)`

are correct, including reflected index n=0. The three negative mixed terms have precisely the summed mass coefficient shown. For n>=5 the correction is zero. The five beta residuals are strictly positive, so the whole multiplier has strict supported defects.

The fixed f,g adjacent minors, correction row H(K), f(2), and every alpha residual were reproduced. The proxy uses i_n=min(n,8); for n=9,10 the nonprincipal template certificate supplies the missing comparisons, rather than silently applying a principal-minor bound. For n>=11 the correction vanishes, and the retained (8,9) base minor has supported kernel diagonals throughout the remaining output range, including the last index.

The kernel y²Z_k is strict on its entire support. The selected intermediate pairs in the authored proof have positive y² minors and supported positive Z_k minors; the two terminal positions are covered explicitly. No strictness is lost at the boundary.

## 6. Original Local TP2, not just an auxiliary kernel assertion

The four fixed initial comparisons were independently recomputed. The recurrence propagates time order from q_0<=q_1 using the proved kernels. Fixed-lower-row addition gives Pi<=E_k. The exact identity

`q_(k+1)=fZ_k+q_k+y(A+B)`

and fixed-upper-row comparison give S_k<=fZ_k. The strict proxy and actual multiplier complete

`S_k<=fZ_k<Pi M_k<=E_k M_k=D_k`.

Ratio transitivity applies on every interior index because all rows have dense positive support. The terminal original target is checked directly by the zero next coefficient of S_k and positive next coefficient of D_k.

The ell=0 orientation is correctly separated: the actual right child has degree12, the left child degree16. Independently reconstructed original target minors are all positive, with minimum **15896632320**, matching the authored base. This provides the finite initial case without using the wrong endpoint ordering of the new ray formula.

## Final audited conclusion

The proof establishes the original strict Local TP2 inequality on all `LR²L^ell`, ell>=0, with the stated previously established general dependencies. The new finite continuum certificates, spectral residue/mass argument, nonconstant multiplier correction and strict proxy assembly are valid. This is an internally audited additional infinite family, not a proof of arbitrary-tree Local TP2, an external peer review, a formal proof-assistant check, or a canonical status promotion.
