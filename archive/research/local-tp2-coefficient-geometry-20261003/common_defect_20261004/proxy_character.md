# The coupled-prefix D representation and a canonical signed residual

Status: **proved arbitrary-origin algebra and both actual origin-switch
rules; exact initialized canonical obstruction to signing the remaining
prefix residual separately.** No new arbitrary-parent BOTH strict Q<D
gate is proved. Full-tree strict Local TP2 remains **OPEN**.

This extends the anchored-origin identity from
`../common_crosscenter_20261004/proxy_algebra.md` while retaining its
actual negative anchor. The old coarse Robin bound is not repeated or
adopted. Character signs below refer to the complete finite
chi_a(U)chi_b(V) array; scalar polynomial evaluations do not replace them.

## 1. The actual E row uses the preceding prefix

Fix an origin that is currently the **smaller endpoint register**, with
endpoint X=1+y a_X, trace t=3yX-x, and frozen seeds b0,b1 and anchor a_O.
Let U_-1=0, U_0=1, U_j=tU_(j-1)-U_(j-2), and

    f_j=b0 U_j+b1 U_(j-1),
    R_j=sum_(i=0)^j U_i, R_-1=0,
    Z_N=b0 R_(N-1)+b1 R_(N-2).

The existing exact register/anchor identities are

    g=f_(N-1), s=f_N,
    B_N=(C_N-1)/y=a_O+Z_N,
    b0+b1-[1+(2x+3)a_X]=(t-2)a_O.

Now use the actual canonical equality B_N=a_X+e_N+g. Since

    Z_N-f_(N-1)=Z_(N-1),

we obtain the missing correlated E formula

    e_N=a_O-a_X+Z_(N-1),
    E_N=y[a_O-a_X+Z_(N-1)].                         (1)

The exact negative anchor H=a_O-a_X is part of (1). It cannot be
dropped merely because Z_(N-1) has a certified kernel. On advancing
this same smaller origin by one short step,

    e_(N+1)-e_N=f_(N-1),
    B_(N+1)-B_N=f_N.

Thus (1) has unconditional retention transport for every N. This is a
polynomial identity, independent of a cone premise and independent of
Fricke. The actual state still retains Fricke and ordinary positivity.

## 2. Both new origins determine the first valid smaller-register use

At the parent put n=e+g, c=e+g+s, B=a+e+g and T=3yC-x.
For the new endpoint C, the normalized endpoint is a_X=B and the
anchor is a_O=a. Hence the same signed anchor at either initialization is

    H=a_O-a_X=-(e+g)=-n.                            (2)

The short initialization has forward seeds (c,e) and larger index 1.
It becomes the smaller register when that record takes a long step;
its first smaller index is 2. Formula (1) gives

    e_2=H+Z_1=-n+c=s.                               (3)

The long initialization has reverse seeds (e,c) and larger index 2.
After a long retention it first becomes the smaller register at index 3,
and (1) gives

    e_3=H+Z_2=-n+(T+1)e+c=s+e(T+1)=s+d.             (4)

These are exactly the old outgoing gaps, with their already certified
raw/y kernels; no unproved child-center packet is used. The root
ordinary P endpoint has (b0,b1,a_O,a_X)=(2P,0,0,1); its first smaller
use is N=2 and e_2=2P-1=2x+3. The endpoint-1 smaller origin retains
H=0 and remains the separate boundary origin.

Equations (1)-(4) describe arbitrary retained lengths and BOTH switch
types. They do not prove a cross-prefix LR inequality after a switch.

## 3. The full Q,D tensor retains three correlated prefix factors

Put A=t-2, beta=3y², q0=y(b0+b1), J=yA, and

    M0=2P+beta a_O,
    e_N=H+Z_(N-1),
    L_N=3y³ e_N=3y² E_N,
    d0_N=M0 E_N.

The complete actual pair is

    Q_N=J Z_N+q0,
    D_N=E_N[M0+beta Z_N]=L_N Z_N+d0_N.              (5)

Here D_N denotes the **actual D polynomial**, not the old spectral
diagonal tensor whose unrelated notation was also D_N. Formula (5)
contains the full anchor, preceding prefix, and current prefix. It is
not an independent replacement of E by a cone seed.

Bilinearity and common multiplication give the universal tensor identity

    R(Q_N,D_N)=T_ZN R(J,L_N)+Psi_N,
    Psi_N=R(JZ_N,d0_N)+R(q0,L_N Z_N)+R(q0,d0_N).     (6)

Every term is explicit in frozen origin data and N. Under an ordinary
MP_sharp or MP_01 origin, Z_N is strict in raw/y modes for N>=2 by the
earlier prefix resolvent theorem. Under the weaker core MP_0 origin,
strict prefix certification is available only for N>=3; its N=2 prefix
is L_-1 and is merely weak. The algebra (1)-(6) and the strong-certified
first-long counterexample are unchanged. Nevertheless the source R(J,L_N) and Psi_N
are not automatically cones. The factor y is kept within the actual
polynomials; no y cone multiplication is inferred.

Equation (6) is a possible quantitative correlated margin formulation:
if the full boundary of T_ZN R(J,L_N)+Psi_N is strict, then the weaker
target gate Q<D is strict. It is not being relabeled as a proved gate.
The next section shows why independently signing its two pieces cannot
be a common proof, even at an ordinary initialized origin.

## 4. Actual first-long obstruction to a nonnegative residual

Take the genuine first long from the normalized root. Its smaller
endpoint is P and its already certified frozen ordinary origin is

    t=3x²+8x+6, b0=2P, b1=0, a_O=0, a_X=1, N=2.

The complete correlated quantities are

    Z_2=28+46x+28x²+6x³,
    Z_1=4+2x,
    H=-1,
    e_2=3+2x,
    J=4+12x+11x²+3x³,
    L_2=3y³(3+2x), d0_2=2yP(3+2x).

The **entire** character tensor R(J,L_2) is nonnegative. Its adjacent
boundary is (129,195,90,18). However the residual in (6) has

    [chi_6(U)chi_0(V)]Psi_2=-2504,

and also coefficients

    (5,1):-1572, (7,1):-600, (8,2):-72,

with their symmetric transposes. Its full adjacent boundary is

    (11688,24412,4804,-2504,0,0,0).                  (7)

The positive common-factor contribution at n=3 is 1311780, so the
complete strict Q,D minor there is 1309276. Every actual supported
Q,D minor is positive. This state satisfies normalized Fricke, actual
ancestry, and the previously certified packets/registers. Therefore (7)
refutes a proposed separately nonnegative Psi_N source on actual data;
it does not refute Q<D, the origin certificate, or Local TP2.

Moving the anchor contribution from L_N into Psi_N loses even more
information: the unanchored source R(J,3y³Z_(N-1)) is also nonnegative
in this state, but its corresponding residual has negative central
coefficient -52128. The full grouping in (6) is the stronger retained
comparison and still needs quantitative compensation.

## 5. Exact scope

| Obligation | Status |
| --- | --- |
| Actual smaller-origin E/Q/D representation, all N | PROVED exact identities with signed anchor. |
| BOTH creation plus first smaller-register use | PROVED by (2)-(4); index restrictions explicit. |
| Complete coupled-prefix tensor split | PROVED universal algebra, central selector normalized. |
| Separately nonnegative residual Psi_N | FALSE at actual first long. |
| Full source R(J,L_N) on every initialization and BOTH advance | OPEN; finite examples are not an invariant proof. |
| Quantified common-factor compensation of Psi_N | OPEN for arbitrary certified origins/switches. |
| BOTH strict Q<D | OPEN. |
| IMPLIES TARGET once Q<D is supplied | Inherited proved direct S<=Q<D sandwich, including terminal. |
| Full-tree strict Local TP2 | OPEN. |

`proxy_character_verify.py` uses standard Python exact integer arithmetic
only. It verifies the actual root-P, forward-C, and reverse-C first
smaller uses against normalized Fricke states; computes complete finite
character arrays; verifies (6) through Clebsch-Gordan common-product
multiplication; and reproduces the signed residual (7). Formal-trace
replays check prefix indexing. They validate the universal formulas and
the explicit counterexample, not arbitrary-parent positivity. Results
are in `proxy_character_results.json`.
