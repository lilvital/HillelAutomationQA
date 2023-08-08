# print(2/0)

try:
    print(int(input("Enter first number: ")) / int(input("Enter second number: ")))
except ZeroDivisionError:
    print("Please,STOP, dividing by zero")
    # print(2/0)
except ValueError:
    print("You wrote not integer")
finally:
    print("Finally")

# while True:
#     try:
#         result = input("Enter a number : ")
#         int_result = int(result)
#         print(int_result)
#         break
#     except:
#         continue