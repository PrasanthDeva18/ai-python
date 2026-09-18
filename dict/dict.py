a = {"name" : "prasanth"}

print(a["name"])

#same as js


#loop

b = {
    "name" : "prasanth",
    "class" : "IT",
    "roll number" : 80
}

for key, value in b.items():
    print(f"{key}, {value}")


dictA = {
  "name" : "Prasanth",
  "rollNo" : 80
}

print(dictA['name'])

# dict.keys()
# dict.values()
# dict.items()

# del dictA['name']

a= dictA.pop('rollNo') # removes the key and returns the value

print(dictA, a)