# A first-difference convolution cone: exact TP2 criterion

**Later update:** `resumed_extension_kernel_support.md`, independently audited in
`resumed_extension_support_audit.md`, proves positive integer first differences
and all required support statements for the entire canonical tree. Thus hypothesis
(4) of the conditional reduction below, and its nonnegative-row prerequisites,
are now established. The remaining obligations are the kernel TP2 conditions,
the two multiplier inequalities, and the pairwise likelihood-ratio orders.
Statements below that described support as open record the earlier stage.

Status: the general kernel theorem below is proved. Membership of the full canonical Markov family in this stronger cone, and the required canonical pairwise order, are not proved here.

## Definitions

Let h_0>h_1>...>h_m>0, put h_n=0 for n>m, and extend h symmetrically to negative indices. Let

P(q)=h_0+sum_(n=1)^m h_n(q^n+q^(-n)).

Define

g_n=h_n-h_(n+1)>0,
Delta_n=h_n^2-h_(n-1)h_(n+1),
delta_n=Delta_n-Delta_(n+1),
r_n=delta_n/g_n,

for 0<=n<=m, with h_(-1)=h_1 and Delta_(m+1)=0. Then delta_m=h_m^2, so r_m=h_m>0.

Let

J_h(i,j)=h_(|i-j|)-h_(i+j+1), i,j>=0.

All entries in the band |i-j|<=m are positive, and all entries outside it are zero. In particular the first row of J_h is g.

## Theorem

J_h is TP2 if and only if r_0>=r_1>=...>=r_m.

### Necessity

The adjacent minor with rows 0,1 and columns n,n+1, for 0<=n<m, equals

[delta_n g_(n+1)-delta_(n+1)g_n]/h_(n+1).

This identity includes n=0 with the stated symmetric extension of h. Since its denominator and the g terms are positive, these minors give exactly r_n>=r_(n+1). The final adjacent minor n=m is h_m^2>0.

### Sufficiency: interior away from support boundary

By symmetry of J_h, consider adjacent rows i,i+1 and columns j,j+1 with j>=i. Put

a=j-i, b=i+j+1.

Thus b+1>=a+2. The minor is

M(a,b)=(h_a-h_b)(h_a-h_(b+2))
        -(h_(a-1)-h_(b+1))(h_(a+1)-h_(b+1)).

For a=0, h_(a-1)=h_1, as required by the absolute value in J_h.

Suppose b+1<=m. Define t_n=(h_(n-1)+h_(n+1))/h_n. Algebra gives

M(a,b)=Delta_a-Delta_(b+1)-h_a h_(b+1)(t_(b+1)-t_a).

The exact difference identity

t_(k+1)-t_k=delta_k/(h_k h_(k+1))

therefore gives

M(a,b)=sum_(k=a)^b delta_k f_k,
f_k=1-h_a h_(b+1)/(h_k h_(k+1)).

The sequence f_k is decreasing, because h is decreasing. The positive weights g_k have the telescoping identity

sum_(k=a)^b g_k f_k
=(h_a-h_(b+1))
 -h_a h_(b+1)(1/h_(b+1)-1/h_a)=0.

By hypothesis r_k=delta_k/g_k is decreasing. For completeness, the weighted rearrangement identity is

(sum g)(sum g r f)-(sum g r)(sum g f)
=sum_(a<=u<v<=b) g_u g_v (r_u-r_v)(f_u-f_v)>=0.

Because sum g f=0, this proves sum delta_k f_k>=0, hence M(a,b)>=0.

### Sufficiency: support boundary

If a>m, the entire minor vanishes. Assume a<=m.

If b=m, then h_(b+1)=h_(b+2)=0 and the displayed polynomial formula reduces to

M(a,m)=Delta_a-h_a h_m.

Since r_k>=r_m=h_m for all k<=m,

Delta_a=sum_(k=a)^m delta_k
         >=h_m sum_(k=a)^m g_k=h_m h_a,

so M(a,m)>=0.

If b>m, the formula reduces to M(a,b)=Delta_a, which is nonnegative because every delta_k=r_k g_k is positive (r_k>=r_m>0). Thus every adjacent minor is nonnegative.

### All minors

The support of each row is a positive interval [max(0,i-m),i+m]. Consider arbitrary rows i<k and columns j<l. If either off-diagonal entry J(i,l) or J(k,j) vanishes, the determinant is nonnegative. Otherwise |i-l|<=m and |k-j|<=m, so every entry throughout that row-column rectangle is positive. Multiplying adjacent log-supermodular inequalities throughout the rectangle yields J(i,j)J(k,l)>=J(i,l)J(k,j). Thus all minors are nonnegative. QED.

## Polynomial multiplication and the exact meaning of J_h

Define the basis

B_k(q)=sum_(i=-k)^k q^i.

Then P=sum_(k=0)^m g_k B_k. If Q is any symmetric Laurent polynomial, taking first differences of coefficients in B_k P gives

H(B_k P)[n]-H(B_k P)[n+1]
=h_(|n-k|)-h_(n+k+1)=J_h(k,n).

Thus if alpha_Q(n)=H(Q)[n]-H(Q)[n+1], then

alpha_(QP)=alpha_Q J_h.

Consequently J_(PQ)=J_P J_Q as an identity of multiplication operators in the B_k basis. The matrices have finite bandwidth, so all sums needed for a fixed entry or minor are finite.

It follows immediately that the class defined by the theorem is multiplicatively closed: J_P and J_Q are nonnegative TP2 matrices, so J_(PQ) is TP2 by Cauchy–Binet. The product has positive first differences at every supported index because its first-difference row is alpha_Q J_P; for each supported output index at least one positive in-band term exists.

Moreover a common factor from this class preserves likelihood-ratio order of first-difference rows.

## A sufficient pairwise invariant for original Local TP2

For every nonnegative first-difference row alpha_P,

H(P)[n]=sum_(k>=n) alpha_P(k).

The tail-sum matrix T(k,n)=1[n<=k] is TP2. Therefore

alpha_S<=_lr alpha_D  ==>  H(S)<=_lr H(D).

This is a valid sufficient condition, with no parity caveat. It does not establish the required first-difference order for the canonical S,D.

## What was checked and what was not proved

Exact finite checks found alpha_S<=_lr alpha_D through canonical depth6. Both proposed stronger sandwich inequalities in first differences held through depth4. At depth4, C,M_C,S,D and the nonroot endpoint gap E=Y-X satisfy the theorem's local ratio conditions. The root E=x+1 has g_0=0 and is outside the positive-support assumptions.

These computations are evidence only. There is no assertion here that the complete canonical family belongs to this cone or that the canonical pair order follows inductively.

The stronger cone is distinct from the earlier folded-convolution cone. For example H(t_(x+2)-2)=[10,8,3] has a folded-TP2 kernel, but its J kernel has top-left minor -5. Likewise H(t_(x+2)+2)=[14,8,3] has a J minor (rows0,1; columns1,2) equal to -2. Thus this new cone cannot simply be substituted into the earlier t_X±2 propagation plan.

## Degree-independent reduction for the multiplier t_X+a

Assume X has positive integer first differences and J_X is TP2. Put y=x+1 and t_X=3yX-x.

The matrix J_y is tridiagonal, with diagonal (0,1,1,...) and all super/subdiagonal entries equal to 1. Its only negative 2-by-2 minor is the principal minor with rows and columns (0,1), equal to -1. All other minors are nonnegative.

Consequently, Cauchy–Binet for J_(yX)=J_X J_y proves every minor whose output column pair is not (0,1) nonnegative. In particular, all adjacent minors of its first two rows at column indices n>=1 are nonnegative. This conclusion uses the positive factor J_X and the exact location of the single negative minor; it does not assert J_y itself is TP2.

Write v=H(yX), b_n=v_n-v_(n+1), c_n=v_n-v_(n+3), and let tau_n(v) be the top-two-row adjacent minor of J_v at columns n,n+1. For g=H(t_X+a), direct coefficient expansion gives

- tau_0(g)=(3b_0+a+1)(3c_0+a)-(3b_1-1)^2;
- tau_1(g)=(3b_1-1)(3c_1-1)-3b_2(3c_0+a);
- tau_2(g)=9tau_2(v)+3b_3;
- tau_n(g)=9tau_n(v) for n>=3.

Thus the already established nonnegativity of tau_n(v) for n>=1 guarantees every tau_n(g) with n>=2. The first-difference coefficients of g are

3b_0+a+1, 3b_1-1, 3b_2,3b_3,... .

For a in [-2,2] they are strictly positive when X is nonconstant with positive integer first differences. The new kernel criterion therefore proves the following exact conditional closure statement:

**For nonconstant X with positive integer first differences, J_X TP2, and a in [-2,2], J_(t_X+a) is TP2 if and only if the two displayed inequalities tau_0(g)>=0 and tau_1(g)>=0 hold.**

This is a degree-independent two-inequality reduction. The quantities needed are b_0,b_1,b_2,c_0,c_1, equivalently the first five first-difference coefficients of X:

b_0=alpha_X(1),
b_1=alpha_X(0)+alpha_X(1)+alpha_X(2),
b_2=alpha_X(1)+alpha_X(2)+alpha_X(3),
c_0=alpha_X(0)+3alpha_X(1)+2alpha_X(2)+alpha_X(3),
c_1=alpha_X(0)+2alpha_X(1)+3alpha_X(2)+2alpha_X(3)+alpha_X(4).

The two scalar inequalities remain to be established for the canonical X. They do not follow merely from J_X TP2, integer coefficients, and the central ratio bound h_0<=3h_1/2. Indeed h_X=[12,8,3] satisfies those hypotheses, but H(t_X)=[84,68,33,9] has first differences [16,35,24,9] and top-left J minor 16*(84-9)-35^2=-25.

For a ranging over an interval, tau_0(g) is increasing in a on [-2,2], whereas tau_1(g) is decreasing. Hence an entire interval can be checked by the lower endpoint for tau_0 and the upper endpoint for tau_1. The earlier explicit failures at a=±2 for X=x+2 show why that full interval is unsuitable for this stronger cone.

## Exact conditional reduction for the full canonical tree

At a canonical node, let X,Y be its two endpoints sorted by degree. Set

E=Y-X,
M=3(x+1)C+1-x=t_C+1,
A=(x+2)X.

The known algebraic identity is D=EM. Suppose the following hold at every canonical node:

1. C has positive integer first differences, and J_C is TP2.
2. The two scalar conditions below hold for the first five coefficients u_i=alpha_C(i), with missing coefficients interpreted as zero:

   U=3u_1+2,
   V=3(u_0+u_1+u_2)-1,
   W=3(u_0+3u_1+2u_2+u_3)+1,
   Z=3(u_0+2u_1+3u_2+2u_3+u_4)-1,
   B=3(u_1+u_2+u_3),

   U W >= V^2,
   V Z >= B W.

   By the proved degree-independent reduction, these conditions imply J_M is TP2.
3. The nonnegative first-difference rows satisfy the two pairwise comparisons

   alpha_A <=_lr alpha_E,
   alpha_S <=_lr alpha_(AM).

4. alpha_S(n)>0 for all 0<=n<=deg S, and alpha_D is nonnegative with alpha_D(deg D)>0. Canonically deg D>deg S.

Then common-factor preservation by J_M proves

alpha_S <=_lr alpha_(AM) <=_lr alpha_(EM)=alpha_D.

In this setting even weak first-difference order yields the original *strict* Local TP2 conclusion. Indeed direct tail summation gives the exact identity

F_n=H(D)[n+1]H(S)[n]-H(D)[n]H(S)[n+1]
   =sum_(j>n) [alpha_S(n)alpha_D(j)-alpha_D(n)alpha_S(j)].

Every summand is nonnegative by the pairwise order. The term j=deg D is strictly positive for every 0<=n<=deg S, because alpha_S(n)>0, alpha_D(deg D)>0, and alpha_S(deg D)=0. Thus F_n>0 on the entire required support.

**Missing global proof obligations are explicit:** no canonical induction has been proved for (1), for the two low-coefficient inequalities in (2), or for the two first-difference pair orders in (3). Positive first-difference support in (4) must also be established canonically rather than inferred from ordinary x-coefficient positivity. Finite checks in the preceding section do not settle any of these infinite statements.

The independently proved all-left Local TP2 theorem can serve as a genuine boundary condition for a future canonical induction. It does not establish the missing interior closure listed here. This note supplies a new exact convolution criterion and a conditional reduction, not a proof for the full canonical tree.
