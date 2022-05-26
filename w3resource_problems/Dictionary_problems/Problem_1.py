"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.

Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

"""

sample_dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x = sample_dict.values()


mod_dict1 = sorted(sample_dict1.items(), key=lambda x: x[1], reverse=True)
sample_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


def sort_test(x):
    return x[1]

# noinspection PyTypeChecker
mod_dict = sorted(sample_dict.items(), key=sort_test, reverse=False)

print(dict(mod_dict))
print((dict(mod_dict1)))