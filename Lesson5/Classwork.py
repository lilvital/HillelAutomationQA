# user_word = input("Word")
#
# while "o" not in user_word and "O" not in user_word:
#     user_word = input("pls put with o")
#
# print("nt")

# def check_for_letter_o():
#     user_word = input("Word")
#
#     while "o" not in user_word and "O" not in user_word:
#         user_word = input("pls put with o")
#
#     print("nt")
#
# check_for_letter_o()

# def summ(first_num, second_num, third_num=0, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     # first_num = int(input("1 "))
#     # second_num = int(input("2 "))
#
#     return first_num + second_num + third_num
# sum_result = summ(1,2,6,[1,2,4], **{"k":1})
#
# print(sum_result)

# def get_summ(*args):
#     return sum(args)
#
# print(get_summ(1,2,3,4,5,6))
# def get_summ_with_tuple(nums_tuple):
#     return sum(nums_tuple)
#
# print(get_summ_with_tuple((1,2,3,4,5,6)))
#
# def summ_with_kwargs(**kwargs):
#     print(kwargs)
#     return sum(kwargs.values())
#
# print(summ_with_kwargs(a=2, b=10))

# test_list = [1]
# def change_element_in_list(list_to_change):
#     list_to_change[0] = 1000
#
# change_element_in_list(test_list)
# print(test_list)
#
# a = 0
# def change_num_to_ten(num_to_change):
#     num_to_change = 100500
#
# change_num_to_ten(a)
# print(a)

# import import_example
from import_example import get_sum
print(get_sum(1,2,4))

