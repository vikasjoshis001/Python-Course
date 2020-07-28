import math
import os
import random
import re
import sys
s = "hello world"
str1=''
str2=''
for i in range(0,len(s)):
    if s[i] == " ":
        k = i+1
        l = len(s)-k
        m = i + l
        for j in range(k,(m+1)):
            str2+=s[j]
        break
    else:
        str1+=s[i]
z = ord(str1[0]) 
print(str1[0])
print(z)
c = z - 32
o = chr(c)
print(o)
str1.capitalize()
print(str1)


