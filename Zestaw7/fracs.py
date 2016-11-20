import fractions
import sys

class Frac:

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        return "%s/%s" % (str(self.x), str(self.y))

    def __repr__(self):
        return "Frac(%s, %s)" % (str(self.x), str(self.y))

    def __cmp__(self, other):
        if other.__float__() == self.__float__():
            return 0
        elif self.__float__() > other.__float__():
            return 1
        else:
            return -1

    # frac + frac , frac + int
    def __add__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return Frac(self, 1).__add__(other, 1)
            return other.__add__(Frac(self, 1))

        if isinstance(other, int):
            return self.__add__(Frac(other,1))


        res = Frac(0, lcm(self.y, other.y))

        if self.y != res.y:
            res.x += res.y / self.y * self.x
        else:
            res.x += self.x

        if other.y != res.y:
            res.x += res.y / other.y * other.x
        else:
            res.x += other.x

        return res


    __radd__  = __add__


    #frac1 - frac2, frac - int
    def __sub__(self, other):  # frac1 - frac2
		
        if isinstance(other, int):
            return self.__sub__(Frac(other, 1))

        l = lcm(self.y, other.y)
        res = Frac(0, l)

        if self.y != res.y:
            res.x += res.y / self.y * self.x
        else:
            res.x += self.x

        if other.y != res.y:
            res.x -= res.y / other.y * other.x
        else:
            res.x -= other.x

        return res

    def __rsub__(self, other):  # int-frac
        if isinstance(other,int):
            return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1 * frac2
        if isinstance(self,int):
            return other.__mul__(Frac(self, 1))
        if isinstance(other, int):
            return self.__mul__(Frac(other, 1))
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __div__(self, other):  # frac1 / frac2
        if isinstance(other, int):
            return self.__div__(Frac(1,other))
        if self.y != 0:
            if other.y != 0:
                return self.__mul__(Frac(other.y, other.x))

    def __rdiv__(self, other):
        if isinstance(other,int):
            return self.__div__(Frac(other, 1))

    def frac2float(frac):  # konwersja do float
        return (float(frac.x) / float(frac.y))

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):
        return Frac((-1)*self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(frac):  # konwersja do float
        return (float(frac.x) / float(frac.y))

    def simplify(frac):
        while fractions.gcd(frac.x, frac.y) > 1:
            Gcd = fractions.gcd(frac.x, frac.y)
            frac.x = int(float(frac.x) / Gcd)
            frac.y = int(float(frac.y) / Gcd)
        return frac



# lowest common multiplier
def lcm(x, y):
    lcm = 0
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
        
  




