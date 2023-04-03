# Stealthy Numbers

# a + b = c + d + 1
# can show that a < c <= d < b
# let (d = c + x1) and (a = c - x2) [implies that b = c + x1 + x2 + 1]
# can show that c = x2 * (1 + x1 + x2)

# Figure out how to account for duplicates... 
# then could use an integral over complicated function and subtract out duplicates

from time import time_ns
start_time = time_ns()

x1 = 0
x2 = 1
N = 10 ** 6
stealthy_numbers = set()
count = 0
p = 0
while 1:
    while 1:
        c = x2 * (1 + x1 + x2)
        d = c + x1
        cd = c*d
        if cd > N:
            break
        else:
            if cd in stealthy_numbers:
                p+=1
                print(p, cd)
            stealthy_numbers.add(cd)
            count += 1
        x2 += 1
    if x2 == 1:
        break
    x2 = 1
    x1 += 1

elapsed = (time_ns() - start_time) / 1000000
print(len(stealthy_numbers), count)
print(elapsed, "ms")
