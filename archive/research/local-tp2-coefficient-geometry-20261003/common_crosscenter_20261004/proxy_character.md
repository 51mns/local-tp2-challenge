# Robin quantitative geometry and a weaker common target gate

Status: **proved universal diagonal identity and conditional quantitative
lower bounds; proved weaker target reduction; exact canonical obstruction
to a coarse sufficient bound and to a sourcewise positivity shortcut.**
Arbitrary BOTH preservation of either proxy, and full-tree strict Local
TP2, remain **OPEN**. Nothing below substitutes free rows for the actual
Fricke/ancestry data.

Notation: y=x+1, P=x+2, Q=S-G, Pi=XP M, V=PX+P²C,
E=ye, G=yg, S=ys, D=EM. Thus Pi=PQ+V. T_f, J(f,g), R(f,g)
are the finite two-character tensors in
`../common_midpoint_20261004/network_relative_character.md`.
The boundary selector [chi_(2n)(U)chi_0(V)]R(f,g) is the adjacent
half-row minor W_n(f,g), including n=0 without an extra factor two.
Tensor inequalities below mean **character-coefficient** inequalities,
not positivity at numeric values of U,V.

## 1. The fixed-endpoint proxy can be weakened without making target a premise

Keep canonical algebra, the four regular LR companions, K_G and K_M,
and the origin/current-packet subsystem. Replace the old strict gate

    W_n(Q,Pi)>0

by the weaker explicit comparison

    W_n(Q,D)>0, 0<=n<deg Q.                           (1)

This is a sufficient gate for target, with a direct proof. The existing
K_G and R<=lrG imply G<=lrS by

    R(G,S)=R(G,tG)+R(R,G)>=character0.

Here 1<=lr t and folded convolution through K_G supplies the first
term. Linearity then gives R(S,Q)=R(G,S)>=character0. Hence

    S<=lr Q<lr D.                                    (2)

Actual degree ordering gives deg S=deg Q=deg X+deg C+1 and
deg D=deg Y+deg C+1>=deg Q+1. Every interior supported target minor
is strict by the positive dense supports and ratio transitivity; its
terminal minor is H(S)_degS H(D)_(degS+1)>0. The terminal Q,D
comparison is automatic for the same reason.

The proof of all four LR companion links at BOTH children in
`../common_closure_20261004/reduction_common.md` Section 3 consumes
only the parent four LR links, K_G, and the parent target S<=lrD
derived in (2). It does not subsequently use Pi. Therefore that whole
LR transport theorem remains valid for the replacement predicate.
The exact origin/register transport is likewise unchanged.

The old predicate implies (1): XP<=lrE transported through K_M
gives Pi<=lrD, and strict Q<lrPi implies strict Q<lrD on all interior
Q indices. The converse is not asserted. In particular we do **not**
claim the replacement predicate implies old P_Q. The implication is
proved directly by (2).

This avoids treating target itself as an invariant. Its extra comparison
is genuinely different algebraically:

    R(Q,D)=R(S,D)-R(G,D).

Under the derived orders G<=S<=D, it demands the target surplus exceed
the nonnegative incoming-gap surplus R(G,D), rather than simply demand
the target. BOTH-child preservation of (1) is still an analytic gate;
the reduction alone is not a closure proof.

## 2. Two exact Fourier surpluses and a promising signed correction

Let F=E-XP. The falsification lane independently derived the following
canonical invariant, replayed here by a universal sparse-polynomial
identity. Short mutation gives F'=F+G. Long mutation gives

    F'=(x²-1)e+x+y(r-1)+ya(2+3x)+3y³a(a+e).          (3)

Canonical a,e>=ordinary0 and r>=ordinary1 imply Fourier entry positivity
of every term in (3): x²-1 has half-row (1,0,1). The root has F=-1;
the first short has half-row (6,5,2), and every long step is covered
directly by (3). Therefore **every canonical nonroot has H(F)>=0**.
This is entry positivity only. At the actual first long,

    F=x²+x-1, H(F)=(1,1,1), delta(F)=(0,-1,1),

so F is not a folded cone multiplier.

There is also an interior-endpoint comparison at the level of entries:

    Q-V=2P(xC-y)+y(X-P)(3C-2).                       (4)

Every actual X other than 1 is P or an earlier center, so X-P>=ordinary0.
Every actual center dominates the initial center 2x²+6x+5 ordinarily.
The half-row of xC-y is

    (2H(C)_1-1, H(C)_0+H(C)_2-1,
                       H(C)_1+H(C)_3, H(C)_2+H(C)_4,...),

and is nonnegative. Thus H(Q)>=H(V) for every interior endpoint X!=1.
Neither (3) nor (4) controls the wedge W(Q,V) or gives a quantitative
folded defect; entrywise dominance is not LR dominance.

For the weaker target comparison define the actual correction

    Btilde=D-PQ=V+FM.                                (5)

The exact identity

    R(Q,D)=T_Q+R(Q,Btilde)                            (6)

means that strict K_Q plus weak Q<=lrBtilde would prove strict (1).
If H(Btilde) has positive dense interval support, all its adjacent
comparisons imply all ordered half-row comparisons. The already proved
strict K_Q comes from the retained Robin register and its separate
endpoint-1 theorem; (6) introduces no assumption that y is a cone
multiplier. Showing R(Q,Btilde)>=character0 is a possible common gate,
but remains **OPEN**. Exact root, short, long, and long-long arrays
pass it here; those finite arrays are not a proof for arbitrary ancestry.

The seemingly simple factored source has an actual obstruction. With
A=t-2 and B=P²+3yF one has

    Btilde=CB+F(1-x)+PX,
    R(A,B)=R(A,3yE)-T_A.

At the genuine first short,

    A=1+2x, B=10+25x+22x²+6x³,
    [chi_0chi_0]R(A,B)=-65.

Its next adjacent coefficient is 44. Thus sourcewise R(A,B)>=character0
fails even though the complete actual R(Q,Btilde) is nonnegative there.
The cancellation in the full correlated pair must be retained.

## 3. A quantitative bound from the Robin certificate, valid at all indices

Consider an ordinary certified smaller register with trace t of degree
d>=1 and origin seeds b0,b1. Let p=deg b0 and

    f_N=b0 U_N(t/2)+b1 U_(N-1)(t/2),
    Q=y(f_N-f_(N-1)), N>=1.

The MP_sharp degree bound is deg b1<p+d. The terminal-1 Jacobi path
J_N has eigenangles theta_i=(2i-1)pi/(2N+1), eigenvalues
lambda_i=2cos(theta_i), i=1,...,N, and positive first resolvent weights

    w_i=4sin²(theta_i)/(2N+1)
       =(4-lambda_i²)/(2N+1), sum_i w_i=1.             (7)

The sine eigenvector has squared norm (2N+1)/4; this proves (7) without
an eigenvalue approximation. For N>=2 the first vertex has diagonal
zero and exactly one unit edge, so sum_i w_i lambda_i²=(J_N²)_11=1.
The same second moment is 1 for N=1. Consequently

    sum_i w_i²=3/(2N+1).                              (8)

Let L_r=b0(t-r)+b1 and

    A_i=yL_(lambda_i) prod_(j!=i)(t-lambda_j).

Then Q=sum_i w_i A_i. The smoothed sharp packet and common cone
factors show J(A_i,A_j)>=character0 for i!=j. Its diagonals are strict
by the certified strict-times-weak degree lemma. Therefore

    T_Q >=character sum_i w_i² T_Ai.                 (9)

Every A_i has degree p+Nd+1 and positive Fourier interval support, so
the diagonal strictness covers index zero, every interior index, and
the terminal. This uses smoothed L/H certificates directly; no separate
T_y positivity is used.

Here is an explicit rational uniform lower bound in (9). Put h=H(t),
and let eta_j be the exact minimum on r in [-2,2] of

    delta_j(H(y[b0(t-r)+b1])).

These defects are quadratic polynomials in r; their minima are found
by two endpoints and, for a convex quadratic, its vertex when inside
the interval. Under MP_sharp each eta_j>0. Define the trace minima

    mu_0=(h_0-2)²-h_1²,
    mu_1=h_1²-(h_0+2)h_2,
    mu_j=h_j²-h_(j-1)h_(j+1), j>=2.                  (10)

For a shifted trace these are the minima of the ordinary log-concavity
differences Delta_j=h_j²-h_(j-1)h_(j+1), with reflected indices at
zero. Weak folded TP2 and positive interval support imply
Delta_j=sum_(k=j)^d delta_k>0, so all mu_j in their support are positive.

For each output index 0<=n<=p+Nd+1, begin k_(N-1)=n and work backwards
through its N-1 weak trace factors. If factor stage m has strict
previous degree f_(m-1)=p+d+1+(m-1)d, set

    k_(m-1)=max(d,min(k_m,f_(m-1))).

Use multiplier mu_|k_(m-1)-k_m| if k_m>=1, and
2(lc t)² if k_m=0. Let beta_n be eta_(k_0) times all these multipliers.
For N=1 the product is empty and beta_n=eta_n. A single retained
Cauchy--Binet term at each stage proves delta_n(A_i)>=beta_n uniformly
in every lambda_i and every other spectral root. The central factor
2(lc t)² is the exact folded central-column normalization. Hence

    delta_n(Q) >= 3 beta_n/(2N+1)>0                  (11)

at **every** supported n, without an upper bound on kernel indices.
The ordinary endpoint-1 register is not an MP_sharp origin; (11) is
not asserted for it. Its audited separate Robin theorem remains needed.

Equation (11) is a valid sufficient route to the original proxy if
its bound exceeds H(Q)_(n+1)H(V)_n-H(Q)_nH(V)_(n+1). It does not
follow that this sufficient route is strong enough.

## 4. The coarse lower bound fails, and exact diagonal retention removes that loss

At the actual first long, the retained smaller origin is

    t=3x²+8x+6, (b0,b1)=(2P,0), N=2.

Its exact uniform minima are

    eta=(2712,4576,2488,520,36), mu=(36,22,9).

At n=0, (11) gives 134352/5, while the adverse correction is 174440.
The proposed sufficient domination surplus is -737848/5. The actual
delta_0(Q) is 1396384 and actual strict proxy surplus is 1221944.
Thus the quantitative theorem is valid, but this coarse sufficient
gate already fails at a genuine fully certified seed. This is **not**
a failed proxy or a failure of MP_sharp.

One can keep the full spectral diagonal tensor in (9) exactly, with
no eigenvalues in the final expression. Write

    p_N(z)=U_N(z/2)-U_(N-1)(z/2),
    h_N(z)=4p_(N-1)(z)-z p_(N-2)(z), N>=2,
    h_1(z)=3,
    K_N(a,b)=[h_N(a)p_N(b)-p_N(a)h_N(b)]/(b-a).

The quotient K_N is a polynomial, including a=b by continuity. Set
a=t(xi), b=t(zeta), p_a=p_N(a), h_a=h_N(a), and analogously at b.
The divided difference is taken in the spectral variables a,b **before**
composition: its composed denominator is t(zeta)-t(xi), not zeta-xi.
Thus K_N(t(xi),t(zeta)) is not the Bezoutian of the composed polynomials;
no extra trace divided-difference factor belongs in (12).
Then the **exact** sum of diagonal tensors is

    D_N=sum_i w_i² T_Ai
       =1/(2N+1) Phi[y(xi)y(zeta) {
          3 b0(xi)b0(zeta) p_a p_b
          + b0(xi)b1(zeta) p_a h_b
          + b1(xi)b0(zeta) h_a p_b
          + b1(xi)b1(zeta) K_N(a,b) }].              (12)

Proof: (7) changes w_i² into w_i(4-lambda_i²)/(2N+1).
For N>=2, with m(z)=p_(N-1)(z)/p_N(z),

    sum_i w_i(4-lambda_i²)/(z-lambda_i)
       =(4-z²)m(z)+z=h_N(z)/p_N(z).

Taking the divided difference of this resolvent gives K_N; expanding
the two residue factors gives (12). For N=1 the spectrum is {1}, the
weight is 1, and h_1=3 makes (12) exactly T_Q. Using the N>=2 formula
for h_N at N=1 would be incorrect. The verifier checks (12)'s weighted
one- and two-resolvent polynomial identities by exact path adjugates
for N=1,2,3,4. Those finite checks validate normalization; the displayed
resolvent proof is the all-N theorem.

Under the packet, D_N>=character0 and T_Q-D_N>=character0 by (9).
The four summands displayed in (12) are **not** separately claimed
character-nonnegative, especially for signed b1 or the explicit y pair.
When b1=0, all A_i are Q itself and (12) reduces to

    D_N=3 T_Q/(2N+1).

In the first-long seed this exact diagonal bound plus W(Q,V) is
strictly positive at every index; its minimum is 972/5. This explains
the information lost in (11), without claiming that exact diagonal
retention solves general canonical ancestry.

## 5. The exact mixed margin that remains missing

For i<j put C_ij=prod_(k!=i,j)(t-lambda_k), and use the smoothed origin
blocks yF_ij,yG_ij,yH_ij with parameters lambda_i,lambda_j. Then

    T_Q=D_N+
      2 sum_(i<j) w_iw_j T_Cij {
         T_(yH_ij)-((lambda_i-lambda_j)²/4)T_(yb1) }.
                                                               (13)

This is an exact full-character identity retaining all off-diagonal
contributions. The braces are the sharp packet's character cone.
Its stated weak sign supplies zero as a lower bound; it does not by
itself supply a proved quantitative comparison to the unrelated signed
R(Q,V) correction. To use (13) for closure one must prove the correlated
boundary domination of D_N plus those mixed margins over -R(Q,V).

The old uniform-4 inequality would give an extra
(4-(lambda_i-lambda_j)²/4)T_(yb1) term only if T_(yb1) were itself
character-nonnegative. Such a seed-cone premise was intentionally
removed from MP_sharp and is not reintroduced here. The total tensor
identity (13), rather than a sourcewise seed sign, is the safe retained
information. No independent spectral parameter margin or numeric
polynomial evaluation is being substituted for a character bound.

## 6. ROOT, BOTH, TARGET ledger

| Obligation | Exact status |
| --- | --- |
| ROOT weaker target gate and paired initialization | Inherited from proved root proxy/packets; exact four-state checks here are replay only. |
| BOTH canonical algebra, four LR links under replacement gate | Proved by the direct target sandwich and unchanged companion transport. |
| BOTH origin/register transport and strict K_Q | Inherited proved subsystem; the endpoint-1 exception still uses its separate audit. |
| Ordinary Robin quantitative theorem and exact D_N | Proved conditional on certified origin MP_sharp, for every N and every supported index. |
| Uniform factor-CB bound dominates original signed correction | False already as a sufficient gate at the actual first long. |
| Common factored source R(A,P²+3yF)>=character0 | False at the actual first short (central -65). |
| BOTH strict original proxy Q<Pi | OPEN on arbitrary regular parents. |
| BOTH strict weaker proxy Q<D, or sufficient Q<=Btilde | OPEN. |
| BOTH new-center paired MP_sharp | OPEN and independent of the weaker proxy reduction. |
| IMPLIES TARGET with weaker gate | Proved directly by S<=Q<D, including terminal support. |
| Full-tree strict Local TP2 | OPEN. |

Reproducer: `proxy_character_verify.py` (standard Python exact integer/
Fraction arithmetic; no external modules). Saved result:
`proxy_character_results.json`. It checks universal sparse identities,
weighted path adjugate identities, actual normalized Fricke at each
targeted state, both proxy comparisons at finite seeds, and the exact
failed sufficient bound. It does not enumerate future states or use
finite tests as an arbitrary-parent BOTH proof.
