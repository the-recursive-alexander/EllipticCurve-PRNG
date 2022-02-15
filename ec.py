from math import sqrt

# equation of the form: y^2 = x^3 + ax + b
# to use the global EC with the parameters below import curEC
A = 3
B = 2

class __EC__(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "y^2 = x^3 + {}x + {}".format(self.a, self.b)

    # TODO: broken, does not interact with fields
    def genY(self, x, pos = True):
        a = self.a
        b = self.b

        if pos:
            return sqrt(pow(x,3) + a*x + b)
        else:
            return -sqrt(pow(x,3) + a*x + b)

curEC = __EC__(A, B)
