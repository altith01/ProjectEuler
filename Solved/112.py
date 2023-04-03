# Bouncy numbers

def isBouncy(n):
    if n < 100:
        return False
    increasing = True
    decreasing = True
    old_digit = n%10
    n = n//10
    while n and (increasing or decreasing):
        new_digit = n%10
        if new_digit < old_digit:
            decreasing = False
        if old_digit < new_digit:
            increasing = False
        old_digit = new_digit
        n //= 10
    return not (increasing or decreasing)

x=0
bouncy_count = 0
while True:
    x += 1
    if isBouncy(x):
        bouncy_count += 1
    if x % 100 == 0:
        # if x % 1000 == 0:
            # print(x, bouncy_count/x)
        if bouncy_count/x == 0.99:
            print(x)
            quit()

        