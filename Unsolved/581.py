# 47-smooth triangular numbers

def t(n):
    return n * (n + 1) / 2


class PSmooth:

    def __init__(self, n=0):
        self.my_p = n
        self.my_prime_list = []
        self.__setPrimes(self.getP())

    def setP(self, n):
        self.my_p = n
        self.__setPrimes(self.getP())

    def getP(self):
        return self.my_p

    def __setPrimes(self, n):
        self.my_prime_list = []
        for num in range(2, n + 1, 1):
            if num == 2:
                self.my_prime_list.append(num)
            else:
                is_prime = True
                for prime in self.my_prime_list:
                    if num % prime == 0:
                        is_prime = False
                if is_prime:
                    self.my_prime_list.append(num)

    def __getPrimes(self):
        return self.my_prime_list

    def isPSmooth(self, n):
        for i in range(len(self.__getPrimes())):
            if n == self.__getPrimes()[i]:
                return True
            elif n % self.__getPrimes()[i] == 0:
                return self.isPSmooth(n / self.__getPrimes()[i])
        return False


def no_more(smooth):
    return 100000


problem = PSmooth(47)

ceiling = no_more(problem)

final_sum = 0

for index in range(ceiling):
    if index < problem.getP():
        final_sum += index
    elif problem.isPSmooth(t(index)):
        final_sum += index

print(final_sum)
