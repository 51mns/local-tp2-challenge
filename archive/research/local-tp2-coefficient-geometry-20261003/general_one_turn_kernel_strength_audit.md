# Independent audit of the all-minor strength lemma

**Verdict:** the proposed quantitative all-minor lemma and its relative-kernel consequence are valid. They are genuine general statements, not finite checks. They do not establish the required strength of the one-turn midpoint family by themselves.

Let `h_0,...,h_m` be a finite positive supported Laurent half-row, with symmetric extension and zero extension. Suppose

`delta_n(h)>=lambda h_n` for every supported `n`, with `lambda>0`.

The already proved quantitative adjacent-minor lemma gives

`det K_h[p,p+1;q,q+1]>=lambda K_h(p,q)`.

Since all defects are positive, the folded kernel is TP2 and the half-row decreases. Moreover the terminal inequality is `h_m²>=lambda h_m`, so `h_m>=lambda`. Every positive entry of the folded kernel is therefore at least `lambda`.

## Arbitrary row and column pairs

Take `i<j` and `k<l`, and assume the two diagonal entries `K(i,k)` and `K(j,l)` are positive.

If either cross entry vanishes, the determinant is the product of the diagonal entries. The lower-right entry is at least `lambda`, immediately giving

`det K[i,j;k,l]>=lambda K(i,k)`.

Otherwise both cross entries are positive. The folded kernel has a positive band of width `m`; the two inequalities `|i-l|<=m` and `|j-k|<=m` imply that **every** entry throughout the rectangle is positive. Thus all ratios below are defined.

For each adjacent cell put

`rho_(p,q)=K(p,q+1)K(p+1,q)/(K(p,q)K(p+1,q+1))`.

TP2 says `0<rho_(p,q)<=1`. Exact telescoping gives

`K(i,l)K(j,k)/(K(i,k)K(j,l))=product_(p=i)^(j-1) product_(q=k)^(l-1) rho_(p,q)`.

The product is at most its bottom-right factor. Therefore the normalized determinant of the full rectangle is at least the normalized determinant of the bottom-right adjacent cell. The quantitative adjacent bound yields

`1-K(i,l)K(j,k)/(K(i,k)K(j,l))`

`>=det K[j-1,j;l-1,l]/(K(j-1,l-1)K(j,l))`

`>=lambda/K(j,l)`.

Multiplying by the full diagonal product proves exactly

`det K_h[i,j;k,l]>=lambda K_h(i,k)`.

The positive-diagonal qualification is essential and must be retained in the statement. Both support-boundary cases and the special folded row/column zero are covered: only positivity of band entries, the existing adjacent bound, and the minimum positive entry were used.

## Relative kernel consequence

Let `B` have a positive finite supported half-row `b` and a folded TP2 kernel. Let `H` have a `lambda`-strong half-row `h`. Suppose coefficientwise `h>=b`, and `lambda>=8b_0`.

Then, for every ordered row and column pair,

`det K_H >= 4 det K_B`.

If the right-hand minor vanishes, this follows from TP2 of `K_H`. Otherwise it is positive, so both diagonal entries of `K_B` are positive. Coefficientwise half-row domination gives entrywise kernel domination and hence positive diagonal entries in `K_H`. The all-minor lemma gives

`det K_H >=lambda K_H(i,k)>=lambda K_B(i,k)`.

The cone implies `b_n<=b_0`, so every entry of `K_B` is at most `2b_0`, including its special first row and column. Nonnegative entries therefore imply

`det K_B<=K_B(i,k)K_B(j,l)<=2b_0 K_B(i,k)`.

Combining these estimates with `lambda>=8b_0` proves the desired factor4 domination. There is no missing factor of two from the folded normalization.

For the arbitrary one-turn midpoint `H=A(t-r)(t-s)+B(t-c)`, this supplies a valid reduction to coefficient domination and a quantitative strength bound. Proving that bound uniformly in the inner index remains a separate obligation; this audit does not infer it from the fixed-inner-index certificates.
