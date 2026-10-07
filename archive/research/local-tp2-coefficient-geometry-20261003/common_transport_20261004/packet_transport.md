# Both-child origin-certificate transport and narrowed midpoint blocks

Status: proved conditional transport of a finite certificate subsystem;
proved uniform fixed-trace kernel-block transport from an enlarged origin
packet. The FINAL compressed state theorem is
`packet_expanded_predicate.md`: only changed-center paired MP_2 and
regular-edge strict proxy preservation remain OPEN. M is supplied by
the current paired packet, so it is not an independent third gate in
that expanded predicate. No full-tree Local TP2 theorem is claimed.

All former work is read-only. Foundations used are the normalized mutation
identities, the signed/paired seed identities in
`../common_closure_20261004/invariant_spectral_packet.md`, folded TP2
product/Cauchy--Binet closure, and the finite-dimensional symmetric Jacobi
resolvent used in the prior one-turn and reversed-block theorems. The
new exact reproducer is self-contained.

## 1. One formula for both changed traces and paired seeds

Write beta=3y^2, T=M-1, c=c_A=e+g+s, and A=e+g,B=g. Thus A=B+e,
t=T-beta A, and tau=t+beta e=T-beta B. The current paired relation is
c_B=c+Te. For sigma=0 (short) or sigma=1 (long), define

    n_sigma=g+(1-sigma)e,
    u_sigma=T-beta n_sigma=t+sigma beta e,
    v_sigma=c+sigma Te-n_sigma.

Then the child's complete paired tuple (center trace, forward seed,
endpoint difference) is exactly

    (T',c_A',e')=
      (T+beta v_sigma, (u_sigma+1)v_sigma+(1-2sigma)e, n_sigma).

Here v_0=s and v_1=s+d. In particular the two tuples are

| Child | new T | new c_A | new e |
| --- | --- | --- | --- |
| short | T+beta s | e+(t+1)s | e+g |
| long | T+beta(s+d) | (tau+1)(s+d)-e | g |

These identities hold off the Fricke surface. They retain the ancestry
quantity g rather than substituting arbitrary rows. It can also be
reconstructed from the current paired data by the exact division

    (T-2)(e+g)=C(3C-2)-c-e.

Hence the pair (T,c,e) with canonical divisibility determines its missing
boundary quantity; a generic unrelated triple lacks this information.
The formulas do not imply folded TP2 of their sums or differences.

## 2. Explicit finite origin registers

For an endpoint F, let tau_F=3yF-x. A register consists of a fixed seed
pair (b0,b1), this trace, and one integer N>=1. Its polynomial sequence is

    f_j=b0 U_j(tau_F/2)+b1 U_(j-1)(tau_F/2),  U_-1=0.

The origin seed is certified by positive midpoint MP_2 (Section 4),
including smoothed blocks and its direct relative-minor condition. The
stronger independent-u Packet_2 from the prior campaign suffices but is
not necessary. The conditional Jacobi implication proves that y f_j is
folded TP2 with strictly positive supported defects for every j>=1.
The seed/trace are kept fixed; only N changes. No quantifier over future
canonical states occurs in the register predicate.

At one current normalized state require TWO identities in each register:

| Endpoint register | previous term | actual outgoing term |
| --- | --- | --- |
| smaller X, N_X>=2 | f_(N_X-1)=g | f_(N_X)=s |
| larger Y, N_Y>=1 | f_(N_Y-1)=e+g | f_(N_Y)=s+d |

The previous-term identity is indispensable: one outgoing equality alone
does not identify the correct canonical recurrence boundary.
The stronger smaller-index restriction ensures that its previous term
itself is covered by the packet run-kernel theorem.

For the fixed endpoint 1, use the separate established pure-boundary
register f_j=U_j(z/2), with the known smoothed cone theorem for j>=1.
This register can only be retained or dropped; a new endpoint is never 1.
At the root the smaller register is of this type with N_X=2. The root
larger register has tau_Y=3y(x+2)-x, b0=2(x+2), b1=0, N_Y=1. These are
initialization data imported from established foundations; this campaign
does not redo the root proof.

## 3. BOTH certificate components close under actual mutation

Assume the current two registers and the current positive paired packets

    MP_2(T,c,e),  MP_2(T,e,c).

For a short mutation:

1. Retain the X origin tuple and replace N_X by N_X+1. The new smaller
   endpoint is X, and its required previous/current terms are exactly
   s and ts-g. These are its actual g' and s'.
2. Initialize the new larger endpoint C with origin (T,c,e) and index 1.
   Its previous term is f_0=c=e'+g'. Its outgoing term is
   f_1=Tc+e=(s'+d') at the short child.

For a long mutation:

1. Retain the Y origin tuple and replace N_Y by N_Y+1. The new smaller
   endpoint is Y, and its previous/current terms are exactly
   s+d and tau(s+d)-(e+g), its actual g' and s'.
2. Initialize the new larger endpoint C with REVERSED origin (T,e,c)
   and index 2. Its previous term is f_1=Te+c=c_B=e'+g'. Its outgoing
   term is f_2=e(T^2-1)+Tc=(s'+d') at the long child.

The two new-endpoint identities follow directly from the paired seed
relations; the exact verifier checks them against each child's normalized
mutation, not merely along a special path. The retained-register step is
the homogeneous gap recurrence, with the two required old identities
fixing its boundary. Every outgoing register index is at least 1, so the
conditional packet kernel theorem applies, including central and terminal
indices. The short new register uses f_0=c only as an identity, without
asserting that yf_0 is a cone. The long register starts at f_2, avoiding
the reversed origin's possible y f_0 exception.

After either retention the new smaller register index is at least 2:
it is N_X+1 in the short case and N_Y+1 in the long case. The new larger
register indices 1 and 2 satisfy their lower bound. Thus the exact index
restrictions are preserved at BOTH children.

### Consequence and precise remaining obligations

This proves both-child preservation of ALL origin-register identities and
validity of their origin certificates. In particular both parent actual
outgoing gaps have folded TP2 kernels, and therefore BOTH children's
actual G' do: G'_short=S=yf_(N_X), G'_long=S+D=yf_(N_Y). It also certifies
both outgoing gap kernels at each child from the transported registers.

This is a noncircular subsystem closure conditional on the parent's
current paired packets. It does **not** prove that the new state has its
own new-center paired packets. If a full state predicate contains P_Q,
the current paired packets, and these two registers, the register portion
has proved SHORT and LONG, and its actual K_G gate has no additional
analytic transport obligation. Its new paired packet (which supplies
K_M) and regular-edge strict proxy gates still require proofs, as made
precise in the expanded predicate note. Thus the full-tree conclusion remains
open, and this note does not claim that the previous three analytic gates
have vanished without strengthening the state.

## 4. The minimal midpoint packet

Independent u in the prior H(r,s,u) box is stronger than the Jacobi mixture
proof needs. For a radius R>0 define

    L_r=b0(T-r)+b1,
    H_rs=b0(T-r)(T-s)+b1(T-(r+s)/2).

A midpoint packet, written MP_R, requires positive interval support and
strict folded defects of L_r,yL_r; folded TP2 of H_rs,yH_rs;
nonnegative positive-interval shifted traces with folded TP2 for
|r|<=R; and the DIRECT ordered inequalities

    det K_H>=R^2 det K_|b1|,
    det K_(yH)>=R^2 det K_(y|b1|).

The seeds may have the signed form allowed by the prior packet theorem,
provided deg b1<deg b0+deg T, and all displayed block rows are nonnegative.
For positive origins this sign qualification is unnecessary.

For spectral roots r,s in [-R,R], the exact midpoint polarization is

    mixed=2 det K_H-(r-s)^2 det K_|b1|/2>=0.

This follows from the direct relative bound when the reference minor is
positive, and from TP2 of H when it is nonpositive. Thus a midpoint packet
has exactly the compatibility needed for any symmetric-matrix positive
resolvent whose spectrum lies in [-R,R]. No independent u box is needed.

## 5. Uniform fixed-trace block transport with R=5/2

Let the fixed origin seeds be (b0,b1), and put

    q_N=b0 U_N(T/2)+b1 U_(N-1)(T/2),
    L_N^r=q_N(T-r)-q_(N-1),
    H_N^rs=q_N(T-r)(T-s)-q_(N-1)(T-(r+s)/2).

Here q_N is defined for N>=0 and q_-1=-b1, so the N=0 displayed blocks
are exactly the origin L and midpoint H.

Assume the origin midpoint Packet_(5/2). Then for EVERY N>=0 and every
r,s in [-2,2], the L_N,H_N blocks and their y multiples have folded TP2
kernels, with strict supported defects. This conclusion proves kernel
block preservation under arbitrary retained-endpoint advances; it does
not assert the changed-reference relative-minor bound for the advanced
seed -q_(N-1).

### Single blocks: an ordinary Robin path

Define p_j^r=U_j-rU_(j-1). It is the characteristic polynomial of a
j-vertex tridiagonal symmetric path, off-diagonal entries 1, zero diagonal
except the last value r. Direct expansion gives

    L_N^r=b0 p_(N+1)^r+b1 p_N^r.

The smaller polynomial is the principal minor deleting the first vertex.
Its positive resolvent therefore reduces L_N to the origin L blocks at
the path's eigenvalues.

### Midpoints: a forked path

Write A=(T-r)(T-s), u=(r+s)/2 and

    chi_N=U_N A-U_(N-1)(T-u), N>=0.

For N>=1 this is the characteristic polynomial of a symmetric matrix
with N stem vertices, two leaf vertices of diagonal values r,s, stem
off-diagonal entries 1, and the two final stem-to-leaf weights 1/sqrt(2).
Indeed chi_0=A, chi_1=T A-T+u; attaching another zero-diagonal stem
vertex gives chi_N=T chi_(N-1)-chi_(N-2). Deleting the first stem vertex
has characteristic polynomial chi_(N-1). Therefore

    H_N^rs=b0 chi_N+b1 chi_(N-1), N>=1,

has the same positive-resolvent reduction to the origin L blocks.
The N=0 midpoint is an origin block and needs no matrix reduction.
Its strict supported defects follow even if the stated origin H gate
is only weak TP2: F=L_r(T-s) and G=L_s(T-r) are strict cone products
of the same degree, their polarized mixed minor is nonnegative by the
packet relative bound, and H=(F+G)/2. Positive diagonal terms prove
strictness, including the terminal index. The y mode uses yL and yH
and the same polarization, so no y cone-preservation assumption enters.

### Exact uniform spectral bound

At R=5/2, the two leaf pivots of RI-J are R-r,R-s>=1/2. Eliminating
the leaves makes the last stem pivot

    R-(1/2)/(R-r)-(1/2)/(R-s)>=1/2.

Each successive stem pivot is R-1/p>=1/2 whenever p>=1/2. Thus every
pivot is positive, so RI-J is positive definite at every finite stem
length. The same argument handles the Robin path with its last pivot
R-r>=1/2. Applying a bipartite diagonal sign change to -J gives the
same matrices with leaf potentials -r,-s, so RI+J is also positive
definite. EVERY eigenvalue lies strictly between -5/2 and 5/2.

The fork can have zero first-coordinate residues, for example the
antisymmetric leaf mode when r=s. The spectral theorem gives nonnegative
residues summing to 1; retain positive residues and the corresponding
common polynomial factors. Repeated eigenvalues cause no difficulty:
assign each pole's total residue to one copy and zero to the other
copies. All needed factors remain shifted traces in the same spectral
box, and pairs with equal eigenvalues have zero difference.

Expanding b0 chi+b1 chi_minor or b0 p+b1 p_minor into these positive
resolvent summands leaves origin L blocks on diagonals and the exact
midpoint-compatible pair on every mixed term. Folded product closure
and Cauchy--Binet prove all kernel assertions. Every summand has the
same degree and positive interval support by the strict origin degree
condition, so positive diagonal terms prove strict supported defects
at index zero, all internal indices, and the terminal index. The y
mode uses yL and yH explicitly; multiplication by y is not assumed to
preserve the cone.

### What is not proved

The old Packet_2 does not imply this larger midpoint Packet_(5/2).
Nor does the larger origin packet prove its own full parameter-box
preservation if parameters at the advanced seed are also allowed up to
5/2: the corresponding spectral bound increases. Carrying a fixed origin
and integer advance index avoids that drift for the derived [-2,2]
blocks. A new origin at a changed center still requires its packet proof.

The direct relative-minor bound against the ADVANCED reference
|q_(N-1)| is not supplied by cone membership alone. This remains an exact
missing inequality; no coarse strength-times-domination criterion is
silently substituted for it.

## 6. A precise obstruction to the overstrong independent-u box

The abstract complete independent-u Packet_2 is not automatically closed
under the seed advance (b0,b1)->(Tb0+b1,-b0), even with both smoothing
conditions at the parent. Take

    T=x+41/12, b0=x+5/2, b1=0.

Every T-r is strict folded TP2 for r in [-2,2]: its half-row is
(41/12-r,1), with minimum central defect 1/144. Both b0 and yb0 are
strict folded TP2; yb0 has half-row (9/2,7/2,1), central defect 1/4.
All parent L and H, including y multiples, are therefore strict products
on the full parameter box. The relative reference is zero.

After one advance, the independent corner (r,s,u)=(2,2,-2) has

    H_new=b0[T(T-2)^2-(T+2)],
    delta_0(H_new)=-1939833799/11943936<0.

This is an abstract counterexample, not a canonical or Fricke-completed
state and not a paired-positive-packet counterexample. At the REQUIRED
midpoint u=2 the same data give
`delta_0=6959573561/11943936>0`; the exact replay finds every supported
defect positive in both modes for that midpoint. Thus the independent-u
obstruction is specifically a reason to narrow the predicate, not a
refutation of the minimal midpoint transport theorem.

## Obligation ledger

| Component | ROOT | SHORT | LONG | Consequence |
| --- | --- | --- | --- | --- |
| Two origin registers + current paired Packet_2 | Existing initialization imported | Register identities/certificates preserved | Register identities/certificates preserved | Both actual child K_G gates, and their two outgoing kernel certificates |
| Origin midpoint Packet_(5/2) with fixed-trace index | Not reproved here | Retained-endpoint L/H kernel gates proved for all advances | Same retained-endpoint theorem | Kernel blocks only; changed reference and changed center remain open |
| Final expanded MP_2 + packet/register package | Established augmented root; root-edge proxies already known | New paired origin (supplies M), regular-edge strict proxy remain OPEN | Same | Target implication through P_Q; exact final ledger in packet_expanded_predicate.md |
