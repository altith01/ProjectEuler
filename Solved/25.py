# 1000- digit fibonacci number

import math


def f(n):
    Phi = (1 + math.sqrt(5)) / 2
    phi = (1 - math.sqrt(5)) / 2
    return (n*(math.log10(Phi)) - math.log10(math.sqrt(5)),
            n*(math.log10(-phi)) - math.log10(math.sqrt(5)))


ans = 1
count = 0
print(f(ans))
while f(ans)[0] < 999:
    print(ans)
    print(f(ans))
    ans += 1

print(ans)
