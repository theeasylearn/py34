students = ['nirav','vishvam','utsav','harmil']
print(students)
print(students[0]) #will print student name at 0th position 
print(students[1]) #will print student name at 1st position 
print(students[2]) #will print student name at 2nd position 
print(students[0:2]) #will print student name from 0th position to 2nd position
print(students[:3]) #will print 1st three student name 
print(students[2:]) #will print all student name from 2nd position onwards
students[0] = "Nirav bariya"
del students[3]
students.append('ram') #will insert new item at the end 
students.append(100) 
students.append(3.14) 
students.append(True)
print(students) 
box = [100,12.7,False,'bhavnagar']
print(box)
print(box * 2)
print(students + box)
another_list = students + box  #create new list using 2 list along with + operator
print(another_list)