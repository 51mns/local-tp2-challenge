# Full-tree external bridge: exact models and remaining obstruction

Status: primary sources checked on 2026-10-03. This note does **not** prove full Local TP2. The useful additions are an exact spectral-source check, a global root exclusion, and a positive path model whose limitation is explicit.

## 1. The mirror factors match exactly, but their positivity is conjectural

Bittmann–Jouteur–Kantarcı Oğuz–Molander–Yıldırım, *A mirror deformation of Markov numbers*, [arXiv:2602.14802v1](https://arxiv.org/html/2602.14802v1), uses exactly

\[
A'=3(x+1)BC-x(B+C)-A,\qquad x=q+q^{-1}.
\]

Theorem 4.4 and Notation 4.5 establish integer polynomial factors
\(G(q+q^{-1})=m(q)m(q^{-1})\). The initial factors are
\(1,1+q,1+2q+2q^2\). Write \(\widetilde b=q^{\deg b}b(q^{-1})\). At a triple with incoming sign \(\epsilon\), Definition 4.1–4.2 gives

\[
m_L=q^{\deg c}\frac{q^\epsilon A+C}{\widetilde b},\qquad
m_R=q^{\deg c}\frac{q^{-\epsilon}B+C}{\widetilde a}.
\]

The left edge retains the sign and the right edge reverses it. This is polynomial divisibility, not a subtraction-free coefficient formula. Global positivity of the factors is **Conjecture 6.2**; §§5.1–5.2 prove it on the Fibonacci and Pell branches. Positivity of the squared Laurent polynomials is separately proved in Theorem 2.2. The paper explicitly distinguishes this deformation from earlier q-Markov deformations.

## 2. A global root exclusion (independent deduction)

**Proposition.** Every canonical polynomial \(G\) satisfies \(G(x)>0\) for \(-2<x<2\). Consequently its mirror factor has no zero on the unit circle except possibly at \(q=-1\); \(q=1\) is excluded by positive evaluation.

**Proof.** Put \(x=2\cos\theta\). The exact factorization gives
\(G(x)=|m(e^{i\theta})|^2\ge0\). Suppose a coordinate of a canonical triple vanishes at a real \(|x|<2\). The Fricke identity then gives

\[
a^2+b^2+xab=(a+xb/2)^2+(1-x^2/4)b^2=0.
\]

Thus all coordinates vanish. Each inverse mutation is the same polynomial map as the forward mutation and preserves the all-zero triple. Following the finite ancestral path back to the root contradicts its coordinate 1. This proves strict positivity. At \(q=1\), the factor evaluates to a positive Markov number. QED.

This is a root-location restriction, not real-rootedness. The root center already has nonreal x-roots. Likewise, spectral factorization yields positive definite Toeplitz Gram matrices, but Local TP2 concerns nonprincipal minors; positive definiteness alone has no such implication.

## 3. Explicit positive Laurent path model from the continuant

Use the exact continued-fraction words recorded in `external_structure.md`. Every letter is \(a_i=\alpha_i x+\beta_i\), with nonnegative integer parameters. The continuant is the tiling sum

\[
K(a_1,\ldots,a_N)=\sum_{\mathcal T}\prod_{i\text{ a monomer of }\mathcal T}a_i,
\]

where \(\mathcal T\) ranges over monomer–domino tilings of the ordered sites; a domino has weight 1. This follows directly from deletion of the last tile, \(K_N=a_NK_{N-1}+K_{N-2}\).

After \(x=q+q^{-1}\), replace a monomer at site i by \(\alpha_i\) copies of each height increment +1 and −1, and \(\beta_i\) copies of increment 0. A domino occupies two sites and changes height by 0. The number of decorated tilings of final height n is exactly \(H(G)_n\). Equivalently it is the path count from (0,0) to (N,n) in this finite layered directed graph. This is an explicit positive coefficient model; no numerical extrapolation enters the identity.

It is **not** an ordered planar network to which coefficientwise LGV positivity can be applied automatically. Opposite height steps between adjacent levels cross without sharing a vertex. Planarizing those crossings introduces additional paths. There is also an algebraic obstruction to a letterwise folded-TP2 argument: the actual seed letter \(2x+2\) has \(h=(2,2)\), and

\[
\Delta_0-\Delta_1=(2^2-2^2)-2^2=-4.
\]

Thus even a valid positive path interpretation of each letter does not supply the required folded kernel property. A successful network proof needs canonical multi-letter cancellation and an exact realization of the differences S and D, neither of which is furnished by this model.

## 4. Why nearby cluster theorems cannot presently close the gap

| Primary source | Exact conclusion relevant here | Applicability limitation |
|---|---|---|
| Chen–Huang–Sun, [arXiv:2408.03792v2](https://arxiv.org/html/2408.03792v2), Definition 2.17, Theorem 6.8 | Type-A F-polynomials satisfy coefficient log-concavity while every exponent other than one is held fixed. The proof uses multiaffinity. | This is not log-concavity after identifying variables, nor Fourier coefficient MLR. It is also an ordinary finite-type statement. |
| Kang–Lee–Lim, [arXiv:2508.04396v2](https://arxiv.org/html/2508.04396v2), Theorem 12 and Conjecture 1 | Surface rank polynomials are unimodal; some single-lamination specializations are unimodal. | Single-lamination log-concavity remains conjectural. The statistic differs from partially occupied weighted pairs and their ± decorations. |
| Banaian–Gyoda, [arXiv:2507.06900v3](https://arxiv.org/abs/2507.06900), Corollary 8.33 | The exact generalized Markov polynomial is a weighted-fence ideal enumerator, at initial cluster variables 1 and parameters equal to x. | The known skein positivity identifies a polynomial expansion, not our two difference rows and their adjacent Fourier minors. See `external_structure.md` for the exact specialization. |

The first limitation is visible without cluster theory. The ideal enumerator of the three-element fence with two minimal elements u,w and common maximum v is

\[
F(u,v,w)=1+u+w+uw+uvw.
\]

It is multiaffine and hence coordinatewise log-concave. Nevertheless
\(F(q,q,q)=1+2q+q^2+q^3\) fails coefficient log-concavity because \(1^2<2\cdot1\). This is a counterexample to the proposed implication, not a claim that this particular specialization is AIMath's deformation.

## 5. Stronger spectral hypotheses: exact failure and a conditional alternative

Ordinary log-concavity of positive spectral factors is insufficient; `continuation_kernel/folded_kernel_theorem.md` contains an exact counterexample with a negative folded minor. Requiring the canonical factors to be Pólya-frequency of order 3 also fails already at the next all-left center:

\[
m_{13}(q)=2+4q+5q^2+2q^3,
\qquad
\det\begin{pmatrix}4&5&2\\2&4&5\\0&2&4\end{pmatrix}=-8.
\]

There is a direct conditional criterion for the symmetric row h. Put
\(\Delta_n=h_n^2-h_{n-1}h_{n+1}\) and let \(D_n\) be the contiguous 3-by-3 Toeplitz determinant centered at n. Direct determinant expansion gives

\[
h_nD_n=\Delta_n^2-\Delta_{n-1}\Delta_{n+1}.
\]

If \(\Delta_n\ge0\) and \(D_n>0\) throughout \(|n|\le d\), where h has positive support \([-d,d]\), then every supported \(\Delta_n\) is positive. Symmetry and the identity at n=0 give \(\Delta_0>\Delta_1\); strict log-concavity of \(\Delta\) then gives \(\Delta_n>\Delta_{n+1}\) throughout the positive support. Hence the folded kernel is TP2 with strictly positive supported defect differences. This is an elementary sufficient condition, not an established invariant of the full canonical tree.

The verifier `fulltree_external_checks.py` reproduces the displayed small obstructions and checks the continuant path model against independent scalar mutations at the root and its two children. It performs no broad tree scan. None of the external sources checked supplies the missing full-tree S,D MLR theorem.

## 6. Why positive two-state transfer is not yet a ferromagnetic MLR proof

The new exact positive model in `fulltree_kernel_positive_transfer.md` gives

\[
\widehat T(q)=W_-q^{-1}+W_0+W_+q,\qquad
W_-=W_+=\begin{pmatrix}3&3\\3&3\end{pmatrix},\quad
W_0=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\]

Although \(\det\widehat T=1\), the decorated local factor is not MTP2 in its internal state and the natural decoration order \(-1<0<1\). Fix the right state to 0. Its table in the left state and decoration is

\[
\begin{pmatrix}3&3&3\\3&4&3\end{pmatrix},
\]

whose adjacent minors are +3 and −3. Reversing the left-state order merely interchanges their signs. Thus the elementary decorated factors do not satisfy the local log-supermodularity hypothesis of a routine FKG/Holley argument.

There is also a distinction at positive real q. Its ordinary two-state Ising representation has coupling

\[
J(q)=\tfrac14\log\frac{9y^2}{9y^2-1},\qquad y=1+q+q^{-1},
\]

and opposite endpoint fields \(\pm\tfrac14\log((3y+1)/(3y-1))\). The formal variable q changes these couplings as well as the fields. Its coefficients therefore do not represent the magnetization distribution of a fixed-coupling two-state Ising model with q serving solely as the external field.

Even true ferromagnetism does not guarantee MLR under path extension for three-state spins. Give spins \(s,t\in\{-1,0,1\}\) equal single-site weights and couple them by \(u^{st}\), with \(u=3/2\). The pair interaction is strictly TP2 because every ordered 2-by-2 cross ratio is \(u^{(s'-s)(t'-t)}>1\). The single-spin half-row is (1,1). The two-spin magnetization half-row, scaled by 6, is (14,12,9). Their central comparison minor is \(12-14=-2\). Moreover this symmetric two-spin coefficient sequence is log-concave, yet its folded defect at n=1 is \(18-81=-63\). Ferromagnetic path extension alone therefore cannot establish the needed conclusion.

The closest exact external total-positivity result checked is Marcin Lis, [*The Planar Ising Model and Total Positivity*](https://doi.org/10.1007/s10955-016-1690-x), Corollary 2.2. It concerns two-point correlations between contiguous, correctly ordered boundary sets of a single planar, zero-field Ising graph. Its indices are boundary vertices, not magnetization coefficients or graph size. No identification of our four coefficient entries with that boundary correlation matrix has been found. A selective canonical path-switching construction could still work, but neither this theorem nor standard correlation monotonicity presently supplies it.
