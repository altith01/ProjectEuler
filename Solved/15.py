# Lattice Paths :)

import math


def binomial(n, k):
    return math.factorial(n)//math.factorial(n-k)//math.factorial(k)


def num_paths(x, y):
    return binomial(x+y, x)


grid_dimensions = [20, 20]

print(num_paths(grid_dimensions[0],
                grid_dimensions[1]))
