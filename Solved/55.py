# Lychrel Numbers

def is_palindrome(n):
    num = str(n)
    num1 = num[:len(num)//2]
    num2 = (num[-(len(num)//2):])[::-1]
    if num1 == num2:
        return True
    else:
        return False

def is_lychrel(n):
    c = 0
    while c < 50:
        n = n + int((str(n))[::-1])
        if is_palindrome(n):
            return False
        c += 1
    return True

count = 0
for x in range(1, 10001):
    if is_lychrel(x):
        count += 1

print(count)
