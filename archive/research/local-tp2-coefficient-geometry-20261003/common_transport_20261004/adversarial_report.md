# Structural Fricke audit and one frozen generic-closure probe

**Outcome:** a self-contained positive-ray degree-descent classification
was proved and independently checked with the root lane. The frozen
generic search found no child failure. Neither result proves the three
original analytic P_Q closure gates or full-tree strict Local TP2.

The classification is detailed in `adversarial_classification.md`.
The integer Laurent precedent is Bittmann et al., arXiv:2602.14802v1,
Proposition 2.3. This note labels the integer consequence as a
reproof/adaptation, with no novelty claim. The proof here explicitly
works over R[x] under strict positivity for every x>=0: evaluation at
x=0 forces every constant coordinate to exceed 2/3, eliminating the
exceptional 1/3 degree cancellation without an integrality assumption.
Mutation preserves positive-ray values via CC*=A²+B²+xAB>0. The sum
of degrees strictly descends to the unique positive constant triple111.

Consequently the campaign's ordinary-positive Fricke states, even with
real coefficients, are actual mutation-orbit states. Their integrality
is a conclusion. This rigorously separates the OFF-FRICKE generic probe
from the actual-state problem; there is no unrelated positive normalized
Fricke class to exploit for an abstract counterexample.

## Frozen structural probe and precise scope

The two deterministic integer families were frozen before execution in
`adversarial_frozen.md`. The new reproducer is standalone and imports
only Python standard-library arithmetic. It uses exact integers and
binomial Fourier transforms; no discovery floats or random samples.

For m=0..6,L in {1,4,16},h in {0,1,4,16,64}, put
a=4L(y^m+h*x^m). The 6300 perturbed states have
e=(2x+1)a+1+B*y^N, N=m+1..m+5,B in {1,4,16}, and
r=e+rho*a, rho in {1/4,1/2,3/4,1}. The 105 inherited states are exact
long updates from the positive normalized ancestor (0,a,a).

Each tested parent meets all stated ordinary bounds, integer/dense
ordinary support, strict current endpoint degrees, and dense positive
Fourier support. Since r>=e, every ordinary network barrier is positive
for all orders by the known Q_j-P_j>=0 identity. The inherited ancestors
also have r=e and the same barrier property. These are structural
constraints preserved by construction, not inferred from a finite
barrier cutoff. Character strip/support and inverse degree pattern were
separately checked and recorded, not silently assumed for the whole class.

ALL parent P_Q gates were required before inspecting children:
E<=G,R<=G,XP<=E,YP<=G; folded G and M; strict proxy W(Q,XP M)>0
at every supported Q index. BOTH complete child predicates, including
the four LR links and all G/M/proxy gates, were then checked. Central
reflection and terminal zero-extension are explicit in the code.

| Family | Tested | Full parent P_Q passes | Both complete children pass |
|---|---:|---:|---:|
| Perturbed integer family | 6300 | 1872 | 1872 |
| Inherited integer family | 105 | 16 | 16 |
| Total | 6405 | 1888 | 1888 |

Among accepted parents, the individually checked additional conditions
had these counts: rational sufficient golden strip1638; dense character
support of X,Y,C,E,G,R1756; character multiplicative strip1712; strict
character additive separation1888; endpoint character inequalities1616;
inverse canonical degree pattern58. These counts are **individual**, not
claimed to describe one joint subset. Twelve of the inherited accepted
parents also have a full P_Q ancestor. Every accepted state is off
Fricke; the reproducer explicitly asserts its residual is nonzero.
The inherited residual is a(a-1).

No actual or abstract child obstruction was found in this scope. This
does not prove generic closure, and it does not promote a finite lattice
test to a continuous or all-degree result. The search stopped at the
frozen families, as requested; no canonical tree depth was increased.

## Independent small-degree conclusions

The classification note includes an independent exact valuation proof
that eta=e-r=0 on Fricke forces the normalized root. It also eliminates
the constant-a/linear-e,r Fricke family: positive constant a forces only
the first long state(1,2x+3,2x+4); a=0 with genuinely linear e,r forces
only the first short state(0,2x+4,2x+3). These are structural rigidity
results, not new TP2 path-family claims.

## Reproduction and remaining obligations

Run from this directory:

    python adversarial_probe.py

The output is `adversarial_results.json`, containing the frozen scope,
exact counts, accepted examples, and a field reserved for any exact
full-parent child witness (null in this run). Proof and audit do not
depend on finite numerical passes.

| Statement | ROOT | BOTH CHILDREN | IMPLIES TARGET |
|---|---|---|---|
| Positive-ray Fricke class | contains111 and the canonical root | positive-ray Fricke preservation proved; descent classifies the orbit | not established |
| Generic P_Q plus the constructed ordinary constraints | parents filtered exactly | only the stated bounded passes | inherited implication from P_Q; no new proof here |
| Full-tree analytic closure | earlier roots remain foundations | G/M/proxy preservation still requires proof | strict Local TP2 remains open |

Only new `adversarial_*` files were written. Prior work is read-only;
no GitHub or external write was used. The packet origin-certificate
subsystem is reviewed separately in `adversarial_packet_audit.md`.
