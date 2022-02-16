from ec import curEC
from modarith import FieldNum

class Point():

    def __init__(self, x, y):
        self.x = FieldNum(x)
        self.y = FieldNum(y)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    """
    Adds two points together according to the binary operation
    defined on a finite field of points belonging to an elliptic
    curve E: y^2 = x^3 + ax + b

    Adding together the points P(x_p, y_p) and Q(x_q, y_q) 
    yields R(x_r, y_r) and 

    x_r = s^2 - x_p - y_p
    y_r = -y_p + s(x_p - x_r)

    where

    s = (y_p - y_q) / (x_p - x_q), if P is not equal to Q
    s = (3x_p^2 + a) / (2y_p) if P = Q

    in cryptography, these equations are done over a finite 
    field, so we mod each one by some large prime p

    for a PRNG, we only use the case when P = Q (?)
    """
    def __add__(self, point2):
        (x_p, y_p, x_q, y_q) = (self.x, self.y, point2.x, point2.y)

        if(point2 is PointID()):
            return self
        else:
            if(x_p == x_q and y_p == y_q):
                s = (FieldNum(3)*(x_p**2) + FieldNum(curEC.a)) / (FieldNum(2)*y_p)
            else:
                try:
                    s = (y_p - y_q) / (x_p - x_q)
                except:
                    return PointID()

            x_r = s**2 - x_p - x_q
            y_r = s*(x_p - x_r) - y_p
            
            return Point(x_r.val, y_r.val)
    
    def __mul__(self, a):
        P = self
        for i in range(1, a):
            P = self.__add__(P)
        return P

class PointID(Point, object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PointID, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.x = '-'
        self.y = '-'
    
    def __str__(self):
        return "(-, -)"

    def __add__(self, other):
        if other is PointID():
            return PointID()
        else:
            return other