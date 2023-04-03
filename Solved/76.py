# Counting summations
from time import time_ns
start = time_ns()

full_data = dict({
    1:[0],
    2:[1,1],
    3:[2,1,1]
})

for n in range(4, 101):
    data = [0]
    for i in range(1, (n+1)//2):
        value = sum(full_data[n-i][1:i+1])
        data.append(value)
        data[0] += value
    if n % 2 == 0:
        value = full_data[n//2][0] + 1
        data.append(value)
        data[0] += value
    remaining = full_data[n-1][n//2:]
    data += remaining
    data[0] += sum(remaining)
    full_data.update({
        n: data
    })


answer = full_data[100][0]
elapsed = (time_ns() - start)/1000000
print(answer)
print(elapsed, "ms")
