# Longest Collatz sequence

def f0(n):
    return n//2


def f1(n):
    return 3*n + 1


def collatz_length(n):
    term = n
    count = 1
    while term > 1:
        if term % 2 == 0:
            term = f0(term)
            count += 1
        else:
            term = f1(term)
            count += 1
    return count


cap = 1000000

answer = [0, 0]

for num in range(cap):
    if collatz_length(num) > answer[1]:
        answer = [num, collatz_length(num)]

print(answer)
