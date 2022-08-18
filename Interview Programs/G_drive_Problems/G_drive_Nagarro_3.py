"""
Find the longest palendrom in a string?
Example
Input: abfgerccdedccfgfer
Output: ccdedcc
"""

str1 = "abfge"


def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l = l - 1
        r += 1
    return s[l+1:r]


res = ""
for i in range(len(str1)):
    # "abbba"
    odd = helper(str1, i, i)
    # "abba"
    even = helper(str1, i, i+1)
    if len(even) > 1 or len(odd) > 1:
        res = max(odd, even, res, key=len)
    else:
        print("There is no palindrome in the given string")

print(res)






