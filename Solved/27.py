# Quadratic primes

from UsefulStuff.PrimeGenerator import *


def is_prime(num, p_list):
    for p in p_list:
        if p > math.sqrt(num):
            return True
        elif num % p == 0:
            return False
    return True


primes = get_primes(1000)

ans = (0, 0, 0)

for b in primes:
    for a in range(-999, 1000, 1):
        n = 0
        candidate = n ** 2 + a * n + b
        while candidate > 1 and is_prime(candidate, primes):
            n += 1
            candidate = n ** 2 + a * n + b
        if n > ans[2]:
            ans = (a, b, n)

print(ans)
print(ans[0] * ans[1])
