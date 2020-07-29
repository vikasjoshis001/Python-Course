from itertools import combinations

S = input()
l = S.split(" ")
k = int(l[1])
a = []
for i in range(0,len(l[0])):
    a.append(l[0][i])
a.sort()
b = ''
word = b.join(a)

for g in range(1,k+1):
    C = list(combinations(word,g))
    C.sort()
    for i in range(0,len(C)):
        for j in range(0,len(C[i])):
            print(C[i][j],end=(""))
        print('\r')