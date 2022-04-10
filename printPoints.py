import sys
sys.path.insert(0, './lib')

from point import *
from ec import *
from modarith import *


def main():
    f = open("./output/points.txt", 'w')
    Field.m = int(input("Size of Field: "))
    a = int(input("Elliptic Curve a: "))
    b = int(input("Elliptic Curve b: "))
    ec.curEC = EC(a, b)
    points = ec.curEC.points()
    for point in points:
        print(point)
        f.write(str(point))
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()