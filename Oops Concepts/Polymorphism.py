"""
Method overloading
1. Method overloading is an example of compile time polymorphism
2. When object bound with method at compile time is known as compile time polymorphism.
2. More than one methods are sharing same name but different signature.
"""


def multi(x,y):
    return x*y

print(multi(4,5))

def multi(x,y,z):
    return x*y*z

print(multi(4,5,6))


"""
Method overriding
1. Method overriding is an example of run time polymorphism.
2. When object bound with method at run time is known as run time polymorphism
2. defining the method in child class with the same name it was defined in the parent class
"""


# Python program to demonstrate
# method overriding


# Defining parent class
class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        Employee.__init__(self, name, base_pay)
        # self.name = name
        # self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.sales_incentive


if __name__ == '__main__':
    john = SalesEmployee('John', 5000, 1500)
    print(john.get_pay())

    jane = Employee('Jane', 5000)
    print(jane.get_pay())
