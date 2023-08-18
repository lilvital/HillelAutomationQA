import math

class Round:
    def __init__(self, radius):
        if radius < 0:
            radius = -radius
        self.__radius = radius # приватное (Закріть переменную от изменения)

    def get_perimeter(self):
        return math.pi * self.__radius * 2

round = Round(-5)
print(round.get_perimeter())
round.radius = -5
round.__radius = -5 # Приватное
round._Round__radius = -5
print(round.get_perimeter())

#DRY - Don`t Repeat Yourself
#YAGNI -  You ain`t gonna need it
#KISS - Keep It Simple, Stupid