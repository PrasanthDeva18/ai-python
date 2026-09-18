print("hello world")

a = 10
b = "hello"


c = 1.4
print(type(c))

d = 'hello'

print(type(d))


x=y=10

print(x)

print(y)


# summary

# list is ordered, changeble and allow duplicate member

# few methods are : append - to insert the element in the list at the last,
# insert(position, value) use for insert the value at the specific position 
# extend() - two merge the two list and list + tuple as well
# using the + operator also used to merge the list 

# replace value based on indices

# remove and pop method is there remove based on the value, and pop remove the last value or based on index , clear method used to remove all


# Range is a python function - range(start, end, skip) by default start is 0
# will based on the given number it will skip the number 


# example usecase

# executing the loop for number of times

# looping through collections by an index

# create list or tuples of number 


a = list(range(1, 11, 1))

print(a)


a = [1,2,3,"hello world"]

for i in a:
  print(i)

for i in range(len(a)):
  print(i)


for i in range(1, 10, 2):
  print(i)



# tuples


# tuples are ordered and unchangeble, allow duplicates ()

# performing the operation, change the tuple to list and do

a = (1,3,2,5,4,8,7,5)

print(a)


b = sorted(a)

print(b) # if the direct sorted return the list
b.sort(reverse=True)
print(b)

c = tuple(sorted(b)) # using the tuple method return as tuple


print(c)

# sets are unordered, unchangeble, and not allow duplicate elements {}


set_unqiue = {1,5,3,5,4}

print(set_unqiue) # in the set by default sorted and also remove the duplicates

sorted_list = sorted(set_unqiue)
print(sorted_list)


# using the sorted method to sort the set it return as list right, but the back to set using the set , may be not return as order set, because it store the values as hash table in comouter memory by python

back_to_set = set(sorted_list)
print(back_to_set)


# core set operations

# union | or .union(), difference, intersection, symmetric difference 

union_ex1 = {1,2,3,4}
union_ex2 = {1,5,6}

# union_ex1.union(union_ex2)

print(union_ex1 |union_ex2) # combines all the unique items

    
# & intersection - it will return which item keep in both sets

print(union_ex1 & union_ex2)

# - differnce - it will return not presented items in b sets

print(union_ex1 - union_ex2)

# ^ it will return not presented items in both sets 
print(union_ex1 ^ union_ex2)





pr_methods_set = {1,2,4,5}

# pr_methods_set.add(5) #Quietly ignores duplicates , for adding single items

pr_methods_set.update([1,2,7,8,9]) # adding a list of items using list


print(pr_methods_set)
