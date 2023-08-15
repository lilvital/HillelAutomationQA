class Figure:
    def __init__(self, measure_of_length):
        self.measure_of_length = measure_of_length

    def get_square(self):
        pass

    def get_perimeter(self):
        pass



class Square(Figure):

    def __init__(self, side, measure_of_length):
        super().__init__(measure_of_length)
        self.side = side
        self.measure_of_length = measure_of_length

    def get_square(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4

# square1 = Square(6, "sm")
# print(f"{square1.side}{square1.measure_of_length}")
#
# square2 = Square(100, "km")
# print(f"{square2.side}{square2.measure_of_length}")
#
# print(square1 == square2)

square = Square(5, "sm")
print(square.get_square())
print(square.get_perimeter())