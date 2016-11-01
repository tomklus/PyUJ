from triangles import Triangle
from points import Point
import unittest

class TestTriangle(unittest.TestCase): 
	
	def setUp(self): pass
	
	def test_str_tri(self):
		self.assertEqual(Triangle(0,0,0,3,3,0).__str__(), "[(0, 0), (0, 3), (3, 0)]")
	
	def test_repr_tri(self):
		self.assertEqual(Triangle(0,0,0,3,3,0).__str__(), "[(0, 0), (0, 3), (3, 0)]")
		
	def test_eq_tri(self):
		self.assertTrue(Triangle(0,0,0,3,3,0).__eq__(Triangle(0,0,0,3,3,0)))
		self.assertFalse(Triangle(0,0,0,3,0,3).__eq__(Triangle(0,0,0,3,3,0)))
		
	def test_ne_tri(self):
		self.assertFalse(Triangle(0,0,0,3,3,0).__ne__(Triangle(0,0,0,3,3,0)))
		self.assertTrue(Triangle(0,0,0,3,0,3).__ne__(Triangle(0,0,0,3,3,0)))

	def test_center_tri(self):
		self.assertEqual(Triangle(0,0,0,3,3,0).center(), Point(1,1))
		
	def test_area_tri(self):
		self.assertEqual(round(Triangle(0,0,0,3,3,0).area(), 5), 4.5)
		
	def test_move_tri(self):
		self.assertEqual(Triangle(0,0,0,3,3,0).move(1, 0), Triangle(1,0,1,3,4,0))
	
	def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

