while True:
    a=eval(input("Enter 1st Number: "))
    b=eval(input("Enter 2nd Number: "))
    operator=input("Enetr operator to operate: \n1.'+'\n2.'-'\n3.'*'\n4.'/'\n5.'%'\n")
    if (operator == '1'):
        add=a+b
        print ("Addition of ",a,"and ",b,"is ",add)
    elif (operator == '2'):
        sub=a-b
        print ("Substraction of ",a,"and ",b,"is ",sub)

    elif (operator == '3'):
        mul=a*b
        print ("Multiplication of ",a,"and ",b,"is ",mul)

    elif (operator == '4'):
        div=a/b
        print ("Division of ",a,"and ",b,"is ",div)

    elif (operator == '5'):
        rem=a%b
        print ("Reminder of ",a,"and ",b,"is ",rem)

    else:
        print("INVALID OPERATOR")
    ans=input("Do you want to use again: \n1.YES (press enter)\n2.NO (press q)\n").lower()
    if (ans == 'q'):
        exit()