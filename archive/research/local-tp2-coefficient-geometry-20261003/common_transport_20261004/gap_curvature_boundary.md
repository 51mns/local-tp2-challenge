# Exact Catalan projection of the paired Cassini curvature

Status: the projection formula is proved for every polynomial Cassini triple. The new two-curvature auxiliary invariant has a valid conditional BOTH-child closure proof in `proxy_curvature.md`, independently audited here. A stronger claim that nonnegative curvature produces a nonnegative signed Cassini boundary correction is false on the actual first short child. No child gap or target counterexample is obtained.

## 1. Conditional curvature closure audit

Use D_F=R(1,F), kappa(r,g,s)=D_g²-D_r D_s. The exact same-trace identity

    kappa(g,s,ts-g)-kappa(r,g,s)=D_t R(g,s), s=tg-r,

follows by divided-product differentiation with barred midpoint values. The sibling identity for B=A+TE,

    [D_B²-D_E D_(TB-E)]-[D_A²+D_E D_(TA+E)]
       =D_T[R(E,A)+R(E,B)],

is valid off Fricke and retains both signed seeds.

At an actual regular state, the proved parent P_Q consequences give G<=lrS<=lrD and E<=lrG,S,D. Thus every Bezoutian in the two smaller-endpoint updates and sibling difference has nonnegative characters. The D_t,D_tl,D_T arrays are nonnegative because the actual traces have nonnegative noncentral Fourier coefficients. The short larger-endpoint curvature is a sum of two nonnegative character products, and the long one exceeds it by the nonnegative sibling difference. Therefore the stated pair (kappa_X,kappa_Y)>=char0 does close under BOTH children conditional on P_Q and itself. The root exception and first-level seeds are correctly distinguished. No folded-kernel positivity of an arbitrary mixed sum is assumed in this audit.

This closes an auxiliary obligation only. Its Catalan projection must still be combined with the complete polarized Cassini block to get a gap defect.

## 2. Projection formula, including central and terminal conventions

For r,g,s with one-variable Cassini correction K=g²-rs, the exact polarized identity is

    2T_g-J(r,s)=Sigma_K-L kappa,
    L=(U²-4)(V²-4), Sigma_K=Phi(K(xi)+K(zeta)).         (1)

Let k_j=H(K)_j and define the two even character boundary rows

    b_n=[chi_(2n)(U)chi_0(V)]kappa,
    c_n=[chi_(2n)(U)chi_2(V)]kappa,
    a_n=c_n-3b_n.

All rows are finite and zero extended. Curvature, a difference of products of diagonal D arrays, has matching character parity in U,V. Therefore these are exactly the terms relevant to the Catalan boundary.

Since V²-4=chi_2(V)-3, the trivial-V projection is

    Lambda_V[(V²-4)kappa]=sum_n a_n chi_(2n)(U).

Multiplication by U²-4=chi_2(U)-3 consequently gives the following boundary coefficients for the signed correction -L kappa:

    gamma_0=3a_0-a_1,
    gamma_n=2a_n-a_(n-1)-a_(n+1), n>=1.              (2)

At n=0, chi_2 chi_0 has no trivial character, so the central formula is different from an unmodified second difference. At the top two indices, the same formulas use zero extension; no output boundary is omitted.

For Sigma_K, write the Laurent first-kind polynomials C_j as C_j(U)=chi_j(U)-chi_(j-2)(U) for j>=2 and C_1=chi_1. The exact transformed sum is

    Sigma_K=2k_0+sum_(j>=1)k_j C_j(U)C_j(V).

Only j=2 contributes to the trivial V character. Hence

    Lambda_V Sigma_K=(2k_0+k_2)chi_0(U)-k_2 chi_2(U). (3)

In particular the projected Cassini correction is not generally character-nonnegative even when K has a positive Fourier row. Combining (1)-(3), with j_n the boundary coefficient of J(r,s), gives the exact complete gap-defect equation

    2delta_0(g)=j_0+(2k_0+k_2)+gamma_0,
    2delta_1(g)=j_1-k_2+gamma_1,
    2delta_n(g)=j_n+gamma_n, n>=2.                   (4)

The mixed block and signed curvature must remain together. Dropping either does not follow from curvature positivity.

## 3. Active actual witness against a nonnegative correction gate

Take the first degree-ordered short child of the canonical root. This state satisfies the entire regular P_Q and both nonnegative curvatures. Its smaller-endpoint curvature is exactly

    kappa_X=45+68chi_1(U)chi_1(V)
             +36[chi_2(U)+chi_2(V)]
             +40[chi_3(U)chi_1(V)+chi_1(U)chi_3(V)]
             +56chi_2(U)chi_2(V)
             +16[chi_4(U)+chi_4(V)].

Thus every one of its character coefficients is nonnegative. Nonetheless its two rows and their signed combination are

    b=(45,36,16), c=(36,56,0), a=(-99,-52,-48).

Equation (2) gives

    gamma=(-245,43,-44,48).                          (5)

The negative central and n=2 terms are actual canonical signed cancellations. Direct Clebsch--Gordan multiplication of -L kappa gives the same list; the result is not an artifact of truncating the formula.

At this state K=y², with half-row (3,2,1), so Sigma_K has projected coefficients (7,-1,0,0). The actual mixed block J(r,s) has boundary

    j=(622,470,268,-16).

The complete sum in (4) is

    j+Sigma+gamma=(384,512,224,32),

equal to twice the strictly positive actual gap defects

    delta(G)=(192,256,112,16).

Thus neither the signed curvature term nor the mixed term is separately positive in the full supported range. The witness refutes the proposed auxiliary implication

    P_Q and kappa_X,kappa_Y>=char0  =>  gamma_n>=0 for all n,

on an actual state. It does not refute P_Q child closure, the curvature invariant, the actual gap kernel, or Local TP2.

## 4. Remaining gap connection and reproducer

The closed curvature pair is useful new state information, but an additional inequality coupling j_n and gamma_n in (4) is still needed to prove a previously unknown child gap kernel. Requiring the complete right side of (4) to be nonnegative is equivalent to that kernel gate; it is not promoted here as a new independent invariant. No immediate implication of K_G' from P_Q plus the curvature pair has been proved or disproved.

`gap_curvature_reproducer.py` computes the actual root and first short child directly in sparse integer Laurent arithmetic, independently constructs D and Bezoutian characters from Fourier coefficients, and multiplies characters with an independent Clebsch--Gordan loop. It verifies all regular P_Q gates and both curvature signs before recording the failed correction sign. It imports only the frozen network lane's scalar Laurent arithmetic, not `proxy_curvature_verify.py` or its character code. Output is `gap_curvature_results.json`. This single exact witness and normalization check are not a larger tree scan.

ROOT / BOTH / TARGET status: the curvature pair has an explicit root exception and proved first-level seeds; its BOTH-child sign closure is conditional on P_Q. The nonnegative signed-correction strengthening fails on the first regular short state. The gap-kernel implication of the surviving curvature pair remains OPEN.
