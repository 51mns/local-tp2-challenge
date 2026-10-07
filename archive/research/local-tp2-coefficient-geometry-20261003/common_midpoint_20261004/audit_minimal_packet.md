# Exact midpoint packet: redundant gates removed, transport still open

Status: the following sharp packet is a valid replacement for the old
uniform-4 midpoint packet in its origin-run, register, and target implications.
Its definition removes redundant H gates and converts the infinite mixed
condition to an exact finite character test. This is a logical reduction;
arbitrary regular-state BOTH-child preservation is still OPEN.

## 1. Explicit packet and its scope

Let T be a real polynomial of positive degree d, b0 a nonzero real
polynomial of degree p>=0, and b1 a real polynomial satisfying

`deg b1 < p+d`.

The zero seed b1 is allowed, with degree -infinity. One-sign signed seeds
are permitted, but their absolute values are not required to be cones.
Canonical ordinary bounds and Fricke correlations remain part of the
actual common predicate; they are not replaced by this abstract packet.

Write

`L_r=b0(T-r)+b1`,
`F_rs=L_r(T-s)`, `G_rs=L_s(T-r)`,
`H_rs=b0(T-r)(T-s)+b1(T-(r+s)/2)`.

Define MP_sharp(T,b0,b1) by these three requirements:

1. For every r in [-2,2], T-r has positive Fourier interval support and
   a weak folded-TP2 kernel.
2. For every r in [-2,2], L_r and yL_r have positive Fourier interval
   support and strictly positive folded defects at every supported index.
3. For every r,s in [-2,2], every ordered folded mixed minor of F_rs,G_rs
   is nonnegative, separately in the raw and y-smoothed modes.

There is no b0, yb0, b1, or yb1 folded-cone requirement. In particular the
actual reversed root has b0=1 and delta_0(yb0)=-1, so such an auxiliary
requirement would exclude the root. Neither H support nor an H cone is a
separate premise. The degree condition is essential in the strict-product
argument below; unrestricted strict-times-weak preservation is not claimed.

This is the sharp sufficient certificate for the stated resolvent proof.
No claim is made that it is the weakest possible predicate implying the
original Local TP2 target.

## 2. Exact strict-times-weak lemma, including both boundaries

Let A have positive Fourier interval support of degree f and strictly
positive supported folded defects. Let B have positive interval support
of degree h>=1 and a weak folded-TP2 kernel. Assume f>=h. Then AB has
strictly positive supported folded defects.

For the half-row b of B, set
`Delta_j=b_j^2-b_(j-1)b_(j+1)`, with reflection at zero. The exact
telescoping identity is

`Delta_j=sum_(k=j)^h delta_k(B)>0`, `0<=j<=h`,

because every delta_k is nonnegative and the terminal
`delta_h=b_h^2` is positive. Folded multiplication gives
`K_AB=K_A K_B`. For an output defect index 0<=n<=f+h, retain the
Cauchy--Binet term with intermediate adjacent indices i,i+1, where

`i=max(h,min(n,f))`.

Then 0<=i<=f. Its first minor is `delta_i(A)>0`. For n>=1, i>=h
implies every sum-index term b_(i+n), b_(i+n+1), b_(i+n+2) vanishes.
The remaining second minor is exactly `Delta_|i-n|>0`; also
`|i-n|<=h` on the entire stated output support. For n=0, i=h and the
second minor is `2b_h^2>0`, using the central-column factor two.
All other Cauchy--Binet terms are nonnegative. This proves the lemma.

Since deg L_r=p+d>=d, the lemma applies to L_r or yL_r times any
one shifted trace. Repeating the lemma is valid: each multiplication
increases the strict factor's degree, so it stays at least d. Positive
interval support is preserved by convolution of positive interval rows.

## 3. H gates follow from the exact mixed gate

The degree bound gives deg L=p+d and deg F=deg G=p+2d. Each of F,G
is strict by Section 2, as is each smoothed product yF,yG. They have
positive interval support of the same fixed degree.

Because `H=(F+G)/2`, its support is the same positive interval, and at
every ordered minor

`det K_H=(det K_F+det K_G+Mix(F,G))/4>=0`.

At every supported defect, the two diagonal terms are strictly positive,
so H is strict there. The identical argument applies to yH. Thus both
H support and H TP2 are redundant under MP_sharp; they are derived
conclusions, not silently retained assumptions.

With delta=(r-s)/2, F=H+delta b1 and G=H-delta b1. Exact polarization gives

`Mix(F,G)=2[det K_H-delta^2 det K_b1]`.

Consequently the sharp packet's third requirement is exactly

`det K_H >= ((r-s)^2/4) det K_b1`

for all ordered minors, and likewise for yH,yb1. If b1 has one sign,
`T_|b1|=T_b1`, so its signed and absolute reference descriptions agree.
The old one-sign-seed MP_2 implies this requirement: if a reference minor is nonnegative,
its uniform-4 bound suffices; if negative, the separately assumed H cone
suffices. MP_sharp therefore weakens the old sufficient packet correctly.

## 4. Finite character cone and exact scalar copositivity

The independently checked universal theorem in
`network_relative_character.md` identifies all ordered relative minor
inequalities with character nonnegativity of one finite tensor. Set

`T_f=Phi(f(xi)f(zeta))`,
`J(f,g)=T_(f+g)-T_f-T_g`.

The exact mixed gate is

`T_H-delta^2 T_b1 >=_character 0`,

and separately the same expression with yH,yb1. Its necessity uses
rows (0,1) and ALL column pairs, not just adjacent columns. Sufficiency
uses the one- or two-character-positive factors R(C_i,C_j). The
central column is normalized without a duplicate factor two.

Put u=(r+s)/2, w=delta^2. The exact parameter domain is
`|u|<=2, 0<=w<=W=(2-|u|)^2`. With
`A_u=(T-u)L_u`, H=A_u-wb0, the tensor is

`B(u,w)=T_Au-w[J(A_u,b0)+T_b1]+w^2 T_b0`.

Fix u and a character index, and write its scalar coefficient as
`E(w)=a+bw+cw^2`. For W>0 define

`m=a+bW/2`, `z=E(W)`.

Then E is nonnegative throughout [0,W] exactly when the 2x2 matrix
`[[a,m],[m,z]]` is copositive, equivalently

`a>=0, z>=0, and (m>=0 or m^2<=a z)`.

This follows by writing
`E(Wt)=a(1-t)^2+2m t(1-t)+z t^2` and homogenizing over nonnegative
coordinates. The case W=0 requires only a>=0, already supplied by
the diagonal cone. If c<=0, endpoint nonnegativity alone suffices by
concavity. Positive semidefiniteness would be an unnecessary stronger
condition when m>sqrt(a z).

This is an exact finite reformulation of the existing mixed gate; it
is not its child-preservation proof. Nor does pairwise positivity of
arbitrary positive pencils suffice for mixtures of three or more
terms. The resolvent argument below specifically uses mixed-minor
nonnegativity, not merely two-term cone membership.

## 5. Origin theorem and the retained register/M implications

Let U_-1=0, U_0=1, U_N=T U_(N-1)-U_(N-2), and
`q_N=b0 U_N+b1 U_(N-1)`. Under MP_sharp, every q_N with N>=1 is
strict in both raw and y modes.

Indeed, the N-vertex unit-off-diagonal path has simple eigenvalues
lambda_j in [-2,2], and its endpoint resolvent has positive weights
w_j summing to one:

`U_(N-1)/U_N=sum_j w_j/(T-lambda_j)`.

Hence

`q_N=sum_j w_j L_(lambda_j) product_(k!=j)(T-lambda_k)`.

Each summand is strict by Section 2, has positive interval support,
and has degree p+Nd. For distinct summands, removing common shifted
factors leaves the exact F_rs,G_rs pair. Its mixed tensor is positive
by MP_sharp; restoring common cone factors preserves that sign.
Expanding the tensor of the positive weighted sum gives positive
diagonal tensors plus nonnegative mixed tensors. The supported
diagonal defects remain strictly positive at every index, including
the terminal one, because all summands have the same degree. Replace
each L by yL to prove the smoothed theorem independently. N=0 is not
asserted and no seed cone is needed.

The same proof covers q_N-rho q_(N-1) for N>=1, |rho|<=1, using a
path with terminal diagonal rho. Its Gershgorin bounds remain within
[-2,2], and deleting the first vertex gives the Robin cofactor needed
for the positive endpoint resolvent. This supplies strict Q for
ordinary certified origins at rho=1. The endpoint-1 origin is instead
covered by the audited yW_N theorem, N>=2.

Therefore replacing every old origin packet by MP_sharp retains the
already proved register conclusions and exact BOTH-child register
identities. In particular the smaller previous index is N_X-1>=1,
so CURRENT K_G is certified. CURRENT M=T+1 is supplied by the trace
gate at r=-1. The current paired sharp packets thus retain the old
P_REG=>P_Q=>target implication when the LR and strict proxy components
are kept. The exact augmented root clause is also unchanged.

## 6. ROOT, BOTH, TARGET: exact status

| Obligation | Status |
| --- | --- |
| ROOT current paired MP_sharp | Proved; the independently replayed uniform-4 base certificates also certify the sharp arrays directly. |
| ROOT to BOTH first children, current paired packets | Proved on the entire parameter square in both orientations and both modes. |
| Algebra, LR companions, origin-register BOTH transport | Retained proved implications; exact mixed gate suffices for every origin theorem used. |
| Strict K_Q at both child records | Retained Robin-origin proof plus the audited endpoint-1 yW_N boundary. |
| Arbitrary regular parent to BOTH full changed-center paired MP_sharp | OPEN. Child traces, all L parameters, and correlated mixed tensors have not been shown to follow. |
| Arbitrary regular parent to BOTH strict proxy | OPEN. Strict delta(Q) does not sign its mixed comparison with V. |
| IMPLIES TARGET | Retained for regular states through the old P_Q reduction, and for the exact initial root clause. |

The new Robin r=-1 reversed single-block subgate is a useful proved
part of changed-center transport; it does not remove the full packet
obligation. The two remaining analytic obligations are A_sharp (both
new paired packets) and the regular-edge strict proxy. Full-tree
strict Local TP2 remains OPEN.

Audited network source SHA-256:
`0ed6f97744bb78e810438285c6cd7e1520197940b6e5c57881c9692f29fa617d`.
