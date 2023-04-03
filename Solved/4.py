# Largest Palindromic Product

# :)

def is_palindrome(n):
    if type(n) == int:
        n = str(n)
    if len(n) < 2:
        return True
    elif n[-1] == n[0]:
        return is_palindrome(n[1:-1])
    else:
        return False


drome = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if is_palindrome(x*y):
            if x*y > drome:
                drome = x*y

print(drome)
