# A finite strictness reduction for the actual origin consumers

Status: **proved conditional origin theorem and sufficient-predicate
weakening; arbitrary BOTH closure remains OPEN.** The weak mixed gate
cannot be reduced to discrete future path spectra: their simultaneous
root pairs are dense in the full parameter square. Strictness of every
single block, however, is more than the actual origin proof needs.

All prior directories are read only. This note uses the established
folded-kernel criterion, exact character/minor equivalence, strict-product
CB indexing and the actual register identities. It introduces no future
target assertion, no new path class and no state scan.

## 1. The proposed weaker packet is an explicit present-time condition

Let T have degree d>=1, b0 nonzero of degree p>=0, and
`deg b1<p+d`. Retain the current shifted-trace and exact mixed gates:

* For every r in [-2,2], T-r has positive Fourier interval support and
  a weak folded-TP2 kernel.
* Put `L_r=b0(T-r)+b1`, `F_rs=L_r(T-s)`, `G_rs=L_s(T-r)`.
  For every r,s in [-2,2], J(F_rs,G_rs) and J(yF_rs,yG_rs) are
  character nonnegative.

Replace strictness of every single block by:

* For every r in [-2,2], L_r and yL_r have positive Fourier interval
  support and **weak** folded-TP2 kernels.
* L_0 and yL_0 have strictly positive supported defects.

Call this core condition W_0(T,b0,b1). The optional W_01 also requires
strict supported defects of L_-1 and yL_-1. Each contains finitely many
character/defect coefficient polynomials on the existing compact parameter
domains and one (or two) explicit strict parameter values. Neither has
a quantifier over future recurrence lengths. MP_sharp implies W_01,
which implies W_0. These are strict-anchor labels, not a change to the
radius-two trace/mixed parameter boxes.

No seed cone is added. In particular the reversed root seed y remains
outside the folded cone. No strict claim about every midpoint H is
needed or silently retained; its weak cone follows from the weak F/G
cones and the exact nonnegative mixed gate.

## 2. A nonnegative quadratic has at most one interior zero

For each supported defect index j in either mode,

`E_j(r)=delta_j(L_r)` or `delta_j(yL_r)`

is a polynomial of degree at most two in r. Under W_0 it is nonnegative
throughout [-2,2], and `E_j(0)>0`. Thus it is not the zero polynomial.
Every zero in (-2,2) has even multiplicity, so there is at most one
such zero. This includes constant and linear polynomials.

Consequently, among any two or more distinct spectral points strictly
inside (-2,2), at least one makes this particular defect strictly
positive. The point may depend on j. The conclusion does not require
every single block at those spectral points to be strict at all indices.

## 3. The common-factor CB term preserves a selected base defect

Let A have degree f>=d, positive interval support and a weak folded
kernel. Let B have degree d, positive interval support and a weak folded
kernel. For an output defect n, the exact CB term with intermediate
indices i,i+1, where `i=max(d,min(n,f))`, gives

`delta_n(AB)>=delta_i(A) c_(i,n)(B)`,

where `c_(i,0)=2(lc B)^2>0`, and for n>=1,
`c_(i,n)=Delta_|i-n|(B)>0`.

The strict positivity of the latter follows from
`Delta_j=sum_(k=j)^d delta_k(B)` and the positive terminal defect.
All other CB terms are nonnegative. This is the old strict-product
indexing used as a lower bound for a possibly weak first factor.

Iterating through any fixed number of shifted trace factors selects
one supported base index k0. This k0 depends only on the degree p+d
(or p+d+1 in y mode), the factor count and output n. It does not depend
on the spectral values or which residue summand is selected. Every
multiplier in the retained product is strictly positive.

## 4. Ordinary runs and Robin runs are strict at their actual indices

Use normalized continuants `U_-1=0,U_0=1,U_N=T U_(N-1)-U_(N-2)` and

`q_N=b0 U_N+b1 U_(N-1)`.

For N>=2 and |rho|<=1, the terminal-rho Jacobi path has N distinct
eigenvalues lambda_i strictly inside (-2,2), with positive endpoint
weights w_i. Strict interior location follows from the exact quadratic
forms: at rho=1 the upper form still has a positive first-boundary term,
and at rho=-1 the lower form does; a zero vector along the whole stem
is the only equality case. Simplicity and positive weights follow from
the nonzero path edges. Its resolvent gives

`q_N-rho q_(N-1)=sum_i w_i A_i`,
`A_i=L_(lambda_i) prod_(j!=i)(T-lambda_j)`.

Every A_i has the same fixed positive degree and positive interval
support, and is weak folded TP2. For one output defect n, Section 3
selects a common base index k0. Section 2 ensures that at least one
lambda_i has `delta_k0(L_(lambda_i))>0`; hence the corresponding A_i
has a strictly positive output defect. The exact mixed gate supplies
`J(A_i,A_j)>=character0` after the common factors are restored.
Therefore the positive diagonal contribution in

`T_(sum_i w_i A_i)=sum_i w_i^2 T_Ai+sum_(i<j)w_iw_j J(A_i,A_j)`

proves strictness at n. This argument applies separately at every
supported n, including zero and terminal. The y proof starts with
yL and uses the separately retained y mixed gate.

Thus W_0 supplies strict raw/y `q_N-rho q_(N-1)` for **N>=2**, every
|rho|<=1. At N=1, W_0 directly supplies rho=0. The optional W_01
also supplies rho=-1. Neither asserts the N=1 theorem for other rho.
That loss is explicit and does not affect the actual consumers below.

## 5. Prefixes, windows and all actual register consumers

The existing prefix is

`Z_N=b0 R_(N-1)+b1 R_(N-2)`, `R_j=sum_(i=0)^j U_i`.

Let m=N-1>=1. The resolvent R_(m-1)/R_m has, after cancellation:

| m | Surviving path | Positive poles | Required strict source |
| --- | --- | --- | --- |
| 1 | One-vertex Robin diagonal -1 | {-1} | L_-1; W_01 only |
| 2 | One-vertex pure path | {0} | L_0 |
| >=3 even, m=2h | Pure path on h vertices | h>=2 distinct interior poles | Quadratic zero count |
| >=3 odd, m=2h+1 | Robin -1 path on h+1 vertices | h+1>=2 distinct interior poles | Quadratic zero count |

The cancelled roots remain weak shifted trace factors. The degree bound
and the same common base-index argument prove strict Z_N and yZ_N for
every N>=3 under W_0, and every N>=2 under W_01. N=1 remains excluded:
Z_1=b0 is not certified as a cone. N=2 is only weak under W_0.

The contiguous-window theorem is also retained. Its odd formula uses
a strict q_N at rho=0, N>=1. Its even formula uses a strict
q_N+q_(N-1) at rho=-1 with N=m+k>=2 because the window starts at
index m>=1. Multiplication by the old weak shifted trace prefactors
retains strictness with the existing degree comparison.

The complete dependency map is:

| Actual conclusion | Index/source | Outcome |
| --- | --- | --- |
| Current smaller previous gap f_(N_X-1), N_X>=2 | Ordinary q_j, j>=1; j=1 uses L_0 | Strict raw/y |
| Both current outgoing origin gaps | q_N, N>=1 | Strict raw/y |
| New short larger origin at index 1 | Forward L_0 | Strict raw/y |
| New long larger origin at index 2, previous index 1 | Reversed q_2 and L_0 | Strict raw/y |
| Current/child Q at ordinary smaller register | Robin rho=1, N_X>=2 | Strict raw/y normalized difference, hence actual Q |
| Short reverse child anchor | Parent forward L_-1 | Strict raw/y under W_01; not a core W_0 consequence |
| Long reverse child anchor | Parent reversed q_2+q_1 | Strict raw/y by N=2 theorem |
| Ordinary anchor-prefix trace tails | Z_N, N>=3 under W_0; N>=2 under W_01 | Strict raw/y prefix at those indices, same beta degree gate |
| Endpoint-1 exception | Existing independent U, prefix and y Robin theorems | Unchanged; not assigned either packet |

The main register/kernel/target proof consumes only the core W_0 rows;
the short reverse anchor and full prefix N>=2 theorem are optional
previous subgates retained by W_01. Neither version consumes N=1 Robin
with arbitrary rho.
The previous stronger quantitative bound using a uniform positive
minimum eta_j over the full single interval is **not** retained: that
minimum may now be zero. The exact diagonal/mixed identities remain
algebraically valid; their use at N>=2 remains justified by the proof
above. No missing numerical margin is declared solved.

## 6. A genuinely weaker paired certificate

The weakening is strict as an abstract paired certificate. Let

`T=10x+1+5 sqrt(17)`, `e=1`, `c=2`.

For q in [-4,2], put B=1+5sqrt(17)-q. Then
`19<B<=5+5sqrt(17)<26`. The rows of T-q and y(T-q) are

`(B,10)`, `(B+20,B+10,10)`.

Their defects are respectively

`(B^2-200,100)`,
`(-B^2+10B+400,B^2+10B-200,100)`.

Raw defects are strict. The smoothed central defect is nonnegative
and is zero exactly at q=-4, because its positive root is
5+5sqrt(17). All other smoothed defects are strict. The forward and
reverse singles are `2[T-(r-1/2)]` and `T-(r-2)`. Hence both are weak
on the full r interval, and strict at r=0,-1. At r=-2 the reverse y
single has central defect zero, so MP_sharp fails.

For the mixed gate, each midpoint H is gamma(T-q1)(T-q2), with
gamma=2 or 1 and q1,q2 in [-4,2], by the same exact root-bound argument
as the preceding relaxed paired examples. Raw H and yH are weak cones
by product closure. The only positive reference selectors of T_y are
columns (0,2) and (1,2), each coefficient one. The following elementary
rational bounds hold throughout the square:

* Raw central H defect is at least 20000 gamma^2 by one exact CB term.
* The yH selector (0,2) is greater than
  `(361+380+300)*361 gamma^2=375801 gamma^2`.
* Its selector (1,2) is greater than
  `(361+190-200)*(361-100) gamma^2=91611 gamma^2`.

These dominate the largest uniform reference 16 T_y or 16 T_1.
All remaining reference characters are zero or negative and are covered
by the H cones. Thus even the uniform-4 relative bounds hold in both
orientations and modes over the full continuous square, proving the
retained sharp mixed gate. This is W_01 paired and not MP_sharp paired,
so it also proves the core W_0 certificate can be strictly weaker.
It is an abstract noncanonical certificate, not a canonical counterexample
to full-tree Local TP2. No interior-zero example is asserted.

## 7. Dense future root sets do not weaken the weak mixed requirement

For the N-vertex pure path, roots are
`lambda_j=2 cos(j pi/(N+1))`, 1<=j<=N. For any prescribed r,s in
[-2,2], choose the two integer grid indices nearest their inverse cosine
angles. As N grows, the corresponding roots of the **same** path tend
to r,s. Distinct indices can be chosen even when r=s. Hence the union
of same-path ordered root pairs is dense in the full square.

Every character coefficient of J(F_rs,G_rs) is a polynomial, hence
continuous in r,s. Nonnegativity at every future N and every same-N
root pair is therefore equivalent to its full continuum nonnegativity.
The same statement holds in y mode. Restricting to these infinitely
many spectra would relabel the open gate, not weaken it. Allowing only
currently occurring finite counts would lose the certificate needed
for unrestricted retained-origin advance unless a separate induction
of the count-dependent inequalities were proved.

The strictness reduction in Sections 1-5 does not do this. It uses
nonnegative finite quadratics and the number of distinct positive
residues to prove strict **sums**, with one strict present-time anchor
in the core certificate. It leaves the weak mixed continuum gate intact.

## 8. ROOT, BOTH and TARGET under the weaker predicate

Keep canonical algebra/ordinary bounds/Fricke and ancestry, all four
LR companions, the exact two origin registers and strict interior Q<D.
Replace both current and ordinary origin MP_sharp certificates by W_0.
Call this core alternative P_0. Its optional version P_01 uses W_01
instead. The root keeps its existing LR exception.

For the adopted versions, explicitly retain the additional integer flags
`delta_0(T_current-2)>=1` and `delta_0(t_origin-2)>=1` for every stored
ordinary origin trace. Endpoint 1 is excluded from the latter flag.
These are recorded central invariants, not consequences of a weak packet.
The root current trace has central defect 185, and its initial ordinary
P-origin trace has defect 2. On either advance,
`T_child=T_current+beta v`, where the retained actual outgoing v is raw
strict of degree at least two. The weak degree-two beta and the old CB
degree gate make beta v strict. Convexity of the nonnegative central-row
cone gives `delta_0(T_child-2)>=delta_0(T_current-2)+delta_0(beta v)>0`.
Integer coefficients give the required flag at least one. Each newly
created ordinary origin stores the old current T and inherits its flag;
retention keeps the stored trace fixed. This proves ROOT and BOTH
transport of the flags using Section 4, without a child packet or proxy.
There is no third unresolved closure type. These explicit flags also
permit the ordinary SHORT lower-block theorem in `proxy_algebra.md`;
plain W_0 by itself does not supply that theorem's central flag.

ROOT and both first children satisfy both versions because their stronger
certificates are already proved. Sections 4-5 retain strict G/Q,
the parent trace gate still supplies M, and S<=Q<D proves TARGET
directly. The same parent target/LR proof and exact register
initialization/retention transport BOTH without assuming either child
packet. P_01 retains all prior qualitative consumers in Section 5.
P_0 retains the core proof, central trace and ordinary prefix tails
at N>=3, but not the short reverse-anchor/prefix-N=2 strict subgates.
Optional full-box uniform positive eta estimates are not included in
either version.

This is a sufficient weaker predicate, not its closure theorem. Exactly
two closure types remain: BOTH new paired W_0 packets, and BOTH strict
Q'<D'. The new packet still has weak single, shifted-trace and mixed
conditions, plus its strict anchor at zero. They have not been proved from
an arbitrary regular parent. Full-tree strict Local TP2 remains OPEN.

Independent reviews of Sections 1-8: `packet_spectral_sparse_audit.md`,
`packet_algebra_weakening_audit.md`, and the parent's ROOT_AUDIT.md.
The genuine paired witness additionally has an independent continuum and
exact quadratic-field replay in `falsification_weakening_audit.md` and its
verifier. `audit_packet_weakening_verify.py` checks the universal symbolic
quadratic defect identity, the Delta telescoping identity, and the exact
recorded ROOT flag rows; it does not substitute a grid for this proof.
