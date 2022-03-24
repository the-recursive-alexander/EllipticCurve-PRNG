from point import *
from ec import *
from modarith import *

def kPModule(k, P):
    return P*k

def newK(P, n):
    if(P.x == '-'):
        return 0
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
    for i in range(0,n):
        P = kPModule(k, P)
        print(P.x)
        k = newK(P, i) 
    print("Done.")

if __name__ == "__main__":
    main()