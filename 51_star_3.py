n=int(input("How many Rows: "))
i=1
while i<=n:
    x=n+1
    j=x
    while j>i:
        print("*",end='')
        j-=1
    print("\n")
    i+=1