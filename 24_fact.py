def fact(n) : lambda x: n*fact(n-1) if (n>0) else print("1")
fact(5)