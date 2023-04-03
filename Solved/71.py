# Ordered fractions

FRAC = 3/7
answer_n = 0
answer_frac = 0
for d in range(2, 1000001):
    n = int(FRAC*d)
    frac = n/d
    if frac > answer_frac and frac < FRAC:
        answer_n = n
        answer_frac = frac
        # print(f"{n}/{d}")
print(answer_n)
