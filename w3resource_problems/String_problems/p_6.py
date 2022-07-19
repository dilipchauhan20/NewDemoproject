"""
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
   If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
   given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

user_input = input("Please Enetr your string: ")


def add_str(sample_str):
    if len(sample_str) >= 3:
        if sample_str[-3:] == "ing":
            return sample_str + "ly"
        else:
            return sample_str + "ing"
    else:
        return sample_str


print(add_str(user_input))
