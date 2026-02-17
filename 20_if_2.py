# write a program to figure out whether given shape is portrait, or landscape or square using given length and width, 
#input: length & width 
length = int(input("Enter length"))
width = int(input("Enter width"))

if length>width:
    print("given shape is portrait")

if length<width:
    print("given shape is landscape")

if length==width:
    print("given shape is square")

print('good bye')