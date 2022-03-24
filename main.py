from ec import curEC
from modarith import Field

def generateGroupTable():
    pointList = curEC.points()
    length = len(pointList)
    print("      ", end="")
    for p in pointList:
        print(" {} ".format(p), end="")
    print()
    for i in range(0, length):
        print(pointList[i], end="")
        for j in range(0, length):
            p1 = pointList[i]
            p2 = pointList[j]
            p3 = p1 + p2
            print(" {} ".format(p3), end="")
        print()

def main():
    Field.m = 7
    generateGroupTable()
    

if __name__ == '__main__':
    main()