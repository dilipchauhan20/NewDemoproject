"""
79. Write a Python program to create a flat list of all the values in a flat dictionary. Go to the editor
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the values of the said flat dictionary:
[19, 20, 21, 20]
"""
dict1 = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

print(list(dict1.values()))
print(list(dict1.keys()))
