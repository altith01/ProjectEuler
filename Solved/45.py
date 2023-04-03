# Triangluar, pentagonal, and hexagonal

import math


def is_triangle(n):
    new = int(math.sqrt(2 * n))
    if (new * (new + 1)) / 2 == n:
        return True
    else:
        return False


def is_pentagon(n):
    x = round((1 + math.sqrt(1 - 4 * 3 * (-2) * n)) / (2 * 3))
    if 0 < n == (x * (3 * x - 1)) // 2:
        return True
    else:
        return False


def is_hexagon(n):
    x = round((1 + math.sqrt(1 - 4 * 2 * (-1) * n)) / (2 * 2))
    if 0 < n == (x * (2 * x - 1)):
        return True
    else:
        return False


def t(n):
    return (n * (n + 1)) // 2


def h(n):
    return n * ((2 * n) - 1)


ans = 144

while not (is_triangle(h(ans)) and is_pentagon(h(ans))):
    ans += 1

print(h(ans))
