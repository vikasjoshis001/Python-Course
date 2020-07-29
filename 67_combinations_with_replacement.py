from itertools import combinations_with_replacement

S = input()
l = S.split(" ")
k = int(l[1])
a = []
for i in range(0,len(l[0])):
    a.append(l[0][i])
a.sort()
b = ''
word = b.join(a)

C = list(combinations_with_replacement(word,k))
C.sort()
for i in range(0,len(C)):
    for j in range(0,len(C[i])):
        print(C[i][j],end=(""))
    print('\r')