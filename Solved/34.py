# Digit factorials

# Little slow...

import math


def factorial_sum(n):
    if n // 10 == 0:
        return math.factorial(n)
    else:
        return math.factorial(n % 10) + factorial_sum(n // 10)


cap = 10000000

numbers = []

for number in range(3, cap):
    if factorial_sum(number) == number:
        numbers.append(number)

print(numbers)
print(sum(numbers))
