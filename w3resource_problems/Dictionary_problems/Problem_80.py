"""
80. Write a Python program to find the key of the maximum value in a dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
Finds the key of the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')
"""

dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# list1 = dict1.items()
def get_key_of_max_value(d1):
    return max(d1,key=d1.get), min(d1, key=d1.get)

print(get_key_of_max_value(dict1))
# maximum and minimum value of the said dictionary:
print(max(dict1, key=dict1.get), min(dict1, key=dict1.get))




# Sort the keys by its values
print(sorted(dict1, key=dict1.get))

# Fetch the value of any key by using get method
print(dict1.get('Theodore'))


# Lambda function example
x = lambda a: a * a
print(x(5))
