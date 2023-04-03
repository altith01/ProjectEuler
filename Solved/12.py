# Highly divisible triangular number

import math


def t(n):
    return n*(n+1)//2


def num_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            count += 2
    if n % math.sqrt(n) == 0:
        count += 1
    return count


answer_index = 1

while not num_divisors(t(answer_index)) > 500:
    answer_index += 1

print(t(answer_index))
