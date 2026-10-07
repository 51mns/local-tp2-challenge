# Exact finite character certificate for every folded relative and mixed minor

Status: proved universal algebra. This replaces the infinite ordered-minor test by a finite character-coefficient test and preserves the midpoint cancellation exactly. It does not prove changed-center packet closure. Positive support, shifted-trace gates, and strict single-block gates of the packet remain separate premises.

## 1. Definitions and the precise coefficient selector

For a real polynomial f let h=H(f), reflected and zero extended, and K_f be its folded multiplication kernel. Put

    T_f=Phi(f(ξ)f(ζ)),
    J(f,g)=Phi(f(ξ)g(ζ)+g(ξ)f(ζ)),
    R(f,g)=Phi((f(ξ)g(ζ)-g(ξ)f(ζ))/(ζ-ξ)),

where Phi(ξ+ζ)=UV and Phi(ξζ)=U²+V²-4. Character coefficients are in chi_a(U)chi_b(V), with chi_a the second-kind Chebyshev character.

For column indices 0<=k<l define the selector

    Sel_(k,l)=[chi_(k+l-1)(U)chi_(l-k-1)(V)].

The established exact character formula gives Sel_(k,l)R(f,g)=H(f)_k H(g)_l-H(f)_l H(g)_k. At k=0 this selects the diagonal character (l-1,l-1), with no factor two. At k>0 the symmetric transpose coefficient is the same.

## 2. Every folded row is a cosine multiplication row

Let C_0(x)=1 and for i>=1 define the first-kind Laurent polynomial by

    C_i(q+q^-1)=q^i+q^-i.

Then at every j>=0,

    H(C_0 f)_j=h_j,
    H(C_i f)_0=2h_i, i>0,
    H(C_i f)_j=h_|i-j|+h_(i+j), i,j>0.

Therefore row i of K_f is exactly H(C_i f). This covers the central column convention and all support boundaries. There is no positivity assumption in this identity.

For every 0<=i<j,

    R(C_0,C_j)=chi_(j-1)(U)chi_(j-1)(V),

and, when i>0,

    R(C_i,C_j)=chi_(i+j-1)(U)chi_(j-i-1)(V)
                +chi_(j-i-1)(U)chi_(i+j-1)(V).       (1)

These follow from their Fourier half-rows, which are the coordinate unit rows at 0 or i respectively, and the established character formula. Thus the multiplier in (1) is character-nonnegative in every case. In particular R(C_0,C_1)=1; R(C_1,C_2)=chi_2(U)+chi_2(V).

## 3. Universal ordered-minor identity and relative equivalence

For row indices i<j and columns k<l,

    det K_f[{i,j},{k,l}]
       =Sel_(k,l) R(fC_i,fC_j)
       =Sel_(k,l)[T_f R(C_i,C_j)].                  (2)

The second equality is the product identity for the ordinary Bezoutian, followed by the algebra homomorphism Phi. It is not a TP2 assumption.

Consequently, for ANY real polynomials f,b and ANY real number gamma,

    det K_f[I,J]>=gamma det K_b[I,J] for ALL ordered I,J
      iff T_f-gamma T_b has nonnegative characters. (3)

Sufficiency: subtract (2) for f and gamma times b. Multiply the character-nonnegative difference by (1). Clebsch--Gordan multiplication has nonnegative integer coefficients, so every selected coefficient is nonnegative.

Necessity: use rows (0,1), for which the multiplier is exactly one. The differences for all column pairs are precisely all character coefficients of T_f-gamma T_b. More explicitly, every nonzero coefficient has equal character parity and is symmetric in U,V, because each T_f=R(f,xf) has the established Fourier-minor expansion. For a>=b>=0 with equal parity, its inverse indices are

    k=(a-b)/2, l=(a+b+2)/2.

They satisfy 0<=k<l; for a=b the index k=0 uses the correctly normalized central row. Coefficients with different parities vanish identically, and the coefficients a<b are the symmetric duplicates. Thus no coefficient is missed.

This theorem requires no positive-interval support or ordinary positivity. All rows are finite polynomials and zero extended. Its application to a packet must still check the packet's support and strictness premises separately. Arbitrarily large folded row or column indices cause no problem: (2) remains exact, and the positivity proof uses their explicit one- or two-character multiplier. No finite band enumeration is part of the proof.

A negative coefficient in the tensor difference immediately yields an exact counterminor using rows (0,1) and the inverse column indices above. Conversely a complete finite character array with no negative entries certifies every ordered folded minor, including those at unbounded kernel indices.

## 4. Mixed-minor equivalence

Define the polarized ordered folded minor

    Mix_(I,J)(f,g)=det K_(f+g)[I,J]-det K_f[I,J]-det K_g[I,J].

It is the sum of the two cross-diagonal products minus the two cross-off-diagonal products. Polarizing (2) gives

    Mix_(I,J)(f,g)=Sel_(k,l)[J(f,g)R(C_i,C_j)].        (4)

Therefore

    Mix_(I,J)(f,g)>=0 for EVERY ordered I,J
       iff J(f,g)>=char0.                            (5)

Again the converse uses rows (0,1). This is an exact two-row compound certificate, not sourcewise positivity of an arbitrary network expansion.

## 5. The sharp midpoint condition is exactly one finite tensor cone

For midpoint seeds (b0,b1) and trace T define

    L_r=b0(T-r)+b1,
    H_rs=b0(T-r)(T-s)+b1(T-(r+s)/2),
    F_rs=L_r(T-s), G_rs=L_s(T-r),
    delta=(r-s)/2.

Then F_rs=H_rs+delta b1 and G_rs=H_rs-delta b1. Thus

    J(F_rs,G_rs)=2[T_Hrs-delta² T_b1].               (6)

By (3)-(5), the following are EXACTLY equivalent at each parameter pair:

1. every mixed folded minor of F_rs,G_rs is nonnegative;
2. every ordered folded minor satisfies det K_Hrs>=delta² det K_b1;
3. the finite tensor B_rs=T_Hrs-delta² T_b1 is character-nonnegative.

The smoothed condition is the same exact equivalence with yF,yG,yH,yb1. It is not inferred from the unsmoothed condition, because y is not a cone multiplier. For the packet's one-sign seed, |b1|=b1 or -b1, so its sign does not change T_b1 or the determinant reference.

This is precisely the parameter-dependent relative bound suggested in the brief, with coefficient (r-s)²/4. The uniform radius-2 condition with coefficient 4 is sufficient but may be stronger. This note does not claim that the sharp condition is preserved by either child. Trace kernels, L/yL strictness, H/yH positive support and folded cones, and the origin register conditions remain as specified in the expanded predicate.

## 6. Exact u,w quadratic and both changed-center substitutions

Let u=(r+s)/2,w=(r-s)²/4. For r,s in [-2,2] the exact domain is

    |u|<=2, 0<=w<=(2-|u|)².

Set A_u=b0(T-u)²+b1(T-u). Then H_rs=A_u-wb0, and (6) becomes the finite quadratic-in-w certificate

    B(u,w)=T_Au-w[J(A_u,b0)+T_b1]+w² T_b0.           (7)

Each character coefficient has degree at most four in u and two in w. The entire all-minor question is therefore a finite array of scalar polynomial inequalities on this explicit domain. This observation is algebraic; no positivity of its individual power or Bernstein coefficients is asserted.

For the unified actual child update from the preceding transport theorem, put

    beta=3y², n_sigma=g+(1-sigma)e,
    u_sigma=T-beta n_sigma,
    v_sigma=c+sigma Te-n_sigma, sigma=0,1,
    T'=T+beta v_sigma,
    c'=(u_sigma+1)v_sigma+(1-2sigma)e, e'=n_sigma.

Apply (7) twice at each child: (T',b0,b1)=(T',c',e') and (T',e',c'). These are the exact forward and reversed new-center mixed certificates, retaining ancestry g and canonical Fricke data. No independent seed rows have been substituted. The algebraic reduction is common to BOTH children; proving these four resulting character arrays nonnegative is still open.

## 7. Additional transport and computational consequences

If (3) holds and p has a folded-TP2 kernel with the requisite positive support, then

    T_(pf)-gamma T_(pb)=T_p(T_f-gamma T_b)>=char0.

Thus all ordered relative minors transport through COMMON multiplication by a cone polynomial, with the reference scaled by the same p. This does not authorize multiplication by y. The analogous mixed statement follows from J(pf,pg)=T_p J(f,g).

The finite character arrays can be computed directly from Fourier rows. For h=H(f), the row of xf is q_n=h_(n-1)+h_(n+1), including q_0=2h_1. For a>=b of equal parity, the tensor coefficient is h_k q_l-h_l q_k with the inverse indices above. Computing all coefficients costs O(d²) after the Fourier transform; no four-index kernel search is needed. The smoothed case is computed independently.

`network_relative_character.py` implements this certificate and exact witness extraction, and verifies the row/minor normalization against direct kernel calculations. `network_relative_character_results.json` records finite identity checks only. The all-index theorem is the proof above. No new path family, target proof, or changed-center closure has been claimed.
