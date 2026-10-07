#!/usr/bin/env python3
"""Small exact reference for PROBLEM.md, not a full-tree proof.

Run in Terminal / VS Code's integrated terminal (macOS/Linux) or PowerShell
(Windows), from the repository root. Python 3.10+, standard library only.
Polynomial coefficients are integers in ascending powers of x.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from math import comb
from typing import Iterator

Poly = tuple[int, ...]
State = tuple[Poly, Poly, Poly]
ROOT: State = ((1,), (5, 6, 2), (2, 1))


def trim(p: list[int] | tuple[int, ...]) -> Poly:
    values = list(p)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [0])


def degree(p: Poly) -> int:
    return -1 if p == (0,) else len(p) - 1


def add(a: Poly, b: Poly) -> Poly:
    return trim([u + v for u, v in itertools.zip_longest(a, b, fillvalue=0)])


def scale(p: Poly, factor: int) -> Poly:
    return trim([factor * value for value in p])


def sub(a: Poly, b: Poly) -> Poly:
    return add(a, scale(b, -1))


def mul(a: Poly, b: Poly) -> Poly:
    result = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b):
                result[i + j] += u * v
    return trim(result)


def children(state: State, max_degree: int = 512) -> tuple[Poly, Poly]:
    a, c, b = state
    projected = max(degree(a), degree(b)) + degree(c) + 1
    if projected > max_degree:
        raise ValueError(f'Child degree {projected} exceeds limit {max_degree}; '
                         'use a shorter word or explicitly raise --max-degree.')
    def mutation(fixed: Poly, other: Poly) -> Poly:
        product = scale(mul(mul((1, 1), fixed), c), 3)
        return sub(sub(product, mul((0, 1), add(fixed, c))), other)
    return mutation(a, b), mutation(b, a)


def state_for_word(word: str, max_degree: int = 512) -> State:
    if set(word) - set('LR'):
        raise ValueError('A word must contain only uppercase L and R; use an empty string for the root.')
    state = ROOT
    for letter in word:
        a, c, b = state
        left, right = children(state, max_degree)
        state = (a, left, c) if letter == 'L' else (c, right, b)
    return state


def half_row(p: Poly) -> Poly:
    """[q^n]P(q+q^-1), n>=0, with exact binomial arithmetic."""
    return tuple(sum(p[j] * comb(j, (j - n) // 2)
                     for j in range(n, len(p), 2))
                 for n in range(len(p)))


def adjacent_minors(hs: Poly, hd: Poly) -> Poly:
    def get(row: Poly, n: int) -> int:
        return row[n] if n < len(row) else 0
    return tuple(value * get(hd, n + 1) - get(hs, n + 1) * get(hd, n)
                 for n, value in enumerate(hs))


def target(state: State, max_degree: int = 512) -> dict:
    left, right = children(state, max_degree)
    if degree(left) == degree(right):
        raise ValueError('Unexpected equal child degrees; inspect the state and conventions.')
    u, v = sorted((left, right), key=degree)
    s, d = sub(u, state[1]), sub(v, u)
    hs, hd = half_row(s), half_row(d)
    values = adjacent_minors(hs, hd)
    failures = [{'index': n, 'value': value} for n, value in enumerate(values) if value <= 0]
    margins = []
    for n, value in enumerate(values):
        if n + 1 < len(hd) and hs[n] * hd[n + 1] > 0:
            margins.append((Fraction(value, hs[n] * hd[n + 1]), n))
    minimum = min(margins) if margins else None
    return {'S': s, 'D': d, 'H_S': hs, 'H_D': hd, 'minors': values,
            'degree_S': degree(s), 'degree_D': degree(d),
            'all_strict': not failures, 'failures': failures,
            'minimum_relative_margin': None if minimum is None else {
                'index': minimum[1], 'numerator': minimum[0].numerator,
                'denominator': minimum[0].denominator}}


def nodes(depth: int, max_degree: int = 512) -> Iterator[tuple[str, State]]:
    if depth < 0:
        raise ValueError('Depth must be nonnegative.')
    stack = [('', ROOT)]
    while stack:
        word, state = stack.pop()
        yield word, state
        if len(word) < depth:
            a, c, b = state
            left, right = children(state, max_degree)
            stack.append((word + 'R', (c, right, b)))
            stack.append((word + 'L', (a, left, c)))


def scan(depth: int, max_degree: int = 512) -> dict:
    states = minors = 0
    for word, state in nodes(depth, max_degree):
        result = target(state, max_degree)
        states += 1
        minors += len(result['minors'])
        if result['failures']:
            return {'status': 'COUNTEREXAMPLE_FOUND', 'word': word,
                    'states_checked': states, 'supported_minors_checked': minors, **result}
    return {'status': 'NO_COUNTEREXAMPLE_IN_THIS_FINITE_SEARCH',
            'exhaustive_depth': depth, 'states_checked': states,
            'supported_minors_checked': minors, 'full_tree_status': 'OPEN'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--word', help='Literal canonical word, e.g. LRL; empty string denotes the root.')
    group.add_argument('--depth', type=int, help='Exhaustively check words through this finite depth.')
    parser.add_argument('--max-degree', type=int, default=512,
                        help='Explicit resource guard for naive polynomial arithmetic (default 512).')
    args = parser.parse_args()
    try:
        if args.max_degree < 4:
            raise ValueError('--max-degree must be at least 4.')
        if args.depth is not None:
            if args.depth > 16:
                raise ValueError('The small reference checker caps exhaustive depth at 16; '
                                 'use an appropriate audited search implementation for larger runs.')
            output = scan(args.depth, args.max_degree)
            failed = output['status'] == 'COUNTEREXAMPLE_FOUND'
        else:
            word = args.word if args.word is not None else ''
            output = {'word': word, **target(state_for_word(word, args.max_degree), args.max_degree)}
            failed = not output['all_strict']
        print(json.dumps(output, indent=2))
        return 1 if failed else 0
    except ValueError as exc:
        parser.error(str(exc))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
