a = (1,2,3,4)

print(a)
print(a[0])


#tuples are unchangeable
"""
but if you want add, delete or update, convert the tuple into list and perform
"""

# example

b = list(a)
b.append(5)
c = tuple(b)

print(c)
# same for rest, or if you need add for without only possible is use the tuple + tuple

#tuples unpacking

d = (1,2,3)

# if we extract tuples like this we have to extract same number of elements in tuples

(a1, a2, a3) = d

print(a1,a2,a3)

e = (1,2,3,4)

(b1,b2,*b3) = e

print(b1,b2,b3)




