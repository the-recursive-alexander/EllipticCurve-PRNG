from point import Point
from ec import EC
from modarith import FieldNum

p = FieldNum.P

print("addition:")
for i in range(0, p):
    for j in range(0, p):
        a = FieldNum(i)
        b = FieldNum(j)
        print(a+b, end = " ")
    print()

print("multiplication:")
for i in range(0, p):
    for j in range(0, p):
        a = FieldNum(i)
        b = FieldNum(j)
        print(a*b, end = " ")
    print()

print("powers:")
a = FieldNum(3)
for i in range(0, p):
    print(a**i)

print(a**6)