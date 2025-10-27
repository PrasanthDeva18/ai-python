a = [1,2,3]
b = [4,5,6]

print(a+b)

for i in a:
  b.append(i)

print(b)

print(a.extend(b))
