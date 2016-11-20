import unittest
from fracs import *

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_str(self):
        self.assertEqual(Frac(5,1).__str__(), "5")
        self.assertEqual(Frac(5, 2).__str__(), "5/2")

    def test_repr(self):
        self.assertEqual(Frac(5,1).__repr__(), "Frac(5, 1)")
        self.assertEqual(Frac(5, 2).__repr__(), "Frac(5, 2)")

    def test_cmp(self):
        self.assertEqual(Frac(2, 2).__cmp__(Frac(4, 4)), 0)
        self.assertEqual(Frac(2, 1).__cmp__(Frac(4, 1)), -1)
        self.assertEqual(Frac(2, 1).__cmp__(Frac(1, 4)), 1)


    def test_add(self):
        self.assertEqual(Frac(1, 2).__add__(Frac(1, 3)), Frac(5, 6))

    def test_sub(self):
        self.assertEqual(Frac(1, 2).__sub__(Frac(1, 1)), Frac(-1, 2))

    def test_rsub(self):
        self.assertEqual(Frac(1, 2).__rsub__(1), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(Frac(1, 2).__mul__(Frac(1, 2)), Frac(1, 4))

    def test_rmul(self):
        self.assertEqual(Frac(1, 2).__rmul__(1), Frac(1, 2))

    def test_div(self):
        self.assertEqual(Frac(1, 2).__div__(Frac(1, 2)), Frac(1, 1))

    def test_rdiv(self):
        self.assertEqual(Frac(1, 2).__rdiv__(2), Frac(1, 4))


    def test_pos(self):
        self.assertEqual(Frac(-1, 1).__pos__(), Frac(-1, 1))

    def test_neg(self):
        self.assertEqual(Frac(1, 84).__neg__(), Frac(-1,84))

    def test_float(self):
        self.assertEqual(Frac(1, 2).__float__(), 0.5)
        self.assertEqual(Frac(1, 4).__float__(), 0.25)
        self.assertEqual(Frac(1, 16).__float__(), 0.0625)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy