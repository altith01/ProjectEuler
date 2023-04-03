
import math


def f(n):
    Phi = (1 + math.sqrt(5)) / 2
    phi = (1 - math.sqrt(5)) / 2
    return int((Phi**n - phi**n) / math.sqrt(5))
