#list related methods 
list = [] #empty list 
print(list)
list.append('kiwi')
list.append('pinapple')
list.append('mango')
list.append('mango')
list.append('banana')
print(list)
list.insert(0,'apple')
list.insert(1,'graps')
print(list)
print("apple is at position ",list.index('apple')) #0
# print("watermelon is at position ",list.index('watermelon')) 
#if you try to findout position of item not in list, it will return error and code will stop
print("count of mango ",list.count('mango'))
list.remove('mango') #remove mango if any
list.pop(1) #remove value at 1st position
print(list)
# list2 = list #create reference of list into list2 (reference means same list, not 2 separate list)
list2 = list.copy()
list.clear()
print(list)
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
print('good bye')