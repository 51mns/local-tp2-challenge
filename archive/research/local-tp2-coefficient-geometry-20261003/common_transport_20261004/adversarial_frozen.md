# Frozen targeted generic-closure probe

Frozen before computation. Only this new directory's adversarial_* files
are written. Earlier code is read-only. The known a=x² auxiliary endpoint
witness is not reproduced.

The structural Fricke classification is proved in
adversarial_classification.md, independently audited with the root lane.
Thus the remaining search is explicitly OFF-FRICKE unless its residual
vanishes, in which case a positive ordinary state is actual by descent.

For m=0..6, L in {1,4,16}, h in {0,1,4,16,64}, set

    a=4L((x+1)^m+h*x^m).

For N=m+1..m+5 and B in {1,4,16}, put

    e=(2x+1)a+1+B(x+1)^N,
    r=e+rho*a, rho in {1/4,1/2,3/4,1}.

This is a 6300-state deterministic integer family, with no random
sampling. It ensures all ordinary bounds a>=0,e>=a+1,r>=1,r<=a+e,
e>=(2x+1)a, g>=a+e+r+1, dense ordinary support, deg a<deg e,
and dense positive Fourier support. Since r>=e, every network barrier
Q_j(t-2)r-P_j(t-2)e is ordinary-positive for all j, by Q_j-P_j>=0.
The golden-ratio lower bound is automatic; the upper bound is not
silently inferred and is checked through the rational sufficient 3r<=5e.

Before child checks, require ALL regular P_Q gates: E<=lrG,R<=lrG,
XP<=lrE,YP<=lrG, folded G/M, and strict W(Q,XP M) on Q support.
Test BOTH complete child predicates, focusing on G/M/proxy failures.
The four inherited LR links are still explicitly checked.

Record character multiplicative strip, endpoint character support,
strict endpoint degrees, and the inverse-neighbor degree pattern on
every accepted parent, rather than assuming them. An exact child failure
is decisive only for the hypotheses it actually meets. Full Fricke
residual and exact arrays/rows accompany any witness.

Stop this family after the first full-parent child failure. If none is
found, report the finite scope only; do not expand indefinitely. The
Fricke classification is not a finite-scan inference.

Before execution also include the 105-state inherited family obtained by
one exact long update from (a_old,e_old,r_old)=(0,a,a), with the same
105 choices of a above. Equivalently e=(2x+1)a+1+a, r=e+a. This family
retains a genuine positive normalized ancestor, strict canonical degree
pattern, integer/dense support, and all ordinary network barriers at
that ancestor and at the tested parent. Test whether the ancestor also
has P_Q, rather than assuming it. Its Fricke residual is a(a-1), so it
is off-surface for these a. This is a targeted correlation family, not
an arbitrary random perturbation.
