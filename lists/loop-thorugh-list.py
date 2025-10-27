a = [10,11,12,13]

for i in a:
    print(i)
    
for i in range(len(a)):
    print(i)
    
i = 0
while i < len(a):
    print(a[i])
    i+=1
    
#comphersion in list
b = [x for x in a if 11 in x]

print(b)
