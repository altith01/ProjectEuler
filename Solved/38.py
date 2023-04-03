# Pandigital multiples


def next_pandigital(p):
    for i in range(len(p) - 1, 0, -1):
        if p[i] < p[i-1]:
            p1 = p[:i-1]
            p2 = p[i-1:]
            old_top = 0
            new_top = 1
            for j in range(len(p2)):
                if p2[new_top] < p2[j] < p2[old_top]:
                    new_top = j
            parts = p2.partition(p2[new_top])
            parts = parts[0] + parts[2]
            c_list = []
            bottom = ''
            for c in parts:
                c_list.append(c)
            c_list.sort(reverse=True)
            for c in c_list:
                bottom += c
            p2 = p2[new_top] + bottom
            return p1 + p2


def is_con_prod(p):
    for n in range(1, 5):
        integer = int(p[:n])
        string = ''
        multiplier = 1
        while len(string) < 9:
            string += str(integer*multiplier)
            multiplier += 1
        if string == p:
            return True
    return False


pandigital = '987654321'

while pandigital is not None and not is_con_prod(pandigital):
    pandigital = next_pandigital(pandigital)

print(pandigital)
