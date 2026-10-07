# Independent mathematical audit of the two mixed-ray theorems

**Verdict: PASS.** The proof in `mixed_ray_all.md`, using
`mixed_ray_kernel_theorem.md` and the stated exact parameter certificates,
proves the original strict Local TP2 inequality at every canonical state
`LR^k` and `RL^k`, for all integers `k>=0`. The result concerns these
two infinite families. It does not prove arbitrary mixed words or the
full canonical tree.

This audit checks the mathematical assembly, including the infinite
index argument, coefficient signs, supports, and strictness. The
continuum certificates have their own independent arithmetic replay.
In addition, this audit independently reconstructed all six original
finite bases from the frozen canonical recurrence and compared every
saved array and minor, as described below.

## 1. Canonical identification and both weak comparisons

Use the manuscript's notation

`y=x+1`, `P1=x+2`, `P=2x^2+6x+5`,

`t=3yP-x`, `w=2P1(2x+3)`.

The retained endpoint on each mixed tail is P. Subtracting successive
center recurrences gives the homogeneous gap recurrence
`q_(k+1)=t q_k-q_(k-1)`. Its two actual initial conditions yield
precisely the displayed left and right mixed Chebyshev combinations.
The seed for the right family is P1, so its initial gap is
`y(t+w)`, not `y(t+w+1)`. The manuscript distinguishes these correctly.

For k>=1 the prior center has greater degree than P. The short child
therefore retains P, giving `S_k=q_(k+1)`. The difference of the two
mutations gives `D_k=E_k M_k` with the stated E and M. If d is the
degree of the current center, the child degrees are d+3 and 2d-2.
Here d=3k+3 or 3k+4, so the latter is strictly larger for every k>=1.

Each mixed gap q_j has a folded-TP2 kernel. Broadening by the positive
polynomial t and the exact recurrence propagate the verified initial
comparison `q_0<=lr q_1` to every successive pair. This argument is
valid even beyond the support of the preceding shorter row.

The endpoint comparison uses one fixed lower row B0=P1P for all
summands of E_k. Thus summing the upper rows is legitimate. It proves
`B0<=lr E_k` without a closure assumption for arbitrary sums of cone
polynomials.

For the second weak comparison, the residual identity is exact because

`(t-2)-xP=(2x+3)P-P1=y(w+1)`.

Hence `S_k=(t-2)yZ_k+q_k+y(w+1)`. Gap time order and the listed fixed
base comparisons put both residual summands below S_k in LR order.
Writing F=(t-2)yZ_k, bilinearity gives
`W(S_k,F)=W(q_k+y(w+1),S_k)>=0` for every ordered pair. F has a
dense positive row, so the subtraction step is valid and proves
`S_k<=lr F`.

## 2. Compatible resolvents and the unbounded prefix margin

The compatibility theorem's principal-minor estimate is valid. After
positive diagonal symmetrization, TP2 and a principal minor imply

`A(i,j)^2<=A(i,i+1)^2 A(j,j)/A(i+1,i+1)`.

The diagonal ratio is at least one half. Therefore every principal
minor is at least half the central folded defect. This is sufficient
for the constant-difference compatibility identity: the midpoint
defect greater than eight compensates for every difference of absolute
value at most four. For nonprincipal pairs the identity-matrix minor
vanishes. Cauchy--Binet preserves this pairwise compatibility under a
common cone factor.

The Jacobi resolvent proof is legitimate for both u_N and v_N. The
Jacobi matrices are irreducible real symmetric matrices with unit
off-diagonals, and with either zero diagonal or first diagonal entry
-1. Their simple spectra lie in [-2,2]; the last components of their
eigenvectors are nonzero. Thus the residues are positive and sum to
one. The extra y factor is absorbed into a remaining root factor when
the degree permits; all exceptional low-degree cases are separately
certified.

For the quantitative prefix argument, the four active denominators are
correct:

| Prefix | k=2h | k=2h+1 |
| --- | --- | --- |
| Left family | u_h | v_(h+1) |
| Right family | v_h | u_h |

The corresponding outside factors account for all other roots of T_k.
Thus each summand is exactly an L_a or R_a template times all roots of
T_k except one active root. The active residue count can be less than
k; the weaker bound `sum lambda_i^2>=1/k` remains valid. No fictitious
Jacobi interpretation of the whole prefix T_k is needed.

The balanced-pair root count is correct. Opposite u roots pair with
zero linear coefficient. For v roots, the magnitude of the negative
partner is at least that of the positive partner and at most two.
The resulting pair has the form `t^2+s t-c` with s in [0,2] and c in
[0,4]. Any unpaired v root lies in [-1,0]. If both a zero u root and
an unpaired v root occur, they form one more allowed pair. Consequently
T_k has at most one unpaired factor; deleting one root leaves at least
`floor((k-2)/2)` balanced pairs and at most two single factors.

The squared weights are essential and are handled correctly:

`delta_0(Z)>=sum lambda_i^2 delta_0(Z_i)`.

This uses certified nonnegative mixed minors, not just individual
cone membership. The product estimate
`delta_0(FG)>=delta_0(F)delta_0(G)` retains the principal intermediate
pair (0,1) in Cauchy--Binet. Combining it with the four continuum
margins gives the stated factor `40*(4/5)^2*90^J`, or its right-ray
analogue with 100. Fewer than two singles only improves the bound.

At x=2, t=223 and w=56. The exact summand masses divided by T_k(2)
are `56+1/(223-a)` and `279-1/(223-a)`, respectively. Each exceeds
half the mass of their weighted average. This justifies the mass
comparison independently of the residue sizes. The resulting lower
bound is

`delta_0(Z_k)/Z_k(2)>[64/(5k)]*90^floor((k-2)/2)`

for the left family, with a larger bound for the right. It exceeds
75 at k=4 and k=5; advancing by two multiplies the expression by
`90k/(k+2)>1`. Hence the needed margin holds at every k>=4.

## 3. Multiplier and proxy strictness, including terminal indices

Although y^2 has one zero folded defect, Q=y^2Z has strictly positive
supported defects. In `K_(y^2)K_Z`, the intermediate pair (0,1) gives
strictness through degree(Z). The pair (2,3), whose first minor is one,
gives the last two indices; the corresponding Z minors are
`Delta_(d-1)>0` and `h_d^2>0`. This covers the full support and does
not rely on an invalid general strict-product assertion.

In the opposite product order, (0,1) gives
`delta_2(Q)>=delta_0(Z)`. Together with `H(Q)[3]<=9Z(2)`, the prefix
margin makes the potentially negative correction in delta_2(M)
strictly harmless. The manuscript's four formulas for the defects of
`M=3Q+2P1` are exact. The other low corrections are nonnegative by
the monotonicity of cone rows. Thus M is a strict supported cone
multiplier for k>=4, proving `P1 P M<=lr D`.

For the strict proxy comparison, the five fixed adjacent minors are
`(2232,2790,1860,378,36)`. The low-output-index Cauchy--Binet term
uses the corresponding adjacent principal kernel minor, which is at
least delta_0(Z). The remainder K=2PP1^2 satisfies

`W_n((t-2)yZ,K)>=-663 H(K)[n] Z(2)`.

The five exact positive differences
`75m_n-663H(K)[n]=(26844,95214,79830,9786,48)` therefore prove
strictness at indices zero through four. This bound even leaves a
positive margin at the smallest case, index four.

Above index four K contributes zero. At every remaining index
n<=degree(Z)+4, retaining the base pair with first index
`i=min(n,4)` gives a strictly positive kernel minor: its displacement
`n-i` belongs to [0,degree(Z)]. At the terminal displacement it is
the positive leading square. Hence the proxy comparison is strict
through its full required range.

Finally `degree(S)=degree((t-2)yZ)=degree(Z)+4`, and the strict proxy
has one additional degree. All rows are dense and positive on their
supports. The weak--strict--weak LR chain therefore yields strict
original S,D minors at every n<degree(S). At n=degree(S), strictness
also follows directly from `H(S)[n]>0`, `H(S)[n+1]=0`, and
`H(D)[n+1]>0`. There is no lost terminal case.

## 4. Independent original finite bases and scope

I reconstructed the canonical states LR^k and RL^k for k=1,2,3 using
the frozen `tp2_source.py` recurrence, independently of the new
`mixed_ray_bases.py` implementation. Every ordinary S,D array, every
half-row, and every F entry agrees exactly with
`mixed_ray_bases.json`. All 81 required minors are positive, and every
D degree exceeds its S degree. The base generator also contains its
separate direct Laurent implementation.

The k=0 states are already covered by the established all-left and
all-right results. These bases together with the unbounded k>=4 proof
complete the two stated mixed-ray theorems. General canonical words
with further alternations remain outside this proof.
