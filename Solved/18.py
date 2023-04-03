# Maximum path sum 1
# Suboptimal solution, does not work for 67.
# Keeping this one for comparison

def max_path(triangle, level, position):
    if level == len(triangle) - 1:
        return int(triangle[level][position])
    else:
        return int(triangle[level][position]) + max(max_path(triangle, level + 1, position), max_path(triangle, level + 1, position + 1))


text = open("18.txt", "r")

lines = text.readlines()

triangle = []

for line in lines:
    triangle.append(line.replace("\n", "").split())

print(max_path(triangle, 0, 0))
