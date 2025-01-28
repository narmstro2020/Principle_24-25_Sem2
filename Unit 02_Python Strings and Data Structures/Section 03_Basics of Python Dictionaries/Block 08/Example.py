my_dict = {"name": "Alice", "age": 30}


my_dict2 = dict.fromkeys(my_dict)
print(my_dict2)

my_dict2.update(my_dict)

print(my_dict2)

