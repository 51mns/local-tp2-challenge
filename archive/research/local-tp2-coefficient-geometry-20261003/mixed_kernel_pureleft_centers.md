# Every pure-left center belongs to the sufficient center cone F

This is a companion to `mixed_kernel_pureleft_multiplier.md`; the notation and the eight residue boxes are unchanged.

For every integer m at least 2, the half-row of

\[
Q_m=yT_m(x+3/2)
\]

is 3-strong. To prove this, use exactly the same factorization as before, replacing each residue \(2^dy^2R\) by \(2^dyR\). The removed scaled quartics remain 1-strong. The minimum exact Bernstein coefficients of the margins \(\delta_n-3h_n\) are:

| m modulo 8 | Lower bounds in order of supported indices |
|---|---|
| 0 | 58420, 172926, 105672, 37512, 5680, 208 |
| 1 | 2899408, 5696920, 4361910, 1727064, 377536, 35280, 928 |
| 2 | 36, 210, 60, 4 |
| 3 | 3038, 5140, 2966, 568, 40 |
| 4 | 93424, 178368, 114056, 34616, 4680, 208 |
| 5 | 3501688, 7027648, 5129016, 1961820, 395128, 35280, 928 |
| 6 | 114320374, 239565988, 190864316, 85324380, 22116144, 3139792, 199808, 3904 |
| 7 | 3378, 7170, 3646, 764, 40 |

All are positive on their complete continuous parameter boxes. The strength-product theorem yields the claimed 3-strong bound for every m at least 2. The deterministic script `mixed_kernel_pureleft_centers.py` generates the full rational certificate artifact `mixed_kernel_pureleft_centers_certificates.json`; it imports the residue definitions from the multiplier verifier so the boxes cannot drift.

Now put \(g_m=1+Q_m\) and \(q=H(Q_m)\). Adding 1 changes its defects by

\[
\begin{aligned}
\delta_0(H(g_m))&=\delta_0(q)+2q_0+q_2+1,\\
\delta_1(H(g_m))&=\delta_1(q)-q_2,\\
\delta_n(H(g_m))&=\delta_n(q)\quad(n\ge2).
\end{aligned}
\]

Since a 3-strong row is decreasing, these expressions imply

\[
\delta_n(H(g_m))\ge2H(g_m)[n]
\]

at every supported n: at index 1 use \(3q_1-q_2\ge2q_1\), and at index 0 the margin beyond \(2(q_0+1)\) is at least \(3q_0+q_2-1>0\).

For the second condition defining F, use \(yg_m=y+P_m\), where \(P_m=y^2T_m\) is 4-strong by the multiplier theorem. If \(h=H(P_m)\), then

\[
\delta_0(H(yg_m))=\delta_0(h)+2h_0+h_2-4h_1-1
\ge2h_0+h_2-1>0.
\]

Thus \(g_m\in F\) for every m at least 2. The remaining center \(g_1=2x^2+6x+5\) has half-row \((9,6,2)\), defect differences \((27,14,4)\), and \(\delta_0(H(yg_1))=31\), so it also belongs to F.

**Consequently every pure-left center \(g_m\), m at least 1, supplies all three hypotheses of the conditional general first-sandwich induction:** \(K_{g_m}\) is TP2, \(K_{t_{g_m}}\) is TP2, and \(\delta_0(H(g_m))\ge H(g_m)[0]+H(g_m)[1]\). This is an actual infinite canonical subfamily theorem. It does not establish F for centers after arbitrary mixed mutations.
