"""
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate
a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

user_input = input("Please enter your value by comma separated: ")

list1 = user_input.split(",")
print(list1)
print(tuple(list1))