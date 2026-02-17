# write a program to calculate amount of profit or loss or break even using given purchase & sale price
sale_price = float(input("enter sale price"))
purchase_price = float(input("enter purchase price"))

difference = sale_price - purchase_price 
if difference>0:
    print(f"you have made profit of {difference}")

if difference<0:
    print(f"you have made loss of {difference}")

if difference==0:
    print("you have made no loss no profit (break even)")

print("good bye.")
