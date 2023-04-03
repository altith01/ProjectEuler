# Pandigital products

import math


def nine_pandigital(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    comb = a+b+c
    if len(comb) == 9:
        if '1' in comb and '2' in comb and '3' in comb and \
                '4' in comb and '5' in comb and '6' in comb and \
                '7' in comb and '8' in comb and '9' in comb:
            return True
        else:
            return False
    else:
        return False


products = {}

for a in range(1, 99):
    for b in range(111, 9999):
        c = a*b
        if int(math.log10(a)) + int(math.log10(b)) + int(math.log10(c)) + 3 > 9:
            break
        if nine_pandigital(a, b, c):
            products.update({c: c})

ans = 0

for product in products:
    ans += product

print(ans)
