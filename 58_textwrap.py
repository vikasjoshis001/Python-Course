mystring=input("Enter a String: ")
width=int(input("Enter width: "))
length=len(mystring)
# z=length/width
# y=round(z,0)
i=0
while i<=length:
    j=0
    while j<width:
        print(mystring[i+j],end='')
        j+=1
    print("\n")
    i+=width
