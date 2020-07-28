# Enter your code here. Read input from STDIN. Print output to STDOUT
# a=[]
# b=[]
test_case=int(input("Number of test case: "))
set_a=int(input("Number of elements in Set A: "))
elements_a=(input("Elements of Set A: "))
set_b=int(input("Number of elements in Set B: "))
elements_b=(input("Elements of Set B: "))
a=elements_a.split()
b=elements_b.split()
try:
    if (len(a)!=set_a and len(b)!=set_b):
        print("Please Enter Number of Elements in Sets properly separated by space")
    else:
        pass
except:
    pass
a=set(a)
b=set(b)
a=list(a)
b=list(b)
set_a=len(a)
set_b=len(b)
# print(a,b)
i=0
count=0
while i<set_a:
    j=0
    while j<set_b:
        if b[j]==a[i]:
            count+=1
        else:
            pass
        j+=1
    i+=1
if (count==set_a):
    print("Set A is subset of Set B")
else:
    print("Set A is not an subset of Set B")


