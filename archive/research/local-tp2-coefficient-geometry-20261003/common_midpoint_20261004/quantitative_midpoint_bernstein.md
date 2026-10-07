# Exact continuum certificates for the root and both first-child paired midpoint packets

Status: the original radius-2 paired midpoint packets hold at the root and at
each of its two actual children, in BOTH seed orientations and independently
in the raw and y-smoothed modes. The proof uses finite exact tensor-Bernstein
certificates for the entire parameter square and the audited all-index
character theorem. This closes the NEW paired-packet obligation on both
root edges in the frozen expanded predicate. It does not prove changed-center
packet transport from an arbitrary regular parent, or regular-edge proxy
transport. Full-tree strict Local TP2 remains OPEN.

## 1. Exact canonical inputs and the finite theorem

Put y=x+1. The normalized canonical data are

    X=1+ya, t=2x+3+3y²a, k=X(3X−2),
    g=(t−2)e+k+r, s=tg−r,
    C=1+y(a+e+g), T=3yC−x, c=e+g+s.

The Fricke correlation retained by the verifier is

    rg=(t−2)e²+2ke+3aX².

The root is (a,e,r)=(0,1,1). Its short child is
(a,e+g,g); its long child is (a+e,g,e+g). These are the two
degree-ordered child labels, not fixed left/right Farey directions.
The three resulting paired tuples are as follows; coefficient vectors
below are ordinary powers of x, starting at the constant coefficient.

| State | T | c | e |
| --- | --- | --- | --- |
| root | (15,32,24,6) | (12,14,4) | (1) |
| first short child | (39,116,132,66,12) | (33,64,40,8) | (4,2) |
| first long child | (87,308,444,324,120,18) | (167,500,620,398,132,18) | (3,2) |

For each row the two packet orientations are (T,b0,b1)=(T,c,e)
and (T,e,c). For r,s in [−2,2], define

    L_r=b0(T−r)+b1,
    H_rs=b0(T−r)(T−s)+b1(T−(r+s)/2).

**Finite-base theorem.** At every one of these three canonical states
and in each seed orientation:

1. all shifted traces T−r have positive interval support and folded TP2;
2. L_r and yL_r have positive interval support and strictly positive
   supported folded defects, including the central and terminal defects;
3. H_rs and yH_rs have positive interval support and folded TP2, and
   in fact have strictly positive supported folded defects;
4. every ordered folded minor satisfies

       det K_Hrs >= 4 det K_b1,
       det K_(yHrs) >= 4 det K_(yb1);

5. independently, every ordered folded minor also satisfies the sharp
   midpoint inequalities with coefficient (r−s)²/4 in place of 4.

Thus both original MP_2 packets are proved at BOTH actual root children.
The reference is b1, which is positive here, so |b1|=b1. The pure H
cones are certified separately; a relative inequality against a
potentially negative reference minor is not used to infer their signs.

## 2. The exact finite all-index reduction

Write h=H(f) for the reflected, zero-extended Fourier half-row of f.
Let

    T_f=Phi(f(ξ)f(ζ))=R(f,xf),
    J(f,g)=T_(f+g)−T_f−T_g.

The tensor coefficients are in the character basis
chi_a(U)chi_b(V). If 0<=i<j and
q=H(xf), the coefficient h_i q_j−h_j q_i is put at

    (a,b)=(i+j−1,j−i−1),

and also at (b,a) when i>0. There is only one copy at i=0.
The finite arrays in this note are computed by this complete column-pair
formula, through the terminal column deg(f)+1.

The independently audited theorem in
`network_relative_character.md` gives, for every real gamma,

    T_f−gamma T_b >=character 0
       iff det K_f[I,J]>=gamma det K_b[I,J]
            for EVERY ordered row pair I and column pair J.

Its proof covers unbounded folded-kernel indices: every row i is
H(C_i f), and its two-row Bezoutian is
T_f R(C_i,C_j), where R(C_i,C_j) is one or two positive
characters. The first two rows give the converse. Equal-parity
character indices and symmetry exhaust all coefficients, including
the central diagonal normalization. We use this theorem rather than
enumerating a finite kernel-index band.

In particular the pure T_f character cone proves all folded minors of
f nonnegative. The character coefficient (2n,0) of T_f is precisely

    delta_n(h)=h_n²−h_(n−1)h_(n+1)−h_(n+1)²+h_n h_(n+2),

including reflection at n=0 and zero extension at the terminal index.
These supported coefficients are checked strictly positive separately.

## 3. Nine power coefficients and nine Bernstein coefficients

Set p=T−2, alpha=2−r, beta=2−s, so alpha,beta are in [0,4].
Define

    L2=b0p+b1, U=pL2,
    A=b0p+b1/2, B=b0.

The exact ordinary polynomial identity is

    H_rs=U+(alpha+beta)A+alpha beta B.

Its sharp relative tensor

    E(alpha,beta)=T_Hrs−(alpha−beta)² T_b1/4

has bidegree (2,2), with power arrays

| Power index | Character array |
| --- | --- |
| (0,0) | T_U |
| (1,0), (0,1) | J(U,A) |
| (2,0), (0,2) | T_A−T_b1/4 |
| (1,1) | J(U,B)+2T_A+T_b1/2 |
| (2,1), (1,2) | J(A,B) |
| (2,2) | T_B |

For the pure H tensor, remove the reference terms:
the (2,0),(0,2) arrays become T_A, and (1,1) becomes
J(U,B)+2T_A. For the original uniform-4 relative tensor,
subtract 4T_b1 from the pure (0,0) array.

For an array-valued polynomial E=sum c_ij alpha^i beta^j,
its tensor-Bernstein arrays on this exact square are

    B_kl = sum_(i<=k,j<=l)
             c_ij 4^(i+j)
             binom(k,i)/binom(2,i)
             binom(l,j)/binom(2,j),   0<=k,l<=2.

Indeed alpha=4u, beta=4v gives
E(4u,4v)=sum B_kl binom(2,k)u^k(1−u)^(2−k)
                         binom(2,l)v^l(1−v)^(2−l).
These basis functions are nonnegative and sum to one on [0,1]².
Thus nonnegative character coefficients in every B_kl prove the
corresponding all-index inequality at every real parameter pair.
Strict positivity of the supported (2n,0) coefficient of every
B_kl proves a strict supported defect even at the boundary.
No finite parameter sampling is used.

There is an exact correlated corner interpretation. Put
V=H_(−2,2)=H_(2,−2), W=H_(−2,−2), U=H_(2,2), E=T_b1.
The nine SHARP Bernstein arrays are

    B00=T_U; B10=B01=J(U,V)/2;
    B20=B02=T_V−4E;
    B11=J(U,W)/4+T_V/2+2E;
    B21=B12=J(V,W)/2; B22=T_W.

For the pure H array remove the E terms; for the uniform-4 array
subtract 4E from every pure-H Bernstein array. These identities
offer a sufficient reduction to three corner cones and three
correlated corner-mixed arrays. They do not say that corner cone
membership alone proves the continuum inequality. Nonnegative
Bernstein coefficients are sufficient; they are not necessary for
an arbitrary nonnegative quadratic on an interval or square.
They follow by V=U+4A and W=U+8A+16B and quadratic polarization;
the reproducer additionally verifies them in the free symbol space
spanned by T_U,T_A,T_B,J(U,A),J(U,B),J(A,B),T_b1. Thus this
identity check is universal, independently of the three finite states.

For smoothing, replace U,A,B,b1 by yU,yA,yB,yb1 BEFORE
forming the quadratic and polarized tensors. The full calculation is
independent of the raw one; y is not assumed to preserve the cone.

## 4. Shifted traces, L blocks, and support boundaries

For a trace or an L block write r=2−4u, 0<=u<=1, and
P_r=P0+uP1. For the trace P0=T−2,P1=4; for L,
P0=L2,P1=4b0. Its three interval-Bernstein tensor arrays are

    T_P0,
    T_P0+J(P0,P1)/2,
    T_P0+J(P0,P1)+T_P1.

The smoothed L calculation uses yP0,yP1. Complete character arrays,
not only the adjacent defects, are recorded. Every supported defect
array is strictly positive. Every character array is nonnegative.
The three unsmoothed trace certificates likewise have all character
coefficients nonnegative and all supported defects strictly positive.

Support and degree are proved separately. At the root, short child,
and long child, T−2 has constant 13,37,85 respectively, and every
ordinary coefficient is positive. Each seed is also a dense ordinary
positive polynomial. Consequently T−r has the same positive interval
support for all r in [−2,2]. L2 and U are dense and ordinary positive.
The nonnegative-alpha,beta expansion in Section 3, and
L_r=L2+alpha b0, show that every raw block has the same fixed dense
positive support as its corner block. Multiplication by y preserves
this ordinary positive support, without invoking any folded-cone
claim. Fourier half-rows are therefore positive on every supported
index and zero beyond their stated degrees.

The seed degree checks are explicit:

| State/orientation | deg T | deg b0 | deg b1 | deg L | deg H |
| --- | ---: | ---: | ---: | ---: | ---: |
| root forward | 3 | 2 | 0 | 5 | 8 |
| root reverse | 3 | 0 | 2 | 3 | 6 |
| first short forward | 4 | 3 | 1 | 7 | 11 |
| first short reverse | 4 | 1 | 3 | 5 | 9 |
| first long forward | 5 | 5 | 1 | 10 | 15 |
| first long reverse | 5 | 1 | 5 | 6 | 11 |

In every row deg b1<deg b0+deg T. The effective smoothed seeds
yb0,yb1 both gain one degree, preserving this strict inequality,
and the smoothed L,H degrees each gain one. In particular the
reference has smaller degree than L, and both supported terminal
defects are checked rather than inferred from an interior division.
The verifier asserts all these positivity and degree statements.

## 5. Complete exact certificate results

The following table reports all-character Bernstein slots for EACH of
the sharp relative, uniform-4 relative, and pure H tensor arrays.
Zeros are permitted in this all-character certificate. The two
reported strict minima are over all supported H or L defects and all
parameter-Bernstein indices.

| State/orientation/mode | deg H | slots per tensor | minimum supported H defect | minimum supported L defect |
| --- | ---: | ---: | ---: | ---: |
| root forward raw | 8 | 729 | 20736 | 576 |
| root forward y | 9 | 900 | 20736 | 576 |
| root reverse raw | 6 | 441 | 1296 | 36 |
| root reverse y | 7 | 576 | 1296 | 36 |
| first short forward raw | 11 | 1296 | 1327104 | 9216 |
| first short forward y | 12 | 1521 | 1327104 | 9216 |
| first short reverse raw | 9 | 900 | 82944 | 576 |
| first short reverse y | 10 | 1089 | 82944 | 576 |
| first long forward raw | 15 | 2304 | 34012224 | 104976 |
| first long forward y | 16 | 2601 | 34012224 | 104976 |
| first long reverse raw | 11 | 1296 | 419904 | 1296 |
| first long reverse y | 12 | 1521 | 419904 | 1296 |

All 15,174 slots in each of the three tensor families are nonnegative.
All 1,242 supported H-defect and 270 supported L-defect Bernstein
slots are strictly positive. The 45 supported trace-defect slots
are strictly positive, with minimum 36,144,324 at the three states.
The complete trace/L character certificates also pass.

`quantitative_midpoint_bernstein.py` uses standard Python only,
exact integers and Fractions, no imports from parent arithmetic. It
constructs the actual states, checks the Fricke identity, and writes
the concise `quantitative_midpoint_bernstein_results.json` plus
`quantitative_midpoint_bernstein_full.json.gz`. The latter contains
every sparse character-Bernstein array and every supported strict
defect array; omitted sparse entries are exactly zero. The summary
retains every canonical state polynomial, support/degree assertions,
counts, minima, verdicts, and SHA-256 hashes of both the uncompressed
payload and deterministic gzip archive (mtime=0). The archive is a
complete finite proof certificate, not a sampled path log.

## 6. An actual obstruction to sourcewise power positivity

The stronger demand that every POWER coefficient in Section 3 be
character-nonnegative already fails at the root, reversed smoothed
orientation. There b0=e=1, so yB=y and H(y)=(1,1).
The alpha² beta² coefficient at the central character is

    delta_0(H(y))=−1.

The sharp reference subtraction has total parameter degree two and
cannot change this degree-four coefficient. This is an actual-root
obstruction to the power-coefficient proof strategy, independently
confirmed by the falsification lane. It is not a
counterexample to the sharp inequality or original MP_2: every
Bernstein certificate above passes. Positive coefficients in the
ordinary canonical variables do not justify arbitrary cone sums.

## 7. Scope of closure

| Obligation | Result of this note |
| --- | --- |
| ROOT paired MP_2 | Proved directly on the entire parameter square, raw+y and both orientations. |
| ROOT → short child paired MP_2 | Proved, including all kernel indices, positive support and terminal defects. |
| ROOT → long child paired MP_2 | Proved with the same complete obligations. |
| Arbitrary regular parent → short/long child new-center MP_2 | OPEN; the finite-base theorem supplies no induction for this changed tuple. |
| Regular-edge strict proxy transport | OPEN; not asserted by the relative-minor certificate. |
| IMPLIES TARGET | Through the prior expanded-predicate reduction once its remaining regular-state closure gates are proved. No all-tree theorem follows from this note alone. |

In combination with the previously proved first-level LR/proxy
initialization and exact origin-register transport, the two root
children now satisfy the expanded regular predicate. Further
changed-center packet transport still requires a correlated algebraic
inequality for arbitrary regular states; passing finite bases does
not supply it.
