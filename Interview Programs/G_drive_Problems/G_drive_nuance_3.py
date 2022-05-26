"""
Programming question asked on 17th may

anagram program

str1 = "abcd"
str2 = "bcda"

str1 and str2 are anagram
"""

str1 = "abcd"
str2 = "bcda"

def check_anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        return True

print(check_anagram(str1, str2))