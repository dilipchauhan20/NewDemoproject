"""
12. Write a Python program to remove a key from a dictionary.
new_dict = {'a': 10, 'b': 9, 'c': 2, 'd': 5}
Result:
{'b': 9, 'c': 2, 'd': 5}

"""
new_dict = {'a': 10, 'b': 9, 'c': 2, 'd': 5}

if 'a' in new_dict:
    del new_dict['a']

print(new_dict)
