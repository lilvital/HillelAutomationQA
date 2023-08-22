class MyIteraror:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            self.current = 0
            raise StopIteration

iterator = MyIteraror(10)
for number in iterator:
    print(number)