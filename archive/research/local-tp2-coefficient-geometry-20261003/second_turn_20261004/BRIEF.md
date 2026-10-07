# Additional-turn research brief — 2026-10-04 JST

Base: private research branch commit 61010cce29d0a82d9ba6db22d8df686fdbe179b7. Public failure ledger read at 6e770f3b3e3f26af5df5308572917559343b68f4. User explicitly requested continuation with multiple GPT-6.1 agents. This is private branch research, not a public campaign-state change or theorem promotion.

Target: strict canonical Local TP2 along L^m R L^ell for every m,ell>=0, keeping the existing all-L^mR^k proof as a dependency. This family is not a claim about arbitrary paths. It is only worth pursuing if an actual coefficient-kernel mechanism closes; positivity of ordinary coefficients alone is insufficient.

Candidate new mechanism: the negative initial coefficient on this additional-turn ray may be absorbed by an exact Chebyshev index shift. Put y=x+1,z=2x+3, T_j=sum_(i=0)^j U_i(z/2), g_j=1+yT_j, T_-1=0. Set P=g_m, X=g_(m+1), tau=3yX-x, c=T_m,d=T_(m+2). With old first-right center C_1=(3yP-x)X-1-xP, the proposed identity is

    (C_1-P)/y = tau*c+d.

Along the ray retaining X, let Q_(-1)=P,Q_0=C_1 and Q_(ell+1)=tau Q_ell-Q_(ell-1)-xX. Then the proposed homogeneous-gap and prefix formulas are

    Q_ell-Q_(ell-1)=y[c U_(ell+1)(tau/2)+d U_ell(tau/2)],
    Q_ell=1+y[c R_(ell+1)(tau)+d R_ell(tau)],

where R_j=sum_(i=0)^j U_i(tau/2). Thus the positive pair (c,d) is the reversed coefficient pair of the already studied first-turn construction at inner index m+1. For ell>=1 the retained endpoint X is the lower-degree endpoint, so the outgoing short gap continues this ray. The ell=0 state is covered by the existing theorem and must not be given the wrong orientation.

These formulas are candidates pending exact verification. Even if they hold, they do not establish folded-kernel membership or Local TP2. Needed next: actual single and midpoint blocks with reversed coefficients, quantitative all-minor compatibility, initial LR comparisons, and final central/proxy estimate.

Do not restart generic all-pair quotient TP2, raw-gap LGV, or larger finite scans as substitutes for this mechanism. Falsification may test proposed sufficient conditions but is not an infinite proof. If a candidate fails, record its exact failure and retain only what is proved. No success from a renamed old obligation.

Files are owned by prefixes: reduction_, kernels_, proxy_, falsification_, audit_. Existing parent files and fulltree_20261004 are read-only dependencies. Python exact integer/Fraction calculations; SymPy is unavailable. Research scripts may reuse parent polynomial tools, but independent checks must disclose and avoid shared load-bearing implementations where practical.
