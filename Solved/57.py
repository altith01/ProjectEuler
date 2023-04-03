# Square root convergents

def next_iteration(n):
    return 2 * n[1] + n[0], n[0] + n[1]


c = 0
ans = 0
approx = 3, 2
while c < 1000:
    approx = next_iteration(approx)
    if len(str(approx[0])) > len(str(approx[1])):
        ans += 1
    c += 1
print(ans)
