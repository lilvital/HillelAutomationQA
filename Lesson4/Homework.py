#1
#
# while True:
#     input_word = input("Enter word with letter o ")
#     if "o" in input_word.lower():
#         print("Good job")
#         break
#     else:
#         print("Try more")


#2
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst2 = []
#
# for item in lst1:
#     if isinstance(item,str):
#         lst2.append(item)
#
# print(lst2)

#3

int_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_list = 0

for item in int_lst:
    if item % 2 == 0:
        sum_list += item

print(sum_list)