import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
		self.assertEqual(sub_frac([1, 2], [2, 7]), [3, 14])

    def test_mul_frac(self): 
		self.assertEqual(mul_frac([3, 5], [2, 3]), [6, 15])

    def test_div_frac(self): 
		self.assertEqual(div_frac([3, 5], [2, 3]), [9, 10])

    def test_is_positive(self): 
		self.assertFalse(is_positive([-1, 1]))
		self.assertFalse(is_positive([1, -1]))
		self.assertTrue(is_positive([1, 4951]))
	
    def test_is_zero(self): 
		self.assertTrue(is_zero([0, 84]))

    def test_cmp_frac(self): 
		self.assertEqual(cmp_frac([3, 5], [2, 3]), -1)
		self.assertEqual(cmp_frac([3, 5], [6, 10]), 0)
		self.assertEqual(cmp_frac([1, 4], [2, 17]), 1)

    def test_frac2float(self): 
		self.assertEqual(frac2float([1, 2]), 0.5)
		self.assertEqual(frac2float([1, 4]), 0.25)
		self.assertEqual(frac2float([1, 16]), 0.0625)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
