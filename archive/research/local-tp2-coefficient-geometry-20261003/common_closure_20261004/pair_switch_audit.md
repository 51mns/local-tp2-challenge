# Independent paired fixed-C switch audit

**Verdict:** the paired seed relations, common Cassini identity and the
ordinary coefficient bound c_A<=Te are proved. The degree extension and
ROOT mapping of the paired positive spectral packets pass the audit,
conditional on the explicitly cited earlier audited foundations.
BOTH-child spectral-packet closure, connection to the complete regular
predicate P_Q, and full-tree Local TP2 remain OPEN.
Earlier frozen pair files are unchanged.

## 1. Exact paired seeds and shared Cassini residual

Use the normalized canonical state, y=x+1,z=2x+3,
t=z+3y²a, k=(1+ya)(1+3ya), g=(t-2)e+k+r,
s=tg-r, Z=a+e+g, C=1+yZ and

    T=3yC-x=t+3y²(e+g), M=T+1, d=eM.

The fixed-C packet at the short child has seed (c_A,+e), and at
the long child seed (c_B,-e), where

    c_A=e+g+s, c_B=g+s+d=c_A+Te.                         (1)

Equation (1) follows from d=e(T+1), without imposing Fricke.
Let the exact normalized Fricke residual be

    F=rg-(t-2)e²-2ke-3a(1+ya)².

Both stronger off-Fricke identities hold universally in Z[x,a,e,r]:

    c_A²+e(Tc_A+e)-C²(1+3Z)=-(T-2)F,
    c_B²-e(Tc_B-e)-C²(1+3Z)=-(T-2)F.                     (2)

The first is the fixed-C version of the endpoint-swapped Cassini
residual audited in `pair_signed_seed_audit.md`, applied to the short
normalized child (a,e+g,g), whose new g is s. The normalized residual
is unchanged by that child mutation. Alternatively, the accompanying
independent sparse verifier expands the displayed left side directly.
The two left sides in (2) are identical after (1):

    (c_A+Te)²-e(T(c_A+Te)-e)=c_A²+eTc_A+e².

Thus on the canonical Fricke surface F=0, both Cassini constants are
exactly C²(1+3Z), with the stated signs.

Write u_N=U_N(T/2), u_-1=0,u_0=1. The two homogeneous runs are

    q_N^A=c_A u_N+e u_(N-1),
    q_N^B=c_B u_N-e u_(N-1)
         =c_A u_N+e u_(N+1), N>=0.                       (3)

The final equality uses Tu_N-u_(N-1)=u_(N+1). Their previous seeds
are q_-1^A=-e and q_-1^B=+e. This is an exact elimination of the
negative seed through the correlated sibling relation (1); it is not
a claim that arbitrary signed Robin seeds are positive.

## 2. Global ordinary coefficient bounds

All comparisons in this section use the ordinary x basis. Define
b=e-a-1. At the root b=0. Under the short child,

    b'=b+g.

Under the long child, b'=g-a-e-1. The previously proved positive
growth identity gives

    b'=r+2xe+3y²a(a+e)+(4y-1)a >= r.

Canonical r>=1 and g>=1 hold by induction: root r=1; new r is
g or e+g; and g=(t-2)e+k+r with k>=1. Hence b>=0 globally,
and b>=1 at every nonroot state. In particular e>=a+1 is proved.

The independently proposed stronger invariant also passes:

    e>=(z-2)a.

Its root is immediate. Short updates add g to the old margin. Long
updates have the exact positive margin

    g-(z-2)(a+e)=3y²a(a+e)+1+za+r >=0.                   (4)

This stronger bound is not needed for the following c_A inequality.

The exact universal decomposition is

    Te-c_A=3y²e²+(3x²+4x)g+e-k+3y²bg.                   (5)

Proof: substitute c_A=e+(t+1)g-r and
r=g-(t-2)e-k, obtaining
3y²e²+e-k+[3y²(e-a)-z]g. Now e-a=b+1 and
3y²-z=3x²+4x, giving (5).

For a nonroot canonical state, g>=k because g-k=(t-2)e+r>=0.
Since b>=1 and 3y²>=1 coefficientwise,

    3y²bg-k=(3y²b-1)g+(g-k)>=0.

Every other term in (5), grouped as 3y²e²+(3x²+4x)g+e,
is nonnegative. At the root b=0,e=k=1,g=z, and (5) is
3y²+(3x²+4x)z=6x³+20x²+18x+3>=0. Thus

    c_A<=Te,  Te<=c_B<=2Te                              (6)

holds globally. The lower bound in (6) uses c_A>=0, which follows
from the established ordinary positivity of e,g,s. No division or
Fourier LR cancellation is used. In particular (6) supplies an actual
correlated seed bound; it does not imply a character coefficient bound.

## 3. Packet degree correction and the ROOT mapping

For a positive spectral packet (T,c,d0), the sufficient degree condition
is

    deg T>0, deg d0<deg c+deg T, N>=1.                   (7)

The earlier stronger condition deg d0<=deg c excludes the reversed
packet unnecessarily. In the Jacobi residue expansion of
c p_N(T)+d0 p_(N-1)(T), every summand is

    [c(T-r_i)+d0] product_(j!=i)(T-r_j).

Under (7), the bracket has degree deg c+deg T and leading coefficient
lc(c)lc(T)>0, independent of r_i. Thus every whole summand has degree
deg c+N deg T and the same positive leading coefficient
lc(c)lc(T)^N. Multiplication by y raises every degree by one and
preserves this property. The quadratic midpoint/mixed blocks likewise
have leading term cT²: d0(T-u) has strictly smaller degree.

Therefore the diagonal strict-support argument in the earlier Jacobi
proof remains valid: given the packet's shifted-trace cones, strict
single blocks and mixed compatibility, all residue summands have the
same dense positive interval support through the full degree. Their
positive squared residue weights contribute a strict defect at every
supported index, including the terminal one. This applies to N=1;
there are simply no omitted-root factors then. The smoothed reversed
N=0 exception must still be excluded.

The strict inequality in (7) holds on actual canonical states for both
(T,c_A,e) and (T,e,c_A). When a is nonzero, let d_a=deg a and
d_e=deg e. Endpoint degree orientation gives d_e>d_a, and the
ordinary positive state with r<=a+e gives

    deg c_A=2d_a+d_e+4,
    deg T=d_a+d_e+4,
    deg(eT)=d_a+2d_e+4>deg c_A.

If a=0, then deg c_A=d_e+2 and deg(eT)=2d_e+3,
again strictly larger. These degree formulas follow by identifying
the leading terms of g,s,T; lower-degree r cannot cancel them.

At the root, e=1=T_0, T_1=z+1, and

    c_A=z²+z=T_2=(12,14,4),
    T=z+3y²T_1=(15,32,24,6).

Here T_j=sum_(i=0)^j U_i(z/2). The forward packet is precisely
`../recovery_oneturn_closure.md` at m=1:
(A,B,t)=(T_2,T_0,z+3y²T_1). Its Sections 4--5 supply the entire
three-parameter boxes, smoothed and unsmoothed relative minors, and
Jacobi compatibility. The reversed packet is precisely
`../second_turn_20261004/kernels_theorem.md` at m=0:
(c,d,tau)=(T_0,T_2,z+3y²T_1). Its Sections 1 and 6 supply the
corresponding reversed boxes and scaled relative-minor result. Its
explicit N>=1 restriction excludes yT_0=y at N=0, whose central
defect is negative.

The packets therefore establish the ROOT under those read-only audited
foundations, with the corrected degree condition. The actual long run
in (3) is the reversed packet at index N+1:

    q_N^B=e u_(N+1)+c_A u_N.

Its smallest index is 1, so it respects the reversed theorem's exception.
This root verification is not a proof that either packet's spectral
conditions propagate through a switch at an arbitrary canonical state.

## 4. Scope and reproducer

`pair_switch_audit.py` uses the earlier independent sparse integer
polynomial utility only, leaving that file unchanged. It directly checks
the residuals and all coefficient decompositions in Z[x,a,e,r], plus
the Chebyshev normalization in formal T,c_A,e. The symbolic zero
identities are universal; the coefficient inequalities are the induction
proofs above. Root arrays are saved in `pair_switch_audit_results.json`.

| Statement | Audit status |
| --- | --- |
| BOTH fixed-C seeds and common Cassini residual | PROVED |
| e>=a+1 and e>=(z-2)a under BOTH mutations | PROVED, ordinary basis |
| c_A<=Te and Te<=c_B<=2Te | PROVED, ordinary basis |
| Degree extension and spectral-to-cone implication | PROVED, conditional on packet hypotheses |
| Paired spectral packet ROOT | PASSES cited audited foundations |
| Paired spectral packet BOTH-child closure | OPEN |
| Paired packet implies the complete regular P_Q predicate | OPEN |
| Full-tree Local TP2 | OPEN |
