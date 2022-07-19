"""
5. Write a Python program to get a single string from two given strings, separated by a space and swap
   the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

sample_str1 = 'abc'
sample_str2 = 'xyz'

new_sample_str1 = sample_str2[:2] + sample_str1[2:]
new_sample_str2 = sample_str1[:2] + sample_str2[2:]
print(new_sample_str1 + " " + new_sample_str2)