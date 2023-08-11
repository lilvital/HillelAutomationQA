def first_decorator(func):
    def wrapper(*args, **kwargs):
        print("Second_IN")
        func(*args, **kwargs)
        print("Second_OUT")

    return wrapper
    

@first_decorator
def print_hello(word_to_print):
    print(word_to_print)

print_hello("lol")