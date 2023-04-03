# Square Digit Chains
# Slow :(

def reaches89(n):
    num = n
    while num != 1:
        if num == 89:
            return True
        new = 0
        for char in str(num):
            new += int(char) ** 2
        num = new
    return False


count = 0
flags = set()
flags.add(89)

for n in range(1, 10000000):
    # if reaches89(n):
    #     print(n)
    #     count += 1
    num = n
    used = set()
    while num != 1:
        # used.add(num)
        if num in flags:
            # print(n)
            count += 1
            # flags.union(used)
            flags.add(n)
            break
        new = 0
        for char in str(num):
            new += int(char) ** 2
        num = new
print(count)
