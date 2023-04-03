# Totient maximum

from UsefulStuff.PrimeGenerator import get_primes

primes = get_primes(1000)


def phi(n):
    prime_list = get_primes(n + 1)
    value = n
    for p in prime_list:
        if n/p == n//p:
            value *= (1 - 1/p)
    return round(value)


number = 1
for prime in primes:
    if number * prime > 1000000:
        break
    else:
        number *= prime
totient = phi(number)
print(number, totient, number/totient)
