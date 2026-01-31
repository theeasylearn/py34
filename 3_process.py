# write a program to figure out simple interest of given amount rate and year 
amount = input("Enter principal amount") #string 
rate = input("Enter rate of interest") 
year = input("Enter year ")
#calculate interest amount 
#  interest = amount * rate * year / 100
#convert string into integer 
amount = int(amount)
rate = float(rate)
year = float(year)
#process 
interest =  (amount * rate * year) / 100
#display interest
# print("simple interest = ",interest) or
print(f"simple interest = {interest}")
