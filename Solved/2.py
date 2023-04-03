# Even Fibonacci Numbers

# Could optimize with a non-recursive fibonacci formula

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def find_stop(stop_value):
    n = 0
    while fibonacci(n) <= stop_value:
        n += 1
    return n


answer = 0

for num in range(2, find_stop(4000000), 3):
    answer += fibonacci(num)

print(answer)
