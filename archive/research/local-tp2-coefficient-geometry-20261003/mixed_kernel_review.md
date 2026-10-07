# Independent review of the general second-sandwich reduction

**Reviewed:** `mixed_second_sandwich.md`, Sections 1–4. **Result: PASS.** This review confirms the global positivity theorem and the stated conditional upper-band comparison; it does not prove the unresolved low band.

1. The mutation identity
   \[
   U-A-C=((2y-1)C-y)+(C-B)+y(A-1)(3C-1)
   \]
   is exact. The bracket's B-basis coefficients are exactly those listed. The established bounds \(c_1\ge c_0\ge3\) make them positive through degree \(C+1\). When \(\deg A\ge1\), the term involving the leading B-basis coefficient of \(A-1\), together with the dense row of \(3C-1\), fills all remaining degrees through \(\deg U\). For \(A=1\), the bracket already covers the full support. The root row is \((1,3,2)\), so both mutations prove \(C-A-B>_B0\) universally.

2. Expanding \(M=3yC-x+1\) and the original shorter-child difference gives
   \[
   3S=(3X-1)M-(3X+3Y+x-1).
   \]
   The correction has degree \(Y\), since every canonical larger endpoint has degree at least one and positive leading coefficient. Its listed B-basis coefficients are correct. The strict global center surplus and \(c_1\ge c_0\) prove \(0<_B R<_B M\), including indices 0 and 1 where the constants change.

3. Direct expansion yields the primitive minors
   \[
   W_n(3X-1,3PX)=9\delta_X(n)\quad(n\ge1),
   \]
   and \(W_0=9\delta_X(0)-3(h_0+2h_1+h_2)\). Thus the claimed scalar condition is exact when \(K_X\) is TP2. The stronger margin \(\delta_X(0)\ge h_0+h_1\) implies it because a folded-cone row is decreasing. The two boundary endpoints \(1,x+2\) give first minor 6 directly.

4. The factors of 3 in the determinant identity are correct:
   \[
   9W_n(S,Z)=W_n((3X-1)M,3Z)-W_n(R,3Z).
   \]
   If \(K_M\) is TP2, common-factor preservation makes the first term nonnegative under the stated primitive hypotheses. The second term vanishes for every \(n\ge\deg Y+1\), with zero extension of the row of R. This proves the conditional upper band exactly as stated.

The positivity of \(M-R\) supplies no missing likelihood-ratio comparison; the manuscript correctly leaves \(0\le n\le\deg Y\) open. This review does not independently rerun the separate Section 5 shortcut counterexample.
