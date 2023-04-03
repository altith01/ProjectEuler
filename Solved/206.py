# Concealed Square
# Since 1-2-3-4-5-6-7-8-9-0 ends in a 0, it is divisible by 2 and 5.
# Since it is a square, then it must be (at least) twice divisible by 2 and 5.
# So the number is 1-2-3-4-5-6-7-8-900
# So we can look for the unique square 1-2-3-4-5-6-7-8-9

import math
import time


def build(list_of_numbers):
    value = 0
    position = 0
    for number in list_of_numbers:
        value += number * (10 ** position)
        position += 1
    return value


def is_digit_here(number, digit, position):
    return (number % 10**(position+1)) // (10 ** position) == digit


def is_good(number, root_length):
    position = 0
    digit = 10
    if root_length == 10:
        stop = 99
    else:
        stop = root_length
    while position < stop and digit > 0:
        if not is_digit_here(number, digit % 10, position):
            return False
        position += 2
        digit -= 1
    return True


t1 = time.time()*1000

# low = 1020304050607080900
# high = 1929394959697989990
#
# l_root = math.sqrt(low)
# h_root = math.sqrt(high)
#
# print("low root:", l_root)
# print("high root:", h_root)
# print((math.ceil(h_root) - math.floor(l_root))//100*4, "candidates")

# We see the first digit of root must be 1 and last must be 0

possible_digits = {9: [0],
                   8: [3, 7],
                   7: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   6: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   4: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   0: [1]}


def find(progress):
    if len(progress) == 0:
        for digit in possible_digits[9 - len(progress)]:
            return find(progress + [digit])
    elif len(progress) == 10:
        current = build(progress)
        if is_good(current**2, len(progress)):
            return current
    else:
        current = build(progress)
        # print(current, "  \t", len(progress), "\t", current**2, is_good(current**2, len(progress)))
        if is_good(current**2, len(progress)):
            for digit in possible_digits[9 - len(progress)]:
                r = find(progress + [digit])
                if r is not None:
                    return r


root = find([])
print("Root:", root, "\nSquare:", root**2)


print()
print(round(time.time()*1000 - t1, 3), "milliseconds")
