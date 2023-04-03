# Coin Sums

# Probably could have done this nicer...

def coins(n, c):
    if n == 0:
        return 1
    elif n <= 1:
        return coins(n-1, 1)
    elif n <= 2:
        if c < 2:
            return coins(n - 1, 1)
        else:
            return coins(n - 2, 2) + coins(n - 1, 1)
    elif n <= 5:
        if c < 2:
            return coins(n - 1, 1)
        elif c < 5:
            return coins(n - 2, 2) + coins(n - 1, 1)
        else:
            return coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
    elif n <= 10:
        if c < 2:
            return coins(n - 1, 1)
        elif c < 5:
            return coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 10:
            return coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        else:
            return coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
    elif n <= 20:
        if c < 2:
            return coins(n - 1, 1)
        elif c < 5:
            return coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 10:
            return coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 20:
            return coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        else:
            return coins(n - 20, 20) + coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
    elif n <= 50:
        if c < 2:
            return coins(n - 1, 1)
        elif c < 5:
            return coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 10:
            return coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 20:
            return coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 50:
            return coins(n - 20, 20) + coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        else:
            return coins(n - 50, 50) + coins(n - 20, 20) + coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + \
                   coins(n - 1, 1)
    elif n <= 100:
        if c < 2:
            return coins(n - 1, 1)
        elif c < 5:
            return coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 10:
            return coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 20:
            return coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 50:
            return coins(n - 20, 20) + coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 100:
            return coins(n - 50, 50) + coins(n - 20, 20) + coins(n - 10, 10) + coins(n - 5, 5) + coins(n - 2, 2) + \
                   coins(n - 1, 1)
        else:
            return coins(n - 100, 100) + coins(n - 50, 50) + coins(n - 20, 20) + coins(n - 10, 10) + coins(n - 5, 5) + \
                   coins(n - 2, 2) + coins(n - 1, 1)
    else:
        if c < 2:
            return coins(n - 1, 1)
        elif c < 5:
            return coins(n - 2, 2) + coins(n - 1, 1)
        elif c < 10:
            return coins(n-5, 5) + coins(n-2, 2) + coins(n-1, 1)
        elif c < 20:
            return coins(n-10, 10) + coins(n-5, 5) + coins(n-2, 2) + coins(n-1, 1)
        elif c < 50:
            return coins(n-20, 20) + coins(n-10, 10) + coins(n-5, 5) + coins(n-2, 2) + coins(n-1, 1)
        elif c < 100:
            return coins(n-50, 50) + coins(n-20, 20) + coins(n-10, 10) + coins(n-5, 5) + coins(n-2, 2) + coins(n-1, 1)
        elif c < 200:
            return coins(n-100, 100) + coins(n-50, 50) + coins(n-20, 20) + coins(n-10, 10) + coins(n-5, 5) + \
                   coins(n-2, 2) + coins(n-1, 1)
        else:
            return coins(n-200, 200) + coins(n-100, 100) + coins(n-50, 50) + coins(n-20, 20) + coins(n-10, 10) + \
                   coins(n-5, 5) + coins(n-2, 2) + coins(n-1, 1)


print(coins(200, 200))
