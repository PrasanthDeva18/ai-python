# 1️⃣ Using append() – adds an element to the END of the list
a = [1, 2, 3, 4]
a.append(5)  
print("After append:", a)  
# Output: [1, 2, 3, 4, 5]
# append() adds one item to the end of the list.

# 2️⃣ Using insert() – adds an element at a SPECIFIC position
b = [1, 2, 3, 4]
b.insert(2, 44)  
print("After insert:", b)  
# Output: [1, 2, 44, 3, 4]
# insert(index, value) puts the value BEFORE the given index.

# 3️⃣ Using extend() – merges another iterable into the list
a.extend(b)
print("After extend (merge):", a)
# Output: [1, 2, 3, 4, 5, 1, 2, 44, 3, 4]
# extend() adds each element from b into a — it does NOT create a nested list like append() would.

# 4️⃣ Using extend() with tuple
c = [1, 2, 3, 4]
d = (5, 6, 7, 8)

c.extend(d)
print("After extending with tuple:", c)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
# extend() can take any iterable (list, tuple, set, dict, etc.)
