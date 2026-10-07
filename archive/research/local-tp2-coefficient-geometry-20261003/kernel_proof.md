# Independent kernel attack on Local TP2

All coefficient lists are in increasing powers of x. Exploratory calculations used exact Python integer arithmetic. The deliverable's independent `verify.py` rechecks the explicit counterexamples. No finite search is claimed as an infinite proof.

## 1. A general positive-kernel lemma

Set K_a(k,n)=[q^n](q+q^{-1}+a)^k, for k,n >= 0.

**Lemma.** K_a is TP2 in (k,n) for every real a >= sqrt(2). This bound is necessary for TP2 of the whole array.

**Proof.** For a symmetric Laurent polynomial with nonnegative coefficient half-row h=(h_0,h_1,...), multiplying by x+a, where x=q+q^{-1}, is right multiplication by the tridiagonal matrix

- T[0,0]=a and T[0,1]=1;
- T[1,0]=2, T[1,1]=a, T[1,2]=1;
- for i>=2, T[i,i-1]=1, T[i,i]=a, T[i,i+1]=1.

Every potentially negative 2-by-2 minor of T is an adjacent principal minor. The first is a^2-2 and the others are a^2-1. All other minors are nonnegative. Thus T is TP2 when a>=sqrt(2). The rows h^(0)=(1,0,...) and h^(1)=(a,1,0,...) are likelihood-ratio ordered. Cauchy–Binet shows this ordering is preserved by multiplying both rows by T, proving h^(k)<=_lr h^(k+1) inductively. Transitivity gives all pairs of times. Necessity follows from the minor with times k=1,2 and spatial indices n=0,1, which is a^2-2. QED.

Consequently, nonnegative coefficient rows s,d in the basis (x+a)^k whose coefficient matrix is TP2 imply H(S),H(D) are TP2, for a>=sqrt(2). This is a modest extension of the known a=2 binomial kernel.

It does not immediately apply to the canonical root: S=4(x+1)^2(x+2). In the shifted basis y=x+a, its y^2 coefficient is 16-12a<0 for every a>=sqrt(2). Thus every shift covered by the lemma fails coefficient positivity at the root.

## 2. Exact identity for multiplication by x+a

Let h_n=H(P)[n], extend h_{-1}=h_1 by symmetry, and extend h_n=0 beyond the degree. Define the log-concavity defects

Delta_n = h_n^2 - h_{n-1} h_{n+1}, n>=0.

If Q=(x+a)P, then for every n>=0,

H(Q)[n+1] H(P)[n] - H(Q)[n] H(P)[n+1]
= Delta_n - Delta_{n+1}.

The expression is independent of a. The n=0 formula is h_0^2+h_0 h_2-2h_1^2, so the fold at zero is incorporated exactly.

Thus decreasing nonnegative defects are a sufficient and necessary condition for the pair (P,(x+a)P) to be TP2. This is stronger than ordinary log-concavity.

Exact enumeration through depth 6 (127 canonical nodes) found decreasing defects for each C, S, and D separately. This is only finite evidence. More importantly, Section 4 proves that this individual property cannot by itself bridge ordinary coefficient MLR to Laurent-coefficient MLR.

## 3. Real-rootedness and ultra-log-concavity do not suffice

Take S=(x+1)^3 and D=(x+1)^4. Then:

- S,D have dense positive coefficients, are divisible by x+1, are real-negative-rooted, and their coefficient rows are ultra-log-concave.
- Their ordinary coefficient ratios D_i/S_i are 1,4/3,2,4,+infinity, strictly increasing.
- H(S)=[7,6,3,1], H(D)=[19,16,10,4,1]. Both symmetric Laurent rows are log-concave.
- The n=0 target determinant equals 7*16-6*19=-2.

This obstruction has exactly the canonical root degrees 3 and 4. It rules out using raw coefficient MLR, real-rootedness, ULC, and individual H-log-concavity together without an additional quantitative condition.

## 4. Even decreasing log-concavity defects do not suffice

A stronger exact counterexample is

S=10(x+1)(x+2)^2,
D=S+x(x+1)(x+2)^2+2x^3(x+1).

Coefficient rows:

S=[40,80,50,10], D=[40,84,58,17,3].

These are dense and positive, divisible by x+1, of increasing degrees 3 and 4. Ordinary coefficient ratios are

1, 21/20, 29/25, 17/10, +infinity,

strictly increasing. Laurent half-rows and their symmetric log-concavity defects are

H(S)=[140,110,50,10],
Delta(S)=[7500,5100,1400,100,0];
H(D)=[174,135,70,17,3],
Delta(D)=[12051,6045,2605,79,9,0].

Both defect sequences are strictly decreasing to zero. Nevertheless the target determinants are

[-240,950,150,30].

Therefore ordinary coefficient MLR plus positive dense coefficients, x+1 divisibility, increasing degree, symmetric H-log-concavity, and decreasing LC defects of both individual rows still does not imply Local TP2. An argument must use a genuine relation between the canonical S and D, or a stronger pairwise invariant.

## 5. Other exact checks and excluded routes

Raw ordinary-coefficient MLR held at every canonical node tested through depth 5. This is an unproved candidate invariant, not a proof of Local TP2.

Shift x+1 cannot provide a universal positive coefficient basis: at the first left child,

S_L(y-1)=-y+2y^2+12y^3+8y^4.

The common factor (x+1)^2 is not universal. At the root,

S=4(x+1)^2(x+2),
D=2(x+1)(x+2)(3(x+1)^2+1).

D has only a simple x+1 factor. At the left child, S_L also has only a simple x+1 factor, with derivative S_L'(-1)=-1.

No infinite proof or counterexample to the canonical Local TP2 conjecture was obtained. The reusable result is the exact sqrt(2)-shift kernel lemma, plus the two explicit obstructions showing what a successful pairwise invariant must go beyond.

## 6. Strongest combined obstruction (recommended reference)

The following example simultaneously meets every individual shape condition above, including real-rootedness with all roots at most -1:

S=(x+1)^2(4x+5)=[5,14,13,4],
D=(x+1)^2(2x+3)(4x+9)=[27,84,95,46,8].

Both are dense positive, real-negative-rooted, PF-infinity and ultra-log-concave. Both are divisible by (x+1)^2. Their degrees are 3 and 4. Their raw coefficient ratios

27/5 < 6 < 95/13 < 23/2 < +infinity

are strictly increasing. Their Laurent rows are

H(S)=[31,26,13,4],
H(D)=[265,222,127,46,8].

Their symmetric log-concavity defects are

Delta(S)=[285,273,65,16,0],
Delta(D)=[20941,15629,5917,1100,64,0].

Both defect rows strictly decrease to zero. However, the target determinants are

[-8,416,90,32].

In particular 31*222-26*265=-8. Therefore even the combination of all of these shape hypotheses does not make the H transform MLR preserving. The key missing information must genuinely couple the canonical pair S,D more tightly than ordinary coefficient MLR.
