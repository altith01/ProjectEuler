# Coin partitions

# def p(n):
#     if n == 0:
#         return 1
#     else:
#         value = 1
#         for _ in range(n):
#             value = p_n(value)

# def p_n(previous):



from time import time_ns
start = time_ns()

full_data = dict({
    1:[0],
    2:[1,1],
    3:[2,1,1]
})

n = 4
while 1:
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
    print(data[0])
    if data[0]+1 % 1000000 == 0:
        answer = n
        break
    full_data.update({
        n: data
    })
    n += 1


elapsed = (time_ns() - start)/1000000
print(answer)
print(elapsed, "ms")
