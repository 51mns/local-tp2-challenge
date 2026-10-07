# Frozen actual paired-midpoint search

Frozen before computation; write only falsification_* here. Prior files
are read-only. No generic off-Fricke search and no unrestricted random
or deep-tree scan.

The state is rebuilt from normalized root (a,e,r)=(0,1,1), using degree
short s / long l moves. At each state T=M-1, c=c_A=e+g+s. Test BOTH
origins (b0,b1)=(c,e) and (e,c). For each origin and each parameter pair

    (-2,-2),(-2,2),(2,2),(0,0),(-1,1),(0,2),(-2,0),(1,2),
    (-3/2,3/2),(3/2,3/2),(3/2,2),(-1/2,1/2),

set u=(r+s)/2 and H=b0(T-r)(T-s)+b1(T-u). Test H and yH.
Record shift/L/yL support and folded defects for every distinct endpoint
parameter occurring in this grid. A defect failure is already a precise
actual MP_2 obstruction.

The actual scope is all seven states through depth2, plus s^j (j<=12),
ls^j (j<=10), l^j (j<=6), and (sl)^j,(ls)^j (j<=5), with midpoint degree
cap160. Repeated paths are removed. Enumeration order is path length,
then s before l. Minimal means earliest in this frozen scope, not a
global all-tree minimum.

Direct uniform and sharp relative gate:

    det K_H>=4 det K_b1,
    det K_H>=((r-s)^2/4) det K_b1.

Use a proved all-ordered-minor strength theorem only as a positive exact
certificate when its premises hold: lambda=min delta(H)_n/H_n,
alpha=min H_n/b_n, alpha>=2, deg H>=deg b, and b_n<=b0;
lambda*alpha>=8b0 certifies uniform4. This is a
genuine ALL-index certificate for a fixed state/parameter, not a claim
that scalar-gate failure is a minor failure. If that certificate does
not apply, inspect the exact finite relative band below. The corresponding
threshold for factor c is2c*b0.

## Complete finite band for a positive reference minor

Let D=deg h>=d=deg b, assume folded TP2 of h and only NONNEGATIVE b
entries (no reference cone hypothesis). If det K_b>0, its
two diagonal entries are positive, hence |k-i|<=d,|l-j|<=d. Write
u=j-i>0, v0=k-i, v1=l-j, with |v0|,|v1|<=d and u+v1-v0>0.
If u>D+d both off-diagonals of BOTH kernels vanish. Those rectangles
are covered by the exact entrywise ratio check h_n²>=c*b_n² for all
reference n. Otherwise 1<=u<=D+d. Once i>D+d all reflection sums are
past D and the rectangle is Toeplitz; every further translation is
identical. Therefore enumerate 0<=i<=D+d+1, 1<=u<=D+d,
v0,v1 in [-d,d], retaining valid nonnegative ordered indices and
positive reference determinants. This covers ALL ordered minors with
positive reference. Nonpositive references are automatic from TP2 of h.
Central column scaling is evaluated by the exact folded kernel, not a
Toeplitz shortcut. If the ratio check fails, record a far Toeplitz exact
witness. If a reference or tested row fails its cone hypothesis, do not
use the automatic reductions and record that failure separately.

Before computation add the network lane's proposed exact character
reduction: relative ALL ordered folded minors are equivalent to relative
minors of rows(0,1) and ALL column pairs0<=k<l<=D+1. Those row(0,1)
differences equal all character coefficients of the associated bivariate
relative product; the other row-pair factors are character-positive.
Use this as a complete certificate only after independent proof audit.
Before that audit, negative rows(0,1) are valid global counterexamples
and passes are labelled restricted, unless the all-minor strength lemma
also supplies an independent positive certificate.

No pass is extrapolated to continuous r,s or arbitrary actual paths.
If no exact actual obstruction is found, stop this scope and derive an
analytic extremal identity or audit the packet lane rather than expand.
