n=int(input("How many Rows: "))
i=1
while i<=n:
    j=n+1
    k=1
    # x=(n+1)-k
    while k<i:
        print(" ",end="")
        k+=1
    while j>i:
        print("*",end='')
        j-=1
    print("\n")
    i+=1