# circular primes

from UsefulStuff.PrimeGenerator import *


cap = 1000000

primes = get_primes(cap)

primes1 = [2]

for prime in primes:
    string = str(prime)
    if '2' not in string and '4' not in string and '6' not in string and '8' not in string and '0' not in string:
        primes1.append(prime)

circulars = []

for prime in primes1:
    string = str(prime)
    length = len(string)
    circular = True
    while length > 1:
        string = string[1:] + string[0]
        if int(string) not in primes:
            circular = False
            break
        length -= 1
    if circular:
        circulars.append(prime)

print(circulars)
print(len(circulars))
