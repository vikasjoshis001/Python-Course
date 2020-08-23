import cmath
import math

z = input()
z = complex(z)
x = z.real
y = z.imag
print(x,y)
x2 = x*x
y2 = y*y
sum = x2+y2
r = math.sqrt(sum)
print(r)
ph = cmath.phase(z)
print(ph)
