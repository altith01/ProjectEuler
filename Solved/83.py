# Path sum: four ways

from heapq import *
from sys import maxsize
from time import time_ns

start_time = time_ns()
# -------------------------------------------------------------------
matrix = []
with open("Solved/83.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        matrix.append([int(x) for x in line.strip().split(",")])

distances = dict()
unvisited = set()

for i in range(80):
    for j in range(80): 
        distances.update({
            (i, j): maxsize
        })
        unvisited.add((i,j))
# -------------------------------------------------------------------

shortest = maxsize
next_nodes = []
current = (0,0)
distances[current] = matrix[current[0]][current[1]]
while 1:
    adjacent = []
    if (current[0]+1, current[1]) in unvisited:
        adjacent.append((current[0]+1, current[1]))
    if (current[0]-1, current[1]) in unvisited:
        adjacent.append((current[0]-1, current[1]))
    if (current[0], current[1]+1) in unvisited:
        adjacent.append((current[0], current[1]+1))
    if (current[0], current[1]-1) in unvisited:
        adjacent.append((current[0], current[1]-1))
    for neighbor in adjacent:
        distance = min(distances[neighbor], distances[current] + matrix[neighbor[0]][neighbor[1]])
        distances[neighbor] = distance
        heappush(next_nodes, [distance, neighbor])
        next_nodes
    unvisited.remove(current)
    if (79, 79) not in unvisited:
        shortest = min(shortest, distances[(79, 79)])
        break
    else:
        current = heappop(next_nodes)[1]
        while current not in unvisited:
            current = heappop(next_nodes)[1]
elapsed = (time_ns() - start_time) / 1000000
print(elapsed, "ms")
print(shortest)
