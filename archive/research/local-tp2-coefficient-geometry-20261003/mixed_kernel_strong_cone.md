# Quantitative folded-convolution cone and a multiplier reduction

**Status:** general infinite lemmas proved below. The proposed cone is not proved invariant under canonical mutation. No full-tree kernel or Local TP2 conclusion is claimed from these lemmas alone.

Use the folded kernel K_h and defects

Delta_n=h_n^2-h_(n-1)h_(n+1),
delta_n=Delta_n-Delta_(n+1),

with symmetric extension h_(-1)=h_1 and zero extension after the finite positive support. All statements below assume the positive interval support needed by the established folded-kernel theorem.

## 1. Quantitative adjacent-minor lemma

Call h **lambda-strong** if delta_n>=lambda h_n for every supported n, where lambda>0.

Then every adjacent minor of K_h satisfies

minor K_h[rows i,i+1; columns j,j+1] >= lambda K_h(i,j).

For an interior minor, symmetry permits j>=i>=1. Set a=j-i,b=i+j. The established formula is

M=Delta_a-Delta_(b+1)+h_a h_(b+1)(t_(b+1)-t_a),

t_n=(h_(n-1)+h_(n+1))/h_n.

Both terms are nonnegative. Therefore, within support,

M>=sum_(k=a)^b delta_k
 >=lambda sum_(k=a)^b h_k
 >=lambda(h_a+h_b)=lambda K_h(i,j),

where b>=a+2. At the support boundary the direct expression is Delta_a+h_a h_b, yielding the same bound; outside the band both sides are zero. For row0 the minor is delta_j and K_h(0,j)=h_j. For column0 and i>=1 the minor is2delta_i and K_h(i,0)=2h_i. This proves all cases.

## 2. Multiplicative strength

If P is lambda-strong and Q is mu-strong, then PQ is lambda*mu-strong.

Proof: K_(PQ)=K_P K_Q. In Cauchy–Binet for its minor with rows0,1 and columns n,n+1, retain only the nonnegative terms with intermediate pair k,k+1. The first minor is delta_k(P)>=lambda h_P(k). The second is at least mu K_Q(k,n) by Section1. Thus

delta_n(PQ)>=lambda*mu sum_k h_P(k)K_Q(k,n)
             =lambda*mu H(PQ)[n].

All other Cauchy–Binet terms are nonnegative. QED.

This is genuine product closure with a quantitative margin; it is not closure under arbitrary sums or subtractions.

## 3. Multiplication by y has a controlled tail

Suppose h=H(P) is an integer 1-strong row of degree m>=2. Let v=H(yP), y=x+1. Then

delta_n(v)>=v_n for every n>=1.

Only the central index n=0 can fail.

Let W(i,j) be the minor of the first two rows of K_P at columns i,j. Cauchy–Binet with K_y gives, for n>=1,

delta_n(v)=W(n-1,n)+W(n-1,n+1)+W(n-1,n+2)
            +W(n,n+2)+W(n+1,n+2).

All five terms are nonnegative; the missing pair n,n+1 has zero minor in K_y. For1<=n<=m-1, the identities

W(i,k)=(h_k/h_j)W(i,j)+(h_i/h_j)W(j,k), i<j<k,

with a positive intermediate h_j, and W(j,j+1)=delta_j>=h_j, give

W(n-1,n)>=h_(n-1),
W(n-1,n+1)>=h_(n-1),
W(n-1,n+2)>=h_(n-1),
W(n,n+2)>=h_n,
W(n+1,n+2)>=h_(n+1).

These bounds remain valid when n=m-1 and the final column is m+1: then W(i,m+1)=h_i h_m>=h_i by integrality. Hence

delta_n(v)>=3h_(n-1)+h_n+h_(n+1)>=v_n.

At n=m the exact formula is

delta_m(v)=delta_(m-1)(h)+h_(m-1)h_m
            >=h_(m-1)+h_m=v_m,

because h_(m-1)>=1. At n=m+1, delta_(m+1)(v)=h_m^2>=h_m=v_(m+1). This completes the proof.

For later use, the n=1 estimate is stronger:

delta_1(v)>=3h_0+h_1+h_2=v_1+2h_0>=(5/3)v_1,

because h is decreasing and v_1=h_0+h_1+h_2<=3h_0.

## 4. Exact useful consequence for t_P=3yP-x

Suppose P is integer 1-strong, has degree at least2, and

delta_0(H(yP))>=0.

Then t_P=3yP-x is 2-strong.

To prove this, put v=H(yP) and g=H(t_P). Then g_0=3v_0, g_1=3v_1-1, and g_n=3v_n for n>=2. Direct expansion gives

delta_0(g)=9delta_0(v)+12v_1-2,
delta_1(g)=9delta_1(v)-6v_1-3v_3+1,
delta_2(g)=9delta_2(v)+3v_3,
delta_n(g)=9delta_n(v), n>=3.

At n=0, 2v_1-v_0=h_0+2h_2>=1, so

delta_0(g)-2g_0>=12v_1-2-6v_0>=4.

At n=1, Section3 and v_3<=v_1 give

delta_1(g)>=15v_1-6v_1-3v_3+1>=6v_1+1>2g_1.

At every n>=2, Section3 gives delta_n(g)>=9v_n>=2g_n. Its positive interval support is immediate from the integer positive first differences of v. QED.

## 5. A single product-closed sufficient bundle for the center hypotheses

Define the proposed center cone F by

- C has a positive integer Laurent half-row of degree at least2;
- delta_n(H(C))>=2H(C)[n] at every supported n;
- delta_0(H(yC))>=0.

Then F is product-closed. Indeed, Section2 makes a product of two such C at least4-strong, hence2-strong. Section3 and the central condition show that yC has a folded-TP2 kernel. Thus y(CD)=(yC)D has a folded-TP2 kernel by ordinary product closure, proving the required central condition for CD.

For every C in F, Section4 proves K_(t_C) TP2 (in fact t_C is2-strong), while K_C is TP2 by definition. Also

delta_0(H(C))>=2h_0>=h_0+h_1.

Therefore F supplies exactly the three center assumptions used in the conditional general first-sandwich induction:

K_C TP2,
K_(3yC-x) TP2,
delta_0(H(C))>=h_0+h_1.

The root center is in F: H(Croot)=[9,6,2], delta=[27,14,4]>=2[9,6,2], and H(yCroot)=[21,17,8,2] has central defect31.

**The remaining obligation is canonical mutation preservation of F.** The preceding product lemmas do not prove it, because the mutation includes subtraction. This manuscript does not assert that arbitrary triples satisfying the already proved support/dominance invariant preserve F, nor that all canonical centers lie in F.

## 6. Useful weak saturation observation

The weak class of P for which both K_P and K_(yP) are TP2 is product-closed and stable under multiplication by y. The latter follows because y^2 itself lies in the folded cone: its half-row is[3,2,1] and its defect differences are[4,0,1]. Thus K_(y^2P)=K_(y^2)K_P is TP2.

This observation avoids imposing infinitely many separate conditions K_(y^jP): the cases j=0,1 imply all integer j>=0. It does not restore closure under sums or canonical subtraction.
