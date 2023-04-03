# Coded Triangle Numbers

import math


def is_t(n):
    if 2*n == int(math.sqrt(2 * n)) * \
            (int(math.sqrt(2 * n)) + 1):
        return True
    else:
        return False


def word_value(s):
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = 0
    for i in range(len(s)):
        for j in range(1, 27):
            if s[i] == alphabet[j]:
                value += j
    return value


text = open('42.txt', 'r')

lines = text.readlines()

line = lines[0]

words = []

word = ''

for char in line:
    if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if word != '':
            words.append(word)
        word = ''
    else:
        word += char

count = 0

for word in words:
    if is_t(word_value(word)):
        count += 1

print(count)
