# Independent audit of strict Local TP2 on L²R^k

**Verdict: PASS for every integer k>=0.** The proof in
`general_one_turn_m2.md` closes the original Local TP2 inequality on
this entire one-turn ray. It does not establish arbitrary initial
left-run length m or arbitrary canonical words.

The independent verifier `general_one_turn_m2_full_audit.py` reconstructs
the fixed coefficient data, canonical seeds, exact fixed comparison
rows, and both continuum mass margins using the frozen canonical
polynomial helper. It does not import the new certificate generators.
Its output is `general_one_turn_m2_full_audit.json`.

## 1. Identification with the original canonical problem

The fixed endpoint P=(13,26,18,4) is exactly the center at L. The
center C_0 at L² equals `1+ya`, with a=(33,64,40,8). The first right
gap from that state is exactly `y(at+b)`, where b=(4,2) and
t=(39,116,132,66,12). These assertions were independently checked
against the original mutations, not just the new closed formulas.

The fixed-endpoint mutation gives
`C_(k+1)=tC_k-C_(k-1)-xP`, with C_-1=1, and subtraction gives the
homogeneous gap recurrence. Thus the stated outer Chebyshev formulas
have the correct seeds and hold for every k.

For k>=1 the fixed endpoint has degree three and the other endpoint
has degree 4k, so the fixed endpoint is the short-child endpoint.
Consequently S_k=q_(k+1), and direct subtraction of the two mutations
gives D_k=E_kM_k. The degrees are

`degree(C_k)=4k+4`, `degree(S_k)=4k+8`,

`degree(D_k)=8k+5`.

The last exceeds degree(S_k) already at k=1. Thus no child-orientation
exception is omitted. The case k=0 is separately covered by the
established all-left theorem.

The uniform initial endpoint/gap/correction comparisons and their
conditional propagation were independently proved in
`general_one_turn_preliminary_audit.md`. The fixed-m=2 increment-kernel
theorem supplies the only cone assumption in that propagation, giving
both weak preliminary sandwiches unconditionally here.

## 2. Relative kernel compatibility really applies to all outer indices

The finite reduction in `general_one_turn_kernel_theorem.md` is sound.
For a positive minor of K_B, bandwidth one forces columns i+e,j+f
with e,f in {-1,0,1}. With degree(H)=11, shifting a first row above
13 down to 13 leaves every relevant entry in the Toeplitz region.
Reducing a row gap above 13 to 13 leaves both cross entries zero and
preserves both diagonal entries. Boundary index zero causes no
exception in the gap reduction. Thus the stated 1,543 patterns cover
every pair with a positive B minor; a zero B minor is handled by the
separate cone certificate for H.

The relative bound `det(K_H)>=4det(K_B)` is exactly what is needed
for differences `(r-s)B`. The mixed-minor identity gives

`mixed(K_F,K_G)=2det(K_H)-(r-s)^2det(K_B)/2>=0`

because |r-s|<=4 and K_B is TP2. This controls nonprincipal minors
as well as principal ones. Common cone factors preserve compatibility
by Cauchy--Binet. The positive Jacobi-residue sums therefore yield
the required all-index cone statements without assuming closure under
arbitrary positive sums.

Strict supported defects follow from the positive diagonal terms in
the sum: all summands have the same degree and strictly positive
supported defects. The extra y factor is handled by an omitted root
factor when the outer degree is at least three, with degrees zero,
one, and two separately certified. The parity factorization of the
prefixes covers Z_k and yZ_k, including k=0,1.

## 3. Exact interval margins and the squared-residue bound

The independent audit computes the two differences directly in Z[u],
with r=2-4u and 0<=u<=1:

`delta_0(t-r)-4(t-r)(2)=3009+3688u+16u^2`,

`delta_0(a(t-r)+b)-800[a(t-r)+b](2)`

`=9999933+9224984u+28816u^2`.

All coefficients are positive. Thus their strict positivity on the
whole interval is established directly, and the coefficients agree
exactly with the source's exported Bernstein certificates.

For k=2h the active Jacobi factor is the outer U_h; for k=2h+1 it is
the outer adjacent sum U_(h+1)+U_h. The complementary factor supplies
all other roots of the prefix T_k. Every active denominator has
positive degree for k>=1, in particular at k=1. There are at most k
positive residues and they sum to one.

Each resolvent summand contains one template a(t-r)+b and exactly
k-1 propagators t-r. Pairwise compatibility gives the crucial
quadratic bound with squared weights,

`delta_0(Z_k)>=sum_i lambda_i^2 delta_0(Z_i)`.

Retaining intermediate indices (0,1) in Cauchy--Binet proves
`delta_0(FG)>=delta_0(F)delta_0(G)` for these cone factors. It follows
that every summand has defect-to-mass ratio greater than
`800*4^(k-1)`.

The independently checked masses are t(2)=1519, a(2)=385, and b(2)=8.
Every summand divided by T_k(2) has mass
`385+8/(1519-r)`, which lies strictly between 385 and 386. Therefore
each summand mass exceeds half of the weighted-average mass. Together
with `sum lambda_i^2>=1/k`, this gives

`delta_0(Z_k)>[400*4^(k-1)/k] Z_k(2)>=400 Z_k(2)`.

The final inequality holds at k=1 and propagates by the factor
`4k/(k+1)>1`. Thus the proof covers every k>=1, with no finite-index
exceptions or extrapolation from samples.

## 4. Multiplier and full-support strict comparison

For Q=y²Z_k, retaining (0,1) in K_(y²)K_Z proves strict defects
through degree(Z). The retained pair (2,3) supplies the last two
indices; the relevant Z minors are positive by the leading/support
boundary formula. Thus the zero middle defect of y² does not create
a gap in the strictness proof.

In the reverse product order, (0,1) gives
`delta_2(Q)>=delta_0(Z_k)`. Since H(Q)[3]<=9Z_k(2), the central mass
bound implies `3delta_2(Q)>2H(Q)[3]`. The source's four explicit
defect expansions for `M=3Q+2P1` are exact. They prove strict cone
membership for M throughout its supported range and every k>=1.

The independently reconstructed fixed proxy rows are

`H(Ay)=(1001,867,560,258,78,12)`,

`H(By)=(3750,3306,2250,1155,426,102,12)`,

`H(K)=(1268,1076,650,268,68,8)`, with `(Ay)(2)=4551`.

All six source adjacent minors agree exactly. After subtracting the
worst-case positive-polynomial remainder bound, the margins at central
threshold 256 are

`(9091668,20546964,14014650,3853740,418596,456)`.

They are positive; the actual central ratio exceeds 400. The
adjacent-principal-minor lower bound therefore proves strict proxy
comparison for output indices zero through five.

Above index five, the remainder K contributes zero. Retaining the
base pair with first index i=min(n,5) gives a strictly positive kernel
minor whenever `0<=n-i<=degree(Z_k)`. At the terminal displacement
it is the positive leading square. This proves strictness through
degree(AyZ_k)=4k+8, with no unsupported extension of finite-band
strictness.

The final weak--strict--weak chain preserves strictness at every index
below degree(S). At the terminal index the original minor is directly
positive because H(S) is positive there, vanishes at the next index,
and H(D) is still positive at that next index. All required supports
are dense and positive by the proved cone constructions and canonical
support theorem.

## Conclusion

The original strict Local TP2 statement is proved on L²R^k for every
k>=0. All k>=1 follow from the uniform quantitative proof; k=0 is the
already established all-left state. The proof supplies a new entire
one-turn ray, not closure for every initial run length or the full
canonical tree.
