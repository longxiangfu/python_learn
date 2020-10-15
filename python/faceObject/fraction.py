"""
类特殊方法，内部调用了内置函数
"""
from fractions import Fraction


class Fraction1:
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + "/" + str(self.denom)

    __repr__ = __str__


f = Fraction1(2, 3)
print(f)

m, n = Fraction(1, 6), Fraction(3, 6)
print(m)
print(n)
s = m + n
print(s)
