test_string = "abc"
test_list = ["abc", "My name is Vitalik", "qweqe"]

# for char in test_string:
#     print(char)

# for string_in_list in test_list:
#     print(string_in_list)
#     for letter in string_in_list:
#         print(letter)

test_dict = {1: "name", 2: "second name"}

for dict_elem in test_dict.values():
    print(dict_elem)

for key,value in test_dict.items():
    print(key,value)
