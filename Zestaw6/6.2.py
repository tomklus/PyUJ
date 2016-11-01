# Kod testujacy modul.
from points import *

import unittest

class TestPoint(unittest.TestCase): 
	def setUp(self): pass
	
	def test_str(self):
		self.assertEqual(Point(4,4).__str__(), "(4, 4)")
		
	def test_repr_pt(self):
		self.assertEqual(Point(4,33).__repr__(), "Point(4, 33)")
		
	def test_eq_pt(self):
		self.assertTrue(Point(4,33).__eq__(Point(4,33)))
		self.assertFalse(Point(2,11).__eq__(Point(4,22)))
		
	def test_ne_pt(self):
		self.assertTrue(Point(4,33).__ne__(Point(4,34)))
		self.assertFalse(Point(2,11).__ne__(Point(2,11)))
		
	def test_vec_add(self):
		self.assertEqual(Point(4,33).__add__(Point(1, 2)), Point(5, 35))
		
	def test_vec_sub(self):
		self.assertEqual(Point(4,33).__sub__(Point(1, 2)), Point(3, 31))
		
	def test_vec_mul(self):
		self.assertEqual(Point(4,3).__mul__(Point(1, 2)), Point(4, 6))
		
	def test_vec_cross(self):
		self.assertEqual(Point(1, 4).cross(Point(4,1)), -15)
		
	def test_vec_len(self):
		self.assertEqual(Point(4,3).length(), 5)
		
	def test_dist(self):
		self.assertEqual(Point(0,0).distance(Point(0,1)), 1)
	
	def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
