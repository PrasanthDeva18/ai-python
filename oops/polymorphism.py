# Class Polymorphism

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Car:
    def __init__(self):
        self.a = "4 Wheel"
        self.b = "2 Door"

    def Sound(self):
        print("Zooe")


class Truck:
    def __init__(self):
        self.a = "6 Wheel"
        self.b = "2 Door"
    
    def Sound(self):
        print("Druu Druu")

class Bus:
    def __init__(self):
        self.a = "8 Wheel"
        self.b = "2 Door"
    
    def Sound(self):
        print("Drrrck")

bus = Bus()
truck = Truck()
car = Car()

for x in (bus, truck, car):
    print(x.a)
    print(x.b)
    x.Sound()


# Inheritance in class polymorphism


# method overriding (the child class replacing the parent class's method) is the most common way we achieve polymorphism in Object-Oriented Programming.
