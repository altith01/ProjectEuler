# Distinct prime factors

from UsefulStuff.PrimeGenerator import *


def distinct_primes(n, c, p):
    f = []
    x = n
    while x != 1:
        for prime in p:
            if prime > math.sqrt(x) + 1:
                f.append(x)
                x = x//x
                break
            if x % prime == 0:
                x = x // prime
                if prime not in f:
                    f.append(prime)
                break
        if len(f) > c:
            return False
    if len(f) == c:
        return True
    else:
        return False


num = 1000
primes = get_primes(num)
ans = 1
count = 0

print(distinct_primes(134047, 4, get_primes(200000)))

while count < 4:
    ans += 1
    if distinct_primes(ans, 4, primes):
        count += 1
    else:
        count = 0
    if ans > num:
        num *= 10
        primes = get_primes(num)

print(ans - 3)
