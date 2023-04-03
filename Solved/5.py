# Smallest multiple

# Epic

def get_primes(n):
    p_list = []
    for i in range(2, n + 1, 1):
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
    return p_list


def get_factors(n):
    factors = []
    p_list = get_primes(n)
    part = n
    while 1 == 1:
        if part == 1:
            break
        for p in p_list:
            if part % p == 0:
                exists = False
                for index in range(len(factors)):
                    if p == factors[index][0]:
                        exists = True
                        factors[index][1] += 1
                        break
                if not exists:
                    factors.append([p, 1])
                part = int(part/p)
    return factors


number = 20

answer_factors = []

for num in range(2, number + 1, 1):
    new_factors = get_factors(num)
    for new_factor in new_factors:
        exists = False
        for factor in answer_factors:
            if factor[0] == new_factor[0]:
                exists = True
                factor[1] = max(new_factor[1], factor[1])
                break
        if not exists:
            answer_factors.append(new_factor)

final_answer = 1

for factor in answer_factors:
    while factor[1] > 0:
        final_answer *= factor[0]
        factor[1] -= 1

print(final_answer)
