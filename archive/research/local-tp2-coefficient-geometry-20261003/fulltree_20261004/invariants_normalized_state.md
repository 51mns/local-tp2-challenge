# A positive normalized state with an exact square constraint

**Status: proved global algebra and coefficient bounds; Local TP2 remains open.**
All coefficientwise statements in this note use the ordinary `x` basis. They must not be read as folded-kernel or Fourier likelihood-ratio statements.

## 1. Three positive state coordinates

Put `y=x+1`. Orient the endpoints by degree as `X,Y`, with `deg X<deg Y`, and let `C` be the center. Define

```
a=(X-1)/y,  e=(Y-X)/y,  g=(C-Y)/y,
X=1+ya,    t=3yX-x=2x+3+3y²a,    k=X(3X-2),
r=g-(t-2)e-k.
```

At the root `(a,e,r)=(0,1,1)` and `g=2x+3`.
The three independent state coordinates may be taken to be `(a,e,r)`; then

```
g=(t-2)e+k+r,
s=(U-C)/y=tg-r=(t-1)g+(t-2)e+k,
M=3yC+1-x=t+1+3y²(e+g),
d=(V-U)/y=eM.
```

The original quantities are `S=ys`, `D=yd`. Here `U,V` are the short and long children, respectively. Degree orientation determines which is the Farey left or right child; the labels below mean short/long, not a fixed letter L/R.

Both updates have an exact positive form:

| Move | new a | new e | new r | new g |
|---|---|---|---|---|
| Short child | a | e+g | g | s |
| Long child | a+e | g | e+g | s+d |

For example the new short remainder is
`tg-r-(t-2)(e+g)-k=g`, using `g=(t-2)e+k+r`.
For the long update, the new trace is `t'=t+3y²e` and
`k'-k=ye(6X-2)+3y²e²`; direct substitution gives `r'=e+g`.
The scalar mutations and both remainder formulas are also checked as symbolic identities in `Z[x,a,e,r]` by the independent sparse-polynomial verifier `invariants_normalized_verify.py`. Its checks hold off the Fricke surface as well.

## 2. Global positive bounds

At every canonical state:

```
a,e,r,g have nonnegative ordinary coefficients,
0 <= a <= e,
0 < r <= a+e,
g >= a+e+r+1.
```

Here `r>0` means a nonzero polynomial, and all inequalities are ordinary coefficientwise.

**Proof.** The root satisfies them. Given nonnegative `a,e,r`, the formulas for `t-2=2x+1+3y²a`, `k=(1+ya)(1+3ya)`, and `g` are positive polynomial expressions. The two updates therefore preserve nonnegativity. In addition,

```
g-a-e-r-1 = 2xe + 3y²ae + (4y-1)a + 3y²a²,
```

whose coefficients are nonnegative because `4y-1=4x+3`. This proves the growth bound whenever the coordinates are nonnegative.

For `a<=e`, the short update gives `e'-a'=(e-a)+g>=0`; the long update gives `e'-a'=g-a-e>=0`. For the remainder bound, the short update gives `a'+e'-r'=a+e`, and the long update gives `a'+e'-r'=a`. Positivity of the new remainder follows from `r'=g` or `e+g`. These observations prove the bounds at every depth.

Every nonzero `a`, and every `e,r,g,s,d`, has positive ordinary coefficients throughout its degree interval. This follows simultaneously from the same updates: sums preserve dense support, `t-2` and `k` have dense nonnegative support with positive constant and leading coefficients, and `g` contains `(t-2)e`; the root supplies the initial dense intervals. The zero polynomial `a=0` persists precisely when the endpoint `X=1` is retained. No Fourier shape conclusion follows just from this density.

If `T` is the endpoint replaced in the previous mutation, then at a nonroot state

```
r=(Y-T)/y,    a+e-r=(T-1)/y.
```

Indeed `C=tY-xX-T`, so `g-(t-2)e-k=(Y-T)/y`. At the root the same algebraic representation uses `T=1`, but `T` there is only an auxiliary boundary value, not a preceding canonical endpoint.

## 3. Fricke becomes a positive product identity

Let

```
I=X²+Y²+C²+x(XY+XC+YC)-3yXYC.
```

The exact residual identity is

```
I/y² = r g -(t-2)e² -2ke -3aX².                 (1)
```

This is checked symbolically, and the expression on the right is unchanged under both normalized updates. Thus its vanishing at the root proves the positive identity globally:

```
r g = (t-2)e² + 2ke + 3aX².                    (2)
```

Substituting `r=g-(t-2)e-k` also gives

```
g²=(t-2)e(e+g)+k(g+2e)+3aX².                   (3)
```

All summands on the right have nonnegative ordinary coefficients. This retains a nonlinear canonical constraint absent from generic positive triples.

There is a second useful exact form. Put `h=a+e-r>=0`. Then

```
e²-(2x+1)a(a+e)-e-2a = h(g+a+e),              (4)
```

and consequently

```
e² >= (2x+1)a(a+e)+e+2a.                       (5)
```

To prove (4), write the right side of (1) as the quadratic `F(r)=r[(t-2)e+k+r]-(t-2)e²-2ke-3aX²`. Its value at `r=a+e` is the left side of (4), and
`F(a+e)-F(r)=(a+e-r)(g+a+e)`.
On the canonical surface `F(r)=0`, giving (4). The verifier checks the stronger off-surface identity, with residual exactly `F(r)`.

The same normalization simplifies the fixed-endpoint Cassini constant:

```
g²-rs=X²(1+3a).                                 (6)
```

Off the canonical surface the difference between the two sides of (6) is exactly `-(t-2)F(r)`. Hence the verifier proves (6) as an algebraic consequence of Fricke, with no division by a polynomial. This supplies a compact Pell relation for the consecutive normalized gaps `r,g,s`; it still does not imply a bivariate coefficient-minor inequality.

## 4. A selective LR induction and its unresolved conditions

Write `P <=lr Q` for all ordered Fourier half-row minors of `(P,Q)` being nonnegative. A possible finite normalized invariant is

```
a <=lr e <=lr g <=lr s <=lr d,
```

together with folded-kernel membership for the canonical normalized endpoints and gaps `a,e,g,a+e,e+g,a+e+g` and the outgoing quotients. This is a candidate, not a theorem.

Some parts of its propagation are automatic. In the short update, `a'<=lr e'<=lr g'` follows from `a'=a,e'=e+g,g'=s` and the old chain. In the long update it follows from `a'=a+e,e'=g,g'=s+d`. A positive sum of rows below one fixed row stays below it, and a positive sum of rows above one fixed row stays above it.

The additional comparison `r'<=lr g'` is automatic by the same reasoning: in the short case it is `g<=lr s`; in the long case it is `e+g<=lr s+d`.

If the new gap `g'` has a folded TP2 kernel, the next link `g'<=lr s'` follows from the exact Christoffel-Darboux identity

```
W(g',s') = W(r',g') + W(g',t'g'),
```

where `s'=t'g'-r'`. The first term is nonnegative by the preceding comparison; the second follows from broadening with the nonnegative Fourier row of `t'` through the TP2 folded kernel of `g'`.

**The substantive missing steps are preservation of these actual folded kernels and the final comparison `s'<=lr d'`.** Moreover, the desired target uses `(ys',yd')`, so even quotient LR must be transported through multiplication by `y`; this transport has a central signed term and is not automatic. The exact target is

```
W_n(ys,yd)>0   for 0<=n<=deg(ys).
```

The positive state recurrence and constraints (2)-(5) have not yet been converted into these coefficient-minor inequalities.

## 5. Finite probes and limits

`invariants_probe.py` rebuilds the original scalar tree, divides the actual endpoint and gap polynomials by `y`, and independently checks the state formulas and identities. The saved bounded scan covers 255 states through depth 7, with maximum short quotient degree 121. It finds no failure of folded membership for `a,e,r,g,s,d` or the displayed quotient LR chain. This is finite evidence only.

A strengthened abstract package additionally requiring folded membership of `a+e,e+g,a+e+g` was stress-tested on 50,000 random integer triples; 1,498 met all filters and passed both updates. No general closure theorem follows from that experiment, and the sampled triples generally do not satisfy Fricke.

Arbitrary positive-mixture compatibility cannot be added as an invariant. At the canonical path `R`,

```
e=2x+3,
g=6x³+28x²+44x+24,
```

and their polarized folded defect at index 2 is `-12`, despite the actual sum being in the cone in the finite check. The general degree-support explanation is proved independently in `bivariate_mixed_support.md`. Thus a proof must control the actual mixture weights and canonical product constraints rather than assume convex closure.
