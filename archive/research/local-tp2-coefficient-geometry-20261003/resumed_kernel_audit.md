# Independent audit of the first-difference kernel theorem

Audited manuscript: `resumed_kernel_first_difference.md`.

**Verdict:** the stated theorem and its multiplication and tail-sum consequences are valid under the explicit finite, strictly decreasing positive half-row hypothesis. I found no mathematical gap. This is a general auxiliary theorem, not a proof of canonical Local TP2 or of canonical membership in this stronger cone.

## Algebra and all support cases

Write `g_n=h_n-h_(n+1)`, `Delta_n=h_n^2-h_(n-1)h_(n+1)`, `delta_n=Delta_n-Delta_(n+1)`, and `r_n=delta_n/g_n`. Symmetry means `h_(-1)=h_1`, including when computing `Delta_0`.

1. For `0<=n<m`, the top adjacent minor is exactly

   `(delta_n*g_(n+1)-delta_(n+1)*g_n)/h_(n+1)`.

   The division is legitimate. The last top adjacent minor is `h_m^2`; all later top minors vanish. Thus necessity imposes precisely the listed inequalities, without an omitted terminal inequality. For `m=0`, the condition is empty and `J=h_0 I`, as required.

2. For an adjacent minor transposed if necessary so `j>=i`, put `a=j-i`, `b=i+j+1`. The manuscript's direct expansion is correct, including `a=0`. In the interior `b+1<=m`, it gives

   `M=sum_(k=a)^b delta_k [1-h_a*h_(b+1)/(h_k*h_(k+1))]`.

   Every denominator is strictly positive. The bracket decreases with `k`. Its `g`-weighted sum is zero because `g_k/(h_k*h_(k+1))=1/h_(k+1)-1/h_k`. Weighted covariance of two decreasing sequences proves `M>=0` exactly as asserted.

3. At `b=m`, direct expansion gives `M=Delta_a-h_a*h_m`. The facts `r_k>=r_m=h_m` and `Delta_a=sum_(k=a)^m delta_k` prove its nonnegativity. At `b>m`, it gives `M=Delta_a>=0`. For `a>m`, the determinant vanishes; when `a=m+1`, a single entry of the submatrix can still be positive, but the determinant is zero. Thus “the minor vanishes” is correct if “minor” denotes the determinant, as usual.

4. A completely explicit passage to nonadjacent minors is available. For arbitrary rows `i<k` and columns `j<l`, if either off-diagonal entry is zero, nonnegative entries immediately give a nonnegative determinant. Otherwise `|i-l|<=m` and `|k-j|<=m`. Every cell in the entire row-column rectangle then lies in the positive band, so summing its adjacent log-supermodular inequalities gives

   `log J(i,j)+log J(k,l)>=log J(i,l)+log J(k,j)`.

   This proves the desired minor. It avoids needing to state a separate transitivity theorem for likelihood-ratio order with zeros.

## Normalization and consequences

The basis `B_k=sum_(i=-k)^k q^i` has coefficient `1` at zero as well as at its other exponents. Consequently `P=sum_k g_k B_k` and the telescoping identity for the first difference of `B_k P` produces exactly `h_(|n-k|)-h_(n+k+1)`, with no missing factor of two at the center.

It follows that `alpha_(QP)=alpha_Q J_P` and `J_(PQ)=J_P J_Q`. All sums are finite for fixed entries because these matrices have finite bandwidth. Cauchy–Binet therefore proves product TP2 without a convergence issue. If the factor degrees are `p,q`, strict positivity of product first differences at output index `0<=n<=p+q` follows by choosing intermediate index `k=min(n,q)`: its coefficient `alpha_Q(k)` is positive and `|k-n|<=p`, so the selected `J_P(k,n)` is positive. The product remains inside the theorem's stated class.

The tail matrix `T(k,n)=1[n<=k]` is nonnegative TP2. The identity `H(P)=alpha_P T` and Cauchy–Binet validate the sufficient implication from nonnegative first-difference likelihood-ratio order to ordinary half-row likelihood-ratio order. No parity issue or center normalization is missing.

The two stated exclusions are correct: `h=[10,8,3]` has the `J` top-left minor `-5`, and `h=[14,8,3]` has its top-row minor at columns `1,2` equal to `-2`.

## Independent exact finite checks

`resumed_kernel_audit.py` imports no project polynomial routines and uses Python integer arithmetic plus exact rational arithmetic. Its output is `resumed_kernel_audit.json`.

- Exhausted all 2,509 strictly decreasing integer half-rows with 1–6 entries selected from integers 1–12.
- Compared the proposed ratio criterion with every adjacent minor in a finite square of side `2m+3`; all cases agreed.
- Independently checked 9,922 interior covariance identities, 5,632 cases `b=m`, 85,450 cases `b>m`, and 37,764 cases `a>m`.
- For the 99 rows satisfying the criterion, checked every two-row/two-column minor in those squares: 36,161 minors, all nonnegative.
- For 300 pairs sampled from accepted rows, directly convolved the symmetric coefficient sequences, checked strict decrease and the product criterion, and checked 43,200 entries of `J_(PQ)=J_P J_Q`.

All checks passed. The finite computations support the audited general proof; they are not used as a finite-to-infinite argument and establish no new canonical-family induction.

## Addendum: final conditional reduction and strictness

The later sections on `t_X+a` and the full canonical tree were also audited algebraically, without rerunning a corpus.

- The assertion about `J_y`, `y=x+1`, is correct. For a nonnegative tridiagonal matrix, a negative two-by-two minor would require both off-diagonal entries positive. Their band constraints force consecutive rows and the identical consecutive column pair. Here these principal minors are `-1` at indices `(0,1)` and `0` elsewhere. Thus `(0,1)` is the only negative minor, and every Cauchy–Binet expansion with another output column pair has only nonnegative terms.
- All four formulas for `tau_n(H(t_X+a))` are correct, including the correction `+3b_3` at `n=2`. The formulas expressing `b_0,b_1,b_2,c_0,c_1` in the first five entries of `alpha_X` are also correct. For nonconstant `X` with positive integer first differences and `a` in `[-2,2]`, every supported output first difference is positive, so the kernel criterion applies. These scope restrictions should appear explicitly in the standalone conditional iff statement; without a restriction on `a`, its scalar tests need not guarantee nonnegative entries.
- For `a=1`, the definitions of `U,V,W,Z,B` give exactly the two conditions `UW>=V^2` and `VZ>=BW`. The claimed monotonicity of the first scalar condition in `a`, and reverse monotonicity of the second, are correct on the stated interval.
- The displayed counterexample `H(X)=[12,8,3]` does lie in the `J` cone, while `H(t_X)=[84,68,33,9]` has top-left minor `-25`; thus it correctly disproves automatic scalar closure from the weaker listed assumptions.
- The strictness identity

  `F_n=sum_(j>n)[alpha_S(n)alpha_D(j)-alpha_D(n)alpha_S(j)]`

  follows exactly by expanding the two tail sums. Under the stated nonnegativity, pairwise order, and strict support assumptions, the summand at `j=deg D` is positive for every `0<=n<=deg S`; all others are nonnegative. Thus the final conditional theorem establishes strict Local TP2 if its four explicit hypotheses are proved throughout the canonical tree.

No additional mathematical gap was found. The canonical induction and positivity obligations remain unproved exactly as the manuscript states.
