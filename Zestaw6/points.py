import math	
class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): 	         # zwraca string "(x, y)"
		return "(%s, %s)" % (self.x, self.y)

    def __repr__(self): 	        # zwraca string "Point(x, y)"
		return "Point(%s, %s)" % (self.x, self.y)
	
    def __eq__(self, other): 	   # obsluga point1 == point2
		if self.x == other.x:
			if self.y == other.y:
				return True
		return False

    def __ne__(self, other):        # obsluga point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): 	  # v1 + v2
		return Point(self.x + other.x, self.y + other.y)


    def __sub__(self, other): 	  # v1 - v2
		return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other): 	  # v1 * v2, iloczyn skalarny
		return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def distance(self, other): 
		return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))
    
    def length(self): 	          # dlugosc wektora
		return math.sqrt(self.x * self.x + self.y * self.y)

