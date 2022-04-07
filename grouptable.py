# need to import system so that our imports can find the modules in the lib folder
import sys
sys.path.insert(0, './lib')
##############################################

from ec import curEC
from modarith import Field

def generateGroupTable():
    f = open("./output/table.txt", "w")
    pointList = curEC.points()
    length = len(pointList)
    #print("      ", end="")
    f.write("      ")
    for p in pointList:
        #print(" {} ".format(p), end="")
        f.write("   {}   ".format(p))
    #print()
    f.write("\n")
    for i in range(0, length):
        #print(pointList[i], end="")
        f.write(str(pointList[i]))
        for j in range(0, length):
            p1 = pointList[i]
            p2 = pointList[j]
            p3 = p1 + p2
            #print(" {} ".format(p3), end="")
            f.write("   {}   ".format(p3))
        f.write("\n")
        #print()
    f.close()

def main():
    Field.m = 7
    generateGroupTable()
    

if __name__ == '__main__':
    main()