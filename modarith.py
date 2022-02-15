
class FieldNum():

    P = 17 # indicates the size of our finite field of integers MUST BE PRIME

    def __init__(self, val):
        self.val = val

    def __add__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val

        return (a + b) % p

    def __sub__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val

        return (a - b) % p

    def __mul__(self, fieldNum):
        p = FieldNum.P
        a = self.val
        b = fieldNum.val

        return (a * b) % p

    def __NEG__(self):
        return -self.val