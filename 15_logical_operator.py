# num1 = int(input("Enter 1st number"))
# num2 = int(input("Enter 2nd number"))
# num3 = int(input("Enter 3rd number"))

num1 = 10 
num2 = 20 
num3 = 30

result = num1 < num2 and num2 < num3 # 1
print(f"{result} = {num1} < {num2} and {num2} < {num3}")

result = num1 > num2 or num2 < num3 # 1
print(f"{result} = {num1} > {num2} or {num2} < {num3}")

result = num1 > num2 or num2 > num3 # 0
print(f"{result} = {num1} > {num2} or {num2} > {num3}")

result = not (num1 > num2 or num2 > num3) # 0
print(f"{result} = not ({num1} > {num2} or {num2} > {num3})")
