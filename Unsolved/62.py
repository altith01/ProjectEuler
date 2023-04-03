# Cubic permutations
# Slow :(

def is_cube(n):
    t = round(n**(1/3))
    return t**3 == n


def is_perm(n1, n2):
    return sorted((str(n1))) == sorted((str(n2)))


length = 3
groups = {}
base = 100
while True:
    n = base ** 3
    added = False
    for cube in groups:
        if is_perm(cube, n):
            groups.update({cube: groups[cube] + [n]})

            added = True
            if len(groups[cube]) == 5:
                print("WHOOOOOOOOOOOAAAAAAAAAAAAAA")
                base_check = base + 1
                while len(str(base_check**3)) == length:
                    if is_perm(base_check ** 3, cube):
                        groups.update({cube: groups[cube] + [base_check ** 3]})
                    base_check += 1
                if len(groups[cube]) == 5:
                    print(cube)
                    quit()
    if not added:
        groups.update({n: [n]})
    base += 1
    if len(str(base**3)) != length:
        length = len(str(base**3))
        groups = {}
