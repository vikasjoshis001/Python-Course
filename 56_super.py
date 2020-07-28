i=0
data_valid=[]
set_A=input("Enter Elements of Set A: ")
A=set(set_A)
n=int(input("Total Number of different sets: "))
while i<n:
    set_n=input("Elements of set: ")
    l=set_n.split()
    s=set(l)
    unknown=s.difference(A)
    z=A.difference(l)
    list_1=list(A)
    # list_2=list(s)
    if (list_1!=l):
        valid="False"
    elif (len(z)>0):
        valid="False"
    else:
        valid="True"
    data_valid.append(valid)
    i+=1
if (valid[0]=='False' or valid[1]=='False'):
    print("False")
else:
    print("True")

