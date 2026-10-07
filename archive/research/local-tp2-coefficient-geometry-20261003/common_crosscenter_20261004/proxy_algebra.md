# Exact anchored origins and a fixed-band proxy reduction

**Status.** The two anchored-origin identities have unconditional BOTH
transport under the canonical algebra. For an ordinary certified origin,
the unanchored prefix is strict folded TP2 in raw and y modes. The anchor
can change defects only in a fixed low band. A universal common-product
lemma reduces the original strict proxy to a fixed origin band, conditional
on one frozen endpoint source. The source and low-band signs are not proved
at arbitrary new origins. Neither strict proxy BOTH closure nor full-tree
Local TP2 is claimed.

Older directories are read only. This note uses the already audited sharp
midpoint resolvent theorem and the register identities; it does not use a
new-center child packet or a target assertion to prove the identities.

## 1. The exact anchor, including BOTH new origins

Put y=x+1, P=x+2, z=2x+3, X=1+y a_X, t=3yX-x,
A=t-2 and B=(C-1)/y. Set U_-1=0, U_0=1,
U_j=t U_(j-1)-U_(j-2), and

    R_j=sum_(i=0)^j U_i, R_-1=0.

For an origin f_j=b0 U_j+b1 U_(j-1), the exact identities are

    (U_N-U_(N-1)-1)/(t-2)=R_(N-1), N>=1,
    f_N-f_(N-1)=b0+b1+A[b0 R_(N-1)+b1 R_(N-2)].       (1)

Here N=1 uses R_-1=0 and f_0=b0. The canonical fixed-endpoint
identity is

    Q=y(f_N-f_(N-1))=y[A B+k0], k0=1+z a_X.           (2)

Consequently, if b0+b1-k0=A a_O, the complete normalized center is

    B_N=a_O+Z_N,
    Z_N=b0 R_(N-1)+b1 R_(N-2).                       (3)

This is an equality, including its initial anchor. It is stronger than
an assertion that B is an unspecified sum of gap windows.

At a canonical parent use a,e,r, g=A_X e+X(3X-2)+r,
s=t_X g-r, c=e+g+s, B=a+e+g, T=3yC-x=z+3y^2 B.
Direct substitution, with the r terms cancelling, gives

    c+e-[1+z B]=(T-2)a.                               (4)

No Fricke equation is required for (4); it holds for arbitrary a,e,r
under the displayed canonical definitions. BOTH new endpoint-C origins
have seed sum c+e. Thus their common anchor is exactly the old parent a:

| Initialization | Seeds (b0,b1) | Index | Formula for new B |
| --- | --- | --- | --- |
| Short, new larger endpoint C | (c,e) | 1 | a+c=B+s |
| Long, new larger endpoint C | (e,c) | 2 | a+(T+1)e+c=B+s+d |

The long index is important: its B is a+c+e(T+1), not a+c+Te.
For every retained origin,

    B_(N+1)-B_N=f_N.                                  (5)

Hence its fixed tuple (t,b0,b1,a_O) stays unchanged and N advances by
one. The smaller root origin has t=z, (b0,b1,a_O,N)=(1,0,0,2).
The larger root origin has endpoint P, trace 3yP-x, and
(b0,b1,a_O,N)=(2P,0,0,1). Both (3) give the root B=2P.
Equations (4)-(5) prove BOTH initialization/retention of these anchor
identities at every degree, not just at the saved seed examples.

## 2. What the certified packet does sign

For an ordinary MP_sharp(t,b0,b1) origin, Z_N in (3) is strict folded
TP2 in both modes for N>=2. Indeed, write m=N-1. The exact prefix
factorizations are

    R_(2h)=U_h (U_h+U_(h-1)),
    R_(2h+1)=U_h (U_(h+1)+U_h).

Thus R_(m-1)/R_m is respectively U_(h-1)/U_h or
(U_h+U_(h-1))/(U_(h+1)+U_h). These are positive first-vertex
resolvents for a unit path, or the Robin path with terminal diagonal -1.
All roots of R_m lie in [-2,2]; canceled roots have zero residues.
Retaining the positive residues gives

    Z_N=sum_i w_i L_(lambda_i) prod_(j!=i)(t-lambda_j).

Every summand has degree deg b0+m deg t. Diagonal summands are strict
by the sharp packet's degree-controlled product theorem. Distinct
summands have exactly the existing mixed residual pair
L_r(t-s), L_s(t-r), after common factors are removed. The sharp mixed
gate and common-product closure sign their cross terms. The same proof
uses yL blocks independently. This establishes the infinite prefix
statement, including both support boundaries. N=1 is excluded because
Z_1=b0 need not be a cone. The endpoint-1 origin is exceptional and is
not assigned an ordinary MP_sharp certificate here.

Nothing in this argument says that the anchor a_O is a cone or is
compatible with Z_N. There is, however, an exact support reduction.
For reflected, zero-extended Fourier rows, adding a_O changes a raw
folded defect only at n<=deg a_O+1. Adding y a_O changes a smoothed
defect only at n<=deg a_O+2. Therefore (3) already supplies strict
normalized-center defects outside those fixed bands at every ordinary
smaller register, whose N is at least 2. If a_O=0 the entire B_N is
strict. Ordinary a_O<=e alone cannot be substituted for these mixed
signs; it is an entrywise bound, not a compound-kernel bound.

## 2a. A fixed-band shifted-center-trace corollary

For the same ordinary smaller origin, the actual center trace is

    T_C=z+beta B_N=beta Z_N+(z+beta a_O), beta=3y^2.

Every actual ordinary endpoint has deg t>=2. Thus N>=2 gives

deg Z_N>=2. The positive weak factor y^2 has degree 2 and defects
(4,0,1), so the strict-times-weak lemma makes beta Z_N strict. It also
makes beta(yZ_N) strict, using the independently certified y-prefix.
Set

    h=1 if a_O=0; otherwise h=deg a_O+2.

For EVERY real r (in particular every r in [-2,2]), the raw perturbation
z-r+beta a_O has degree h. Therefore the shifted center trace T_C-r
has strictly positive supported defects at every n>=h+2. Its y-smoothed
version has strictly positive supported defects at every n>=h+3.
Both conclusions are uniform in r and N. The only unsupplied trace
signs lie in the fixed bands 0..h+1 raw and 0..h+2 smoothed.

This is an arbitrary-origin analytical consequence, rather than a
finite-state check. It applies at BOTH children whenever their transported
smaller origin is ordinary. The result concerns defects; positive support
in the small perturbation band remains a separate premise if it is needed
for a full packet.

The raw endpoint-1 case is supplied separately by the existing pure
prefix theorem in `../continuation_prefix.md`: R_m(z) is strict raw folded
TP2 for every m>=1. Here a_O=0 and Z_N=R_(N-1)(z). For N>=3 its degree
is at least 2, so the same y^2 strict-product lemma applies. At N=2 the
base beta R_1(z)=6y^2P has exact half-row (60,48,24,6) and defects
(432,576,252,36), all positive. Thus the raw shifted-center-trace
corollary holds also at every retained endpoint-1 record, with h=1:
strict supported defects at all n>=3, uniformly in r and N>=2.
Together these arguments cover raw upper-band trace defects at BOTH
children. The smoothed statement in this corollary is restricted to
ordinary origins; no smoothed endpoint-1 extension is needed here.

## 3. A smaller original-proxy band once a frozen source is signed

Using X=1+y a_X and C=1+yB, put

    J=y(t-2), L=3y^2 X P,
    b=y(1+z a_X), K=2 X P^2.

Then the original proxy has the exact center split

    Q=J B+b, Pi=L B+K.                                (6)

Substitute the exact anchored origin (3):

    Q=J Z_N+q0, Pi=L Z_N+p0,
    q0=J a_O+b, p0=L a_O+K.                            (7)

The four polynomials J,L,q0,p0 are fixed when the endpoint origin is
retained. They do not depend on N. In particular the correction band
below does not grow with the current center degree. For canonical
nonzero anchors the band endpoint is deg X+deg a_O+3, by positive
leading coefficients. For a_O=0 it is deg X+2.

**Universal sufficient subgate.** Suppose Z_N has a strict folded
kernel and positive Fourier interval support, and the fixed positive
rows H(J),H(L) have strictly positive adjacent LR minors throughout
0<=i<=deg J, with deg L=deg J+1. Then

    W_n(Q,Pi)>0 for every n>max(deg q0,deg p0)
                 through deg Q.                       (8)

Thus it remains to check only 0<=n<=min(deg Q,max(deg q0,deg p0)).
This is an exact universal reduction, not a claim that its frozen source
has been proved at every new endpoint.

Proof: beyond the stated band both anchor rows vanish at n,n+1, so
W_n(Q,Pi)=W_n(JZ_N,LZ_N). By Cauchy--Binet the latter is a sum of
nonnegative base LR minors times ordered minors of K_Z. Choose the
adjacent base columns i,i+1 with i=min(n,deg J). Their base minor is
strict. Their kernel minor is strict whenever |n-i|<=deg Z_N.
To see this directly in characters, for i=0 it is delta_n(Z_N);
for i>0 multiply T_Z by R(C_i,C_(i+1))=chi_(2i)(U)+chi_(2i)(V).
The positive defect coefficient delta_|n-i|(Z_N) contributes to the
selected chi_(2n)(U)chi_0(V) coefficient by Clebsch--Gordan. The degree
bound on n gives |n-i|<=deg Z_N. This proves (8), including terminal
support; no cancellation through an LR multiplier is used.

More generally, weak source LR plus its positive terminal minor is
sufficient if deg Z_N>=deg J: retain i=deg J for every n. That kernel
minor is strict throughout 0<=n<=deg J+deg Z_N by the same argument.

The smoothed source has the compact exact expression

    L=P J+rho, rho=yP^2, H(rho)=(14,11,5,1),
    W_n(J,L)=delta_n(J)+W_n(J,rho).                    (9)

Its only adjacent corrections are

    n=0: delta_0(J)+11 j0-14 j1,
    n=1: delta_1(J)+5 j1-11 j2,
    n=2: delta_2(J)+j2-5 j3,
    n=3: delta_3(J)-j4,
    n>=4: delta_n(J).

Here K_J itself is not a premise of MP_sharp(t,b0,b1): the packet
shifted-trace gate is raw, and y cannot be silently multiplied into it.
If K_J is known, (9) reduces source LR to four explicit boundary
inequalities. The actual endpoint X=P has J row (26,21,11,3), source
adjacent minors (72,81,45,9), all strict. The endpoint X=1 has
source row (30,-12,6), so this particular common reduction correctly
excludes that endpoint. No assertion that all nonboundary endpoints
satisfy (9) follows from these two evaluations.

## 4. Relation to the weaker D proxy

With E=y e, D=EM and F=E-XP,

    D-PQ=V+F M, V=PX+P^2 C.                            (10)

The useful proposed sufficient comparison R(Q,D-PQ)>=_char0 would
imply R(Q,D)>=T_Q and hence strict Q<D from the proved strict Q.
Formula (10) does not sign that comparison even if F has nonnegative
Fourier entries. The anchored identity (3) retains the correlation for
any attempt to dominate this source; it does not turn entrywise F
positivity or a_O<=e into an LR statement.

## 5. Scope and remaining premises

| Obligation | Outcome |
| --- | --- |
| ROOT anchored identities | Exact, both endpoint origins |
| Arbitrary canonical BOTH anchored-register transport | PROVED, no Fricke or sign hypothesis needed for the algebra |
| Ordinary certified prefix Z_N strict raw/y, N>=2 | PROVED by existing sharp resolvent machinery |
| Anchor effects on normalized-center kernels | Exact fixed low-band reduction; signs OPEN |
| Shifted center trace at BOTH children | Strict raw defects for n>=h+2, including endpoint-1 with h=1; ordinary smoothed defects for n>=h+3; uniform in r,N; low-band signs OPEN |
| Original proxy outside the fixed origin band | PROVED conditional on the frozen smoothed source gate |
| Initialization/BOTH signs of that source and residual band | OPEN |
| Weaker Q<D / full strict Local TP2 | OPEN |

`proxy_algebra_verify.py` independently replays the universal anchor
cancellation in a formal four-variable ring, the prefix/division identities,
BOTH register initialization and retention at root and first-level records,
the fixed support-band equality, and the two source examples. These are
exact identity checks and finite theorem seeds, not an infinite sign scan.
The independent audit lane checked the prefix indexing, canceled-residue
argument, common-product strictness at n=0 and the terminal index, and
reported PASS. The source values in this final note match the replay.
