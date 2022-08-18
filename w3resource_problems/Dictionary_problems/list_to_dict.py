"""
write a program to convert List to Dict
"""

list1 = [[2, 5], [9, 2], [10, 12], [6, 8], [22, 23]]
dict2 = {}


for i in list1:
    x = i[0]
    # keys = dict2.keys()
    dict2[x] = i[1]

print(dict2)
