str1 = [1,3,23,11,44,3,23,2,3]
list2 = []

for i in str1:
    if str1.count(i) > 1:
        list2.append(i)

print(list(set(list2)))