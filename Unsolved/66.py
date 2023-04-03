# Diophantine equation
import sys
sys.path.append(".")
import math
from UsefulStuff.PolygonNumbers import is_square

X = 0
D = 0
for d in range(1, 1001):
    if is_square(d):
        pass
    else:
        y = 1
        x2 = d * (y ** 2) + 1
        while not is_square(x2):
            y += 1
            x2 = d*(y**2)+1
        x = math.sqrt(x2)
        if x > X:
            X = x
            D = d
        print(D, d, x)
print(D)
