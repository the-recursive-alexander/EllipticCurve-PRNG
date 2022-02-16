from point import *
from ec import curEC
from modarith import FieldNum
import unittest

class Test(unittest.TestCase):

    def test_addition_in_field(self):
        p = FieldNum.P
        for i in range(0, p):
            for j in range(0, p):
                a = FieldNum(i)
                b = FieldNum(j)
                self.assertEqual(int(a+b), (a.val + b.val) % p)

    def test_subtraction_in_field(self):
        p = FieldNum.P
        for i in range(0, p):
            for j in range(0, p):
                a = FieldNum(i)
                b = FieldNum(j)
                self.assertEqual(int(a-b), (a.val - b.val) % p)

    def test_multiplication_in_field(self):
        p = FieldNum.P
        for i in range(0, p):
            for j in range(0, p):
                a = FieldNum(i)
                b = FieldNum(j)
                self.assertEqual(int(a*b), (a.val * b.val) % p)

    def test_inverse_in_field(self):
        p = FieldNum.P
        inverses = [1, 4, 5, 2, 3, 6]
        for i in range(1, p):
            a = FieldNum(i)
            self.assertEqual(int(~a), inverses[i-1])

    def test_point_display(self):
        a = Point(1, 2)
        b = Point(3, 4)
        self.assertEqual(str(a), "(1, 2)")
        self.assertEqual(str(b), "(3, 4)")

    def test_point_doubling(self):
        a = Point(0, 3)
        c = a + a
        self.assertEqual(str(c), "(2, 3)")
        FieldNum.P = 17
        b = Point(14, 0)
        d = b + b
        self.assertEqual(str(d), "(-, -)")
        FieldNum.P = 7
    
    def test_point_addition(self):
        a = Point(2, 4)
        b = Point(0, 4)
        c = a + b
        self.assertEqual(str(c), "(5, 3)")

    def test_addition_with_identity(self):
        a = PointID()
        b = Point(0, 3)
        self.assertEqual(str(a), "(-, -)")
        self.assertEqual(str(a+a), "(-, -)")
        self.assertEqual(str(a+b), str(b))
        self.assertEqual(str(b+a), str(b))
        c = a + a + a + a
        d = a + b + a + a
        self.assertEqual(str(c), str(a))
        self.assertEqual(str(d), str(b))
        a2 = PointID()
        self.assertEqual(a, a2)
        c = Point(0, 4)
        self.assertEqual(str(b+c), "(-, -)")


    def test_scalar_multiplication_of_points(self):
        a = Point(0,3)
        self.assertEqual(str(a*1), str(a))
        self.assertEqual(str(a*2), str(Point(2, 3)))
        self.assertEqual(str(a*3), str(Point(5, 4)))
        self.assertEqual(str(a*4), str(Point(4, 6)))
        self.assertEqual(str(a*5), str(Point(4, 1)))

    """
    # creates a table of points in the group created by the finite field F_7 under point addition
    def test(self):
        points = [Point(0, 3), Point(0, 4), Point(2, 3), Point(2, 4), Point(4, 1), Point(4, 6), Point(5, 3), Point(5, 4)]
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                print(points[i] + points[j], end=" ")
            print()
    """
    

if __name__ == '__main__':
    FieldNum.P = 7
    (curEC.A, curEC.B) = (3, 2)
    unittest.main()

    
