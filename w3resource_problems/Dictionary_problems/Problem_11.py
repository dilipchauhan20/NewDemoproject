"""
11. Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1':5,'data2':10,'data3':2}
Result:
100
"""
my_dict = {'data1':5,'data2':10,'data3':2}

print(my_dict.values())
multi_val = 1
for i in my_dict:
    multi_val = multi_val * my_dict[i]

print(multi_val)
