#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    splited = s.split(" ");
    str1=''
    str2=''
    space =" "
    a=''
    l=[]
    print(len(splited))
    for i in range(0,len(splited)):
        for ele in splited[i]: 
            print(ele) 
            l.append(ele)
            a[i]=l[i]
            print(a)
    print(l)
    # str1+=l[]
    # s1 = str1.capitalize()
    # s2 = str2.capitalize()
    # a+=s1
    # a+=space
    # s+=s2
    # print(s)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    solve(s)

    # result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
