"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
   If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
sample_String = 'w3wslodgdlkgkd'

if len(sample_String) >= 2:
    print(sample_String[:2] + sample_String[-2:])
else:
    print("Empty String")


