# Frozen exact falsification predicates

Frozen before the first new scan, 2026-10-03. Paths use `s` for the
degree-short update and `l` for the degree-long update; these are not
the original Farey L/R letters. Enumerate breadth-first, `s` before `l`.
Every actual state is rebuilt twice, from the original scalar mutation
and from the positive normalized recurrence. Ordinary coefficient arrays
are ascending in x. Fourier rows use the exact binomial transform.

## Scope and predicates

The first scope is the entire degree-ordered tree through depth 6
(127 states). This is a bounded falsification scope, not a closure proof.
Do not extend it simply to accumulate target passes.

* F: folded defects of each a,e,r,g,s,d and each y-smoothed version.
  Zero a is allowed separately; other rows have interval support.
* O: fixed orientation e<=lr r, and separately r<=lr e, tested to
  diagnose whether either can be part of a common ordering predicate.
* R(h,b): the scaled sufficient relative-minor premise, with exact
  lambda=min(delta_n(h)/h_n) and alpha=min(h_n/b_n), requiring
  lambda>0, b_n<=b_0, and lambda*alpha>=8b_0. Probe (h,b)=(g,e),
  (s,r), and their smoothed versions. This is a sufficient premise,
  not a necessary condition for minor dominance.
* A (common_quantitative): H(C) is lc(C)-strong and H(yC) is
  lc(C)/2-strong at every supported index.
* B (common_quantitative): every H(3yC-x-u), -2<=u<=2, is
  3lc(C)/4-strong. Minimize the exact quadratic margin in u on
  the closed interval; this is not endpoint sampling.
* T (common_reduction): P1=x+2, X=1+ya, Z=a+e+g,
  t=3yX-x, J=y(t-2), M=2P1+3y²Z, b=(t-2)(e-a)+2k+r.
  T1: yb<=lr S=y(tg-r). T2: XP1<=lr ye.
  T3: JZ<lr XP1M at all 0<=n<=deg(JZ).
  T4: M and Z have nonnegative folded defects.

Revision frozen after first scope and before rerun: reduction corrected
its earlier root-exclusion sign error; T2 at root has W0=+1, so include
the root for all T predicates. Add T5: Q=S-yg strictly precedes XP1M
through deg Q; T6: yg is folded and yr<=lr yg. These are the alternate
Q companion's additional gates. The shifted-trace quadratic's central
linear coefficient was independently corrected to -2h0-h2+lambda
(reflection gives delta0=h0²-2h1²+h0h2) before final evidence.

Second revision frozen before the targeted run: C (common_quantitative)
uses F=tY, G=F-C, f=H(F), g=H(G), c=H(C), and the exact nonnegative
subtraction remainder R_n in ../fulltree_20261004/quantitative_subtraction.md.
Require delta_n(c)-lc(C)c_n>=R_n/32, and separately use all three
y-smoothed rows with strength lc(C)/2. Check the identity B+R directly.
Targeted fixed-endpoint scope: s^j and ls^j for 0<=j<=80; additionally
prefixes ss l, sl l, lll, lsl, slsl followed by 0..12 s moves, and
alternating sl/ls words with at most 16 moves and degree cap 400.
Stop extending a ray when a new actual failure is located; retain all
predecessors to certify minimality along that ray. This is a focused
test of a uniform remainder fraction, not a large tree sweep.

Third revision frozen before extra probes:

* D (common_quantitative): actual G=yg has lc(G)/2 strength, optionally
  full lc(G) strength for nonroot. Short S=tG-R with R=yr must have
  surplus delta(S)-lc(S)S_n/2 >= remainder(tG,R)_n/32. Long G'=S+D
  must have lc(G')/2 strength. Scope all depth<=6 and s^j (j<=35),
  ls^j (j<=20).
* Relative-band refinements (common_quantitative): d=deg(b),
  alpha=min_{0<=n<=d}(h_n/b_n), lambda_local=min_{0<=n<=d+1}delta_n/h_n;
  and sharper L_d=min_{0<=a<=d} of delta_a/h_a and
  (delta_a+delta_(a+1)+delta_(a+2))/(h_a+h_(a+2)). Both require
  alpha>=2 and scalar strength*alpha>=8b0. Probe h=s,b=r and ys,yr
  on complete short ray j=0..60 (small degrees), not the whole tree.
* Spectral packet corners (common_invariant): fixed-X
  (tau,c,d)=(t,g,-r), fixed-Y=(t+3y²e,e+g,e-r); fixed-X a=0 excluded.
  For r,s,u each in {-2,2}, check folded membership of tau-r,
  L=c(tau-r)+d, yL, H=c(tau-r)(tau-s)+d(tau-u), yH.
  Scope all depth<=4 plus ls^j (j<=8), lls^j (j<=6). Corner passes
  do not establish the continuous parameter packet. Record actual
  coefficient witnesses first; do not infer continuum or closure.

Focused packet revision frozen before ray execution: fixed-X=P1 states
ls^j, 0<=j<=80, only midpoint endpoint (2,2,-2) and its smoothing;
iterative recurrence and original scalar crosscheck, all defects, stop
on a negative. No relative-minor or continuous parameter assertion.

Small abstract regular-row test (common_reduction), frozen before scan:
drop only the canonical Fricke equation; retain ordinary bounds 0<=a<=e,
0<r<=a+e and g>=a+e+r+1, plus E<=G, R<=G, XP1<=E, YP1<=G,
folded G and M, and strict Q<XP1M. Enumerate a constant in {0,1,2},
e=e0+e1*x with 2<=e0<=10, 1<=e1<=5, and all r=r0+r1*x
with 0<=r0<=a+e0, 0<=r1<=e1, r nonzero. Test both child updates
against the same gates. Any noncanonical witness is explicitly an
abstract obstruction only; it does not refute the Fricke predicate.

Narrow rational extension frozen before rerun: a0,a1 in {0,1/2,1};
e0=a0+v0, v0 in {1,2}; e1=a1+v1, v1 in {1/2,1};
e2 in {1/2,1}; r_i=(a+e)_i*w_i, independent w_i in {1/4,1/2,1}.
Thus 1944 exact rational states with linear a and quadratic e/r.
All parent regular gates and both full child surrogate predicates are
checked, with the Fricke equation omitted. Also freeze outgoing actual
D=EM half-leading-coefficient strength on the existing 170 gap states.

LR orientation means h_n v_(n+1)-h_(n+1) v_n>=0. Supported
adjacent minors suffice for dense positive rows; exact witnesses are
saved when a negative adjacent minor disproves an all-order assertion.
All tests include central n=0 and terminal support. Minimal means
shortest path within the complete breadth-first scope (then s before l,
then smallest failed index), not smallest polynomial coefficient.

The old R13 rough-subtraction failure is already known and is not a
new deliverable here. The script imports none of the earlier code.
