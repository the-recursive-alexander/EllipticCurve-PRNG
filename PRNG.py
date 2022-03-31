from point import *
from ec import *
from modarith import *

def kPModule(k, P, n):
    retPoint = P*k
    if(retPoint.x == '-'):
        k1 = (P.y + FieldNum(n)).val
        retPoint = P*k1
    return retPoint

def newK(P, n):
    return (P.x + FieldNum(n)).val

def findFirstPoint(i):
    return curEC.findPoint(i)
    
def main():
    print("Setting prime...")
    Field.m = 2927
    print("Done.")
    print("Initializing Parameters...")
    n = int(input("Print how many numbers?: "))
    seed = 1453
    print("Done.")
    print("Determining a start point, P...")
    P = Point(1, 16157) #curEC.points()[3]
    print("Point is {}".format(str(P)))
    print("Done.")
    print("Setting Elliptic Curve...")
    ec.curEC = EC(0, 7)
    print("Done.")

    print("Printing Random Numbers...")
    k = seed
    f = open("output.txt", 'w')
    for i in range(0,n):
        P = kPModule(k, P, i)
        f.write(str(bin(P.x.val))[2:])
        f.write("\n")
        k = newK(P, i)
    f.close()
    print("Done.")

if __name__ == "__main__":
    main()