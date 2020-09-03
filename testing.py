from Point import Point
from util import distance

y1 = int(input('Enter y1: '))
x1 = int(input('Enter x1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

a = Point(x1,y1)
b = Point(x2,y2)
c = distance(a,b)

print('Distance is ' + str(c))
