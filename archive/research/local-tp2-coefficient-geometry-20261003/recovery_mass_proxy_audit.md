# Independent audit of the one-turn mass and proxy argument

Scope: `fulltree_oneturn_mass_proxy.md`, including its continuum finite bridge
and analytic tail. The result is **conditional** on the separate kernel
theorems specified below. It is not an arbitrary-tree Local TP2 proof.

**Verdict: PASS, conditional on those explicit kernel inputs.** Mathematical
review found no remaining gap in this multiplier/proxy argument. The complete
independent finite replay also passed and reproduced every saved certificate
record exactly.

## Mathematical review

The multiplier/proxy argument is valid under these inputs:

- Strict supported folded defects of the shifted trace factors `t-r`, of
  the single templates `A(t-r)+B`, and of the resulting prefix summands.
- Nonnegative symmetrized mixed kernel minors for distinct prefix summands.
- For the analytic inner-index tail, strengths
  `3*2^(2m-3)` for `A(t-r)+B`, `3*2^(m-2)` for `y(t-2)`, and
  `3*2^(m-1)` for `t-r`.

These are explicit dependencies, not consequences of positivity of their
coefficients. The separate one-turn closure work must supply them.

### Prefix residues, their number, and squared weights

Let `u_j=U_j(t/2)` and `v_j=u_j+u_(j-1)`. The exact factorizations
`R_(2h)=u_h v_h` and `R_(2h+1)=u_h v_(h+1)` give

`R_(2h-1)/R_(2h)=u_(h-1)/u_h`,
`R_(2h)/R_(2h+1)=v_h/v_(h+1)`.

Thus the quoted positive Jacobi-resolvent representation applies directly
to `R_(k-1)/R_k`, even when some roots of `R_k` cancel from that quotient.
Every active residue is positive, their sum is one (from the leading
`1/t` term), and their number is at most `k`. The summand for an active
root still contains all `k-1` remaining root factors of `R_k`.

The central Cauchy--Binet term is exactly
`delta_0(F) delta_0(G)`; the folded zero-index multiplicity introduces no
extra factor. It proves
`delta_0(Z_i)>=gamma_m*4^(k-1)*Z_i(2)`.

Since `B(2)<=A(2)` and `t(2)-2>1`, each ratio
`Z_i(2)/R_k(2)=A(2)+B(2)/(t(2)-r_i)` lies strictly between `A(2)` and
`2A(2)`. The convex average `Z_k(2)` therefore satisfies
`Z_i(2)>Z_k(2)/2` for every active summand.

Under pairwise compatibility, expansion of the quadratic central minor
retains nonnegative cross terms. Cauchy--Schwarz gives
`sum lambda_i^2 >= 1/|I| >= 1/k`; and `4^(k-1)>=k` for all `k>=1`
(induction from `k=1`, since `4k>=k+1`). Consequently
`delta_0(Z_k)>gamma_m*Z_k(2)/2>6Z_k(2)`. The proof includes `k=1`.

### Multiplier and strict supported indices

For `y^2`, the Fourier half-row is `(3,2,1)` and the supported defect
row is `(4,0,1)`. Despite its central zero at index one, multiplication
by a strict supported cone polynomial `Z` is strict. Put `d=deg Z`.
For `0<=n<=d`, retain the intermediate pair `(n,n+1)` in
`K_Z K_(y^2)`; its second principal minor is positive. For `n=d+1,d+2`,
retain `(d,d+1)`; the second minor has displacement one or two and is
positive. These cover the entire degree `d+2`.

For the specific index-two defect, retain intermediate `(0,1)` and
output columns `(2,3)` in the same product. This gives
`delta_2(y^2Z)>=delta_0(Z)*delta_2(y^2)=delta_0(Z)`.
The inequality `H(y^2Z)_3<=9Z(2)` is immediate from its nonnegative
full Laurent mass. The proved central mass margin therefore supplies
`3delta_2(y^2Z)>2H(y^2Z)_3`.

Independent expansion of `M=3Q+2(x+2)` gives exactly the four defect
formulas displayed in the reviewed manuscript. At indices zero and one,
the extra terms are nonnegative because a folded-cone half-row decreases;
the constant terms are strictly positive. The index-two estimate just
proved handles its negative correction. All later indices remain strict.

### Proxy comparison and terminal support

The finite/analytic criterion gives strictly positive adjacent base minors
`w_n` for `0<=n<=m+3`. Both rows have positive interval support, and
the upper row has one extra terminal position. Ratio transitivity
therefore supplies every ordered nonnegative minor needed in
Cauchy--Binet.

Every adjacent principal kernel minor of a folded-cone row `h` is at
least `delta_0(h)`. The boundary principal minor is exactly `delta_0`.
For an interior principal minor, the usual folded formula has
`a=0,b=2i`; it is at least
`Delta_0-Delta_(2i+1)=sum_(j=0)^(2i) delta_j >= delta_0`.
Its remaining cross term is nonnegative by monotonicity of
`(h_(j-1)+h_(j+1))/h_j`; zero-support cases follow from the expanded
formula. This proves the manuscript's retained Cauchy--Binet lower bound.

The correction minor is at least `-J(2)Z(2)H(K)_n`, since each
coefficient of the nonnegative product `JZ` is at most its full mass.
The strict condition `gamma_m*w_n>2J(2)H(K)_n` absorbs that correction.

For `n>=m+4`, both coefficients of `K` in the correction vanish.
Retaining input pair `(m+3,m+4)` is valid: its first minor equals the
positive product of the terminal coefficients of `J` and `V`. The
kernel minor has displacement `n-(m+3)`, which is at most `deg Z`
through the terminal index of `JZ`. Strict supported defects of `Z`
make this minor positive, including equality in that support bound.

### Analytic tail

The degrees are `deg(t-r)=m+2` and `deg(A(t-r)+B)=2m+3`, giving the
correct mass denominators `2m+5` and `4m+7`. For a decreasing supported
half-row, `h_0>=mass/(2d+1)`; the stated strengths therefore imply (6).

Independent ordinary expansion verifies
`V=(x+2)J+R`, `R=(x+1)(x+2)^2`, with Fourier row `(14,11,5,1)`.
Hence `w_n=delta_n(J)+M_n(J,R)>=(lambda_J-14)j_n`, using only
`j_(n+1)<=j_n` and `H(R)_n<=14`.

The Laurent coefficient comparisons used in (8) are valid:
`H(y^2)-H(y)=(2,1,1)>=0`, and
`2H(y^2)-H((x+2)^2)=(0,0,1)>=0`. Also `P>=x+2` follows from
`T_m>=1`. These prove `J>=2y^2P` and `K<=2J` without a cone
assumption on differences.

At `x=2`, the inner recurrence gives
`T_m(2)<=(7^(m+1)-1)/6`, so `P(2)<=(7^(m+1)+1)/2<=4*7^m`, and
`J(2)=27P(2)-12<=108*7^m`. For `m>=6`,
`lambda_J-14>=lambda_J/2`. Combining the two strengths reduces the
required bound exactly to `(8/7)^m>3072(4m+7)`.

The scalar ratio at successive indices is
`8(4m+7)/(7(4m+11))`; subtracting its denominator from its numerator
gives `4m-21>0` for `m>=6`. Thus an exact check at 106 proves this
bound at every later index. The trace mass ratio is
`2(2m+5)/(2m+7)>1`, and the template gamma ratio is
`4(4m+7)/(4m+11)>1`. Their exact starting checks prove the required
bounds throughout `m>=391`. No finite scan is being extrapolated.

## Independent finite implementation

`recovery_mass_proxy_audit.py` imports no implementation routines from the
original verifier. It builds the Chebyshev prefixes in ordinary `x`
coefficients, multiplies in that basis, and transforms using the defining
binomial formula `H(x^j)_n=binom(j,(j-n)/2)` at matching parity.

The only large product uses a byte packing base strictly larger than the
product of the two ordinary coefficient sums. This bounds every product
coefficient, so no carry is possible. A coefficient-sum identity is checked
after extraction. All arithmetic uses Python arbitrary-precision integers
and exact rational numbers.

The continuum Bernstein arrays are independently reconstructed from the
margin values at `u=0,1/2,1`: the middle coefficient is
`2f(1/2)-(f(0)+f(1))/2`. This avoids the original power-expansion routine.
Every supported base minor is recomputed. The entire resulting record
array is compared with the original JSON, including all gamma values,
all six continuum coefficients per index, minima, and maximizing witnesses.

The complete replay in `recovery_mass_proxy_audit.json` reports PASS:

- All 389 indices `m=2,...,390` were reconstructed independently.
- All 77,800 supported base proxy minors were strictly positive.
- All 778 continuum Bernstein arrays were strictly positive.
- Every field of all 389 original certificate records matched exactly.
- Exact scalar gates for the analytic tail passed.

The canonical JSON digest of the independently reconstructed record array
is `4b4a935be0bd032db1dc44025bb8f3b6cf9dfa0c0847a49674c28c9a181fdfe9`.
Replay used 33.781 seconds in this environment. The time is not part of the
mathematical certificate.
