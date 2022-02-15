
from distutils.log import ERROR


class FieldNum():

    P = 7 # indicates the size of our finite field of integers MUST BE PRIME

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __int__(self):
        return self.val

    # a+b
    def __add__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val

        return FieldNum((a + b) % p)

    # a-b
    def __sub__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val
        return FieldNum((a - b) % p)
    # a*b
    def __mul__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val

        return FieldNum((a * b) % p)

    # -a (additive inverse)
    def __neg__(self):
        return ERROR("not implemented")


    # ~a (multiplicative inverse)
    # TODO: make more efficient
    def __invert__(self):
        p = FieldNum.P
        a = self.val
        for i in range(0, p):
            if((a * i) % p == 1):
               return FieldNum(i)
        return ERROR("inverse not found")
    
    def __truediv__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val
        for i in range(0, p):
            if((b * i) % p == a):
                return FieldNum(i)
        return ERROR("result not found")

    # a**b
    def __pow__(self, b):
        p = FieldNum.P
        a = self.val
       
        return FieldNum((a ** b) % p)
    
    def sqrt(self):

        return 0

    def __EQ__(self, fieldNum):
        return self.val == fieldNum.val