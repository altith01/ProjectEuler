# Integer Right Triangles

import math

p_cap = 1000

a_cap = p_cap/(2+math.sqrt(2))

integral_perimeters = {}

for a in range(1, int(a_cap)+1):
    b = a
    c = round(math.sqrt(a ** 2 + b ** 2))
    while a + b + c <= 1000:
        if a ** 2 + b ** 2 == c ** 2:
            try:
                integral_perimeters[a + b + c] += [(a, b, c)]
            except KeyError:
                integral_perimeters.update({a + b + c: [(a, b, c)]})
        b += 1
        c = round(math.sqrt(a ** 2 + b ** 2))

ans = [0, []]

for key in integral_perimeters:
    if len(integral_perimeters[key]) > len(ans[1]):
        ans[0] = key
        ans[1] = integral_perimeters[key]

print(ans)
