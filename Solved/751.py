# Concatenation Coincidence

from decimal import Decimal
from time import time_ns

START_TIME = time_ns()

def b(theta, n):
    result = theta
    while n > 1:
        result = b_n(result)
        n -= 1
    return result

def b_n(previous):
    return Decimal(int(previous) * (Decimal(previous) - int(previous) + 1))

def a_n(b_n):
    return int(b_n)

def expected_a(theta, a_list):
    current_length = 0
    for a in a_list:
        current_length += len(str(a))
    num_string = str(theta).replace(".", "")
    num_string = num_string[current_length:]

def theta_a(theta, a):
    if theta == 2:
        return Decimal(str("2.") + str(a))
    else:
        return Decimal(str(theta) + str(a))

def tau(a_list):
    return Decimal(str(str(a_list[0]) + "." + "".join(str(x) for x in a_list[1:])))

theta = 2
a_list = [a_n(theta)]
n = 2
a = 2

while len(str(tau(a_list))) < 26:
    while a < a_n(b(theta_a(theta, a), n)):
        a += 1
    a_list.append(a)
    theta = theta_a(theta, a)
    n += 1
    # print(a, theta, tau(a_list))
elapsed = (time_ns()-START_TIME)/1000000
print(elapsed, "ms")
print(theta)
# print(tau(a_list))
# print(theta == tau(a_list))
# print(len(str(theta)))