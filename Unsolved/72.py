# Counting fractions


def number_with_numerator(n, max_d):
    # Returns number of reduced fractions with prime numerator n denominator up to max_d
    if n == 1:
        print(n, max_d - 1)
        return max_d - 1
    else:
        print(n, max_d - max_d//n - (n - 1))
        return max_d - max_d//n - (n - 1)

print(sum(number_with_numerator(i, 8) for i in range(1,8)))
