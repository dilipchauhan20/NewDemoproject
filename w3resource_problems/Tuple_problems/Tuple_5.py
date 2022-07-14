from abc import ABC


"""
5. Write a Python program to add an item in a tuple.
"""

tuplex = (3, 9, 1, 4)
tuplex1 = (20, 30, 40)

tuplex = tuplex[:3] + tuplex1 + tuplex[:3]

print(tuplex)