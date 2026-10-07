# Independent audit of the positive full-tree transfer

Audited manuscript: `fulltree_kernel_positive_transfer.md`.

**Verdict:** its global positivity induction and constant-congruence obstruction are correct. Two additional targeted computations below exclude elementary grouping and boundary-collapse shortcuts. None contradicts the actual canonical Local TP2 conjecture.

## Exact global identities

For `R=[[1,1],[0,1]]`, substitution of `Q=R Qhat R^T` into the mediant recursion gives exactly

`Qhat_C=Qhat_A^T That Qhat_B^T`,

where `That=R^T T R=[[3y,3y-1],[3y+1,3y]]`.

All stated transformed seed matrices and the positive exceptional boundary transfer `Qhat_0^T That=[[2y,2y-1],[1,1]]` are correct. Endpoint0 remains only a left endpoint, so its signed matrix is always absorbed into this positive transfer when it matters. Every other canonical transformed matrix therefore has nonnegative integer ordinary coefficients by induction.

The identity `Q12-Q21=x` is preserved by the determinant-one congruence; consequently all transformed matrix gaps are symmetric. This justifies removing the transpose in the gap identities. Both root gap matrices are correct:

`E_A=y[[2x,2],[2,0]]`,

`E_B=y[[2x+1,1],[1,0]]`.

Under a left step, the new gap to the old center is `Qhat_A^T That E_B`, and the other gap is this matrix plus `E_A`. The right update has the stated symmetric form and adds `E_B`. Every multiplication and addition is nonnegative, including the boundary case. Thus the two gap-positivity inductions are valid at every canonical word, not just along a fixed ray.

Finally the first row of `R` is `(1,1)`, so the original scalar top-left polynomial is exactly `e^T Qhat e`; the scalar gap is the corresponding sum of four gap entries.

The constant-congruence obstruction is also valid: for `v=(a,b)`, `v^T T v=3ya²`. An invertible constant real congruence necessarily has at least one nonzero first-coordinate column, hence at least one diagonal entry is a positive multiple of `y`, whose central folded minor is negative.

## Two connectors do not yield an ordinary coefficient-block TP2 matrix

Direct multiplication gives

`That²=[[18y²-1,18y²-6y],[18y²+6y,18y²-1]]`.

Taking the central Laurent coefficient in each entry gives the two-state matrix

`[[53,48],[60,53]]`.

Its determinant is `53²-48*60=-71`. Therefore grouping two connectors does not produce a TP2 coefficient-block kernel in the natural state ordering, even at the single spatial index zero. Simultaneously reversing the state order on rows and columns leaves this principal minor unchanged.

## Positive unweighted boundary sums are still insufficient

The connector has trace `6y` and determinant1. With `e=(1,1)^T`, its third power has the exact boundary sum

`e^T That³ e=432y³-24y`.

Its ordinary coefficients are all positive, and its Laurent half-row is

`[3000,2568,1296,432]`.

Nevertheless its central folded defect is

`3000²+3000*1296-2*2568²=-301248`.

Thus products of positive connector blocks followed by unweighted boundary summation need not lie in the folded cone. The actual canonical gap seeds, their symmetry relations, and their constrained placement in the transfer products cannot be discarded in a proposed selective closure theorem.

These are deliberately targeted structural counterexamples, not a broad depth scan. The standalone exact verifier `fulltree_alternative_transfer_audit.py` reproduces all displayed seed identities and both obstructions. The positivity model remains useful, but an LGV or variation-diminishing proof still has to incorporate the canonical gap constraints or act directly on the required pairwise determinant.
