num1 = int(input("Enter number"))
num2 = int(input("Enter another number"))

result = num1 is num2 
print(f"{result} {num1} is {num2}",id(num1),id(num2))

result = num1 is not num2 
print(f"{result} {num1} is not {num2}",id(num1),id(num2))