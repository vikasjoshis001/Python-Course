a=input("Enter 1st string: ")
b=input("Enter 2nd string: ")
c=input("Enter 3rd string: ")
if (ord(a[0])<ord(b[0]) and ord(a[0])<ord(c[0]) and ord(b[0])<ord(c[0])):
    print(a,b,c)

if (ord(a[0])<ord(b[0]) and ord(a[0])<ord(c[0]) and ord(c[0])<ord(b[0])):
    print(a,c,b)

if (ord(b[0])<ord(a[0]) and ord(b[0])<ord(c[0]) and ord(a[0])<ord(c[0])):
    print(b,a,c)

if (ord(b[0])<ord(a[0]) and ord(b[0])<ord(c[0]) and ord(c[0])<ord(a[0])):
    print(b,c,a)

if (ord(c[0])<ord(b[0]) and ord(c[0])<ord(a[0]) and ord(a[0])<ord(b[0])):
    print(c,a,b)

if (ord(c[0])<ord(b[0]) and ord(c[0])<ord(a[0]) and ord(b[0])<ord(a[0])):
    print(c,b,a)****
