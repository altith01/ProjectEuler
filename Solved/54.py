# Poker hands

class Hand:
    def __init__(self, string):
        self.__cards = (self.make_card(string[0:2]), self.make_card(string[3:5]), self.make_card(string[6:8]),
                        self.make_card(string[9:11]), self.make_card(string[12:14]))

    def make_card(self, string):
        if string[0] == "A":
            return 14, string[1]
        elif string[0] == "K":
            return 13, string[1]
        elif string[0] == "Q":
            return 12, string[1]
        elif string[0] == "J":
            return 11, string[1]
        elif string[0] == "T":
            return 10, string[1]
        else:
            return int(string[0]), string[1]

    def card(self, n):
        return self.__cards[n]

    def cards(self):
        return self.__cards

    def is_royal(self):
        if self.card(0)[0] == 10 or self.card(0)[0] == 11 or self.card(0)[0] == 12 or self.card(0)[0] == 13 or\
                self.card(0)[0] == 14:
            if self.is_straight_flush():
                return True
        return False

    def is_straight_flush(self):
        if self.is_flush() and self.is_straight():
            return True
        return False

    def is_flush(self):
        if self.card(0)[1] == self.card(1)[1] == self.card(2)[1] == self.card(3)[1] == self.card(4)[1]:
            return True
        return False

    def is_straight(self):
        arr = []
        for card in self.cards():
            arr += [card[0]]
        if max(arr) - 1 in arr and max(arr) - 2 in arr and max(arr) - 3 in arr and max(arr) - 4 in arr:
            return True
        else:
            return False

    def is_four(self):
        lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in self.cards():
            lis[card[0]-2] += 1
        if 4 in lis:
            return True
        return False

    def is_full(self):
        lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in self.cards():
            lis[card[0]-2] += 1
        if 3 in lis and 2 in lis:
            return True
        return False

    def is_three(self):
        lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in self.cards():
            lis[card[0]-2] += 1
        if 3 in lis:
            return True
        return False

    def is_two(self):
        lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in self.cards():
            lis[card[0]-2] += 1
        if 2 in lis:
            return True
        return False

    def is_two_two(self):
        lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for card in self.cards():
            lis[card[0]-2] += 1
        if lis.count(2) == 2:
            return True
        return False

    def rank(self):
        if self.is_royal():
            return 9
        elif self.is_straight_flush():
            return 8
        elif self.is_four():
            return 7
        elif self.is_full():
            return 6
        elif self.is_flush():
            return 5
        elif self.is_straight():
            return 4
        elif self.is_three():
            return 3
        elif self.is_two_two():
            return 2
        elif self.is_two():
            return 1
        else:
            return 0

    def tie(self, r):
        if r == 8 or r == 4:
            top = 0
            for card in self.cards():
                if card[0] > top:
                    top = card[0]
            return top
        elif r == 7:
            val = 0
            for card in self.cards():
                if val == card[0]:
                    break
                else:
                    val = card[0]
            return val
        elif r == 6 or r == 3:
            lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for card in self.cards():
                lis[card[0]-2] += 1
            return lis.index(3) + 2
        elif r == 2:
            lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for card in self.cards():
                lis[card[0] - 2] += 1
            first = lis.index(2) + 2
            second = lis.index(2, first-1) + 2
            return second, first, lis.index(1) + 2
        elif r == 1:
            lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for card in self.cards():
                lis[card[0] - 2] += 1
            first = lis.index(1) + 2
            second = lis.index(1, first - 1) + 2
            third = lis.index(1, second - 1) + 2
            return lis.index(2) + 2, third, second, first
        elif r == 5 or r == 0:
            lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for card in self.cards():
                lis[card[0] - 2] += 1
            first = lis.index(1) + 2
            second = lis.index(1, first - 1) + 2
            third = lis.index(1, second - 1) + 2
            fourth = lis.index(1, third - 1) + 2
            fifth = lis.index(1, fourth - 1) + 2
            return fifth, fourth, third, second, first


text = open("54.txt", "r")

lines = text.readlines()

p1_wins = 0

for line in lines:
    p1 = Hand(line[:14])
    p2 = Hand(line[15:])
    r1 = p1.rank()
    r2 = p2.rank()
    if r1 > r2:
        p1_wins += 1
    elif r1 == r2:
        t1 = p1.tie(r1)
        t2 = p2.tie(r2)
        if t1 > t2:
            p1_wins += 1

print(p1_wins)
