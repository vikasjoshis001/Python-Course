import matplotlib.pyplot as pyplot
print ("This program is to show your marks of different subject: ")
subject=["Maths","BEE","Physics","EG","EM"]
marks=[]
i=0
while i<5:
    print("Enter marks of ",subject[i],": ")
    m=eval(input())
    marks.append(m)
    i+=1
pyplot.bar(subject,marks)
pyplot.xlabel("Subjects")
pyplot.ylabel("Marks")
pyplot.title("Marks of different Subjects")
pyplot.show()