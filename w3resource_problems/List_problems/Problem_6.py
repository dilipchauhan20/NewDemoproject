"""
6. Write a Python program to get a list, sorted in increasing order by the last element in each
tuple from a given list of non-empty tuples.

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# print(sample_list[0][1])

# def order_func(elem):
#     return elem[1]
# def sort_list(list1):
#     return sorted(list1, key=order_func)


# Alternate solution
def sort_list(list1):
    return sorted(list1, key=lambda x: x[1])

print(sort_list(sample_list))