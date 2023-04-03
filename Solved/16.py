# Power digit sum

def digit_sum(n):
    if n//10 == 0:
        return n
    else:
        addend = n % 10
        return addend + digit_sum(n//10)


print(digit_sum(2**1000))
