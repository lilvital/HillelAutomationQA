from abc import ABC, abstractmethod
#Интерфейс = абстрактный класс с абстрактными методами
class ISeeing:
    @abstractmethod
    def see(self):
        pass


class IWalkable:
    @abstractmethod
    def walk(self):
        pass

# class ISeeingAndWalkable():
#     @abstractmethod
#     def see(self):
#         pass
#
#     @abstractmethod
#     def walk(self):
#         pass

class Person(ISeeing, IWalkable):
    def see(self):
        print("This person see u")

    def walk(self):
        print("This person walking")


class BlindPerson(IWalkable):
    def walk(self):
        print("This person walking")