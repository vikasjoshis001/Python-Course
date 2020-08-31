from collections import OrderedDict
N = int(input())
mylist = []
dict = {}
l = []
dict = OrderedDict()
str = ["a","b"]

for i in range(N):
    S = input()
    mylist = S.split(" ")
    val = mylist[-1]
    for i in range(len(mylist)):
        try:
            mylist[i] = int(mylist[i])
        except:
            l.append(mylist[i])
    x = " ".join(l)
    l = []
    
    for i in range(len(str)):
        if x==str[i]:
            dict[str[i]] += int(val)
            break
    else:
        str.append(x)
        dict[x] = int(val)


str.pop(0)
str.pop(0)
for i in range(len(str)):
    print(str[i],end = ' ')
    print(dict[str[i]])
