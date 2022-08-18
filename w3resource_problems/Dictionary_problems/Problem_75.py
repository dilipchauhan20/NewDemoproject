"""
75. Write a Python program to find all keys in the provided dictionary that have the given value.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Find all keys in the said dictionary that have the specified value:
['Roxanne', 'Betty']
"""

names = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}


# Getting values by list comprehension
# def get_the_keys_by_value(d1, val):
#     return list(key for key, value in d1.items() if value==val)


# getting value by for loop and if else condition
def get_the_keys_by_value(d1, val):
    list1 = []
    for item in d1:
        # print(item)
        if d1.get(item) == val:
            list1.append(item)
    return list1


print(get_the_keys_by_value(names, 20))