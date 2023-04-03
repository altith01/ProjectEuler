# Sub-string divisibility

from UsefulStuff.DecreasingPandigitals import *

primes = [2, 3, 5, 7, 11, 13, 17]
specials = []
pandigital = '9876543210'

while len(pandigital) == 10:
    for i in range(len(primes)):
        is_special = True
        if int(pandigital[i + 1:i + 4]) % primes[i] != 0:
            is_special = False
            break
    if is_special:
        specials.append(pandigital)
    pandigital = next_pandigital(pandigital)

ans = 0

for special in specials:
    ans += int(special)

print(ans)
