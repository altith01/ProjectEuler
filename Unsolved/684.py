# Inverse Digit Sum
# Slow, need to figure out more clever way

from UsefulStuff.Fibonacci import f
import time

MY_MOD = 1000000007

# this is slow with large n
def s(n):
    t = time.time()
    d = n % 9
    print(time.time() - t, d)
    k = (n // 9) % (MY_MOD - 1)
    print(time.time() - t, k)
    # value = int(str(d) + k * '9') % MY_MOD
    nines = 0
    for _ in range(k):
        nines = (nines * 10 + 9) % MY_MOD
        print(_)
    print(time.time() - t)
    return nines
    # num_digits = math.ceil(n / 9)
    # remaining = n
    # value = 0
    # while num_digits > 0:
    #     new_digit = (remaining - ((num_digits - 1) * 9))
    #     value = (value * 10) + new_digit
    #     remaining -= new_digit
    #     num_digits -= 1
    # return value


def S(n, start=1):
    return sum(s(i) for i in range(start, n+1)) % MY_MOD


# answer = 0
# for i in range(2, 91):
#     answer *= 2
#     answer += S(f(i), f(i-1) + 1)
#     answer %= MY_MOD
#     print(answer, i)




x = time.time()
# print(s(927927593))
print(f(80))
print(time.time()-x)


# current = 1
# prior = 1
# running_S = S(current)
# answer = running_S
# temp = current
# current += prior
# prior = temp
# for _ in range(3, 91):
#     running_S += S(current, prior+1) % 1000000007
#     running_S %= 1000000007
#     answer += running_S
#     answer = answer % 1000000007
#     temp = current
#     current += prior
#     prior = temp
#     print(_, answer)
# print(answer)

