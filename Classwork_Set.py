#Set = unordered and unchangeable
set_example = {"test", 1, 2, 3, True, False} # отрезало тру потому что тру = 1

print(set_example)

list_example = ["testgmail@gmail.com", "testgmail@gmail.com", "Lol"]
set_from_list = set(list_example)
print(set_from_list)

tuple_from_list = tuple(list_example)
print(tuple_from_list)

list_from_set = list(list_example)
print(list_from_set)