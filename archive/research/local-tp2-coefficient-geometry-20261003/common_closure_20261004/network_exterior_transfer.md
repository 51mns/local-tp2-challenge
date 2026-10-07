# Exact selective exterior transfer and an active canonical obstruction

Status: the transfer and obstruction below are proved algebraically. They do not prove or disprove the row predicate or canonical Local TP2. The obstruction concerns a proposed sourcewise nonnegative exterior-square transport, and is active on the actual root right child.

## 1. A determinant-one selective transfer

Use the canonical matrices and conventions of `../fulltree_kernel_row_states.md`. For each matrix set

\[
G=Q_{11},\quad s=Q_{21},\quad r=G-s,\quad d=Q_{22},\quad
u=3yG-x-s,\quad v=3yG-x+r=u+G.
\]

The positive congruence is

\[
\widehat Q=\begin{pmatrix}r-s-x+d&s+x-d\\s-d&d\end{pmatrix}.
\]

For the actual Farey mediant \(C=A^{\mathsf T}TB^{\mathsf T}\), the selective row recurrence therefore reduces exactly to

\[
\boxed{\begin{pmatrix}r_C\\s_C\end{pmatrix}
=N_A\begin{pmatrix}u_B\\G_B\end{pmatrix},\qquad
N_A=\begin{pmatrix}r_A-x&s_A-d_A\\s_A+x&d_A\end{pmatrix}.}
\tag{1}
\]

This retains the boundary corrections \(-x,+x\), and replaces the correlated pair \((u_B,v_B)\) by \((u_B,G_B)\) using their exact difference. The canonical identity

\[
G_A d_A=s_A^2+xs_A+1
\]

implies

\[
\det N_A=(r_A-x)d_A-(s_A-d_A)(s_A+x)=1.
\tag{2}
\]

For the signed boundary \(A=Q_0\), one has \(r_A=y,s_A=-x,d_A=1\), so

\[
N_0=\begin{pmatrix}1&-y\\0&1\end{pmatrix},\qquad
s_C=G_B,\quad r_C=u_B-yG_B=2yG_B-x-s_B.
\tag{3}
\]

Thus the exceptional boundary cannot be silently put into the interior positive class. Both canonical child steps are covered by (1): the left child uses \((A,C)\), and the right child uses \((C,B)\).

## 2. Exact polarized exterior coefficients

Write \(N_A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), and let \(U=H(u_B)\), \(F=H(G_B)\). Denote the folded multiplication kernels of \(a,b,c,d\) by \(A,B,C,D\), respectively. Then

\[
H(r_C)_n=\sum_i\{U_iA(i,n)+F_iB(i,n)\},\qquad
H(s_C)_n=\sum_i\{U_iC(i,n)+F_iD(i,n)\}.
\]

For any \(n<m\), define

\[
\begin{aligned}
P^{UU}_{ij}(n,m)&=C(i,n)A(j,m)-C(i,m)A(j,n),\\
P^{FF}_{ij}(n,m)&=D(i,n)B(j,m)-D(i,m)B(j,n),\\
P^{UF}_{ij}(n,m)&=C(i,n)B(j,m)-C(i,m)B(j,n)\\
&\quad+D(j,n)A(i,m)-D(j,m)A(i,n).
\end{aligned}
\]

Let \(\widetilde P_{ii}=P_{ii}\) and \(\widetilde P_{ij}=P_{ij}+P_{ji}\) for \(i<j\) in the two unmixed families. Direct expansion gives the exact identity

\[
\boxed{\begin{aligned}
&H(s_C)_nH(r_C)_m-H(s_C)_mH(r_C)_n\\
&=\sum_{i\le j}U_iU_j\widetilde P^{UU}_{ij}(n,m)
+\sum_{i\le j}F_iF_j\widetilde P^{FF}_{ij}(n,m)
+\sum_{i,j}U_iF_jP^{UF}_{ij}(n,m).
\end{aligned}}
\tag{4}
\]

All sums are finite because the input rows have finite support. No truncation of the infinite folded kernels is assumed. Formula (4) includes central, interior, and terminal output indices, with the same kernel convention \(K_h(i,0)=2h_i\) for \(i>0\). It is a selective two-output exterior transport, rather than a claim that every scalar entry kernel is TP2.

The input is constrained: \(u_B=3yG_B-x-s_B\), and the determinant-one relation couples \(G_B,s_B,d_B\). These constraints have not been discarded in the example below. Treating every summand in (4) as nonnegative is nevertheless impossible.

## 3. Universal negative diagonal source coefficient

Every interior canonical matrix satisfies

\[
\deg G=\deg s+1\ge2,\qquad \operatorname{lc}(G)>0,\quad \operatorname{lc}(s)>0.
\tag{5}
\]

Here is an algebraic degree proof independent of a depth scan. For \(A=Q_0\), the original matrix multiplication gives

\[
G_C=(2x+3)G_B-(s_B+x),\qquad s_C=G_B,\qquad d_C=s_B.
\]

The endpoint \(Q_1\) has degrees \(1,0,0\) for \(G,s,d\); the initial center has degrees \(2,1,0\). For interior \(A\),

\[
\begin{aligned}
G_C&=(3yG_A+s_A)G_B-G_A(s_B+x),\\
s_C&=(3y(s_A+x)+d_A)G_B-(s_A+x)(s_B+x),\\
d_C&=(3y(s_A+x)+d_A)s_B-(s_A+x)d_B.
\end{aligned}
\]

The inductive degrees are \(\deg d=\deg G-2\) in the interior. The displayed first terms give degrees \(\deg G_A+\deg G_B+1\), one less, and two less, respectively; every subtractive term has strictly smaller degree. For the right endpoint \(Q_1\), \(\deg(s_B+x)=1\) and \(\deg d_B=0\), which still leaves these degrees strict. The leading coefficients are positive. This proves (5) under both canonical mutations.

For an interior \(A\), set \(m=\deg c=\deg(s_A+x)\). Then \(\deg a=\deg(r_A-x)=m+1\). Put \(i=m+1\). The central diagonal coefficient in (4) is

\[
\begin{aligned}
\widetilde P^{UU}_{ii}(0,1)
&=C(i,0)A(i,1)-C(i,1)A(i,0)\\
&=0-\operatorname{lc}(s_A+x)\,2\operatorname{lc}(G_A)\\
&=\boxed{-2\operatorname{lc}(s_A+x)\operatorname{lc}(G_A)<0.}
\end{aligned}
\tag{6}
\]

The identities used here are exactly \(C(i,0)=0\), \(C(i,1)=H(c)_m\), and \(A(i,0)=2H(a)_{m+1}\). The initial center has \(\deg s=1\), so the extra x in \(c=s+x\) must be retained; replacing its leading coefficient by \(\operatorname{lc}s\) would be wrong in that case.

Consequently, a predicate requiring every polarized source coefficient in (4) to be nonnegative fails for every interior canonical transfer matrix. Positive diagonal normalization of individual source coordinates cannot repair this sign. This is an obstruction to that transport strategy, not to the possibility that the canonical input correlations make the complete sum positive.

## 4. The negative source is active on the actual root right child

Take \(A=Q_{1/2}\), \(B=Q_1\). The transfer and inputs are

\[
N_A=\begin{pmatrix}2x^2+4x+3&x+1\\2x+2&1\end{pmatrix},\qquad
u_B=3x^2+8x+5,\quad G_B=x+2.
\]

All matrices are the actual canonical matrices, and \(\det A=\det B=\det C=\det N_A=1\), with skew difference x. Their half rows are

\[
H(u_B)=(11,8,3),\quad H(G_B)=(2,1),
\]

\[
H(s_C)=(56,45,22,6),\quad H(r_C)=(157,131,76,28,6).
\]

At \(i=2\), (6) is \(-8\), and its active diagonal contribution is \(-8\cdot3^2=-72\). There is also an active \(i=0\) diagonal contribution \(-6\cdot11^2=-726\). The complete central minor is nonetheless

\[
56\cdot131-45\cdot157=271.
\]

The three complete source categories in (4) give

\[
UU:180,\qquad FF:2,\qquad UF:89,\qquad 180+2+89=271.
\]

The other adjacent output minors are \((538,160,36)\), all positive. Therefore this example is not a Local TP2 counterexample, and not even a counterexample to \(s_C\le_{\rm lr}r_C\). It rigorously demonstrates cancellation between positive and negative exterior-source terms on a true canonical transition.

## 5. Candidate statuses and reproducibility

| Predicate | ROOT | LEFT closure | RIGHT closure | IMPLIES TARGET |
|---|---|---|---|---|
| Prow: folded TP2 of r,s and s<=lr r | proved at initial center | unproved; bounded pass | unproved; bounded pass | unproved |
| Pconnector: Prow plus folded TP2 of u,v and v<=lr u | proved at initial center | unproved; bounded pass | unproved; bounded pass | unproved |
| Pext: every polarized source coefficient in (4) is nonnegative for the actual transition | fails for the root right transition | no common closure possible; signed boundary separately | fails on actual root right transition | sourcewise sufficient only; false premise |

The first two predicates were frozen before the bounded probe in `network_candidates.md`. The exact root defects are

\[
\delta(s)=(2,1),\quad\delta(r)=(13,7,4),\quad
\delta(u)=(383,655,246,36),\quad\delta(v)=(670,859,310,36),
\]

and the supported adjacent root minors are \((3,2)\) for s<=lr r and \((75,46,12)\) for v<=lr u. The existing folded-defect criterion supplies root kernel membership. The root support is positive and interval; adjacent LR minors imply all ordered LR minors, including the terminal zero extension.

`network_probe.py` imports parent exact arithmetic and checks 127 centers through depth 6 (maximum G degree 54). It found no failures of Prow or Pconnector. This is bounded evidence, not either closure proof.

`network_exterior_reproducer.py` imports no parent arithmetic: it evaluates all matrices directly in sparse integer Laurent polynomials, reproduces (1),(2), the root cone/minor data, and every signed source term of the active root-right example. Its output is `network_exterior_results.json`.

```
python network_exterior_reproducer.py
python network_probe.py 6
```

Dependencies for the mathematical transfer are the already established canonical matrix recurrence, positive congruence, skew difference, determinant-one identity, and folded multiplication kernel. No arbitrary-positive mixture closure, raw-gap LGV positivity, numerical-to-infinite inference, or new external result is used.
