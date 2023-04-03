# Eulercoin


def gcd(x, y):
    z = max(x,y) % min(x,y)
    if z == 0:
        return min(x,y)
    else:
        return gcd(z, min(x,y))


def modular_inverse(a, n):
    d = gcd(a, n)
    if d != 1:
        return
    n0 = n
    x = 1
    y = 0
    # Want ax+yn=1
    while a > 1:
        q = a // n
        t = n
        n = a % n
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + n0
    return x


c = 1504170715041707
m = 4503599627370517
i = modular_inverse(c, m)
previous = c
total = c
value = c

count = 19
tracker = 0
# n = 1
# data = [(1,c)]

# while count:
#     value = (value + c) % m
#     n += 1
#     effect = value - c
#     if effect < 0 and effect > data[-1][1]:
#         data.append((n, effect))

while count:
    value = (value + c) % m
    if value < previous:
        print(f"{19-count}\t{value}")
        count -= 1
        change = value - previous
        previous = value
        total += value
        while value + change > 0:
            value += change
            previous = value
            total += value
            print(f"{19-count}\t{value}")
            count -= 1
