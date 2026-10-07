# Frozen bivariate curvature pair and BOTH-child conditional closure

Status: universal identities and the conditional sign theorem are proved;
the complete first-level seed arrays pass exact verification. Root and
the gate-audit lane independently checked the analytic identities and
sign proof. This is a new auxiliary closure obligation, conditional on
the parent regular P_Q predicate. No proxy, gap-kernel, or full-tree
target consequence is claimed.

Write R(A,B) for the two-character image of the ordinary Bezoutian,
D_A=R(1,A), and define

    kappa(r,g,s)=D_g²-D_r D_s.

Character multiplication is the positive Clebsch-Gordan product. If a
polynomial A has nonnegative noncentral Fourier coefficients, then
D_A=sum_(j>=1)H(A)_j chi_(j-1)(U)chi_(j-1)(V) is character-nonnegative.
The signed r coordinate in kappa is retained exactly.

For actual parent gaps E,G,R,S,D and Fout=S+D, set

    kappa_X=kappa(R,G,S),
    kappa_Y=kappa(R-E,G+E,Fout).

The two consecutive-gap relations are

    S=tG-R,
    Fout=tl(G+E)-(R-E), tl=3yY-x=t+3yE.

## Exact transport lemma

For arbitrary polynomials r,g,t, put s=tg-r and u=ts-g. Then

    kappa(g,s,u)-kappa(r,g,s)=D_t R(g,s).                 (1)

Proof before Phi: for arguments xi,zeta let D be divided difference,
and bar F=(F(xi)+F(zeta))/2. Product differentiation gives
D_s=bar t D_g+bar g D_t-D_r and
D_u=bar t D_s+bar s D_t-D_g. Subtracting the two curvatures leaves
D_t(bar g D_s-bar s D_g)=D_t B(g,s). Phi is an algebra
homomorphism, so (1) follows. This is an all-degree identity.

It gives the smaller-endpoint curvature at both children:

    kappa_X(short)=kappa_X+D_t R(G,S),
    kappa_X(long)=kappa_Y+D_tl R(G+E,Fout).               (2)

## Exact sibling lemma

For arbitrary E,A,T put B=A+TE and

    kappa_A=D_A²+D_E D_(TA+E),
    kappa_B=D_B²-D_E D_(TB-E).

Then

    kappa_B-kappa_A=D_T[R(E,A)+R(E,B)].                  (3)

To prove it, expand kappa_B-kappa_A using
D_B-D_A=bar T D_E+bar E D_T and
D_(TB-E)=bar T D_B+bar B D_T-D_E,
D_(TA+E)=bar T D_A+bar A D_T+D_E. The difference is
D_T[bar E(D_A+D_B)-D_E(bar A+bar B)], which is (3).
No Fricke assumption or positive-mixture closure is needed for this identity.

For the actual paired packets A=ycA=E+G+S and
B=ycB=G+S+D, their proved sibling relation is B=A+TE,
where T=M-1=3yC-x. The larger-endpoint curvature at the short child
is kappa_A, because its previous fixed-C seed is -E. At the long child
it is kappa_B, because its previous fixed-C seed is +E.

## Conditional BOTH-child sign theorem

Assume the parent regular P_Q predicate and the auxiliary invariant

    kappa_X>=char0, kappa_Y>=char0.                      (4)

The already proved regular reduction gives G<=lrS and S<lrD.
Together with E<=lrG, this gives E<=lrG,S,D. Therefore
G+E<=lrFout, E<=lrA, E<=lrB. All rows have their actual
dense positive interval supports, so adjacent LR transitivity supplies
all-pairs LR and hence character positivity of these R polynomials.

The canonical traces t,tl,T have nonnegative ordinary coefficients,
so their D polynomials are character-nonnegative. Equation (2) proves
both child kappa_X arrays nonnegative.

At the short child, kappa_A is nonnegative directly: D_A,D_E,
D_(TA+E) are character-nonnegative, so both products in its defining
formula are nonnegative. This uses the actual negative previous seed,
not an assumption that all seeds are positive.

Equation (3) and E<=lrA,B then give kappa_B>=kappa_A>=char0.
Thus both child kappa_Y arrays are also nonnegative. The finite
two-curvature invariant (4) is consequently preserved under BOTH
degree-oriented child maps, conditional only on parent P_Q and (4).

## Root status and remaining connection

The original root is an exception to P_Q. Its kappa_X is

    -3+4chi_1(U)chi_1(V)+4chi_2(U)+4chi_2(V),

so (4) cannot be imposed on that root. Its kappa_Y equals D_(G+E)²,
because R=E, and is character-nonnegative. At the root short edge,
D_t=2 and R(G,S) has central coefficient24, so (2) cancels the
negative central coefficient, giving 45. The first long edge is seeded
by the root kappa_Y and the exact positive root R(G+E,Fout).
The complete first-child arrays are saved in `proxy_curvature_results.json`.
Their central pairs (kappa_X,kappa_Y) are (45,8595) for the short child
and (2208,9307) for the long child, and every coefficient is nonnegative.
These are finite seeds, not evidence for the conditional all-degree
sign proof. `proxy_curvature_verify.py` separately verifies the two
universal algebraic identities using six formal evaluation variables.

To connect (4) to a child proxy or to a child folded cone, a further
lemma is required. In particular, polarized Cassini yields

    2T_G-J(R,S)=Sigma_K-(U²-4)(V²-4)kappa_X,

where K=G²-RS and Sigma_K=Phi(K(xi)+K(zeta)). The prefactor
has signed character coefficients. Positive curvature therefore
cannot simply be read as folded-cone positivity. This connection and
strict proxy preservation remain OPEN.
