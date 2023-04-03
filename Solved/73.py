# Counting fractions in a range
# Probably can be optimized more

from time import time_ns

start_time = time_ns()
nums = set()

for d in range(12000, 5, -1):
    bottom = d//3+1
    top = (d-1)//2
    for n in range(bottom, top+1):
        if n/d not in nums:
            nums.add(n/d)
answer = len(nums)
elapsed = (time_ns() - start_time)/1000000
print(answer)
print(elapsed, "ms")
