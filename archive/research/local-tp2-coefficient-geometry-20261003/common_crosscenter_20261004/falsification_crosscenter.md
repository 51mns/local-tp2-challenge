# Exact cross-center obstructions and canonical domain constraints

Status: **two analytically certified relaxed-packet counterexamples**, a
**universal signed-flux obstruction on canonical children**, and a proved
**Fourier surplus invariant on every canonical nonroot state**. None is an
actual canonical child-packet counterexample. Full-tree strict Local TP2,
arbitrary-parent changed-center paired MP_sharp, and the regular-edge proxy
remain OPEN.

All earlier directories were read only. The companion exact verifier is
`falsification_crosscenter.py`; its deterministic output is
`falsification_crosscenter_results.json`. It uses Python integer/Fraction
arithmetic and the established Fourier transform. No former 33-state /
1,584-case packet search is repeated.

## 1. Paired MP_sharp alone does not preserve the abstract child tuple

Two explicit relaxed tuples satisfy even the older **uniform-factor-4
paired midpoint packet on the entire continuous square**. Under the
displayed short tuple update they fail positive Fourier interval support.
These are not normalized states: g/s ancestry and Fricke correlations have
not been imposed.

### A. Degree-one trace, constant positive seeds

Take

    T=20+10x, e=1, c=2, g=0, s=1, beta=3(x+1)^2.

Both seed orders satisfy the strict degree condition 0<1. For every
q in [-4,2], put B=20-q in [18,24]. The trace T-q has half-row (B,10),
and y(T-q) has half-row (B+20,B+10,10). Their folded defects are

    T-q:       (B^2-200, 100),
    y(T-q):    (-B^2+10B+400, B^2+10B-200, 100).

They are strictly positive throughout that interval: lower bounds are
(124,100) and (64,304,100). The actual forward/reverse single blocks are

    2[T-(r-1/2)] and T-(r-2),

so both L and yL gates hold on the full required r box.

Write alpha=(r+s)/2, omega=(r-s)^2/4. The midpoint blocks are

    H_forward=2[(T-alpha)^2+(T-alpha)/2-omega],
    H_reverse=  [(T-alpha)^2+2(T-alpha)-omega].

Each is gamma(T-q1)(T-q2), gamma=2 or 1. For the exact parameter
domain |alpha|<=2, omega<=(2-|alpha|)^2, the two forward roots lie in
[-5/2,2], and the reverse roots lie in [-4,2]. To see the upper bound
for either pair, for a=1/4 or 1 use

    omega <= (2-alpha)^2 <= (2-alpha+a)^2-a^2.

The lower bounds follow similarly from
omega<=(2+alpha)^2 when alpha<=0; the alpha>=0 half is weaker. Thus
H and yH are strict products of the certified shifted traces.

The uniform relative bound also holds at **every ordered minor**, not
just at the defects. In the raw mode the constant seed tensor has only
its central coefficient. The Cauchy--Binet term at intermediate index 1
gives delta0(H)>=20,000 gamma^2. In the y mode the reference tensor T_y
has central coefficient -1 and its only positive selectors are (0,2)
and (1,2), each equal to 1. For the first one, put B1,B2 in [18,24].
The row of yH satisfies

    h1 >= 984 gamma,
    h0-2h2 = gamma B1 B2 >=324 gamma,

so its selector (0,2)=h1(h0-2h2)+h0h3 is >=318,816 gamma^2.
At selector (1,2), the strict-product Cauchy--Binet term gives
delta1(yH)>=304(18^2-10^2)gamma^2=68,096 gamma^2.
The largest required uniform reference is 4T_(2y)=16T_y. All remaining
reference coefficients vanish or are negative. The established finite
character/all-ordered-minor equivalence therefore proves the full
uniform-factor-4 paired packet, and hence MP_sharp, continuously.

Nevertheless the relaxed short update gives

    u=T-beta, T'=23+16x+3x^2,
    c'=(u+1)s+e=19+4x-3x^2, e'=1.

At r=0 the child's forward L has degree 4 and leading coefficient -9.
Positive Fourier interval support fails. This is a low-complexity
counterexample to an **abstract packet-only closure theorem**.
It is not canonical: T+x is not divisible by y, and the chosen g,s do
not obey the normalized ancestry equations.

### B. The trace divisibility alone does not repair closure

Take

    T=11+22x+16x^2+4x^3,
    e=5+2x, c=2e, g=0, s=e.

Here T=z+beta B with B=(8+4x)/3, so C=1+yB really is a polynomial of
the canonical trace form. The shifted trace row is (43-q,34,16,4).
For every q in [-4,2] its defects are

    (225-102q+q^2, 348+16q, 104, 16),

with lower bounds (25,284,104,16). The e and ye defects are
(17,4) and (1,27,4), so both are strict cones. The same midpoint
factor roots used above lie in [-4,2]. Write H=eZ, with Z either
2(T-q1)(T-q2) or (T-q1)(T-q2). All coefficients of T_Z are
nonnegative; its central coefficient has the Cauchy--Binet lower bound

    delta0(Z) >= gamma^2 delta3(T-q1) * 2H(T-q2)_3^2
              =512 gamma^2.

The uniform-factor-4 reference is at most 16T_e. Hence
T_Z-16T_1 is character nonnegative, and multiplication by T_e or T_ye
proves both full continuous relative packets. All single blocks and
midpoint blocks are strict products with the appropriate degree
ordering. Thus this tuple has the same full-box parent certification.

Its short child is

    T'=26+58x+43x^2+10x^3,
    c'=-10-74x-83x^2-32x^3-4x^4.

The forward L0 has leading coefficient -40. The missing ordinary
constraint is already explicit: because g=0, the implied normalized
ancestry parameter is

    a=B-e=-7/3-(2/3)x.

Therefore this witness has trace divisibility and positive seeds but
violates a>=0 as well as normalized g/s and Fricke ancestry. Any valid
canonical closure proof must retain those correlations; paired midpoint
packets do not reconstruct them by themselves.

## 2. A canonical anchored flux is universally signed

For either actual child let z=T'+1, n=e', c=c', and
B=L'_-1=nz+c. The packet-algebra lane obtained an exact anchored
decomposition of the reversed sharp mixed certificate:

    theta=r+1, phi=s+1, eta=(theta+phi)/2,
    kappa=theta phi, omega=(theta-phi)^2/4,
    A=T_z-eta J(z,1)+kappa,
    K=T_B+kappa T_n-eta J(B,n),
    T_H-omega T_c = A K + omega F,
    F=J(B,nz)-J(Bz,n)
     =(U^2-4)(V^2-4)R(1,z)R(B,n).

The verifier independently checks both formulas by character
Clebsch--Gordan multiplication, and checks the whole identity at three
nontrivial parameter pairs in both raw and y modes at both root children.

There is an exact **all-canonical** negative coefficient. Put
d=deg z>0 and f=deg B. At selector columns (0,f+d+1), the first
mixed tensor J(B,nz) vanishes. The second has coefficient
H(n)_0 lc(Bz)>0. Hence

    Sel_(0,f+d+1) F = -H(n)_0 lc(Bz)<0.

This uses only positive leading support and the canonical degree
ordering; it is independent of any parameter-grid search. Concrete
ROOT/BOTH witnesses are:

| Actual child | Central F | Far columns | Character | Far F |
| --- | ---: | --- | --- | ---: |
| Short | -10,296,424 | (0,10) | (9,9) | -1,152 |
| Long | -44,762,988 | (0,12) | (11,11) | -1,944 |

Both first-child full packets are independently known to hold. The
negative F therefore disproves **sourcewise flux positivity**, not the
child certificate. A proof through this decomposition must bound the
negative omega F against A K; discarding F is invalid.

## 3. Canonical Fourier surplus E-XP is nonnegative away from ROOT

Let F0=E-XP=ye-(1+ya)P. The exact mutations give

    F0_short = F0+yg,
    F0_long  = (x^2-1)e+x+y(r-1)+ya(2+3x)+3y^3 a(a+e).

Canonical ordinary bounds give a,e>=0 and r>=1. Every summand in
the long expression has nonnegative Laurent coefficients: in particular
x^2-1 has half-row (1,0,1), and x has half-row (0,1). This proves
Fourier entry nonnegativity at every long child. Short mutations preserve
it because yg is Laurent nonnegative. At ROOT, F0=-1; its first short
and long children have rows (6,5,2) and (1,1,1). Induction therefore
proves F0>=0 Fourier coefficientwise at **every canonical nonroot state**.

This is an entry/support fact. It does not imply folded TP2 of F0,
R(S,F0 M)>=character0, or any proxy mixed compatibility. In fact the
first long F0 has row (1,1,1), whose central folded defect is 0 and whose
index-1 defect is -1. Thus even this actual positive Fourier surplus is
not a folded cone.

## 4. Multiplier and root exceptions remain explicit

The raw beta=3y^2 really is a weak folded cone, with row (9,6,3) and
defects (36,0,9). In contrast, y has central defect -1, and y beta
has row (21,18,9,3) with central defect -18. Thus raw common
beta multiplication can use cone closure; y smoothing cannot be inferred
by treating either y or y beta as a cone multiplier. The smoothed gates
must still be certified separately. A seed-cone requirement would also
exclude the reversed root seed ye=y.

## 5. Targeted checks of new candidate gates; no extrapolation

Only ROOT and its six depth-at-most-two states were checked for the new
proxy source candidates. Every finite character coefficient is
nonnegative for R(G,Pi), R(S,(E-XP)M), R(Q,D-PQ), R(Q,Q_short-next),
and the short proxy increment. The R(Q,D-PQ) minimum nonzero values are
8,192,324,1536,20736,17496,139968 in ROOT,s,l,ss,sl,ls,ll order.
This is a targeted finite-state check of new proposed gates; it is not
an invariant proof or a new full-tree packet scan.

The spectral worker's restricted fixed-trace advance proposal was tested
for N=1,...,4, T=x+41/12, b0=x+5/2, b1=0, and the 25 fixed pairs in
{-1,-1/2,0,1/2,1}^2. The stronger scalar certificate
T_(U_N(T)[(T-r)(T-s)]-U_(N-1)(T)[T-(r+s)/2])
-omega T_(U_(N-1)(T)) has no negative character coefficient in these
100 cases. Common b0/yb0 cone factors then give both modes. This does
not settle the continuous restricted-parameter conjecture.

## ROOT / BOTH / TARGET ledger

| Statement | ROOT | BOTH | TARGET relevance |
| --- | --- | --- | --- |
| Relaxed paired packets A/B | Full-box parent certificate | Short abstract tuple fails support | Shows ancestry cannot be dropped; not an actual-state failure |
| Anchored F source | Exact first-child witnesses | Universal negative far coefficient | Requires a comparison estimate, not sourcewise positivity |
| Fourier E-XP surplus | F0=-1 exception | Entry positivity invariant at every nonroot child | Useful entry fact; no LR/mixed consequence proved |
| New proxy gates | Seven exact states pass | General preservation OPEN | No target proof from samples |
| Full canonical changed-center packet and strict proxy | Base known | Arbitrary-parent closure OPEN | Full-tree strict Local TP2 OPEN |
