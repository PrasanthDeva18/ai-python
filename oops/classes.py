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