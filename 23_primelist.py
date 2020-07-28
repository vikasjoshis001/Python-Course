def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            return n
def primeproducer(N):
    n,c=1,1
    while c<=N:
        n=nextprime(n)
        yield n
        c+=1
N=int(input("Enter total prime numbers you want"))
l=[x for x in primeproducer(N)]
print(l)