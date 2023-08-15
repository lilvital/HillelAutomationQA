from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, heads_count, paw_count):
        self.heads_count = heads_count
        self.paw_count = paw_count

    @abstractmethod
    def get_a_battle_roar(self):
        pass

    @abstractmethod
    def bite(self):
        pass


class Cat(Animal):
    def __init__(self, heads_count, paw_count, tail, claws_count, cat_name):
        super().__init__(heads_count, paw_count)
        self.tail = tail
        self.claws_count = claws_count
        self.cat_name = cat_name


    def get_a_battle_roar(self):
        print("MEEEEOW")

    def bite(self):
        print(f"{self.cat_name} with {self.tail} is going KUS")


class Dog(Animal):
    def __init__(self, heads_count, paw_count, tail, claws_count, dog_name):
        super().__init__(heads_count, paw_count)
        self.tail = tail
        self.claws_count = claws_count
        self.dog_name = dog_name

    def get_a_battle_roar(self):
        print("ARRRRRRGH")

    def bite(self):
        print(f"{self.dog_name} with {self.tail} cut ur leg")

barsik = Cat(heads_count=1, paw_count=4, claws_count=18, tail="BIG PUSHITY XBOCT",cat_name="Barsik")
bobby = Dog(heads_count=1, paw_count=4, claws_count=18, tail="BIG PUSHITY XBOCT",dog_name="Bobby")
barsik.bite()
bobby.bite()

list_animal: [Animal] = [barsik,bobby]
for animal in list_animal:
    animal.bite()

# for animal in list_animal:
#     if animal.type == "Cat":
#         cat_doing_kus
#     if animal.type == "Dog":
#         dog_doing_kus