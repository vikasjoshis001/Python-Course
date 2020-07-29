from itertools import product

A = input()
B = input()
A  = A.split(" ")
B = B.split(" ")
list1 = []
list2 = []
print(A[0])
print(A)
for i in range(0,len(A)):
    integer = int(A[i])
    list1.append(integer)
for j in range(0,len(B)):
    integer = int(B[j])
    list2.append(integer)
print(list1)
print(list2)
C = list(product(list1,list2))
print(C)
for k in range(0,len(C)):
     print (C[k],end=" ")