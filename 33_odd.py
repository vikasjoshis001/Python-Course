def odd(n):
    for i in range(1,2*n):
        if (i%2==1):
            print(i)
def even(n):
    for i in range(0,2*n):
        if (i%2==0):
            print(i)
ans=input("What to you want to print EVEN(E) or ODD(O): ").lower()
n=eval(input("Enter total numbers you want to print: "))
if (ans=='o'):
    odd(n)
else:
    even(n)
