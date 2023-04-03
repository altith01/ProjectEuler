# Square root digital expansion

from decimal import *
from math import sqrt
from time import time_ns
getcontext().prec = 111

start_time = time_ns()

digits = ""
root = Decimal(1)
for n in range(1, 101):
    if int(sqrt(n))**2 != n:
        root = Decimal(int(root))
        for d in range(102):
            while root**2 < n:
                root += Decimal(1/10**(d))
            root -= Decimal(1/10**(d))
        digits += str(root)[0:101].replace(".", "")
    else:
        root = Decimal(int(sqrt(n)))

total = sum(int(x) for x in digits)
elapsed = (time_ns() - start_time) / 1000000
print(total)
print(elapsed, "ms")
