a = {1,2,3,4,4}

# set is unordered, unindexed, unchangeable - not allow duplicates
print(a) #{1,2,3,4} automatically remove duplicates

a.add(5) #{1,2,3,4,5}
a.remove(1) #{2,3,4}


# set operations - &, | , -, ^

for i in a:
    print(i)



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

# if item missing / duplicate method behaviour

pr_methods_set = {1,2,4,5}

# pr_methods_set.add(5) #Quietly ignores duplicates , for adding single items

pr_methods_set.update([1,2,7,8,9]) # adding a list of items using list


print(pr_methods_set)


pr_methods_set.remove(10) # its return the key error, if value not there 
pr_methods_set.discard(10) # leave , not throw any error


pr_methods_set.pop() #remove and returns a random item, but behaviour crashes if set is empty

pr_methods_set.clear() #empties entire set

    