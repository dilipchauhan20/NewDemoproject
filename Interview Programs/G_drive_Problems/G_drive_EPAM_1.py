"""
EPAM Problem no. 17

17.  Write a python program to remove duplicate values in list.
list1 = ['a', 'b', 'a', 'c', 'd', 'j']

O/P = ['a', 'b', 'c', 'd', 'j']
"""
list1 = ['a', 'b', 'a', 'c', 'd', 'j', 'j']
list2 = []
list3 = []

# loop to print list without duplicate char
for new1 in list1:
    if new1 in list3:
        pass
    else:
        list3.append(new1)


# loop to print list of duplicate char of original string
for i in range(0, len(list1)):
    print(i)
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j]:
            list2.append(list1[i])

print(list2)
print(list3)
