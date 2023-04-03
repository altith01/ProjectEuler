# Number Splitting

import math

def is_S_recursive(goal, remaining):
    if goal < 0: 
        return False
    if remaining == "":
        return True if goal == 0 else False
    else:
        for i in range(1, len(remaining)+1):
            part_1 = remaining[i:]
            if i == len(remaining):
                part_2 = remaining
            else:
                part_2 = remaining[:-len(remaining)+i]
            if not part_1 or goal - int(part_2) <= int(part_1):
                if is_S_recursive(goal - int(part_2), part_1):
                    return True
        return False

def is_S_number(n):
    """Takes only perfect squares"""
    return is_S_recursive(int(math.sqrt(n)), str(n))


sum = 0
for root in range (4, 1000001):
    if root % 10000 == 0:
        print(root)
    if is_S_number(root ** 2):
        sum += root ** 2
        # print(f"{root}\t{root**2}")
    
print(sum)

# 128088830547982