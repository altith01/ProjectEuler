# Cyclical figurate numbers
# Worked pretty well

from UsefulStuff.PolygonNumbers import *


def first_two(n):
    return str(n)[:2]


def last_two(n):
    return str(n)[-2:]


class Cycle:
    def __init__(self, numbers, shapes):
        self.__numbers = numbers
        self.__shapes = shapes

    @property
    def numbers(self):
        return self.__numbers

    def add_number(self, number):
        self.__numbers.append(number)

    @property
    def shapes(self):
        return self.__shapes

    @property
    def length(self):
        return len(self.__shapes)

    def add_shape(self, shape):
        self.__shapes.append(shape)


all_numbers = {3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
for i in range(1010, 10000):
    if i % 100 > 9:
        if is_triangle(i):
            all_numbers.update({3: all_numbers[3] + [i]})
        if is_square(i):
            all_numbers.update({4: all_numbers[4] + [i]})
        if is_pentagon(i):
            all_numbers.update({5: all_numbers[5] + [i]})
        if is_hexagon(i):
            all_numbers.update({6: all_numbers[6] + [i]})
        if is_heptagon(i):
            all_numbers.update({7: all_numbers[7] + [i]})
        if is_octagon(i):
            all_numbers.update({8: all_numbers[8] + [i]})

cycles = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

for num in all_numbers[8]:
    new_cycle = Cycle([num], [8])
    cycles.update({new_cycle.length: cycles[new_cycle.length] + [new_cycle]})

for l in range(1, 6):
    for cycle in cycles[l]:
        for shape in range(3, 8):
            if shape not in cycle.shapes:
                for number in all_numbers[shape]:
                    if last_two(cycle.numbers[-1]) == first_two(number):
                        if cycle.length == 5:
                            if last_two(number) == first_two(cycle.numbers[0]):
                                new_cycle = Cycle(cycle.numbers + [number], cycle.shapes + [shape])
                                cycles.update({new_cycle.length: cycles[new_cycle.length] + [new_cycle]})
                        else:
                            new_cycle = Cycle(cycle.numbers + [number], cycle.shapes + [shape])
                            cycles.update({new_cycle.length: cycles[new_cycle.length] + [new_cycle]})

print(cycles[6][0].numbers)
print(cycles[6][0].shapes)
print(sum(cycles[6][0].numbers))
