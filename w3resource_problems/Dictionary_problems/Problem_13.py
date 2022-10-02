"""
13. Write a Python program to map two lists into a dictionary.
list1 = ['red', 'green', 'blue']
list2 = ['#FF0000','#008000', '#0000FF']

Result:
{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
"""

list1 = ['red', 'green', 'blue']
list2 = ['#FF0000','#008000', '#0000FF']

dict1 = dict(zip(list1, list2))

print(dict1)