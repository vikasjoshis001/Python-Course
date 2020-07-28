set_A=input("Enter Elements of Set A: ")
n=int(input("Total Number of different sets: "))
set_n1=input("Elements of set n1: ")
set_n2=input("Elements of set n2: ")
A=set_A.split()
n1=set_n1.split()
n2=set_n2.split()
A=set(A)
n1=set(n1)
n2=set(n2)
diff1=A.difference(n1)
diff2=A.difference(n2)
print(diff2)
x=len(diff1)
y=len(diff2)
P=list(A)
Q=list(n1)
R=list(n2)
data_valid=True
while data_valid==True:
    i=0
    while i<len(P):
        j=0
        while j<len(Q):
            if (P[i]!=Q[j]):
                ans='answer'
                print("False")
                break
            else:
                pass
            j+=1
        i+=1
    if ans=='answer':
        break
    data_valid=False
    l=0
    while l<len(P):
        k=0
        while k<len(R):
            if (P[l]!=R[k]):
                ans='answer'
                print("False")
                break
            else:
                pass
            k+=1
        l+=1
    if ans=='answer':
        break


    if (len(diff1)>0 and len(diff2)>0):
        print("True")
    else:
        print("False")