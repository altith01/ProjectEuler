# Largest Prime Factor

# Really slow lol

import math


def get_primes(n):
    prime_list = []
    for num in range(2, n + 1, 1):
        if num == 2:
            prime_list.append(num)
        else:
            is_prime = True
            for prime in prime_list:
                if num % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(num)
    return prime_list


answer = 600851475143

primes = get_primes(int(math.sqrt(answer)))

can_divide = True

while can_divide:
    divided = False
    for prime in primes:
        if answer % prime == 0 and answer > prime:
            answer /= prime
            print(int(answer))
            divided = True
            break
    if not divided:
        can_divide = False
