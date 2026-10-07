# Independent full-continuum strictness-witness audit

**PASS** for `audit_packet_weakening.md` Section 6. The paired witness
T=10x+1+5sqrt(17), e=1, c=2 satisfies W_01 on the full continuous
parameter square, while failing MP_sharp at one endpoint. This is
abstract and noncanonical; no canonical or target failure follows.

Independently use 4<sqrt(17)<21/5, proved by rational squaring. For
q∈[-4,2], write B=1+5sqrt(17)-q and d=q+4∈[0,6]. Then

    B>19, B<=5+5sqrt(17)<26,
    delta0(y(T-q))=d(10sqrt(17)-d).

The latter is zero exactly at q=-4 and positive otherwise. The raw
defects B^2-200,100 are strictly positive throughout, as are the y
index-one and terminal defects B^2+10B-200,100. Thus both actual
single orientations are weak in the whole box, and strict at r=0,-1.
At reverse r=-2 the y-central defect is zero. The strict degree
condition is 0<1 and all interval supports are positive.

The midpoint factors have roots in [-4,2], by the independent exact
root-domain inequalities already used for the preceding linear paired
certificate. Their raw/y products are weak cones. The reference T_y
has central coefficient -1 and its only positive independent selectors
(0,2),(1,2) equal one. The independently derived uniform lower bounds
are 20000 for raw central, greater than 375801 at y selector (0,2),
and greater than 91611 at y selector (1,2). Each exceeds the largest
uniform reference 16; other reference coefficients are zero or negative.
The full finite-character equivalence proves all ordered mixed minors
throughout the continuous square. No parameter sampling is involved.

Therefore the displayed pair really is W_01 and not MP_sharp. This
audits strictness of the weakening as an abstract certificate, not its
arbitrary-parent preservation. The independent exact Q(sqrt(17))
identity/rational-bound replay is `falsification_weakening_audit.py`
with saved result JSON. The spectral zero-count/consumer theorem is
outside this witness-only audit.
