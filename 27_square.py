def square(N):
    if (N!=0):
        N=(N**2)+square(N-1)
    return N
N=eval(input("Enter number: "))
n=square(N)
print (n)