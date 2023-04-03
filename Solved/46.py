# Goldbach's other conjecture

from UsefulStuff.PrimeGenerator import *


def works(n, p):
    x = 0
    while n - 2 * x ** 2 > 1:
        if n - 2 * x ** 2 in p:
            return True
        x += 1
    return False


a = 1000

primes = get_primes(a)

ans = 3

while works(ans, primes):
    ans += 2
    if ans > a:
        a *= 10
        primes = get_primes(a)

print(ans)
