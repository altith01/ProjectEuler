# Prime digit replacements

from UsefulStuff.PrimeGenerator import *
from UsefulStuff.BinarySearchTree import *


def has_three(n):
    num = str(n)
    parts = []
    for char in num:
        parts.append(char)
    parts.sort()
    prev = 'x'
    c = 1
    for part in parts:
        if part < '3' and part == prev:
            c += 1
            if c == 3:
                return int(part)
        else:
            prev = part
            c = 1
    return -1


def number_primes(num, p1, p2, p3):
    c = 0
    for i in range(0, 10):
        if i != 0 or p1 != 0:
            new = num[:p1] + str(i) + num[p1+1:p2] + str(i) + num[p2+1:p3] + str(i) + num[p3+1:]
            if int(new) in primes:
                c += 1
    return c


def find_pos(n, r):
    num = str(n)
    r = str(r)
    pos = []
    for i in range(len(num)):
        if num[i] == r:
            pos.append(i)
    return pos


def combos(lis):
    c = []
    d = len(lis)
    p1, p2, p3 = 0, 1, 2
    while p1 < d - 2:
        while p2 < d - 1:
            while p3 < d:
                c.append([lis[p1], lis[p2], lis[p3]])
                p3 += 1
            p2 += 1
            p3 = p2 + 1
        p1 += 1
        p2 = p1 + 1
        p3 = p2 + 1
    return c


def is_prime(tree, candidate):
    if tree.data() == candidate:
        return True
    elif tree.data() > candidate and tree.left is not None:
        return is_prime(tree.left, candidate)
    elif tree.data() < candidate and tree.right is not None:
        return is_prime(tree.right, candidate)
    else:
        return False



cap = 999999
while True:
    primes = get_primes(cap)
    root = sortedArrayToBST(primes)
    for prime in primes:
        if prime > 1000:
            rep = has_three(prime)
            if rep > -1:
                spots = find_pos(prime, rep)
                combs = combos(spots)
                p = str(prime)
                for comb in combs:
                    k = 0
                    for t in range(10):
                        member = int(p[:comb[0]] + str(t) + p[comb[0]+1:comb[1]] + str(t) +
                                     p[comb[1]+1:comb[2]] + str(t) + p[comb[2]+1:])
                        if len((str(member))) != len(p) or not is_prime(root, member):
                            k += 1
                        if k > 2:
                            break
                    if k == 2:
                        print(prime)
                        quit()
    cap = cap * 10 + 9
