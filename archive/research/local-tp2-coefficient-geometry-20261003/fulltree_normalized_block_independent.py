"""Independent exact ordinary-bivariate audit of the eight-factor theorem.

No routines or local arrays are imported from the Laurent certificate.
All arithmetic entering the margins uses Python arbitrary-precision ints.
NumPy object arrays only accelerate their storage and matrix operations.
"""
from fractions import Fraction
from math import comb
import json
import time
import numpy as np


def local_tensor(a,b):
    # Ordinary x coefficients of x^2+(3+u)x+5/4+5u/2+v.
    factor=[{(0,0):Fraction(5,4),(1,0):Fraction(5,2),(0,1):Fraction(1)},
            {(0,0):Fraction(3),(1,0):Fraction(1)},
            {(0,0):Fraction(1)}]
    result=np.empty((3,3),dtype=object)
    for i in range(3):
        for j in range(3):
            value=Fraction(0)
            for (p,q),c in factor[i].items():
                for (r,s),d in factor[j].items():
                    up,vp=p+r,q+s
                    if up<=a and vp<=b:
                        value+=c*d*Fraction(comb(a,up),comb(2,up))*Fraction(comb(b,vp),comb(2,vp))
            scaled=64*value
            assert scaled.denominator==1 and scaled>=0
            result[i,j]=int(scaled)
    assert all(result[i,j]==result[j,i] for i in range(3) for j in range(3))
    return result


def fourier_monomial(degree,n):
    n=abs(n)
    return comb(degree,(degree-n)//2) if n<=degree and (degree-n)%2==0 else 0


def margin_weight(i,j,n):
    # The Fourier functional is applied only after ordinary multiplication.
    hi=lambda k:fourier_monomial(i,k)
    hj=lambda k:fourier_monomial(j,k)
    return (127*hi(n)*hj(n)-128*hi(n-1)*hj(n+1)
            -128*hi(n+1)*hj(n+1)+128*hi(n)*hj(n+2))


def main():
    started=time.monotonic()
    local=[local_tensor(a,b) for a in range(3) for b in range(3)]
    local_laurent_masses=[sum(int(tensor[i,j])*2**(i+j)
                              for i in range(3) for j in range(3))
                           for tensor in local]
    assert max(local_laurent_masses)==local_laurent_masses[8]==17956
    local_terms=[[(i,j,int(tensor[i,j])) for i in range(3) for j in range(3)
                  if tensor[i,j]] for tensor in local]
    # Symmetry of the x,z polynomial lets us combine its two off-diagonal
    # monomials. Opposite parities have zero Fourier-functional weight.
    indices=[(i,j) for i in range(17) for j in range(i,17) if (i-j)%2==0]
    assert len(indices)==81
    rows=np.array([i for i,j in indices],dtype=int)
    cols=np.array([j for i,j in indices],dtype=int)
    weights=np.array([[margin_weight(i,j,n)+(margin_weight(j,i,n) if i!=j else 0)
                       for i,j in indices] for n in range(17)],dtype=object)
    # Independently check the support/parity reduction of the functional.
    assert all(margin_weight(i,j,n)==0 for i in range(17) for j in range(17)
               if (i-j)%2 for n in range(17))

    minima=[None]*17
    witnesses=[None]*17
    count=[0]*9
    cases=negative=zero=0
    def visit(depth,first,ordinary):
        nonlocal cases,negative,zero
        if depth==8:
            cases+=1
            margins=weights @ ordinary[rows,cols]
            for n,raw in enumerate(margins):
                value=int(raw)
                negative+=value<0
                zero+=value==0
                if minima[n] is None or value<minima[n]:
                    minima[n]=value
                    witnesses[n]=list(count)
            return
        width=ordinary.shape[0]
        for label in range(first,9):
            child=np.zeros((width+2,width+2),dtype=object)
            for i,j,coefficient in local_terms[label]:
                child[i:i+width,j:j+width]+=ordinary*coefficient
            count[label]+=1
            visit(depth+1,label,child)
            count[label]-=1

    visit(0,0,np.array([[1]],dtype=object))
    assert cases==comb(16,8)==12870
    bound=513*17956**8
    assert bound<2**126<2**127
    result={
        'status':'PASS' if negative==zero==0 else 'FAIL',
        'method':'independent ordinary x,z multiplication, rational Bernstein definition, final binomial Fourier functional',
        'arithmetic':'Python arbitrary-precision integers; NumPy dtype=object',
        'patterns':cases,'distinct_Bernstein_margins':17*cases,
        'negative_coefficients':negative,'zero_coefficients':zero,
        'represented_full_tensor_coefficients':17*3**16,
        'scaling':'64^8 times the Bernstein coefficient of 128 delta_n(P)-H(P)_n^2',
        'local_ordinary_tensors':[[list(map(int,row)) for row in tensor] for tensor in local],
        'local_laurent_coefficient_sums':local_laurent_masses,
        'minimum_by_index':[{'n':n,'minimum':str(value),'histogram':witnesses[n]}
                            for n,value in enumerate(minima)],
        'author_overflow_bound':str(bound),'author_overflow_bound_bits':bound.bit_length(),
        'bound_below_minimum_initializer':bound<2**126,
        'elapsed_seconds':time.monotonic()-started}
    print(json.dumps(result,indent=2))
    assert negative==zero==0


if __name__=='__main__':
    main()
