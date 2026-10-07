# The missing endpoint-1 Robin certificate

**Theorem.** Write y=x+1, z=2x+3, and

    W_N=U_N(z/2)-U_(N-1)(z/2).

For every integer N>=2, yW_N has positive interval Fourier support and
strictly positive folded defects at every supported index. Raw W_N has
the same conclusion by the existing `../continuation_difference.md`.
The N=1 strict assertion is false: yW_1=2y² has defect delta_1=0.

This closes the boundary exception in applying the new Robin-minus
origin argument to Q=S-G. It does not establish the final strict proxy.

## Exact bounded-degree certificates

Use the root-pair domains already analytically proved for W_N:

    f=x²+s x+c, 5/2<=s<=3, 5/4<=c<=9/4;
    g is an independent member of the same domain;
    5/4<=a<=3/2 for a middle linear factor;
    2/3<=a_in<=3/2, 3/2<=b_in<=2 for the isolated inner pair.

Multiplying each possible reserved residue by y gives the following
exact lower bounds, in order from index0 through the terminal index.

| Block | Strict lower bounds |
| --- | --- |
| yfg | 57055/256, 112605/256, 18945/64, 1605/16, 57/4, 1 |
| y(x+a)f | 7395/256, 17327/256, 651/16, 135/16, 1 |
| y(x+a)fg | 6533675/4096, 13227625/4096, 2496225/1024, 253049/256, 14149/64, 357/16, 1 |
| y(x+a_in)(x+b_in) | 17/18, 97/9, 103/36, 1 |

`root_boundary_q_verify.py` constructs each Fourier row with reflection
at zero and zero extension at the upper support, computes its folded
defects exactly over the full parameter cube, and expands them in the
tensor Bernstein basis. Every rational coefficient is positive. The
complete power and Bernstein coefficients are saved in the result JSON.
The displayed lower bounds are the minimum Bernstein coefficients;
these are continuum polynomial certificates, not sampled values.

## Every N>=2 is covered

The existing root-pair proof provides W_N, up to the positive scalar
2^N, as a product of general quadratics plus the stated possible middle
or inner factors. Reserve blocks as follows:

| N | Reserved residue before multiplying by y | Remaining factors |
| --- | --- | --- |
| N=0 mod4, N>=4 | two general pairs fg | groups of two general pairs |
| N=2 mod4, N>=2 | the innermost pair | groups of two general pairs |
| N=3 mod4, N>=3 | middle linear factor times one general pair | groups of two general pairs |
| N=1 mod4, N>=5 | middle linear factor times two general pairs | groups of two general pairs |

Each reserved block exists at the indicated minimum N. All remaining
quartic blocks have strictly positive supported defects by the old exact
certificate. The four new certificates handle the only y factor. Strict
folded product closure then proves the theorem at every supported index,
including index0 and the terminal index. This does not assume that y is a
cone-preserving multiplier.

## Consequence for the common state

The exceptional endpoint-1 smaller register has f_j=U_j(z/2), N_X>=2.
Thus its actual Q=y(f_N-f_(N-1)) is strict folded TP2 by this theorem.
Other certified origins use the Robin path with terminal potential1,
whose spectrum lies in [-2,2]; the midpoint origin packet proves the
same Q assertion there. The register transport already covers BOTH
children and preserves N_X>=2. Consequently there is no additional
endpoint-1 obstruction to the proposed all-register strict K_Q theorem.

The remaining comparison is still W(Q,Pi)=delta(Q)+W(Q,V). Positivity
of delta(Q) alone does not control the signed second term.
