from modarith import *
import point

# equation of the form: y^2 = x^3 + ax + b

A = 3
B = 2

class EC(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "y^2 = x^3 + {}x + {}".format(self.a, self.b)

    def __repr__(self):
        return "y^2 = x^3 + {}x + {}".format(self.a, self.b)

    """
    returns a list of Point objects
    """
    def points(self):
        a = FieldNum(self.a)
        b = FieldNum(self.b)

        p = Field.m
        point_list = [point.PointID()]
        for x in range(0, p):
            y = (FieldNum(x**3)+a*FieldNum(x)+b).sqrt()
            if y:
                for i in range(0, len(y)):
                    point_list.append(point.Point(x, y[i].val))
            #print(x, y)
        return point_list

    def findPoint(self, n):
        a = FieldNum(self.a)
        b = FieldNum(self.b)
        
        y = '-'
        for x in range(0, n):
            y_list = (FieldNum(x**3)+a*FieldNum(x)+b).sqrt()
            if y_list:
                y = y_list[0].val
        return point.Point(x, y)

curEC = EC(A, B)