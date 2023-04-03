# Number spiral diagonals

step = 2
num = 1
ans = 1

while step < 1001:
    i = 0
    while i < 4:
        num += step
        ans += num
        i += 1
    step += 2

print(ans)
