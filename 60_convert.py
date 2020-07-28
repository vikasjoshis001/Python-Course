def print_formatted(number):
    for i in range (1,(number+1)):
        # print(i," ",int(0o22)," ",int(0h11)," ",int(0b5))
        x=bin(i)
        y=oct(i)
        z=hex(i)
        print(i,end=' ')
        print(y,end=' ')
        print(z,end=' ')
        print(x)

    print("\n")
    # your code goes here
n=int(input("Enter: "))
print_formatted(n)