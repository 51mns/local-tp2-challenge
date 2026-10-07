# Ordinary-positive trace obstruction and actual monotonicity failure

**The ordinary-positive trace/v conditions still do not close the trace
gate.** A separate actual canonical witness defeats the proposed
reverse-single monotonicity sign shortcut. Neither witness is a
counterexample to full canonical MP_sharp preservation or Local TP2.

## 1. Ordinary positive integer coefficients, correct degree/lc pattern

Let beta=3(x+1)^2, z=2x+3 and

    B_K=2(x+K)^2,
    f_K=z+beta B_K,
    v=6(x+2)^5.

For every integer K>=2, f_K, v and the updated trace f_K+beta v have strictly
positive ordinary integer coefficients and positive Fourier interval
support. All parent shifted traces f_K-r, -2<=r<=2, are strict folded
TP2. Both v and yv are strict folded TP2, including their complete
finite character arrays. The v row is (1512,1260,720,270,60,6), with
raw defects (199584,320760,148500,27720,1944,36); both raw and y
minimum nonzero character and supported-defect values are 36.

The trace is even of the canonical polynomial form

    C=1+yB_K, f_K=3yC-x=z+beta B_K.

Its degrees and leading coefficients fit the **relaxed** LONG pattern
dX=0,dY=2,dC=3,deg f=4,deg v=5 and
lcX=lcY=1,lcC=2,lc f=lc v=6. This wording specifies numerical
degree/lc compatibility only. No X,Y,e,r satisfying canonical ancestry
and Fricke are asserted.

The full continuous parent trace certificate is exact. Its row is

    h0=18K^2+48K+51-r,
    h1=12K^2+48K+38,
    h2= 6K^2+24K+30,
    h3=12K+12, h4=6.

For each endpoint r=+-2, all 15 independent finite character coefficients
have nonnegative power coefficients after replacing K by 2+u, and their
constant terms are positive. The saved verifier records every coefficient.
All noncentral tensor coefficients are affine in r; the central derivative
2r-(2h0|_(r=0)+h2) is strictly negative throughout the box. Thus endpoint
certificates prove the entire continuous r interval, with universal
character lower bound 36. This is not a parameter-grid extrapolation.

Yet the updated trace has the exact interior defect

    delta3(f_K+beta v)=-26028K^2+172080K+24574464.

It is negative for every K>=35. At K=34 it is 336816; at K=35 it
is -1287036 and its derivative is already negative. Therefore K=35
is the first failing integer in this family K>=2, by concavity and the
endpoint bounds, not by a larger search.

The primary independently checked instance is K=64:

    delta3(f_64+beta v)=-71023104.

The parent trace f_64-r has strict complete cones on the entire box,
and all the stated ordinary-positive, degree and lc premises hold.
The negative defect is independent of r, since r changes only h0.
This disproves closure from these weakened premises even though the
updated trace still has positive ordinary coefficients and support.

The supervisor independently verified K=64 without worker imports in
`root_obstruction_audit.py` and its saved results. The witness lacks the
canonical normalized ancestry and a certified MP_sharp origin.

## 2. A necessary canonical coefficient gap excludes this family

For a genuine X=1 parent, a=0, t=z and

    B=e+g=2ye+1+r.

If deg B=2, write e=E0+E1x, r=R0+R1x and B=b0+b1x+b2x^2.
Canonical ordinary bounds r<=e coefficientwise and r>=1 imply

    b0=2E0+1+R0 <=3E0+1,
    b1-b2=2E0+R1 >=2E0.

Consequently every such canonical parent satisfies

    b0 <= 1+(3/2)(b1-b2).

For B_K this requires 2K^2<=6K-2, or K^2-3K+1<=0. No integer
K>=3 can satisfy it. Thus the trace obstruction cannot be relabeled
as an ordinary normalized state: it violates a concrete canonical gap
constraint before Fricke or the origin packet is considered. The bound
is necessary only; it is not proposed as sufficient closure information.

## 3. Actual SSS defeats reverse-single monotonicity at its low-band edge

Rebuild the root followed by three SHORT mutations. This is an actual
canonical state, with ordinary bounds and exact Fricke residual zero.
Write T for its center trace, n=e, c=e+g+s, B=n(T+1)+c and
L2=B-3n=n(T-2)+c. The relevant rows are

    H(n)=(113,88,40,8),
    H(L2)=(4691289,4293982,3285216,2085716,1084268,
                         451544,145392,34080,5184,384).

At columns (3,4), character (6,0), the exact mixed coefficient is

    J(L2,n)=-6386912.

This index is j=deg n=3, inside the proposed low band, not the
previously excluded j=deg n+1 boundary. In the y mode the analogous
low-band edge j=4, columns (4,5), character (8,0), is -17705216.

For the raw index, delta3(n)=64 and J(B,n)=-6386528. Hence

    delta3(B-theta n)=delta3(B)-theta J(B,n)+theta^2*64

is increasing throughout theta in [-1,3], rather than decreasing.
The r=2 endpoint cannot serve as the minimum via that proposed
monotonicity argument. The actual L2 defect is nevertheless
554312100448>0. This is a **sign-shortcut counterexample**, not a
single-block or packet-closure failure. Full continuous parent packets
at the preceding SS state are not asserted by this note.

## 4. The weaker index-one proposal also needs its lc correlations

If leading-coefficient/degree correlations are omitted, the proposed
index-one statement fails too. Take

    A=9450423029, f=z+beta A, v=(x+2)^16.

The parent trace has the strict full shifted box and positive integer
coefficients, and v/yv are strict complete cones. However

    delta1(f+beta v+2)=-37216985.

For completeness the parent row is (9A+3-r,6A+2,3A). Its central
defect has minimum 36A^2-27A-7>=2 for A>=1; its index-one defect
has minimum 9A+4. The remaining independent character coefficients
are positive products of these row entries. This proves the continuous
parent certificate directly.

The construction is exact and linear in A:
J(beta,beta v) at index one is -558279000, while
J(beta,z+2+beta v)=-558278991. The base defect is
5275972633116066754; taking its integer quotient by 558278991 plus
one gives the displayed A. Here lc f=28351269087>lc v=1 and the
degree pattern is noncanonical. This therefore refutes only the
weaker proposal as stated without those correlations. It does not
refute a normalized index-one subgate.

## 5. Other requested source checks and scope

On exactly ROOT, its first SHORT, and its first LONG child, the new
SHORT sources R((t-2)G,K), R((t-1)Q,K), R((t-1)D,K), and the mixed
sum R((t-1)Q,K)+R((t-2)G,(t-1)D) have no negative finite characters,
where K=M[G-(t-2)E]+(T-t)S. The unanchored spectral source
R(y(T-2),3y^3[b0(T+1)+b1]) likewise passes at those three states in
both origins. These targeted checks are not invariant proofs.

| Scope | Proven failure/fact | What remains open |
| --- | --- | --- |
| Relaxed trace/v | Ordinary positivity, trace form and degree/lc pattern do not imply trace closure | Full canonical origin-based trace transport |
| Actual SSS | Proposed monotone low-band sign is false | Reverse-single full-parameter closure |
| Necessary ancestry gap | b0<=1+3(b1-b2)/2 for genuine X=1 quadratic B | Quantitative sufficient canonical gap criteria |
| ROOT/BOTH/TARGET | No actual packet/target counterexample claimed | Both remaining closure types and full-tree strict Local TP2 |

`falsification_defect.py` and `falsification_defect_results.json` contain
the exact reproducible witnesses and continuous parent certificate.
All older files are read only. No GitHub writes or broad tree scan.
