# Triangle containment

data = open('102.txt', 'r').readlines()

count = 0
for item in data:
    A, B, C, D, E, F = map(int, item.strip().split(','))
    if A != 0:
        m = B / A
        if (D < m*C and F > m*E) or (D > m*C and F < m*E):
            if C == E:
                X = C
            else:
                n = (F-D)/(E-C)
                b = D - n*C
                X = b/(m-n)
            if (X < 0 and A > 0) or (X > 0 and A < 0):
                count += 1
    elif (C < 0 and E > 0) or (C > 0 and E < 0):
        n = (F-D)/(E-C)
        Y = D - n*C
        if (Y < 0 and B > 0) or (Y > 0 and B < 0):
            count += 1

print(count)

