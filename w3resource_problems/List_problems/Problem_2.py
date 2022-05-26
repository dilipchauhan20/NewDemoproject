"""
2. Write a Python program to multiply all the items in a list.
sample_input = [1,2,-8]
sample_output = -16

"""

sample_input = [1,2,-8]

product_list_elems = 1 # For multiplication we can't choose 0

for i in sample_input:
    product_list_elems *= i

print(product_list_elems)