def generator_numbers(start_num, end_num):
    current_num = start_num
    while current_num <= end_num:
        yield current_num
        current_num += 1


for num in generator_numbers(1, 5):
    print(num)