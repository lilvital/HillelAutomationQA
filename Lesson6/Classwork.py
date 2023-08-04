# variable_is_not_function = 1
# def sum_two_numbers(first_number : int, second_number : int | float) -> int:
#     '''
#     :param first_number:
#     :param second_number:
#     :return:
#     '''
#     return first_number + second_number
#
# print(sum_two_numbers(1,2.1))
# print(variable_is_not_function)

# def wait_for_user_input_qwe():
#     text = input("Input qwe: ")
#     if text == "qwe":
#         return text
#     else:
#         return wait_for_user_input_qwe()
#
# wait_for_user_input_qwe()

# def add_two_to_number(number: int):
#     print(number)
#     if (number == 500):
#         return number
#     else:
#         number += 2
#         add_two_to_number(number)
# add_two_to_number(499)

# def add_ten_to_number(number):
#     return number + 10
#
# add_ten_to_num = lambda a, b, c  : print(a + b + c)
#
# print(add_ten_to_number(0))
# add_ten_to_num(1, 2, 4)

# def is_even_number(list_to_nums):
#     result = []
#     for num in list_to_nums:
#         if num % 2 == 0:
#             result.append(num)
#
#     return result
#
# print(is_even_number(range(1,5)))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 5)))
even_number = [x for x in my_list if x % 2 == 0]
print(even_number)