"""
5. Write a Python program to count the number of strings where the string length is 2 or more and
the first and last character are same from a given list of strings.

sample_list = ['abc', 'xyz', 'aba', '1221']

Expected Result : 2

"""

sample_list = ['abc', 'xyz', 'aba', '1221', 'abcdefga']

def count_str(list1):
    count_1 = 0
    for i in list1:
        if len(i) > 1 and i[0] == i[-1]:
            count_1 += 1
    return count_1

print(count_str(sample_list))