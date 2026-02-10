# student = ['utsav','patel',20,True,True,13.8]
student = {'name':'utsav','surname':'Patel','gender':True,'isMarried':False,'birthdate':13.8}
print(student)
#access specific value
print(student['name']) #utsav
print(student['gender']) #True
#add new key value pair 
student['email'] = 'utsav@gmail.com'
#update existing key value
student['birthdate'] = "13-Aug-2005"
#remove key value pair
del student['isMarried']
print(student)