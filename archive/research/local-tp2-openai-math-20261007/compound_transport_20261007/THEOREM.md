# Finite-channel compound transport and mixed-mass bounds

Primary status: **PROOF_CANDIDATE**. This package gives general quantitative
lemmas and an alternative ray certificate. It does **not** prove arbitrary
four-run or full-tree Local TP2. The two applications below are already covered
by earlier results: no expansion of the proved canonical path set is claimed.
No literature novelty, external independent review, or Lean verification is claimed.

Baseline: private `51mns/AIMath`, commit
`53a780fcc4847e18d8e509df83706c42519f34e6`.

## 1. Mathematical dependencies and the actual change

For a symmetric finite Laurent polynomial P(q), let h_P(n)=[q^n]P(q),
reflect h at zero, and zero-extend outside its degree. All polynomials below
are evaluated at x=q+q^-1. The folded multiplication kernel is

    K_P(0,j)=h_P(j),
    K_P(i,0)=2h_P(i)                         (i>0),
    K_P(i,j)=h_P(|i-j|)+h_P(i+j)             (i,j>0).

Write mass(P)=P(2) and

    delta_n(P)=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2).

The pinned `continuation_kernel/folded_kernel_theorem.md` proves that positive
interval support and delta_n>=0 are equivalent to TP2 of this infinite kernel.
It also proves K_(PQ)=K_PK_Q, common-factor likelihood-ratio preservation, and
strict product closure. Its proof is elementary: the first-row adjacent minor
is delta_n; interior adjacent minors are sums of nonnegative defect differences;
banded support allows adjacent cross-ratios to telescope. We retain the true
infinite kernel. A finite submatrix below is a **lower-bound device**, never
an exact finite-dimensional replacement for that kernel.

The other inherited ingredient is the signed-seed ray identity and positive
Jacobi-resolvent expansion in `signed_seed_20261007/THEOREM.md`, sections 2–5.
The changes here are:

1. retain several intermediate adjacent pairs in Cauchy–Binet, rather than
   a single diagonal pair;
2. obtain quantitative bounds on mixed determinants rather than discard them;
3. carry the resulting geometric rate to a finite starting length, instead
   of requiring the correction budgets at the first length.

Item 3 alone could also be used in the previous criterion when its scalar
rate exceeds one. The distinct improvements are items 1 and 2. All claims
below are sufficient conditions, not claimed necessary conditions.

## 2. Finite-channel transport lemma

For any matrix K with nonnegative ordered two-by-two minors, write

    C2(K)[I,J]=det K[I,J]

for its second compound, where I,J are increasing pairs of indices. Let
S={I_0,...,I_e} be a finite set of such pairs and

    M_K=C2(K)[S,S].

Let w be a strictly positive row vector indexed by S. Suppose each permitted
factor K has a positive scale m(K) and satisfies

    w M_K >= gamma(K) m(K) w,              gamma(K)>0.             (2.1)

Let A be a two-row matrix all of whose ordered minors are nonnegative.
Suppose its restricted minor row satisfies

    det A[:,I_j] >= c w_j                  for all j, c>=0.        (2.2)

Then, for **any finite number, order and choice** of permitted factors,

    det (A K_1 ... K_N)[:,I_j]
      >= c product_s(gamma(K_s)m(K_s)) w_j.                       (2.3)

All products are assumed entrywise well-defined; finite-band kernels and
finite-support starting rows suffice.

### Proof

The two-by-two Cauchy–Binet formula is

    det (A K)[:,J] = sum_I det A[:,I] det K[I,J].

It follows either by expanding the four scalar products and pairing ordered
indices, or from the usual finite Cauchy–Binet identity. Here each coefficient
sum is finite. Dropping pairs outside S drops nonnegative terms, hence the
restricted minor row after multiplication is at least its previous restricted
row times M_K. Equations (2.1)–(2.2) now give one step of (2.3); induction proves
it for every N. The same argument also shows

    C2(K_1 ... K_N)[S,S] >= M_(K_1)...M_(K_N).

There is generally strict inequality. No assertion that S is closed under
the exact infinite dynamics is required. QED.

The row w is a common certificate for the entire permitted factor family.
In the applications, S consists of (j,j+1), j=0,...,e, and w_j=1. Condition
(2.1) is then a lower bound for **column sums** of M_K, not row sums.

## 3. Retaining mixed terms eliminates the mixture-size loss

For a fixed output pair J define the polarized determinant

    B_J(U,V)=det(U+V)[:,J]-det U[:,J]-det V[:,J]

for two-row matrices U,V. Suppose U_1,...,U_M have positive scales a_i and
nonnegative weights lambda_i with sum_i lambda_i=1. If

    det U_i[:,J] >= c a_i,
    B_J(U_i,U_j) >= c(a_i+a_j)                         (i<j),      (3.1)

then

    det(sum_i lambda_i U_i)[:,J] >= c sum_i lambda_i a_i.          (3.2)

### Proof

Expand the quadratic determinant exactly. The right-side lower bound is

    c [ sum_i lambda_i^2 a_i
         +sum_(i<j) lambda_i lambda_j(a_i+a_j) ]
    =c sum_i a_i lambda_i [lambda_i+sum_(j!=i)lambda_j]
    =c sum_i lambda_i a_i.

This proves (3.2), independently of M. The diagonal-only estimate would
retain sum lambda_i^2 and could lose a factor 1/M. It is not legitimate to
remove that loss without the additional mixed inequalities in (3.1).
The proof also covers zero weights and repeated matrices. QED.

Both lemmas combine because Cauchy–Binet is linear in the polarized
coefficient as well. When all polarized minors are nonnegative, their
restricted vector can be transported by the same finite-channel matrix.

## 4. Application to signed canonical rays

Use y=x+1, p=x+2 and the original canonical mutation

    C_next=3yXC-x(X+C)-Y.

At a fixed prefix, label the endpoint retained by the next direction X,
the other endpoint Y, and the center C_0. Define

    t=3yX-x,       T=tY-xX-C_0,
    A=(C_0-Y)/y,  B=(T-Y)/y,      Q=|B|,
    P=pX,         J=y(t-2),       V=3y^2P,
    M_0=3yY-x+1,  K=P M_0,
    q_0=yA,       q_1=y(tA+B),    beta=y(A+B), E_1=C_0-X.

As in the pinned signed criterion, assume exact polynomial division, the
canonical degree relations (a=deg X>=1,b=deg Y), positive interval support
of the displayed positive quantities, sign-uniform B, Q>=0 and Q<=A.
The applications check these conditions explicitly. The inherited global
signed-seed lemma explains their canonical origin but does not imply the
additional Fourier inequalities below.

Let f_r=t-r and L_r=A(t-r)+B, r in [-2,2]. Assume A,yA,f_r,L_r,yL_r are
strict folded-cone polynomials. For r,s in [-2,2], set

    E_(r,s)=L_r f_s,   G_(r,s)=L_s f_r,
    H_(r,s)=(E_(r,s)+G_(r,s))/2
           =A(t-r)(t-s)+B(t-(r+s)/2).

Assume all ordered mixed minors of K_E,K_G are nonnegative, raw and after
multiplication by y. Our certificates use the sufficient finite conditions,
for (F,R)=(H,Q) and (yH,yQ),

    F>=R,       delta_n(F)>=8 max_j h_R(j) h_F(n),                (4.1)

with strict cone F (also when R=0). The pinned quantitative all-minor lemma
then gives det K_F>=4 det K_R on every ordered pair, even if R is not cone.
This proves mixed nonnegativity through the identity

    Mix(K_E,K_G)=2det K_H-((r-s)^2/2)det K_B >=0.                  (4.2)

For signed B, det K_B=det K_Q. If the reference minor is negative, (4.2)
is already nonnegative; otherwise use |r-s|<=4 and the factor-four bound.
Common cone multiplication preserves mixed nonnegativity by Cauchy–Binet.

Retain the four initial likelihood-ratio comparisons

    q_0<=lr q_1, beta<=lr q_1, P<=lr E_1, P<=lr q_1,

and W_j(J,V)>0 for j=0,...,deg J. These are exactly the initial comparisons
in the previous signed criterion, not replaced by computational guesswork.

### New finite quantitative conditions

Put e=deg K=a+b+2. Use S={(j,j+1):0<=j<=e} and w=(1,...,1). Choose a rational
gamma>1 and certify on the whole interval

    w C2(K_(f_r))[S,S] >= gamma mass(f_r) w.                      (4.3)

For the proxy two-row functional define

    D_j(F)=W_j(JF,VF),
    B_j(F,G)=W_j(JF,VG)+W_j(JG,VF).

For the multiplier define

    d_j(F)=delta_j(y^2F),
    b_j(F,G)=delta_j(y^2(F+G))-delta_j(y^2F)-delta_j(y^2G).

Find positive rational constants c_P,c_M such that, for every j=0,...,e,

    D_j(L_r)>=c_P mass(L_r),
    B_j(E_(r,s),G_(r,s))>=c_P gamma [mass(E_(r,s))+mass(G_(r,s))],  (4.4)

and the same inequalities with (D,B,c_P) replaced by (d,b,c_M).             (4.5)

These involve only fixed-degree polynomials on one interval or a square.
There are no unbounded ray lengths in (4.1), (4.3)–(4.5).

### The all-length mass bounds

Let u_-1=0,u_0=1,u_1(z)=z,u_(n+1)=zu_n-u_(n-1), R_N=sum_(i=0)^N u_i.
The exact ray representation is

    Z_N=A R_N(t)+B R_(N-1)(t),
    q_N=y[A u_N(t)+B u_(N-1)(t)], C_N=Y+yZ_N.

The inherited Jacobi-resolvent formula writes, for N>=1,

    Z_N=sum_i lambda_i Z_i,
    Z_i=L_(r_i) product_(j!=i) f_(r_j),
    lambda_i>0, sum_i lambda_i=1, 1<=number of active weights<=N.  (4.6)

There are N spectral factors in total, including canceled outside factors;
there are exactly N-1 propagators in each Z_i. Inactive roots are not given
spurious residues. For N=1 there is one active root -1 and Z_1=L_-1.
The supporting identities are R_2h=u_h(u_h+u_(h-1)) and
R_(2h+1)=u_h(u_(h+1)+u_h). The endpoint resolvent of the path Jacobi matrix
has positive residues of total mass one and eigenvalues in [-2,2].
No sign of B is required in (4.6); positivity is a property of L_r.

Apply the finite-channel lemma to an individual summand, using (4.4).
It gives

    D_j(Z_i)>=c_P gamma^(N-1) mass(Z_i).

For a pair i<j, remove the N-2 common propagators. Its remaining templates
are E_(r_i,r_j),G_(r_i,r_j). Equation (4.4), followed by the same finite-channel
transport of the **mixed** vector, gives

    B_j(Z_i,Z_j)>=c_P gamma^(N-1)[mass(Z_i)+mass(Z_j)].

All omitted ordered minors are nonnegative: for the proxy this follows by
applying the nonnegative minors of the row pair (H(J),H(V)) to the kernel
mixed minors; for the multiplier use the weak-cone kernel K_(y^2).
Thus dropping channels was legitimate for both diagonals and mixed terms.

The identity in section 3 now yields the exact uniform bounds

    W_j(JZ_N,VZ_N)>=c_P gamma^(N-1) mass(Z_N),
    delta_j(y^2Z_N)>=c_M gamma^(N-1) mass(Z_N)                     (4.7)

for every N>=1 and j=0,...,e. There is no 1/N or summand-mass-ratio loss.

## 5. Absorbing corrections and reaching original Local TP2

Write m=deg M_0=b+1, h_j=h_(M_0)(j) and nu_n=h_(n-1)+3h_(n+1).
Let z_1=mass(Z_1)>0 and define finite thresholds

    B_P=mass(J) max_n h_K(n),
    B_M=max_(0<=n<=m+1) [27nu_n+max(-delta_n(M_0),0)/z_1].

Choose an integer N_0>=1 satisfying

    c_P gamma^(N_0-1)>B_P,
    9c_M gamma^(N_0-1)>B_M.                                      (5.1)

Such an integer exists since gamma>1. It is found with rational arithmetic.
For N>=N_0, equation (4.7) absorbs the negative proxy term because

    W_n(JZ_N,K)>=-mass(J)mass(Z_N)h_K(n).

It also makes the actual multiplier M_N=M_0+3y^2Z_N strict cone: expanding
its defect and bounding only adverse cross terms gives

    delta_n(M_N)>=[9c_M gamma^(N-1)-27nu_n]mass(Z_N)+delta_n(M_0).

Here every coefficient of y^2Z_N is at most 9mass(Z_N), and positivity of
the increments q_N gives mass(Z_N)>=z_1. Above n=m+1 the fixed correction
vanishes identically. Strictness there follows from strict cone Z_N and
multiplication by the weak-cone y^2 (its half-row is (3,2,1), with defects
(4,0,1); the positive terminal minors follow by Cauchy–Binet).

The same spectral compatibility proves all q_N are strict cone. The gap
recurrence q_(N+1)=tq_N-q_(N-1) and the four initial orders therefore give

    P<=lr E_N,          S_N<=lr JZ_N,
    E_N=C_(N-1)-X,      S_N=q_(N+1).

The proxy bound is strict for n<=e. For n>e, K has no coefficient, and the
fixed pair (deg J,deg J+1) in Cauchy–Binet supplies strictness through the
support of JZ_N. Finally the original child difference is D_N=E_NM_N, and

    S_N<=lr JZ_N <lr PM_N <=lr E_NM_N=D_N.

The terminal degree difference is

    deg D_N-deg S_N=b+1+(N-1)(a+1)>0.

Thus the strict last supported minor is the product of two positive entries.
This proves original strict Local TP2 for **all N>=N_0**. Directly checking
the finitely many original targets N=0,...,N_0-1 completes the ray. No finite
sample is extrapolated: the infinite tail follows from (2.3), (3.2), and
(5.1). The ray criterion still does not establish preservation under a turn.

## 6. Concrete removal of a failed scalar mass condition

At the canonical root, choose right continuation, so X=p=x+2 and Y=1.
The exact quantities are

    A=2p, B=0, t=3x^2+8x+6, J=3x^3+11x^2+12x+4,
    P=p^2, V=3y^2p^2, M_0=2p, K=2p^3.

At r=2 the half-row of f_r is (10,8,3). The old single-pair rate is

    delta_0(f_2)/mass(f_2)=2/32=1/16.

Consequently a criterion demanding delta_0(f_r)>=2mass(f_r) cannot hold.
This is a failure of that sufficient condition, not of Local TP2.

For r in [-2,2], write a=12-r in [10,14]. The second-compound block on the
four adjacent pairs (0,1),(1,2),(2,3),(3,4) is exactly

    [a^2+3a-128, 55-3a,          9,             0]
    [110-6a,     a^2+3a-64,     64-3a,         9]
    [18,         64-3a,         a^2-64,       64-3a]
    [0,           9,            64-3a,        a^2-64].

For w=(1,1,1,1), the four components of wM-2mass(f_r)w are

    a^2-5a-44,  a^2-5a+20,  a^2-8a+29,  a^2-5a-35.

Each increases on [10,14], and their values at a=10 are (6,70,49,15), all
positive. Hence the finite-channel rate is gamma=2 uniformly on the full
interval, despite the failed scalar rate. This is not a speedup claim or
an improvement of the true underlying determinant: it is a stronger bound.

The full new certificates give

    c_P=67497/32, c_M=657/32, B_P=3840, B_M=216.

N_0=2 suffices, with final margins 6057/16 and 2457/16. The two finite
original-target rows are

    N=0: (272,352,160,24),
    N=1: (3034320,5889604,4023508,1407664,254928,21528,648).

Thus this generic method proves the entire root right ray, which was already
proved previously by other methods. It demonstrates removal of a real
applicability restriction, not a new canonical family.

A second, signed-B example uses prefix LRL and right continuation. It has
12 channels, gamma=2 and N_0=1. Both implementations give

    c_P=126905240098017960185102228628/134474726441,
    c_M=1078509499320574704/134474726441.

This re-proves the already-recorded LRL R^N family. The exact certificate
contains all support, cone, midpoint, initial-order, channel and correction
conditions; the two methods agree on all 2,430 entries for this example and
716 for the root, 3,146 in total.

## 7. Audit, research value and unresolved obligation

`author.py` uses ordinary x polynomials, a binomial coefficient transform and
exact degree-two interpolation. `verifier.py` independently reconstructs
full Laurent polynomials and expands r=4u-2,s=4v-2 symbolically. It imports
neither the author implementation nor expected certificate data. A separate
replay step compares every array and rejects any discrepancy. Both are
written by the same model; this is not an external independent review.

All parameter expressions have degree at most two in each variable. Their
full tensor Bernstein coefficients certify the entire compact interval or
square. Testing three numerical values alone would not suffice.

The useful new mechanism is a finite common left witness for the compound
kernel and a mixed-mass estimate. It could reduce repeated quantitative
certification. It does **not** show that every new canonical trace and every
new signed seed satisfy these conditions. In particular the unproved step
remains preservation, under arbitrary turns, of the qualitative cones,
mixed compatibility and initial likelihood-ratio orders, together with a
common quantitative witness or another suitable bound.

The finite-channel lemma itself permits arbitrary sequences of already
admissible kernels. That statement must not be confused with arbitrary
canonical mutation: a mutation also changes the seeds, trace and correction
polynomials. That identification/preservation obligation has not been solved.
