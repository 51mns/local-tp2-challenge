# A three-condition closure theorem for the first sandwich on the full tree

**Status:** the implication below is proved, with an unbounded induction.
Its three center hypotheses have not been established for the entire
canonical tree. Accordingly, this is a reduction of the global first
sandwich, not an unconditional proof of it.

Set `x=q+q^-1`, `y=x+1`, `P=x+2`. At a canonical triple with endpoints
A,B and center C, write

`U_A=3yAC-x(A+C)-B`, `S_A=U_A-C`,

and define U_B,S_B by interchanging A and B. Let

`t_C=3yC-x`.

Use `H(Q)[n]=[q^n]Q(q+q^-1)` and

`W_n(F,G)=H(F)[n]H(G)[n+1]-H(F)[n+1]H(G)[n]`.

The folded defect satisfies `W_n(C,xC)=delta_C(n)`.

## Three global center hypotheses

Assume that for every canonical center C:

1. Its folded convolution kernel `K_C` is TP2.
2. The folded convolution kernel `K_(t_C)` is TP2.
3. Its central defect has the scalar margin

   `delta_C(0)>=H(C)[0]+H(C)[1]`.

Only these hypotheses are conditional. The coefficient positivity and
support facts used below are already proved for the full tree in
`resumed_extension_kernel_support.md`: A-1 is nonnegative in the
positive-character basis, C dominates both endpoints in that basis,
and the canonical centers and gaps have dense positive Fourier rows.

## Conclusions

Under these three hypotheses, all the following hold at every canonical
triple, with no depth bound:

- `H(A),H(B)<=_lr H(C)`;
- `H(PA)<=_lr H(C-A)` and `H(PB)<=_lr H(C-B)`;
- `H(PC)<=_lr H(S_A)` and `H(PC)<=_lr H(S_B)`.

In particular, if the endpoints are sorted by degree as X,Y and
`E=Y-X`, then

`H(PX)<=_lr H(E)`.

These are Fourier-row statements. No first-difference MLR or unproved
J-kernel membership is used.

## 1. The child-gap lemma

Suppose at the current triple that `H(B)<=_lr H(C)`. There is an exact
decomposition

`S_A=(A-1)t_C+R_B`,

`R_B=2yC-x-B`.

Both summands are Fourier-nonnegative. For the first, A-1 is
positive-character-nonnegative and t_C has positive coefficients. For
the second, the globally proved bracket decomposition gives

`R_B=[2yC-C-y+1]+(C-B)`,

where both terms are positive-character-nonnegative and the first is
dense and strictly positive. Thus all LR comparisons and additions below
are between nonnegative rows; no subtraction closure is being assumed.

Write `a_n=H(PC)[n]` and `h_n=H(C)[n]`. Multiplication of both rows
`H(P)` and `H(3y)` by K_C gives the exact determinant identity

`W_n(PC,3yC)=3 delta_C(n)`.

This also follows by expanding `PC=xC+2C` and `3yC=3xC+3C`.
Consequently,

`W_n(PC,t_C)=3delta_C(n)-W_n(PC,x)`.

The last minor equals a_0 for n=0, equals -a_2 for n=1, and is zero
for n>=2. Since

`a_0=2(h_0+h_1)`,

the central scalar margin and cone nonnegativity prove

`H(PC)<=_lr H(t_C)`.

If A-1 is nonzero, the universal broadening property of the TP2 kernel
K_(t_C) gives

`H(t_C)<=_lr H((A-1)t_C)`.

If A=1, this zero summand is simply omitted.

For the other summand, direct bilinearity gives

`W_n(PC,R_B)=2delta_C(n)-W_n(PC,x)-W_n(PC,B)`.

The cone K_C gives `H(C)<=_lr H(PC)`. Together with the assumed
endpoint order, this implies `W_n(PC,B)<=0`. The n=0 inequality is
therefore guaranteed by

`2delta_C(0)>=2(h_0+h_1)=a_0`.

At n=1 the x contribution is favorable, and at n>=2 it vanishes. Thus

`H(PC)<=_lr H(R_B)`.

Each nonzero summand in the decomposition of S_A is above PC in MLR.
Linearity of the minors in the second row proves

`H(PC)<=_lr H(S_A)`.

The same proof with A and B exchanged gives the corresponding statement
for S_B.

## 2. The simultaneous induction

Maintain two properties at each triple:

`H(A),H(B)<=_lr H(C)`,

`H(PA)<=_lr H(C-A)`, `H(PB)<=_lr H(C-B)`.

The root is `A=1`, `B=P`, `C=2x^2+6x+5`.
Its relevant rows are

`H(C)=(9,6,2)`, `H(C-A)=(8,6,2)`, `H(C-B)=(7,5,2)`,

`H(PA)=(2,1)`, `H(PB)=(6,4,1)`.

The nontrivial adjacent minors for the two gap comparisons are `(4,2)`
and `(2,3)`, respectively; the endpoint comparisons are also immediate.
Thus the entire induction invariant holds at the root.

Consider the child triple `(A,U_A,C)`. By the child-gap lemma,

`H(PC)<=_lr H(U_A-C)`.

This is the required new gap comparison for endpoint C. Since K_P is
TP2 (its defects are `(2,1)`), the old endpoint order A<=_lr C also
gives

`H(PA)<=_lr H(PC)<=_lr H(U_A-C)`.

The retained-endpoint gap decomposes as

`U_A-A=(U_A-C)+(C-A)`.

Both summands are above PA: the first by the preceding chain and the
second by the old gap invariant. Their sum is therefore above PA.

Finally, the cone K_C gives C<=_lr PC. The child-gap lemma then gives
`C<=_lr S_A`, so `U_A=C+S_A>=_lr C`. Together with A<=_lr C this proves
the two new endpoint orders. This completes the induction for one
child, and the exchanged argument handles the other.

## 3. Recovering the endpoint first sandwich

At every nonroot node, its two endpoints are a retained endpoint A of
the preceding triple and that triple's center C. Their degrees satisfy
`deg C>deg A`, and the preceding center-gap invariant is exactly

`H(PA)<=_lr H(C-A)`.

Thus it is the required `H(PX)<=_lr H(Y-X)` at the new node.
At the root, `X=1`, `E=y`, and the only nonzero adjacent minor between
H(P) and H(y) equals 1, so the first sandwich holds there as well.

Useful additional consequences are `H(X)<=_lr H(Y)<=_lr H(C)` and,
by the TP2 kernel K_P,

`H(PX)<=_lr H(PY)<=_lr H(C-Y)`.

Also every child-center gap is at least PC and hence at least C in MLR.

## Precise remaining obligation

The general first sandwich is now reduced to proving the three listed
center conditions throughout the canonical tree. In particular, no
separate endpoint-gap MLR invariant needs to be guessed or verified at
unbounded depth. The current note does not establish those kernel and
scalar conditions, nor the second sandwich needed for full Local TP2.
