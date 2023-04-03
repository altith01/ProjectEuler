# Counting rectangles

from time import time_ns


def rectangles(height, width):
    return (height+1)*height*(width+1)*width//4

def distance_to_2_million(x):
    return max(2000000,x) - min(2000000,x)

start_time = time_ns()
closest_area = 0
closest_distance = 2000000
for h in range(1, 2000):
    for w in range(1, h+1):
        r = rectangles(h, w)
        if r > closest_distance + 2000000:
            break
        d = distance_to_2_million(r)
        if d < closest_distance:
            closest_area = h*w
            closest_distance = d
elapsed = (time_ns() - start_time) / 1000000
print(closest_area, closest_distance)
print(elapsed, "ms")

