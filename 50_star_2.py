n=int(input("How many Rows: "))
i=1
while i<=n:
    j=0
    k=0
    x=n-i
    while k<x:
        print(" ",end="")
        k+=1
    while j<i:
        print("*",end='')
        j+=1
    print("\n")
    i+=1