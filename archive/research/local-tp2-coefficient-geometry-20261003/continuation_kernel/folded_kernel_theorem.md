# Folded convolution: exact criterion, closure, and an autocorrelation obstruction

This note contains genuine general proofs and exact finite calculations. It does not prove canonical Local TP2.

## 1. Definitions

Let h=(h_0,...,h_m) have h_n>0 for 0<=n<=m. Extend it symmetrically by h_{-n}=h_n and by zero for |n|>m. It represents the symmetric Laurent polynomial P(q)=h_0+sum_{n>=1}h_n(q^n+q^{-n}).

The folded convolution matrix K_h acts on half-rows by right multiplication. Its entries are

- K_h(0,j)=h_j;
- K_h(i,0)=2h_i for i>=1;
- K_h(i,j)=h_{|i-j|}+h_{i+j} for i,j>=1.

Thus H(QP)=H(Q) K_h whenever Q is also a polynomial in x=q+q^{-1}.

Define Delta_n=h_n^2-h_{n-1}h_{n+1} for n>=0, with h_{-1}=h_1. In particular Delta_0=h_0^2-h_1^2. Extend Delta by zero beyond m.

## 2. Exact criterion

**Theorem.** K_h is TP2 if and only if

Delta_0 >= Delta_1 >= ... >= Delta_m >= 0.

**Necessity.** The adjacent minor using rows 0,1 and columns n,n+1 is exactly Delta_n-Delta_{n+1}, including n=0.

**Sufficiency.** It suffices to verify adjacent minors and then use the interval support of each row (|i-j|<=m) to obtain monotonic row ratios and all minors.

For adjacent rows and columns wholly in the interior, set a=|j-i|, b=i+j. Because the interior block is symmetric, take j>=i without loss of generality. The minor is

M=(h_a+h_b)(h_a+h_{b+2})-(h_{a-1}+h_{b+1})(h_{a+1}+h_{b+1}).

When a,b+1 are within positive support, define t_n=(h_{n-1}+h_{n+1})/h_n. Direct expansion yields

M=Delta_a-Delta_{b+1}+h_a h_{b+1}(t_{b+1}-t_a).

Also

t_{n+1}-t_n=(Delta_n-Delta_{n+1})/(h_n h_{n+1}) >= 0.

Since a<=b+1, both terms in the expression for M are nonnegative. If b+1 is outside support, then h_{b+1}=h_{b+2}=0 and the original expression is Delta_a+h_a h_b>=0. If a is also outside support the minor is zero.

Adjacent minors involving the first row are Delta_n-Delta_{n+1}. Those involving the first column, except the already counted top-left minor, are twice this quantity. They are nonnegative.

Finally, for each adjacent row pair, the ratios are nondecreasing along the overlap of their positive interval supports. The lower row's support is shifted weakly right, so the leading/trailing zeros have the correct order. Hence all minors for adjacent rows and arbitrary column pairs are nonnegative. Transitivity of likelihood-ratio order then handles arbitrary row pairs. QED.

This proves the criterion directly; no claim of literature novelty is made.

## 3. Consequences

### Common-factor preservation

If K_h is TP2 and H(A)<=_lr H(B), then H(AP)<=_lr H(BP). This is Cauchy–Binet applied to the two-row coefficient matrix multiplied by K_h.

### Multiplicative closure

If K_{H(P)} and K_{H(Q)} are TP2, then so is K_{H(PQ)}, because

K_{H(PQ)}=K_{H(P)} K_{H(Q)}.

The folded-TP2 class is therefore closed under multiplication.

### Broadening under every nonnegative symmetric multiplier

If K_h is TP2 and Q has nonnegative Laurent coefficients, then

H(P)<=_lr H(PQ).

Indeed each row i of K_h is likelihood-ratio above row 0, and H(PQ) is a nonnegative combination of those rows. The conclusion follows by linearity of the pair determinants.

Conversely, requiring this broadening property for every such Q implies it already for Q=x, whose adjacent determinants are Delta_n-Delta_{n+1}. Thus the universal broadening property is equivalent to folded TP2.

### The class is not preserved by multiplication by x+1

Take H(P)=[3,2,1], i.e. P=(x+1)^2. Its defects are [5,1,1,0], so P is in the class. But (x+1)P=(x+1)^3 has H=[7,6,3,1] and defects [13,15,3,1,0], which fail the condition. Thus y=x+1 cannot be treated as an innocuous multiplier in a canonical induction.

## 4. Exact counterexample to a tempting autocorrelation theorem

It is false that the autocorrelation of every positive log-concave coefficient row has a TP2 folded convolution kernel.

Take

a=[6,12,24,34,45,52,60].

Its interior log-concavity defects a_i^2-a_{i-1}a_{i+1} are

[0,168,76,257,4],

so it is log-concave. It is positive, increasing, and every adjacent coefficient ratio is at most 2. Set h_n=sum_k a_k a_{k+n}; then

h=[10241,8166,6100,4032,2334,1032,360].

Its defects are

Delta=[38194525,4213456,4284688,2019624,1286532,224784,129600,0].

The folded minor using rows 0,1 and columns 1,2 is

Delta_1-Delta_2=-71232<0.

If strict rather than weak log-concavity is desired, a=[21,41,79,112,151,174,200] also gives a counterexample; its interior LC defects are [22,1649,615,3313,76] and the corresponding folded minor is -9189654.

Thus a mirror representation P(q)=m(q)m(q^{-1}) plus ordinary log-concavity of m is insufficient to establish folded TP2. A stronger, genuinely canonical property of m would be needed.

## 5. Canonical finite evidence and a possible sandwich

With the canonical Markov recurrence, let X,Y be the two endpoint polynomials sorted by degree, E=Y-X, and M=3(x+1)C+1-x. Then D=EM exactly, and

S=XM-[X+Y+(x+1)C].

Exact enumeration through depth 5 found both inequalities

H((x+2)X)<=_lr H(E),
H(S)<=_lr H((x+2)XM).

If these two inequalities and folded TP2 of M can be proved canonically, common-factor preservation gives the chain

H(S)<=_lr H((x+2)XM)<=_lr H(EM)=H(D).

This is currently only a reduction supported by finite evidence. Replacing x+2 by x+1 fails the first inequality at the first left child, so that apparently minor change is invalid.

Exact enumeration through depth 5 also found E, M, and (x+1)E in the folded-TP2 class at every node except E=x+1 at the root. Root E is a genuine exception, not a numerical issue. Other agents have broader finite checks; none should be conflated with an induction proof.

## 6. Strict multiplicative closure

Suppose both factors P,Q have strictly positive supported half-rows and strictly positive delta_n=Delta_n-Delta_{n+1} for every n from 0 through their respective degrees p,q. Then the product also has strictly positive delta_n for every 0<=n<=p+q.

For the product minor using rows 0,1 and columns n,n+1, expand Cauchy–Binet for K_P K_Q and select intermediate indices k,k+1, where k=min(n,p). The first factor is delta_k(P)>0. For the second factor:

- if k=0, it is delta_n(Q)>0;
- otherwise set a=n-k<=q and b=n+k. The interior-minor formula in Section 2 gives a quantity at least Delta_a(Q)-Delta_{b+1}(Q)>=delta_a(Q)>0, with the same conclusion from the support-boundary formula if b+1 is beyond degree q.

All other Cauchy–Binet terms are nonnegative. Therefore the selected strictly positive term proves strictness of the product minor. QED.

## 7. Exact reduction of the proposed t_X+a invariant

Put t_X=3(x+1)X-x and v=H((x+1)X). For g=H(t_X+a), a in [-2,2], one has

g_0=3v_0+a, g_1=3v_1-1, g_n=3v_n for n>=2.

Write delta_n(v)=Delta_n(v)-Delta_{n+1}(v). Direct expansion gives

- delta_0(g)=9delta_0(v)+a(6v_0+3v_2)+a^2+12v_1-2;
- delta_1(g)=9delta_1(v)-6v_1-3v_3-3a v_2+1;
- delta_2(g)=9delta_2(v)+3v_3;
- delta_n(g)=9delta_n(v) for n>=3.

For nonzero nonnegative integer X, v_0>=1, so delta_0(g) is increasing throughout a in [-2,2], while delta_1(g) is decreasing. Consequently the complete interval condition is equivalent to the two endpoint inequalities

9delta_0(v)-12v_0-6v_2+12v_1+2 >= 0,
9delta_1(v)-6v_1-6v_2-3v_3+1 >= 0,

plus 9delta_2(v)+3v_3>=0 and delta_n(v)>=0 for n>=3. These are exact conditions, not an established canonical invariant.

## 8. Precise limit of a positive two-state transfer

A homogeneous fixed-boundary recurrence R_{k+1}=t R_k-R_{k-1}, with d_k=R_k-R_{k-1}, has the positive-coordinate form

(R_{k+1},d_{k+1})^T = [[t-1,1],[t-2,1]] (R_k,d_k)^T,

and the scalar matrix factors as [[1,1],[0,1]][[1,0],[t-2,1]]. For canonical nonconstant X, t=t_X has t-2 coefficientwise nonnegative.

However, replacing scalar entries by folded convolution matrices does NOT give a TP2 block matrix in either natural state-first or coefficient-interleaved order. Already for X=x+2, H(t_X)=[12,8,3], the block matrix [[K_t-I,I],[K_t-2I,I]] has the minor with rows (state0,n0),(state0,n1) and columns (state0,n0),(state1,n0) equal to -16. Therefore this coordinate change cannot be used as a direct ordinary-TP2 proof.

## 9. Upper band of the proposed second sandwich

Let P=XM and B=X+Y+(x+1)C, so S=P-B. Since deg B=deg C+1, for every n>=deg C+2,

W_n(S,(x+2)P)=W_n(P,(x+2)P)=delta_n(H(P)).

Thus if X and M are in the folded-TP2 class, the second sandwich is automatically valid throughout this upper band, by product closure. In particular n=deg S-1 is included whenever deg X>=2. This still does not prove the target at that index without the first sandwich and the appropriate multiplier-preservation premise.
