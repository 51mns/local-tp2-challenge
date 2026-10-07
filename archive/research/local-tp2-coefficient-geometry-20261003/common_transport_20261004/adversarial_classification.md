# Positive-ray Fricke rigidity: a self-contained descent adaptation

This note is a proof and audit of a structural classification, **not a
proof of full-tree Local TP2**. The root lane proposed the degree descent;
the adversarial lane independently checked its boundary cases and
removed an unnecessary integrality hypothesis using the value at x=0.

Prior work: Bittmann et al., *A Mirror deformation of Markov Numbers*,
arXiv:2602.14802v1 (2026-02-16), Proposition 2.3, already classifies the
positive symmetric integer Laurent solutions into the mutation tree.
Its degree-descent argument is the relevant precedent. The integer
consequence here is a reproof/adaptation, not a claimed new result.
The real positive-ray formulation below is an explicit adaptation with
a complete proof; no claim of literature priority is made.
Source: https://arxiv.org/html/2602.14802v1#S2.SS1

## Theorem and exact hypotheses

Let A,B,C belong to R[x]. Assume each is strictly positive for **every**
real x>=0, and

    I(A,B,C)=A²+B²+C²+x(AB+AC+BC)-3(x+1)ABC=0.

Then, up to permutation, the triple is obtained from (1,1,1) by finitely
many polynomial mutations

    C -> C*=3(x+1)AB-x(A+B)-C.

In particular all its coefficients are integers: this is a conclusion,
not an input hypothesis. The theorem permits negative ordinary
coefficients in an intermediate descent polynomial. It does not require
or infer positivity of those coefficients before completing the descent.

The strict positive-ray hypothesis is retained at every mutation in the
proof. Merely nonzero polynomials, or arbitrary real solutions, are not
the claimed class.

## Step 1: constants in a positive-ray solution exceed 2/3

If one coordinate is a constant a>0, evaluate the Fricke equation at
x=0, writing b=B(0)>0 and c=C(0)>0. It gives

    (3a-2)bc=a²+(b-c)²>0.

Thus a>2/3. This excludes the exceptional cancellation a=1/3 without
integrality. It remains valid after any mutation because the positive-ray
property will be preserved. There is no assertion here that every
constant value of a nonconstant polynomial exceeds 2/3.

Every polynomial strictly positive on an unbounded right ray has a
positive leading coefficient and is nonzero. Its ordinary degree is a
nonnegative integer. Write the sorted degrees p<=q<=r, with leading
coefficients u,v,w>0.

## Step 2: a nonconstant solution has a unique maximum degree

Suppose q=r>0. If p>0, the cubic term has degree p+2q+1, strictly above
all other terms. Its leading coefficient -3uvw is nonzero, impossible.
This includes the case p=q=r>0.

If p=0, the first coordinate is a constant a>2/3. At degree 2q+1 the
only surviving leading combination is

    xBC-3(x+1)aBC,

whose coefficient is (1-3a)vw<0. All remaining terms have degree at most
2q. This is again impossible. Therefore r>q whenever the triple is not
entirely constant.

## Step 3: the maximum has degree p+q+1

There are three cases, including both constant endpoints explicitly.

1. If p>0, the only candidates for the highest degree are C², of degree
   2r, and the cubic, of degree p+q+r+1. The xBC and xAC terms have
   strictly lower degree than the cubic; A² and B² have degree below 2r.
   Consequently the two highest degrees must agree, giving r=p+q+1.
2. If p=0<q, the cubic combines with xBC at degree q+r+1, with nonzero
   coefficient (1-3a)vw. The xAC term has lower degree. Again C² must
   balance it, so r=q+1=p+q+1.
3. If p=q=0, write the positive constants as a,b. Step 1 gives a,b>2/3,
   hence

       a+b-3ab=ab(1/a+1/b-3)<0.

   The coefficient multiplying xC is therefore nonzero. The only
   possible highest degrees are 2r from C² and r+1 from xC. They must
   agree, so r=1=p+q+1. This case cannot be justified by retaining only
   (1-3a)bc, since xAC has the same degree as xBC.

## Step 4: mutation preserves positivity and strictly lowers the degree sum

Regard I as a monic quadratic in C. The displayed C* is its other root,
so it is a polynomial in R[x], satisfies I(A,B,C*)=0, and obeys

    CC*=A²+B²+xAB.

For x>=0 the right side is strictly positive; C(x)>0. Therefore
C*(x)>0 on the entire same ray. This is the reason inverse ordinary
coefficient positivity is unnecessary: pointwise positivity is enough
for the next descent step.

There is no leading cancellation in A²+B²+xAB because all relevant
leading coefficients are positive. Its degree is max(2q,p+q+1). Since
r=p+q+1,

    deg C* = q-p-1  if q>=p+1;
    deg C* = 0      if p=q>0;
    deg C* = 0      if p=q=0,r=1.

In each case deg C*<r. Thus replacing the unique maximum strictly
decreases the **sum of the three ordinary degrees**, a nonnegative
integer. This formulation includes the final degree-one seed step.
After finitely many mutations the triple is entirely constant.

## Step 5: the positive constant triple is (1,1,1)

For positive constants a,b,c, the constant and x coefficients of I=0
give respectively

    a²+b²+c²=3abc,
    ab+ac+bc=3abc.

Subtracting yields

    (a-b)²+(a-c)²+(b-c)²=0.

Thus a=b=c=d>0, and 3d²=3d³ gives d=1. Reversing the finite mutation
sequence proves the theorem. Every reverse mutation starts at integer
polynomials and has integer coefficients, proving the stated automatic
integrality.

## Corollaries for this campaign

1. Every ordinary-nonnegative, nonzero polynomial triple on Fricke is
   in this class if all three constant coefficients are positive. In
   particular this holds for the campaign's normalized ordinary bounds.
   Therefore a Fricke state satisfying these hypotheses is **actual
   mutation-orbit**, not an unrelated abstract state. Searching for an
   off-canonical Fricke counterexample in this class is searching an
   empty difference of classes.
2. The normalized definitions give X(-1)=Y(-1)=C(-1)=1 over R[x]. This
   condition is preserved by mutation, since at x=-1 the new value is
   A(-1)+B(-1)-C(-1)=1. It separately forces every degree-zero endpoint
   in a descent to be 1, also ruling out 1/3. This is a useful alternative
   check, though Step 1 already proves the stronger positive-ray result.
3. The two seed triples before the canonical binary tree are (1,1,1)
   and (1,1,x+2). Mutating a 1 in the latter gives
   (1,x+2,2x²+6x+5). Thus the canonical root used here is precisely the
   next unordered level of the same mutation orbit. The finite reverse
   descent has a unique maximum parent; once the canonical root is
   reached, the two increasing mutations are the degree-short and
   degree-long children. The two equal seed endpoints give only a single
   unordered increasing child.
4. If deg a<deg e and r<=a+e ordinarily, the normalized leading Fricke
   balance forces deg r=deg e and lc(r)=lc(e). Hence the inverse endpoint
   T=1+y(a+e-r) has degree below deg Y. This leading cancellation alone
   is not a proof that a divided normalized inverse remainder has
   nonnegative ordinary coefficients; the positive-ray descent avoids
   needing such an implication.

## Independent eta=0 and low-degree checks

Let eta=e-r. On Fricke, eta=0 forces the normalized root under a>=0 and
e>=1 ordinarily. Indeed F=0 becomes

    e²-ke-3aX²=0, X=1+ya, k=X(3X-2).

Over R[x], gcd(a,X)=1 and gcd(X,3X-2)=1. For any irreducible factor of X,
if its valuation in e were smaller than its valuation in X, e² would be
the unique lowest-valuation term in the displayed equation. Thus X|e.
Writing e=Xw gives w²-(3ya+1)w-3a=0, hence

    (2w-(3ya+1))²-(3ya+1)²=12a.

If a is nonzero of degree m, the squared comparison forces the first
factor's square root to have degree m+1 and leading coefficient equal
up to sign to that of 3ya+1. Of the factors B-(3ya+1), B+(3ya+1), one
has degree m+1 and neither is zero, so their product cannot have degree
m. Contradiction. Thus a=0; w²-w=0 and e>=1 give e=r=1.

There is also a small-degree elimination independent of this descent.
If a=A>0 is constant and e=Bx+C,r=Dx+E with B,D>0, the highest
coefficient forces D=B. Put u=E-C, so r=e+u. Then

    F=e²+(ut-k)e+u(k+u)-3aX².

The cubic coefficient gives u=A. The remaining identity is

    e²-[(2x+1)A+1]e-(2x+1)A²-2A=0.

Its x²,x,constant coefficients give B=2A,C=2A+1,A(A-1)=0.
Consequently only (a,e,r)=(1,2x+3,2x+4) occurs: the first long child.
If a=0 and e,r are genuinely linear, the same equations give
D=B,u=-B/2,C=1-3u,u(u+1)=0; hence only
(0,2x+4,2x+3), the first short child. The constant a=0,e,r case gives
the root (0,1,1). These are rigidity statements, not path-family TP2
results.

## What remains open

The classification does not establish K_G, K_M, or strict child proxy
preservation. Adding Fricke and ordinary positivity to a proposed generic
closure theorem identifies its states with the canonical orbit; it does
not prove any of those analytic inequalities. A root/both-children/target
common predicate is still required. Off-Fricke counterexamples, if found,
would address a broader generic implication and must be labelled as such.
