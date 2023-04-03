# Digit cancelling fractions

# from UsefulStuff.PrimeGenerator import *


# def reduce(n, d, p):
#    for i in range(len(p)):
#        if p[i] > n or p[i] > d:
#            break
#        if n % p[i] == 0 and d % p[i] == 0:
#            return reduce(n//p[i], d//p[i], p)
#    return [n, d]

# ^^^too slow...

def cancel_digit(n, d):
    n1 = n//10
    n2 = n % 10
    d1 = d//10
    d2 = d % 10
    if n1 == d1:
        return n2, d2
    elif n1 == d2:
        return n2, d1
    elif n2 == d1:
        return n1, d2
    elif n2 == d2 and n2 != 0:
        return n1, d1


examples = []

for denominator in range(10, 100):
    for numerator in range(10, denominator):
        cancelled = cancel_digit(numerator, denominator)
        if cancelled is not None and cancelled[1] != 0 and cancelled[0]/cancelled[1] == numerator / denominator:
            examples += [(numerator, denominator)]

print(examples)

ans = [1, 1]

for example in examples:
    ans[0] *= example[0]
    ans[1] *= example[1]

print(ans)
