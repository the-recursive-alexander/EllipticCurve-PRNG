
class Field(object):
    m = 7 # indicates the size of our finite field of integers MUST BE PRIME

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Field, cls).__new__(cls)
        return cls.instance
    
    

class FieldNum():

    def __init__(self, val):
        self.val = val % Field.m

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __int__(self):
        return self.val

    # a+b
    def __add__(self, fieldNum):
        p = Field.m
        a = self.val
        b = fieldNum.val

        return FieldNum((a + b) % p)

    # a-b
    def __sub__(self, fieldNum):
        p = Field.m
        a = self.val
        b = fieldNum.val
        return FieldNum((a - b) % p)
    # a*b
    def __mul__(self, fieldNum):
        p = Field.m
        a = self.val
        b = fieldNum.val

        return FieldNum((a * b) % p)

    # -a (additive inverse)
    def __neg__(self):
        return 


    # ~a (multiplicative inverse)
    # TODO: make more efficient
    def __invert__(self):
        p = Field.m
        a = self.val
        for i in range(0, p):
            if((a * i) % p == 1):
               return FieldNum(i)
        return -1
    
    def __truediv__(self, fieldNum):
        p = Field.m
        a = self.val
        b = fieldNum.val
        for i in range(0, p):
            if((b * i) % p == a):
                return FieldNum(i)
        return -1

    # a**b
    def __pow__(self, b):
        p = Field.m
        a = self.val
       
        return FieldNum((a ** b) % p)
    
    # sqrt(a) = b
    # returns list of FieldNums
    # TODO: create test suite
    def sqrt(self):
        p = Field.m
        a = self.val
        ans_list = []
        for i in range(0, p):
            b = FieldNum(i)
            if ((b*b).val == a):
                ans_list.append(b)
        return ans_list

    def __EQ__(self, fieldNum):
        return self.val == fieldNum.val