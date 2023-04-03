# Largest exponential

from math import log
from time import time_ns

start_time = time_ns()
pairs = [(int(line.strip().split(",")[0]),int(line.strip().split(",")[1])) for line in open('Solved/99.txt', 'r').readlines()]

max_line_index = 0
max_line_modified_exponent = 0
for i in range(len(pairs)):
    modified_exponent = log(pairs[i][0])*pairs[i][1]
    if modified_exponent > max_line_modified_exponent:
        max_line_index = i
        max_line_modified_exponent = modified_exponent

elapsed = (time_ns() - start_time) / 1000000
print(f"Line {max_line_index+1}: {pairs[max_line_index]}")
print(elapsed, "ms")
