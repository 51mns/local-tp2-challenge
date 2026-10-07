# Independent audit of the remaining common gates

**Verdict: common closure remains open.** This lane proved no preservation
of the three analytic gates and found no child failure of the frozen
regular predicate. It did find an exact off-Fricke obstruction to two
auxiliary implications sometimes needed by an easy product/proxy proof.
This is not a canonical counterexample and is not a counterexample to
the proposed predicate itself.

## 1. What the completed reduction does and does not establish

The four LR links in `reduction_common.md` really do propagate through
both degree-ordered mutations once the parent has the two kernel gates
and strict proxy. Their proof uses actual same-row minor identities,
not an invalid assertion that arbitrary positive sums preserve a folded
cone. The strict target follows from the parent predicate, including the
terminal support index.

For the original proposed `root OR P_Q` predicate, the exact status is:

| Component | ROOT / first children | short preservation | long preservation |
|---|---|---|---|
| four actual LR links | proved, with explicit root exceptions | proved conditionally on the full parent predicate | proved conditionally on the full parent predicate |
| folded kernel of actual incoming gap G | proved | open | open |
| folded kernel of actual multiplier M | proved | open | open |
| strict proxy `W(Q,XP M)>0` | proved | open | open |

The actual long-gap boundary lemma removes one support boundary under an
additional strength hypothesis. It does not decide the overlap band.
The bandwidth theorem cannot establish a missing cone gate: its premise
already assumes the dominant kernel is TP2.

## 2. Exact auxiliary obstruction inside the abstract finite class

Set

`a=x^2`, `e=x^2+(x+1)^5`, `r=(a+e)/2`.

The coefficient arrays, in increasing ordinary powers, are

`a=(0,0,1)`, `e=(1,5,11,10,5,1)`,

`r=(1/2,5/2,6,5,5/2,1/2)`.

Using the universal normalized definitions, this state satisfies all
ordinary positive bounds, strict degree orientation, dense positive
Fourier support, all four regular LR links, both folded-kernel gates,
and the strict proxy at every required index. Both children satisfy
the same complete predicate. The exact checks are saved in
`gate_t_obstruction_results.json`.

Nevertheless,

`X=(1,0,1,1)`, `H(X)=(3,3,1,1)`,

`delta(X)=(-6,8,-3,1)`;

`t=(3,2,3,6,3)`, `H(t)=(27,20,15,6,3)`,

`delta(t)=(334,-110,114,-18,9)`.

Also `H(yX)=(9,7,5,2,1)` has defects `(28,-7,12,-2,1)`.
Thus **ordinary bounds plus the complete parent `P_Q` do not imply
`K_X` TP2, `K_t` TP2, or positive strength of `H(yX)`** in the broader
off-Fricke class.

The Fricke residual is nonzero (its constant coefficient is `-7/4`), so
this is explicitly outside the canonical class. It only excludes a
generic proof route that silently derives these extra hypotheses from
the frozen finite gates. It does not show that Fricke is necessary for
closure: generic closure itself remains unresolved.

Reproduce with

`python gate_t_obstruction.py`.

The reproducer uses exact integers/Fractions and imports only the
current campaign's `falsification_probe.py` polynomial arithmetic. It
asserts the complete parent/child gates and ordinary bounds before
recording the failed auxiliary endpoint/trace defects.

## 3. Independent quantitative manuscript audit

Audited `quantitative_common_gates.md` at SHA-256
`8250cf4a5bb4a27c6e314463f240d358c9f7170564a78d7dafde331681693cfe`.

The reference-band all-minor theorem is valid. The adjacent cell bound
uses only three consecutive defects and monotonicity of h. For a fully
positive rectangle, retaining the bottom-right cross-ratio is legitimate:
its displacement is exactly `|j-l|`, which is within the reference
degree. If an off-diagonal vanishes, `alpha>=2` supplies the needed
factor four through the diagonal product. This covers unbounded kernel
indices and support boundaries without enumeration. Its actual scalar
application is refuted at the stated canonical witnesses, so it cannot
serve as an invariant for this campaign. The unconditional
`s>=5r+3` observation is valid and supplies coefficient domination;
it does not repair the missing defect threshold.

The strict trace-base formulas and `lambda>4/3` threshold are valid,
including central and terminal indices. The direct proxy absorption
argument is also valid. Retaining the principal `(n,n+1)` intermediate
pair gives the correct lower bound `w_n delta_0(C)`. The signed
correction rows vanish at the claimed cutoffs. The explicit upper bound

`beta_X <= (63X(2)-12)/(9lambda-12)`

is correct: `p<=yX`, `v<=y^2X`, and
`H(y^2X)_(n+1)<=3H(yX)_n`; evaluation at 2 gives
`3A(2)+L(2)=63X(2)-12`.

These are new sufficient hypotheses, not consequences of original
`P_Q`. In particular, the exact auxiliary state above violates both
`K_X` and the trace-strength premise while satisfying `P_Q`. On the
canonical tree a separate endpoint/center strength invariant must
provide these premises and transport the central-mass inequality.

The nonroot leading-coefficient inequality and conditional long-child
support boundary are valid. A positive strength margin makes D strictly
decreasing, so the negative mixed term at `deg S+1` is absorbed by the
stated leading-coefficient bound. All later indices inherit D exactly.
No conclusion about indices `0,...,deg S` follows from that argument.

## 4. Discovery scope and final classification

`gate_optimize.py` used constrained floating-point discovery in two
frozen scopes: positive constant a with e of degree two, and a=0 with
e of degree four; r was independently coefficientwise bounded by a+e.
It found no negative child gate. The saved optimization files are
discovery logs only, not exact evidence or a mathematical certificate.
No further random search was run after consolidation began.

The exact auxiliary obstruction is separate from these searches and
is independently replayed with rational arithmetic. No actual canonical
state violating `P_Q` closure has been found. No generic admissible
parent with a failing child has been found. No all-tree kernel or Local
TP2 theorem is claimed.
