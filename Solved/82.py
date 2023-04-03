# Path sum: three ways

from heapq import *
from sys import maxsize
from time import time_ns

start_time = time_ns()
# -------------------------------------------------------------------
matrix = []
with open("Solved/82.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        matrix.append([int(x) for x in line.strip().split(",")])

original_distances = dict()
original_unvisited = set()

for i in range(80):
    for j in range(80): 
        original_distances.update({
            (i, j): maxsize
        })
        original_unvisited.add((i,j))
# -------------------------------------------------------------------

shortest = maxsize
for start_row in range(80):
    distances = original_distances.copy()
    unvisited = original_unvisited.copy()
    next_nodes = []
    current = (start_row,0)
    distances[current] = matrix[current[0]][current[1]]
    while 1:
        adjacent = []
        if (current[0]+1, current[1]) in unvisited:
            adjacent.append((current[0]+1, current[1]))
        if (current[0]-1, current[1]) in unvisited:
            adjacent.append((current[0]-1, current[1]))
        if (current[0], current[1]+1) in unvisited:
            adjacent.append((current[0], current[1]+1))
        for neighbor in adjacent:
            distance = min(distances[neighbor], distances[current] + matrix[neighbor[0]][neighbor[1]])
            distances[neighbor] = distance
            heappush(next_nodes, [distance, neighbor])
            next_nodes
        unvisited.remove(current)
        if current[1] == 79:
            shortest = min(shortest, distances[current])
        if not len(unvisited):
            break
        else:
            current = heappop(next_nodes)[1]
            while current not in unvisited:
                current = heappop(next_nodes)[1]
elapsed = (time_ns() - start_time) / 1000000
print(elapsed, "ms")
print(shortest)
