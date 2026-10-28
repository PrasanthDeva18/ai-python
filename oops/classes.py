class Person:
    name : str
    age : int
    phonenumber: str


myPerson1 = Person();
myPerson1.name = "John"
myPerson1.age = 30
myPerson1.phonenumber = "123-456-7890"

print(f"Name: {myPerson1.name}, Age: {myPerson1.age}, Phone Number: {myPerson1.phonenumber}")


# __ as prefix Private 


# access the private variable using getter method 
# set the value means using a setter method

# _ this for protected variable


# Name Mangling means _Classname__privateproperty


# Access inner class from the outer classes
class Outer:

    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display():
            print(f"Hello from Inner")

outer = Outer()
inner = outer.Inner()

inner.display()


# Access outer class from inner class
class Outer1:
    def __init__(self):
        self.name = "Outer"

    class Inner1:
        def __init__(self, outer):
            self.name = outer

        def display():
            print(f"Hello World to Print")

outer1 = Outer1()
inner = outer1.Inner1(outer1)
inner.display()

