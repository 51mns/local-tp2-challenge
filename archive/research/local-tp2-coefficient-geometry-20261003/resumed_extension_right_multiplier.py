"""Exact uniform certificates for the all-right multiplier theorem.

Run from this research directory with standard-library Python.
The reusable arithmetic comes from continuation_prefix.py.  No numerical
parameter sampling or finite-depth assertion is used.
"""
from continuation_prefix import (
    add, bernstein, const, defects, fourier, mul, scale, variable,
)


def pow2(p):
    return mul(p, p)


def certify_positive(name, polynomial, expected_lower=None):
    degrees, coefficients = bernstein(polynomial)
    lower = min(coefficients.values())
    assert lower > 0, (name, lower, coefficients)
    if expected_lower is not None:
        assert lower == expected_lower, (name, lower, expected_lower)
    return {"name": name, "degrees": degrees, "lower_bound": str(lower)}


def main():
    x = variable(0)
    parameter = variable(1)
    c = add(const(4), scale(parameter, 4))
    y = add(x, const(1))
    P = add(x, const(2))
    Q = add(scale(pow2(x), 3), scale(x, 8), c)
    root_row = fourier(Q)
    assert root_row[:3] == [add(c, const(6)), const(8), const(3)]
    root_defects = [
        add(pow2(c), scale(c, 15), const(-74)),
        add(const(37), scale(c, -3)),
        const(9),
    ]
    assert defects(Q) == root_defects

    A = mul(pow2(y), Q)
    initial_row = [
        add(scale(c, 3), const(56)),
        add(scale(c, 2), const(50)),
        add(c, const(31)),
        const(14), const(3),
    ]
    assert fourier(A)[:5] == initial_row
    initial_defects = [
        add(scale(pow2(c), 4), scale(c, 85), const(-128)),
        add(scale(c, 17), const(503)),
        add(pow2(c), scale(c, 37), const(158)),
        add(const(94), scale(c, -3)),
        const(9),
    ]
    assert defects(A) == initial_defects

    mass_Q = add(c, const(28))
    diagonal_minor = add(mul(add(c, const(9)), add(c, const(6))), const(-64))
    propagation_margin = add(diagonal_minor, scale(mass_Q, -1))
    assert propagation_margin == add(pow2(c), scale(c, 14), const(-38))
    initial_margin = add(scale(initial_defects[1], 3), scale(mass_Q, -9))
    assert initial_margin == add(scale(c, 42), const(1257))

    G = add(const(1), scale(A, 3))
    corrected_defects = [
        add(scale(initial_defects[0], 9), scale(initial_row[0], 6),
            scale(initial_row[2], 3), const(1)),
        add(scale(initial_defects[1], 9), scale(initial_row[2], -3)),
    ] + [scale(value, 9) for value in initial_defects[2:]]
    assert defects(G) == corrected_defects

    base = mul(P, add(const(1), scale(pow2(y), 3)))
    assert fourier(base)[:4] == [const(n) for n in (32, 25, 12, 3)]
    assert defects(base) == [const(n) for n in (158, 172, 60, 9)]
    assert defects(P) == [const(2), const(1)]

    certificates = []
    for n, (polynomial, lower) in enumerate(zip(root_defects, (2, 13, 9))):
        certificates.append(certify_positive(f"root_delta_{n}", polynomial, lower))
    for n, (polynomial, lower) in enumerate(zip(initial_defects, (276, 571, 322, 70, 9))):
        certificates.append(certify_positive(f"initial_delta_{n}", polynomial, lower))
    certificates.append(certify_positive("propagation_margin", propagation_margin, 34))
    certificates.append(certify_positive("initial_mass_margin", initial_margin, 1425))
    import json
    print(json.dumps({"status": "PASS", "certificates": certificates}, indent=2))


if __name__ == "__main__":
    main()
