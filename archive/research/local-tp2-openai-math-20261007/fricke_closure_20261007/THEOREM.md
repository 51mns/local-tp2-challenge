# A positive three-coordinate normal form with its exact Fricke constraint

**Primary level: PROOF_CANDIDATE. Full-tree Local TP2 remains open.**
The written algebra and two implementations have been checked in this session.
This is not fresh external review, independent-model review, formal verification
in a proof assistant, or canonical promotion. No new canonical TP2 family is
claimed. The contribution is an exact all-tree coordinate description, a sharper
canonical negative-seed bound, and exact boundaries for two proposed relaxations.

Base: private `51mns/AIMath`, `0f7bb105a3330ba890528bb60b1f85ef6debcef5`.
Owned directory: `research/local-tp2-openai-math-20261007/fricke_closure_20261007/`.
Old proof files and `main` are not changed.

## 1. Goal and rejected shortcut

The target is the original supported adjacent Fourier determinant, not ordinary
coefficient positivity. Let y=x+1, and let the degree-ordered canonical triple
be (X,Y,C), with degrees a<b<c. The root is

    X=1, Y=x+2, C=2x²+6x+5.

The two children are

    U=3yXC-x(X+C)-Y,  V=3yYC-x(Y+C)-X,

ordered so that deg U<deg V. Put S=U-C, D=V-U and

    h_P(n)=[z^n]P(z+z^(-1)),
    W_n(S,D)=h_S(n)h_D(n+1)-h_S(n+1)h_D(n).

The full target is W_n(S,D)>0 for every canonical vertex and every
0<=n<=deg S, using reflection and zero padding. The new normal form below does
not yet prove this inequality.

A proposed way to avoid accumulating many quantitative conditions was to track
only deg(P)² eta(P), where

    delta_n(h)=h_n²-h_(n-1)h_(n+1)-h_(n+1)²+h_n h_(n+2),
    eta(P)=min_(0<=n<=deg P) delta_n(h_P)/h_P(n)².

Section 7 disproves the specific minimum-preservation rule considered here.
This does not invalidate the older, weaker quantitative product estimates.

## 2. Three nonnegative polynomial coordinates

For formal variables u,e,Q over Z[x], set

    beta=3y²,
    X=1+yu,
    g=2x+1+beta u,      t=g+2=3yX-x,
    kappa=X(3X-2)=1+4yu+beta u²,
    A=Q+g e+kappa,
    Y=X+y e,
    C=Y+y A,
    T=Y-y Q=1+y(u+e-Q).                              (2.1)

The inverse-center identity holds identically, without imposing Fricke:

    T=tY-xX-C.                                       (2.2)

The lower-case letters s,l below mean **retain the smaller/larger endpoint**.
They are not the fixed Farey L/R labels. Define

    s: (u,e,Q) -> (u, A+e, A),
    l: (u,e,Q) -> (u+e, A, A+e).                     (2.3)

### Theorem 1 — exact positive normal form

Starting at (u,e,Q)=(0,1,1), (2.1) and (2.3) generate exactly the canonical
binary tree with its endpoints sorted by degree. Every u,e,Q,A has nonnegative
ordinary x coefficients; e,Q,A are nonzero. The inverse quotient

    z=u+e-Q

has nonnegative coefficients at every canonical state. The equations (2.3)
are both positive polynomial maps: they contain no subtraction.

### Proof

At (0,1,1), (2.1) gives the displayed root. Its A is 2x+3 and T=1.
Both maps have nonnegative polynomial coordinates whenever u,e,Q do, so this
positivity follows by induction.

For the short step, the reconstructed endpoints are X and C. Its new seed is

    A_s=A+g(A+e)+kappa
       =(g+1)A+g e+kappa=tA-Q.                       (2.4)

In the original recurrence,

    U-C=(t-1)C-Y-xX
       =y[(t-1)A+(A-Q)]=y(tA-Q),

using (2.2), or equivalently (t-2)Y-xX=y(A-Q). Thus its reconstructed new
center is exactly U.

For the long step, the reconstructed endpoints are Y and C, and the trace is

    t_l=t+beta e.

The new kappa satisfies kappa_l-kappa=(2g+2)e+beta e². Substitution into
A_l=Q_l+g_l e_l+kappa_l gives

    A_l=t_l(A+e)+e-Q.                                (2.5)

On the original long step, its seed relative to retained endpoint Y is A+e,
and its signed previous seed is e-Q. Its next increment is therefore the
right side of (2.5); equivalently direct substitution gives V-C=y A_l.
The new center is V. This verifies both maps, not just one ray.

The inverse quotient updates especially simply:

    z_s=u+e,       z_l=u.                            (2.6)

Since z=0 at the root, z is nonnegative throughout. In addition

    e_s-Q_s=e,    e_l-Q_l=-e.                         (2.7)

Thus e-Q has uniform coefficient sign, including zero at the root.

For completeness, the root has deg C=deg X+deg Y+1 and deg X<deg Y.
If these hold at a node, the mutation retaining X has degree
2 deg X+deg Y+2. For deg X>0 its top term comes from 3yXC; for X=1 the
coefficient of xC is 3-1=2 and remains positive. The longer child has degree
deg X+2 deg Y+2. The child order is consequently strict, the next center is
above both endpoints in degree, and the same degree identity holds at both
children. The maps therefore implement the stated sorting at every step.
Each vertex has both original children, so no path is omitted.

The same induction gives dense positive ordinary coefficients for e,Q,A and
for every nonzero u. The root supplies the base. The dense product g e has
degree deg X+deg Y, which exceeds the degrees of Q and kappa; it therefore
makes A dense. The two updates preserve this property (and the leading
coefficients of e,Q agree). The reconstructed target polynomials in (5.1)
are consequently positive throughout their ordinary and Fourier supports.
This justifies the support assertion used for their terminal minor. QED.

This provides an alternative derivation of the ordinary positivity needed
here; it does not use a conjectured Fourier cone condition.

## 3. The Fricke relation is an exact preserved constraint, not optional data

Define the residual

    R(u,e,Q)=A Q-g e²-2kappa e-3uX².                  (3.1)

### Theorem 2 — both-child Fricke preservation

For arbitrary formal u,e,Q, the original Fricke polynomial

    I(X,Y,C)=X²+Y²+C²+x(XY+XC+YC)-3yXYC

satisfies

    I(X,Y,C)=y² R(u,e,Q).                            (3.2)

Moreover R is unchanged under each polynomial map in (2.3). At the root R=0.
Therefore every canonical state satisfies the positive product identity

    A Q=g e²+2kappa e+3uX².                         (3.3)

### Proof

By (2.2), C+T=tY-xX. Viewing I as a quadratic in C gives

    I=X²+Y²+xXY-CT.

Using C=Y+yA and T=Y-yQ,

    I=X²+xXY-yY(A-Q)+y²AQ.

Now substitute Y=X+ye and A-Q=ge+kappa. The remaining simplifications are

    X-kappa=-3yuX,      x-g=y(2-3X).

They give I=y²(AQ-ge²-2kappa e-3uX²), proving (3.2).

I is symmetric in its three inputs. For fixed X,C it is monic quadratic in Y
with linear coefficient x(X+C)-3yXC. Replacing Y by
3yXC-x(X+C)-Y leaves that quadratic unchanged. This is an algebraic identity,
not a conclusion restricted to I=0. The reconstructions in Theorem 1 thus give
I_s=I_l=I. By (3.2), y²(R_s-R)=y²(R_l-R)=0 in the integral domain Z[x,u,e,Q].
Cancel the nonzero polynomial y². Directly at (0,1,1), A=2x+3, g=2x+1 and
kappa=1, so R=0. Induction proves (3.3). QED.

The same constraint can be written as the exact seed norm

    A²-tAQ+Q²=X²(1+3u).                             (3.4)

Indeed (A-Q)²-gAQ=kappa²-3ugX²-gR and
kappa²-X²(1+3u)=3ugX². Before imposing R=0 the difference between the two
sides of (3.4) is -gR. Equation (3.4) is therefore not an independent
positivity assumption or a newly discovered global Fricke invariant; it is
its expression in these gap coordinates.

## 4. A stronger all-tree bound on a negative seed

### Corollary 3 — coefficientwise domination with a full trace factor

For the degree-ordered short-ray seed B=-Q, every canonical state satisfies

    A-(t-1)Q=1+(2x+3)u+g z >=0                      (4.1)

in ordinary coefficients. In particular A>=(t-1)Q, which is stronger than
Q<=A. Here (4.1) is an identity without the Fricke assumption; nonnegativity
uses the canonical z>=0 supplied by Theorem 1.

Proof: A-(t-1)Q=g(e-Q)+kappa=gz+(kappa-gu), and
kappa-gu=1+(2x+3)u.

This extends to either choice of fixed endpoint. For arbitrary chosen endpoint
X=1+yu, other endpoint Y, and canonical inverse T=1+yz, put

    a=(C-Y)/y,  b=(T-Y)/y,  t=3yX-x.

Then

    a+(t-1)b=1+(2x+3)u+(t-2)z >=0.                  (4.2)

For the larger endpoint this is also checked directly by replacing
(a,b,t,u) with (A+e,e-Q,t+beta e,u+e) in (4.2); the same z occurs.
Whenever b is coefficientwise negative, Q_abs=-b satisfies

    a >= (t-1)Q_abs.                                (4.3)

This holds for both actual continuation directions and all canonical nodes.
For positive b, (4.2) does not imply (4.3); no such implication is claimed.

### A direct relative-error consequence

Let nu=h_t(0). Since t=2x+3+3y²u, t-r has nonnegative ordinary coefficients
for -2<=r<=2 and nu>=3. From (4.3) and nonnegative Laurent convolution,

    a >= (nu-1)Q_abs,
    a(t-r) >= (nu-2)a,

hence uniformly throughout the real interval,

    h_(Q_abs)(n) <= h_(a(t-r))(n) / [(nu-1)(nu-2)]    (4.4)

at every index. Multiplication by y gives the same bound for smoothed rows.
This improves the elementary estimate 1/(nu-2) obtained from Q_abs<=a by
an additional factor nu-1. The result is about relative coefficient size.

It does not, by itself, prove a(t-r), its smoothed version, or their difference
belongs to the folded cone. For example, using the previous normalized
subtraction estimate, a sufficient *additional* condition would be

    eta(a(t-r)) > 4epsilon+2epsilon²,
    epsilon=1/[(nu-1)(nu-2)].

The extra cone and margin hypotheses are exactly the remaining shape issue;
we have not shown them uniformly after both children. This corollary cannot
be presented as a full-tree TP2-preserving invariant.

## 5. The target is recovered without a proxy change

At the current node, the short child gap and difference of children satisfy

    S=y(tA-Q),
    D=y e [t+1+3y²(A+e)].                           (5.1)

The first formula was proved in (2.4). Subtract (2.4) from (2.5):

    A_l-A_s=e[t+1+beta(A+e)].

Multiplying by y proves the second. Both have positive ordinary coefficients.
The degrees are

    deg S=2a+b+2,   deg D=a+2b+2,   deg D-deg S=b-a>0,

where a=deg X and b=deg Y. Thus the terminal target minor is positive from
support, while the interior Fourier comparisons remain the difficult part.
No cancellation of a non-TP2 convolution factor y has been performed.

## 6. Positivity of this coordinate system is not a replacement for TP2

Take a deliberately noncanonical input

    u=0, e=x+23, Q=x+1.

It has u,e,Q>=0, z=22>=0, equal leading coefficients of e and Q, and the
strong bound (4.1). Its reconstruction is

    X=1,
    Y=x²+24x+24,
    C=2x³+51x²+97x+49,
    T=22x+23,
    A=2x²+48x+25.

It even has deg X<deg Y<deg C, deg C=deg X+deg Y+1 and deg T<deg Y.
But its residual is

    R=-43x²-1033x-550 != 0.

Its true mutation gaps give

    h_S=(688,585,311,106,4),
    h_D=(71608,60883,38530,16265,4434,303,6),
    W_0(S,D)=-3176.

This refutes a proposed implication from these ordinary positivity,
domination and degree conditions alone. It is NOT a canonical counterexample.
Its seed also fails the folded cone test: delta_0(A)=-3709. It therefore does
not refute the previously stated signed or compound extension theorems with
all of their hypotheses. Nor does it prove Fricke alone is sufficient.
The appropriate lesson is to retain canonical coupling and genuinely prove
the needed Fourier shape, rather than silently replace it by ordinary positivity.

## 7. A precise counterexample to a one-number margin rule

Consider the candidate universal rule, for positive-degree strict cone F,G,

    deg(FG)² eta(FG) >= min(deg(F)² eta(F), deg(G)² eta(G)).        (7.1)

It would make one degree-corrected margin easier to carry through long products.
It is false even with strictly positive ordinary coefficients and with yF,yG
also strict cone. Take

    F=3+44x+30x²+3x³,     G=x+2.

Exact half-rows and supported defects are

| Polynomial | h | delta |
|---|---|---|
| F | (63,53,30,3) | (241,178,732,9) |
| G | (2,1) | (2,1) |
| FG | (232,199,116,36,3) | (1534,6397,5344,939,9) |
| yF | (169,146,86,33,3) | (463,4204,1747,822,9) |
| yG | (4,3,1) | (2,4,1) |

All displayed defects are positive. Nevertheless,

    eta(F)=241/3969, eta(G)=1/2, eta(FG)=767/26912,
    min(9eta(F),eta(G))=1/2,
    16eta(FG)=767/1682 < 1/2,
    16eta(FG)-1/2=-37/841.

Thus (7.1) fails. This witness refutes only that particular proposed
strengthening. It neither refutes multiplicative cone closure, nor the earlier
weaker normalized product inequality, nor any canonical TP2 claim. F is not
asserted to be a canonical polynomial. A different scalar law is not ruled out.

## 8. What was and was not verified

`symbolic.py` expands identities in Z[x,u,e,Q] with sparse integer arithmetic.
It checks 23 polynomial identities identically, including both-child residual
preservation, both reconstructions, the norm and the stronger seed inequalities.
No values of x,u,e,Q are sampled to infer those identities.

`author.py` generates the normal-form tree using only the positive maps;
`verifier.py` separately generates the tree using only the original mutations
in the full Laurent ring. It performs exact symmetric Laurent division by y,
not the author's binomial formula. It imports neither the author code nor its
expected output. A third orchestration script compares outputs after both have
completed. The outputs match for all 255 s/l words of length <=7, including
all row digests and all 13,120 supported target minors. They also match the
382 negative-seed coefficient-bound checks and both explicit counterexamples.

The all-tree algebra follows from the written proofs, not those 255 vertices.
The 13,120 positive target minors remain bounded regression evidence and do
not extend the previously proved path family. Same-model separate methods are
not external independent review. Formal polynomial expansion is not formal
verification of the full mathematical argument in Lean or another proof assistant.

## 9. Source and strategic placement

The inherited local target and prior conditional kernel methods are fixed in
`compound_transport_20261007/THEOREM.md` and `signed_seed_20261007/THEOREM.md`
at the stated private baseline. This note does not re-audit all previous
three-run certificates.

For a primary-source cross-check, Bittmann, Jouteur, Kantarcı Oğuz, Molander,
and Yıldırım, *A Mirror deformation of Markov Numbers*, arXiv:2602.14802v1,
section 2, equation (1), studies the same deformed equation after
x=z+z^(-1) and its Vieta mutation:
https://arxiv.org/html/2602.14802v1 . The classical Fricke/Vieta mechanism is
not a new discovery here. No theorem from that manuscript is used to fill the
missing Fourier-order step, and no novelty claim follows from this limited check.

Campaign decision: **PIVOT away from the proposed universal one-number margin
rule and from merely adding more fixed rays.** Retain the exact coupled state
and the sharper negative-seed estimate. A justified next advance must establish
Fourier shape/order using the canonical relation or provide a genuine closure
under both (2.3). More normal forms or positive finite scans alone do not meet
that continuation criterion. Full-tree Local TP2 is still open.
