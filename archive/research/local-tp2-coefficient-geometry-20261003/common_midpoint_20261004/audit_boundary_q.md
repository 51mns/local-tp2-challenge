# Independent audit of the endpoint-1 Q boundary

Verdict: **PASS**, with exactly the all-N scope stated in
`root_boundary_q.md`. The theorem proves strict folded TP2 of
`yW_N` for every `N>=2`; it does not prove the signed proxy comparison.

## Analytic coverage of every degree

I checked the root pairing and residue partition in the read-only
`../continuation_difference.md`. Its roots are
`cos((2j-1)pi/(2N+1))-3/2`. The paired quadratics lie in
`5/2<=s<=3, 5/4<=c<=9/4`; the odd-degree middle shift lies in
`5/4<=a<=3/2`; the isolated inner pair has
`2/3<=a_in<=3/2, 3/2<=b_in<=2`. These bounds are unchanged by multiplying
one reserved block by `y`.

| Degree class | Reserved block | Minimum degree | Remaining blocks |
| --- | --- | ---: | --- |
| N=0 mod 4 | two general pairs | 4 | two-pair quartics |
| N=2 mod 4 | isolated inner pair | 2 | two-pair quartics |
| N=3 mod 4 | middle factor and one general pair | 3 | two-pair quartics |
| N=1 mod 4 | middle factor and two general pairs | 5 | two-pair quartics |

The reserved blocks exist at all four stated minimum degrees. Thus the
partition covers every `N>=2`, including N=2,3,4,5, without a missing
small-degree exception. All unreserved quartics retain the old strict
certificate. Only the reserved block receives the single `y` factor.
Strict folded product closure completes the all-N proof, including the
central and terminal indices. No cone-preserving assertion for `y` is used.

## Independent exact certificate reconstruction

`audit_boundary_q_verify.py` uses direct Laurent multiplication and imports
no producer arithmetic. It reconstructs all 22 supported defect polynomials,
every complete parameter degree box, and all 1,813 tensor-Bernstein
coefficients, then verifies the saved expansions and positive minima exactly.
The resulting minima agree with all four rows of the manuscript. The full
closed parameter cubes are certified, rather than finitely sampled.

The script also checks the excluded boundary: `yW_1=2y^2` has
`delta_1=0`. Therefore N>=2 is material. The actual endpoint-1 smaller
register has N_X>=2, so the theorem supplies exactly its needed Q kernel.

The nonboundary Robin-origin application still uses the separate exact
midpoint packet theorem. With that theorem and the already proved register
transport, this removes the endpoint-1 exception to strict K_Q. It does not
sign `W(Q,Pi)=delta(Q)+W(Q,V)`, whose second term is signed.

Reproduce from this directory:

```bash
python audit_boundary_q_verify.py
```

## Frozen source identities

| Source | SHA-256 |
| --- | --- |
| root_boundary_q.md | c34c71c4c7a7f36a54ffb8e9d1eaf6190c82628e5f5fdc0197273d9e6acf9a8a |
| root_boundary_q_verify.py | 7dde796f5cd9794206d55706da2acdf8e5e32ae405d38d8abf88c7e6fd457549 |
| root_boundary_q_results.json | 2095826236daab598d0060a854a7075687cf1a083cc0beebad3e109e350947bb |
| ../continuation_difference.md | 3be9a18fb19b5bd62559af6551f1eb09bcefe3d6a0caa16f399584fec95e2102 |

Full-tree strict Local TP2 and regular-edge strict proxy transport remain OPEN.
