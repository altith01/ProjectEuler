import math


def triangle(n):
    return n*(n+1)//2


def is_triangle(n):
    t = math.floor(math.sqrt(n*2))
    return triangle(t) == n


def square(n):
    return n**2


def is_square(n):
    t = round(math.sqrt(n))
    return square(t) == n


def pentagon(n):
    return n*(3*n-1)//2


def is_pentagon(n):
    t = math.ceil(math.sqrt(n*2/3))
    return pentagon(t) == n


def hexagon(n):
    return n*(2*n-1)


def is_hexagon(n):
    t = math.ceil(math.sqrt(n/2))
    return hexagon(t) == n


def heptagon(n):
    return n*(5*n-3)//2


def is_heptagon(n):
    t = math.ceil(math.sqrt(n*2/5))
    return heptagon(t) == n


def octagon(n):
    return n*(3*n-2)


def is_octagon(n):
    t = math.ceil(math.sqrt(n/3))
    return octagon(t) == n
