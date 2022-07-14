"""
4. Write a Python program to get a string from a given string where all occurrences of its first char
   have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

sample_string = "restartsr"

char = sample_string[0]
sample_string = sample_string.replace(char, '$')
# sample_string = char + sample_string[1:]
print(char + sample_string[1:])

