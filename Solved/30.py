# Digit Fifth Powers

def fifth_sum(n):
    if n // 10 == 0:
        return n**5
    else:
        return (n % 10)**5 + fifth_sum(n // 10)


numbers = []

for num in range(2, 1000000):
    if num == fifth_sum(num):
        numbers.append(num)

print(numbers)
print(sum(numbers))
