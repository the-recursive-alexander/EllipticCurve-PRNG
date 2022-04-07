# need to import sys so that our imports below can find the modules in the lib folder
import sys
sys.path.insert(0, './lib')
#################################################

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
    P = Point(114, 2255) #(1, 1522) #(114, 2255)
    print("Point is {}".format(str(P)))
    print("Done.")
    print("Setting Elliptic Curve...")
    ec.curEC = EC(0, 7)
    print("Done.")

    print("Printing Random Numbers...")
    k = seed
    f = open("./output/output.data", 'w')
    for i in range(0,n):
        P = kPModule(k, P, i)
        f.write(str(bin(P.x.val))[2:])
        print(P.x)
        k = newK(P, i)
    f.close()
    print("Done.")

if __name__ == "__main__":
    main()