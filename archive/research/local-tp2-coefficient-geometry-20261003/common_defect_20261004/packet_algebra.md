# A structural obstruction to combining the two certified orientations

Status: **proved universal obstruction**, including canonical Fricke states
and the entire parent parameter box. It does not refute MP_sharp preservation
or Local TP2. No complete child interior compensation has been proved.
All earlier directories remain read-only.

The audited tensor selector theorem is imported from
`../common_midpoint_20261004/network_relative_character.md`. The canonical
degree/ordinary bounds and packet run theorem are imported from
`../fulltree_20261004/invariants_normalized_state.md` and
`../common_midpoint_20261004/audit_minimal_packet.md`. All displayed algebra
is replayed by the independent standard-library exact verifier
`packet_algebra_verify.py`; fixed root examples normalize the all-index
proof, rather than supplying it.

## 1. A universal degree-separation theorem

Let f,g have positive Fourier interval support, degrees D and E, and positive
leading coefficients. If E>=D+2, then their polarized mixed tensor is NOT
character-nonnegative. In fact, rows (0,1) and columns

    k=D+1, l=D+2

give the exact witness

    Sel_(k,l)J(f,g)=-lc(f)H(g)_(D+2)<0.                              (1)

Proof: write h=H(f),a=H(g), and q=H(xf),b=H(xg). Polarization of the
audited row-(0,1) minor gives

    Sel_(k,l)J(f,g)=h_k b_l+a_k q_l-h_l b_k-a_l q_k.

At the specified columns h_k=h_l=q_l=0 and q_k=h_D=lc(f). Positive
interval support gives a_l>0. This proves (1), with character index

    (k+l-1,l-k-1)=(2D+2,0),

and the equal transposed coefficient. This is an actual ordered mixed
minor, not a negative ordinary power coefficient or scalar evaluation.
No TP2 hypothesis on either f or g is needed. Thus adding their individual
strict kernel properties, Fricke, ordinary positivity, or LR comparisons
cannot make this forbidden mixed sign true.

There is also an exact quantitative mixture obstruction. At j=D+1,

    delta_j(g+epsilon f)=delta_j(g)
                         -epsilon lc(f)H(g)_(D+2).                  (2)

There is no quadratic epsilon term because all entries of f at j,j+1,j+2
vanish. If g is strict, the mixture becomes non-TP2 for every
epsilon>delta_j(g)/(lc(f)H(g)_(D+2)). Thus even individually strict
positive kernels of these degrees cannot form a cone closed under
arbitrary positive mixing. This says nothing about a particular bounded,
correlated canonical child mixture; that mixture needs a quantitative
compensation proof.

## 2. The canonical paired seeds ALWAYS satisfy the forbidden degree gap

Put z0=2x+3, y=x+1 and t=z0+3y^2 a. Let dt=deg t>=1 and de=deg e.
The canonical degree ordering gives de>deg a when a is nonzero. With

    g=(t-2)e+k+r, s=tg-r, c=e+g+s,

the positive leading terms and ordinary remainder bound imply

    deg g=dt+de,
    deg s=deg c=2dt+de,
    dc-de=2dt>=2.                                                   (3)

For a=0 the same formulas hold with dt=1, k=1 and deg r<=de. Thus

    J(e,c) is character-negative at (2de+2,0),                      (4)

for EVERY canonical state. Its coefficient is
-lc(e)H(c)_(de+2), which is strictly negative by positive interval
support. Root y*e is not a cone, but that exception is irrelevant to
(4); even a proof of both seed cones at a nonroot state could not supply
the missing seed compatibility.

This answers the proposed seed-bootstrap shortcut precisely: actual seed
strictness would be useful information, but it cannot turn the two paired
seeds into mutually compatible tensor sources. A LR order of the seeds
also cannot remove the exact witness (4).

## 3. Even the fully certified parent single blocks are incompatible

Assume the parent carries both current packets

    MP_sharp(T,c,e), MP_sharp(T,e,c).

For ANY r,s in [-2,2], define its two individually certified strict blocks

    f=L_s,reverse=e(T-s)+c,
    g=L_r,forward=c(T-r)+e.

Their degrees are D=de+d and E=dc+d, where d=deg T. The strict seed degree
bound makes these degrees independent of the parameters. By (3), E-D is
at least two. Applying (1) therefore proves

    J(L_s,reverse,L_r,forward) NOT>=_char 0                         (5)

for **every parameter pair**, at the exact witness

    (k,l)=(de+d+1,de+d+2),
    coefficient=-lc(eT)H(L_r,forward)_(de+d+2)<0.

The identical argument applies independently to the smoothed blocks yf,yg:
their degree gap is unchanged, and all coefficients in their interval are
positive by the two certified parent packets. The negative character there
is (2D+4,0). Thus the failure is present despite strict raw AND y-mode
certification of every block being combined.

Consequently the paired MP_sharp hypothesis is two certified orientations,
not one jointly mixed-positive collection. A proof that expands a child
into parent forward and reverse blocks and demands every cross-orientation
mixed tensor nonnegative is structurally impossible. The parent's own
within-orientation mixed axiom compares equal-degree blocks and is not
contradicted by (5).

The SAME obstruction applies to every same-index pair of certified parent
origin runs, for all N>=1:

    q_N,F=c U_N(T)+e U_(N-1)(T),
    q_N,R=e U_N(T)+c U_(N-1)(T).

Both are strict raw/y by MP_sharp, but their degrees differ by 2dt, so
J(q_N,R,q_N,F) has the negative witness (1). This is an infinite-index
statement derived from degree formulas, not a finite run replay.

## 4. Shifted-trace factors do not homogenize the two orientations

The canonical degree of T is d=dt+de+2, and

    2<=dc-de=2dt<d.                                                (6)

For a>0 this uses dt=deg a+2 and de>deg a; for a=0 it uses d=de+3>2.
Multiplying either orientation by any finite product of shifted traces
T-lambda changes its degree by an integer multiple of d. Hence no choices
of such factors can make a forward-origin degree equal a reversed-origin
degree. Their degrees have different residues modulo d.

When their resulting degree difference is at least two, (1) again forbids
joint mixed positivity. A difference of exactly one is not covered by (1)
and is not declared impossible. This distinction matters: the argument
does not exclude a more elaborate equal-degree construction using OTHER
canonical factors, nor cancellation among several signed sources. It does
exclude a simple transfer of the ordinary positive-resolvent proof to a
joint paired family by adding shifted-trace factors alone.

## 5. Exact ROOT witnesses and relation to Fricke compensation

The initial canonical root satisfies Fricke and has the audited paired
MP_sharp packets. It has

    e=1,
    c=4x^2+14x+12,
    T=6x^3+24x^2+32x+15.

Thus J(e,c) has coefficient -4 at characters (2,0). At r=s=-1, the two
strict parent single blocks have degrees 3 and 5 and positive leading
coefficients 6 and 24, so their mixed coefficient at columns (4,5),
characters (8,0), is -144. In y mode columns (5,6), characters (10,0),
give the same -144. The verifier checks these as polynomial identities
in independent r,s, so the root single-block obstruction covers the
FULL continuous parameter square, not just the displayed specialization.

The existing child factorization remains exact:

    B'_sharp=A K+omega F,
    F=J(B,b0 z)-J(Bz,b0), z=T'+1.

The preceding theorem identifies a second obstruction to discarding
correlations: even the parent-certified blocks that might be used to
dominate that flux cannot be combined by asserting sourcewise cross
compatibility. Fricke's one-variable paired Cassini identity is retained,

    c^2+Tce+e^2=C^2(1+3(C-1)/y),

but (4)-(5) hold on exactly this surface. It cannot imply those false
cross-character signs. Any full interior proof must obtain compensation
within the trace-weighted equal-degree expressions themselves, or prove
a quantitative bound on the combined signed expression.

## 6. ROOT / BOTH / TARGET scope and the precise remaining blocker

For completeness, the independently reproduced actual monotonicity
obstruction uses the third short child of the normalized root. Let
z0=2x+3 and R_m=sum_(j=0)^m U_j(z0). Its reverse child seed and anchor are

    n=R_3=z0^3+z0^2-z0,
    B=R_4[z0+1+3y^2 R_3]+R_2.

At p=B-3n=L'_2, the exact adjacent mixed coefficient is

    Sel_(3,4)J(p,n)=[chi_6(U)chi_0(V)]J(p,n)=-6386912.              (7)

This index j=3 equals deg n, so it is inside the proposed low-band
monotonicity test. Writing E(theta)=delta_3(B-theta n), one has
delta_3(n)=64 and E'(3)=-Sel_(3,4)J(p,n)=6386912>0. In fact
E'(theta)=6386528+128theta>0 throughout [-1,3], so this defect's
minimum occurs at r=-2, not r=2. This falsifies the proposed common
monotone-decreasing endpoint shortcut. It does NOT assert a negative
single-block defect or an unproved full packet at this third child.
The state is produced by three exact normalized short mutations and
satisfies Fricke; the verifier checks its tuple and (7) directly.

ROOT paired packets and both first-child packets remain proved by earlier
continuum certificates. This note proves a universal obstruction at those
same valid states, not a packet counterexample. BOTH child support/degree,
trace central and upper bands, reverse upper single bands, and mixed outer
layers remain the prior proved subgates.

No complete child single-block or interior mixed gate has been obtained
here. The attempted structural reduction to a jointly compatible paired
origin collection is falsified for arbitrary canonical parents, for all
parameters and infinitely many certified run indices. The root's proposed
single-pencil monotonicity shortcut was found false by the adversarial
lane and independently replayed in (7); it is not used as a premise.

The exact blocker is not a missing assertion of seed positivity: those
seeds, and even individually strict certified blocks, have forced negative
cross-orientation character minors. A successful common induction needs a
quantitative compensated inequality that retains the actual trace/seed and
Fricke correlations. Full new-center paired MP_sharp preservation, direct
Q<D preservation, and full-tree strict Local TP2 remain OPEN.
