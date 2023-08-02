def main_func(first_value, second_value):
    if type(first_value and second_value) == int:
        return first_value * second_value
    elif type(first_value and second_value) == str:
        str_result = first_value + second_value
        return str_result
    else:
        tuple_result = (first_value, second_value)
        return tuple_result

print(main_func(True,False))