import time
import matplotlib.pyplot as pyplot
import math
print("Enter 'important' word five times to check your typing speed: ")
my="important"
i,count=0,0
time_now=time.localtime()
m=time_now.tm_min
s=time_now.tm_sec
y=[]
data_valid=True
# time_now=("Current time is ",str(time_now.tm_min),"M",str(time_now.tm_sec),"S")
# print (time_now)
while i<5:
    user=input("Enter it: ")
    if (user == 'important'):
        time_user = time.localtime()
        mu=time_user.tm_min
        su=time_user.tm_sec
        tm=mu-m
        ts=su-s
        print ("total time is ",abs(tm),"M",abs(ts),"S")
        m=mu
        s=su
        y.append(count)
    else:
        s=0
        a=0
        while data_valid==True:
            if len(user)<len(my):
                v=len(my)-len(user)
                print("you typed wrong total errors are ",v)
                y.append(v)
            elif len(user)>len(my):
                j=len(user)-len(my)
                print("you typed wrong total errors are ",j)
                y.append(j)
            else:
                while s<len(user):
                    if (user[s]==my[s]):
                        pass
                    elif (user[s]!=my[s]):
                        count+=1
                    s+=1
                print("you typed wrong total errors are ",count)
                y.append(count)
            data_valid=False
    i+=1
print(y)
x=[1,2,3,4,5]
pyplot.plot(x,y)
pyplot.xlabel("rounds")
pyplot.ylabel("errors")
pyplot.show()

