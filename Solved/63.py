# Powerful digit counts

count = 0
power = 1
while len(str(9**power)) == power:
    for base in range(1, 10):
        if len(str(base**power)) == power:
            count += 1
    power += 1
print(count)
