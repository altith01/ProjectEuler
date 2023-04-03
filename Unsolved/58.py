# Spiral primes
# Slow :(

import sys
sys.path.append(".")
from UsefulStuff.PrimeGenerator import *

n = 1
c = 0
p = 0
t = 1
BOUND = 690000000
primes = get_primes2(BOUND)

print("Let's get it")

while True:
    c += 2
    for i in range(3):
        n += c
        t += 1
        if is_prime(primes, 0, len(primes)-1, n):
        # if is_prime4(n):
            p += 1
    n += c
    t += 1
    if n > BOUND:
        print("Choose bigger bound")
        break
    if p/t < 0.1:
        print(c + 1)
        break
print("done")
