"""Publication-time finite tests; no universal mathematical conclusion."""
import unittest
import check


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items(): out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(p, factor):
    return {k: factor*v for k, v in p.items() if factor*v}


def mul(p, q):
    out = {}
    for i, u in p.items():
        for j, v in q.items(): out[i+j] = out.get(i+j, 0) + u*v
    return {k: v for k, v in out.items() if v}


def children(state):
    x, y = {1: 1, -1: 1}, {0: 1, 1: 1, -1: 1}
    a, c, b = state
    def mu(fixed, other):
        return add(scale(mul(mul(y, fixed), c), 3), scale(mul(x, add(fixed, c)), -1), scale(other, -1))
    return mu(a, b), mu(b, a)


class ContractTests(unittest.TestCase):
    def test_root(self):
        r = check.target(check.ROOT)
        self.assertEqual(r['H_S'], (40, 32, 16, 4))
        self.assertEqual(r['H_D'], (164, 138, 80, 30, 6))
        self.assertEqual(r['minors'], (272, 352, 160, 24))

    def test_first_children_and_orientation(self):
        left, right = check.children(check.ROOT)
        self.assertEqual(left, (13, 26, 18, 4))
        self.assertEqual(right, (29, 74, 74, 34, 6))
        self.assertEqual(check.state_for_word('L'), (check.ROOT[0], left, check.ROOT[1]))
        self.assertEqual(check.state_for_word('R'), (check.ROOT[1], right, check.ROOT[2]))
        pair = check.children(check.state_for_word('R'))
        self.assertGreater(check.degree(pair[0]), check.degree(pair[1]))

    def test_binomial_parity(self):
        self.assertEqual(check.half_row((0, 0, 1)), (2, 0, 1))
        self.assertEqual(check.half_row((0, 0, 0, 1)), (0, 3, 0, 1))
        self.assertEqual(check.half_row((1, 3, 3, 1)), (7, 6, 3, 1))

    def test_negative_and_zero_controls(self):
        # Noncanonical controls, not counterexamples to the challenge.
        self.assertEqual(check.adjacent_minors((7, 6, 3, 1), (19, 16, 10, 4, 1))[0], -2)
        self.assertEqual(check.adjacent_minors((1, 1), (2, 2))[0], 0)

    def test_input_guards(self):
        with self.assertRaises(ValueError): check.state_for_word('LxR')
        with self.assertRaises(ValueError): check.state_for_word('R'*100, 10)
        with self.assertRaises(ValueError): list(check.nodes(-1))

    def test_finite_count_and_terminal(self):
        r = check.scan(4)
        self.assertEqual(r['states_checked'], 31)
        self.assertEqual(r['supported_minors_checked'], 484)
        for _, state in check.nodes(4):
            t = check.target(state)
            n = t['degree_S']
            self.assertEqual(len(t['minors']), n+1)
            self.assertEqual(t['minors'][-1], t['H_S'][-1]*t['H_D'][n+1])

    def test_direct_laurent_reconstruction(self):
        # Different representation by the same author/model, not a separate reviewer.
        root = ({0: 1}, {0: 9, 1: 6, -1: 6, 2: 2, -2: 2}, {0: 2, 1: 1, -1: 1})
        stack = [('', root)]
        count = 0
        while stack:
            word, state = stack.pop()
            left, right = children(state)
            u, v = sorted((left, right), key=lambda p: max(p))
            s = add(u, scale(state[1], -1))
            d = add(v, scale(u, -1))
            expected = tuple(s.get(n, 0)*d.get(n+1, 0)-s.get(n+1, 0)*d.get(n, 0) for n in range(max(s)+1))
            got = check.target(check.state_for_word(word))
            self.assertEqual(got['H_S'], tuple(s.get(n, 0) for n in range(max(s)+1)))
            self.assertEqual(got['H_D'], tuple(d.get(n, 0) for n in range(max(d)+1)))
            self.assertEqual(got['minors'], expected)
            count += 1
            if len(word) < 5:
                a, c, b = state
                stack.append((word+'R', (c, right, b)))
                stack.append((word+'L', (a, left, c)))
        self.assertEqual(count, 63)


if __name__ == '__main__': unittest.main()
