"""Two whole-interval mass certificates for strict TP2 on L^2 R^k."""
import json
import continuation_prefix as p

x, u = p.variable(0), p.variable(1)


def polynomial(coefficients):
    result, power = {}, p.const(1)
    for coefficient in coefficients:
        result = p.add(result, p.scale(power, coefficient))
        power = p.mul(power, x)
    return result


def mass(poly):
    return p.add(*[{(0,) + key[1:]: value * 2**key[0]}
                   for key, value in poly.items()])


def cert(poly):
    degrees, coefficients = p.bernstein(poly)
    assert min(coefficients.values()) > 0
    return {
        'degrees': degrees,
        'strict_lower_bound': str(min(coefficients.values())),
        'power_coefficients': {','.join(map(str, key[1:])): str(value)
                               for key, value in sorted(poly.items())},
        'bernstein_coefficients': {key: str(value)
                                   for key, value in coefficients.items()},
    }


def main():
    a = polynomial([33, 64, 40, 8])
    b = polynomial([4, 2])
    t = polynomial([39, 116, 132, 66, 12])
    f = p.add(t, p.const(-2), p.scale(u, 4))
    L = p.add(p.mul(a, f), b)
    answer = {}
    for name, block, factor in [('propagator', f, 4), ('resolvent_template', L, 800)]:
        difference = p.add(p.defects(block)[0], p.scale(mass(block), -factor))
        answer[name] = {'mass_factor': factor, 'certificate': cert(difference)}
    print(json.dumps(answer, indent=2))


if __name__ == '__main__':
    main()
