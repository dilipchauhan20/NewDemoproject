"""
99. Write a Python program to split a given multiline string into a list of lines.

Sample Input:
Original string: This
is a
multiline
string.

O/P:
Split the said multiline string into a list of lines:
['This', 'is a', 'multiline', 'string.', '']
"""

sample_str = "This \nis a \nmultiline \nstring."


print(sample_str.split(" \n"))