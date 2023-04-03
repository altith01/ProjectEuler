# Generates a list of all primes up to (and including) cap

import math


def get_primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n % 6+6, 2-(n % 6 > 1)
    sieve = [True] * (n//3)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i & 1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i & 1)+4)//6-1)//k+1)
    return [2, 3] + [3*i+1 | 1 for i in range(1, n//3-correction) if sieve[i]]


def is_prime2(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_prime(arr, low, high, n):
    if high >= low:
        mid = (low + high)//2
        val = arr[mid]
        if n == val:
            return True
        elif n < val:
            return is_prime(arr, low, mid - 1, n)
        else:
            return is_prime(arr, mid + 1, high, n)
    else:
        return False


def get_primes(cap):
    numbers = [[0, 0], [1, 0]]

    for n in range(2, cap):
        numbers.append([n, 1])

    primes = []

    for i in range(cap):
        if numbers[i][1] == 1:
            primes.append(numbers[i][0])
            if i < math.sqrt(cap) + 1:
                for j in range(2 * numbers[i][0], len(numbers), numbers[i][0]):
                    numbers[j][1] = 0

    return primes


def mod_exp(base, exponent, mod):
    ans = 1
    while exponent > 0:
        ans *= base
        ans %= mod
        exponent -= 1
    return ans


def is_prime4(n):
    if n < 2:
        return False
    if n in [2, 3, 5, 7, 11]:
        return True
    for i in [2, 3, 5, 7, 11]:
        if mod_exp(i, n-1, n) != 1:
            return False
    return True


# Use with BinarySearchTree sortedArrayToBST

def is_prime3(tree, candidate):
    if tree.data() == candidate:
        return True
    elif tree.data() > candidate and tree.left is not None:
        return is_prime(tree.left, candidate)
    elif tree.data() < candidate and tree.right is not None:
        return is_prime(tree.right, candidate)
    else:
        return False

# Older, slower implementation...

# def get_primes(n):
#    if n < 2:
#        return []
#    p_list = [2]
#    for i in range(3, n + 1, 2):
#        is_p = True
#        for p in p_list[1:]:
#            if p > math.sqrt(i) + 1:
#                break
#            if i % p == 0:
#                is_p = False
#                break
#        if is_p:
#            p_list.append(i)
#    return p_list
