# Digit factorial chains

from math import factorial
from time import time_ns

start_time = time_ns()
three_cycle = set((169, 363601, 1454))
two_cycle = set((871, 45361, 872, 45362))


def next_in_chain(n):
    next = 0
    while n > 0:
        next += factorial(n % 10)
        n //= 10
    return next


def chain_length(n):
    length = 1
    while 1:
        if n in three_cycle:
            return length + 2
        if n in two_cycle:
            return length + 1
        previous = n
        n = next_in_chain(n)
        if n == previous:
            return length
        length += 1

count = 0
second_terms_success = set()
second_terms_fail = set()
for n in range(1000000):
    second_term = next_in_chain(n)
    if second_term in second_terms_success:
        count += 1
    elif second_term in second_terms_fail:
        pass
    elif chain_length(n) == 60:
        count += 1
        second_terms_success.add(second_term)
        # print(n)
    else:
        second_terms_fail.add(second_term)

elapsed = (time_ns() - start_time)/1000000
print(f"Total: {count}")
print(elapsed, "ms")