# Independent audit of the finite common LR reduction

Verdict: the algebra, target implication, regular-state four-link closure, and exceptional root-to-first-level seeds in `reduction_common.md` are valid. The three analytic gates are correctly left open. This audit does not promote the reduction to an all-tree proof.

## Independent arithmetic and seed audit

`network_reduction_audit.py` uses the network lane's direct sparse Laurent arithmetic, not the polynomial/Fourier arithmetic in `reduction_common.py` and not any parent implementation. It builds the original scalar children at x=q+q^-1 and computes the capital-letter gaps directly. In particular it defines R=tG-S without dividing by y, independently of the normalized reconstruction.

The exact root rows, both first-child rows, all four proposed regular LR links, and both gate-defect lists match the manuscript. The strict proxy margins match exactly, including central and terminal indices:

| seed | W(Q,Pi) through deg Q |
|---|---|
| root | (48,176,88,24) |
| short child | (2004,5772,3448,1008,96) |
| long child | (1221944,2423832,1730408,638012,121452,10764,324) |

The independent direct target root minors are (272,352,160,24). The root E<=G and R<=G links both fail centrally with -2, so the separately specified root seed is necessary. Both children satisfy the regular predicate exactly. No root LR failure was silently turned into a weak inequality.

The checker independently verifies the following identities at both first-child transitions:

- D=EM, Q=(t-2)C-xX, and Pi=PQ+V;
- short/long E,G,R updates;
- both equivalent child Q formulas, child Pi and V formulas, and M_child=M+3yG_child;
- W_n(Q,Pi)=delta_n(Q)+W_n(Q,V), for every supported Q index;
- both G-child defect polarizations and the M-child defect polarization, including the central reflection and upper-support zero extension.

These finite checks validate the displayed examples and implementation. The universal formulas are also checked algebraically below; the finite checks are not offered as an induction proof.

## Target implication and support

For every ordered pair i<j, bilinearity and Q=S-G give

    W_(i,j)(S,Q)=W_(i,j)(G,S).

Thus G<=lr S is exactly sufficient for S<=lr Q. The folded TP2 kernel of the actual M transports XP<=lr E to Pi=XP M<=lr EM=D. Positive dense support and the strict adjacent Q-to-Pi margins give the required strict sandwich at every n<deg S.

The degrees are degQ=degS=p+c+1, degPi=p+c+2, and degD=q+c+1>=degS+1. Therefore S,Q,Pi,D are positive at both adjacent indices when n<degS. This validates transitivity without dividing by a zero coefficient. At n=degS, the target is directly H(S)_n H(D)_(n+1)>0. No smoothing step by y is used in this implication.

The identity W_n(Q,PQ)=delta_n(Q) also holds at n=0: the reflected row gives H(PQ)_0=2q0+2q1 and H(PQ)_1=q0+2q1+q2, so the result is q0²-2q1²+q0q2. The top two indices follow by zero extension. The exact proxy decomposition Pi=PQ+PX+P²C is therefore valid over the full supported range.

## Four-link closure under both children

The base 1<=lr P<=lr t comparison is valid. For the only potentially nontrivial adjacent base minors,

    W0(P,t)=3H(X)0+6H(X)2-2>=1,
    W1(P,t)=H(t)2>=0.

All later ordered minors either have a nonnegative entry from the degree-one P row or vanish. Multiplication by the actual TP2 kernel K_G gives G<=lr PG<=lr tG. Since R<=lr G, one has R<=lr PG. For every ordered pair, not only adjacent pairs,

    W(PG,S)=W(PG,tG)+W(R,PG)>=0,
    W(G,S)=W(G,tG)+W(R,G)>=0.

This supplies PG<=lr S and G<=lr S without requiring K_R, K_P, or K_t to be TP2. The target criterion then supplies S<=lr D using only the stated parent gates.

The sum CP=YP+PG is below the fixed row S because both terms are below S. This uses bilinearity of two-row minors, not folded-cone convexity. The short child's links then follow from E<=G<=S, R'=G, XP<=E and XP<=G, and CP<=S. The long child's links follow from G<=S<=D, E<=G, the old YP<=G, and CP<=S<=D. Summing rows below a fixed comparison row is valid at every ordered pair; combining target rows S+D is valid because each needed source lies below both S and D.

Canonical positive initial-interval supports ensure that any ratio-based transitivity proof is legitimate on common support, while indices beyond the shorter support give zero or positive minors directly. The mathematical proof can equivalently avoid ratios throughout by using the stated all-ordered LR relation and this support observation.

## Remaining scope

The complete common-state argument now isolates only:

1. folded TP2 of G_child;
2. folded TP2 of M_child;
3. strict child proxy surplus delta(Q_child)+W(Q_child,V_child)>0.

The displayed exact closure equations retain the canonical subtraction and mixed terms. No sign for their individual summands has been inferred. In particular the negative terms in the two G polarizations and mixed terms in the M polarization cannot be dropped, and y is not presumed cone-preserving.

The manuscript's overall ROOT / IMPLIES TARGET / partial LEFT-RIGHT statuses are accurate. The established four-link subsystem is a substantive common transport mechanism, but preservation of the three analytic gates remains necessary before asserting arbitrary-path Local TP2.

Reproduce the independent exact audit with:

```
python network_reduction_audit.py
```

Output: `network_reduction_audit_results.json`. Shared foundation: the mathematical folded multiplication/TP2 transport theorem and canonical positivity/dense-support/degree facts. Shared implementation: only `network_exterior_reproducer.py`, within this lane; no reduction or parent arithmetic import.
