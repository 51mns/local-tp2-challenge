# LONG gate: a strictness obstruction and failure of a complete low-block split

**Verdict: HOLD.** No arbitrary canonical-parent LONG preservation theorem
was obtained. Two concrete bridge candidates have exact obstructions below.
The first is a complete-premise counterexample to a relaxed sufficient
lemma, including its support, cone, shifted-trace and central-flag premises.
The second is a genuine certified canonical seed obstruction to a proposed
coupled source split. Neither is a canonical counterexample to Local TP2.

## 1. Exact LONG coupling and what a usable chain would require

Use the existing notation and put

    h=3yY-x-1=y(3Y-1), A=h-1, F=S+D, J=E+G,
    U=h(Q+D), V=hD, B=AG-E,
    Z=G-hE, K=MZ+3yGF.

The universal canonical identities, needing no Fricke for this algebra, are

    Q'=U+B=hF-J,
    D'=V+K=G(M+3yF).

A seemingly analogous SHORT sufficient chain would be

    B<=lr U<=lr V<=lr K.                            (1)

The middle comparison follows weakly from the parent comparison through
the common h kernel. However, unlike SHORT, strict parent transport does
not cover the whole child Q support. Indeed

    R(U,V)=T_h R(Q,D),

and its adjacent minors vanish above deg(hQ), while U has degree deg(hD).
Ordinary LONG has deg D>deg Q. Merely requiring all of (1) weak therefore
does not prove strict child Q'<D', even when both child rows are strict
folded cones and have the correct strict degree order.

A correct conditional chain theorem would replace the last link by
**V<lr K at every supported V index**. With positive dense supports,
transitivity gives U<lr K throughout U's support and B<=lr V,K. Expansion

    R(U+B,V+K)=R(U,V)+R(B,V)+R(U,K)+R(B,K)

then retains the strict R(U,K) term everywhere in the child Q support.
Equivalently this needs a strictly positive independent D-only advance
R(hD,D')=R(hD,K), in addition to the unproved lower-block link B<=U.
Both canonical sign obligations remain OPEN. This conditional statement
does not constitute a strategy bridge.

## 2. Exact counterexample to the weak LONG chain

This is a **relaxed source-chain model**, not a canonical P_0 state. It
refutes the lemma that the displayed weak chain, parent strictness and
the listed cone/support/trace conditions suffice for child strictness.
Let P=x+2 and let C_7=x^7-7x^5+14x^3-7x, whose half-row is the coordinate
unit at index seven. Set

    h=y(3P-1)=3x²+8x+5, Q=P, D=P^4,
    B=hQ, V=hD, U=h(Q+D), K=V+C_7/100.

The h here is the actual initial ordinary-endpoint trace shape with Y=P.
For tau=h+1 and every r in [-2,2], write c=1-r in [-1,3]. The complete
supported defects of tau-r are

    (c²+25c+26, 22-3c, 9).

They are strictly positive throughout the interval: the first is
increasing there and has minimum two at c=-1; the second has minimum
13. Thus even the full shifted-trace premise and the retained integer
central flag delta_0(tau-2)=2 hold.

Every listed source and both child rows have strictly positive ordinary
coefficients and dense positive Fourier interval support. The verifier
checks full finite character arrays for folded cones of h,Q,D,B,V,K
and both child rows, and every ordered relative character for the links
in (1). In particular the parent adjacent minors are (42,28)>0, while

    W(U,V)=(5476,8702,3733,477,0,0,0),
    W(V,K)=(0,0,0,0,0,0,3/100).

The child rows are

    Q'=hD+2hQ, D'=2hD+C_7/100,

with degrees six and seven, respectively. Their complete supported
adjacent minors are

    (21904,34808,14932,1908,0,0,3/100).

Thus strict child comparison fails exactly at indices four and five.
All stated premises of the relaxed weak-chain lemma hold. Fricke,
normalized ancestry, exact origin registers/paired MP_0, and the canonical
formulas for B,K are **not** claimed. Consequently this example is not a
counterexample to P_0=>canonical LONG Q'<D'. It shows that those
canonical correlations must supply extra strictness if this chain is used.

## 3. A fully coupled low-M block is negative at a certified canonical parent

At the genuine first SHORT parent, normalized registers are

    a=0, e=4+2x, r=3+2x.

Its full stronger packet certificate, hence P_0 membership, is inherited
from the audited root-child certificates recorded in
`../common_defect_20261004/ROOT_AUDIT.md`; it is not asserted from a finite
scan. The targeted verifier independently reconstructs Fricke=0, all
four regular LR companions, current G/M cones and parent strict Q<D.

Rather than require signs of MZ separately, retain *all* the low-center
pieces together. Expansion yields exactly

    R(Q',D')=R(Q',GM)+3R(Q',yGF),

    R(Q',GM)=R(U,V)+R(U,MZ)+R(B,V)+R(B,MZ).          (2)

The complete coupled block on the right of (2), including the already
transported parent margin, has central coefficient

    [chi_0(U)chi_0(V)]R(Q',GM)=-1,074,148,800.

The inverse selector is columns (0,1), with no central factor two. Thus
the candidate requiring the complete low-center contribution and the
high-GF contribution separately nonnegative is false on a fully certified
canonical parent. The total child comparison is nevertheless strictly
positive; its smallest supported adjacent minor is 41,472. Cancellation
with the high-GF contribution is essential, even after all four low-M
pieces have been coupled.

The alternate representation hF-J does not evade this issue:

    R(Q',D')=R(hF,D')+R(D',J),

where its subtraction block has central coefficient -49,976,016 at the
same parent. A proof of hF<=D' alone is insufficient. Requiring that
comparison's full margin to dominate R(J,D') just restates the target.

## 4. Scope and bounded decision

ROOT and the established first children are unaffected. BOTH LONG strict
Q<D remains OPEN; no future child packet or target is assumed. The
corrected conditional chain requires two unsolved present-parent signs,
one of them strict over the full hD support. The coupled low-M split
fails already at a certified seed. These findings provide a reason to
stop this lane rather than count additional paths or rename the signed
gap. Full-tree strict Local TP2 remains OPEN.

Reproducer: `long_gate_verify.py`; compact exact output:
`long_gate_results.json`. Standard Python integer/Fraction arithmetic is
used. The finite checks certify only the explicitly stated witnesses;
the strictness diagnosis follows from the exact support argument above.
