# Alternative lane: parity transport is proved, recombination is not

**Decision: PAUSE.** There is a genuine new elementary transport lemma, but no viable complete arbitrary-parent gate emerged. The lemma does not justify investing in another partial-family campaign. The first decisive test of its natural sourcewise recombination fails at the actual canonical ROOT. The weaker sum recombination remains an unproved coupled condition, not a new proof mechanism ready to proceed.

All computations use exact integers and the original mutation. Older artifacts are read only. `alternative_parity_verify.py` writes only `alternative_parity_results.json` here. This lane uses neither child MP_0 packets nor parent/child Q<D assumptions.

## 1. The direct object is already known

For degree-oriented endpoints X,Y and center C, put

    U=3(x+1)XC-x(X+C)-Y,
    V=3(x+1)YC-x(Y+C)-X,
    L=U-C, R=V-C.

The original S=L and D=R-L satisfy exactly

    H(S)_i H(D)_j-H(S)_j H(D)_i
    =H(L)_i H(R)_j-H(L)_j H(R)_i.

This is `fulltree_direct_exchange.md`, not a new bridge. The factorized Fricke exchanges there also supply correlation but no valid deconvolution theorem. Calling monotone branch odds a new theorem would only rename the target.

The positive matrix-gap induction in `fulltree_kernel_positive_transfer.md` does give one additional usable fact: both L and R are divisible by y=x+1 and L/y,R/y have nonnegative ordinary coefficients globally. Both matrix seed gaps are y times nonnegative matrices; each child gap is a nonnegative matrix product of a previous gap. Dividing that common scalar y through the induction proves the assertion at BOTH children, including the exceptional endpoint-0 transfer. This statement is independent of every missing MP_0 or Q<D gate.

## 2. A genuine alternative transport theorem

**Theorem.** For either epsilon=0 or epsilon=1, the infinite matrix

    K^epsilon(m,n)=H((x+1)x^(2m+epsilon))_n,  m,n>=0,

is nonnegative TP2. Each row has positive interval support [0,2m+epsilon+1]. For epsilon=1, every minor in columns 0,1 vanishes. This theorem says nothing about mixed epsilon rows.

**Proof.** Put j>=0 and write adjacent column ratios only where both entries are positive. For epsilon=0 the ratios are

    K(m,2j+1)/K(m,2j) = (2m+1)/(m+j+1),
    K(m,2j+2)/K(m,2j+1) = (m-j)/(2m+1).

Both increase with m: the numerators of their discrete differences from m to m+1 are respectively 2j+1 and 2j+1. For epsilon=1 the corresponding ratios are

    K(m,2j+1)/K(m,2j) = (m+1-j)/(2m+2),
    K(m,2j+2)/K(m,2j+1) = (2m+2)/(m+j+2).

Their discrete-difference numerators are respectively 2j and 2j+2. All denominators are positive. The first ratio at j=0 equals 1/2 for every m. These formulas follow directly from H(x^k)_n=binom(k,(k-n)/2) at matching parity. Thus every ordered row pair has nonnegative adjacent minors throughout its common support. The support intervals are nested, so minors meeting an outer zero are also nonnegative. Multiplying adjacent ratio inequalities proves every ordered column-pair minor. This is an analytical all-index proof, not a kernel scan.

This avoids the fixed-shift obstruction *inside each parity*. It is not the old false assertion that the full kernel H((x+1)x^k)_n is TP2: its k=0,1 and n=0,1 minor is -1.

## 3. Exact source decomposition, and where it breaks

Let f=L/y and g=R/y, with coefficients f_a,g_a. For adjacent Fourier columns n,n+1, Cauchy--Binet gives

    target_n = sum_(a<b) (f_a g_b-f_b g_a)
                         det[H(yx^a),H(yx^b)]_(n,n+1).

Split the sum into even-even, odd-odd, and mixed parity sectors. The theorem proves positivity of the kernel factors in the first two sectors. Accordingly, nonnegative within-parity source minors plus nonnegative *whole mixed-sector sums* are a sufficient bridge to weak Local TP2. Strictness would additionally need a strictly positive contribution at each supported original index.

This conditional bridge is genuinely different from the old spectral MP_0 packet: it has no two-parameter resolvent or separate single-block cone. But neither its canonical source-order preservation nor its mixed-sector sum preservation is proved. Requiring the mixed-sector sum to be nonnegative is stronger than the target when same-parity terms can absorb a negative mixed sum. It must not be advertised as an exact equivalent target or as a completed induction.

The natural easier claim that every mixed sourcewise contribution is nonnegative already fails at canonical ROOT. Original recurrence gives

    X=1, Y=x+2, C=2x^2+6x+5,
    L=[8,20,16,4], R=[24,68,72,34,6],
    f=[8,12,4], g=[24,44,28,6].

Here arrays are ascending ordinary coefficients. At (a,b,n)=(0,1,0),

    f_0 g_1-f_1 g_0=64,
    det[H(y),H(yx)]_(0,1)=det[[1,1],[2,1]]=-1,

so the contribution is **-64**. Other ROOT mixed contributions at (a,b)=(0,3),(2,3) are -144 and -288. These are actual canonical negative terms, with all defining ROOT premises met; no relaxed fake parent is involved. The whole mixed sum is +144, the even-even sum is +128, and the odd-odd sum is zero. Thus the original ROOT target is +272. Negative terms do not refute Local TP2; they decisively refute the proposed termwise transport.

## 4. Separate parity transport cannot simply be combined

Reconstruct the earlier `kernel_proof.md` Section 6 counterexample:

    L=(x+1)^2(4x+5),
    R=(x+1)^2(2x+3)(4x+9).

This is a **relaxed/noncanonical** pair; no Fricke completion, canonical ancestry, parent packet or parent target is asserted. It has positive coefficients and common-y divisibility. Its normalized coefficients are

    f=[5,9,4], g=[27,57,38,8].

Both complete within-parity source orders hold: the only nonzero even-even source minor is 82 and the only nonzero odd-odd source minor is 72; outer-support pairs are nonnegative. Yet the central Fourier target is -8. The even-even contribution is +82, odd-odd is zero, and mixed contribution is -90. This exactly refutes a universal closure theorem whose premises consist only of the two proved parity kernels, positive normalized coefficients and within-parity source orders. It does not refute any canonical implication.

## 5. Comparison with frozen approaches and strategy judgment

- **Fixed shifted powers:** obstructed globally by root coefficient 16-12a and kernel necessity a>=sqrt(2). Parity transport succeeds on two separate subfamilies but fails to make their union TP2; it cannot evade the need for a coupled comparison.
- **Naive LGV/positive connector:** the already audited connector coefficient-block determinant -71 and unweighted boundary folded defect -301248 remain decisive. No network ordering or new weight-preserving switch is supplied here.
- **Separate cones / ordinary MLR:** the earlier combined counterexample already has real-negative roots, PF-infinity, ULC, strict ordinary MLR and decreasing folded defects. The parity calculation locates its remaining failure in the mixed contribution; it does not neutralize that failure.
- **Direct two-gap/Fricke:** exact product and determinant identities remain useful coupling data. Positivity of factors cannot be canceled through convolution. No missing deconvolution or canonical cancellation theorem has been proved.
- **Closed quotient/QW3/far-minor architectures:** this lane does not reopen them. It introduces a genuine binomial TP2 lemma but no target-native preservation theorem strong enough to replace the frozen missing conditions.

The first finite decisive test of termwise parity closure has been completed and is negative at ROOT. A possible next mathematical obligation would be a complete canonical BOTH preservation theorem for the *mixed-sector sum*, together with normalized within-parity source orders and strictness. There is no specified finite symbolic certificate or induction closure for that obligation; presenting it as a finite next task would be misleading. It is another coupled positivity gap. Under this strategy gate's requirement of a viable bridge, **this lane does not pass**. Retain the transport lemma as a small observation; pause additional exploratory tree/family scans unless an independently substantive canonical cancellation theorem is proposed.
