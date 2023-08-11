def sum_from_file(filename):
    total_sum = 0
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                try:
                    number = int(line.strip())
                    total_sum += number
                except ValueError:
                    print("Знайдено помилку у рядку")
                    pass
    except FileNotFoundError:
        print("Файл не знайдено")
    return total_sum

filename = "Homework.txt"
result = sum_from_file(filename)
print(f"Сума чисел з файлу : {result}")
