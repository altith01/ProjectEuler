# Special Pythagorean Triplet

import math

target_sum = 1000

for b in range(target_sum//2):
    for a in range(1, b):
        c = math.sqrt(a**2 + b**2)
        if c - int(c) == 0 and a+b+c == 1000:
            c = int(c)
            print((a, b, c))
            print("Sum: ", a+b+c)
            print("Product: ", a*b*c)
