#example of tuple 
tuple = ('Ankit',10,True,12.7,False,None)
#None absence of value, it is equal to null in c language 
print(tuple)
print(tuple[0]) # Ankit
print(tuple[1:3]) # 10 True 
print(tuple[3:]) # 12.7, False None 
print(tuple[0:2]) #print 2 items from beginning (from left)
print("Position of Ankit ",tuple.index('Ankit'))
# print("Position of Patel ",tuple.index('Patel')) #generate error (KeyError)
print("Count of True",tuple.count(True))
print("Count of Patel",tuple.count('Patel'))
# tuple[0] = "Ankit Patel" #error because tuple is read only list (immutable)
# del tuple[0] #error because tuple is read only list (immutable)
print('good bye')