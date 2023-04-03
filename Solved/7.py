# 10001st prime

def find_prime(n):
    p_list = []
    i = 2
    while len(p_list) < n:
        if i == 2:
            p_list.append(i)
        else:
            is_p = True
            for p in p_list:
                if i % p == 0:
                    is_p = False
                    break
            if is_p:
                p_list.append(i)
        i += 1
    return p_list[-1]


print(find_prime(10001))
