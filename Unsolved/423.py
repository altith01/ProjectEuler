# Consecutive die throws
from math import comb

def a(n, c):
    return comb(n-1, n-1-c)*6*(5**(n-1-c))

def pi(n):
    ...

def C(n):
    ...

def S(L):
    ...
