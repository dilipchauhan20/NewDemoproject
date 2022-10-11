"""
1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at
least three occurrences of five.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""

# list1 = [19, 19, 15, 5, 3, 5, 5, 2]
#
# def new_func(val1):
#     return val1.count(19) == 2 and val1.count(5) == 3
#
# print(new_func(list1))

def my_func(val1):
    return val1.count(19) == 2 and val1.count(5) == 3

print(my_func([19, 19, 15, 5, 3, 6, 5, 2]))