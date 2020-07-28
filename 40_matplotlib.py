import matplotlib.pyplot as pyplot
y=['jan','feb','march','apr','may','jun','july','aug','sep','oct','nov','dec']
x=[1000,1200,800,700,1500,2000,400,250,1332,143,1450,321]
pyplot.ylabel("Months")
pyplot.xlabel("Lightbills")
pyplot.title("Graph of lightbills")
pyplot.plot(x,y)
pyplot.show()