# Exact four-punctured-sphere specialization and its TP2 limitation

**Status:** proved algebraic bridge and exact obstructions to two shortcuts.
This does not prove Local TP2 or refute it. It adds a precise route into
the skein literature without identifying generic positivity with the
required coefficient-minor inequality.

## 1. A specialization of the full skein cubic, including boundary data

Let `y=x+1`, and for an original generalized Markov coordinate `G` set

`t_G=3yG-x`, `kappa=x(x+2)`, `omega=2x^3+3x^2+4`.

For formal, independent `A,B,C`, direct expansion gives the residual identity

```
t_A^2+t_B^2+t_C^2-t_A*t_B*t_C
    + kappa*(t_A+t_B+t_C) + omega-4
 = 9*y^2*(A^2+B^2+C^2+x*(A*B+A*C+B*C)-3*y*A*B*C).
```

Thus canonical coordinates satisfy

`t_A*t_B*t_C=t_A^2+t_B^2+t_C^2+kappa*(t_A+t_B+t_C)+omega-4`.

The affine correction is essential. Under the original mutation
`U=3yAC-x(A+C)-B`, the transformed mutation is exactly

`t_U=t_A*t_C-t_B-kappa`.

This is also an exact specialization of the presentation in Bousseau,
*Strong positivity for the skein algebras of the 4-punctured sphere and
of the 1-punctured torus*, arXiv:2009.02266v2, Theorem 6.12, equation
(126). Set its skein parameter to `A_skein=-1` and its four peripheral
curve variables to `(x,x,x,2)`. Its three `R` parameters become `kappa`,
and its parameter called `y` becomes `omega` (it is not our `x+1`).
The three commutator relations then vanish, and the cubic is exactly
the one displayed above.

There is an explicit monodromy realization, so this is more than a match
of cubic coefficients. With the already proved matrices from
`../continuation_network.md`, put

`P_t=Q_t*J`, `K=[[-1,0],[3y,-1]]`.

At a canonical Farey triple, take the four boundary monodromies to be

`P_A, P_C, P_B, K^(-1)`.

Their product is the identity. Their traces are `(-x,-x,-x,-2)`.
Furthermore

`tr(P_A*P_C)=-t_B`, `tr(P_C*P_B)=-t_A`.

The third trace is

`tr(P_A*P_C*P_B*P_C^(-1))=tr(K*P_C^(-1))=-t_C`.

For any canonical `Q=[[G,s+x],[s,d]]`, direct multiplication of
`P=QJ` gives `tr(K*P^(-1))=x-3yG`, proving all three statements.
The actual pair `P_A*P_B` need not have trace `-t_C`; its unconjugated
pair trace corresponds to the other Vieta root. The presentation and
the two Vieta mutations fix the same canonical coordinate tree from
its seed, so no unproved Fourier property is being inserted into this
identification.

The three seed values are

`t_0=2x+3`, `t_1=3x^2+8x+6`, `t_(1/2)=6x^3+24x^2+32x+15`.

The equal peripheral specialization is preserved by permuting the first
three punctures. It therefore causes no parameter mismatch at a switch
between canonical left and right mutations.

## 2. What the external theorem actually establishes

Bousseau's Theorem 1.2 states that bracelet multiplication structure
constants are nonnegative Laurent polynomials in the skein parameter
and nonnegative polynomials in its three `R` variables and `y` variable.
These are **multiplication structure constants**, not minors of two
Fourier coefficient rows. In particular the result does not identify
the desired antisymmetrized, two-variable quotient with a positive
linear combination of bracelets. The deformation variable `q` in
`x=q+q^(-1)` is a peripheral specialization here, not the skein quantum
parameter, which has already been specialized to `-1`.

The exact bridge is useful for a proposed skein proof: one can now ask
for a positive resolution of the specific normalized two-variable
Bezoutian. A statement only about positive products in the skein basis
does not supply that resolution.

Primary source: https://arxiv.org/pdf/2009.02266v2
Relevant locations: Theorem 1.2; equations (6)--(7); Section 1.2.3;
Theorem 6.12, equation (126).

## 3. Bracelet positivity alone does not imply Fourier MLR

Let the value of a single annular curve be `z=x+2`, and use the bracelet
normalization `T_2(z)=z^2-2`, `T_3(z)=z^3-3z`. Then

```
P=T_2(x+2)=x^2+4x+2,
Q=T_3(x+2)=x^3+6x^2+9x+2.
H(P)=(4,4,1),
H(Q)=(14,12,6,1).
```

Both ordinary and Laurent coefficients are nonnegative, and the
bracelet algebra has its positive product rule. Nevertheless their
central comparison minor is

`H(P)_0*H(Q)_1-H(P)_1*H(Q)_0=4*12-4*14=-8`.

This is an exact counterexample to importing a generic bracelet-positive
or degree-ordered trace statement as Fourier MLR. It is **not** a
canonical AIMath counterexample and does not exclude a proof that uses
the actual coupled pair of outgoing gaps.

## 4. The normalization has a precise signed character factor

Let `L=U-C`, `R=V-C` be the actual short and long outgoing gaps. Their
trace-coordinate gaps are `ell=3yL`, `r=3yR`. Define

`B_(P,Q)(s,z)=(P(s)Q(z)-Q(s)P(z))/(z-s)`.

Then, universally,

`B_(ell,r)(s,z)=9*(s+1)*(z+1)*B_(L,R)(s,z)`.

Apply the earlier exact transformation
`s+z -> UV`, `sz -> U^2+V^2-4`, and use
`chi_j(U)=U_j(U/2)`. It gives

```
R_(ell,r)=9*T_y*R_(L,R),
T_y=chi_2(U)+chi_2(V)+chi_1(U)*chi_1(V)-1.
```

Thus the passage back from traces to the requested gaps is division by
a tensor with a negative trivial-character coefficient. It is not an
automatic positive-cone operation. The following elementary example
shows that even multiplication by `y` does not reflect Fourier MLR:

```
P=y, Q=xy:       adjacent minors = (-1,1),
yP=y^2, yQ=xy^2: adjacent minors = (4,0,1).
```

One cannot prove a weak trace-gap MLR comparison and then cancel `3y`.
Any skein or character proof must retain the normalization or prove a
separate cancellation theorem for the canonical pair.

## 5. Verification and remaining task

`external_skein_bridge.py` verifies the universal residual identity and
the transformed mutation with sparse integer multivariate arithmetic,
independently of a tree-depth scan. It also verifies both displayed
counterexamples and the character multiplier exactly.

No source checked supplies a positive lift of the normalized Bezoutian,
or a canonical cancellation theorem. Those are concrete missing
mathematical statements; the skein theorem alone does not close full
Local TP2.
