#write a program to figure out square or cube of given number. if number is odd calculate & display square if number is even calculate and display cube.
number = int(input("Enter any number")) # 10
reminder = number % 2 #0
if reminder == 0:
    result = number * number * number
else:
    result = number * number

print("result is ",result)
