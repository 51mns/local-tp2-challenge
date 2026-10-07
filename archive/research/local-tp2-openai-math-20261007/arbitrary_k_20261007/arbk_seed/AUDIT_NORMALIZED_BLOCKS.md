# Independent audit of the normalized block theorems

**Verdict: PASS — mathematical block assembly and every exact tensor
coefficient independently reconstructed.**

Reviewed `../arbk_mixed/NORMALIZED_BLOCKS.md` and both of its generating
implementations. The separate verifier `audit_normalized_blocks.py`
imports no author code and reproduces the complete continuum
certificates by a different polynomial basis and Bernstein construction.

## Mathematical review

For `m=0`, the established paired-root decomposition of the prefix
`R_j` has exactly `floor(j/2)` paired factors and at most one remaining
nonpositive root. The pair box `a in [0,4], b in [-4,4]` contains every
actual pair. Four pairs have degree 16. The seed residue with zero through
three pairs, an optional nonpositive single, and optional multiplication
by `y`, has degree at most 16. Thus the normalized product loss is at
most 34, and the resulting factor is exactly `128*34=4352` per complete
eight-root block. Since `4352<3^8`, the stated lower bound

\[
\eta(Z_j),\eta(yZ_j)\ge\frac1{256}\,4352^{-\lfloor j/8\rfloor}
\ge\frac1{256\,3^j}
\]

holds, including `j=0`. No Jacobi mixture loss is required on this
boundary because the old second seed vanishes.

For `m=1,...,4`, an eight-trace block has degree `8d`, `d=m+2`.
Attaching any further such block therefore costs at most
`D=2(8d+1)`, regardless of the accumulated product's degree. The
certificate target `D*rho_m^8` consequently contributes exactly
`rho_m^8` after attachment. The distinguished residue covers every
possible remainder `N=0,...,7`, raw and smoothed. This proves the
summand estimate `E_m*rho_m^(j-1)`. The already established compatibility,
positive squared residue weights, and coefficient comparison with the
average give the correctly retained factor `1/(4j)` for `Z_j,yZ_j`.

The four audited pairs `(rho_m,E_m)` are

| m | rho_m | E_m |
|---|---|---|
| 1 | 1/4 | 1/301 |
| 2 | 1/4 | 1/513 |
| 3 | 1/4 | 1/785 |
| 4 | 1/5 | 1/1114 |

The author's histogram formula follows from averaging the two endpoint
assignments at each middle Bernstein index. All binomial multiplicities
and the distinguished middle-index denominator are correct. The
independent computation below additionally checks this formula against
every expanded tensor coefficient, so the audit does not rely solely on
the symmetry argument.

## Independent exact reconstruction

The author computes the `m=0` coefficients with sparse parameter-power
algebra in the symmetric Laurent basis, and the `m=1,...,4` coefficients
with a compressed endpoint-pair formula. The independent verifier uses:

1. The original canonical mutations in the ordinary `x` basis to
   reconstruct each old trace and both old seeds.
2. Ordinary polynomial multiplication and Fourier Horner conversion.
3. Exact evaluation on the complete tensor interpolation set
   `{0,1/2,1}` in each variable, followed by an independent degree-two
   tensor interpolation to Bernstein coefficients.
4. Exact inverse reconstruction at every supported index.

Every row entry is affine in each independent parameter; hence every
defect and square has degree at most two in each parameter. These exact
interpolation data determine the entire polynomial. They are not a
finite sample substituted for a continuum proof.

Results:

- **223,484** tensor coefficients for all `m=0` blocks and residues
  match every per-index minimum and complete ordered coefficient digest.
- **4,021,860** expanded tensor coefficients for `m=1,...,4` match the
  author's **102,060** symmetry-compressed coefficients, including their
  exact denominators and all repeated orbit entries.
- All normalized margins are nonnegative, every row has positive
  supported coefficients, and every product denominator and rate identity
  matches the theoretical degree bound.

The full audit record is `normalized_blocks_independent_audit.json`.
The verifier does not mutate the author sources or their result files.

## Reproduction and required files

From the common parent directory, with Python's standard library:

```bash
python arbk_mixed/m0_normalized_blocks.py --residues
python arbk_mixed/finite_m_normalized_blocks.py
python arbk_seed/audit_normalized_blocks.py
```

The last command requires the two result JSON files produced by the
first two commands and `arbk_seed/ordinary_arithmetic.py`. It writes
only `arbk_seed/normalized_blocks_independent_audit.json`.

This is a separate mathematical review and implementation within the
shared research session. It is not external peer review or formal
proof-assistant verification. The theorem audited here supplies
normalized old-mixture bounds; the final three-run Local TP2 proof
uses additional explicitly identified ingredients.
