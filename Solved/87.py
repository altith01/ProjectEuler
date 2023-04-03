# Prime power triples
# Not sure if there is a fancy better way

from math import sqrt
import sys
from time import time_ns
sys.path.append(".")
from UsefulStuff.PrimeGenerator import get_primes2

start_time = time_ns()

BOUND = 50000000
primes = get_primes2(int(sqrt(BOUND)))
numbers = set()

for four in primes:
    if four**4 > BOUND:
        break
    for three in primes:
        if four**4 + three**3 > BOUND:
            break
        for two in primes:
            candidate = four**4 + three**3 + two**2
            if candidate > BOUND:
                break
            else:
                numbers.add(candidate)

elapsed = (time_ns() - start_time) / 1000000
print(len(numbers))
print(elapsed, "ms")
