"""
HCL 2nd question program
2. Find a pair with maximum product in array of Integers.
Condition: Return no pairs exits if there is only 1 element in list
list1 = [1, 4, 3, 6, 7, 0]

output = [6,7]
"""

def maxProduct(value1):
    # Check length of the list is grater 2 or not
    if len(value1) < 2:
        return "no pairs exits"
    # Initialize the max product pair
    a = value1[0]
    b = value1[1]

    # Traverse through every possible pair
    # and keep track of max product
    for i in range(0, len(value1)):
        for j in range(i+1, len(value1)):
            if value1[i] * value1[j] > a * b:
                a, b = value1[i], value1[j]
    return a, b


list1 = [11, 4, 83, 6, 7, 0]

print(maxProduct(list1))