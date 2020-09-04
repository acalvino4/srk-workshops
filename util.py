import math
from Point import Point

# takes in to point  objects, returns distance
def distance(a, b):
  x1=a.x
  y1=a.y
  x2=b.x
  y2=b.y
  intermediate = (x2-x1)**2 + (y2-y1)**2
  return math.sqrt(intermediate)
