"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.

"""
dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

new_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

# Lambda function explanation
def sort_test(x):
    return x[1]

print(new_dict)


# # Sorting a list by the 3rd element of the list
# list1 = [[4, 3, 202], [10, 20, 102], [54, 99, 110], [75, 78, 199], [23, 30, 209], [15, 10, 175]]
#
# # sorted(list1, reverse=True)
#
# def fix_value(x):
#     return x[2]
#
# print(sorted(list1, key=fix_value, reverse=True))

