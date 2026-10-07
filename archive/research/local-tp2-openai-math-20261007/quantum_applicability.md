# Family 169: exact quantum-minor applicability boundary

Status: algebraic identities and a bounded applicability analysis. This is not a new proof of universal Local TP2 and does not rule out other quantum or theta lifts.

Let s_i=H(S)_i and d_i=H(D)_i, extended by zero outside finite support, and W_ij=s_i d_j-s_j d_i. Use a quantization parameter v distinct from the Laurent variable q in H. In the centered rank-two quantum torus,

X_(a,b) X_(c,d) = v^(ad-bc) X_(a+c,b+d).

## 1. Two axis lifts must not be conflated

Put S_A=sum_i s_i X_(i,0), S_B=sum_i s_i X_(0,i), and define D_A,D_B likewise.

| Candidate | Coefficient at X_(i,j) | Exact implication |
|---|---|---|
| Reversed-order antisymmetrization Q=S_A D_B-S_B D_A | s_i d_j v^(ij)-s_j d_i v^(-ij) | At v=1 this is W_ij. For i,j>0 with both products positive it has a negative Laurent coefficient, so this candidate is not strongly quantum-positive in the chosen chart. |
| Same-order determinant Q'=S_A D_B-D_A S_B | v^(ij) W_ij | Positivity in the half-cone i<j is exactly the original all-pairs TP2 assertion. Without an independent theta identification, invoking family 169 here is circular. |

These formulas follow directly from the torus multiplication rule; they differ because the second product is ordered differently.

The whole ordered polynomial Q' cannot be coefficientwise nonnegative: W_ji=-W_ij gives the opposite sign in the opposite sector. At the root its coefficient at X_(1,0) is -272. The exact comparison with TP2 concerns the upper sector i<j, with zero padding and the original support/strictness conditions. Extracting that sector is an additional operation whose compatibility with any proposed theta or wall construction must be proved.

At the canonical root, s=(40,32,16,4) and d=(164,138,80,30,6). Thus

- [X_(1,2)]Q = 2560 v^2 - 2208 v^(-2), while W_12=352;
- [X_(1,2)]Q' = 352 v^2;
- [X_(2,3)]Q = 480 v^6 - 320 v^(-6), while W_23=160.

For the specific Q above, replacing the second product by v^kappa times it aligns the two powers at (n,n+1) only when kappa=2n(n+1). No one fixed scalar aligns all adjacent positions. This statement concerns this ordering and this scalar correction only. Index-dependent changes, different monomial embeddings, same-order Q', classical specialization, or other wall models are not excluded.

## 2. A genuine commutator that retains the minors

Instead put the coefficient lists on an affine line:

A=sum_i s_i X_(i,1),  B=sum_i d_i X_(i,1).

For r>=1 define [r]_v=(v^r-v^(-r))/(v-v^(-1)). Then the following identity holds for every pair of finite lists:

(BA-AB)/(v-v^(-1))
 = sum_(i<j) W_ij [j-i]_v X_(i+j,2).                       (1)

Proof: the two contributions with indices i<j to BA-AB are

(d_i s_j-s_i d_j)v^(i-j)+(d_j s_i-s_j d_i)v^(j-i)
 = W_ij (v^(j-i)-v^(-(j-i))).

The diagonal i=j vanishes. Summing proves (1), and also proves divisibility by v-v^(-1) over the integral Laurent coefficient ring.

Write C_N(v) for the X_(N,2) coefficient in (1). For N=2n+1,

C_(2n+1)(v)=sum_(i=0)^n W_(i,2n+1-i) [2n+1-2i]_v.

Because every odd quantum integer [2r+1]_v contains v^0 and contains v^2 exactly when r>=1,

W_(n,n+1) = [v^0]C_(2n+1)(v)-[v^2]C_(2n+1)(v).          (2)

At the root C_3(v)=544[3]_v+352[1]_v=544v^2+896+544v^(-2); equation (2) returns 896-544=352.

This is a precise commutator bridge, but not a new positivity theorem. It is the quantum-integer/SU(2)-character analogue of the existing Bezoutian representation. Ordinary Laurent positivity of C_N does not force the difference in (2) to be positive. The elementary example v^2+v^(-2)=[3]_v-[1]_v distinguishes these cones.

## 3. Why family 169 does not finish the proof at this stage

Source: *Elementary positivity of chromatic quasisymmetric functions*, section 3 `alg:reordering`, section 4 `wall:recursion` and `wall:positivity`.

The positive-reordering theorem assumes an admissible product in ray order with a consistently positive alternating pairing between earlier and later distinct rays. For the affine-line lift,

Omega((i,1),(j,1))=i-j.

At a canonical state, S and D are both positive on a nontrivial overlapping index interval. Therefore the pairings between terms from the two full packets have both signs (already i=0,j=1 and i=1,j=0 at the root). One cannot simply designate A as one input ray packet and B as the other and invoke the theorem. Factoring/reordering individual rays is possible formally, but comparing the two differently weighted packet products is additional information, precisely where W_ij enters.

The source's target-dependent coefficient recursion can prove positivity after nonnegative incoming coefficients and a valid wall system have been independently established. For Q' those incoming coefficients are not known. For the genuine commutator, positivity also has to be in the finite quantum-integer basis, or establish the strict central coefficient drop in (2); the source's arbitrary nonnegative Laurent-series conclusion alone is weaker.

In particular, the source's `alg:strings` uses infinite Weyl-algebra strings with weights h,h+1,... . These are not the finite SU(2) characters [2r+1]_v in (2). A theorem about those source strings does not supply nonnegative finite-string multiplicities here without another identification.

Pinned source sections: [reordering](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/03-reordering.tex), [walls](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/04-walls.tex), and [identification](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/05-triangle.tex).

Thus the bounded outcome is:

1. A direct reversed-order lift fails strong quantum positivity in the root chart.
2. A same-order lift is an exact re-encoding of TP2, and needs a noncircular theta identification.
3. A genuine commutator gives exact quantum-integer formulas and a concrete missing ray-order/finite-string positivity condition. It does not yet enlarge the set of proven canonical words.

An eventual positive result would require a decorated canonical state space, positive incoming wall data, and an identification of its finite string multiplicities with W_ij, or a target-specific positive recursion that proves the strict difference (2). None is claimed here.
