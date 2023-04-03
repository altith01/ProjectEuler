# Path sum: two ways

from heapq import *
from sys import maxsize

# -------------------------------------------------------------------
matrix = []
with open("Solved/81.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        matrix.append([int(x) for x in line.strip().split(",")])

distances = dict()
unvisited = set()
next_nodes = []

for i in range(80):
    for j in range(80):
        if i+j==0:
            distances.update({
                (i, j): matrix[i][j]
            })
        else:
            distances.update({
                (i, j): maxsize
            })
        unvisited.add((i,j))
# -------------------------------------------------------------------


current = (0,0)
while 1:
    adjacent = []
    if (current[0]+1, current[1]) in unvisited:
        adjacent.append((current[0]+1, current[1]))
    if (current[0], current[1]+1) in unvisited:
        adjacent.append((current[0], current[1]+1))
    for neighbor in adjacent:
        distance = min(distances[neighbor], distances[current] + matrix[neighbor[0]][neighbor[1]])
        distances[neighbor] = distance
        heappush(next_nodes, [distance, neighbor])
        next_nodes
    unvisited.remove(current)
    if (79,79) not in unvisited:
        print(distances[(79,79)])
        break
    else:
        current = heappop(next_nodes)[1]
        while current not in unvisited:
            current = heappop(next_nodes)[1]

