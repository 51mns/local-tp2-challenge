# Independent spectral audit of proxy_character.md

**PASS with the qualifications already stated in the source.** The
all-N Robin weights, their squared-weight factor, the uniform
Cauchy--Binet lower bound, the closed diagonal formula, and the retained
mixed expansion are correct. The exact diagonal identity does not prove
arbitrary BOTH proxy preservation. This audit is independent analytical
derivation plus a replay of the existing exact verifier, not a new scan.

## 1. Weights and normalization, including N=1

Let `J_N` be the N-vertex unit-off-diagonal path with terminal diagonal
one. For `N>=2`, a sine eigenvector `u_k=sin(k theta)` satisfies the
last equation precisely when `sin((N+1)theta)=sin(N theta)`.
The N admissible angles are

    theta_j=(2j-1)pi/(2N+1), j=1,...,N.

Their squared vector norm is `(2N+1)/4`. Consequently the first-coordinate
weights are

    w_j=4sin^2(theta_j)/(2N+1)
       =(4-lambda_j^2)/(2N+1), lambda_j=2cos(theta_j).

For N=1 the sole angle is pi/3, lambda=1, and the weight formula gives
one. Thus the formulas need no separate weight normalization at N=1.

The moment computation avoids any trigonometric sum of fourth powers:

    sum_j w_j^2
       =e_1^T(4I-J_N^2)e_1/(2N+1)=3/(2N+1).

Here `(J_N^2)_11=1` for N>=2 because its first vertex has one unit edge,
and for N=1 because `J_1=[1]`. The factor `3/(2N+1)` is exact at every N.

## 2. Exact one- and two-resolvent polynomials

Write `p_N(z)=U_N(z/2)-U_(N-1)(z/2)` in standard Chebyshev notation,
and let `p_0=1`. The endpoint resolvent is `m(z)=p_(N-1)(z)/p_N(z)`.
Set `W=4I-J_N^2`. The polynomial identity

    (4-lambda^2)/(z-lambda)
       =(4-z^2)/(z-lambda)+z+lambda

gives, using `e_1^T J_N e_1=0` for N>=2,

    e_1^T W(zI-J_N)^(-1)e_1
       =(4-z^2)m(z)+z=h_N(z)/p_N(z),
    h_N=4p_(N-1)-z p_(N-2).

The last equality follows immediately from the continuant recurrence
`p_N=z p_(N-1)-p_(N-2)`. At N=1 the first moment is one instead of zero:

    (4-z^2)/(z-1)+z+1=3/(z-1).

Thus `h_1=3` is indispensable and the source handles it correctly.

Because W commutes with the two resolvents, their difference identity gives

    p_N(a)p_N(b) e_1^T(aI-J_N)^(-1)W(bI-J_N)^(-1)e_1
      =[h_N(a)p_N(b)-p_N(a)h_N(b)]/(b-a)=K_N(a,b).

The quotient is a polynomial and extends to the diagonal. It is a divided
difference in the **spectral variables** a,b. After setting
`a=t(xi),b=t(zeta)`, its denominator is `t(zeta)-t(xi)`; substituting the
ordinary Bezoutian denominator `zeta-xi` would insert an unwanted trace
divided-difference factor. The source defines the correct K_N and does
not make that substitution.

For

    A_j=y[b0(t-lambda_j)+b1]p_N(t)/(t-lambda_j),

expand each factor as `y[b0 p_N+b1 p_N/(t-lambda_j)]`.
The b0*b0 coefficient uses `sum w_j^2=3/(2N+1)`; the two cross terms
use `h_N/p_N`; and the b1*b1 term uses K_N. This derives source
equation (12), with every y factor and the overall `1/(2N+1)` exactly
as printed. At N=1, K_1=3 and the expression is exactly T_Q.
At b1=0 every residue polynomial A_j is Q itself, giving
`D_N=3T_Q/(2N+1)` as asserted.

## 3. Cone and strictness scope of the quantitative bounds

Under the ordinary origin MP_sharp hypothesis, every A_j is strict in
the raw mode because the **smoothed** origin block yL is used and is
multiplied by weak shifted traces. Its degree is `deg b0+Nd+1`, which
is the same at every j. The strict-times-weak lemma applies at each stage
because the current strict degree is at least d.

The paired off-diagonal contribution is exactly

    J(A_i,A_j)=2T_Cij [T_(yH_ij)-((lambda_i-lambda_j)^2/4)T_(yb1)].

Hence `T_Q>=_char D_N` and source equation (13) are correct. This
uses the certified smoothed mixed packet, rather than multiplication by
a presumed cone T_y. The four additive terms in the closed formula for
D_N are not individually asserted to be cones; no seed-cone assumption
is silently reintroduced.

The trace minima mu_j in source equation (10) are indeed the minima
of the ordinary differences Delta_j for shifted traces. At j=0, the
minimum is at r=2 because positive support gives `h_0-r>0`; at j=1
it is at r=-2; higher indices do not depend on r. Weak folded TP2 plus
the positive terminal defect implies every Delta_j is strictly positive.

The backwards index selection in the uniform bound retains exactly one
nonnegative Cauchy--Binet term at every product. It keeps the intermediate
index at least d, so all reflected sum terms vanish at positive output
indices; at zero, the second minor is exactly `2(lc t)^2`. Its difference
index stays inside `[0,d]` at every step. Compactness gives positive
origin defect minima eta_j, and multiplication by the exact sum of
squared weights yields the stated lower bound `3 beta_n/(2N+1)`.

The endpoint-1 origin is correctly excluded from this ordinary-packet
quantitative theorem. Its separate Robin theorem remains necessary.

## 4. Target reduction and remaining limitations

The weaker comparison `Q<D` has the direct target proof `S<=Q<D`.
With positive dense support, adjacent comparisons propagate to every
ordered half-row pair, while `deg D>=deg Q+1=deg S+1` supplies the strict
terminal target. The old proxy implies this weaker gate through
`Pi<=D`, but the converse is not used.

I also read the actual LR companion proof in
`../common_closure_20261004/reduction_common.md` Section 3. After its
parent target `S<=D` is derived, its eight child comparisons use only
that target, the four parent LR companions and K_G. They do not consume
Pi or the old proxy elsewhere. Thus replacement by the direct Q<D gate
retains the stated LR subsystem implication.

The source correctly leaves BOTH preservation of Q<D, preservation of
the full changed-center paired packets, and the correlated quantitative
comparison against R(Q,V) open. Neither the positive weights nor the
ordinary numeric positive-semidefiniteness of the matrix W proves that
an unrelated source is character-nonnegative. Only the full packet
mixture proves the D_N character assertions used above.

## 5. Exact replay

I replayed `proxy_character_verify.py` through its `run()` function, with
no output-file mutation. It passed its existing exact sparse identities
and weighted adjugate identities for N=1,2,3,4. The independently
derived all-N identities above are the proof; those checks validate
implementation and normalization only.

The actual first-long coarse central bound is `134352/5`, its proposed
domination surplus is `-737848/5`, and the exact diagonal retention's
minimum surplus for that zero-b1 seed is `972/5`, matching the note.
These numbers are correctly described as a failed sufficient bound and
a successful finite-seed diagonal retention, not a global proxy theorem.
