"""string is anagram or not"""

str1 = "abcdcba"
str2 = "cbaabcd"
# print(sorted(str1))
if sorted(str1) == sorted(str2):
    print("anagram")
else:
    print("Not a anagram")


if str1[::-1]==str1:
    print("Palindrome")
else:
    print("Not palindrome")



# s1 = "Python"
# s2 = "Exercises"
#
# r = f'{s1}{s2}'
# print(r)


# s1 = "Python Quiz"
# p = s1.capitalize()
# q = s1.title()
# print(p[2] + q[2])



# nums1 = [1,2,3]
# nums2 = nums1
#
# nums1[0] = 0
#
# print(nums2)
