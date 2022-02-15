
class FieldNum():

    P = 7 # indicates the size of our finite field of integers MUST BE PRIME

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

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

    # -a
    # TODO: implement actual inverses
    def __NEG__(self):
        return FieldNum(-self.val)
    
    # a^b
    def __pow__(self, b):
        p = FieldNum.P
        a = self.val
       
        return FieldNum((a ** b) % p)
    
    def sqrt(self):

        return 0
