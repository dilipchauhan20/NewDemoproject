"""
Q. What is Lambda Function
--> Lambda functions are anonymous function means that function without name.
    This function can have any number of arguments but only one expression,
    which is evaluated and returned.

Ex.
    lambda a: a*a
"""

lambda_exp = lambda a: a**2

print(lambda_exp(3))


"""
1. What is class?
Ans: Class is nothing but collections of objects. Its a logical entity that have some
attributes and methods.
"""


class MathOps:
    # Attribute
    x = 19
    y = 5

    # sample methods
    def multi(self):
        return self.x + self.y

    def addition(self):
        return self.x * self.y

    def subtraction(self):
        return self.x - self.y

    def division(self):
        return self.x // self.y


# Object Instantiation
p1 = MathOps()

# Accessing class attributes and methods though objects
print(p1.multi())
print(p1.addition())
print(p1.subtraction())
print(p1.division())
print(p1.x)
print(p1.y)


""" Python Constructor """

# Non Parametrized constructor
class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "TestGeekforGeeks"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()
print(obj.geek)



# Parametrized constructor
class MathOps:

    # Constructor
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]

    # sample methods
    def multi(self):
        return self.x + self.y

    def addition(self):
        return self.x * self.y


# Object Instantiation
p1 = MathOps(19, 5)

# Accessing class attributes and methods though objects
print(p1.multi())
print(p1.addition())



















