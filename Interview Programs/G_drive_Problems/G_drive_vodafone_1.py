"""
1. Write program to get swap the alternate characters of the string
sample_input = abcd
sample_output = badc
"""

sample_input = "abcd"

def swap_alt_char(str1):
    str1_list = list(str1)
    for i in range(0, len(str1_list)-1, 2):
        str1_list[i], str1_list[i+1] = str1_list[i+1], str1_list[i]
    return "".join(str1_list)
print(swap_alt_char(sample_input))


# def solve(s):
#     s = list(s)
#     for i in range(0, len(s)-1, 2):
#         s[i], s[i+1] = s[i+1], s[i]
#
#     return ''.join(s)
#
#
# s = "programming"
# print(solve(s))
