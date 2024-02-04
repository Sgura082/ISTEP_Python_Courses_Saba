# empty_dict = {}
# print(type(empty_dict))

# filled_dict = {1: "Hello", "Name": "Irakli", "List": [1, 2, 3, 4, 5]}
# print(filled_dict["LastName"])

# print(filled_dict.get("List", "მოცემული key არ არსებობს ლექსიკონში"))

# filled_dict["Name"] = ""
# print(filled_dict)

# filled_dict.setdefault("Salary", 10000)
# print(filled_dict)



# filled_dict = {1: "Hello", "Name": "Irakli", "List": [1, 2, 3, 4, 5]}

# print(filled_dict.keys())
# print(filled_dict.values())
#
# print(filled_dict.items())
#
# for key, value in filled_dict.items():
#     print(f"Key: {key}, Value: {value}")


# filled_dict = {1: "Hello", "Name": "Irakli", "List": [1, 2, 3, 4, 5]}
# filled_dict2 = {1: "Hello", "Name": "Ana", "LastName": "Tabatadze"}
#
# filled_dict.update(filled_dict2)
# print(filled_dict)


# print(filled_dict.pop(1))
# print(filled_dict)
#
# print(filled_dict.popitem())
# print(filled_dict)
# filled_dict = {1: "Hello", "Name": "Irakli", "List": [1, 2, 3, 4, 5]}
#
# in_operator = "Name" not in filled_dict
# print(in_operator)

# second_dict = filled_dict.copy()
#
# print(filled_dict)
# print(second_dict)
# filled_dict.popitem()
# print(filled_dict)
# print(second_dict)

# frozen_dict = {{"Name", "Username"}: "Hello World"}
#
# if {"Name", "Username"} in frozen_dict:
#     print(frozen_dict[{"Name", "Username"}])

# products = {
#     "Electronics": {
#         "Laptops": {
#             1001: {"Brand": "HP", "Price": 1000, "Quantity": 5},
#             1002: {"Brand": "Asus", "Price": 2000, "Quantity": 10}
#         },
#         "Phones": {
#             2001: {"Brand": "Samsung", "Price": 3000, "Quantity": 2},
#             2002: {"Brand": "iPhone", "Price": 2000, "Quantity": 1}
#         }
#     }
# }
#
# laptop = products['Electronics']['Laptops'][1001]['Price']
# smartphone = products['Electronics']['Phones'][2001]['Price']
# print(type(laptop))
# print(type(smartphone))
# print(f"Full Price {laptop + smartphone}")
dict = {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b,
    '**': a**b,
    '%': a%b,
    '//': a//b
}

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
op = input("enter operation: ")


i = dict.get(op)
print(i)