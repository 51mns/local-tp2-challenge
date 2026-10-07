# Additional-turn assembly: L^m R L^ell

Status: **PROVED_INTERNAL**, with the inherited foundations and internal-review limits recorded in RESULT_JA.md and MANIFEST.json. All new proof components passed analytic audit; the complete finite kernel and proxy bridges were reproduced by separate implementations. This is a scoped research result, not a promotion of the arbitrary-path repository claim.

## Statement

For every pair of integers m,ell>=0, at the canonical Farey-tree state reached by the path L^m R L^ell, orient the children U,V by increasing degree, let S=U-C and D=V-U, and write H(P)_n=[q^n]P(q+q^-1). Then

    H(S)_n H(D)_(n+1)-H(S)_(n+1) H(D)_n > 0
    for every integer 0<=n<=deg S.

The degree-terminal index is included. This statement does not quantify over arbitrary paths or arbitrary numbers of consecutive R moves between the two L runs.

## Exact additional-turn representation

Use the notation and uniform identities of reduction_additional_turn.md. Put

    y=x+1, z=2x+3,
    T_j=sum_(i=0)^j U_i(z/2), g_j=1+yT_j,
    c=T_m, d=T_(m+2), X=g_(m+1), tau=3yX-x.

Let N=ell+1 and R_j(tau)=sum_(i=0)^j U_i(tau/2). To avoid the shifted ell indexing of the reduction note, use

    Z_N=c R_N+d R_(N-1),
    q_N=y[c U_N(tau/2)+d U_(N-1)(tau/2)].

The actual center is C=1+yZ_N. For ell>=1, equivalently N>=2, the lower-degree endpoint is X and

    S=q_(N+1), E=1+yZ_(N-1)-X,
    M=2(x+2)+3y^2 Z_N, D=EM.

At ell=0 the lower-degree endpoint differs, and the pre-existing L^mR^k theorem supplies the result. No additional-turn formula for the short child is applied at that boundary.

The key identity absorbs the initially negative recurrence coefficient:

    (C_(L^mR)-g_m)/y = tau T_m+T_(m+2).

It produces the reversed positive coefficient pair (c,d). This reversal still requires a new kernel proof; it does not follow merely from the previous result for (d,c).

## Kernel and initial comparison inputs

The reversed-pair theorem in kernels_theorem.md establishes strict supported folded defects for the actual increments q_N and the prefixes Z_N,yZ_N, for every m>=0,N>=1. Its proof uses single-template and midpoint-template inequalities on the entire continuous parameter boxes, an analytic tail in m, and a Jacobi-resolvent representation uniform in N. It does not extrapolate a finite scan of N.

The scaled relative-minor lemma, independently checked in audit_scaled_relative_minors.md, is used where the earlier unscaled sufficient condition would be too strong. If H is lambda-strong, H_n>=alpha B_n, and lambda*alpha>=8B_0, then every ordered folded minor satisfies det K_H>=4 det K_B. Here alpha=H(tau)_0-2 follows from the actual midpoint summand d(tau-u); the smoothed argument is separately checked.

The uniform initial comparisons in reduction_additional_turn.md use the existing all-L^mR^k theorem and all-left comparisons. They imply, using the newly established actual kernels,

    S <=lr y(tau-2)Z_N,
    X(x+2) <=lr E.

The time-order induction starts at q_1<=lr q_2. It does not assume q_0<=lr q_1, which is false at m=0.

## Final strict comparison

The theorem in proxy_mass_compare.md establishes, for every m>=0,N>=2,

    M is a strict supported folded-cone polynomial,
    y(tau-2)Z_N <lr X(x+2)M

with strict adjacent minors through deg[y(tau-2)Z_N]. It explicitly handles the three small m cases using central mass bounds, paired propagators where needed, and finitely many exact initial N cases. The unbounded remaining range follows from the stated inequalities, not from a scan.

Multiplication by the TP2 kernel of M transports the second initial comparison, giving

    S <=lr y(tau-2)Z_N <lr X(x+2)M <=lr EM=D.

Every row is nonnegative with a dense initial support. Moreover

    deg S=deg[y(tau-2)Z_N]=2m+4+N(m+3),

so the strict middle comparison covers every required index, including the terminal index of S. Transitivity therefore proves the stated strict Local TP2 inequality for ell>=1. The existing one-turn theorem covers ell=0, completing all m,ell>=0.

## Relation to the public failed-route ledger

The public record at 6e770f3b3e3f26af5df5308572917559343b68f4 already contains all-depth ordinary gap positivity and an obstruction to the raw-gap LGV construction. This assembly does not infer Fourier TP2 from that positivity. The substantive extra obligations are the reversed-pair continuous kernel certificates, their analytic tail, and the final strict proxy inequality. The public campaign state and canonical claim level are not changed here.
