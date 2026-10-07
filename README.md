# Local TP2 Challenge

**Prove the inequality, find an exact counterexample, or find an error in the partial proofs.**

**Status: OPEN in this project — neither a full-tree proof nor a canonical counterexample has been established.**
This is an AI-assisted research question, not a claimed solution to a famous conjecture. Historical internal proofs are offered for audit, not as unquestionable premises.

[日本語](README.ja.md) · [Exact problem](PROBLEM.md) · [Current status](STATUS.md) · [Failed approaches](FAILED_ROUTES.md) · [How to contribute](CONTRIBUTING.md)

## The complete question

Start with the ordered polynomial triple

$$
(A,C,B)=(1,2x^2+6x+5,x+2).
$$

Define

$$
\ell=3(x+1)AC-x(A+C)-B,\qquad
r=3(x+1)BC-x(B+C)-A.
$$

The letter **L** replaces the triple by $(A,\ell,C)$; the letter **R** replaces it by $(C,r,B)$. Every finite word over `{L,R}`, including the empty word, is a canonical state. Read words from left to right.

At each state, form both children again and order the **child polynomials by degree**, calling the smaller one $U$ and the larger one $V$. Define

$$
S=U-C,\qquad D=V-U,\qquad H(P)_n=[q^n]P(q+q^{-1}).
$$

Is it true that, for every canonical state,

$$
\boxed{H(S)_nH(D)_{n+1}-H(S)_{n+1}H(D)_n>0
\quad\text{for every }0\le n\le\deg S?}
$$

Coefficients outside the support are zero. **Zero is a counterexample to the strict assertion.** The terminal index is part of the question. The names L/R do not determine which child has lower degree.

At the empty word:

```text
H(S) = [40, 32, 16, 4]
H(D) = [164, 138, 80, 30, 6]
F    = [272, 352, 160, 24]
```

This statement is self-contained: no private repository, prior chat, model subscription or account is needed to work on it.

## Try the exact checker

Python 3.10+; no third-party packages for the small reference checker.
Run in **Terminal or VS Code's integrated terminal on macOS/Linux**, or **PowerShell on Windows**, from the repository root (`python` may replace `python3` on Windows).

```bash
python3 -m unittest discover -s tests -v
python3 check.py --word LRL
python3 check.py --depth 6
```

The first command tests conventions and negative controls. The second checks every supported minor at one state. The third checks all words of length at most six. These are finite computations, not universal proofs. Large words can be expensive; the reference checker has an explicit degree limit.

## What has been tried?

| Item | Precise public status |
|---|---|
| All $L^mR^kL^j$, with nonnegative exponents | An internal proof package is included for audit. It has not received external peer review or formal verification. |
| $LRLR^N$ and $RLRL^N$ | Signed-seed proof candidates and replay code are included. Not a proof of all four-run paths. |
| Global positive coordinates, character positivity, Fricke identities | Supporting manuscripts are included; these do not themselves prove the Fourier minors. |
| 16,677 states / 10,176,120 supported minors | Historical exact-search report: all positive in that finite scope. This publication does not newly rerun that entire search. |
| Uniform maximum-coefficient margin preservation | The proposed sufficient condition fails on canonical states. This is not a counterexample to Local TP2. |

See [STATUS.md](STATUS.md) before relying on a historical label such as `PROVED_INTERNAL`. The mathematical archive is separated from the entry pages so solvers can start independently.

The search was exhaustive only through **depth 13**. Some selected paths have length 1,024; that is not exhaustive depth 1,024. The smallest reported relative margin was at the centre of $RL^5R^{160}L$, approximately $2.120514229740311\times10^{-7}$, still strictly positive. No conclusion about an infinite limit follows.

## What would be a useful contribution?

A full proof; an exact canonical word and index with a nonpositive minor; a verifiable error in a partial proof; or a genuinely general lemma that changes the problem. A new proof need not use the existing kernel machinery.

Please submit an **[Issue](https://github.com/51mns/local-tp2-challenge/issues)** or pull request with assumptions, exact arithmetic and reproducible steps. Do not promote a finite scan to a proof, or mistake a failed sufficient condition for a counterexample to the target.

[Research map](RESEARCH_MAP.md) · [Manuscript archive](archive/README.md) · [Evidence and provenance](evidence/README.md) · [Sources](REFERENCES.md)

## Licensing and attribution

This project follows the existing AIMath public path-based policy: software **Apache-2.0**, original exposition **CC-BY-4.0**, scientific data **CC0-1.0**, to the extent the contributors hold the relevant rights. See [LICENSE](LICENSE). Third-party works are linked, not relicensed. AI assistance and same-model reimplementations are not external independent review.
