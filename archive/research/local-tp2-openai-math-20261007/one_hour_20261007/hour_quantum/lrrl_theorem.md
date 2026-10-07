# Strict Local TP2 on the entire family LR²L^ell

**Status: PROVED_INTERNAL; shared-session independent audit PASS.**

The independent review is `hour_invariant/LRR_AUDIT.md`. It reconstructs
the original seed and all required coefficient margins using a separate
Laurent implementation, and checks the unbounded proof assembly. This
is an internal mathematical proof and audit, not a claim of external
publication or formal proof-assistant verification.

For every integer `ell >= 0`, the original Local TP2 minors at the
canonical tree node `LR²L^ell` are strictly positive throughout the
support required in the original problem. The unbounded parameter is
`ell`. No assertion about arbitrary prefixes or arbitrary numbers of
turns is made here.

This proof extends the existing relative-compatible folded-kernel method
to a second turn. Its main extra step is a quantitative bound on finitely
many kernel minors of a resolvent template. That bound absorbs both the
nonconstant base-center correction in the exact multiplier and the
correction in the strict proxy comparison. Thus the result concerns the
original coefficient minors, rather than only auxiliary kernel positivity.

The standalone standard-Python script `lrrl_certificate.py` reconstructs
the seed from the original mutations and produces `lrrl_certificates.json`.
The JSON contains **every power coefficient and every tensor Bernstein
coefficient** used below. All arithmetic is exact rational arithmetic;
every Bernstein conversion is also inverted by a separate direct basis
expansion. The script imports no modules from the earlier research.

## 1. Definitions and the exact canonical ray

Set `y=x+1`. For a polynomial `P`, write

\[
h_P(n)=[q^n]P(q+q^{-1}),\qquad n\ge0,
\]

with zero extension outside the support. Define

\[
W_n(P,Q)=h_P(n)h_Q(n+1)-h_P(n+1)h_Q(n).
\]

The notation `P <=lr Q` means that every ordered two-column minor of
their half-rows is nonnegative. For positive interval supports, it is
equivalent to the adjacent inequalities together with the support order.

The canonical mutation at endpoints `A,B` and center `C` is

\[
\mu_A(A,C,B)=3yAC-x(A+C)-B,
\qquad
\mu_B(A,C,B)=3yBC-x(B+C)-A.
\]

The initial triple is `(1, 2x²+6x+5, x+2)`. After the prefix `LRR`, the
fixed endpoint for subsequent left steps, the other endpoint, and the
center are respectively

\[
\begin{aligned}
X={}&194+801x+1408x^2+1336x^3+716x^4+204x^5+24x^6,\\
Y={}&5+6x+2x^2,\\
C_0={}&2897+18192x+51384x^2+85478x^3+92090x^4\\
 &+66484x^5+32088x^6+9960x^7+1800x^8+144x^9.
\end{aligned}
\]

Put

\[
t=3yX-x
=582+2984x+6627x^2+8232x^3+6156x^4+2760x^5+684x^6+72x^7.
\]

The inverse center is

\[
T=tY-xX-C_0=13+26x+18x^2+4x^3.
\]

The two positive seed polynomials are

\[
\begin{aligned}
A=(C_0-Y)/y={}&2892+15294x+36088x^2+49390x^3+42700x^4\\
 &+23784x^5+8304x^6+1656x^7+144x^8,\\
B=(T-Y)/y={}&8+12x+4x^2.
\end{aligned}
\]

Use an independent variable `z` to define

\[
u_0(z)=1,\quad u_1(z)=z,\quad
u_{j+1}(z)=zu_j(z)-u_{j-1}(z),\quad u_{-1}=0,
\]

and `T_k(z)=sum_(j=0)^k u_j(z)`, with `T_-1=0`. In the formulas below,
`u_j,T_k` are evaluated at `t(x)`. Define

\[
Z_k=A T_k+B T_{k-1},\qquad
q_k=y(Au_k+Bu_{k-1}),\qquad C_k=Y+yZ_k.
\tag{1}
\]

The original mutation gives, exactly,

\[
C_{-1}=Y,\quad C_{k+1}=tC_k-C_{k-1}-xX,
\quad C_k-C_{k-1}=q_k,
\quad q_{k+1}=tq_k-q_{k-1}.
\tag{2}
\]

Thus `C_k` is the center at `LR²L^k`. For `k>=1`, its endpoints are
`X,C_(k-1)`. Their degrees are `6` and `7k+2`, respectively, so the
shorter child is the next left center `C_(k+1)`. Consequently the actual
rows in the original problem are

\[
S_k=q_{k+1},\quad
E_k=C_{k-1}-X,\quad
M_k=3yC_k-x+1,\quad D_k=E_kM_k.
\tag{3}
\]

In particular

\[
\deg S_k=7k+16,\qquad \deg D_k=14k+12>\deg S_k\quad(k\ge1).
\tag{4}
\]

All support statements used here also follow from the positive
decompositions proved below. The case `k=0` has the opposite child
ordering; it is checked separately in Section 8.

## 2. Folded-kernel facts used

For a half-row `h`, its folded multiplication kernel is

\[
K_h(i,j)=
\begin{cases}
h_j,&i=0,\\
2h_i,&i>0,\ j=0,\\
h_{|i-j|}+h_{i+j},&i,j>0.
\end{cases}
\]

It acts on row vectors by `H(PQ)=H(P)K_Q`, and `K_(PQ)=K_PK_Q`.
For positive finite interval support, the established folded criterion
says that `K_h` is TP2 if and only if

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}\ge0,
\quad h_{-1}=h_1.
\tag{5}
\]

The following previously proved consequences are used with their precise
support qualifications:

1. Products of cone polynomials are cone polynomials, by finite
   Cauchy–Binet. If both factors have positive supported defects, the
   product has positive supported defects.
2. Positive supported defects imply that every supported adjacent kernel
   minor whose two diagonal entries are positive is positive. Every
   adjacent **principal** kernel minor is at least `delta_0(h)`.
3. If `delta_n(h)>=lambda h_n` for every supported `n`, then every
   ordered kernel minor with positive diagonal entries is at least
   `lambda K_h(i,k)`, with `(i,k)` its upper-left entry.
4. If the preceding strength condition holds for `H`, `H(H)>=H(B)`
   coefficientwise, and `lambda>=8H(B)[0]`, then

   \[
   \det K_H[I,J]\ge4\det K_B[I,J]
   \tag{6}
   \]

   for every ordered pair of rows and columns, provided `B` is in the
   folded cone.

These are the established results in `continuation_independent_audit.md`,
`mixed_ray_kernel_theorem.md`, and `mixed_kernel_all_minor_strength.md`.
For (6), a positive `B` minor has positive diagonal entries. Every entry
of `K_B` is at most `2H(B)[0]`, so the strength lower bound exceeds four
times its diagonal product. Nonpositive `B` minors are immediate.

## 3. Exact parameter certificates and compatible positive mixtures

For independent `r,s,c in [-2,2]`, define

\[
f_r=t-r,\qquad L_r=A(t-r)+B,
\qquad H_{r,s,c}=A(t-r)(t-s)+B(t-c).
\]

The following table records the smallest Bernstein coefficient over
**all supported defects and all parameter coefficients**. Each parameter
is independently replaced by `-2+4u`, `u in [0,1]`.

| Polynomial | Certified expression | Smallest Bernstein coefficient |
|---|---|---:|
| `A` | `delta_n` | 20,736 |
| `B` | `delta_n` | 16 |
| `yA` | `delta_n` | 20,736 |
| `t-r` | `delta_n` | 5,184 |
| `y(t-r)` | `delta_n` | 5,184 |
| `L_r` | `delta_n` | 107,495,424 |
| `yL_r` | `delta_n` | 107,495,424 |
| `H_(r,s,c)` | `delta_n - 128H(H_(r,s,c))[n]` | 557,160,726,528 |
| `y[A(t²-1)+Bt]` | `delta_n` | 557,256,278,016 |

Every listed polynomial has dense positive ordinary coefficients on the
entire parameter box. These coefficient statements, including
`H_(r,s,c)-B`, are also fully certified. Since `H(B)=(16,12,4)`, the
midpoint strength `128=8H(B)[0]` and (6) give the infinite-kernel relative
minor inequality, uniformly in the full box.

For two roots `r,s`, let

\[
F=A(t-r)(t-s)+B(t-s),\qquad
G=A(t-r)(t-s)+B(t-r).
\]

Their difference is `(r-s)B` and their midpoint is
`H_(r,s,(r+s)/2)`. On any fixed ordered rows and columns, the coefficient
of `ab` in `det(aK_F+bK_G)` is

\[
2\det K_{H_{r,s,(r+s)/2}}
-\frac{(r-s)^2}{2}\det K_B\ge0.
\tag{7}
\]

The inequality uses `|r-s|<=4` and (6). Multiplication by a common cone
polynomial preserves this nonnegative mixed-minor property: compare the
coefficient of `ab` in Cauchy–Binet. This explicitly justifies the
mixtures below; arbitrary positive-sum closure of the folded cone is
never assumed.

For either Chebyshev family `p_N=u_N` or `p_N=v_N=u_N+u_(N-1)`, the
Jacobi resolvent gives

\[
\frac{p_{N-1}(z)}{p_N(z)}
=\sum_i\frac{\lambda_i}{z-r_i},
\qquad r_i\in[-2,2],\quad\lambda_i>0,\quad\sum_i\lambda_i=1.
\tag{8}
\]

For completeness, the matrices have unit off-diagonals and zero diagonal
for `u_N`, and diagonal `(-1,0,...,0)` for `v_N`. Their spectra lie in
`[-2,2]`, are simple, and their last-coordinate spectral weights are
positive. Their last diagonal resolvent entry is the ratio in (8).

Equation (8) writes `Ap_N(t)+Bp_(N-1)(t)` as a positive mixture of

\[
L_{r_i}\prod_{j\ne i}(t-r_j).
\tag{9}
\]

Each summand is a strict supported cone product. Removing the common
omitted-root product from two summands leaves exactly `F,G` in (7).
Thus all pairwise mixed minors are nonnegative, and diagonal terms
prove strict supported defects of the mixture.

For the increment `q_k`, include the factor `y`. When `k>=3`, any two
summands have at least one common root factor; absorb `y` into that
factor, using the certified `y(t-r)`. Diagonal summands use `yL_r`.
The cases `k=0,1,2` are precisely `yA`, `yL_0`, and the last row of the
certificate table. Hence every `q_k` has positive supported defects.

The exact prefix identities

\[
T_{2h}=u_hv_h,\qquad T_{2h+1}=u_hv_{h+1}
\]

give

\[
Z_{2h}=v_h(Au_h+Bu_{h-1}),\qquad
Z_{2h+1}=u_h(Av_{h+1}+Bv_h).
\tag{10}
\]

Therefore every `Z_k` is a strict supported cone polynomial. The same
holds for `yZ_k`, by absorbing `y` into an outside root factor whenever
one exists. The remaining cases are `yZ_0=yA` and `yZ_1=yL_(-1)`.

Finally `Q_k=y²Z_k` is in the cone because `y²` has row `(3,2,1)` and
defects `(4,0,1)`. It also has positive supported defects. In
`K_(y²)K_(Z_k)`, for `n<=deg Z_k` retain intermediate pair `(0,1)`;
for the last two indices retain `(2,3)`. The corresponding `y²` defects
are positive and the supported adjacent `Z_k` minor is positive.

## 4. The weak comparisons to a fixed proxy

Let

\[
\Pi=X(x+2),\qquad f=y(t-2),\qquad g=3y^2\Pi,
\]

and

\[
M_0=3yY-x+1=16+32x+24x^2+6x^3,\qquad K=\Pi M_0.
\]

Thus the exact multiplier and proxy are

\[
M_k=M_0+3y^2Z_k,\qquad \Pi M_k=gZ_k+K.
\tag{11}
\]

Exact fixed-row arithmetic certifies

\[
q_0\le_{\rm lr}q_1,\quad
y(A+B)\le_{\rm lr}q_1,\quad
\Pi\le_{\rm lr}C_0-X,\quad
\Pi\le_{\rm lr}q_1.
\tag{12}
\]

Every adjacent comparison is strictly positive through the smaller
degree; the complete integer lists are in the JSON.

Because `q_j` has a TP2 folded kernel, multiplying the evident comparison
`1<=lr t` by `q_j` gives `q_j<=lr tq_j`. The recurrence (2) now yields,
at every ordered column pair,

\[
W(q_j,q_{j+1})=W(q_j,tq_j)+W(q_{j-1},q_j)\ge0.
\]

Induction from (12) proves the entire time order `q_j<=lr q_(j+1)`.
Also

\[
E_k=(C_0-X)+\sum_{j=1}^{k-1}q_j,
\]

so (12) gives

\[
\Pi\le_{\rm lr}E_k\qquad(k\ge1).
\tag{13}
\]

The exact telescoping identity

\[
q_{k+1}=(t-2)yZ_k+q_k+y(A+B)
\tag{14}
\]

and the time order show that both terms being subtracted from
`q_(k+1)` are narrower in likelihood-ratio order. Hence

\[
S_k=q_{k+1}\le_{\rm lr}fZ_k.
\tag{15}
\]

Here and below all rows have dense positive support; subtraction in
(14) produces the separately positive polynomial `fZ_k`.

## 5. Uniform quantitative bounds for every run length

The prefix factorization and (8) give, for every `k>=1`,

\[
Z_k=\sum_{i\in I}\lambda_iZ_i,\qquad
Z_i=L_{r_i}\prod_{j\ne i}(t-r_j),
\tag{16}
\]

where `r_1,...,r_k` are all roots of the independent-variable polynomial
`T_k(z)`, the active set `I` has `1<=|I|<=k`, and positive residues
sum to one. Each product in (16) has exactly `k-1` propagator factors.
For even `k=2h`, the active denominator is `u_h` after removing `v_h`;
for odd `k=2h+1`, it is `v_(h+1)` after removing `u_h`. This also covers
`k=1`. Distinct factors have no common roots by the Chebyshev recurrence.

The exact evaluations and bounds are

\[
A(2)=2797528,\quad B(2)=48,\quad t(2)=338722,
\]

\[
L_r(2)\le947589874320,
\quad (t-r)(2)\le338724,
\quad \delta_0(t-r)\ge435(t-r)(2).
\tag{17}
\]

The last inequality is separately certified on the whole interval.
Moreover

\[
\frac{Z_i(2)}{T_k(t(2))}=A(2)+\frac{B(2)}{t(2)-r_i}.
\]

All these numbers lie strictly between `A(2)` and `2A(2)`. Their
weighted average is `Z_k(2)/T_k(t(2))`, so

\[
Z_i(2)>\tfrac12Z_k(2),\qquad
\sum_{i\in I}\lambda_i^2\ge\frac1{|I|}\ge\frac1k.
\tag{18}
\]

The nonnegative mixed minors proved in Section 3 imply that any selected
minor of `K_(Z_k)` is at least the sum of its diagonal contributions
`sum lambda_i² det K_(Z_i)`. The same holds after multiplication by
`y²`, since that common multiplier is a cone polynomial.

Suppose a fixed adjacent row pair `(a,a+1)` and column pair `(n,n+1)`
satisfy, for every `r in [-2,2]`,

\[
\det K_{L_r}[(a,a+1),(n,n+1)]\ge\alpha L_r(2).
\tag{19}
\]

In the product for each `Z_i`, retain intermediate pair `(n,n+1)` after
the template and after every propagator. Each adjacent principal
propagator minor is at least its central defect. Equations (17)–(19)
therefore give

\[
\begin{aligned}
\det K_{Z_k}[(a,a+1),(n,n+1)]
&\ge\sum_i\lambda_i^2\alpha\,435^{k-1}Z_i(2)\\
&\ge\frac{\alpha\,435^{k-1}}{2k}Z_k(2)
\ge\frac\alpha2Z_k(2).
\end{aligned}
\tag{20}
\]

The last step uses `435^(k-1)>=k`, valid for all `k>=1`. Exactly the
same argument, with the template `y²L_r`, proves

\[
\delta_n(y^2Z_k)\ge\frac\beta2Z_k(2)
\tag{21}
\]

whenever `delta_n(y²L_r)>=beta L_r(2)` uniformly in `r`. These bounds
explicitly retain the squared spectral weights. They are not estimates
at finitely many run lengths.

## 6. The exact multiplier is a cone polynomial

Put `h=H(y²Z_k)` and `m=H(M_0)=(64,50,24,6)`, with `m_-1=m_1`.
The exact constant defects are

\[
\delta(M_0)=(632,688,240,36),
\]

so `M_0` itself is in the cone. Also
`h_j<= (y²Z_k)(2)=9Z_k(2)`.
Expanding (5) for `M_k=3y²Z_k+M_0`, its mixed part is

\[
3\bigl(2h_nm_n-h_{n-1}m_{n+1}-m_{n-1}h_{n+1}
-2h_{n+1}m_{n+1}+h_nm_{n+2}+m_nh_{n+2}\bigr).
\]

Discard the positive terms and bound the three negative terms by mass.
Then

\[
\delta_n(M_k)\ge9\delta_n(y^2Z_k)
-27Z_k(2)(m_{n-1}+3m_{n+1})+\delta_n(M_0).
\tag{22}
\]

For `n=0,...,4`, the continuum certificates give
`delta_n(y²L_r)>=beta_n L_r(2)` with the following integers:

| `n` | `beta_n` | `beta_n - 6(m_(n-1)+3m_(n+1))` |
|---:|---:|---:|
| 0 | 9,257,671,245 | 9,257,670,045 |
| 1 | 23,253,961,033 | 23,253,960,217 |
| 2 | 27,139,331,618 | 27,139,331,210 |
| 3 | 22,199,966,965 | 22,199,966,821 |
| 4 | 13,865,402,773 | 13,865,402,737 |

Equations (21) and (22) make every one of these defects positive. For
`n>=5`, the negative correction vanishes, since `m` has support only
through 3, while `y²Z_k` has positive supported defects. Thus `M_k`
has positive supported defects for every `k>=1`. Multiplying (13) by
its TP2 kernel proves

\[
\Pi M_k\le_{\rm lr}E_kM_k=D_k.
\tag{23}
\]

## 7. Strict comparison to the proxy

The degree of `f=y(t-2)` is 8 and that of `g=3y²Pi` is 9. Their nine
supported adjacent minors are

\[
w=(902402904,1937398461,1641077505,814361913,251107200,
47434752,5137056,276912,5184).
\tag{24}
\]

They are all positive, so `f<=lr g` at every ordered pair. The fixed
correction has degree 10, mass factor `f(2)=1016160`, and half-row

\[
H(K)=(5493840,5066548,3967664,2625430,1454864,665574,
245872,70824,15000,2088,144).
\tag{25}
\]

For `0<=n<=10`, take `i_n=min(n,8)`. The interval certificates prove
(19) for `(a,n)=(i_n,n)` and the following `alpha_n`:

| `n` | `alpha_n` | `w_(i_n) alpha_n - 2 f(2) H(K)[n]` |
|---:|---:|---:|
| 0 | 169,642,463 | 153,074,686,012,003,752 |
| 1 | 2,064,106,360 | 3,998,986,188,357,480,600 |
| 2 | 2,831,195,954 | 4,646,203,928,793,514,290 |
| 3 | 2,384,116,463 | 1,941,528,307,909,576,119 |
| 4 | 1,904,306,391 | 478,182,089,036,910,720 |
| 5 | 1,741,592,332 | 82,610,647,694,169,984 |
| 6 | 1,716,888,939 | 8,819,254,934,840,544 |
| 7 | 1,715,350,492 | 474,857,198,409,024 |
| 8 | 1,715,324,201 | 8,861,755,857,984 |
| 9 | 1,545,681,738 | 8,008,570,645,632 |
| 10 | 1,129,953,741 | 5,857,387,539,264 |

Cauchy–Binet, retaining `(i_n,i_n+1)`, and (20) imply

\[
W_n(fZ_k,gZ_k)\ge\tfrac12w_{i_n}\alpha_n Z_k(2).
\tag{26}
\]

The only possibly negative part of the correction satisfies

\[
W_n(fZ_k,K)\ge-f(2)Z_k(2)H(K)[n].
\tag{27}
\]

The positive residuals in the table prove, for every `0<=n<=10`,

\[
W_n(fZ_k,gZ_k+K)>0.
\tag{28}
\]

At `n>=11`, both correction entries vanish. Retain the input pair
`(i,i+1)` with `i=min(n,8)` in Cauchy–Binet. Its fixed minor (24) is
positive, and the corresponding adjacent kernel minor of `Z_k` is
positive whenever

\[
0\le n-i\le\deg Z_k.
\]

This holds at every index through
`deg(fZ_k)=deg S_k=7k+16`. Thus (28) is strict throughout the required
support, including the terminal index. In particular

\[
fZ_k<_{\rm lr}gZ_k+K=\Pi M_k
\tag{29}
\]

in the supported adjacent sense needed here.

## 8. Conclusion and initial state

Combining (15), (29), and (23) gives

\[
S_k\le_{\rm lr}fZ_k<_{\rm lr}\Pi M_k\le_{\rm lr}D_k
\qquad(k\ge1).
\]

For `0<=n<deg S_k`, all relevant row entries are positive, so ratio
transitivity preserves the strict middle comparison. At `n=deg S_k`,
the next `S_k` entry vanishes while `D_k` has a positive next entry by
(4). Hence

\[
F_{LR^2L^k}(n)
=H(S_k)[n]H(D_k)[n+1]-H(S_k)[n+1]H(D_k)[n]>0
\]

for every required `n` and every integer `k>=1`.

At `k=0`, the original short child is the right child, of degree 12,
while the left child has degree 16. Direct exact evaluation from the
canonical mutation gives 13 positive Local TP2 minors. The smallest is
`15,896,632,320`; the complete list is in the JSON. This supplies the
single finite initial case, so the theorem holds for every `ell>=0`.

## Relation to the public OpenAI mathematics material

Family 169 suggested separating a positive summand construction from
the exact identification of the target, while Family 180 suggested
explicit control of mixed paired-state terms. Neither source's stated
theorem directly implies the result here. The proof above uses the
existing AIMath folded-kernel and Jacobi-resolvent framework, with new
fixed-prefix parameter certificates and new quantitative correction
bounds that reach the original `F_n`. This is an actual extra infinite
family; it does not settle the full binary tree.
