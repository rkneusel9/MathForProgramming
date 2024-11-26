#
#  file:  newton.py
#
#  Newton's method to locate the zeros of a function
#
#  RTK, 02-Nov-2023
#  Last update: 03-Nov-2023
#
################################################################

import sys
import numpy as np
import matplotlib.pylab as plt

def f(x):
    return x**3 + 3*x**2 - 3*x - 10

def df(x):
    return 3*x**2 + 6*x - 3

def Newton(f, df, x=1.0, eps=1e-7):
    """Newton's method to locate a zero of a function"""
    xold = x
    x = x - f(x) / df(x)
    while (abs(x-xold) > eps):
        xold = x
        x = x - f(x) / df(x)
    return x

#  Locate the roots using different starting positions on the command line
#  Roots at x = -2.7912878, -2.0, 1.7912878
x0 = float(sys.argv[1])
root = Newton(f, df, x0)
print("Root at %0.7f" % root)

lo,hi,n = -3.4,2.2,600
x = np.linspace(lo,hi,n)
plt.plot(x,f(x), color='k')
plt.plot([lo,hi],[0,0], color='k', linewidth=0.5)
plt.plot([0,0],[min(f(x)),max(f(x))], color='k', linewidth=0.5)
plt.plot([x0,x0],[0,0], marker='s', fillstyle='none', color='k')
plt.plot([root,root],[0,0], marker='o', fillstyle='none', color='k')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("newton.eps", dpi=300)
plt.show()

