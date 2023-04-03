# Largest product in grid

num_adjacent = 4


def left_product(grid, row, col):
    if col > len(grid[row]) - num_adjacent:
        return 0
    else:
        product = 1
        for i in range(num_adjacent):
            product *= grid[row][col + i]
        return product


def down_product(grid, row, col):
    if row > len(grid) - num_adjacent:
        return 0
    else:
        product = 1
        for i in range(num_adjacent):
            product *= grid[row + i][col]
        return product


def diagonal_up_product(grid, row, col):
    if col >= len(grid[row]) - num_adjacent or row < num_adjacent - 1:
        return 0
    else:
        product = 1
        for i in range(num_adjacent):
            product *= grid[row - i][col + i]
        return product


def diagonal_down_product(grid, row, col):
    if col >= len(grid[row]) - num_adjacent or row > len(grid) - num_adjacent:
        return 0
    else:
        product = 1
        for i in range(num_adjacent):
            product *= grid[row + i][col + i]
        return product


text = open("11.txt", "r")

num_grid = []

for line in text.readlines():
    if '\n' in line:
        line = line[:-1]
    num_grid.append([])
    num = ''
    for char in line:
        if char != ' ':
            num += char
        else:
            num_grid[-1].append(int(num))
            num = ''
    num_grid[-1].append(int(num))

answer = 0

for r in range(len(num_grid)):
    for c in range(len(num_grid[r])):
        new = max(left_product(num_grid, r, c),
                  down_product(num_grid, r, c),
                  diagonal_up_product(num_grid, r, c),
                  diagonal_down_product(num_grid, r, c))
        if new > answer:
            answer = new

print(answer)
