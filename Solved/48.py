# Self powers

answer = 0

for x in range(1,1001):
    new = x**x
    answer += new

answer = str(answer)
print(answer[-10:])
