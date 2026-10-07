#!/usr/bin/env python3
"""Exact symmetric Laurent arithmetic with certified carry-free convolution."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def get(h,n):
    return h[abs(n)] if abs(n)<len(h) else 0


def add(h,k):
    return [get(h,n)+get(k,n) for n in range(max(len(h),len(k)))]


def scale(h,c):
    return [c*v for v in h]


def times_y(h):
    return [get(h,n-1)+get(h,n)+get(h,n+1) for n in range(len(h)+1)]


def delta(h,n):
    return get(h,n)**2-get(h,n-1)*get(h,n+1)-get(h,n+1)**2+get(h,n)*get(h,n+2)


def positive_convolution(a,b):
    """Return ordinary convolution exactly, with a proved no-carry width."""
    assert all(v>=0 for v in a+b) and max(a)>0 and max(b)>0
    bits=max(a).bit_length()+max(b).bit_length()+min(len(a),len(b)).bit_length()
    width=(bits+7)//8
    assert min(len(a),len(b))*max(a)*max(b)<1<<(8*width)
    pack=lambda p:int.from_bytes(b''.join(v.to_bytes(width,'little') for v in p),'little')
    n=len(a)+len(b)-1
    raw=(pack(a)*pack(b)).to_bytes(width*n,'little')
    return [int.from_bytes(raw[i*width:(i+1)*width],'little') for i in range(n)]


def multiply(h,k):
    full_h=list(reversed(h[1:]))+h
    full_k=list(reversed(k[1:]))+k
    out=positive_convolution(full_h,full_k)
    degree=len(h)+len(k)-2
    assert out==list(reversed(out))
    return out[degree:]


def digest(values):
    h=sha256()
    for v in values:h.update((str(v)+'\n').encode())
    return h.hexdigest()


