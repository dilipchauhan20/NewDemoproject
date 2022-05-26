"""
2. Write program to get the duplicate chars from the string
"""

sample_input = "abcdab"

new_list = []
new_list1 = []
for i in sample_input:
    if i not in new_list:
        new_list.append(i)
    else:
        new_list1.append(i)

print("".join(new_list))
print("".join(new_list1))