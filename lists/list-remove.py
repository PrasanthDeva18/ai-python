# method - pop(), clear(), remove(), del - keyword

a = [1,2,3,4]
b = [1,2,3,4,4]

# remove the item in list based on item using remove method
a.remove(3)

# remove the item in list based on item using remove method but its same value repat it will delete first one
b.remove(4)

# delete the list specific index
a.pop(0)

# delete the item in the list last one if give without index mention in pop
a.pop()

# clear method will empty the list
a.clear()
