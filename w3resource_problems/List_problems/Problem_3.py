"""
3. Write a Python program to get the largest number from a list.
sample_input = [23,56,12,88,09]

sample_output = 88

"""

sample_input = [88,56,12,-8,-9]
# sample_input.sort()
# print(sample_input[-1])

# without using sort method

def largest_num(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max

print(largest_num(sample_input))