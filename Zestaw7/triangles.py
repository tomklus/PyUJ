from points import Point
import math
import copy

class Triangle:
    """Klasa reprezentujaca trojkaty na plaszczyznie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        # Nalezy zabezpieczyc przed sytuacjz, gdy punkty sap wspolliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        if self.pt1.__eq__(self.pt2):
            if self.pt2.__eq__(self.pt3):
                raise ValueError

    def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[%s, %s, %s]" % (self.pt1.__str__(), self.pt2.__str__(), self.pt3.__str__())

    def __repr__(self):         # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle(%s, %s, %s, %s, %s, %s)" % (str(self.pt1.x), str(self.pt1.y), str(self.pt2.x), str(self.pt2.y), str(self.pt3.x), str(self.pt3.y))

    def __eq__(self, other):    # obsluga tr1 == tr2
        if self.pt1.__eq__(other.pt1):
            if self.pt2.__eq__(other.pt2):
                if self.pt3.__eq__(other.pt3):
                    return True
        return False

    def __ne__(self, other):        # obsluga tr1 != tr2
        return not self == other

    def center(self):           # zwraca srodek trojkata
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):             # pole powierzchni
        s = (self.pt1.distance(self.pt2) + self.pt2.distance(self.pt3) + self.pt3.distance(self.pt1)) / 2
        return math.sqrt(s * (s - self.pt1.distance(self.pt2)) * (s - self.pt2.distance(self.pt3)) * (
        s - self.pt3.distance(self.pt1)))

    def move(self, x, y):       # przesuniacie o (x, y)
        a = self.pt1.__add__(Point(x, y))
        b = self.pt2.__add__(Point(x, y))
        c = self.pt3.__add__(Point(x, y))
        return Triangle(a.x, a.y, b.x, b.y, c.x, c.y)

    def make4(self): 	           # zwraca lista czterech mniejszych
        Tr1 = copy.copy(self)
        Tr2 = copy.copy(self)
        Tr3 = copy.copy(self)
        Tr4 = copy.copy(self)
        Tr1.pt1 = Tr1.center()
        Tr2.pt2 = Tr2.center()
        Tr3.pt3 = Tr3.center()
        Tr4.pt1 = Point(float(self.pt1.x+self.pt2.x)/2, float(self.pt1.y+self.pt2.y)/2)
        return [Tr1, Tr2, Tr3, Tr4]
