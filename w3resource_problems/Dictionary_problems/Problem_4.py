"""
4. Write a Python script to check whether a given key already exists in a
 dictionary.

"""
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def check_key(i):
    if i in sample_dict:
        return "The value matched"
    else:
        return "Not matched"


print(check_key(2))