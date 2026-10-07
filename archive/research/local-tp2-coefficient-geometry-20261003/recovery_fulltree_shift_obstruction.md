# A universal obstruction to the shifted-power approach

Status: exact obstruction to a proof strategy, **not** a counterexample to
canonical Local TP2. The canonical full-tree theorem remains open.

Write

\[
H(P)_n=[q^n]P(q+q^{-1}),\qquad
K_a(m,n)=H((x+a)^m)_n.
\]

A natural Cauchy–Binet strategy would expand each gap in the basis
\((x+a)^m\), prove nonnegative coefficient rows with likelihood-ratio
order in \(m\), and transport that order through a TP2 kernel \(K_a\).
There is **no real constant shift \(a\)** for which both of the following
hold:

1. The entire kernel \(K_a(m,n)\), \(m,n\ge0\), is nonnegative TP2.
2. Every canonical short gap has nonnegative coefficients in \(x+a\).

In fact the root short gap alone rules out the second condition whenever
the first could hold.

## Proof

Nonnegativity of the entry \(K_a(1,0)=a\) forces \(a\ge0\).
The first two nonconstant power rows are

\[
K_a(1,\cdot)=(a,1,0,\ldots),\qquad
K_a(2,\cdot)=(a^2+2,2a,1,0,\ldots).
\]

Their minor in columns 0 and 1 is

\[
a(2a)-(a^2+2)=a^2-2.
\]

Consequently condition 1 requires \(a\ge\sqrt2\).
At the canonical root, independent substitution into the original
mutation recurrence gives

\[
S(x)=8+20x+16x^2+4x^3=4(x+1)^2(x+2).
\]

Set \(u=x+a\). The coefficient of \(u^2\) in \(S(u-a)\) is

\[
16-12a.
\]

Condition 2 therefore requires \(a\le4/3\). These conditions are
incompatible because \(2>16/9\), equivalently \(\sqrt2>4/3\).
This proves the obstruction. Positive rescaling of the affine basis
generator does not repair it: it scales rows and coefficients by
positive factors and changes neither sign condition.

## The unshifted-to-y compromise also fails on actual canonical data

Choosing \(y=x+1\) keeps the root short-gap coefficients nonnegative,
but its full power kernel already has the negative minor \(-1\) above.
Moreover even coefficient positivity does not survive the first left
move. At that canonical state,

\[
S(x)=21+71x+86x^2+44x^3+8x^4,
\]

and hence

\[
S(y-1)=-y+2y^2+12y^3+8y^4.
\]

Thus a blanket claim of nonnegative y-coefficients for all canonical
gaps is false. This is an actual canonical obstruction, unlike abstract
triples that fail the Fricke identity.

There is also a root obstruction to y-coefficient likelihood-ratio
order. The exact root rows are

\[
S(y-1)=(0,0,4,4),\qquad D(y-1)=(0,2,2,6,6),
\]

so their determinant in degrees 1 and 2 is \(-8\).

## Scope and remaining question

This excludes the simple combination of a single shifted monomial
basis, nonnegative gap coefficient rows, and unrestricted TP2
transport. It does not exclude signed cancellation, a different basis,
a restricted-degree kernel with separately bounded correction terms,
or a direct paired-network proof using the canonical Fricke/Cassini
identities. No counterexample to the desired Fourier minors is
asserted.

`recovery_fulltree_shift_obstruction.py` verifies the displayed symbolic
coefficient identities and reconstructs the root and first-left gap
directly from the original scalar recurrence. The contradiction above
is an algebraic proof for all shifts; a finite scan of shifts is not
used.
