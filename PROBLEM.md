# Exact problem contract

This file defines the target independently of the research archive.

Work in Z[x]. At the empty word set `(A,C,B)=(1, 2x²+6x+5, x+2)`. For an ordered triple define

```text
left_child  = 3(x+1) A C - x(A+C) - B
right_child = 3(x+1) B C - x(B+C) - A
L(A,C,B)    = (A, left_child, C)
R(A,C,B)    = (C, right_child, B)
```

Read a finite word over `{L,R}` from left to right. At its resulting state calculate the two child polynomials, and order them by polynomial degree: `deg U < deg V`. Degree order is not the same as the letter order.

Set `S=U-C`, `D=V-U`. For `P(x)=sum_j a_j x^j`, define

$$
H(P)_n=\sum_{\substack{j\ge n\\j\equiv n\pmod2}}a_j\binom{j}{(j-n)/2}\qquad(n\ge0).
$$

Equivalently `H(P)_n=[q^n] P(q+q^(-1))`. This is the symmetric Laurent **half-row**: do not double its positive-index coefficients. Negative indices are reflected when used in auxiliary formulae; indices above the degree have coefficient zero.

## The assertion

For every finite canonical word and every integer `n` with `0 <= n <= deg S`,

$$
F_n=H(S)_nH(D)_{n+1}-H(S)_{n+1}H(D)_n>0.
$$

A refutation must specify a canonical word and supported index with `F_n <= 0`. A noncanonical pair of positive polynomials is not a refutation. Failure of an auxiliary sufficient condition is not a refutation. Checking a finite set of words is not a universal proof.

## Conventions to audit

- The empty word is included.
- Child polynomials are computed from the same parent, before either move is made.
- Both the subtraction `S=U-C` and the subtraction `D=V-U` are part of the target.
- The terminal index `n=deg S` is included; `H(S)_(n+1)=0` there.
- Dividing S and D by x+1 changes the coefficient rows and cannot silently replace the target.
- The root endpoints are not symmetric. Do not exchange all letters L/R in a partial theorem without a proof.

## Exact root fixture

```text
S(x) = 8 + 20x + 16x² + 4x³
D(x) = 16 + 48x + 56x² + 30x³ + 6x⁴
H(S) = [40, 32, 16, 4]
H(D) = [164, 138, 80, 30, 6]
F    = [272, 352, 160, 24]
```

The short implementation in `check.py` computes the literal contract, rather than a stronger auxiliary cone assertion.
