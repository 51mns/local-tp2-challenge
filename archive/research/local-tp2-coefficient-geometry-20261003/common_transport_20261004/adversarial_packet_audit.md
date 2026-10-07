# Independent audit: origin subsystem, MP_2 reduction, and optional 5/2 blocks

**Verdict: PASS for the conditional subsystem and the stated two-component
reduction. No complete common closure or full-tree Local TP2 theorem.**
Audited `packet_transport.md` and `packet_expanded_predicate.md` directly,
using the read-only normalized recurrence, prior positive paired packet
root certificates, folded product/strength foundations, and the proved
P_Q target/LR reduction. The new formal checker independently verifies
12 identities in Z[x,a,e,r], with no Fricke assumption or earlier code
imports. It also replays the given abstract independent-u obstruction.

The effective main predicate may use midpoint MP_2 everywhere. The
optional MP_(5/2) block theorem is separate and is not needed for actual
gap-register closure. Editorial distinctions about root-child proxy and
the older three-gate ledger are specified below; no new scan was used.

## 1. Previous and current register identities are correctly paired

For fixed endpoint F and trace tau_F=3yF-x, the origin sequence is

    f_j=b0 U_j(tau_F/2)+b1 U_(j-1)(tau_F/2), U_-1=0.

It satisfies f_(j+1)=tau_F f_j-f_(j-1). The current smaller register
requires N_X>=2 and BOTH f_(N_X-1)=g, f_NX=s. The larger register
requires N_Y>=1 and BOTH f_(N_Y-1)=e+g, f_NY=s+d.
These are quotient identities: the corresponding actual gaps are y
times these polynomials. One outgoing identity alone would not fix the
recurrence boundary; the two-identity condition is necessary.

The index N_X>=2 is also necessary to obtain CURRENT G=yf_(N_X-1)
from a run theorem valid only at indices j>=1. No cone is silently
asserted for a reversed seed at index0.

Let T=M-1,c=c_A=e+g+s,tau=t+3y²e. The independent formal checks give:

| Child | Retained new smaller register | New larger register |
|---|---|---|
| short | old X, N_X+1; previous s, current ts-g | (T,c,e), N=1; previous c, current Tc+e |
| long | old Y, N_Y+1; previous s+d, current tau(s+d)-(e+g) | (T,e,c), N=2; previous Te+c, current e(T²-1)+Tc |

At the short child its actual quotient pair is g'=s,s'=ts-g, and
e'+g'=e+g+s=c. At the long child g'=s+d,s'=tau(s+d)-(e+g), and
e'+g'=g+s+d=Te+c. The new larger current terms equal s'+d' in each
case. All identities hold off Fricke as polynomial identities.

The new smaller indices satisfy N_X+1>=3 or N_Y+1>=2; the new larger
indices1 and2 meet their N_Y>=1 restriction. The new origins are
certified by the PARENT's two current paired packets. Retained origins
keep their original trace/seeds and certificate. Thus all register
identities and certificate components really do close under BOTH moves,
conditional on the stated current paired inputs.

This proves both parent outgoing kernels and both child CURRENT G'
kernels, plus their outgoing kernel certificates. It does not prove
that either child has its own newly centered paired packet.

## 2. Midpoint MP_2 is sufficient; the independent-u condition can be removed

For origin seeds (b0,b1), set L_r=b0(T-r)+b1 and

    H_rs=b0(T-r)(T-s)+b1(T-(r+s)/2).

Define F=L_r(T-s),G=L_s(T-r). Then F-G=(r-s)b1 and H=(F+G)/2.
At every ordered folded minor, exact quadratic polarization gives

    mixed(F,G)=2 det K_H-(r-s)² det K_|b1|/2.

For r,s in [-R,R], the direct bound det K_H>=R² det K_|b1|
makes this nonnegative if the reference minor is positive. If it is
nonpositive, folded TP2 of H is sufficient. The same derivation uses
yH and y|b1| explicitly, so it does not require multiplication by y
to preserve folded TP2.

The ordinary U_N path Jacobi spectrum lies in [-2,2]. Its first-coordinate
spectral residues are positive and sum to1. The resolvent expansion of
b0 U_N+b1 U_(N-1) therefore has origin L blocks on diagonals and only
the displayed midpoint-compatible pairs on mixed terms. This uses no
independent parameter u. Folded product closure and Cauchy--Binet give
strict supported defects for every N>=1 in both modes. The strict seed
degree condition deg b1<deg b0+deg T gives equal degrees for all summands,
so diagonal strictness also covers the terminal index. Zero is covered
by the folded kernel theorem with reflection, not a separate guess.

Thus midpoint MP_2 is enough for every current paired input and every
ordinary origin certificate. The older independent-u packets are stronger
than necessary. Their established roots imply the required MP_2 roots.

## 3. CURRENT G/M and the exact two remaining analytic components

For a regular expanded state, CURRENT G follows from its smaller origin
at index N_X-1>=1. CURRENT M is the paired packet's shifted trace at
parameter -1: T-(-1)=T+1=M. No generic product or positive-sum theorem
has been introduced to obtain either gate.

Therefore the four LR companions, current paired MP_2 in both seed
orientations, two certified registers, and strict proxy imply the old
P_Q. Its established target implication includes the terminal support,
and its established transport proves all four LR companions at BOTH
children. The register subsystem also closes at BOTH children as above.
The two remaining regular-child components are precisely:

1. BOTH orientations of the new current-center paired MP_2;
2. the child's strict proxy W_n(Q',Pi')>0 on its entire required support.

Child K_M is supplied when its new paired packet is proved. It is not a
third independent obligation in this strengthened predicate. Conversely
the original parent P_Q alone has not been proved to preserve child M.
The transport note's older three-gate ledger is superseded only in the
explicit expanded formulation, not for the original predicate.

## 4. Root and first-level exceptions must remain explicit

At the canonical root the smaller origin is the established pure sequence
U_j(z/2), N_X=2: g=U_1=z,s=U_2. It is retained on the endpoint1 boundary
and dropped when that endpoint is lost; a new endpoint is never1.
The larger root origin is (tau_Y,b0,b1)=(3x²+8x+6,2(x+2),0),N_Y=1:
f_0=e+g and f_1=s+d. Its MP_2 follows from strict factor products and
zero reference. For example the worst shifted trace at parameter2 has
row(10,8,3) and strictly positive defects(2,25,9); b0 and yb0 are also
strict positive-support cone factors.

This Y-origin is a real exception to an enlarged-origin requirement:
at parameter5/2 its trace row is(19/2,8,3) and delta0=-37/4. Therefore
it must not be justified by the optional MP_(5/2) theorem. MP_2 already
certifies all its actual U_N run gaps.

The augmented root clause is needed because E<=G and R<=G fail centrally
there. Its target is established directly. Both first children already
have the earlier complete P_Q proof, which includes their strict proxies.
The new origin-register components follow from root paired transport.
Thus **only the new child paired MP_2 is still open on the two root
edges**, not their strict proxy. For arbitrary regular edges the two
components packet/proxy both remain open. Existing first-level P_Q must
not be promoted to a first-level new-center packet theorem.

## 5. The optional MP_(5/2) fixed-trace block theorem is valid

The definition q_-1=-b1 is required and is now explicit. For N>=0,

    L_N=q_N(T-r)-q_(N-1),
    H_N=q_N(T-r)(T-s)-q_(N-1)(T-(r+s)/2).

The Robin path characteristic polynomial p_j=U_j-rU_(j-1) gives
L_N=b0 p_(N+1)+b1 p_N, with p_N the first-vertex principal minor.
The fork with N stem vertices and two leaves has characteristic
chi_N=U_N(T-r)(T-s)-U_(N-1)(T-(r+s)/2). Its leaf edge squares are1/2;
the exact N=1 determinant is T(T-r)(T-s)-T+(r+s)/2. Removing the first
stem yields chi_(N-1), hence H_N=b0 chi_N+b1 chi_(N-1).

For r,s in [-2,2], use R=5/2. Leaf pivots R-r,R-s are at least1/2,
and their Schur complement is at least1/2. Every subsequent pivot
R-1/p remains at least1/2 when p>=1/2. The Robin endpoint has the
same pivot bound. Therefore RI-J is positive definite at every finite
length; bipartite signs give RI+J positive definite too. All eigenvalues
are strictly inside(-5/2,5/2).

Their first-coordinate residues are nonnegative and sum to1. Zero
residues merely retain a common shifted-trace factor; repeated eigenvalues
can be handled by assigning the total residue to one copy. The same
midpoint polarization and origin packet factors then prove the L_N/H_N
kernel assertions in both modes. All needed shifted traces stay inside
the origin parameter box. Strict origin degree prevents leading
cancellation; positive diagonal terms cover every supported index.

For N=0, L is strict by hypothesis. Although origin H was required only
weak TP2, F=L_r(T-s) and G=L_s(T-r) are strict same-degree products and
have nonnegative mixed minors; H=(F+G)/2 is consequently strict. This
completes the stated N=0 strictness without strengthening the packet.

This is a conditional theorem about advanced block KERNELS for parameters
[-2,2]. It does not prove the advanced packet's direct relative bounds
against |q_(N-1)|, nor preserve the whole5/2 parameter box. Even a
two-vertex Robin path with endpoint5/2 has characteristic value -1 at
lambda5/2, so its largest eigenvalue is larger than5/2. Enlarging the
advanced box changes the required spectral box. Changing the center
also changes the trace and origin; neither issue is silently closed.

## 6. Obstruction classification and final ledger

The independent-u witness T=x+41/12,b0=x+5/2,b1=0 is **abstract**, not
canonical or Fricke-completed. Exact replay verifies the reported
advanced corner delta0=-1939833799/11943936, while its required midpoint
gives delta0=6959573561/11943936>0. It refutes the broader independent-u
advance predicate, not MP_2 actual-gap transport or the MP_(5/2) theorem.

| Component | ROOT | SHORT/LONG | Target consequence |
|---|---|---|---|
| Origin identities/certificates with current paired MP_2 | established initialization | BOTH proved | current and outgoing G kernels |
| Expanded regular predicate | augmented root exception | rows/registers proved; new paired MP_2/proxy open | old P_Q target implication |
| Root edges of expanded predicate | old first-level P_Q plus new registers | new child MP_2 alone open | existing first-level target/proxy proofs retained |
| Optional origin MP_(5/2) | not established for every root origin | all fixed-trace L/H kernel blocks proved conditionally | no changed-reference or changed-center closure |

Reproduce the independent formal checks with

    python adversarial_packet_check.py

The result JSON records twelve zero symbolic residuals and the exact
abstract witness replay. The proof audit, rather than a finite scan,
supports the Robin/fork and midpoint implications. No all-tree conclusion
is asserted.
