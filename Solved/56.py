# Powerful digit sum
# Not slow, but probably some optimizing could be done

def digital_sum(n):
    num = str(n)
    val = 0
    for char in num:
        val += int(char)
    return val


ans = 0
for a in range(1, 100):
    for b in range(1, 100):
        new = digital_sum(a**b)
        if new > ans:
            ans = new
print(ans)
