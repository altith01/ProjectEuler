# Odd period square roots
# Kinda slow

from UsefulStuff.PolygonNumbers import is_square
import math
import time

t1 = time.time()*1000

def period(N):
    if is_square(N):
        return 0
    index = 0
    steps = {}
    a = math.floor(math.sqrt(N))
    d = N - a ** 2
    n = math.floor((math.sqrt(N) + a)/d)
    s = a - n * d
    steps.update({index: (a, d, n, s)})
    while True:
        index += 1
        a = n
        d = (N - s ** 2) // d
        n = math.floor((math.sqrt(N) - s) / d)
        s = -s - n * d
        for i in range(index):
            if steps[i] == (a, d, n, s):
                return index - i
        steps.update({index: (a, d, n, s)})


count = 0
for N in range(2, 10000):
    if period(N) % 2 == 1:
        count += 1
print(count)

print()
print(round(time.time()*1000 - t1,3), "milliseconds")
