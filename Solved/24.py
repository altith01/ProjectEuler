# Lexicographic Permutations

import math


def nth_lexicographic_permutation(n, ordered):
    string = ''
    remaining = ordered
    while len(remaining) > 0:
        string += str(remaining[((n-1) % math.factorial(len(remaining)))//math.factorial(len(remaining)-1)])
        remaining.pop(((n-1) % math.factorial(len(remaining)))//math.factorial(len(remaining)-1))
        print(string)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nth_lexicographic_permutation(1000000, digits)
