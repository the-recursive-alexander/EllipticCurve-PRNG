from point import *
from ec import *
from modarith import *

def kPModule(k, P):
    return P*k

def newK(P, n):
    return (P.x + FieldNum(n)).val

def findFirstPoint(i):
    return curEC.findPoint(i)
    
def main():
    print("Setting prime...")
    FieldNum.P = 491
    print("Done.")
    print("Initializing Parameters...")
    n = 10
    seed = 79
    print("Done.")
    print("Determining a start point, P...")
    P = findFirstPoint(8)
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