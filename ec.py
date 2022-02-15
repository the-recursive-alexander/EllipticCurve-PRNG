from math import sqrt

# equation of the form: y^2 = x^3 + ax + b

A = 3 # the global parameter A
B = 4 # the global parameter B

class EC(object):

    def __init__(self):
        self.a = A
        self.b = B

    def genY(self, x, pos = True):
        a = self.a
        b = self.b

        if pos:
            return sqrt(pow(x,3) + a*x + b)
        else:
            return -sqrt(pow(x,3) + a*x + b)