# Maximum path sum II
# Came back with fresh mind months later and creamed this one

text = open("Solved/67.txt", "r")

lines = text.readlines()

triangle = []

for line in lines:
    triangle.append(line.replace("\n", "").split())

index = len(triangle) - 1

sums = {}

while index >= 0:
    for i in range(index+1):
        if i in sums:
            sums.update({i: int(triangle[index][i]) + max(sums[i], sums[i+1])})
        else:
            sums.update({i: int(triangle[index][i])})
    index -= 1

print(sums[0])
