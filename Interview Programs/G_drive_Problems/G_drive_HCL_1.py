"""
HCL program questions
1. WAP to count duplicate character in a string.
"""
str1 = 'sbcdddaabb'


# for i in range(0,len(str1)):
#     counter = 1
#     for j in range(i+1,len(str1)):
#         if str1[i] == str1[j] and str1[i] != ' ':
#             # print(str1[j])
#             counter += 1
#             str1 = str1[:j] + '0' + str1[j+1:]
#             # print(str1)
#
#     if counter > 1 and str1[i] != '0':
#         print(str1[i], " - ", counter)

new_str = ""

for i in range(0, len(str1)):
    counter = 1
    for j in range(i+1, len(str1)):
        if str1[i] == str1[j] and str1[i] != " ":
            counter += 1
            str1 = str1[:j] + '0' + str1[j+1:]

    if counter > 1 and str1[i] != '0':
        print(str1[i], "- ", counter)

# print(new_str)
