# Multiples of 3 and 5

answer = 0

for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        answer += x

print(answer)
