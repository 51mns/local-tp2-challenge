# Canonical proxy cancellations and the remaining sign connection

Status: the product exchanges, center-block reduction and exact obstacles
below are proved. The finite curvature pair in `proxy_curvature.md`
has conditional BOTH-child closure. Strict child proxy preservation
from parent P_Q remains OPEN. No scalar mass gate or arbitrary positive
sum closure is invoked.

## 1. Fricke removes the proxy subtraction before positivity

At an actual degree-oriented state set c=3yC-x=M-1 and P=x+2.
The proxy pair has the useful equivalent form

    Q=cX-PC, Pi=PMX.                                    (1)

Let I=X²+Y²+C²+x(XY+XC+YC)-3yXYC. Direct expansion gives

    YQ=G²+X²+xXC-I, G=C-Y.                              (2)

Indeed cXY=X²+Y²+C²+xC(X+Y)-I, and subtracting
PCY cancels the xCY term and leaves (C-Y)². On every actual
canonical state I=0. Thus (2) is a positive ordinary product identity
for the proxy itself, retaining the actual endpoint/center correlation.

Write U=C+S and V=C+Fout for the actual short/long children.
The Fricke invariant is preserved exactly by mutation, so BOTH child
proxy subtractions have the corresponding completed form

    C Q'_short=S²+X²+xXU,
    C Q'_long=Fout²+Y²+xYV.                             (3)

Off Fricke, both right sides in (3) have the same error -I as (2).
The verifier directly checks the universal residuals in Z[x,X,Y,C].
These identities improve on separating the negative terms in the prior
proxy-flux expansion: each child Q' is now tied to the actual incoming
gap square and the retained endpoint. All terms on the right have
nonnegative ordinary/Laurent coefficients. This statement is not
character-cone positivity of those terms or of their sum.

In two-character notation (3) gives the exact reductions

    T_C R(Q'_short,Pi'_short)
       =R(S²+X²+xXU, CXP M'),
    T_C R(Q'_long,Pi'_long)
       =R(Fout²+Y²+xYV, CYP M').                        (4)

A positivity proof of the right sides alone would not finish the child
proxy, because LR convolution does not reflect order. For example take
the actual canonical multiplier Croot=2x²+6x+5 and the noncanonical test
pair (y,xy). Its central LR minor is -1. After multiplication by Croot,
the pair is (yCroot,xyCroot), whose defect row is (31,91,26,4), all
positive; therefore its complete character polynomial is nonnegative.
This is an exact obstruction to universal cancellation of T_C, not an
actual proxy counterexample. A reflection/cancellation theorem for the
specific correlated pair in (4) would be an additional required lemma.

## 2. The center-conditioned block has only one adjacent correction

For any endpoint J at fixed center C define Q_J=cJ-PC and Pi_J=PMJ.
Common-product transport and bilinearity give

    R(Q_J,Pi_J)=T_J Gamma_C-T_P R(C,MJ),
    Gamma_C=R(M-1,PM)=T_M-D_(PM).                       (5)

Here D_F=R(1,F). This is a complete signed center-conditioned
formula; the two terms in (5) are not assumed to be nonnegative
separately. It specializes to J=X or Y without treating endpoints as
independent parameters.

Because D_(PM) has character coefficients only on the diagonal,
its adjacent boundary contains only H(PM)_1 at n=0. Consequently

    [chi_0chi_0]Gamma_C=delta_0(M)-H(PM)_1,
    [chi_(2n)chi_0]Gamma_C=delta_n(M), n>=1.             (6)

Let h=H(yC). Since M=3yC+1-x, exact expansion at the folded
central index gives

    delta_0(M)-H(PM)_1=9delta_0(h)+3h_0+6h_1.           (7)

Thus parent K_M TP2 plus the single explicit condition
9delta_0(yC)+3H(yC)_0+6H(yC)_1>=0 implies all-pairs LR for
(M-1,PM), using the actual positive dense interval supports. A
nonnegative delta_0(yC) gives strict central positivity, but it does
not control delta_n(M) at n>=1. In particular, K_(yC) alone does
not imply that all of Gamma_C is nonnegative; K_M remains an explicit
hypothesis. Strictness throughout also needs positive interior
delta_n(M), not merely TP2. The terminal minor is already positive
because its value is the squared leading coefficient of M.

This one-central-index condition is a local analytic reduction, not a
return to a scalar strength-times-mass gate. Its BOTH-child propagation
and its ability to dominate the remaining signed correction in (5)
have not been proved.

## 3. Positive curvature is closed, but the Cassini forcing can be negative

`proxy_curvature.md` proves that the two arrays

    kappa_X=D_G²-D_R D_S,
    kappa_Y=D_(G+E)²-D_(R-E) D_Fout

are nonnegative at both first-level seeds and preserve nonnegativity
under BOTH child maps, assuming the parent regular P_Q and both parent
curvatures nonnegative. The proof keeps the signed preceding fixed-C
seed, uses the exact sibling relation ycB=ycA+TE, and uses the LR
links that are already consequences of P_Q. The ordinary bound
cA<=Te supplies valid canonical seed information but is not converted
silently into a Fourier inequality in that sign proof.

For actual Cassini K=G²-RS, the exact polarization is

    2T_G-J(R,S)=Sigma_K-L kappa_X,
    Sigma_K=Phi(K(xi)+K(zeta)), L=(U²-4)(V²-4).          (8)

Before Phi this is just the difference-of-values expansion of
G²-RS=K, with L=(zeta-xi)². The signed L cannot be dropped.
Writing b_n=[chi_(2n)chi_0]kappa_X,
c_n=[chi_(2n)chi_2]kappa_X and a_n=c_n-3b_n, the boundary
of -L kappa_X is

    n=0: 3a_0-a_1,
    n>=1: 2a_n-a_(n-1)-a_(n+1).                        (9)

Equation (9) follows from chi_2 chi_j=chi_(j+2)+chi_j+chi_(j-2)
when j>=2, with the central boundary handled separately. The finite
arrays are zero extended. Curvature positivity does not determine
these second differences.

There is an exact **actual canonical** obstruction at the first short
child. Its entire kappa_X character array is nonnegative, but

    b=(45,36,16), c=(36,56,0), a=(-99,-52,-48),
    boundary(-L kappa_X)=(-245,43,-44,48).                (10)

Thus the proposed inference "positive curvature gives nonnegative
polarized-Cassini forcing" is false on a genuine reachable state.
Its incoming G has defects (192,256,112,16), all positive, so (10)
is neither a gap-cone nor a proxy counterexample. The other terms in
(8) cancel the negative sources. The network lane independently
derived (9) and (10); the reproducer here checks (10) directly by
Clebsch-Gordan multiplication of the complete saved curvature array.

## 4. Conclusions and exact reproducibility

The nontrivial new positive transport is the finite two-curvature
companion. The new proxy reductions (2)--(7) retain canonical
correlations and identify an explicit cancellation/reflection problem
and a central block correction. They do not eliminate any of the three
original child gates. No conclusion here presupposes a child proxy.

| Statement | Status |
| --- | --- |
| Positive ordinary Fricke proxy exchanges at BOTH children | PROVED |
| Center-block identities and single-central-index reduction | PROVED |
| Curvature pair, first-level seeds and conditional BOTH closure | PROVED; independent analytic audit passed |
| Positive curvature implies favorable Cassini forcing | FALSE at actual first-short child |
| Parent P_Q plus curvature implies a child proxy/cone | OPEN |
| Strict proxy BOTH preservation / full-tree Local TP2 | OPEN |

Exact files: `proxy_curvature_verify.py`, `proxy_curvature_results.json`,
`proxy_fricke_verify.py`, `proxy_fricke_results.json`. They use integer
polynomial arithmetic and the read-only character transform foundation.
Only root and first-level arrays were computed, to prove finite seeds
and reproduce the exact obstruction. No larger scan is presented as
closure evidence.
