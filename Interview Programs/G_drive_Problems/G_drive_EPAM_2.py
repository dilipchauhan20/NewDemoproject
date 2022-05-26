"""
EPAM Problem no. 18

17.  Write a python program to remove duplicate values in list.
str1 = 'abacdbj'

O/P = abcdj
"""

str1 = 'abacdbjj'
# str2 = ''
#
#
# for i in str1:
#     if i not in str2:
#         str2 += i
#
# print(str2)

# list1 = []
# for i in str1:
#     if i not in list1:
#         list1.append(i)
#
# print(list1 )

counter = 0
for i in range(0, len(str1)):
    for j in range(i+1, len(str1)):
        if str1[i] == str1[j]:
            counter += 1

print(counter)