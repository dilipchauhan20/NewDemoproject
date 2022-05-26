sample_str = "Sachin scored 172 runs from 102 balls by hitting 17 boundaries and 9 sixes."


# # This will return the list of digits for ex. [172, 102, 17, 9]
# print("Original string : " + sample_str)
#
# num = [int(x) for x in sample_str.split() if x.isdigit()]
#
# print("The numbers list is : " + str(num))

# # this will return the string of all digits for ex. 172102179
# print("Original String : " + sample_str)
# num = ""
# for c in sample_str:
#     if c.isdigit():
#         num = num + c
# print(num)

# WAP to remove duplicate chars from string

input_str = "abcdsabtest"
list1 = []

for i in input_str:
    if i not in list1:
        list1.append(i)
print("".join(list1))


# str1 = ""
# for i in input_str:
#     if i not in str1:
#         str1 += i
# print(str1)


# my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
# del my_dict['Dave']  #removes key-value pair of 'Dave'
# my_dict.pop('Ava')   #removes the value of 'Ava'
# my_dict.popitem()    #removes the last inserted item
# print(my_dict)