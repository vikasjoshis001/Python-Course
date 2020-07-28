import time
import matplotlib.pyplot as pyplot

times=[]
mistakes=0
i=0
print("This Programmes Helps you to type faster.You have tp type word 'important' for five times")
input("Enter to continue")
while i<5:
    start=time.time()
    print ("Type here: ")
    word=input()
    end=time.time()
    total=end - start
    times.append(total)
    if (word != 'important'):
        mistakes+=1
    i+=1

print("Your total mistakes are ",mistakes)
print("Your Evolution is: ")
time.sleep(5)
x=[1,2,3,4,5]
y=times
pyplot.plot(x,y)
pyplot.xlabel("Number of attempts")
pyplot.ylabel("Total time")
pyplot.show()
