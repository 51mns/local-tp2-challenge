"""Exact symbolic checks for the uniform one-turn first comparison.

The proof for every m is in general_one_turn_first.md. This verifier
checks a generic recurrence identity, not an enumeration over m.
"""
from fractions import Fraction
from continuation_prefix import add, const, fourier, mul, scale, variable


def minors(a,b):
    n=max(len(a),len(b))
    a=a+[0]*(n+1-len(a))
    b=b+[0]*(n+1-len(b))
    return [a[j]*b[j+1]-a[j+1]*b[j] for j in range(n)]


def main():
    x,pm,pm_previous=[variable(j) for j in range(3)]
    y=add(x,const(1))
    P=add(x,const(2))
    z=add(scale(x,2),const(3))
    pm_next=add(mul(z,pm),scale(pm_previous,-1))
    generic_increment=scale(add(pm_next,pm,pm_previous),Fraction(1,2))
    assert generic_increment==mul(P,pm)

    p0=y
    p1=mul(y,z)
    p2=mul(y,add(mul(z,z),const(-1)))
    g1=add(const(1),p0,p1)
    assert mul(P,g1)==add(scale(p2,Fraction(1,2)),p1,z)
    assert add(P,p0)==z
    assert fourier(z)[:2]==[const(3),const(2)]
    assert fourier(p1)[:3]==[const(7),const(5),const(2)]
    assert fourier(mul(P,P))[:3]==[const(6),const(4),const(1)]
    assert minors([3,2],[7,5,2])==[1,4,0]
    assert minors([6,4,1],[7,5,2])==[2,3,0]
    print('PASS: generic telescoping identity and all base comparisons')
    print('All-m MLR follows from the proved p_j ray order and fixed-upper-row mixture.')


if __name__=='__main__':
    main()
