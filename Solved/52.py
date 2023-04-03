# Permuted Multiples

def same_digits(n, m):
    n = str(n)
    m = str(m)
    cn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for char in n:
        cn[int(char)] += 1
    for char in m:
        cm[int(char)] += 1
    if cn == cm:
        return True
    else:
        return False


ans = 0
done = False

while not done:
    ans += 1
    if len(str(ans)) == len(str(6*ans)):
        for i in range(2, 7):
            if not same_digits(ans, i * ans):
                break
            if i == 6:
                done = True

print(ans)