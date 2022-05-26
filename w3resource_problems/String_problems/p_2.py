"""
2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

str1 = "GoOgle.com"
dict1 = {}

for i in str1.lower():
    keys = dict1.keys()
    if i in keys:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)