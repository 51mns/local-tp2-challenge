# Common signed-seed packet and its exact open closure obligations

Status: exact all-state algebra, a sufficient infinite run-kernel lemma,
and an infinite obstruction to a coarse sufficient gate. No full-tree
closure or Local TP2 theorem is claimed here.

This lane writes only `invariant_*` in the new campaign directory. It
uses the read-only normalized state identities from
`../fulltree_20261004/invariants_normalized_state.md`, the folded product
and all-minor theorems from `../mixed_kernel_all_minor_strength.md`, and
the Jacobi/polarization argument stated in
`../second_turn_20261004/kernels_theorem.md`. The exact reproducer
`invariant_signed_seed_verify.py` imports no parent arithmetic.

## 1. A signed coordinate whose two closures are exact

Put `h=a+e-r`, `eta=h-a=e-r`, `Y=1+y(a+e)`, and

    tau=t+3y^2e=3yY-x,  c=e+g,  q1=s+d.

Here `d=e(t+1+3y^2(e+g))` is the outgoing child difference from the
brief. The identities

    q1=tau*c+eta,
    c^2+eta*q1=Y^2(1+3(a+e))

hold at every canonical state. The stronger second identity is

    c^2+eta*q1-Y^2(1+3(a+e))=-(tau-2)F,
    F=rg-(t-2)e^2-2ke-3a(1+ya)^2.

Thus the only error off the canonical Fricke surface is the displayed
multiple of its residual. The first identity holds off that surface.

Both degree-ordered mutations reset the signed coordinate exactly:

| Mutation | new eta |
| --- | --- |
| short | old e |
| long | -old e |

At the root `eta=0`. At every nonroot canonical state its coefficients
therefore have one sign, determined by the last degree-ordered move.
It is not legitimate to treat `eta` as a positive correction globally.

Fixing the endpoint Y gives homogeneous normalized gaps with boundary
`q_-1=-eta`, `q_0=c`. For every integer N>=0,

    q_N=c U_N(tau/2)+eta U_(N-1)(tau/2),  U_-1=0.

This is an all-state reversal identity. It is not a special-path
assumption and does not itself assert a Fourier inequality.

### Both switches share a more restrictive paired seed

Let Z=a+e+g=(C-1)/y and T=M-1=3yC-x. At the two children, the packet
attached to their common larger endpoint C has the following seeds:

| Child | c seed | signed d0 seed |
| --- | --- | --- |
| short | c_A=e+g+s | e |
| long | c_B=g+s+d | -e |

They are not unrelated positive/negative abstract packets. Since
d=eM, they satisfy

    c_B=c_A+T e.

Fricke supplies the same endpoint correction to both:

    c_A^2+e(Tc_A+e)=C^2(1+3Z),
    c_B^2-e(Tc_B-e)=C^2(1+3Z).

Off the Fricke surface each left side minus the common right side is
exactly `-(T-2)F`; the reproducer verifies every coefficient in the
formal variables x,a,e,r. The first shear relation is unconditional.

For N>=0 their actual subsequent normalized gaps therefore have the
coupled positive forms

    q_N^A=c_A U_N(T/2)+e U_(N-1)(T/2),
    q_N^B=c_A U_N(T/2)+e U_(N+1)(T/2).

The second follows from `TU_N-U_(N-1)=U_(N+1)`; it eliminates the
negative seed only for these actual run polynomials. All displayed
summands are Laurent-nonnegative because the canonical T has ordinary
constant at least 2 and every U_N has roots in [-2,2]. This does not
license cone closure under their sum. The positive paired forms are a
genuine common-switch reduction; their folded compatibility is the
remaining mathematical obligation.

### A proved common coefficient bound on the paired seeds

All inequalities in this paragraph are ordinary coefficientwise.
Put beta=e-a-1. It is nonnegative at the root. Its updates are
`beta_short=beta+g` and `beta_long=g-a-e-1>=r`; since g,r>=1,
**every nonroot state has beta>=1**. The exact identity

    T e-c_A=3y^2e^2+(3x^2+4x)g+e-k+3y^2 beta g

then proves `c_A<=T e`: at every nonroot state,
`3y^2 beta g>=3y^2g>=3y^2k>=k`. At the root beta=0 and e=k=1,
so the difference is `3y^2+(3x^2+4x)z>=0`. Consequently

    c_A<=T e<=c_B<=2T e.

This proof uses only the proved positive normalized recurrence and
ordinary bounds, not a Fourier or cone assertion. The independent
paired audit checks the identities and induction separately.

There is another common ordinary strengthening, `e>=(z-2)a`.
The short move retains a and increases e. For the long move the
exact difference is

    g-(z-2)(a+e)=3y^2a(a+e)+1+za+r>=0.

Both ordinary strengthenings therefore have proved ROOT, SHORT and
LONG, but neither implies Local TP2.

## 2. Frozen noncircular spectral packet

A packet has a trace `tau` of positive degree, a nonnegative seed `c`,
and a signed seed `d0` whose coefficients have one sign and satisfy
`deg d0<deg c+deg tau`. The strict bound ensures that the d0 term
cannot cancel a leading term, including when it is negative. It holds
for both current signed seed pairs and the reversed positive pair
below.
Let `b=|d0|` denote its
coefficientwise absolute value. For independent r,s,u in [-2,2], put

    L_r=c(tau-r)+d0,
    H_rsu=c(tau-r)(tau-s)+d0(tau-u).

The packet predicate is:

1. Every `tau-r` has a nonnegative positive-interval half-row and a
   folded TP2 kernel.
2. Every `L_r` and `yL_r` has positive interval support and strictly
   positive supported folded defects.
3. Every `H_rsu` and `yH_rsu` is folded TP2 and has positive interval
   support.
4. For every ordered folded minor, `det K_H>=4 det K_b` and
   `det K_(yH)>=4 det K_(yb)`.

These are explicit coefficient-kernel conditions on three current
polynomials and a fixed parameter box. They contain neither Local TP2
nor a quantifier over future canonical states. In particular condition
4 uses the **actual** minor inequalities. It does not replace them by
the failed strength-times-domination estimate of Section 4.

The two natural packets at one normalized state are

| Fixed endpoint | tau | c | d0 |
| --- | --- | --- | --- |
| X=1+ya | t | g | -r |
| Y=1+y(a+e) | t+3y^2e | e+g | e-r |

The sign of d0 is retained in every block. It disappears only in the
reference determinant, where multiplication of a kernel by -1 leaves
its two-by-two determinants unchanged.

## 3. What a packet proves, and why its closure is still open

For r,s in [-2,2], define

    F=c(tau-r)(tau-s)+d0(tau-s),
    G=c(tau-r)(tau-s)+d0(tau-r).

Their midpoint is H with `u=(r+s)/2` and their difference is
`(r-s)d0`. Polarization gives, at every ordered minor,

    mixed(K_F,K_G)=2 det K_H-(r-s)^2 det K_b/2.

The same formula holds after multiplication by y. If the reference
minor is nonpositive, condition 3 suffices. If it is positive,
condition 4 and `(r-s)^2<=16` suffice. Thus the two families are
compatible for either sign of d0.

The positive-residue Jacobi resolvent of U_N now writes
`c U_N+d0 U_(N-1)` as a positive weighted sum of `L_r` times products
of other shifted traces. Diagonal terms are strict cone products;
every pair of distinct terms leaves precisely the compatible F,G
pair after removal of its common factors. Cauchy--Binet proves strict
folded defects for every N>=1, in both smoothed and unsmoothed modes.
All summands have the same degree and positive interval support, so
their positive diagonal contributions also handle every terminal
index. This is the signed-seed version of the cited reversed-block
argument; no arbitrary-positive-mixture closure is used.

For clarity, the degrees in that argument are not an implicit
assumption: every L block has degree `deg c+deg tau`, every H block
has degree `deg c+2deg tau`, and every Nth resolvent summand has degree
`deg c+Ndeg tau`. The strict degree bound on d0 makes these equalities
valid even for reversed positive seeds with deg d0>deg c.

It follows that a packet proves all future gaps on its current fixed
endpoint run. This implication does **not** prove packet closure.
Advancing a fixed endpoint changes seeds by

    (c,d0) -> (tau*c+d0,-c).

Its next single block is

    c[tau(tau-r)-1]+d0(tau-r).

The polynomial `tau(tau-r)-1` has roots
`(r+-sqrt(r^2+4))/2`; at r=2 its positive root is `1+sqrt(2)>2`.
Consequently the old [-2,2] factor box does not automatically cover
even the next single blocks. This is a precise gap in a resolvent-only
closure proof, not a counterexample to actual packet preservation.
Changing endpoints additionally changes the trace and couples new
seeds through the Fricke identity in Section 1.

### Explicit obligations

| Obligation | Status |
| --- | --- |
| ROOT for both naive packets | False: fixed-X packet fails below. |
| ROOT with an exact a=0 boundary disjunct | Its algebra is available; fixed-Y root packet follows from products as detailed below, but a complete two-child invariant still needs the nonboundary packet gates. |
| SHORT | Seed recurrence exact; preservation of all packet blocks and direct relative minors remains open. |
| LONG | Seed reset and changed-trace Cassini identity exact; preservation of all packet blocks and direct relative minors remains open. |
| IMPLIES TARGET | Packet alone proves actual gap kernels; strict Local TP2 still requires the independently isolated LR companions and final proxy comparison. |

The exact pure-boundary formulas are `a=0,e=T_m,r=U_m,g=U_(m+1)`.
Keeping this boundary as a disjunct is a root-inclusive state design,
but it supplies no excuse to omit either closure obligation after a
positive a appears.

For the fixed-Y root packet, `tau=3x^2+8x+6`, `c=2(x+2)`, and d0=0.
Every tau-r is a strict folded factor by the constant-a=1 case of
`invariant_shifted_trace_lemma.md`. Both c and yc are strict: their
half-rows are (4,2) and (8,6,2). Hence all L and H blocks, including
their y multiples, are cone products. The reference b is zero, so
the direct relative-minor gates follow from TP2 itself over the entire
parameter box. This is a continuum root proof for that packet, not
a corner scan.

The naive fixed-X packet already fails at the root, at
`(r,s,u)=(2,2,-2)`:

    H=z(z-2)^2-(z+2)=8x^3+20x^2+12x-2,
    H(H)=(38,36,20,8),  delta_0=-388.

This is an actual canonical counterexample to that packet definition,
not to the original Local TP2 target. Falsification's boundary-aware
corner passes for positive a are bounded evidence only; they are not
ROOT/SHORT/LONG proofs over the parameter continuum.

## 4. Infinitely many actual states defeat the coarse scaled gate

At the pure-short state of depth m, `r=U_m(z/2)` and
`s=U_(m+2)(z/2)`. Consider the sufficient criterion

    s is lambda-strong, H(s)>=alpha H(r), lambda alpha>=8 H(r)_0,

or its y-smoothed counterpart. Every admissible lambda is at most the
terminal leading coefficient `2^(m+2)`. Every admissible alpha is at
most the central ratio. Because

    U_(m+2)<=z^2 U_m

coefficientwise and U_m has decreasing half-row,

    alpha<=H(z^2 U_m)_0/H(U_m)_0<=17+24+8=49.

The same bound holds after multiplication by y, since `yU_m` is
character-positive and hence decreasing. The elementary recurrence
proves `U_m>=2^m y^m` coefficientwise: U_m>=U_(m-1) implies
`U_(m+1)>=(z-1)U_m=2yU_m`, starting with U_0=1,U_1=z.
Central trinomial coefficients are maximal, so

    H(U_m)_0>=6^m/(2m+1),
    H(yU_m)_0>=3*6^m/(2m+3).

Therefore the sufficient gate is impossible in the unsmoothed mode
whenever

    3^m>(49/2)(2m+1),

and in the smoothed mode whenever

    3^m>(49/6)(2m+3).

The first inequality holds exactly at m=6, the second at m=5. Each
propagates because multiplying the left side by 3 exceeds the ratio
of the consecutive linear right sides. Thus the coarse gate fails at
**every m>=6 unsmoothed and every m>=5 smoothed**, on actual reachable
states. The reproducer also computes optimal lambda and optimal alpha
for m<=12; its earlier failures agree with the independent lane.

This theorem does not refute `det K_s>=4 det K_r` or its smoothed
version. Those direct inequalities remain plausible, and independent
bounded enumeration includes millions of passing ordered minors even
at the coarse-gate failures. Replacing actual minor domination by
strength-times-domination would discard precisely the useful margin.

| Coarse-gate obligation | Status |
| --- | --- |
| ROOT | Proved in both modes: optimal (lambda,alpha) are (2,16) unsmoothed and (4,32) smoothed, with b0=1. |
| SHORT | False on actual states: first reproduced failures m=4 unsmoothed and m=3 smoothed; the theorem above gives entire infinite tails. |
| LONG | Irrelevant as a common closure candidate after SHORT is refuted; no closure claim. |
| IMPLIES TARGET | Supplies the relative-minor lemma, not Local TP2 by itself. |

For the weaker direct `det K_s>=4 det K_r` predicate, ROOT follows
from the coarse gate. Both mutation closures remain open. Direct
domination is therefore retained as a candidate packet input, rather
than incorrectly discarded with its overstrong sufficient criterion.

## 5. A root-proved paired positive packet, with both closures open

The common-switch relation removes the negative seed for the actual
long run. This gives an explicit stronger kernel candidate at each
state: require BOTH packets

    Packet(T,c_A,e),   Packet(T,e,c_A).

This is a predicate on one positive seed pair in both orientations.
It neither assumes any future target nor treats unrelated positive
mixtures as compatible. The forward packet yields q_N^A for N>=1;
the reversed packet yields q_N^B at its outer index N+1>=1, including
q_0^B. The conclusion for q_0^A=c_A is not needed for this implication.

The reversed packet meets the amended strict degree condition. If
a>0, write da=deg a,de=deg e. Degree orientation gives de>da, and

    deg c_A=2da+de+4,
    deg(Te)=da+2de+4>deg c_A.

If a=0 then `deg c_A=de+2` and `deg(Te)=2de+3`. Thus
`deg c_A<deg e+deg T` in every canonical state.

The root is an exact match to two existing continuum block theorems:

    (c_A,e,T)=(T_2,T_0,z+3y^2T_1),
    T_0=1, T_1=z+1, T_2=z^2+z.

The trace is `6x^3+24x^2+32x+15`, and c_A is
`4x^2+14x+12`. The forward packet is precisely inner m=1 in
`../recovery_oneturn_closure.md`, with `(A,B,t)=(T_2,T_0,T)`;
the reversed packet is inner m=0 in
`../second_turn_20261004/kernels_theorem.md`, with
`(c,d,tau)=(T_0,T_2,T)`. Both use the entire independent [-2,2]^3
box, both include smoothed blocks, and both prove the ordered relative
minor gate against their own second seed. The root proof is conditional
only on those existing audited foundations, not on a new numerical
scan. Independent paired audit checks this tuple/degree matching.

| Paired positive packet obligation | Status |
| --- | --- |
| ROOT | Proved from the exact forward m=1 and reversed m=0 block matches, conditional on their stated audited foundations. |
| SHORT | Open: the next center trace and paired seeds change; old packet factor boxes do not imply the new packet automatically. |
| LONG | Open for the same reason, with the exact shear/Cassini relation retained. |
| IMPLIES TARGET | Proves only the two specified common-C run-polynomial kernel families. Their connection to the complete common state predicate and all three analytic gates remains open. |

In particular q_0^A=c_A is **not** the short child's actual
center-to-larger-endpoint gap g'=s: it is e'+g'. Hence this paired
packet implication alone must not be reported as all-tree gap-cone
closure. Keeping track of the fixed endpoint when embedding these
run polynomials into the full tree, preserving the packet at both
children, and proving the final strict proxy are separate obligations.
