"""
str1 = "I am a boy"
O/P = {"I": 1, "am":2, "a":1, "boy":3}
"""

str1 = "I am a boy"
str2 = str1.split(" ")

dict1 = {}
for i in str2:
    keys = dict1.keys()
    dict1[i] = len(i)

print(dict1)
# print(str2)