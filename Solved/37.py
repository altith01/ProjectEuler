# Truncatable Primes

from UsefulStuff.PrimeGenerator import *


primes = get_primes(1000000)


def is_prime(n):
    if n < 2:
        return False
    for p in primes:
        if p >= int(math.sqrt(n)) + 1:
            break
        if n % p == 0:
            return False
    return True


def left_truncatable(p):
    x = p
    while x > 0:
        if not is_prime(x):
            return False
        x = x % 10**int(math.log10(x))
    return True


def right_truncatable(p):
    x = p
    while x > 0:
        if not is_prime(x):
            return False
        x = x // 10
    return True


truncatables = []
count = 0

for prime in primes:
    if prime > 10:
        if left_truncatable(prime) and right_truncatable(prime):
            truncatables.append(prime)
            count += 1
    if count == 11:
        break

print(truncatables)
print(sum(truncatables))
