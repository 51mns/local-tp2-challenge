# Independent audit: the bivariate curvature pair

**Verdict: PASS for conditional BOTH-child closure.** The two curvature
identities and the sign theorem in `proxy_curvature.md` are valid.
They add a genuinely transported auxiliary condition given parent P_Q;
they do not provide child folded cones or the strict proxy.

Audited source SHA-256:
`21e541e4e8e706b63f06b196cfc0d8be4353eb50a870c7c0981e1746e62466d8`.

Before the character homomorphism, use divided differences and averages.
Product differentiation gives
`D_s=bar(t)D_g+bar(g)D_t-D_r` and
`D_u=bar(t)D_s+bar(s)D_t-D_g`.
Subtracting the curvatures cancels both bar(t) terms and leaves
`D_t[bar(g)D_s-bar(s)D_g]`, the Bezoutian forcing with the stated LR
orientation. This proves the fixed-trace identity in all degrees.

The sibling identity similarly follows by expanding D_B-D_A and the
two D_(T seed +/- E) terms. The remaining bracket has exactly the
orientation `R(E,A)+R(E,B)`; no sign reversal was found.

The actual child identification is also correct. The short child's
larger-endpoint curvature has previous seed -E and its next polynomial
is `T(E+G+S)+E`; the long child's previous seed is +E and its next
polynomial is `T(G+S+D)-E`. Hence the two displayed sibling curvatures
are the actual child coordinates, not arbitrary positive seeds.

Parent P_Q supplies G<=lr S, S<=lr D and E<=lr G, hence all the
comparisons used to sign the forcing tensors. Positive character
multiplication preserves these signs. The short larger-endpoint
curvature is positive directly from its negative previous seed;
the sibling identity then signs the long one. No child P_Q premise
is inserted into this conditional argument.

The root has the explicitly negative central kappa_X coefficient -3,
so it remains a separate exception. The saved complete first-level
character arrays supply exact seeds: central values (45,8595) and
(2208,9307), with no negative coefficients. These are finite seed
checks, not a depth extrapolation. The underlying exact identity
checks and first-level records in `proxy_curvature_verify.py` were
inspected along with the analytical proof.

Finally, polarized Cassini leaves the signed factor
`(U^2-4)(V^2-4)` multiplying curvature. Its sign prevents reading
positive curvature as folded positivity without another cancellation
lemma. That missing connection is explicitly retained. This audit
promotes only the conditional auxiliary closure, not the actual kernel
or Local TP2 target.

The final seed-explanation revision has also been checked. Its complete
first-child arrays and central pairs agree with the exact read-only
replay already performed. The six-variable identity checks supply
algebra, while the saved first-child arrays supply finite seeds; the
revision correctly keeps these two roles separate. It changes no
mathematical hypothesis or promoted consequence.
