# Bitwise-OR operations on random integers
from time import time_ns
from math import comb

start_time = time_ns()

data = [[1] + [0]*32]
other_data = [[sum(data[0][0:-1]), data[0][-1]]]
distribution = [0]
for n in range(50):
    data.append([0]*33)
    for i in range(33):
        for j in range(33-i):
            data[-1][i + j] += comb(32-i, j)*data[-2][i]/2**(32-i)
    other_data.append([sum(data[-1][0:-1]), data[-1][-1]])
    distribution.append(other_data[-1][1]-other_data[-2][1])
    # print(n+1, other_data[-1], distribution[-1])

ans = round(sum([i*distribution[i] for i in range(len(distribution))])/sum(distribution), 10)
elapsed = (time_ns() - start_time) / 1000000
print(ans)
print(elapsed, "ms")



# import random
# Testing - value should be ~6.35
# results = []
# for _ in range(100000):
#     x = 0
#     n = 0
#     while x < 2**32-1:
#         y = random.randint(0, 2**32-1)
#         x = x|y
#         n += 1
#     results.append(n)
# print(sum(results)/len(results))
