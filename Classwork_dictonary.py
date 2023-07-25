#Dictionary unordered and changeable

employees_dict = {"testmail@gmail.com":"Test Employee 1",
                  "testmail2@gmail.com": "Test Employee 2",
                  1: 2,}

print(employees_dict[1])
employees_dict[1] = "NEW VALUE"
print(employees_dict[1])
print(len(employees_dict))