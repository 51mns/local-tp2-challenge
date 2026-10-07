# A complete candidate proof on every R²L^ell ray state

Status: **PROVED_INTERNAL for the displayed infinite family; shared-session independent audit PASS.** The independent review is `../hour_quantum/AUDIT_R2_RAY.md`, with a separately implemented reconstruction of all 993 parameter-certificate coefficients. This is a proof for a new infinite family, using finite exact continuous-parameter certificates and an unbounded spectral argument. The review is neither blind nor an external or formal proof verification. It does not prove arbitrary-tree Local TP2 and does not change the canonical claim status.

## 1. Statement and dependencies

For every integer ell>=0, consider the canonical Farey-tree state at path `R R L^ell`. Let U,V be its two child centers ordered by degree, C its center, S=U-C, D=V-U, and

\[
H(P)_n=[q^n]P(q+q^{-1}).
\]

The claimed conclusion is

\[
H(S)_nH(D)_{n+1}-H(S)_{n+1}H(D)_n>0
\quad(0\le n\le\deg S).
\]

The proof uses these already established general lemmas from the previous research directory `local-tp2-coefficient-geometry-20261003/`:

- `continuation_kernel/folded_kernel_theorem.md`: the exact folded-kernel criterion, all-minor TP2, multiplication/Cauchy–Binet closure and strict product closure.
- `mixed_kernel_all_minor_strength.md`: lambda-strength implies the quantitative all-minor bound and its factor-4 relative corollary.
- The elementary finite Jacobi resolvent and prefix factorizations stated in `general_one_turn_kernel_theorem.md` and `second_turn_20261004/proxy_mass_compare.md`. Their precise use is restated below.

No missing full-tree MP_0, proxy-preservation gate, arbitrary positive-sum closure, or future Local TP2 assertion is assumed.

For a symmetric half-row h, extend h_-j=h_j and h_j=0 above its support, and put

\[
\delta_j(h)=h_j^2-h_{j-1}h_{j+1}-h_{j+1}^2+h_jh_{j+2}.
\]

The folded multiplication kernel has entries

\[
K_h(0,j)=h_j,\quad K_h(i,0)=2h_i\ (i>0),\quad
K_h(i,j)=h_{|i-j|}+h_{i+j}\ (i,j>0).
\]

For positive interval rows, `delta_j>=0` at every supported j is exactly its TP2 criterion. Lambda-strength means `delta_j>=lambda h_j` throughout that support.

## 2. A positive origin after two R steps

Put y=x+1 and p=x+2. Starting from `(1,2x²+6x+5,p)`, perform the original R mutation twice. Write P=p, X for the first R center, C_0 for the second R center, and Z_old for the original root center. Then

\[
X=29+74x+74x^2+34x^3+6x^4,
\quad Z_{\rm old}=5+6x+2x^2.
\]

The positive normalized seeds and the new trace are

\[
\begin{aligned}
A&=(C_0-P)/y\\
 &=167+500x+620x^2+398x^3+132x^4+18x^5,\\
B&=(Z_{\rm old}-P)/y=3+2x,\\
\tau&=3yX-x=87+308x+444x^2+324x^3+120x^4+18x^5.
\end{aligned}
\]

Unlike the previously completed `L^m R L^ell` case, the additional turn here has a positive seed B because the replaced old center is already larger than P.

Define `C_-1=P`, `C_-2=Z_old`. The original mutation gives

\[
C_0=\tau P-Z_{\rm old}-xX,
\qquad C_{N+1}=\tau C_N-C_{N-1}-xX.
\]

For N>=0 these are exactly the centers at `R²L^N`. Let

\[
u_N=U_N(\tau/2),\quad u_{-1}=0,\quad
R_N=\sum_{j=0}^N u_j,\quad R_{-1}=0.
\]

Then the exact consecutive-gap and center formulas are

\[
q_N=C_N-C_{N-1}=y(Au_N+Bu_{N-1}),
\]
\[
Z_N=AR_N+BR_{N-1},\qquad C_N=P+yZ_N.
\tag{1}
\]

The initial previous gap is `C_-1-C_-2=-yB`; hence the plus sign in the formula is essential. Formula (1) follows from the homogeneous gap recurrence and its two initial values, and summing the gaps.

The degrees are

\[
\deg\tau=\deg A=5,\quad\deg B=1,
\quad\deg Z_N=5+5N,\quad\deg C_N=6+5N.
\]

For N>=1 the actual endpoints are X and C_(N-1). Their degrees are 4 and 1+5N, respectively. Thus X is the lower-degree endpoint. At these states

\[
S_N=q_{N+1},\quad E_N=C_{N-1}-X,
\quad M_N=3yC_N-x+1,\quad D_N=E_NM_N.
\tag{2}
\]

In particular

\[
\deg S_N=11+5N,\quad\deg D_N=8+10N>\deg S_N.
\]

N=0 has the opposite endpoint orientation; it is checked separately in Section 8.

## 3. Finite certificates for an entire spectral box

For independent r,s,c in [-2,2] define

\[
L_r=A(\tau-r)+B,
\]
\[
H_{r,s,c}=A(\tau-r)(\tau-s)+B(\tau-c).
\]

`verify_r2_ray.py` constructs the canonical root and both R mutations from scratch with integer polynomials. It builds each defect polynomial in the independent parameters, substitutes r=2-4u_0, s=2-4u_1, c=2-4u_2, and computes every tensor Bernstein coefficient on the unit cube. No saved results or old polynomial implementation are imported.

`r2_ray_certificates.json` contains all the arrays. The complete margins are:

| Polynomial | Required strength lambda | Degree in x | Minimum Bernstein coefficient of delta_j-lambda H_j over all j |
|---|---:|---:|---:|
| tau-r | 1 | 5 | 306 |
| L_r | 1 | 10 | 104652 |
| yL_r | 1 | 11 | 104652 |
| H_(r,s,c) | 24 | 15 | 33872256 |
| yH_(r,s,c) | 56 | 16 | 33685632 |

All coefficients are strictly positive. Each parameter degree is at most two in a defect, so the saved 3- or 27-entry arrays cover the **entire** interval/cube, including every supported output index.

All involved ordinary polynomial coefficients are positive throughout support for every parameter: tau has constant coefficient 87, so tau-r has positive constant coefficient at least 85, and A,B have positive dense ordinary support. The leading A terms dominate the lower-degree B terms without cancellation. The smoothing factor y is treated through its own L and H certificates.

The base rows A,yA,B,yB also have strict supported folded defects. In particular

\[
H(B)=(3,2),\quad H(yB)=(7,5,2).
\]

The references are decreasing and nonnegative. Moreover H_(r,s,c)>=B and yH_(r,s,c)>=yB coefficientwise, because tau-c has positive ordinary constant coefficient at least 85. Since 24=8H(B)_0 and 56=8H(yB)_0, the quantitative all-minor corollary yields

\[
\det K_H\ge4\det K_B,
\qquad \det K_{yH}\ge4\det K_{yB}
\tag{3}
\]

for **every** ordered pair of row and column indices of the infinite kernels.

### Consequence: actual gap and prefix kernels for all N

The monic U_N(t/2) is the characteristic polynomial of a path Jacobi matrix. Its previous/next ratio has positive resolvent weights summing to one at roots in [-2,2]. Therefore `Au_N+Bu_(N-1)` is a positive weighted sum of

\[
L_{r_i}\prod_{j\ne i}(\tau-r_j).
\]

For two spectral roots r,s, the remaining pair after removing common factors is

\[
F=A(\tau-r)(\tau-s)+B(\tau-s),\quad
G=A(\tau-r)(\tau-s)+B(\tau-r).
\]

Its midpoint is H_(r,s,(r+s)/2), and F-G=(r-s)B. At every ordered minor the polarized kernel determinant is exactly

\[
2\det K_H-\frac{(r-s)^2}{2}\det K_B\ge0.
\tag{4}
\]

When the reference minor is positive, this follows from (3) and (r-s)²<=16; when it is nonpositive, it follows from TP2 of K_H. The y version uses the separately certified yH,yB. Multiplication by the common shifted factors preserves the mixed-minor sign by Cauchy–Binet. Diagonal summands are strict cone products with the same degree and positive interval support. At least one positive weight therefore makes every supported output defect strictly positive.

For the prefixes, let V_j=U_j+U_(j-1). The exact factorizations are

\[
R_{2h}=U_hV_h,\qquad R_{2h+1}=U_hV_{h+1}.
\]

Hence R_(N-1)/R_N is respectively U_(h-1)/U_h or V_h/V_(h+1). Each is a Jacobi resolvent with nonnegative residues, whose active residues are positive and sum to one. All prefix roots are in [-2,2]. Restore the outside root factors: Z_N is a sum of the same form, with N-1 propagators in each active summand and at most N active weights. The preceding compatibility proof applies without change.

Thus every q_N, Z_N, yZ_N for N>=0 has a strict supported folded TP2 kernel. N=0 follows from the directly certified A,yA. This is an unbounded N theorem, not a finite path scan.

## 4. A low-index mass bound propagated without limiting N

The needed Cauchy–Binet selection is

\[
\delta_j(FG)\ge\delta_j(F)\delta_0(G)
\tag{5}
\]

for two folded-cone polynomials and a supported index j of F. To prove it, retain intermediate indices (j,j+1) in K_FK_G. The first minor is delta_j(F). The principal minor K_G[(j,j+1),(j,j+1)] is at least delta_0(G), including j=0. For j>=1 this is the folded adjacent-minor formula with displacement zero, using monotonicity of the Delta sequence; if a sum-index is outside support its boundary formula gives the same bound. Every other Cauchy–Binet term is nonnegative.

The exact one-parameter Bernstein mass certificates are

\[
\delta_0(\tau-r)>22(\tau(2)-r),
\]
\[
\delta_j(L_r)>40000L_r(2),\qquad j=0,1,2,3,
\tag{6}
\]

uniformly for r in [-2,2]. The first margin has complete Bernstein array

`(951,9527,18119)`.

The four L margins have arrays

- j=0: `(78391898628,82834341084,87282164356)`;
- j=1: `(3724877934480,3733712708456,3742556826944)`;
- j=2: `(3187127279500,3192143699108,3197165187260)`;
- j=3: `(553415845908,554183352380,554952106340)`.

Consider the active prefix resolvent summands Z_i. Their masses satisfy Z_i(2)>Z_N(2)/2. Indeed

\[
\frac{Z_i(2)}{R_N(\tau(2))}=A(2)+\frac{B(2)}{\tau(2)-r_i},
\]

and

\[
A(2)=9519,\quad B(2)=7,\quad\tau(2)=7567,
\quad B(2)<A(2)(\tau(2)-2).
\]

Thus every displayed ratio lies strictly between A(2) and 2A(2), as does its positive weighted average.

Applying (5)-(6) to each product gives, for j=0,1,2,3,

\[
\delta_j(Z_i)>40000\,22^{N-1} Z_i(2).
\]

The same all-minor compatibility used in (4) makes every off-diagonal contribution to delta_j(Z_N) nonnegative. For active weights lambda_i, there are at most N of them, so sum lambda_i²>=1/N. Consequently

\[
\delta_j(Z_N)>
\frac{40000\,22^{N-1}}{2N}Z_N(2).
\]

The quantity 22^(N-1)/N is at least one for every N>=1: its initial value is one and its next/previous ratio is 22N/(N+1)>=11. We obtain

\[
\boxed{\delta_j(Z_N)>20000Z_N(2)\quad
(j=0,1,2,3;\ N\ge1).}
\tag{7}
\]

This retains a finite set of low indices while treating arbitrarily large degree and outer run length.

## 5. The actual multiplier has a strict folded kernel

The exact decomposition is

\[
M_N=K_0+3y^2Z_N,\qquad K_0=3yP-x+1=7+8x+3x^2.
\]

Put Q=y²Z_N and h=H(Q). The row of y² is (3,2,1), with defects (4,0,1). Equation (5), or its retained principal minor directly, gives

\[
\delta_j(Q)\ge4\delta_j(Z_N)>80000 Z_N(2),
\quad j=0,1,2,3.
\tag{8}
\]

Q has strict supported defects everywhere. For n<=deg Z_N retain the intermediate pair (n,n+1), with a principal y² minor at least 4. At the two remaining indices retain (deg Z_N,deg Z_N+1); the y² minors are respectively Delta_1(y²)=1 and Delta_2(y²)=1. Here deg Z_N>=10, so their sum-index terms lie outside the y² support. All other terms are nonnegative.

Write Pol_j(h,K_0)=delta_j(h+H(K_0))-delta_j(h)-delta_j(H(K_0)). Since H(K_0)=(13,8,3), the four nonzero polarizations are exactly

\[
\begin{array}{ll}
 j=0:&29h_0-32h_1+13h_2,\\
 j=1:&-3h_0+16h_1-19h_2+8h_3,\\
 j=2:&6h_2-8h_3+3h_4,\\
 j=3:&-3h_4.
\end{array}
\]

Their total negative coefficient weights are 32,22,8,3. Every h_i<=Q(2)=9Z_N(2), and K_0 has defects (80,16,9). Therefore for 0<=j<=3,

\[
\begin{aligned}
\delta_j(M_N)
&=9\delta_j(Q)+3\operatorname{Pol}_j(h,K_0)+\delta_j(K_0)\\
&>(9\cdot4\cdot20000-3\cdot32\cdot9)Z_N(2)>0.
\end{aligned}
\]

For j>=4 the correction vanishes, so delta_j(M_N)=9delta_j(Q)>0 throughout support. This proves the actual multiplier assertion without assuming that addition preserves the folded cone.

## 6. Initial LR comparisons and their all-N transport

Let beta=y(A+B) and E_1=C_0-X. Four exact initial comparisons are certified:

\[
q_0\le_{\rm lr}q_1,\quad
\beta\le_{\rm lr}q_1,\quad
pX\le_{\rm lr}E_1,\quad E_1\le_{\rm lr}q_1.
\tag{9}
\]

Every supported adjacent minor is strictly positive in the saved certificate. These are finite base inequalities, not a sampled preservation hypothesis. The respective minimum minors are 12678336,12678336,108,12678336; complete arrays and both rows are saved.

The homogeneous recurrence gives

\[
W_n(q_N,q_{N+1})=W_n(q_N,\tau q_N)+W_n(q_{N-1},q_N).
\]

The first term is nonnegative by broadening through the now-proved kernel of q_N and the nonnegative Laurent row of tau. Starting from (9), this proves q_N<=lr q_(N+1) for every N>=0.

Also

\[
E_N=E_1+\sum_{j=1}^{N-1}q_j,
\]

so pX<=lr E_N follows from (9) and time order, by summing rows above the same fixed lower row.

Finally beta=(tau-2)P-xX and the original recurrence give

\[
S_N=JZ_N+q_N+\beta,\qquad J=y(\tau-2).
\]

Both q_N and beta lie below S_N=q_(N+1). Their sum also lies below that one fixed upper row; this use of linearity is valid even though cone addition in general is not. Hence

\[
W_n(S_N,JZ_N)=W_n(q_N+\beta,S_N)\ge0,
\quad S_N\le_{\rm lr}JZ_N.
\tag{10}
\]

All rows on both sides have nonnegative dense support.

## 7. Strict proxy comparison, including the extra correction index

Set

\[
V=3y^2Xp,\quad K=XpK_0,\quad
\Pi_N=XpM_N=VZ_N+K.
\]

We have deg J=6, deg V=7, deg K=7, and V=pJ+yp². The complete fixed adjacent minors of H(J),H(V) are

`w=(936750,1819824,1298778,477216,94392,8784,324)`.

Every one is positive, so all ordered base minors are nonnegative. Furthermore

\[
J(2)=22695,
\quad H(K)=(23158,20596,14430,7859,3240,962,186,18).
\]

The exact thresholds are

\[
\max_{0\le n\le6}\frac{J(2)H(K)_n}{w_n}
=\frac{234515}{18}<20000,
\]
\[
\frac{J(2)H(K)_7}{w_6}=\frac{7565}{6}<20000.
\tag{11}
\]

For 0<=n<=6, retain intermediate pair (n,n+1) in the Cauchy–Binet expansion after multiplication by K_(Z_N). Its principal kernel minor is at least delta_0(Z_N), so

\[
W_n(JZ_N,VZ_N)\ge w_n\delta_0(Z_N).
\]

For n=7 retain (6,7). The folded adjacent-minor formula bounds the remaining kernel minor below by delta_1(Z_N), so

\[
W_7(JZ_N,VZ_N)\ge w_6\delta_1(Z_N).
\]

At every n the adverse correction is bounded by

\[
W_n(JZ_N,K)\ge-J(2)Z_N(2)H(K)_n.
\]

Equations (7) and (11) therefore prove strict positivity of W_n(JZ_N,Pi_N) for n=0,...,7. This explicitly treats the extra index n=deg J+1, which the earlier central-only proxy bound did not cover.

For 8<=n<=deg(JZ_N), K has no supported coefficients, so its wedge is zero. Retain the same positive base minor w_6 at (6,7). The kernel minor is at least delta_(n-6)(Z_N)>0 because 0<=n-6<=deg Z_N. The support-boundary form gives the same result at the terminal index. Thus

\[
\boxed{JZ_N<_{\rm lr}\Pi_N\quad
(0\le n\le\deg(JZ_N),\ N\ge1).}
\tag{12}
\]

## 8. Original target and ell=0

Multiplying pX<=lr E_N through the actual TP2 kernel M_N gives

\[
\Pi_N=pXM_N\le_{\rm lr}E_NM_N=D_N.
\]

Combine this with (10)-(12):

\[
S_N\le_{\rm lr}JZ_N<_{\rm lr}\Pi_N\le_{\rm lr}D_N.
\]

The first two rows have common degree 11+5N, Pi_N has degree 12+5N, and D_N has degree 8+10N. On every interior S_N index all denominators needed for ratio transitivity are positive. The strict middle comparison therefore proves the original strict Local TP2 target there. At the terminal index its determinant is directly

\[
H(S_N)_{\deg S_N}H(D_N)_{\deg S_N+1}>0.
\]

This covers every N=ell>=1.

For ell=0 the state is the single canonical `R²` state with the other endpoint orientation. The direct integer recurrence gives its full original minor list

`(131712050280,286440837228,249104117028,129005162476,42395098972,8788090128,1093639536,73111896,1994544)`.

All are positive. This is an exact finite base proof; it is also covered by the pre-existing all-right theorem. Together with the unbounded argument above, it completes the proposed all-ell theorem.

## 9. Verification and limits

Run `python3 verify_r2_ray.py` in this directory, using Python 3 in the VS Code terminal or another shell. Only the standard library is required. It writes `r2_ray_certificates.json` and verifies every finite gate used above: 993 exact Bernstein coefficients, all fixed-base kernel defects and LR comparisons, the canonical recurrence anchor, and both scalar proxy thresholds.

The universal conclusion uses the Jacobi-resolvent argument, mixed-minor compatibility, the low-index mass propagation, and the displayed LR chain. It is not extrapolated from a finite collection of positive outer-path examples. The proof does not infer arbitrary `L^mR^kL^ell`, arbitrary root-to-node paths, or full-tree Local TP2 from this new family.
