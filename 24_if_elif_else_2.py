# write a program to findout whether given shape is portrait, landscape or square using given length and width if elif decision making statement if 

#input: length & width 

# Input: length & width
length = int(input("Enter length: "))
width = int(input("Enter width: "))

if length > width:
    print("Landscape")
elif length < width:
    print("Portrait")
else:
    print("Square")
