# The retained origin packet supplies strict K_Q

Status: **proved conditional BOTH-child consequence** of the certified
origin-register subsystem. The strict proxy itself and full-tree Local
TP2 remain **OPEN**. This note does not assume a new-center child packet.

Use y=x+1, P=x+2, t=3yX-x, A=t-2 and M=3yC-x+1. Set

    Q=S-G=AC-xX,  Pi=XPM,  V=PX+P^2 C.

Then Pi=PQ+V. For reflected Fourier half-rows q=H(Q), v=H(V),

    W_n(Q,Pi)=delta_n(q)+q_n v_(n+1)-q_(n+1) v_n,
    delta_n(q)=q_n^2-q_(n-1)q_(n+1)-q_(n+1)^2+q_n q_(n+2).

At zero the convention is q_-1=q_1. Outside upper support every entry is
zero. All statements below include these two conventions.

## 1. A Robin specialization within the existing MP_2 box

Let a fixed origin have trace t and seeds (b0,b1), with certified midpoint
MP_2 as defined in `../common_transport_20261004/packet_transport.md`, or
the weaker sharp MP2_exact in `packet_transport_subgate.md` Section 1.
Write

    f_j=b0 U_j(t/2)+b1 U_(j-1)(t/2), U_-1=0,
    p_N(t)=U_N(t/2)-U_(N-1)(t/2).

For every N>=1,

    f_N-f_(N-1)=b0 p_N(t)+b1 p_(N-1)(t).

Here p_N is the characteristic polynomial of the N-vertex symmetric
path J_N with off-diagonal entries 1 and terminal diagonal entry 1;
all other diagonal entries are zero. Its first-vertex deletion has
characteristic polynomial p_(N-1). For N=1 this deletion is the empty
matrix with characteristic polynomial 1.

For a real vector u one has the exact identities

    2||u||^2-u^T J_N u=u_1^2+sum_(i<N)(u_i-u_(i+1))^2,
    2||u||^2+u^T J_N u=u_1^2+2u_N^2+
                                      sum_(i<N)(u_i+u_(i+1))^2.

Both right sides are positive for every nonzero u. Thus every eigenvalue
r_i lies strictly between -2 and 2. An eigenvector with first coordinate
zero is zero by the tridiagonal recurrence. Consequently the first
resolvent residues w_i are positive and sum to 1, and

    p_(N-1)(t)/p_N(t)=sum_i w_i/(t-r_i),
    f_N-f_(N-1)=sum_i w_i L_(r_i) prod_(j!=i)(t-r_j),
    L_r=b0(t-r)+b1.

This is exactly the origin packet's positive-resolvent setting. For a
pair of eigenvalues r,s the two residual blocks are

    F=L_r(t-s), G=L_s(t-r), (F+G)/2=H_rs,
    F-G=(r-s)b1,
    mixed(F,G)=2 T_(H_rs)-(r-s)^2 T_(b1)/2.

The MP2_exact hypothesis is precisely nonnegativity of this mixed term
in both modes, so the argument applies directly under the weaker final
packet. Alternatively the older MP_2 direct minor bound and TP2 gate make
this mixed term nonnegative: if the reference minor is nonnegative use
(r-s)^2<=16, and if it is negative use T_(H_rs)>=0. Each diagonal term
uses a strict origin L block and cone shifted traces. The exact strict
times weak folded product proof, with the strict factor degree at least
the shifted trace degree, is in `packet_transport_subgate.md` Section 2;
the degree condition below guarantees that comparison at each successive
factor. That proof and Cauchy--Binet therefore give
strict supported folded defects for both f_N-f_(N-1) and its y multiple.
The y mode uses the certified yL and yH blocks, not a presumption that y
is a cone multiplier. The strict origin degree condition
deg b1<deg b0+deg t gives every residue summand the same positive leading
degree; hence its positive diagonal contribution covers index zero,
every interior supported index, and the terminal index.

Thus a certified MP_2 or MP2_exact origin supplies strict K_(f_N-f_(N-1)) and
strict K_(y(f_N-f_(N-1))) for every N>=1. No radius enlargement or
new relative reference is introduced.

## 2. The endpoint-1 exception is independently covered

The special origin f_j=U_j(z/2), z=2x+3, does not carry the ordinary
packet certificate. Its actual indices satisfy N_X>=2. The exact
continuum Bernstein proof in `root_boundary_q.md` proves strict
K_(y[U_N(z/2)-U_(N-1)(z/2)]) for every N>=2. The independent replay is
`audit_boundary_q_verify.py` and its saved result JSON; it checks 22
defects and all 1,813 Bernstein coefficients, including the full
four-congruence factor partition. N=1 is correctly excluded: its
smoothed terminal-adjacent defect is zero.

## 3. Application to both actual children

The smaller register has f_(N_X-1)=g, f_(N_X)=s, N_X>=2, so

    Q=y(f_(N_X)-f_(N_X-1)).

The retained-register transport already proved in
`../common_transport_20261004/packet_transport.md`
gives at the short child the old X origin with index N_X+1>=3, and at
the long child the old Y origin with index N_Y+1>=2. The Y origin is
ordinary and certified; an endpoint-1 origin can only be retained in
the short case. The preceding two theorems therefore supply strict
K_Q at BOTH children, including root edges, from the parent's origin
registers and paired origin-initialization certificates. This does not
use the child's new-center packet, the child's proxy, or a target theorem.

## 4. A rigorous support reduction of the remaining proxy

Let d_X=deg X and d_C=deg C. Canonical degree ordering gives d_C>d_X,
and the only d_X=0 endpoint is X=1. Direct positive-leading-degree
calculation gives

    deg Q=d_X+d_C+1, deg Pi=deg Q+1, deg V=d_C+2.

When d_X>=2, every index n>deg V through deg Q has V_n=V_(n+1)=0.
The strict proxy there is precisely delta_n(Q)>0, now supplied by the
origin theorem. The only potentially unresolved indices are

    0<=n<=min(deg Q-1,deg C+2).

The terminal index is always strictly positive even when not in this
tail. If X=1, lc Q=2 lc C, lc Pi=3 lc C, and the terminal proxy is
6(lc C)^2. If d_X>=1, lc Q=lc Pi=3 lc X lc C and deg V<=deg Q, so the
terminal proxy is (3 lc X lc C)^2. Thus the terminal adds no new gate.

At zero the remaining exact inequality is

    q_0^2-2q_1^2+q_0q_2+q_0v_1-q_1v_0>0.

At interior overlap indices 1<=n<=min(deg Q-1,deg C+2) it is

    delta_n(q)>q_(n+1)v_n-q_n v_(n+1).

These inequalities are still OPEN in general. The existing MP_2
relative reference is b1^2, whereas this correction couples Q and V;
the former does not automatically bound the latter.

In particular W(Q,V)>=0 is an invalid proposed simplification. At
n=deg V<deg Q its value is exactly -q_(deg V+1) lc V<0. The canonical
two-long state (normalized mutations long,long from a=0,e=r=1) has
deg X=2, deg C=7, deg Q=10, deg V=9 and W_9(Q,V)=-7776. This is a
negative correction in an actual state, not a failed strict proxy.

## 5. Fixed-endpoint cancellation and one reduced trace source

The exact fixed-endpoint identity is

    A Pi=3yXP Q+XP[A+Px]
         =3yXP Q+XP[3yX+P(x-1)].

The bracket is 3yX+x^2+x-2. The alternative 3yX+xP-2 has an extra x
and is incorrect. In the ordinary register q=f_N-f_(N-1), one also has

    Q=yq, q=A(C-X)/y+X(3X-2).

These are correlated exact formulas but do not justify convolution
reflection through A or C. For the fixed trace source L=3yXP,

    R(A,L)=T_A+R(A,P^2).

Writing a_n=H(A)_n, its adjacent coefficients are

    w_0=delta_0(A)+4a_0-6a_1,
    w_1=delta_1(A)+a_1-4a_2,
    w_2=delta_2(A)-a_3,
    w_n=delta_n(A), n>=3.

The same MP_2 shifted-trace gate at parameter -2 gives
delta_1(A+4)=delta_1(A)-4a_2>=0. Hence w_1>=a_1>0, and the coefficients
n>=3 are nonnegative from K_A. The exact sources at n=0 and n=2 remain
uncontrolled by this deduction. For the genuine endpoint X=P one has
w_0=-6, so sourcewise nonnegativity still cannot be asserted.

`proxy_robin_verify.py` replays the exact algebra, Robin determinant
recurrences, degree formulas, support reduction example, and trace
source formulas. Finite recurrence replays are sanity checks of the
displayed analytical theorem; they are not its infinite proof.
