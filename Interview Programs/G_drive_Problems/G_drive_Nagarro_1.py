"""
Input an array and then print the repeating characters??
Example:
Input:1,3,23,11,44,3,23,2,3.
Output:3,23
"""

list1 = [1,3,23,11,44,3,23,2,3]
list2 = list(set(i for i in list1 if list1.count(i) > 1))


# for i in list1:
#     n = list1.count(i)
#     if n > 1:
#         if list2.count(i) == 0:
#             list2.append(i)

print(list2)
