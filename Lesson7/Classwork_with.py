# try:
#
#     file = open("file.txt")
# except UnicodeDecodeError:
#     pass
# finally:
#     file.close()


with open("file.txt", "w") as file: #w - при новом открытие стирает все, записывает новое
    # print(file.readline())
    file.write("abc\n")
    file.write("Lol\n")

with open("file.txt", "a") as file: #a - записывает новое не удаляя старое
    file.write("NEW data\n")

with open("file.txt", "r") as file: #r - просто читает,,
    result = file.readlines()

print(result)

result_array = []

for r in result:
    result_array.append(r.replace("\n", " "))

print(result_array)