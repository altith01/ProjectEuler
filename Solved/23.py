# Non-abundant Sums

import math


def d(n):
    total = 1
    for div in range(2, int(math.sqrt(n)) + 1):
        if div**2 == n:
            total += div
        elif n % div == 0:
            total += div
            total += n//div
    return total


def is_abundant(n):
    if n < d(n):
        return True
    else:
        return False


abundants = []

for i in range(1, 28123):
    if is_abundant(i):
        abundants.append(i)

sums = {}

for index in range(len(abundants)):
    for addend in abundants[index:]:
        if (abundants[index]+addend) > 28123:
            break
        sums.update({abundants[index]+addend: abundants[index]+addend})

answer = 0

for i in range(1, 28123):
    try:
        sums[i]
    except KeyError:
        answer += i

print(answer)
