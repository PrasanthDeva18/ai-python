a = ["prasanth", 1, True]

print(len(a))
print(a[0])

# using the list constructor to make the list 

b = ("hello", 1, 2)

c = list(b)

print(c)

#  The search will start at index 2 (included) and end at index 5 (not included).
d = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Smartwatch",
    "Headphones",
    "Camera",
    "Bluetooth Speaker",
    "Gaming Console",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
    "Router",
    "Drone",
    "Smart TV",
    "Projector",
    "Power Bank",
    "External Hard Drive",
    "USB Flash Drive",
    "Smart Light"
]

print(d[2:5])

#negative indexing

print(d[-1])

print(d[-4:-1]) #"USB Flash Drive", "External Hard Drive", "Projector", "Power Bank",

# in operator check exist or not

if 1 in a:
    print(f"yes its availbale {a}")
