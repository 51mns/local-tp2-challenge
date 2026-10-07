# Independent audit of the root and first-child midpoint certificates

Verdict: **PASS** for the complete finite-base continuum theorem in
`quantitative_midpoint_bernstein.md`. This initializes the original
uniform-4 paired MP_2, and the weaker sharp paired packet, at the root
and at BOTH actual first children. Arbitrary regular-state changed-center
preservation is not proved.

## Actual input and independent arithmetic

`audit_midpoint_base_verify.py` imports no producer arithmetic. It starts
from the original scalar triple

`X=1, Y=x+2, C=2x^2+6x+5`

and computes the two original mutations

`U=3(x+1)XC-x(X+C)-Y`,
`V=3(x+1)YC-x(Y+C)-X`.

The root and first-child triples are respectively `(X,Y,C)`, `(X,C,U)`,
and `(Y,C,V)`. For each actual triple it independently reconstructs
`e=(Y-X)/(x+1)`, `c=(U-X)/(x+1)`, and `T=3(x+1)C-x`, using exact
ordinary division. These match every recorded trace and seed in both
orientations. This route does not use the producer's normalized-state
Fricke recurrence to generate its base input.

The auditor then substitutes `x=q+q^-1` and directly expands the
parameter polynomials at `r=2-4u, s=2-4v`. It forms the full first-two-row
all-column-pair Laurent minors and reconstructs every recorded Bernstein
coefficient, including the inverse Bernstein-to-power expansion. No
floating point or parameter sampling occurs.

## Full tensor coverage, parameter boxes, and boundaries

For a polynomial of degree D, the producer's tensor loop includes
ALL pairs `0<=i<j<=D+1`, using `H(f)` and `H(xf)`. The terminal
degree-D+1 column is present. Relabeling by
`(a,b)=(i+j-1,j-i-1)` and its transpose covers the complete finite
equal-parity symmetric character array. At i=0 there is one copy.
This is the entire first-two-row relative tensor, not an adjacent-only
test. The independently audited network equivalence promotes this
finite array to EVERY ordered folded minor at unbounded kernel indices.

The exact relative parameter bidegree is (2,2); all nine coefficients
of the full closed unit cube are checked for every character index.
Absent sparse entries are zero. The separate L and trace tensors have
univariate degree at most two, so all three interval-Bernstein
coefficients are checked. All supported defect indices from zero
through the terminal degree are reconstructed with reflection and
zero extension. The effective smoothed seeds both gain one degree;
their degree inequality remains strict.

Positive support is checked separately. Every T-2 and both seeds are
dense ordinary-positive polynomials. The corner polynomials L_2 and
H_22 are reconstructed and agree with their saved ordinary arrays.
Their positive constant/base terms, together with the nonnegative
`alpha=2-r, beta=2-s` block expansion, give fixed positive interval
support on the complete parameter square. The strict seed-degree bound
prevents leading cancellation. Multiplication by y is used here only
for ordinary support; its folded cones are checked independently.

## Exact certificate counts and logical implication

| Independently reconstructed family | Bernstein coefficients | Verdict |
| --- | ---: | --- |
| Full sharp and uniform-4 relative tensors, all 12 records | 30,348 | Nonnegative |
| Pure H, L, and trace full character tensors | 17,607 | Nonnegative |
| All supported strict H and L defects | 1,512 | Positive |
| All supported strict trace defects | 45 | Positive |

The pure-tensor split is 15,174 H, 2,202 L, and 231 trace slots.
The strict-defect split is 1,242 H and 270 L slots. All manuscript
degrees, counts, and displayed minima agree with the exact results.

Pure H/L/trace cones are certified separately. In particular no inference
of H TP2 is made solely from a relative bound against a reference with
possibly negative minors. The raw and y-mode arrays are computed and
audited separately; y is never assumed to be a cone multiplier.
The negative reversed-root smoothed power coefficient `delta_0(y)=-1`
is a correct obstruction to power-coefficient positivity, and does not
conflict with the positive Bernstein certificates.

The final Section 3 corner interpretation is also correct. With
V=U+4A and W=U+8A+16B, direct polarization gives the displayed
J(U,V)/2, T_V-4T_b1, J(U,W)/4+T_V/2+2T_b1, and J(V,W)/2 arrays,
including all reference coefficients and normalizations. It is expressly
a sufficient correlated Bernstein certificate; corner cone membership
alone and necessity of Bernstein positivity are not asserted.
The final generator's formal check works in the seven free quadratic
symbols, including the independent reference tensor, and correctly
checks this universal identity rather than extrapolating from base states.
Its added output flag is true; the regenerated archive was replayed after
this final change and all mathematical arrays remained unchanged.

Combined with the prior first-level LR/proxy seeds and exact register
transport, the result establishes the augmented-root-to-regular-predicate
initialization at BOTH children. The general A_sharp packet transport and
regular-edge strict proxy remain OPEN; no full-tree induction follows.

Reproduce from this directory:

```bash
python audit_midpoint_base_verify.py
```

The auditor checks the deterministic gzip archive and its uncompressed
payload against the summary hashes before rebuilding the certificates.

## Frozen source identities

| Source | SHA-256 |
| --- | --- |
| quantitative_midpoint_bernstein.md | 3ffdba42b10b12b9fb99cb1709acf74e7772055f9884dfdf84b9225a24054e0f |
| quantitative_midpoint_bernstein.py | f5493c952da7444eed5d42972ab09c277a07a94d3847971d2d4de3f944d8628c |
| quantitative_midpoint_bernstein_results.json | 955f7a226aad769794bc7d73b97172400db75635a640462d742ea9f8ab003c7b |
| quantitative_midpoint_bernstein_full.json.gz | f15175c91b32e83cd306f6382a07efeab4bb3c457bf9c9c4893894a2edeb89cc |
| Full uncompressed certificate payload | f327efbd821aba82504b2708ffd980e00d6b68877c672e5788e0192248096d14 |
| network_relative_character.md | 0ed6f97744bb78e810438285c6cd7e1520197940b6e5c57881c9692f29fa617d |

Full-tree strict Local TP2 remains OPEN.
