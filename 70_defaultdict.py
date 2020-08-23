from collections import defaultdict

integer = input()
z = integer.split(" ")
numbers = []
for i in range(len(z)):
    numbers.append(int(z[i]))
n = numbers[0]
m = numbers[1]
val = 0

letters1 = []
letters2 = []

for i in range(n):
    letter1 = input()
    letters1.append(letter1)

for j in range(m):
    letter2 = input()
    letters2.append(letter2)

for i in range(len(letters2)):
    val = 0
    for j in range(len(letters1)):
        if letters2[i] == letters1[j]:
            print(j+1,end=" ")
        else:
            val += 1
    if (val == len(letters1)):
        print(-1,end=" ")
    print("\r")