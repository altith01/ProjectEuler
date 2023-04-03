# Names Scores

def char_value(c):
    for i in range(len('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
        if c == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i]:
            return i + 1
    return 0


file = open('22.txt', 'r')

text = file.readlines()

names = []

new_name = ''

for char in text[0]:
    if char != '"' and char != ',':
        new_name += char
    else:
        if len(new_name) > 0:
            names.append(new_name)
        new_name = ''

names.sort()

answer = 0

for index in range(len(names)):
    score = 0
    for char in names[index]:
        score += char_value(char)
    score *= index + 1
    answer += score

print(answer)
