# Sum square difference

# Easy lol

def sum_of_squares(n):
    if n == 1:
        return 1
    return n**2 + sum_of_squares(n-1)


def square_of_sum(n):
    return (n*(n+1)//2)**2


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


print(difference(100))
