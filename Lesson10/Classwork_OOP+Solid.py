def get_sum(first_num, second_num):
    result = first_num + second_num
    print(result)# не является первым принципом солида

def get_sum(first_num, second_num):
    return (first_num + second_num) # является первым принципом солида

print(get_sum(1, 2))
with open("result.txt", "x") as file:
    file.write(get_sum(1, 2).__str__())