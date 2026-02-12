
a = {10,20,30}
b = {20,30,40}

print(a,b) 

a.add(10) #ignore 
a.add(100) 
a.add(200)
print(a)

fruits = {'apple','banana','pineapple','mango'}
print(fruits)

union = a.union(b)
print(union)

intersection = a.intersection(b)
print(intersection)

difference = a.difference(b)
print(difference)