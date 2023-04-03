# Consecutive prime sum
# could improve

from UsefulStuff.PrimeGenerator import *


primes = get_primes(999999)

max = 1
ans = 0

for i in range(len(primes)):
    for j in range(i+max-1, len(primes)):
        if j-i+1>max:
            new = sum(primes[i:j])
            if new > 999999:
                break
            if new in primes:
                max = j-i+1
                ans = new

print(ans,max)
