class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)
    def inverse(self):
        return Fraction(self.denom,self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a+b
print("fraction show :",c)
print("inverse of the b  = ", b.inverse())