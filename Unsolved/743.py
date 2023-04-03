# Window into a Matrix
from math import factorial
from mod import Mod
from time import time_ns

MOD = 1000000007

def comb(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))
                         
# function assumes that k divides n
def A(k, n):
    return int(sum((Mod(comb(k, 2*l),MOD) * Mod(comb(2*l, l),MOD) * Mod(2,MOD)**(int(n / k)*(k - 2*l))) for l in range(k//2 + 1)))

start_time = time_ns()
ans = A(10**3, 10**16)
elapsed = (time_ns() - start_time) / 1000000
print(ans)
print(elapsed, "ms")