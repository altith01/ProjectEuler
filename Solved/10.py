# Summation of Primes Below 2000000

from UsefulStuff.PrimeGenerator import*

up_to = 2000000

to_sum = get_primes(up_to - 1)

answer = 0

for num in to_sum:
    answer += num

print(answer)
