import math

AB = float(input())
BC = float(input())

AC = AB/BC

phai = math.atan(AC)

theta = (180 - phai)/2

print(theta)