#
#  file: dual.py
#
#  A simple dual numbers class
#
#  RTK, 16-Feb-2022
#  Last update:  16-Feb-2022
#
################################################################

from math import sin, cos, log, exp, sqrt

#
#  For automatic differentiation, x --> Dual(x,1) -- variable
#                                 c --> Dual(c,0) -- some constant
#

################################################################
#  Dual
#
class Dual:
    """Basic dual numbers"""

    def __init__(self, a,b):
        """Constructor"""
        self.a = a
        self.b = b

    def __str__(self):
        if (self.b >= 0.0):
            return "%f+%fe" % (self.a, self.b)
        else:
            return "%f-%fe" % (self.a, abs(self.b))
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, z):
        return Dual(self.a+z.a, self.b+z.b)

    def __sub__(self, z):
        return Dual(self.a-z.a, self.b-z.b)

    def __mul__(self, z):
        return Dual(self.a*z.a, self.a*z.b+self.b*z.a)

    def __truediv__(self, z):
        return Dual(self.a/z.a, (self.b*z.a-self.a*z.b)/(z.a*z.a))

    def __pow__(self, z):
        return Dual(self.a**z, z*self.b*self.a**(z-1.0))

    def sqrt(self):
        t = sqrt(self.a)
        return Dual(t, 0.5*self.b/t)

    def sin(self):
        return Dual(sin(self.a), self.b*cos(self.a))

    def cos(self):
        return Dual(cos(self.a), -self.b*sin(self.a))
    
    def tan(self):
        return self.sin() / self.cos()
    
    def exp(self):
        return Dual(exp(self.a), self.b*exp(self.a))

    def log(self):
        return Dual(log(self.a), self.b/self.a)

