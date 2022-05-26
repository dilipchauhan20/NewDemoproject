"""
Sapient Interview programm

2. write program to eliminate repeating character from string.

sample_input = "abcdab"

sample_output = "abcd"
"""

sample_input = "abcdab"
list1 = []

for char in sample_input:
    if char not in list1:
        list1.append(char)

print("".join(list1))

