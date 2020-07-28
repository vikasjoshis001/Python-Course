n=eval(input("Enter Number to check: "))
for i in range (2,n):
    if (n%i==0):
        print ("Number is not prime")
        break
else:
    print("Number is prime")