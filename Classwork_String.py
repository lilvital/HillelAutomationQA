#print("Vitalik" in "My name is Vitalik") #поиск в строке

# test_string = ("My name is Vitalik")

# print(test_string.upper())#Upper case
# print(test_string.lower())#Lower case

# print(test_string.startswith("My"))# проверка начала строки на слово
# print(test_string.endswith("Vitalik"))# проверка конца строки на слово
# print(test_string.startswith("name", 3))# проверка с 3 символа

# print(test_string + "27")
# print(test_string + str(27))# типизируем 27 с числа в стрингу

# test_string_procent = ("My name is Vitalik, my age is %s, i`m lived Odesa")
# procent_result = test_string_procent % 22 # после процента пишем что нужно вставить в строку
# print(procent_result)


# test_string_format = ("My name is Vitalik, my age is {}, i`m lived {}")# вместо скобочек вставляет данные
# test_string_format1 = ("My name is Vitalik, my age is {age}, i`m lived {city}")# по названию вставляет
# format_result = test_string_format.format(22,"Odesa")
# format_result = test_string_format1.format(age = 22,city = "Odesa")
# print(format_result)

# test_string_fstring = f"My name is Vitalik, my age is, i`m lived Odesa {1}, {'dsa'}, {True}" # после f идет строка,но в скобочках int,str,bool
# print(test_string_fstring)

# print(test_string.capitalize())# первый символ Аппер, все остальные делает Ловер кейс
# print(test_string.title())# каждое новое слово с большой буквы
# print(test_string.count("i"))# кол-во опеределенных символов в строке
# print(len(test_string))# длинна строки
# print(test_string.find("is"))# возвращает индекс первого нахождения субстсроки
# int_str = "123"
# str_str = "asd"
# alnum_str = "1ф"
# print(int_str.isnumeric())# проверка только ли числа в строке
# print(str_str.isalpha())# проверка только ли буквы в строке
# print((alnum_str.isalnum())) # проверка на числа или буквы в строке вместе


test_str = "abc123def"
print(test_str[0]) # вывод символа под индексом
print(test_str[1:4]) # вывод символа c какого-то по какой-то первый аргумент включительно, второй нет
print(test_str[2:7:2]) # вывод с шагом 2
print(test_str[-1]) # выводит последний элемент
print(test_str[-6:-1]) # считает с конца
print('12')