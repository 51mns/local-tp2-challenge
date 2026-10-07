# Signed seeds: a global algebraic lemma and a finite ray certificate

Primary level: **PROOF_CANDIDATE**. The derivations below and two arithmetic implementations have been checked in this session. This is not a new external review, Lean proof, or canonical promotion. The full canonical-tree Local TP2 assertion remains open.

Repository baseline: `51mns/AIMath`, research commit `3395b151e8882a0657c2a1ee417d56022acf4593`; accepted main `c8e61e0e398f540bc8c5de79663398d689f37473`. Owned path for this campaign: `research/local-tp2-openai-math-20261007/signed_seed_20261007/`.

## 1. Scope and efficiency decision

The prior extension criterion requires a nonnegative second seed B. That hypothesis is not preserved even by a single forward step: the exact seed update along a fixed-boundary ray is `(A,B) -> (t A+B,-A)`. Repeated enumeration of positive-B prefixes therefore cannot by itself give an arbitrary-turn induction.

We remove that sign restriction, without replacing it by the desired TP2 inequality. The signed coefficient is retained inside each spectral summand. The reference for the determinant estimate is Q=+B or -B with a nonnegative half-row. A reference-cone assumption is unnecessary. Only the actual two-parameter midpoint is used, not an independent third parameter.

This campaign proves a global seed-positivity lemma, gives a signed-seed sufficient criterion with no unbounded ray length in its hypotheses, and supplies complete exact certificates for `LRL R^N` and `RLR L^N`, for every N>=0. It does NOT show the whole criterion is preserved under both next turns. In particular it does not prove all four-run words or the full tree.

## 2. An all-tree algebraic lemma, proved without finite enumeration

Use y=x+1, p=x+2. The root is `(1,2x^2+6x+5,p)`. The two original mutations are

    U=3yXC-x(X+C)-Y,    V=3yYC-x(Y+C)-X.

Every canonical polynomial can be written `G=1+y g` with `g` a polynomial having nonnegative integer x-coefficients. At a state write the two endpoints and center as

    X=1+y u,    Y=1+y v,    C=1+y w.

The quotient-coordinate mutation at endpoint u is

    w_new = 1+(2x+3)(u+w)+3y^2 u w-v
          = t_u w+c_u-v,
    t_u=2x+3+3y^2 u,    c_u=1+(2x+3)u.

At the root `(u,w,v)=(0,2p,1)`, all entries and both differences w-u,w-v have nonnegative coefficients. If these properties hold at a parent, then

    w_new-w = (t_u-2)w+(w-v)+c_u

has nonnegative coefficients, because `t_u-2=2x+1+3y^2u`. The new center is coefficientwise above both new endpoints. The right mutation has the identical argument with u,v exchanged. This proves the assertion and both gap inequalities by induction on the length of an arbitrary word. No cone or Fourier order has been used.

For either chosen continuation direction, label its fixed endpoint X and the other endpoint Y. Define

    t=3yX-x,
    T=tY-xX-C,
    A=(C-Y)/y,
    B=(T-Y)/y.

Here T is the inverse center. At the root T=1. At every nonroot, applying the inverse mutation reconstructs an endpoint of the previous state. Consequently T=1+y z with nonnegative quotient z, and w>=z coefficientwise: the current center dominates the preceding center, which dominates that endpoint. Therefore

    A-B=(C-T)/y=w-z >= 0.

More importantly the sum has the subtraction-free identity

    A+B = 1+(2x+3)u+(2x+1)v+3(x+1)^2 u v >= 0.       (S)

To prove (S), expand `(t-2)Y-xX=y(A+B)` using X=1+yu and Y=1+yv.

The polynomial B is sign-uniform in ordinary x-coefficients, with zero allowed. For a nonroot, T and Y are either an endpoint and the center of the preceding state, or the two preceding endpoints. A center dominates either endpoint. The difference of the two endpoints is sign-uniform as well: initially v-u=1, and after any mutation one endpoint is the old center, which dominates the other endpoint. At the root B is -1 for left continuation and 0 for right continuation. This proves sign-uniformity at every node.

Combining the sign statement with A+B>=0 and A-B>=0 gives

    Q=|B| is a polynomial,    0<=Q<=A                    (G)

in ordinary coefficients, hence also in symmetric Laurent coefficients. This holds for **all canonical prefixes and both choices of continuation direction**.

Finally, when the fixed endpoint is kept and one forward move is made,

    A_next=t A+B,    B_next=-A.                          (U)

Indeed yA is the current increment and yB is the negative of the previous increment; the increments satisfy the homogeneous second-order recurrence. Formulas (G) and (U) explain why negative B is natural, not a counterexample to Local TP2.

The regression tests of (S), (G), and (U) check implementation conventions only. Their all-tree validity rests on the induction and algebra above.

## 3. Folded kernels used in the extension argument

For a polynomial F define `h_F(n)=[q^n]F(q+q^-1)`, reflecting negative n and padding with zero after the degree. Put

    delta_n(h)=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2).

A positive interval half-row is called strict cone when every supported delta is positive; weak cone allows zero delta. Its multiplication kernel is

    K_h(0,j)=h_j;
    K_h(i,0)=2h_i  (i>0);
    K_h(i,j)=h_|i-j|+h_(i+j)  (i,j>0).

We use the finite folded-kernel criterion: K_h is TP2 iff all delta_n>=0. Also `H(FG)=H(F)K_G`, `K_(FG)=K_F K_G`. The criterion, common-factor order preservation, strict product closure, and support-boundary proof are recorded at the pinned baseline in

* `research/local-tp2-coefficient-geometry-20261003/continuation_kernel/folded_kernel_theorem.md`;
* `research/local-tp2-coefficient-geometry-20261003/mixed_kernel_all_minor_strength.md`.

The elementary reason for the criterion is worth recording. Write `Delta_n=h_n^2-h_(n-1)h_(n+1)`. A first-row adjacent kernel minor is `Delta_n-Delta_(n+1)=delta_n`. For an interior adjacent cell let a=|j-i| and b=i+j. Where the divisions are supported its determinant is

    Delta_a-Delta_(b+1)+h_a h_(b+1)(t_(b+1)-t_a),
    t_n=(h_(n-1)+h_(n+1))/h_n.

The identity `h_n h_(n+1)(t_(n+1)-t_n)=delta_n` makes this nonnegative. Boundary cells are evaluated directly without division. Positive support is exactly the band |i-j|<=degree, so adjacent cross-ratios telescope to every larger rectangle. Products and preservation of likelihood-ratio order then follow by Cauchy--Binet.

We also use the quantitative consequence: if `delta_n(H)>=lambda h_H(n)` throughout support, then every ordered minor with positive diagonal entries satisfies

    det K_H[(i,j),(a,b)] >= lambda K_H(i,a).             (K)

One proof first derives the adjacent bound from the same formula, then telescopes rectangle cross-ratios and retains the bottom-right cell. If an off-diagonal corner is zero, the determinant is the diagonal product and every positive kernel entry is at least lambda. This also handles the boundaries.

If Q has any nonnegative half-row, M=max h_Q, H>=Q coefficientwise, and `delta_n(H)>=8M h_H(n)`, equation (K) gives

    det K_H[I,J] >= 4 det K_Q[I,J]                     (R)

for every ordered pair I,J. Indeed positive Q minors are at most their diagonal product, with the lower diagonal entry at most 2M. Nonpositive Q minors need only TP2 of K_H. **Q need not belong to the cone.** If B=+Q or -Q, the two-by-two determinants of K_B equal those of K_Q.

## 4. A signed-seed finite criterion

The following are sufficient conditions, not assertions that they hold at every canonical prefix. They are exactly the conditions certified in the accompanying programs (some harmless fixed-row positivity checks are stronger than needed).

Take fixed canonical data X,C_0,Y and t,A,B as in section 2, in either continuation direction. Let Q=+B or -B have a nonnegative half-row, Q<=A. Assume the canonical degree identities

    deg X=a, deg Y=b, deg t=a+1=h,
    deg C_0=a+b+1, deg A=a+b, deg B<deg A+h,

with positive leading coefficients. All fixed quantities that are used as positive rows below must have positive interval support.

Define

    P=pX,        M_0=3yY-x+1,
    J=y(t-2),    V=3y^2P,       K=P M_0,
    beta=y(A+B), E_1=C_0-X,
    q_0=yA,      q_1=y(tA+B).

Let d=deg J=a+2, e=deg K=a+b+2, m=deg M_0=b+1.

### 4.1 Cone and mixed-kernel conditions

A and yA are strict cone. For every r,s in [-2,2], put

    f_r=t-r,
    L_r=A(t-r)+B,
    H_rs=A(t-r)(t-s)+B(t-(r+s)/2).

Require positive interval support and strict cone membership of f_r,L_r,yL_r. Require, for both (H_rs,Q) and (yH_rs,yQ),

    F>=reference coefficientwise,
    delta_n(F)>=8 max(H(reference)) H(F)_n.

When the reference is zero require strict delta explicitly. The supplied certificates actually have strictly positive margins also for the displayed strength inequalities. By (R), both required all-minor comparisons follow on the entire infinite kernels.

### 4.2 Mass and low-band templates

Assume tau=t(2)>=6 and, on r in [-2,2],

    delta_0(f_r)>=2 f_r(2).

For every n=0,...,e choose alpha_n>0 with

    det K_(L_r)[(i_n,i_n+1),(n,n+1)] >= alpha_n L_r(2),
    i_n=min(n,d).

For every n=0,...,m+1 choose beta_n>0 with

    delta_n(y^2 L_r)>=beta_n L_r(2).

These are finitely many inequalities in a single compact interval. The programs certify them using all Bernstein coefficients, not a sampling inference.

### 4.3 Four initial orders and two correction budgets

Require the four likelihood-ratio orders

    q_0 <=lr q_1,   beta <=lr q_1,
    P <=lr E_1,     P <=lr q_1.

With positive interval rows it suffices to check their finite adjacent minors through the smaller support. Also require

    w_j=W_j(J,V)>0  (j=0,...,d).

Write `m_j=H(M_0)_j`, `nu_n=m_(n-1)+3m_(n+1)` with reflection. Set `Z_1=A(t+1)+B`. Require the strictly positive finite budgets

    (w_(i_n) alpha_n)/2 > J(2) H(K)_n                  (D1)

for n=0,...,e, and

    9 beta_n/2 > 27 nu_n + max(-delta_n(M_0),0)/Z_1(2) (D2)

for n=0,...,m+1.

**Theorem.** These hypotheses imply the original strict Local TP2 at every state formed by appending N copies of the selected direction, for every N>=1. The prefix N=0 may be checked directly, with its own actual degree orientation.

## 5. Proof of the signed extension

### 5.1 Exact identification with the original ray

Let u_-1=0,u_0=1,u_1(z)=z,u_(j+1)=zu_j-u_(j-1), and R_N=sum_(j=0)^N u_j, R_-1=0. Evaluate all at t and define

    Z_N=A R_N+B R_(N-1),
    q_N=y(Au_N+Bu_(N-1)),
    C_N=Y+y Z_N.

Then C_-1=Y, C_-2=T, and direct substitution gives

    C_(N+1)=tC_N-C_(N-1)-xX,
    q_N=C_N-C_(N-1),   q_(N+1)=tq_N-q_(N-1).

For N>=1 the fixed endpoint X has lower degree than C_(N-1), so the actual degree-oriented target is

    S_N=q_(N+1),  E_N=C_(N-1)-X,
    M_N=M_0+3y^2 Z_N,  D_N=E_N M_N.

Also

    P M_N=V Z_N+K,
    S_N=JZ_N+q_N+beta,
    E_N=E_1+sum_(j=1)^(N-1) q_j.                       (I)

No sign of B was assumed in these identities.

### 5.2 Signed B inside a positive spectral mixture

For two spectral roots r,s set F=L_r(t-s), G=L_s(t-r). Their average is H_rs and F-G=(r-s)B. The coefficient of uv in the two-by-two determinant of uK_F+vK_G is exactly

    2 det K_(H_rs) - ((r-s)^2/2) det K_B >=0.          (M)

It follows from (R), det K_B=det K_Q, and |r-s|<=4. If det K_B<=0 it follows already from nonnegativity of det K_H. The same statement holds after multiplication by y by the certified smoothed midpoint. This identity is valid for signed B: no positive-mixture theorem is being applied to A and B separately.

The u_N and v_N=u_N+u_(N-1) families are characteristic polynomials of path Jacobi matrices with unit off-diagonals and, for v_N, one endpoint diagonal -1. Their spectra lie in [-2,2] (the absolute row-sum bound suffices); their eigenvalues are simple and endpoint eigenvector coordinates nonzero by the tridiagonal recurrence. The endpoint resolvent therefore gives

    p_(N-1)(z)/p_N(z)=sum_i lambda_i/(z-r_i),
    lambda_i>0, sum_i lambda_i=1.

Thus `A p_N(t)+B p_(N-1)(t)` is a positive mixture of `L_(r_i)` times the other shifted trace factors, even when B<0. Every summand is positive by the certified L_r. Its individual kernel is strict; pairwise mixed determinants are nonnegative by (M) and Cauchy--Binet with common cone factors.

The identities

    R_(2j)=u_j v_j,       R_(2j+1)=u_j v_(j+1),
    Z_(2j)=v_j(Au_j+Bu_(j-1)),
    Z_(2j+1)=u_j(Av_(j+1)+Bv_j)

give, for N>=1,

    Z_N=sum_i lambda_i Z_i,
    Z_i=L_(r_i) product_(j!=i)(t-r_j),

with exactly N-1 propagators, between one and N active positive weights, and total weight one. This proves strict cone membership of Z_N and q_N, raw and smoothed as needed. The weak-cone factor y^2 has row (3,2,1) and deltas (4,0,1); Cauchy--Binet using indices (0,1) or (2,3) shows y^2 Z_N is strict through its entire support.

### 5.3 Uniform mass comparison: the repair needed for signed B

Put A_*=A(2), B_*=B(2). By Q<=A, |B_*|<=A_*. Every active summand satisfies

    Z_i(2)/R_N(tau)=A_*+B_*/(tau-r_i).

Since tau>=6, this lies between 3A_*/4 and 5A_*/4. Its ratio to the weighted average is at least 3/5, so the conservative bound

    Z_i(2)>=Z_N(2)/2

holds for either sign of B. This replaces the positive-B endpoint-ratio argument; using that argument without repair would be invalid.

Retain the same adjacent column pair after each propagator. Each principal propagator minor is at least delta_0(f_r)>=2f_r(2). Retaining the diagonal terms of the spectral mixture, with their **squared** weights, yields

    det K_(Z_N)[(i_n,i_n+1),(n,n+1)]
      >= alpha_n 2^(N-1) sum_i lambda_i^2 Z_i(2)
      >= (alpha_n/2) (2^(N-1)/N) Z_N(2)
      >= alpha_n Z_N(2)/2.

Here sum_i lambda_i^2>=1/N and 2^(N-1)>=N. The same argument from y^2L_r gives

    delta_n(y^2 Z_N)>=beta_n Z_N(2)/2.                (B)

Because q_j is positive, Z_N increases in mass for N>=1 even for negative B. Thus Z_N(2)>=Z_1(2). This replaces the other use of B>=0 in the old criterion.

### 5.4 Multiplier and strict proxy comparison

Expanding delta(M_0+3y^2Z_N) and bounding only the negative cross terms, using each coefficient of y^2Z_N at most 9Z_N(2), gives

    delta_n(M_N)
      >= (9beta_n/2-27nu_n)Z_N(2)+delta_n(M_0).

For n<=m+1 this is strictly positive by (D2) and the minimum mass Z_1(2). For n>=m+2 all correction terms vanish; strictness follows from y^2Z_N. Thus the actual M_N is strict cone, not merely its dominant part.

Cauchy--Binet on the two rows J,V and K_(Z_N), retaining the fixed pair i_n,i_n+1, and (B) give

    W_n(JZ_N,VZ_N)>=w_(i_n) alpha_n Z_N(2)/2.

The adverse correction is bounded by

    W_n(JZ_N,K)>=-J(2)Z_N(2)H(K)_n.

Budget (D1) proves strict positivity through n=e. Above e, K has vanished; retain the pair d,d+1, whose fixed minor is w_d>0. The corresponding kernel minor is positive whenever n-d is within the support of Z_N. This covers all remaining n through deg(JZ_N), including the terminal one. Hence

    JZ_N <lr VZ_N+K=P M_N.                            (P)

### 5.5 Return to the original target

For any q_N with a cone kernel, nonnegativity of t gives q_N<=lr tq_N. The exact recurrence yields at any ordered columns

    W(q_N,q_(N+1))=W(q_N,tq_N)+W(q_(N-1),q_N).

The initial q_0<=lr q_1 therefore propagates. Using the other three initial comparisons and (I) gives

    P<=lr E_N,    S_N<=lr JZ_N.

These uses of addition keep one common comparison row fixed; they do not assume arbitrary sums preserve the cone. Multiplication by the now-proved cone kernel of M_N and (P) produce

    S_N <=lr JZ_N <lr P M_N <=lr E_N M_N=D_N.

Every intermediate supported entry is positive, so interior strictness survives transitivity. Finally

    deg S_N=2a+b+2+N(a+1),
    deg D_N=a+2b+2+2N(a+1),
    deg D_N-deg S_N=b+1+(N-1)(a+1)>0.

At the final supported index S_N has next entry zero and D_N has next entry positive. The original determinant there is a product of two positive entries. This proves the theorem for every N>=1, with no unbounded computation.

## 6. Two exact applications

`core.py` starts from the frozen root and applies the original polynomial mutations. `signed_gate.py` reconstructs all interval and midpoint inequalities via exact degree-two interpolation and Bernstein conversion. All defining expressions have degree at most two in each spectral variable, so the conversion is exact on the full interval or rectangle.

`verify_direct.py` imports neither author module nor expected certificate. It instead applies the mutations directly in the full Laurent ring, keeps negative exponents, expands the parameter polynomials symbolically after r=4u-2,s=4v-2, and converts monomials to Bernstein coefficients. A separate comparison after the runs checks every generated coefficient array.

The instances are:

| prefix | continuation | deg X,Y,A,B,t | certified coefficients and budget entries |
|---|---|---|---:|
| LRL | R | 6,3,9,2,7 | 1566 |
| RLR | L | 7,4,11,3,8 | 1821 |

Both have B<0. Every required interval/rectangle margin and fixed correction budget passes, and all 3387 entries match between the two constructions. Their prefix targets are checked directly. The conclusion is therefore strict original Local TP2 on

    LRL R^N and RLR L^N,  for every integer N>=0.

This is a proof with finite exact certificates, not observation up to a finite N. The programs also include finite recurrence/degree regressions and a negative control: a quadratic positive at all interpolation nodes but negative between them is correctly rejected by the full Bernstein test.

## 7. Remaining obligation and claim discipline

The global identities (S),(G),(U) do not imply a cone or likelihood-ratio order. What is still missing is a preservation theorem, under an arbitrary next turn, for the trace cone, the signed single/midpoint compatibility, the four initial orders, and quantitative correction budgets. The sufficient mass gate can also fail for small fixed endpoints even when the target holds, so it must not be promoted to a necessary characterization.

A four-run example is not a proof for arbitrary four-run lengths. Even a theorem for all four runs would not by itself give arbitrary numbers of runs. No percentage of completion, probability of success, or novelty is asserted. This work adds a concrete sign-handling mechanism and two certified infinite rays; it leaves the full-tree assertion open.
