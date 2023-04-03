# Prime Permutations
# could make improvements

from UsefulStuff.PrimeGenerator import *
from UsefulStuff.DecreasingPandigitals import *


primes = get_primes(9999)


def permutations(n):
    num = str(n)
    c = []
    for char in num:
        c.append(char)
    c.sort(reverse=True)
    key = '4321'
    perms = []
    while len(key)>3:
        candidate = int(c[int(key[0]) - 1] + c[int(key[1]) - 1] + c[int(key[2]) - 1] + c[int(key[3]) - 1])
        if candidate in primes and candidate>999:
            perms.append(candidate)
        key = next_pandigital(key)
    return perms


def increasing(n):
    num = str(n)
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True


for prime in primes:
    if prime < 1000:
        pass
    else:
        test = permutations(prime)
        for i in range(len(test)-2):
            for j in range(i+1, len(test)-1):
                if test[i] != test[j] and 2 * test[j] - test[i] in test:
                    print(str(test[i]) + str(test[j]) + str(2 * test[j] - test[i]))
