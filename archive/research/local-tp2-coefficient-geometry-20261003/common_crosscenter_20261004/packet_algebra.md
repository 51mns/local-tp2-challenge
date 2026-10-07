# Anchored reverse blocks and the unavoidable signed mixed flux

Status: **proved universal trace compatibility, proved BOTH-child reverse
single-block support and upper-index strictness, and an exact mixed-flux
factorization with a universal negative source coefficient**. Arbitrary-parent
full changed-center paired MP_sharp preservation remains OPEN. No new path
class, finite-state closure, or full-tree Local TP2 theorem is claimed.

The only imported analytic theorems are the audited finite character/minor
equivalence and the MP_sharp Robin/window theorem in
`../common_midpoint_20261004/{network_relative_character,audit_minimal_packet,
packet_transport_subgate}.md`. Canonical ordinary bounds and degree ordering
come from `../fulltree_20261004/invariants_normalized_state.md`.
`packet_algebra_verify.py` independently replays the algebra and two fixed
root-edge normalization examples using a standard-library sparse polynomial
ring with arbitrary-precision rational arithmetic.
The continuum/all-index proofs are below; those examples are not their proof.

## 1. A universal shifted-trace compatibility theorem

Let f have degree d>=1. Assume f-r has positive Fourier interval support and
a weak folded-TP2 kernel for every r in [-2,2]. Write h=H(f), with reflection
at zero and zero extension. Then

    J(f-r,f-s) >=_char 0       for every r,s in [-2,2].                 (1)

In fact, the full shifted-trace gate and (1) follow from the two endpoint
kernel gates f-2,f+2 and the positive support of f-2. The converse implication
from the full shifted gate to the endpoint gates is immediate.

Put alpha=(r+s)/2 and omega=(r-s)^2/4. Exact polarization gives

    J(f-r,f-s)/2 = T_(f-alpha) - omega T_1.                            (2)

Here T_1 has just the character coefficient (0,0), equal to 1. Every other
coefficient of T_(f-alpha) is affine in alpha, so the two endpoint trace
tensors certify it. The central coefficient of (2) is exactly

    delta_0(f) -(r+s)(h_0+h_2/2)+rs,
    delta_0(f)=h_0^2-2h_1^2+h_0h_2.                                  (3)

Positive support of f-2 gives h_0>2, and h_2>=0. The derivative of (3) in r
is s-h_0-h_2/2<0, and the derivative in s is r-h_0-h_2/2<0. Its minimum
on the full square is therefore delta_0(f-2)>=0. This proves (1) and all
ordered mixed minors through the audited character theorem.

For the shifted-trace gate itself, every noncentral coefficient is again
affine in r. Its central coefficient is
delta_0(f)-r(2h_0+h_2)+r^2, whose derivative is negative on [-2,2]. Thus
the same endpoints suffice. Positive support throughout follows from h_0>2
and the unchanged noncentral Fourier entries. No smoothing by y is asserted;
this theorem concerns the raw trace family appearing in the packet.

## 2. BOTH reverse single blocks are one anchored Robin-window pencil

Retain the exact child variables from the brief:

    beta=3y^2, n=g+(1-sigma)e, v=s+sigma d,
    u=T-beta n, h=(1-2sigma)e, p=n+v,
    T'=T+beta v, c'=(u+1)v+h, e'=n.

The exact beta cancellation gives

    L'_r,rev=n(T'-r)+c'=(T-r)n+(T+1)v+h.

Define the anchor B=L'_-1,rev and theta=r+1. Then, for BOTH children,

    L'_r,rev = B-theta n,          -1<=theta<=3.                       (4)

The anchors have certified parent-origin descriptions:

| Child | Parent origin | Exact anchor |
| --- | --- | --- |
| short | q_j=c U_j(T)+e U_(j-1)(T) | B=q_1+q_0=c(T+1)+e |
| long | q_j=e U_j(T)+c U_(j-1)(T) | B=q_2+q_1=e(T^2+T-1)+c(T+1) |

U_-1=0,U_0=1,U_j=T U_(j-1)-U_(j-2). The short anchor is a parent
single block. The long anchor is the N=2,rho=-1 Robin block. Thus BOTH
B and yB are strict folded TP2 with positive Fourier interval support,
using only the current paired MP_sharp packets. This recovers the old r=-1
subgate and puts the rest of the parameter interval into one low-degree
anchor perturbation, rather than an unrelated fixed-trace advance.

The canonical ordinary bounds prove positive support of L'_r,rev and
yL'_r,rev for **all** r in [-2,2]. Indeed T-r has dense positive ordinary
coefficients (T has ordinary constant at least 3), n,v are positive and
dense. In the short case h=e>=0. In the long case v=s+d>=d=e(T+1)>=e,
so (T+1)v-e=T v+(v-e) is positive and dense. Products/sums then supply
dense ordinary support through the full degree; the ordinary-to-Fourier
transform and multiplication by y preserve positive interval support.
This is a support argument, not a cone argument.

The forward single blocks c'(T'-r)+n and their y multiples have positive
interval support for the same full parameter interval: c',n are the actual
canonical positive child coordinates and T'-r has dense positive ordinary
coefficients. This also resolves support of every child shifted trace and
every child midpoint H, in BOTH orientations. All child packet degree
conditions hold. Forward deg n<deg c'+deg T' is immediate. In reverse,
short deg c'=deg t+deg s<deg n+deg s+2=deg n+deg T', since deg n>=deg t;
long deg c'=deg e+2+deg v<deg g+2+deg v=deg n+deg T', since deg g>deg e.
Here deg T'=deg v+2, using the canonical degree hierarchy. These support
and degree statements do not sign any remaining low-index defect or mixed
interior character.

Let D=deg n and f=deg B. Canonical ordering gives D=deg g and
deg T=D+2; the sharp degree condition or the displayed origin formulas
give f>D+1. In raw mode, n has no Fourier entries past D. Therefore

    delta_j(L'_r,rev)=delta_j(B)>0        for D+2<=j<=f,                 (5)

uniformly on the full parameter interval, because a defect uses only
entries at j-1,j,j+1,j+2. In y mode the same argument gives

    delta_j(yL'_r,rev)=delta_j(yB)>0      for D+3<=j<=f+1.               (6)

These are genuine arbitrary-parent BOTH subgates, including the terminal
indices. Only the raw prefix 0<=j<=D+1 and smoothed prefix
0<=j<=D+2 can change with r. No forward-child single-block assertion is
inferred from this result.

There is one extra parameter-dependent boundary gate. At raw j=D+1,

    delta_(D+1)(B-theta n)
       =delta_(D+1)(B)+theta lc(n)H(B)_(D+2),                        (6a)

and at smoothed j=D+2 the same formula holds with B,n replaced by yB,yn.
Since theta=r+1>=0 for -1<=r<=2, both expressions are strictly positive
on that parameter subinterval. Thus the unresolved prefixes there shrink
to raw 0<=j<=D and smoothed 0<=j<=D+1. The remaining part -2<=r<-1 is
not certified at these two boundary indices.

## 3. Exact finite criterion for the remaining reverse single prefix

For either mode replace (B,n) by (yB,yn) if needed, and at a supported
defect j write

    E_j(theta)=delta_j(B-theta n)
               =a_j-theta b_j+theta^2 c_j,
    a_j=delta_j(B)>0,
    b_j=[the same adjacent selector]J(B,n), c_j=delta_j(n).             (7)

No sign of b_j or c_j follows merely from the parent packet. Set

    A_j=E_j(-1), Z_j=E_j(3),
    M_j=a_j-b_j-3c_j.

With t=(theta+1)/4 one has the exact Bernstein form

    E_j(theta)=A_j(1-t)^2+2M_j t(1-t)+Z_j t^2.                        (8)

Consequently strict positivity on the entire closed interval is EXACTLY

    A_j>0, Z_j>0, and
    [ M_j>=0 OR M_j^2<A_j Z_j ].                                     (9)

The weak version uses >= and <= respectively. This is the elementary
strict/weak copositivity criterion for a 2x2 matrix. It is not a claim that
the parent hypotheses imply these finitely many inequalities. Equations
(5)-(6) make (9) necessary only on the displayed low prefixes. Neither
power-coefficient positivity nor a seed-cone premise is being substituted.

## 4. A compact exact factorization of the full changed-center mixed gate

The following algebra holds for ANY seed pair (b0,b1) at trace T', so it
applies to BOTH child orientations without relaxing their correlations.
Put

    z=T'+1, B=b0 z+b1,
    theta=r+1, phi=s+1, eta=(theta+phi)/2,
    kappa=theta phi, omega=(theta-phi)^2/4.

For the reverse orientation b0=n,b1=c', B is the certified anchor above.
For the forward orientation b0=c',b1=n the algebra holds, but its B is
not certified by Section 2. Introduce

    A = T_(z-eta)-omega T_1,
    K = T_B+kappa T_b0-eta J(B,b0),
    F = J(B,b0 z)-J(B z,b0).                                         (10)

Then the EXACT child sharp tensor is

    T_H-omega T_b1 = A K+omega F,                                   (11)
    H=B(z-eta)-b0(eta z-kappa).

This identity is before any inequalities. A is half the mixed tensor
of the two child shifted traces; if the full child trace gate is proved,
Section 1 certifies A. K is half the mixed tensor of the two affine
single blocks B-theta b0,B-phi b0. It is not an axiom of the parent packet.
The new term F is the exact signed cross-center flux.

Its Bezoutian form is particularly short:

    F = Phi((z(zeta)-z(xi))
            (B(xi)b0(zeta)-b0(xi)B(zeta)))
      = (U^2-4)(V^2-4) R(1,z) R(B,b0).                              (12)

The universal discriminant factor is

    (chi_2(U)-3)(chi_2(V)-3),

which has both positive and negative characters. The smoothed identity
is the same (10)-(12) with B,b0,b1 replaced by yB,yb0,yb1; z is unchanged.
One must not multiply the raw certificate by T_y and assume positivity.

## 5. Sourcewise flux positivity is false at EVERY canonical child

Assume the packet degree condition deg b1<deg b0+deg z, and let
D=deg b0,d'=deg z>=1,f=D+d'=deg B. The polynomial b0 z has degree f,
whereas Bz has degree f+d'. Use rows (0,1) and columns

    k=0, l=f+d'+1.

In the first term of F=J(B,b0z)-J(Bz,b0), both inputs have degree f, so
that selected coefficient is zero. In the second term, the half-row of
x(Bz) has terminal entry lc(Bz), while the half-row of b0 at zero is
H(b0)_0>0; all other entries in that column vanish. Hence

    [chi_(f+d')(U)chi_(f+d')(V)] F
         = -H(b0)_0 lc(Bz) < 0.                                    (13)

The central-column normalization has NO extra factor two. This is an
all-state analytical obstruction to the sufficient proposal F>=_char0,
in BOTH orientations and BOTH modes. Fricke and paired Cassini cannot
remove (13): it uses the exact canonical degree inequality and positive
leading/support coefficients, which those correlations preserve.

Two fixed audited root-edge reverse examples independently normalize it:

| Child | D,d',f | selector (k,l) | character | coefficient of F |
| --- | --- | --- | --- | --- |
| root short | 1,4,5 | (0,10) | (9,9) | -1152 |
| root long | 1,5,6 | (0,12) | (11,11) | -1944 |

Those root children satisfy the full paired packet by the prior continuum
audit. Thus the negative flux is a failed sourcewise decomposition, NOT a
negative child sharp tensor. At the same terminal-column selector the
complete tensor has coefficient H(H)_0 lc H>0, since the reference seed
has smaller degree. Exact compensation by A K is compulsory.

More generally, let M=deg H=f+d'. For every 0<=k<=M,

    Sel_(k,M+1) F=-H(b0)_k lc H,
    Sel_(k,M+1)(T_H-omega T_b1)=H(H)_k lc H>0.                       (14)

The first formula is negative exactly for k<=D and zero past that support.
The second proves the **entire outer character layer a+b=2M** of the child
mixed gate, in BOTH orientations and BOTH modes, throughout the continuous
parameter square. For this support proof no child trace kernel is needed:
canonical b0,b1 have dense positive ordinary coefficients, as do T'-r and
T'-alpha for r,alpha in [-2,2], so H has positive Fourier interval support
of its fixed degree M. The lower-degree reference vanishes in the selected
column. The y mode uses yH,yb1 directly and its own terminal column.
At these coefficients the factorization enforces the exact compensation

    Sel_(k,M+1) A K=lc H[H(H)_k+omega H(b0)_k]>0.

This resolves an actual full-square mixed boundary, while the interior
character layers remain unproved. It also explains why the universally
negative source (13) produces no boundary counterexample to the packet.

## 6. Scope and remaining induction obligations

ROOT remains covered by the prior continuum proofs. All BOTH child packet
support and degree gates and the
reverse r=-1 anchor are proved; BOTH full-parameter reverse strict defects
are proved on the upper bands (5)-(6), with (6a) extending them by one index
for r>=-1. The reverse low-prefix criterion
(9) is exact but not proved from the parent hypotheses. The trace-family
compatibility theorem (1) is universal; it does not prove a changed trace
gate that is not already known. The factorization (11) is exact for BOTH
orientations and modes, the complete mixed outer character layer (14) is
strictly positive, and the sourcewise flux sign obstruction (13) is
universal, including Fricke states.

What remains for full A_sharp is: the noncentral child shifted-trace gates;
the reverse low-prefix (9); all forward child single-block strictness; and
the compensated character inequality A K+omega F>=_char0 on its interior
character layers throughout the full square, in both orientations and
modes. The paired Cassini identity

    c^2+e(Tc+e)=C^2(1+3(C-1)/y)

becomes B^2-(z+1)nB+(z+1)n^2=D_child in anchored reverse child coordinates,
where D_child is the corresponding positive endpoint correction. This
one-variable identity has not supplied the remaining cross-variable
compensation. The separate strict
proxy overlap gate is also OPEN. No TARGET closure follows from these
partial packet gates.
