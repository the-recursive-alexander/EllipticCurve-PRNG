from point import Point
from ec import EC

def kPModule(k, P):
    newP = P
    for i in range(1, k):
        newP = newP + newP
    return newP

def newK(P, n, p):
    return (P.x + n) % p

def findFirstPoint():
    ec = EC()
    P = Point(0, ec.genY(0))
    x = P.x
    y = P.y

    i = 0
    while(type(x) != int or type(y) != int):
        P = Point(i, ec.genY(i))
        x = P.x
        y = P.y
        i = i + 1
        print(P)
    return P

def main():
    ec = EC()
    SEED = 3
    p = 17
    P = findFirstPoint()
    N = 10
    k = SEED

    print("P is ", P)

    for i in range(0, N):
       
        newP = kPModule(k, P)
        print(newP.x)
        k = newK(newP, i, p)


    return

if __name__ == "__main__":
    main()