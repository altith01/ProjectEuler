# Reciprocal cycles

def cycle(n, d):
    c = []
    while (n, n // d) not in c:
        c += [(n, n // d)]
        if n//d == 0:
            n = n*10
        else:
            n = (n % d)*10
    i = 0
    while c[i] != (n, n // d):
        i += 1
    return c[i:]


ans = [0, 0]

for denom in range(1, 1000):
    candidate = len(cycle(1, denom))
    if candidate > ans[1]:
        ans[0] = denom
        ans[1] = candidate

print(ans)
