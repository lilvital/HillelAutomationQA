from abc import ABC, abstractmethod
import math


class Figure(ABC):

    def __init__(self, side):
        self.side = side


    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Triangle(Figure):

    def __init__(self, side, second_side, third_side, h):
        super().__init__(side)
        self.second_side = second_side
        self.third_side = third_side
        self.h = h

    def get_perimeter(self):
        perimeter = self.side + self.second_side + self.third_side
        print(f"Triangle perimeter = {perimeter}")

    def get_square(self):
        square = (self.side * self.h)/2
        print(f"Triangle square = {square}")


class Round(Figure):

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"Round perimeter = {perimeter}")

    def get_square(self):
        square = math.pi * self.radius ** 2
        print(f"Round square = {square}")

triangle = Triangle(side=10, second_side=2, third_side=5, h=2)

round = Round(radius=3)

list_figures : [Figure] = [triangle, round]
for figure in list_figures:
    figure.get_perimeter()
    figure.get_square()