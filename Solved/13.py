# Large sum

text = open('13.txt', 'r')

total = 0

lines = text.readlines()

for line in lines:
    if '\n' in line:
        line = line[:-1]
    total += int(line)

total = str(total)

print(total[:10])
