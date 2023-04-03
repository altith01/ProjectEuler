# Pandigital Prime

from UsefulStuff.DecreasingPandigitals import *
from UsefulStuff.PrimeGenerator import *

primes = get_primes(int(math.sqrt(987654321)) + 1)


def is_prime(n):
    for p in primes:
        if p > math.sqrt(n) + 1:
            break
        if n % p == 0:
            return False
    return True


pandigital = '987654321'

while not is_prime(int(pandigital)):
    pandigital = next_pandigital(pandigital)

print(pandigital)
