"""
100. Write a Python program to check whether any word in a given sting contains
duplicate characters or not. Return True or False.


Sample Output:
Original text:
Filter out the factorials of the said list.
Check whether any word in the said sting contains duplicate characters or not!
O/p = False

Original text:
Python Exercise.
Check whether any word in the said sting contains duplicate characters or not!
O/P = False

Original text:
The wait is over.
Check whether any word in the said sting contains duplicate characters or not!
O/P = True

"""
# input1 = "Filter out the factorials of the said list."


def check_dup_str_word(str1):
    word_list = str1.split()
    for word in word_list:
        if len(word) > len(set(word)):
            return False
    return True



text = "Filter out the factorials of the said list."
print("Original text:")
print(text)
print("Check whether any word in the said sting contains duplicate characters or not!")
print(check_dup_str_word(text))
text = "Python Exercise."
print("\nOriginal text:")
print(text)
print("Check whether any word in the said sting contains duplicate characters or not!")
print(check_dup_str_word(text))
text = "The wait is over."
print("\nOriginal text:")
print(text)
print("Check whether any word in the said sting contains duplicate characters or not!")
print(check_dup_str_word(text))