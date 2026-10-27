class Person: 
    def __init__(self, name: str, age: int = 18, phonenumber: str = "123"):
        self.name = name
        self.age = age
        self.phonenumber = phonenumber


myPerson1 = Person("prasanth");

print(f"{myPerson1.name}");


# __init__ is a special function in Python classes. It runs automatically when you create a new object. It sets up the starting values (properties) for that object.
# self refers to the specific object you are creating. It connects the values you provide to that individual object, keeping it separate from others.

# two types of properties 
# Class Properties and Object Properties

# Class Methods
class Temp:
    def __init__(self, a):
        self.a = a
    def print(self):
        print(f"{self.a}")

p = Temp(5)

print(p.print())


# The __str__() method is a special method that controls what is returned when the object is printed:
class Test:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"{self.a}"

p = Test(5)

print(p)


# using del keywords to delete - method and properties

