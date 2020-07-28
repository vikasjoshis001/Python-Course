s = input("Enter your name")
x = s.split(" ")
y = []

for i in range(0,len(x)):
    if x[i] == '':
        y.append(x[i])
    else:
        try:
            int(x[i][0])
            y.append(x[i])
        except :
            if (ord(x[i][0]) > 96) and (ord(x[i][0])) < 123:
                c = ord(x[i][0])
                c = c - 32
                c = chr(c)
                word = c + x[i][0 + 1:]
                y.append(word)
            else:
                y.append(x[i])
z = " ".join(y)
print(z)

