"""
1. Write a python program to calculate the length of the string without using len().

"""

str2 = "anlsadfsd"
counter1 = 0


def len_str(str1, c1=counter1):
    for char in str1:
        c1 += 1
    return c1


print(len_str(str2))
print(len(str2))

































