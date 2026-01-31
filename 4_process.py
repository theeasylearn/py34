# write a program to accept 3 subject marks of student, calculate & display total & average using it
maths = input("Enter maths marks")
science = input("Enter science marks")
english = input("Enter english marks")
maths = int(maths)
science = int(science)
english = int(english) 
total = maths + science + english
print(f"total = {total}")
average = total / 3 
print(f"average = {average}")