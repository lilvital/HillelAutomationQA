def get_square(limit):
    num = 1
    while num <= limit:
        yield num ** 2
        num += 1

for el in get_square(5):
    print(el)