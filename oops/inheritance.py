class Parent:
    land_detail : str
    father_name: str
    mother_name: str
    total_bank_amount: str

class Child(Parent):
    pass

mydata = Child();

mydata.father_name = "Deva"

print(f"{mydata.father_name}")


# when we add the init function to the child class, it cut off the parent methods and obhect inheritance 


class Parent2:
    def __init__(self):
        self.a = 10

class Child2(Parent2):
    def __init__(self):
        Parent2.__init__(self)
        self.b  = 30

class Child3(Child2):
    def __init__(self):
        super().__init__()
        self.a1 = 40


obj1 = Child2()
obj2 = Child3()

print(obj1.b)
print(obj1.a)

print(obj2.a1)

        