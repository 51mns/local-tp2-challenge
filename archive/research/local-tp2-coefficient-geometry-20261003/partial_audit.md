# Independent audit of the universal positivity and terminal-minor argument

This note audits a partial result only. It does **not** prove the interior local TP2 inequalities.

## Definitions and result

Work in `Z[x]`, with coefficientwise order `P ≼ Q`. A polynomial is *dense positive* when every coefficient from degree zero through its degree is strictly positive.

The root state, oriented by endpoint degree, is

\[
 (X,Y,C)=(1,x+2,2x^2+6x+5).
\]

For either endpoint `T`, let `Z` be the other endpoint and put

\[
 W_T=3(x+1)TC-x(T+C)-Z.
\]

Its child state has endpoints `(T,C)` and center `W_T`. At an oriented state define

\[
 U=W_X,\qquad V=W_Y,\qquad S=U-C,\qquad D=V-U.
\]

For a polynomial `P`, set

\[
 H(P)_k=\sum_{\substack{j\ge k\\j-k\text{ even}}}
       P_j\binom{j}{(j-k)/2},\qquad k\ge0,
\]

with coefficients and transformed coefficients zero above their supports. Write `s=deg S`, `d=deg D`, and

\[
 F(k)=H(S)_kH(D)_{k+1}-H(S)_{k+1}H(D)_k.
\]

**Audited result.** At every finite node of this canonical tree, `S` and `D` are dense positive integral polynomials, `d>s`, and

\[
 F(s)\ge24>0.
\]

The bound is attained at the root. The claims about dense positivity and unequal degrees are unconditional consequences of the mutation recurrence; no finite enumeration is needed.

## A simultaneous induction that closes all positivity gaps

The following stronger invariant holds at every state:

1. `a=deg X < b=deg Y < c=deg C`, with `c=a+b+1`.
2. `1 ≼ X ≼ Y ≼ C`; all three polynomials are dense positive and integral.
3. `Y-X` and `C-Y` are dense positive through degrees `b` and `c`, respectively. Consequently `C-X` is dense positive through degree `c`.
4. Every coefficient of `C`, from degree zero through degree `c`, is at least 2. Also `C_0≥5`.
5. The only constant polynomial occurring in the tree is `1`; every other polynomial has constant coefficient at least 2.

These statements hold directly at the root: `Y-X=1+x`, `C-Y=3+5x+2x²`.

The proposed identity is algebraically exact:

\[
 W_T-C=3(x+1)(T-1)C+x(2C-T)+(2C-Z).\tag{1}
\]

Because `T ≼ C` and `Z ≼ C`, both `2C-T` and `2C-Z` dominate `C` coefficientwise.

* If `T=1`, the first term of (1) vanishes. The remaining sum dominates `(1+x)C`, so every coefficient through degree `c+1` is at least 2. Its leading coefficient is exactly `2 C_c`, so its degree is `c+1`.
* If `T≠1`, then `t=deg T≥1`, and `T-1` is dense positive: its constant coefficient is positive by invariant 5, and its higher coefficients agree with those of `T`. The first term of (1) is therefore dense positive through degree `t+c+1`, with every coefficient at least 6. The other two terms are coefficientwise nonnegative. Thus `W_T-C` is dense positive through degree `t+c+1`, and its leading coefficient is `3 T_t C_c`.

In both cases,

\[
 \deg W_T=\deg(W_T-C)=t+c+1>c.
\]

The new endpoints `(T,C)` are already oriented by degree. Their difference `C-T` is dense positive through degree `c`; the new center-to-larger-endpoint difference is `W_T-C`, just proved dense positive. Thus the endpoint and center order invariants propagate. The new center has every coefficient at least 2, its constant coefficient strictly exceeds the old center's, and its degree is positive. This also propagates invariants 4 and 5. Finally the new center-degree identity is exactly `c'=a'+b'+1`.

There is consequently no hidden assumption that degree order implies coefficient order: coefficient order is proved separately by this simultaneous induction.

## S and D

Apply (1) with `T=X` to obtain dense positivity of `S=U-C` and

\[
 s=a+c+1.
\]

Subtracting the two mutation formulas gives the exact factorization

\[
 D=(Y-X)\bigl(3(x+1)C+1-x\bigr).\tag{2}
\]

The second factor is dense positive. Indeed, writing it as `B`, its coefficients are

\[
 B_0=3C_0+1,\quad
 B_1=3(C_0+C_1)-1,\quad
 B_k=3(C_{k-1}+C_k)\ (2\le k\le c),\quad
 B_{c+1}=3C_c.
\]

Every coefficient is at least 6, by the center coefficient invariant. Since `Y-X` is dense positive and integral through degree `b`, (2) shows that `D` is dense positive through degree

\[
 d=b+c+1>s.
\]

Moreover, every coefficient `D_k` for `0≤k≤d` is at least 6: each such convolution coefficient has at least one summand formed from a coefficient of `Y-X` at least 1 and a coefficient of `B` at least 6.

## Transform support and the terminal lower bound

The transformation `H` preserves degree and the leading coefficient. It also maps a dense positive polynomial to a sequence strictly positive at every index inside its support, since the summand `j=k` is the positive coefficient `P_k`.

The leading coefficient of `S` is

\[
 S_s=\begin{cases}
 2C_c,&X=1,\\
 3X_aC_c,&X\ne1,
 \end{cases}
\]

so `H(S)_s=S_s≥4`. Because `s+1≤d`, we also have `H(D)_{s+1}≥D_{s+1}≥6`, whereas `H(S)_{s+1}=0`. Hence

\[
 F(s)=H(S)_sH(D)_{s+1}\ge4\cdot6=24.
\]

At the root,

\[
 S=8+20x+16x^2+4x^3,\qquad
 D=16+48x+56x^2+30x^3+6x^4,
\]

and `F(3)=4·6=24`. This root arithmetic is checked in the included `verify.py`; it is illustrative and is not the basis of the universal proof.

## Degree labels, if the rational Stern–Brocot labels are used

For a reduced label `p/q` in this tree,

\[
 \deg G_{p/q}=p+q-1.
\]

It holds for the root labels `0/1`, `1/1`, and `1/2`. Neighboring boundary labels have determinant of absolute value 1. Their mediant is already reduced: a common divisor of the new numerator and denominator would divide that determinant. Each child label is the mediant of its retained endpoint and old center, so its numerator-plus-denominator is the sum of those two heights. The just-proved degree recurrence `deg W=deg T+deg C+1` completes the induction. Degree inequalities can alternatively be obtained entirely from the state invariant, without rational labels.

## Exact implication from adjacent minors to all ordered minors

Let `A_k=H(S)_k` and `B_k=H(D)_k`. For `0≤i<j`, consider

\[
 M(i,j)=A_iB_j-B_iA_j.
\]

If every adjacent `F(k)≥0` for `0≤k<s`, the ratios `B_k/A_k` are nondecreasing for `0≤k≤s`. Therefore `M(i,j)≥0` for all `i<j`:

* For `j≤s`, this follows from the ratio comparison.
* For `i≤s<j≤d`, it follows from `M(i,j)=A_iB_j>0`.
* If `i>s` or `j>d`, the minor is zero by support.

If the adjacent inequalities are **strict**, `F(k)>0` for `0≤k<s`, then the ratios strictly increase, and the exact strictness region is

\[
 M(i,j)>0\quad\Longleftrightarrow\quad 0\le i<j,\ i\le s,\ j\le d.
\]

Nonnegative adjacent minors alone do **not** imply strictness for pairs lying wholly inside `0,…,s`. This distinction should be preserved in any theorem statement.

## Audit verdict and remaining work

The partial proof is sound with the induction and support arguments made explicit as above. It proves the endpoint `F(deg S)≥24`, dense coefficient positivity, degree orientation, and the reduction from all ordered minors to adjacent ones. It does not prove `F(k)>0` for the interior indices `0≤k<deg S`; those are precisely the remaining local TP2 inequalities.
