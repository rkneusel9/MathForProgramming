#
#  file: NumberSets.py
#
#  Multiplies any order lists representing reals,
#  complex, quaternions, octonions, and sedenions, ...
#
#  CayleyDickson code from:
#       https://www.johndcook.com/blog/2018/07/10/cayley-dickson/
#  used with permission
#
#  RTK, 20-Feb-2022
#  Last update:  20-Feb-2022
#
################################################################

import numpy as np

#
#  Base code from John Cook's site.  Will multiply any
#  number from R, C, H, O, S, and higher.  Pass the number
#  as a NumPy vector.
#
def conj(x):
        xstar = -x
        xstar[0] *= -1
        return xstar 

def CayleyDickson(x, y):
    n = len(x)

    if n == 1:
        return x*y

    m = n // 2

    a, b = x[:m], x[m:]
    c, d = y[:m], y[m:]
    z = np.zeros(n)
    z[:m] = CayleyDickson(a, c) - CayleyDickson(conj(d), b)
    z[m:] = CayleyDickson(d, a) + CayleyDickson(b, conj(c))
    return z


#
#  RTK additions
#

################################################################
#  Number
#
class Number:
    """Base implementation"""

    def __init__(self, v):
        """Constructor"""
        self.v = v
    
    def __iter__(self):
        return iter(self.v)

    def __add__(self, z):
        ans = []
        for i in range(len(self.v)):
            ans.append(self.v[i]+z.v[i])
        return Number(ans)

    def __sub__(self, z):
        ans = []
        for i in range(len(self.v)):
            ans.append(self.v[i]-z.v[i])
        return Number(ans)

    def __mul__(self, z):
        A = np.array(self.v)
        B = np.array(list(z))
        return Number(list(CayleyDickson(A,B)))

    def __neg__(self):
        ans = []
        for i in range(len(self.v)):
            ans.append(-self.v[i])
        return Number(ans)
    
    def conj(self):
        ans = [self.v[0]]
        for i in range(1,len(self.v)):
            ans.append(-self.v[i])
        return Number(ans)

    def __abs__(self):
        c = self * self.conj()
        return np.sqrt(c.v[0])

    def inv(self):
        m = self.__abs__()**2
        return Number([v/m for v in list(self.conj())])

    def __truediv__(self, z):
        zinv = np.array(list(z.conj())) / abs(z)**2
        A = np.array(self.v)
        return Number(list(CayleyDickson(A,zinv)))


################################################################
#  Quaternion
#
class Quaternion:
    """A simple quaternion class"""

    def __init__(self, a, b=None, c=None, d=None):
        """Constructor"""
        if (b == None):
            self.n = Number(a)
        else:
            self.n = Number([a,b,c,d])
    def __str__(self):
        a,b,c,d = list(self.n)
        ans = "%g%+gi%+gj%+gk" % (a,b,c,d)
        return ans
    def __repr__(self):
        return self.__str__()
    def __iter__(self):
        return iter(list(self.n))
    def __add__(self, z):
        return Quaternion(list(self.n + z.n))
    def __sub__(self, z):
        return Quaternion(list(self.n - z.n))
    def __mul__(self, z):
        return Quaternion(list(self.n * z.n))
    def __neg__(self):
        return Quaternion(list(-self.n))
    def conj(self):
        return Quaternion(list(self.n.conj()))
    def __abs__(self):
        return abs(self.n)
    def __truediv__(self, z):
        return Quaternion(list(self.n / z.n))


################################################################
#  Octonion
#
class Octonion:
    """A simple octonion class"""

    def __init__(self, a, b=None, c=None, d=None, e=None, f=None, g=None, h=None):
        """Constructor"""
        if (b == None):
            self.n = Number(a)
        else:
            self.n = Number([a,b,c,d,e,f,g,h])
    def __str__(self):
        a,b,c,d,e,f,g,h = list(self.n)
        ans = "%g,%g,%g,%g,%g,%g,%g,%g" % (a,b,c,d,e,f,g,h)
        return ans
    def __repr__(self):
        return self.__str__()
    def __iter__(self):
        return iter(list(self.n))
    def __add__(self, z):
        return Octonion(list(self.n + z.n))
    def __sub__(self, z):
        return Octonion(list(self.n - z.n))
    def __mul__(self, z):
        return Octonion(list(self.n * z.n))
    def __neg__(self):
        return Octonion(list(-self.n))
    def conj(self):
        return Octonion(list(self.n.conj()))
    def __abs__(self):
        return abs(self.n)
    def __truediv__(self, z):
        return Octonion(list(self.n / z.n))


################################################################
#  Sedenion
#
class Sedenion:
    """A simple sedenion class"""

    def __init__(self, a, b=None, c=None, d=None, e=None, f=None, g=None, h=None,
                  i=None, j=None, k=None, l=None, m=None, n=None, o=None, p=None):
        """Constructor"""
        if (b == None):
            self.n = Number(a)
        else:
            self.n = Number([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])
    def __str__(self):
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = list(self.n)
        ans = "%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g" % (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        return ans
    def __repr__(self):
        return self.__str__()
    def __iter__(self):
        return iter(list(self.n))
    def __add__(self, z):
        return Sedenion(list(self.n + z.n))
    def __sub__(self, z):
        return Sedenion(list(self.n - z.n))
    def __mul__(self, z):
        return Sedenion(list(self.n * z.n))
    def __neg__(self):
        return Sedenion(list(-self.n))
    def conj(self):
        return Sedenion(list(self.n.conj()))
    def __abs__(self):
        return abs(self.n)

