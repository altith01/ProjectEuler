# Large non-Mersenne prime

import time

t1 = time.time()*1000

e = 7830457
a = 28433

pieces = {}

power = 1
pieces.update({0: 2})
pieces.update({1: 4})
while 2 ** (power + 1) < e:
    power += 1
    pieces.update({power: (pieces[power-1] ** 2) % (10 ** 10)})
answer = 1

thing = e
while 1 == 1:
    other = 2 ** power
    if other <= thing:
        answer *= pieces[power]
        thing -= other
    if power == 0:
        break
    else:
        power -= 1
answer *= a
answer += 1
print(answer % 10 ** 10)

print(t1 - time.time()*1000)
print(t1 == time.time()*1000)
