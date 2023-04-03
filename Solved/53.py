# Combinatoric selections


def ncr(n, r):
    val = 1
    while r > 0:
        val *= (n - (r - 1)) / r
        r -= 1
    return int(val)


count = 0
for n in range(1, 101):
    mid = n/2
    for r in range(1, n):
        if r > mid:
            pass
        else:
            if ncr(n, r) > 1000000:
                count += (int(mid + 0.5) - 1 - (r - 1)) * 2
                if mid % 1 == 0:
                    count += 1
                break

print(count)
