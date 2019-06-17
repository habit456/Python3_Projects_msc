class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __eq__(self, other):
        n1 = self.num * other.den
        n2 = other.num * self.den
        return n1 == n2

    def __add__(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = (self.den * other.den)
        common = self.gcd(num, den)
        return Fraction(num // common, den // common)

    def __sub__(self, other):
        num = (self.num * other.den) - (other.num * self.den)
        den = (self.den * other.den)
        common = self.gcd(num, den)
        return Fraction(num // common, den // common)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        common = self.gcd(num, den)
        return Fraction(num // common, den // common)

    def __truediv__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        common = self.gcd(num, den)
        return Fraction(num // common, den // common)

    def __lt__(self, other):
        return (self.num / self.den) < (other.num / other.den)

    def __gt__(self, other):
        return (self.num / self.den) > (other.num / other.den)

    def __le__(self, other):
        return (self.num / self.den) <= (other.num / other.den)

    def __ge__(self, other):
        return (self.num / self.den) >= (other.num / other.den)

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n


f1 = Fraction(4, 6)
f2 = Fraction(3, 6)
f3 = Fraction(2, 6)

print(f3 >= f1)
