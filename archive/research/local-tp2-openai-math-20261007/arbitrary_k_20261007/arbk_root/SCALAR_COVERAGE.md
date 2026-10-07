# Exact coverage of all (m,k) by finitely many scalar checks

**Primary status: PROVED_INTERNAL.** All scalar values and ratios were
independently reconstructed, and their infinite monotonicity was reviewed.

This supplements `GENERIC_ARBITRARY_K_CLOSURE.md`. All inequalities in
this note are rational inequalities. `verify_scalar_closure.py` records
both their exact values and the consecutive ratios; no floating-point
comparison is load-bearing.

## Definitions

Write d=m+2, D=2(dk+2), D_J=2(dk+3), b=2dk-3. Given certified old
normalized bounds e_j, put

\[
a=e_k/2,\quad z=e_{k-1}/729,\quad
 f=az/D,\quad l=f/4,\quad g=lz/D.
\]

For a fixed m<=69, compute T=T_m(2) by `u_0=1,u_1=7,u_(j+1)=7u_j-u_(j-1)`
and summation. Use

\[
M=5+27T,\quad \alpha=TM^{k-1}/b,\quad
s=9\alpha,\quad c=18\alpha^2,\quad
\beta=((M+2)/(2d+1)-1)^2.
\]

All are rigorous lower bounds for the quantities to which they are
applied, by the separate mass-domination proof. The eight reported
scalar gates are

\[
G_1=f\beta s/12,\quad G_2=gs^2/48,\quad
G_3=lzc/(96D_J),\quad G_4=lc/(96\cdot1296),\quad
G_5=zs/(2D),\quad G_6=c/2,\quad G_7=s,\quad G_8=\beta.
\]

All eight exceed one at their listed corner. G_8 is constant in k;
all seven others have consecutive k ratios greater than one there.
The two separate correction gates G_3,G_4 ensure the minimum in the
closure theorem, so no branch of a minimum is silently omitted.

## The fixed-m ranges

| m | Old normalized bounds e_j | Proved for all k at least |
|---|---|---:|
| 0 | `1/(256·3^j)` | 21 |
| 1 | `(1/301)(1/4)^(j-1)/(4j)` | 11 |
| 2 | `(1/513)(1/4)^(j-1)/(4j)` | 6 |
| 3 | `(1/785)(1/4)^(j-1)/(4j)` | 5 |
| 4 | `(1/1114)(1/5)^(j-1)/(4j)` | 4 |
| 5 | `ell_5 r_5^(j-1)/(4j)` | 5 |
| each m=6,...,69 | `ell_m r_m^(j-1)/(4j)` | 3 |

The exact real-interval Bernstein certificates give
`r_m=e_m^trace/[2(m+3)]` and ell_m as the smaller normalized bound of the
old single and its y multiple. Every value and its input hash is in
`scalar_closure_results.json` and the referenced certificate tables.
The short trace blocks for m=1,...,4 and the paired-root blocks for m=0
are derived in `../arbk_mixed`; they are not numerical root samples.

Each of G_1,...,G_7, for fixed m, is a positive constant times an
exponential in k, divided by a product of nonnegative powers of the
positive linear factors

`k`, `k-1`, `dk+2`, `dk+3`, `2dk-3`.

For m=0 the k and k-1 factors are simply absent because no resolvent
weight loss is needed. Each consecutive ratio is therefore a constant
times factors

\[
\left(\frac{Ak+B}{A(k+1)+B}\right)^p,
\qquad A,p\ge0,\quad Ak+B>0.
\]

Every such factor is increasing in k. Consequently the exact ratio
check at the listed threshold proves every later value of every gate.
The old strength bounds are

\[
\Lambda_{m,j}=\frac{3\,2^{2m-3}(3\,2^{m-1})^{j-1}}{2j}
\quad(m\ge1),\qquad
\Lambda_{0,j}=9^{\lfloor j/2\rfloor}.
\]

They are nondecreasing in j; the fixed thresholds satisfy
`Lambda_(m,k-1)>=189` and the raw/smoothed subtraction condition
`Lambda_(m,k)>=8H(yT_m)_0` (or 10 at m=0). The exact finite-m central
coefficients are reconstructed by the symmetric Laurent recurrence.
These checks validate all input hypotheses throughout each infinite
k tail, not only the numerical gates.

The only remaining prefixes with k>=3 are therefore

`m=0,k=3..20`; `m=1,k=3..10`; `m=2,k=3..5`;
`m=3,k=3..4`; `m=4,k=3`; `m=5,k=3..4`.

There are exactly 34. Each receives a continuum mixed-kernel certificate
and a finite-ray certificate proving every final left length, as
recorded in the respective result JSONs.

## The analytic m>=70 tail

Set c0=1/400000000, sigma=59/100 and

\[
E_m=\frac{c_0^2\sigma^{2m+1}}{16(m+3)},\quad
r_m=\frac{c_0\sigma^m}{4(m+3)},\qquad
e_j=E_mr_m^{j-1}/(4j).
\]

The old single-only perturbation gate is already valid at m=70:

\[
\frac{c_0^2\sigma^{2m+1}}{4(m+3)}
\ge12\frac{2m+5}{9\,6^m}.
\]

Its consecutive ratio is
`6 sigma² (m+3)/(m+4) (2m+5)/(2m+7)>1` and is increasing. Together
with the inherited normalized product and trace lemmas this supplies
the old normalized bounds for every m>=70.

For the new scalar gates use the conservative mass M=27·6^m and

\[
s=\frac9{32}\frac{M^k}{b},\quad
c=\frac9{512}\frac{M^{2k}}{b^2},\quad
\beta=\frac{M^2}{4(2d+1)^2}.
\]

The beta bound also uses `M>=4d-2`, which follows immediately at m=0
and then from the displayed exponential bound; this makes the
mass-average central estimate sufficient after subtracting one.

All eight gates exceed one at (m,k)=(70,3), as verified exactly. At
k=3, their consecutive ratios in m are positive constants times
products of increasing fractions `(Am+B)/(A(m+1)+B)`. The constants
coming from their exponentials are positive fixed powers of 6 and
sigma. Each ratio exceeds one at 70, proving the k=3 gates for every
m>=70.

For unbounded k, the exact calculation also establishes

\[
r_m^2M\ge16\quad(m\ge70).
\]

Its consecutive m ratio is `6 sigma² ((m+3)/(m+4))²>1`, increasing.
The following elementary fractions hold for every d>=2,k>=3:

\[
\frac{k}{k+1}\ge\frac34,\quad
\frac{k-1}{k}\ge\frac23,\quad
\frac{dk+2}{d(k+1)+2},\frac{dk+3}{d(k+1)+3}\ge\frac34,
\quad\frac{2dk-3}{2d(k+1)-3}\ge\frac23.
\]

They give consecutive-k lower bounds, respectively for G_1,...,G_7,

\[
\frac{r_m^2M}{4},\quad
\frac{r_m^3M^2}{12},\quad
\frac{r_m^3M^2}{12},\quad
\frac{r_m^2M^2}{6},\quad
\frac{r_mM}{3},\quad
\frac49M^2,\quad\frac23M.
\]

All exceed one because r_m<=1, M>=27 and r_m²M>=16. Thus the gates
hold for every m>=70,k>=3. The eighth gate beta is independent of k.
The strength input at j=2 grows by a factor 8 in m; at j=3 its ratio
to the sufficient coarse subtraction requirement `4*7^(m+1)`
grows exactly by 16/7. Their m=70 corner checks therefore cover the
same full region.

Together the analytic tail, the 70 fixed-m tails, and the 34 finite
prefixes cover every m>=0,k>=3. k<=2 and final length zero come from
the explicitly pinned previous theorems.
