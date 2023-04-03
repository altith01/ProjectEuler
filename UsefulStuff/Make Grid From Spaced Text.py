

text = open("???.txt", "r")

lines = text.readlines()

grid = []

for line in lines:
    if '\n' in line:
        line = line[:-1]
    grid.append([])
    num = ''
    for char in line:
        if char != ' ':
            num += char
        else:
            grid[-1].append(int(num))
            num = ''
    grid[-1].append(int(num))
