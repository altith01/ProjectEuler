# XOR decryption

from statistics import mode


text = open('Solved/59.txt').read()
characters = text.split(',')

commons = " ea"
mode0 = int(mode([characters[i] for i in range(len(characters)) if i % 3 == 0]))
mode1 = int(mode([characters[i] for i in range(len(characters)) if i % 3 == 1]))
mode2 = int(mode([characters[i] for i in range(len(characters)) if i % 3 == 2]))

keys = []
for common0 in commons:
    for common1 in commons:
        for common2 in commons:
            char0 = chr(ord(common0) ^ mode0)
            char1 = chr(ord(common1) ^ mode1)
            char2 = chr(ord(common2) ^ mode2)
            keys.append(char0 + char1 + char2)

for key in keys:
    a = key[0]
    b = key[1]
    c = key[2]
    decrypt = ''
    bad = False
    for i in range(len(characters)):
        if i % 3 == 0:
            x = ord(a)
        elif i % 3 == 1:
            x = ord(b)
        else:
            x = ord(c)
        n = int(characters[i]) ^ x
        if 128 > n > 31:
            decrypt += chr(n)
        else:
            bad = True
            break
    if not bad:
        print(a+b+c+":", decrypt)
        print(sum(ord(char) for char in decrypt))
        print()
