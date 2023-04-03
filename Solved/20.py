# Factorial Digit Sum

import math


def sum_digits(n):
    if n//10 == 0:
        return n
    else:
        return n % 10 + sum_digits(n//10)


print(sum_digits(math.factorial(100)))

