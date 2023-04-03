# Convergents of e

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))


def nth_convergent(n):
    num = 1
    denom = 0
    for i in range(n, 0, -1):
        num, denom = denom, num
        if i == 1:
            a = 2
        elif i % 3 == 0:
            a = (i//3)*2
        else:
            a = 1
        num = a * denom + num
    return num, denom


def sum_digits(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s


print(sum_digits(nth_convergent(100)[0]))
