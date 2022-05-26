"""
4. Write a Python program to get the smallest number from a list.
sample_input = [1, 2, -8, 0]

sample_output = -8

"""
sample_input = [1, 2, -8, 0]


# def smallest_num(list1):
#     lowest_num = list1[0]
#     for i in list1:
#         if i < lowest_num:
#             lowest_num = i
#     return lowest_num
#
#
# print(smallest_num(sample_input))


# Short solution using sort method
sample_input.sort()
# print(sample_input)
print(sample_input[0])

