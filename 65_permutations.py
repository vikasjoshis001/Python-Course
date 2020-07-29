from itertools import permutations

S = input()
l = S.split(" ")
k = int(l[1])
word = l[0]
perm = list(permutations(word,k))
perm.sort()
for i in range(0,len(perm)):
    for j in range(0,len(perm[i])):
         print(perm[i][j],end=(""))
    print('\r')
