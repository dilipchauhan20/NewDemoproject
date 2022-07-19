"""
Find the longest palendrom in a string?
Example
Input: abfgerccdedccfgfer
Output: ccdedcc
"""

str1 = "abfgerccdedccfgfer"


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
    res = max(odd, even, res, key=len)

print(res)






