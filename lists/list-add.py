# 1. Changing value by index
a = [1, 2, 3, 4]
a[1] = 10  # Replace the value at index 1 (second element) with 10
print("a:", a)  # Output: [1, 10, 3, 4]

# 2. Replacing a range of indices with new values
b = [1, 2, 3, 4]
b[1:3] = [5, 6]  # Replace indices 1 and 2 (2nd and 3rd elements) with 5, 6
print("b:", b)  # Output: [1, 5, 6, 4]

# 3. Replacing a single index using a slice with multiple values
c = [1, 2, 3, 4]
c[2:3] = [7, 8]  # Replace index 2 (third element) with two values 7 and 8
print("c:", c)  # Output: [1, 2, 7, 8, 4]

# 4. Replacing multiple indices with a single value
d = [1, 2, 3, 4]
d[1:4] = [20]  # Replace indices 1, 2, 3 with a single value 20
print("d:", d)  # Output: [1, 20]

# 5. Using insert() to add an element at a specific index
e = [1, 2, 3, 4]
e.insert(2, "5")  # Insert "5" at index 2 (before the third element)
print("e:", e)  # Output: [1, 2, '5', 3, 4]
