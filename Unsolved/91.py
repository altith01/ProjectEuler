# Right triangles with integer coordinates
from time import time_ns

def count_right_triangles(n):
    count = 0
    for i in range(1, n + 1):
        count = count_right_triangles_helper(i, count)
    return count

# Missing all triangles not laying on an axis
def count_right_triangles_helper(i, previous):
    new = 0
    new += 3 + 6*(i-1)
    if i % 2 == 0:
        new += 2
    return previous + new

start_time = time_ns()
ans = count_right_triangles(50)
elapsed = (time_ns() - start_time) / 1000000
print(ans)
print(elapsed, "ms")
