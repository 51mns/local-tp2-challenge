# Supervisor audit and scope of promotion

**Full-tree strict Local TP2: OPEN.** This checkpoint promotes a conditional
common-state reduction and the explicitly delimited lemmas below. It is not
a completed proof or a machine-checked formalization of the full theorem.

The primary deliverable is `RESULT_JA.md`; the exact expanded state and its
two remaining obligations are in `packet_expanded_predicate.md`. The original
campaign brief records the starting three-gate formulation, not the final
expanded-state ledger.

## 1. Origin registers and the two remaining obligations

The supervisor checked both mutation identities, both previous/current
register equalities, and the index bounds. Keeping only the outgoing-term
identity would not determine the recurrence boundary; the final predicate
therefore keeps both. The smaller register must have N>=2. A retained
larger register starts at N>=1 and becomes a smaller register at N+1>=2.
The new larger register starts at 1 on short and 2 on long.

These facts supply CURRENT K_G from the smaller previous term. CURRENT K_M
comes from the current midpoint packet's shifted trace at rho=-1, since
T+1=M. Hence old P_Q follows from the expanded regular predicate. Old P_Q
then provides the target and four child LR links. The child register data
and its origin certification are algebraically transported from the parent.

No future-state target claim is embedded in the registers. They hold fixed
origin polynomials and a current integer index; the origin packet theorem
provides an all-index implication. The packet condition remains a genuine
analytic universal minor condition and is not reduced to finite sampling.

The old independent-u packet can be weakened to its midpoint restriction
MP_2 for BOTH origins and current pairs: the Jacobi mixture uses only
u=(r+s)/2, and the path spectrum is in [-2,2]. The old stronger initial
packets imply the narrowed initial packets. The optional radius-5/2 theorem
is not used to initialize the root Y origin; that origin would fail its
larger shifted-trace box.

The root is an explicit exceptional clause because the regular LR links
fail there. Its target, packet and register initialization are established.
Prior first-level FULL P_Q supplies root-child LR and strict proxy. It does
not supply root-child new-center midpoint packets. Consequently obligation
A includes the root edges; obligation B is still open on regular parents.

This leaves two TYPES of analytic closure assertion: new current paired
MP_2, and strict proxy. Neither is proved here. A sufficient strengthened
predicate may be harder to preserve than the original one; the bookkeeping
reduction does not establish a numerical estimate of remaining work.

## 2. Auxiliary lemmas independently audited

| Claim | Audit | Promoted scope |
| --- | --- | --- |
| Origin subsystem, midpoint weakening, fixed-origin block theorem | `adversarial_packet_audit.md` | Conditional statements with root/index exceptions retained |
| Trace factors through radius 5/2 and Robin propagators | `center_trace_audit.md` | Explicit sufficient coefficient hypotheses; their child preservation open |
| Local multiplier theorem and centerbase | `center_multiplier_audit.md` | K_C, three local half-strength bounds and B0 premise required |
| Two bivariate curvatures | `center_curvature_audit.md` | Conditional BOTH closure under parent P_Q; exact first-level seeds |

The supervisor independently checked the trace central cubic bound and its
degree-0/1 exceptions; the multiplier sum-of-squares inequality and degree-2
terminal treatment; and the two curvature identities and their LR signs.
The classification proof was checked by degree descent on the positive
real ray. Its integer Laurent classification case is an adaptation of the
cited existing result, not a novelty claim.

For the optional forked spectral argument, Schur pivots stay >=1/2 at
radius 5/2 for every finite stem length. Both signs of the matrix are
covered. Resolvent residues may be zero; they need only be nonnegative and
sum to one. Repeated eigenvalues are handled by grouped residues and common
factors. q_-1=-b1 is needed at N=0. The N=0 midpoint's strictness follows
from strict diagonal cone products and nonnegative mixed terms; it is not
assumed from a merely weak H gate.

## 3. Negative evidence and reproducibility

The actual first-short negative signed-Cassini correction is reproduced by
two independent lanes. Its negative entries disprove one attempted forcing
inequality, while the actual gap defects remain positive. Abstract packet,
multiplier, character-shape and convolution-reflection obstructions retain
their explicit noncanonical scope. None is a counterexample to the target.

`verify_campaign.py` replays formal polynomial identities and finite
seeds/obstacles against the saved exact results. Lane manifests verify
frozen sources and outputs. `replay_results.json` records the successful
replay. The old bounded off-Fricke search is not expanded or used as a
general proof. The analytical all-index arguments are contained in the
notes and independent audits, not inferred from the replay sample sizes.

All previous repository files are preserved. The checkpoint adds only this
new directory to the private research branch; no main/public write is part
of this campaign. The public reference was reread at unchanged commit
6e770f3b3e3f26af5df5308572917559343b68f4.
