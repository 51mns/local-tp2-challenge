# Independent logical-scope review of the arbitrary-path continuation

**Verdict: the stated global algebraic results and conditional lemmas do
not, separately or together, close Local TP2 on the full canonical tree.**
The reviewed manuscripts currently preserve that distinction. This review
checks logical dependencies and scope; it does not repeat the separate
symbolic audits or claim external peer review.

## 1. Reviewed claims and their exact reach

| Manuscript | Established reach | Premise or conclusion still missing |
| --- | --- | --- |
| `invariants_normalized_state.md` | Positive normalized updates, ordinary coefficient bounds and support, and Fricke/Cassini identities at every canonical depth | Preservation of the proposed folded kernels; the complete quotient LR chain; final transport through multiplication by `x+1` |
| `network_quotient_constraints.md` | Sharp scalar coefficient bounds and polynomial barriers at every depth and every barrier index | A quadratic Fourier-minor bound using these ordinary coefficient constraints |
| `quantitative_subtraction.md` | Exact subtraction identity and nonnegative remainder under hypotheses that hold for canonical `F,G,C` | Control of the complete margin `B_n+R_n`; the stronger sufficient invariant `B_n>=0` is false |
| `quantitative_shifted_trace.md` | A uniform theorem for every real shift in `[-2,2]`, conditional on smoothed strength `lambda>=4` | The necessary canonical smoothed-strength premise, with separate handling of ineligible small seeds |
| `bivariate_mixed_support.md` | All-degree polarization/support identities and exact canonical failures of an enlarged mixed-tensor invariant | Positivity of the complete target Bezoutian under arbitrary canonical mutations |

The all-depth normalized statements are supported by explicit induction
and identities, not by the depth-seven scan. In particular the barrier
proof simultaneously assumes all `m` at the preceding tree depth; its
short-child step uses `m-1` at that preceding depth. This is a valid
induction and leaves no unverified large-`m` tail.

The ordinary coefficient order in the first two notes is never itself a
Fourier likelihood-ratio order. The positive Fricke products and the
normalized Cassini identity are same-variable polynomial identities;
they are not identities asserting positivity of bivariate minors.

## 2. Character-positivity premises really are available

The canonical application in `quantitative_subtraction.md` depends on
`../resumed_extension_kernel_support.md`, Sections 2--4, reviewed in
`../resumed_extension_support_audit.md`. That prior all-tree theorem
establishes, for every canonical endpoint or center `P`, a positive
integer expansion in

`B_j(q)=sum_(i=-j)^j q^i`,

with `alpha_P(j)=H(P)_j-H(P)_(j+1)` and `alpha_P(0)>=1`.
It separately establishes support and positivity of canonical gaps.
No canonical folded-kernel assertion is required for that theorem.

For `t_X=3(x+1)X-x`, its `B` coefficients are exactly

```
3alpha_X(1)+1                         at index 0,
3(alpha_X(0)+alpha_X(1)+alpha_X(2))-1  at index 1,
3(alpha_X(j-1)+alpha_X(j)+alpha_X(j+1)) at j>=2.
```

These are nonnegative using the proved `alpha_X(0)>=1` premise.
The proved product rule

`B_i B_j=sum_(r=|i-j|)^(i+j) B_r`

therefore makes `F=t_XY` character-nonnegative, and makes `H(F)`
nonincreasing. The inverse endpoint `T` is canonical at a nonroot
state; the root uses the auxiliary value `T=1`. Thus `G=xX+T` and
`C` have nonnegative Fourier rows. Multiplication by `y=x+1=B_1`
preserves the needed character nonnegativity of `F` and Laurent
nonnegativity of `G,C`. The subtraction lemma's assumptions in both
the ordinary and smoothed applications are consequently unconditional.

This reasoning establishes the **hypotheses of the subtraction
identity**, not the required sign of its complete margin. It does not
silently assume the folded conclusion being sought.

The `B_j` character basis here is different from the second-kind
`chi_j` basis in the bivariate notes. Their relation is already specified
in the earlier bivariate manuscript. Positivity in the first is a linear
half-row shape statement; positivity of the particular bivariate tensor
in the second is a quadratic statement. They must not be substituted
for one another.

## 3. Conditional claims and excluded shortcuts

The normalized LR propagation statements are correct as conditional
claims. The nonzero canonical rows have dense initial support and
strictly increasing degrees, so the relevant LR comparisons compose;
the possible zero `a` row is harmless. Positive sums preserve a
comparison with one fixed upper or lower row. The identity

`W(g',t'g'-r')=W(g',t'g')+W(r',g')`

does prove the next indicated comparison **if** the required folded
kernel of `g'` is known. No reviewed proof establishes that invariant
under both arbitrary child updates.

The shifted-trace lemma likewise has a genuine global-in-shift proof,
but a conditional input. Its monotonicity follows from the input
strength by telescoping the defect differences and using symmetric
logconcavity. Its terminal index forces `v_d>=lambda`. In particular
the lemma with `lambda>=4` cannot be applied to the root center
`P=2x^2+6x+5`: `H((x+1)P)` has terminal entry 2. The boundary endpoints
`1` and `x+2` also fail that necessary threshold. Earlier specialized
ray/seed arguments may treat these cases; the new lemma alone does not.

The updated subtraction manuscript reports an exact negative sufficient
bound at `R^13`, `lambda=0`, `n=0`, together with a larger positive
remainder and positive actual defect. Thus `B_n>=0` is **refuted as a
universal canonical invariant**, not merely unproved. The bounded
depth-seven observations cannot be promoted to an induction. This
scope review does not independently rerun that large-integer example;
its executable and the separate arithmetic review carry that role.

The mixed-tensor support obstruction also occurs on canonical data,
including the root. It rules out insisting that every mixed component
be character-positive. It does not rule out cancellation in the complete
target or refute Local TP2. The manuscript now correctly refers to
strict positivity of the **required adjacent minors** in its examples,
rather than suggesting every position in an array with forced zeros
must be strictly positive.

## 4. The original target still includes a signed central condition

With the normalized coordinates, the actual target is

`S=ys`, `D=yd`, `d=eM`,

and requires `W_n(ys,yd)>0` for every `0<=n<=deg(ys)` at every
canonical state. This is not the same as proving the quotient
comparison `s<=lr d`.

For precision, write

`W_ij=H(s)_i H(d)_j-H(s)_j H(d)_i`.

Direct expansion of multiplication by `y` gives

```
W_0(ys,yd) = -W_01+W_02+2W_12,
W_n(ys,yd) = W_(n-1,n)+W_(n-1,n+1)+W_(n-1,n+2)
              +W_(n,n+2)+W_(n+1,n+2),  n>=1.
```

This is the same exact normalization embodied in `../tp2_source.py`
(`qw_value`). Quotient LR would control all summands for `n>=1`;
the central expression retains a negative term. Neither all-tree
quotient LR nor the extra strict central inequality has been proved
by this continuation. Other direct proof routes could establish the
actual target without these particular intermediate conditions.

The bivariate equivalent, already proved algebraically in
`../recovery_fulltree_bivariate_character.md`, is positivity of

`[chi_(2n)(U) chi_0(V)] R(S,D)`.

The new support lemmas do not make that boundary positive after an
arbitrary mutation; they identify some signed terms that must be kept.

## 5. What can honestly be reported

There is no unsupported all-tree TP2 conclusion in the reviewed source
versions. Their union gives stronger exact canonical constraints,
valid conditional analytic estimates, and explicit exclusions of
several tempting larger invariants. It does **not** give an arbitrary-
path induction, a certificate covering every canonical state, or a
counterexample to Local TP2.

The earlier `../GENERAL_ONE_TURN_RESULT_JA.md` explicitly proves
`L^m R^k` for all `m,k>=0`, and explicitly does **not** extend this to
all `R^m L^k` by symmetry. Therefore the remaining range should not be
described solely as paths with at least two direction changes. General
right-first one-turn paths are also outside that specific theorem,
except for separately proved subfamilies.

The separate symbolic reviews are `audit_normalized_report.md` and
`bivariate_audit_quantitative.md`. Their PASS verdicts certify the
stated identities and conditional lemmas, not full Local TP2. The
reviewed source hashes are recorded in `external_scope_audit_sources.json`.
