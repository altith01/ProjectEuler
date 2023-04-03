# Amicable Numbers

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


def amicable(n):
    if n == d(d(n)) and n != d(n):
        return True
    else:
        return False


answer = 0

for i in range(1, 10001):
    if amicable(i):
        print(i)
        answer += i

print(answer)
