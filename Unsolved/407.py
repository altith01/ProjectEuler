# Idempotents
# Need tricks to find faster...
# Prime powers are all 1

sum = 0
for n in range (1, 10**4+1):
    for a in range(n//2 + 1):
        square = a**2 % n
        if square == n-a:
            value = square
            break
        elif square == a:
            value = square
    sum += value
    # print(n, value)
print(sum)