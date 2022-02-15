from point import Point
from ec import EC

ec = EC()

p1 = Point(1, ec.genY(1))
p2 = Point(0, ec.genY(0))

print(p1)
print(p2)
print(p1+p2)