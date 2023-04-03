# Pentagonal Numbers

import math


def p(n):
    return (n * (3 * n - 1)) // 2


def is_pentagonal(n):
    x = round((1 + math.sqrt(1 - 4 * 3 * (-2) * n)) / (2 * 3))
    if 0 < n == (x * (3 * x - 1)) // 2:
        return True
    else:
        return False


a = 1
done = False

while not done:
    for b in range(a-1, 0, -1):
        if is_pentagonal(p(a) + p(b)) and is_pentagonal(p(a) - p(b)):
            print(a, b, p(a), p(b), p(a) - p(b))
            done = True
    a += 1
