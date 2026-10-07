# Independent audit of the one-turn analytic closure

**Verdict: PASS for the new analytic deductions and the assembled one-turn theorem, using the explicitly identified previously audited foundation lemmas.** The companion finite-single/residue and mass/proxy audits have completed with PASS and were read during finalization. No mathematical correction to Sections 2, 3, or 5 is required. The conclusion is the full family \(L^mR^k\), not the full canonical tree.

This audit inspected `recovery_oneturn_closure.md`, the original normalized-tail and all-minor-strength proofs, the Chebyshev/Jacobi compatibility proof, the exact one-turn reduction, and the mass/proxy theorem. The recovered double-block finite computations were independently audited in `recovery_finite_audit.md`. The finite single-block and residue certificates and the detailed mass/proxy audit were independently replayed by the companion auditors. Their completed reports `recovery_single_audit.md`/`.json` and `recovery_mass_proxy_audit.md`/`.json` were inspected: both report PASS with exact certificate agreement. This report audits how those results discharge the analytic dependencies.

## 1. Prefix inputs and normalized smoothing

The residue-to-prefix strength propagation uses multiplicative strength closure, never arbitrary positive-sum closure. A scaled smoothed residue of base degree d has strength \(2^{d-1}\) and mass at most \(3\,2^d(9/2)^d\). Hence its normalized defect is at least \(1/[6(9/2)^d]\). Grouping the remaining quartics into degree-16 blocks produces the stated factor \(4352^{-r}\), with \(m=d+16r\) and \(d\le18\). The exact inequalities
\[
4352(59/100)^{16}<1,\qquad
6(1/400000000)((9/2)(59/100))^{18}<1
\]
were checked with Python rational arithmetic. The explicit m=1 row supplies the excluded low-prefix case. Thus the new \(\eta(yT_m)\) bound follows from the audited residue data and normalized-block theorem.

## 2. Smoothed shifted-trace strength

Let \(\lambda=2^{m-1}\), \(h=H(y^3T_m)\), and \(a=3-r\in[1,5]\). The row of \(y(t-r)\) is exactly
\[
3h+(a+4,a+2,2,0,\ldots).
\]
All five stated perturbation formulas were independently expanded with an exact symbolic polynomial dictionary in Python; their coefficients agree identically, including reflection at n=0.

The needed row facts follow from the prefix strength theorem: h decreases, its final coefficient is \(2^m=2\lambda\), and all supported entries are at least \(2\lambda\). Writing h as H(yQ) gives \(h_0\le2h_1\) for any Laurent-nonnegative Q.

After subtracting \((3\lambda/2)b_n\), the author's lower bounds use only these inequalities and \(1\le a\le5\). At n=0, use \(h_1\le h_0\), discard the nonnegative h2 term, and minimize the quadratic constant at a=5. At n=1, use \(h_0\le2h_1\), \(h_2\le h_1\), and discard the nonnegative h3 term. At n=2, use \(h_3\le h_2\); at n=3 use \(h_4\le h_3\). This gives exactly the printed lower bounds.

The first two resulting quadratics are increasing for \(\lambda\ge8\), with values 85 and 151 at 8. The other supported-index bounds are strictly positive there. No support-edge term is omitted because missing entries are zero. The m=1,2,3 interval certificates are the separate finite inputs. Therefore (3) is proved for every m>=1 once those inputs pass.

## 3. Infinite single-block and smoothed-midpoint bounds

The degrees and normalized product denominators are consistent. Both single dominant products have bound
\[
E_L=c_0^2\sigma^{2m+1}/[4(m+3)],
\]
and the smoothed double dominant product has bound
\[
E_{yH}=c_0^3\sigma^{3m+1}/[16(m+3)^2].
\]
The corresponding strength products are \(3\,2^{2m-1}\) for each single dominant term and \(9\,2^{3m-2}\) for the smoothed double term.

For a single correction the coefficientwise domination follows from
\[
F\ge(t_0-2)A\ge(t_0-2)B,
\qquad
\frac1{t_0-2}\le\frac3{t_0}\le\epsilon_m,
\]
using \(t_0\ge3\). Multiplication by Laurent-nonnegative y preserves it. The old double-product domination similarly remains valid after multiplication by y. Thus all three corrections obey the same epsilon bound, including outside their smaller support.

The perturbation estimate consumes at most half the dominant defect because \(4\epsilon+2\epsilon^2\le6\epsilon\le E/2\). Since the resulting row is at most twice the dominant row, one quarter of dominant strength remains. This proves the single-block bound (5).

Exact Python rational arithmetic checked at m=391 both \(E_L\ge12\epsilon_m\) and \(E_{yH}\ge12\epsilon_m\), and both displayed consecutive ratios are strictly greater than one. Their nonconstant factors increase, so the assertions propagate to every larger integer. The mass bound
\[
H(yB)_0\le(7^m-1)/2
\]
requires dominant strength at least \(16(7^m-1)\), precisely the printed \(96(7^m-1)/6\). This exact inequality holds at 391, and the stated recurrence propagates it. Therefore the stronger smoothed threshold in (6) is obtained, not merely the unsmoothed threshold.

## 4. Relative minors and reference kernels

The all-minor corollary requires that the reference row be nonnegative and bounded by its central entry; it does not require the reference kernel to be TP2. Both B and yB have this property. In particular, m=1 gives B=1 and H(yB)=(1,1), which satisfies the actual corollary even though y itself is not a folded-cone factor.

Coefficientwise domination of H over B and yH over yB follows from the Laurent-nonnegative shifted factors with constant term greater than one and A>=B. Combining the finite bridge with the infinite tail therefore gives both relative-minor bounds on all ordered kernel minors. No infinite kernel-index enumeration is substituted for the all-minor theorem.

## 5. Jacobi compatibility and small outer indices

For the selected pair F,G, their difference is \((r-s)B\) and their midpoint is \(H_{r,s,(r+s)/2}\). Polarizing a two-by-two determinant gives exactly
\[
\operatorname{mixed}(K_F,K_G)
=2\det K_H-\frac{(r-s)^2}{2}\det K_B.
\]
If the reference determinant is nonpositive, midpoint TP2 suffices. If it is positive, the relative factor 4 and \((r-s)^2\le16\) suffice. The same proof works for yF,yG with reference yB. Thus smoothing is justified at the pair itself, avoiding any assumption that multiplication by y preserves the cone.

For both monic Chebyshev/Jacobi families, the roots are simple and lie in [-2,2], and the last-coordinate spectral residues are positive with sum one. The weighted-sum identity is exact. Each diagonal summand is a strict cone product, using L or yL; each pair has a common omitted-root product of cone factors. Cauchy–Binet preserves the nonnegative mixed minors after common multiplication. The diagonal contributions give strict supported defects because their weights are positive and every summand has the same dense degree support.

This covers N=1 (no off-diagonal pair) and N=2 (empty common product) directly. The N=0 boundary is A or yA. Prefix factorization gives the Z families; the strengthened smoothed resolvent argument already supplies y times each bracket, so multiplying by the outside cone factor proves yZ as well. Alternatively the author's absorption of y into an outside trace factor is valid when that factor is nonconstant, with the stated low cases covered separately. Hence q_k, Z_k, and yZ_k have strict supported defects for every outer index.

## 6. Logical dependency and final scope

There is no circular dependency. The order is:

1. Prefix factorization, residue certificates, sharp trace strength, and normalized blocks.
2. New smoothed trace and single/midpoint tail estimates plus their finite bridges.
3. Relative minor bounds and Jacobi compatibility for all outer indices.
4. The independently audited mass/proxy theorem using these new kernel and strength inputs.
5. The unconditional recurrence reduction and the old boundary-ray theorems.

The final comparison chain has the positive supported intervals required for likelihood-ratio transitivity. JZ has the same degree as the short child S, and the strict middle comparison covers every n through that degree, including the last determinant. The companion mass/proxy and finite-single/residue audits have passed. Consequently the cited foundation lemmas and verified new obligations prove strict original Local TP2 at every L^mR^k with m,k>=0.

This audit does not extend the conclusion to paths with another turn, such as L^mR^kL^ell. It must not be described as a proof of the full-tree conjecture.

## Final dependency and artifact review

The finalized manuscript now explicitly includes the single-correction bound `1/(t0-2)<=3/t0<=epsilon_m`, a reproducible dependency table, and the correct open scope beyond one turn. The referenced `recovery_oneturn_checks.py` and its PASS result artifact are present. The companion audit reports explicitly distinguish finite replays from inherited mathematical lemmas. No unresolved editorial correction remains.

No original foundation file was modified by this audit. The reviewed finalized manuscript SHA-256 is `f2abc526cfbefb0b21e033ef0e117af18ccefc3c417d7ba585a5c77d593da639`.
