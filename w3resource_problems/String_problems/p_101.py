"""
101. Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string. Go to the editor
Sample Output:
42
Error in input!
Error in input!
"""

u_input1 = "42"
u_input2 = "32"

u_input1, u_input2 = "0" + u_input1, "0" + u_input2

if (u_input1.isnumeric() and u_input2.isnumeric()):
    print(str(int(u_input1) + int(u_input2)))
else:
    print("Error in input!")

