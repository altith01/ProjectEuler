# Double-base Palindromes

def d_to_b(n):
    return bin(n)[2:]


def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-i-1]:
            return False
    return True


ans = 0

for number in range(1000000):
    if is_palindrome(str(number)) and is_palindrome(d_to_b(number)):
        ans += number

print(ans)