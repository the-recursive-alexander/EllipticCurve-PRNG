from ec import EC
from modarith import FieldNum

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ec = EC() 
    
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

    for a PRNG, we only use the case when P = Q (?)
    """
    def __add__(self, point2):
        (x_p, y_p, x_q, y_q) = (self.x, self.y, point2.x, point2.y)

        if(x_p == x_q and y_p == y_q):
            s = (3*pow(x_p,2) + self.ec.a) / (2*y_p)
        else:
            s = (y_p - y_q) / (x_p - x_q)

        x_r = pow(s,2) - x_p - x_q
        y_r = s*(x_p - x_r) - y_p

        return Point(x_r, y_r)