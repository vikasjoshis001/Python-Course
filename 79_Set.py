setM = set()
setN = set()
setA = set()
setB = set()
setC = set()
Mlist = []
Nlist = []

M = int(input())
str = input()
Mlist = str.split(" ")
for i in range(len(Mlist)):
    setM.add(int(Mlist[i]))

N = int(input())
s = input()
Nlist = s.split(" ")
for i in range(len(Nlist)):
    setN.add(int(Nlist[i]))

setA = setM.union(setN)
setB = setM.intersection(setN)
setC = setA.difference(setB)
setC = sorted(setC)
print(setM)
print(setN)
print(setA)
print(setB)
print(setC)


