# Universal positivity of canonical first differences

**Theorem status: proved for the entire canonical tree, with no depth bound.** This establishes first-difference support and coefficientwise gap dominance. It does not establish the remaining likelihood-ratio comparisons or J-kernel membership.

## 1. Positive character basis

Write x=q+q^(-1), y=x+1, and

B_j(q)=sum_(i=-j)^j q^i, j>=0.

For any polynomial P(x), its unique expansion P=sum alpha_P(j) B_j satisfies

alpha_P(j)=H(P)[j]-H(P)[j+1].

The basis has the exact product rule

B_i B_j=sum_(k=|i-j|)^(i+j) B_k.

Thus coefficientwise nonnegativity in this basis is preserved by addition and multiplication. Write P>=_B Q for coefficientwise comparison in this basis. Also B_0=1 and B_1=y, and

y B_0=B_1,
y B_j=B_(j-1)+B_j+B_(j+1) for j>=1.

Consequently, if C=sum c_j B_j, then the coefficients of yC are c_1 at index0 and c_(n-1)+c_n+c_(n+1) at index n>=1, with zero extension.

## 2. Induction invariant

For every canonical triple (A,C,B), the following hold:

1. A,B,C have positive integer B-coefficients at every index within their respective degrees. Their constant B-coefficients a_0,b_0 are at least1.
2. C-A and C-B have strictly positive B-coefficients at every index from0 through deg C. In particular C>=_B A,B.
3. c_0>=3 and c_1>=c_0.
4. deg C>max(deg A,deg B).

At the canonical root,

A=1: alpha_A=[1],
B=x+2: alpha_B=[1,1],
C=2x^2+6x+5: alpha_C=[3,4,2].

The two gap rows are [2,4,2] and [2,3,2], so every invariant holds.

## 3. One mutation preserves the invariant

Consider the child

U=3yAC-x(A+C)-B,

which is the new center in the triple (A,U,C). Define

R=3AC-A-C.

Since x=y-1,

U=yR+A+C-B.

Because A>=_B1 and C>=_B1,

R=(2C-1)+(A-1)(3C-1)>=_B2C-1>=_B0.

The child-center gap S_U=U-C has the exact decomposition

S_U=[2yC-C-y+1]
    +y(A-1)(3C-1)+(A-1)+(C-B).

Every term after the bracket is B-nonnegative. The bracket has B-coefficients

- index0: 2c_1-c_0+1;
- index1: 2c_0+c_1+2c_2-1;
- index n>=2: 2c_(n-1)+c_n+2c_(n+1).

By the invariant these are strictly positive from index0 through deg C+1. Thus S_U is strictly positive throughout that initial interval.

### Strictness in the new upper support

Put a=deg A and c=deg C. If a=0, then deg U=c+1, already covered above.

If a>=1, A-1 has a positive coefficient at B_a, and 3C-1 has positive coefficients at every B_j for0<=j<=c. Since c>a, their product has a positive coefficient at every B_n for0<=n<=a+c: for n>=a choose j=n-a, so B_a B_j contains B_n; for n<a choose j=a-n, so B_a B_j again contains B_n. These chosen j all belong to [0,c]. Multiplication by y then has positive coefficients throughout0..a+c+1, because the product has positive coefficients at every index and degree at least1.

Hence S_U has strictly positive coefficients throughout0..deg U, where deg U=a+c+1. The degree assertion follows from the positive leading term of yR; all other terms have degree at most c. In the case a=0, the leading coefficient of R is (3a_0-1)c_c>0, so the same degree formula applies.

Therefore U-C is dense and strictly positive, U is dense and strictly positive, and

U-A=(U-C)+(C-A)

is dense and strictly positive throughout0..deg U. This proves the required gap dominance and support for the child triple. In particular the new constant coefficient is at least c_0>=3.

### Preservation of the central low-coefficient inequality

Write u_j, r_j for the B-coefficients of U,R. The multiplication rule gives

u_1-u_0
=r_0+r_2+(a_1-a_0)+(c_1-c_0)-(b_1-b_0).

Since r_2>=0, a_1>=0, c_1>=b_1, b_0>=1, and

r_0=3(AC)_0-a_0-c_0>=3a_0c_0-a_0-c_0,

we obtain

u_1-u_0>=3a_0c_0-2a_0-2c_0+b_0
          =(a_0-1)(3c_0-2)+c_0-2+b_0
          >=c_0-1>=2.

Thus u_1>=u_0. Its constant coefficient remains at least3, and deg U>deg C>deg A. The entire invariant is preserved.

The other mutation has the identical proof after exchanging A and B. Therefore induction proves the invariant for every canonical node. QED.

## 4. Consequences for S,E,M,D

Let X,Y denote the two endpoints sorted by degree, let U,V denote the children sorted by degree, and set

S=U-C,
E=Y-X,
M=3yC+1-x=y(3C-1)+2,
D=V-U=EM.

The last equality is the direct difference of the two canonical mutation formulas.

### S

Both child-center gaps have strictly positive B-coefficients throughout their full support by Section3. In particular

alpha_S(n)>0 for every0<=n<=deg S.

### Endpoint gap E

At the root, E=(x+2)-1=B_1, with first-difference row [0,1], so it is nonnegative.

At every nonroot node, one endpoint is the previous center and the other is a retained endpoint from the previous triple. The previous center has larger degree, and the proved central-gap invariant shows that their difference is dense and strictly B-positive. Therefore alpha_E is strictly positive throughout its support at every nonroot node.

### Multiplier M

Its B-coefficients are

m_0=3c_1+2,
m_1=3(c_0+c_1+c_2)-1,
m_n=3(c_(n-1)+c_n+c_(n+1)) for n>=2.

They are strictly positive throughout0..deg C+1.

### D

The positive product rule proves alpha_D>=0. At a nonroot node, both E and M have dense positive coefficient rows; their product has a positive coefficient at every index through deg E+deg M (choose positive terms B_i B_j with i+j=n).

At the root E=B_1=y. Since M has dense positive support of degree at least1, the displayed multiplication rule for y shows yM also has dense positive support. Thus, at every canonical node,

alpha_D(n)>0 for every0<=n<=deg D.

The endpoint degrees are distinct: this is true at the root and thereafter because the new endpoint is the previous center, whose degree exceeds the retained endpoint's degree. Hence deg D>deg S, as also follows directly from the positive leading degrees in the two child formulas.

## 5. What this discharges and what remains

This proves globally:

- all canonical G have strictly decreasing positive Laurent half-rows;
- every central-endpoint gap and every child-center gap has strictly decreasing positive Laurent half-rows;
- E has nonnegative first differences, dense and strictly positive except for its root constant coefficient;
- M,S,D have positive first differences throughout their full supports;
- the positivity/support hypothesis needed for the strict tail-sum implication in resumed_kernel_first_difference.md is completely established.

It does not prove first-difference MLR between S and D. It also does not prove J_C TP2, the two low-coefficient multiplier inequalities, or either first-difference sandwich comparison. Those remain the global interior closure obligations.
